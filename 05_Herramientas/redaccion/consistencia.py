#!/usr/bin/env python3
"""Contraste de fechas e importes de los documentos del corpus con PARAMETROS, especificaciones e índice."""
import glob, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = '/Users/germanjaraba/Proyectos/Revista Carelis'
MES = 'ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic'
fuentes = [os.path.join(AQUI, 'PARAMETROS.md'), os.path.join(AQUI, 'referencias', '_cal_tabla.md'), os.path.join(AQUI, 'referencias', 'RECTOR.txt'),
           os.path.join(AQUI, 'referencias', '_indice_sec.txt')] + glob.glob(os.path.join(AQUI, 'specs', '*.md'))
ref = '\n'.join(open(f, encoding='utf-8').read() for f in fuentes)
fechas_ok = set(re.findall(rf'\b\d{{2}}-(?:{MES})-\d{{4}}\b', ref))
# fechas sin año en referencias: dd-mmm → se aceptan con 2026 o 2027
for d, m in re.findall(rf'\b(\d{{2}})-({MES})\b(?!-\d)', ref):
    fechas_ok |= {f'{d}-{m}-2026', f'{d}-{m}-2027'}
nums_ok = {n.replace('.', '') for n in re.findall(r'\b\d{1,3}(?:\.\d{3})+\b|\b\d+\b', ref)}
docs = sorted(glob.glob(os.path.join(RAIZ, '02_Corpus_Documental', '**', '*_v*.md'), recursive=True))
sel = [a for a in sys.argv[1:]]
for d in docs:
    cod = os.path.basename(d).split('_')[0]
    if sel and cod not in sel: continue
    t = open(d, encoding='utf-8').read()
    fx = sorted({f for f in re.findall(rf'\b\d{{2}}-(?:{MES})-\d{{4}}\b', t)} - fechas_ok)
    imp = sorted({n for n in re.findall(r'\b(\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?\s?USD\b', t) if n.replace('.', '') not in nums_ok},
                 key=lambda x: int(x.replace('.', '')))
    print(f'{cod}: fechas no previstas {fx or "ninguna"} · importes no previstos {imp or "ninguno"}')
