#!/usr/bin/env python3
"""Hoja comparativa de las tres direcciones: columnas A, B, C; filas apertura, revista, pliego abierto y ciclo."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = os.path.join(BASE, 'capturas')
COLS = [('A', 'A · Escenario (ruleta: escenario de cifras)'), ('B', 'B · Revista-objeto (referencia: WIRED)'), ('C', 'C · Sistema (mejor diseñador)')]
FILAS = [('p1', 'Apertura'), ('p2', 'Revista · portada'), ('p2b', 'Revista · pliego 02-03'), ('p3', 'Ciclo y compuertas')]
W, H, M, CAB, ROT = 720, 450, 28, 64, 250
def fuente(t):
    for f in ('/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/System/Library/Fonts/Helvetica.ttc'):
        try: return ImageFont.truetype(f, t)
        except Exception: pass
    return ImageFont.load_default()
hoja = Image.new('RGB', (ROT + len(COLS) * (W + M) + M, CAB + len(FILAS) * (H + M) + M), '#E9EBEF')
d = ImageDraw.Draw(hoja)
for j, (k, nombre) in enumerate(COLS):
    d.text((ROT + M + j * (W + M), 22), nombre, fill='#0D0E12', font=fuente(24))
for i, (f, nombre) in enumerate(FILAS):
    y = CAB + M + i * (H + M)
    d.text((M, y + H // 2 - 12), nombre, fill='#5B6472', font=fuente(20))
    for j, (k, _) in enumerate(COLS):
        x = ROT + M + j * (W + M)
        ruta = os.path.join(CAP, f'{k}_{f}.png')
        if os.path.exists(ruta):
            im = Image.open(ruta).convert('RGB'); im.thumbnail((W, H))
            hoja.paste(im, (x + (W - im.width) // 2, y + (H - im.height) // 2))
        else:
            d.rectangle([x, y, x + W, y + H], outline='#5B6472'); d.text((x + 20, y + 20), 'Sin captura', fill='#5B6472', font=fuente(18))
salida = os.path.join(CAP, 'comparativa_direcciones.png'); hoja.save(salida, optimize=True); print(salida)
