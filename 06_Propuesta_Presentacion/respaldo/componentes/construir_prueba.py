#!/usr/bin/env python3
"""Banco de prueba del libro: revista.css + revista-paginas.css + libro.css + libro.js + fragmento de páginas."""
import os
d = os.path.dirname(os.path.abspath(__file__))
leer = lambda n: open(os.path.join(d, n), encoding='utf-8').read()
css = leer('revista.css') + leer('revista-paginas.css') + leer('libro.css')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Prueba del libro</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400..900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}
body{{margin:0;min-height:100vh;display:grid;place-items:center;background:radial-gradient(120% 90% at 50% 30%,#E9EBEF 0,#C9CCD2 70%);font-family:Archivo}}
.mesa{{width:min(92vw,1300px)}} @media (max-width:700px){{.mesa{{width:calc(100vw - 32px)}}}}
.estado{{text-align:center;font:500 14px Archivo;margin-top:18px;color:#0D0E12}}
</style></head><body><div class="mesa"><div id="libro" class="revista"></div><p class="estado" id="estado"></p></div>
<div id="fuente" hidden>{leer('revista-fragmento.html')}</div>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/Draggable.min.js"></script>
<script>{leer('libro.js')}</script>
<script>
gsap.registerPlugin(Draggable);
const nombres=['C1 · Portada','C2-01 · Doble premium','02-03 · Sumario y créditos','04-05 · Pulso Techno','08-09 · Bajo el Lente','16-17 · Reportaje Central','20-21 · En Primera Fila','28-29 · ADN Gamer','36-37 · Espacio Business','40-41 · Conexión en Vivo','44-45 · Ruta Inteligente','48-C3 · Última Página y zona NFC','C4 · Contraportada'];
const q=new URLSearchParams(location.search), una=q.has('una');
const pags=[...document.querySelectorAll('#fuente .pg')];
const L=Libro.crear(document.getElementById('libro'),pags,{{nombres:una?null:nombres,unaPagina:una,alCambiar:(k)=>document.getElementById('estado').textContent=una?('Página '+(k+1)+' de '+pags.length):nombres[k]}});
if(q.has('pliego')) L.ir(+q.get('pliego'),true);
if(q.has('reticula')) document.getElementById('libro').classList.add('reticula');
if(q.has('giro')) {{ L.ir(+q.get('giro')-1,true); setTimeout(()=>{{ L.siguiente(); setTimeout(()=>gsap.globalTimeline.pause(),420); }},300); }}
</script></body></html>'''
open(os.path.join(d, 'libro-prueba.html'), 'w', encoding='utf-8').write(html)
print('banco de prueba listo')
