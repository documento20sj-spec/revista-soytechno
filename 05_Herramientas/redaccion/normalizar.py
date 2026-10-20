#!/usr/bin/env python3
"""Envuelve en acentos graves las referencias a códigos documentales fuera de tramos de código."""
import re, sys
PAT = re.compile(r'(?<![\w`-])((?:DIR|IND|MAN|GUI|PRO|KIT|REG|CAL|PLA|PLI|EXP)-(?:ED|ID|PP|PR|CO|LG|RP|EV|NW|CR|EX|FI|OR|MD|CM|DI|PV)(?:-ST-\d{4}-\d{2})?|DOC-E(?:\d\d)?-\d\d|PLT-DOC-\d\d)(?![\w-])')
def proc(linea):
    partes = linea.split('`')
    for i in range(0, len(partes), 2):
        partes[i] = PAT.sub(lambda m: '`' + m.group(1) + '`', partes[i])
    return '`'.join(partes)
for ruta in sys.argv[1:]:
    lineas = open(ruta, encoding='utf-8').read().split('\n')
    h2 = next(i for i, l in enumerate(lineas) if l.startswith('## '))
    n = 0
    for i in range(h2, len(lineas)):
        nueva = proc(lineas[i])
        if nueva != lineas[i]:
            n += nueva.count('`') - lineas[i].count('`'); lineas[i] = nueva
    open(ruta, 'w', encoding='utf-8').write('\n'.join(lineas))
    print(f'{ruta.split("/")[-1][:17]}: {n // 2} referencias normalizadas')
