import json
import glob
import os

notebooks = glob.glob('*.ipynb')
for nb_path in notebooks:
    print(f"=== Notebook: {nb_path} ===")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    cells = nb.get('cells', [])
    print(f"Total cells: {len(cells)}")
    errors = []
    widgets_in_outputs = 0
    mulai_selesai = 0
    images_count = 0
    for idx, c in enumerate(cells):
        src = ''.join(c.get('source', []))
        if 'MULAI CODE' in src or 'SELESAI CODE' in src:
            mulai_selesai += 1
        for out in c.get('outputs', []):
            if out.get('output_type') == 'error':
                errors.append((idx, out.get('ename'), out.get('evalue')))
            data = out.get('data', {})
            if 'application/vnd.jupyter.widget-view+json' in data:
                widgets_in_outputs += 1
            if 'image/png' in data or 'image/jpeg' in data:
                images_count += 1
    has_nb_widgets = 'widgets' in nb.get('metadata', {})
    widget_keys_count = len(nb.get('metadata', {}).get('widgets', {}).get('application/vnd.jupyter.widget-state+json', {}).get('state', {})) if has_nb_widgets else 0
    print(f"Errors: {len(errors)}")
    for e in errors:
        print(f"  Cell {e[0]}: {e[1]} - {e[2]}")
    print(f"Widget views in outputs: {widgets_in_outputs}")
    print(f"Notebook metadata widgets count: {widget_keys_count}")
    print(f"Images count: {images_count}")
    print(f"Cells with MULAI/SELESAI code: {mulai_selesai}")
    print()
