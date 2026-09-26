"""Execute all default notebook lessons, failing on any unexpected cell error."""
from pathlib import Path
import argparse, json, sys
import nbformat
from nbclient import NotebookClient
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--kernel',default='python3');args=p.parse_args()
target=ROOT/'runs';target.mkdir(exist_ok=True)
results=[]
for path in sorted(ROOT.glob('0*/*.ipynb')):
    notebook=nbformat.read(path,as_version=4)
    nbformat.validate(notebook)
    NotebookClient(notebook,timeout=300,kernel_name=args.kernel,resources={'metadata':{'path':str(path.parent)}}).execute()
    nbformat.write(notebook,target/path.name)
    results.append({'notebook':str(path.relative_to(ROOT)),'status':'passed','external_labs':'disabled'})
    print('PASS',path.name,flush=True)
(target/'validation.json').write_text(json.dumps(results,indent=2))
print(f'{len(results)} notebooks passed. External downloads/inference are not validated by this check.')
