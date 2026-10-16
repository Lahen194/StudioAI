import json
import os

with open('Pipeline_submission_BFGAI_Fakhira_Lahen_Siregar_(4)_(1)_(1).ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("Cells summary:")
for i, c in enumerate(nb['cells']):
    ctype = c.get('cell_type')
    outs = c.get('outputs', [])
    out_types = []
    has_widget = False
    has_image = False
    has_text = False
    has_error = False
    for o in outs:
        otype = o.get('output_type')
        if otype == 'error':
            has_error = True
        data = o.get('data', {})
        if 'application/vnd.jupyter.widget-view+json' in data:
            has_widget = True
        if 'image/png' in data or 'image/jpeg' in data:
            has_image = True
        if 'text/plain' in data or 'text/html' in data or otype == 'stream':
            has_text = True
    
    tags = []
    if has_error: tags.append("ERROR")
    if has_widget: tags.append(f"WIDGET({sum(1 for o in outs if 'application/vnd.jupyter.widget-view+json' in o.get('data', {}))})")
    if has_image: tags.append("IMAGE")
    if has_text: tags.append("TEXT/STREAM")
    if outs and not tags: tags.append("OTHER")
    
    if outs or ctype == 'code':
        print(f"Cell {i:2d} [{ctype}]: {', '.join(tags) if tags else 'NO OUTPUT'}")
