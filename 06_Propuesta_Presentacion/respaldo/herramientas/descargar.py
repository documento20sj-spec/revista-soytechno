#!/usr/bin/env python3
"""Descarga los recursos listados en _fotos/descargas-propuestas.md a presentacion/descargas/ (solo con permiso del usuario).
Uso: python3 -I herramientas/descargar.py   ·   cada tipo en su carpeta: fotos/, fuentes/, gsap/."""
import os, re, sys, urllib.request
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(BASE, 'descargas')
LISTA = open(os.path.join(BASE, '_fotos', 'descargas-propuestas.md'), encoding='utf-8').read()
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'}
def bajar(url, carpeta, nombre):
    os.makedirs(os.path.join(DEST, carpeta), exist_ok=True)
    ruta = os.path.join(DEST, carpeta, nombre)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r, open(ruta, 'wb') as f:
        f.write(r.read())
    print(f'{os.path.getsize(ruta) / 1024:7.0f} KB  {carpeta}/{nombre}')
for idf, url in re.findall(r'\| \w+\.webp \| (https://images\.unsplash\.com/photo-([0-9a-f-]+)\?[^ |]+) \|', LISTA) and \
        [(m[1], m[0]) for m in re.findall(r'\| \w+\.webp \| (https://images\.unsplash\.com/photo-([0-9a-f-]+)\?[^ |]+) \|', LISTA)]:
    bajar(url, 'fotos', idf + '.webp')
for nombre, url in re.findall(r'\| (\S+\.woff2) \| (https://fonts\.gstatic\.com/\S+) \|', LISTA):
    bajar(url, 'fuentes', nombre)
for js in ['gsap.min.js', 'ScrollTrigger.min.js', 'SplitText.min.js', 'Draggable.min.js', 'CustomEase.min.js']:
    bajar(f'https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/{js}', 'gsap', js)
