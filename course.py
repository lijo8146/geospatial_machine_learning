"""Small, inspectable teaching utilities. Synthetic fixtures are never observations."""
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'data' / 'generated'
OUT.mkdir(parents=True, exist_ok=True)

def points(n=240, seed=42):
    rng = np.random.default_rng(seed)
    lon = rng.uniform(-105.32, -105.12, n)
    lat = rng.uniform(39.88, 40.08, n)
    # A deliberately artificial surface, not a fire perimeter or land-cover map.
    score = np.sin((lon + 105.32)*65) + np.cos((lat-39.88)*65)
    label = (score + rng.normal(0, .35, n) > 0).astype(int)
    block = ((lon+105.32)//.05).astype(int)*4 + ((lat-39.88)//.05).astype(int)
    return pd.DataFrame(dict(point_id=[f'p{i:04}' for i in range(n)],
        longitude=lon, latitude=lat, label=label, block=block, signal=score))

def embeddings(frame, dimensions=64, seed=12):
    rng = np.random.default_rng(seed)
    latent = np.column_stack([frame.signal, np.sin(frame.latitude*10), np.cos(frame.longitude*10)])
    x = latent @ rng.normal(size=(3, dimensions)) + rng.normal(0, .5, (len(frame), dimensions))
    return x / np.linalg.norm(x, axis=1, keepdims=True)

def evaluate(frame, x):
    from sklearn.model_selection import GroupShuffleSplit
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.dummy import DummyClassifier
    from sklearn.metrics import balanced_accuracy_score, confusion_matrix
    x = np.asarray(x)
    if x.ndim != 2 or len(x) != len(frame) or not np.isfinite(x).all():
        raise ValueError('Expected one finite embedding row per labeled point.')
    if frame.point_id.duplicated().any():
        raise ValueError('point_id must be unique.')
    train, test = next(GroupShuffleSplit(n_splits=1, test_size=.25, random_state=42).split(x, frame.label, frame.block))
    if set(frame.iloc[train].label) != set(frame.label) or set(frame.iloc[test].label) != set(frame.label):
        raise ValueError('Every class must occur in train and test; collect more spatially distributed labels.')
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42))
    model.fit(x[train], frame.label.iloc[train])
    pred = model.predict(x[test])
    dummy = DummyClassifier(strategy='most_frequent').fit(x[train], frame.label.iloc[train])
    metrics = dict(balanced_accuracy=float(balanced_accuracy_score(frame.label.iloc[test], pred)),
        baseline=float(balanced_accuracy_score(frame.label.iloc[test], dummy.predict(x[test]))),
        train_count=len(train), test_count=len(test))
    return model, metrics, confusion_matrix(frame.label.iloc[test], pred), train, test

def h3_summary(frame, resolution):
    import h3
    f = frame.copy()
    if not f.latitude.between(-90,90).all() or not f.longitude.between(-180,180).all():
        raise ValueError('Expected WGS84 longitude/latitude in degrees.')
    f['hex'] = [h3.latlng_to_cell(lat, lon, resolution) for lat,lon in zip(f.latitude,f.longitude)]
    return f.groupby('hex',as_index=False).agg(mean_probability=('probability','mean'), count=('probability','size'))

def raster_fixture():
    import rasterio
    from rasterio.transform import from_origin
    path = OUT / 'synthetic_rgb.tif'
    rng=np.random.default_rng(42)
    image=rng.integers(1,10000,(3,256,256),dtype=np.uint16)
    with rasterio.open(path,'w',driver='GTiff',height=256,width=256,count=3,
            dtype='uint16',crs='EPSG:32613',transform=from_origin(475000,4430000,10,10),nodata=0) as dst:
        dst.write(image)
        dst.update_tags(source='SYNTHETIC teaching fixture; no scientific interpretation')
    return path
