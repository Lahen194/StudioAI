import json

with open('Pipeline_submission_BFGAI_Fakhira_Lahen_Siregar_(4)_(1)_(1).ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("=== Scanning Pipeline_submission_BFGAI_Fakhira_Lahen_Siregar_(4)_(1)_(1).ipynb ===")
for i, c in enumerate(nb['cells']):
    src = ''.join(c.get('source', []))
    lines = [l.strip() for l in src.splitlines() if any(k in l.lower() for k in ['mulai', 'selesai', 'todo', 'kriteria'])]
    if lines:
        print(f"Cell {i} ({c.get('cell_type')}): {lines}")
