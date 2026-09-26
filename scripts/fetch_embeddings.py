"""Acquire real labeled-point embeddings. Never substitute synthetic data on failure."""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
import pandas as pd
from course import ROOT

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',choices=['alphaearth','tessera'])
    p.add_argument('--labels',type=Path,required=True)
    p.add_argument('--year',type=int,required=True)
    p.add_argument('--project',help='Registered Earth Engine Cloud project')
    args=p.parse_args()
    f=pd.read_csv(args.labels,dtype={'point_id':str})
    required={'point_id','longitude','latitude','label','block','year','label_source'}
    if not required.issubset(f.columns): raise ValueError(f'Required columns: {sorted(required)}')
    if f.empty or f.point_id.duplicated().any() or f[list(required)].isna().any().any():
        raise ValueError('Labels must be nonempty, complete and have unique IDs.')
    if not f.year.eq(args.year).all(): raise ValueError('Label year must match requested embedding year.')
    if not f.longitude.between(-180,180).all() or not f.latitude.between(-90,90).all():
        raise ValueError('Invalid WGS84 coordinates.')
    if args.source=='alphaearth':
        if not args.project: p.error('--project is required for AlphaEarth')
        import ee
        ee.Initialize(project=args.project)
        bands=[f'A{i:02}' for i in range(64)]
        features=ee.FeatureCollection([ee.Feature(ee.Geometry.Point([r.longitude,r.latitude]),{'point_id':r.point_id}) for r in f.itertuples()])
        collection=ee.ImageCollection('GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL').filterDate(f'{args.year}-01-01',f'{args.year+1}-01-01').filterBounds(features.geometry())
        if collection.size().getInfo()==0: raise ValueError('No AlphaEarth coverage for requested year/locations.')
        # Small-label exercise only: use an EE export for large collections.
        sampled=collection.mosaic().select(bands).sampleRegions(collection=features,properties=['point_id'],scale=10,geometries=False).getInfo()
        by_id={r['properties']['point_id']:r['properties'] for r in sampled['features']}
        x=np.array([[by_id.get(pid,{}).get(b,np.nan) for b in bands] for pid in f.point_id])
    else:
        from geotessera import GeoTessera
        from pyproj import Transformer
        from rasterio.transform import rowcol
        gt=GeoTessera()
        bounds=(float(f.longitude.min()-.0001),float(f.latitude.min()-.0001),float(f.longitude.max()+.0001),float(f.latitude.max()+.0001))
        blocks=gt.registry.load_blocks_for_region(bounds=bounds,year=args.year)
        if not len(blocks): raise ValueError('No TESSERA coverage for this area/year.')
        x=np.full((len(f),128),np.nan)
        for year,lon,lat,array,crs,transform in gt.fetch_embeddings(blocks):
            if array.ndim!=3 or array.shape[2]!=128: raise ValueError('Expected H x W x 128 TESSERA v1 embeddings.')
            tx,ty=Transformer.from_crs(4326,crs,always_xy=True).transform(f.longitude.to_numpy(),f.latitude.to_numpy())
            rr,cc=rowcol(transform,tx,ty);rr=np.asarray(rr);cc=np.asarray(cc)
            valid=(rr>=0)&(rr<array.shape[0])&(cc>=0)&(cc<array.shape[1])
            values=array[rr[valid],cc[valid]].astype(float)
            values[np.linalg.norm(values,axis=1)==0]=np.nan
            x[valid]=values
    target=ROOT/'data/real';target.mkdir(parents=True,exist_ok=True)
    result=f.copy()
    for i in range(x.shape[1]): result[f'e{i:03}']=x[:,i]
    result.to_csv(target/f'{args.source}.csv',index=False)
    import importlib.metadata as metadata
    package='earthengine-api' if args.source=='alphaearth' else 'geotessera'
    provenance=dict(source=args.source,year=args.year,labels=str(args.labels.resolve()),package=package,version=metadata.version(package),rows=len(f),finite_rows=int(np.isfinite(x).all(axis=1).sum()))
    (target/f'{args.source}.metadata.json').write_text(json.dumps(provenance,indent=2))
    print(provenance)
if __name__=='__main__': main()
