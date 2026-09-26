"""Evaluate real sources on the identical finite cohort and spatial split."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
import pandas as pd
from course import ROOT,evaluate

def main():
    folder=ROOT/'data/real'
    a=pd.read_csv(folder/'alphaearth.csv',dtype={'point_id':str}).set_index('point_id',verify_integrity=True)
    b=pd.read_csv(folder/'tessera.csv',dtype={'point_id':str}).set_index('point_id',verify_integrity=True)
    print('Source rows:', {'alphaearth': len(a), 'tessera': len(b)})
    ids=a.index.intersection(b.index,sort=False)
    print('IDs absent from other source:', {'alphaearth': len(a.index.difference(b.index)), 'tessera': len(b.index.difference(a.index))})
    a,b=a.loc[ids],b.loc[ids]
    for col in ['longitude','latitude','label','block','year','label_source']:
        if not a[col].equals(b[col]): raise ValueError(f'Mismatched {col}; compare the same observations.')
    ca=[f'e{i:03}' for i in range(64)];cb=[f'e{i:03}' for i in range(128)]
    good=np.isfinite(a[ca]).all(axis=1)&np.isfinite(b[cb]).all(axis=1)
    print('Common IDs:',len(ids),'Excluded missing vectors:',int((~good).sum()))
    frame=a.loc[good].reset_index()
    rows=[]
    for name,table,columns in [('alphaearth',a,ca),('tessera',b,cb)]:
        model,metrics,confusion,train,test=evaluate(frame,table.loc[good,columns].to_numpy())
        rows.append(dict(source=name,**metrics));print(name,confusion)
        prediction=frame[['point_id','longitude','latitude','label','block','year']].copy()
        prediction['split']=np.where(prediction.index.isin(test),'test','train')
        prediction['prediction']=model.predict(table.loc[good,columns].to_numpy())
        if 1 in model.classes_:
            prediction['probability']=model.predict_proba(table.loc[good,columns].to_numpy())[:,list(model.classes_).index(1)]
        prediction.to_csv(folder/f'{name}_predictions.csv',index=False)
    pd.DataFrame(rows).to_csv(folder/'comparison.csv',index=False)
    print(pd.DataFrame(rows))
if __name__=='__main__': main()
