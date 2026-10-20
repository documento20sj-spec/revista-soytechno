#!/usr/bin/env python3
"""Constructor de los documentos de dirección del Proyecto Editorial Revista Corporativa SoyTechno.

Dos familias de documentos:

1. Documentos de dirección (cuerpos HTML en `05_Herramientas/src/`), con HTML y PDF:
     00_Indice_Documental/IND-ED-ST-2026-01_Indice_Maestro_v1.html / .pdf
     01_Documento_Rector/DIR-ED-ST-2026-01_Documento_Rector_v1.html / .pdf   (5 páginas obligatorias)
2. Documentos del corpus (Bloques I a III), redactados en Markdown dentro de su carpeta de
   `02_Corpus_Documental/`: el .md es la fuente oficial y se genera a su lado el .html de lectura.

Uso:
    python3 05_Herramientas/construir.py                     # todo: dirección (HTML + PDF) y corpus (HTML)
    python3 05_Herramientas/construir.py --md                # solo los documentos del corpus
    python3 05_Herramientas/construir.py --solo-html         # sin PDF en los documentos de dirección
    python3 05_Herramientas/construir.py MAN-ID-ST-2026-01   # un documento por código
    python3 05_Herramientas/construir.py ruta/al/archivo.md  # un documento por ruta

Requisitos: Python 3 con el paquete markdown, Google Chrome para los PDF (modo headless, sin red)
y PyMuPDF opcional para verificar el número de páginas.
"""
import base64
import glob
import html as htmlmod
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CORPUS = os.path.join(RAIZ, '02_Corpus_Documental')

FUENTES = [
    ('Lexend', 'normal', '100 900', 'Lexend-variable.woff2'),
    ('Source Sans 3', 'normal', '200 900', 'SourceSans3-variable.woff2'),
    ('Source Sans 3', 'italic', '200 900', 'SourceSans3-italic-variable.woff2'),
    ('JetBrains Mono', 'normal', '100 800', 'JetBrainsMono-variable.woff2'),
]

DOCUMENTOS = [
    dict(
        codigo='IND-ED-ST-2026-01',
        src='indice_maestro.body.html',
        out='00_Indice_Documental/IND-ED-ST-2026-01_Indice_Maestro_v1',
        title='Índice Maestro y Catálogo de Documentos · Revista Corporativa SoyTechno',
        header='Índice Maestro · Revista Corporativa SoyTechno',
        code='IND-ED-ST-2026-01 · v1.0',
        footer='Directriz de gestión documental · Uso interno',
        estilo='lectura',   # una columna, lectura en pantalla y teléfono
        fs=9.5,
        paginas=None,
    ),
    dict(
        codigo='DIR-ED-ST-2026-01',
        src='documento_rector.body.html',
        out='01_Documento_Rector/DIR-ED-ST-2026-01_Documento_Rector_v1',
        title='Documento Rector · Revista Corporativa SoyTechno',
        header='Documento Rector · Revista Corporativa SoyTechno',
        code='DIR-ED-ST-2026-01 · v1.0',
        footer='Directriz estratégica y operativa · Uso interno',
        fs=7.9,      # cuerpo de impresión (pt); controla la extensión de cinco páginas
        paginas=5,   # extensión obligatoria: una unidad documental por página
    ),
]

CSS = r"""
:root{
  --ink:#0F172A; --ink-2:#1E293B; --muted:#475569; --line:#E2E8F0; --line-2:#CBD5E1;
  --bg:#FFFFFF; --bg-2:#F8FAFC; --bg-3:#F1F5F9; --accent:#2563EB; --accent-ink:#1D4ED8; --accent-bg:#EFF6FF; --carbon:#0D0E12;
  --f-head:"Lexend","Avenir Next","Helvetica Neue",Arial,sans-serif;
  --f-body:"Source Sans 3","Avenir Next","Helvetica Neue",Arial,sans-serif;
  --f-mono:"JetBrains Mono","SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{font-size:10pt;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:var(--f-body);color:var(--ink);line-height:1.3;background:var(--bg);font-variant-numeric:tabular-nums}
h1,h2,h3{font-family:var(--f-head);color:var(--ink);margin:0;line-height:1.15;break-after:avoid}
p{margin:0 0 2.6pt}
ul{margin:0 0 3pt;padding-left:8pt;list-style:none}
li{margin:0 0 1.3pt;position:relative}
ul > li::before{content:"";position:absolute;left:-6.5pt;top:.5em;width:2.8pt;height:2.8pt;border-radius:50%;background:var(--accent)}
b,strong{font-weight:600}
em{font-style:italic}
.mono{font-family:var(--f-mono);font-size:.92em}
.small{font-size:.86em;color:var(--muted);margin-top:1pt}
/* Cabecera del documento */
.doc-cab{border-bottom:1.4pt solid var(--ink);padding-bottom:4pt;margin-bottom:5pt}
.doc-top{display:flex;justify-content:space-between;font-family:var(--f-mono);font-size:.8em;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:3pt}
.doc-cab h1{font-size:1.95em;font-weight:600;letter-spacing:-.012em;margin:0 0 4pt}
.doc-meta{display:grid;grid-template-columns:repeat(5,1fr);gap:3pt 8pt;border-top:.6pt solid var(--line-2);padding-top:3pt;margin-bottom:3pt}
.doc-meta div{font-size:.94em}
.doc-meta b{display:block;font-family:var(--f-head);font-size:.74em;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.doc-obj{font-size:.9em;color:var(--ink-2);margin:0}
/* Unidades */
.unidad + .unidad{break-before:page;page-break-before:always}
h2{display:flex;align-items:center;gap:6pt;font-size:1.5em;font-weight:600;letter-spacing:-.006em;padding-bottom:3pt;border-bottom:1.4pt solid var(--ink);margin:0 0 3pt}
h2 .n{font-family:var(--f-mono);font-size:.5em;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--accent);padding:2pt 5pt;border-radius:2pt}
h3{font-size:1.06em;font-weight:600;margin:4pt 0 1.6pt;color:var(--ink)}
h3 .num{color:var(--accent);margin-right:4pt}
/* Retículas */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:0 10pt}
.g2 > div,.g-roles > div,.g-ciclo > div{min-width:0}
.g-roles{display:grid;grid-template-columns:1.08fr 1fr;gap:0 10pt}
.g-ciclo{display:grid;grid-template-columns:1.45fr 1fr;gap:0 10pt;align-items:start}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:5pt;margin:1pt 0 2pt}
.card{border:.6pt solid var(--line-2);border-top:2pt solid var(--accent);border-radius:2pt;padding:3pt 5pt;font-size:.9em;background:var(--bg-2)}
.card b{display:block;font-family:var(--f-head);font-size:1em;font-weight:600;margin-bottom:1.5pt}
ul.cols2{columns:2;column-gap:10pt}
ul.cols2 li{break-inside:avoid}
/* Índice maestro: estados, fichas, matrices y mapas */
.chip{display:inline-block;font-family:var(--f-head);font-size:.74em;font-weight:600;line-height:1;padding:2pt 5pt;border-radius:7pt;white-space:nowrap;vertical-align:middle}
.chip.emi{background:#DBEAFE;color:#1E3A8A}.chip.vig{background:#DCFCE7;color:#166534}.chip.pend{background:#FEF3C7;color:#92400E}
.chip.rec{background:#EDE9FE;color:#5B21B6}.chip.ref{background:#F1F5F9;color:#334155}.chip.par{background:#FFEDD5;color:#9A3412}
.sev{display:inline-block;font-family:var(--f-head);font-size:.74em;font-weight:600;line-height:1;padding:2pt 5pt;border-radius:7pt;white-space:nowrap}
.sev-a{background:#FFE4E6;color:#9F1239}.sev-m{background:#FEF3C7;color:#92400E}.sev-b{background:#DCFCE7;color:#166534}
.ficha{border:.6pt solid var(--line-2);border-left:2.6pt solid var(--accent);border-radius:2pt;padding:3.5pt 7pt 3pt;margin:0 0 4pt;background:#fff;break-inside:avoid;page-break-inside:avoid}
.ficha.rec{border-left-color:#7C3AED}
.ficha .fh{display:flex;align-items:baseline;gap:6pt;margin-bottom:1pt}
.ficha .fh .n{font-family:var(--f-mono);color:var(--muted);font-size:.86em}
.ficha .fh .cod{font-family:var(--f-mono);font-weight:500;color:var(--accent-ink);white-space:nowrap}
.ficha .fh .tit{font-family:var(--f-head);font-weight:600;flex:1}
.ficha .meta{font-size:.86em;color:var(--muted);margin:0 0 1.6pt}
.ficha .meta b{color:var(--ink-2);font-weight:600}
.ficha p{margin:0 0 1.6pt}
.ficha .comp{background:var(--accent-bg);border-radius:2pt;padding:1.8pt 5pt;margin-top:1.8pt}
.ficha .comp b{color:var(--accent-ink)}
.fig{break-inside:avoid;page-break-inside:avoid;margin:2pt 0 5pt}
.fig svg{display:block;width:100%;height:auto}
.fig .cap{font-size:.8em;color:var(--muted);margin-top:2pt}
.mp-box{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:.8}.mp-blk{fill:#F8FAFC;stroke:#94A3B8;stroke-width:.8}
.mp-rec{fill:#FFFFFF;stroke:#7C3AED;stroke-width:.9;stroke-dasharray:4 3}.mp-dark{fill:#0F172A}
.mp-hdr{fill:#2563EB}.mp-hdr-rec{fill:#7C3AED}.mp-hdr-ink{fill:#1E293B}
.mp-t{font-family:"Lexend",sans-serif;font-size:10px;font-weight:600;fill:#0F172A}
.mp-tw{font-family:"Lexend",sans-serif;font-size:10px;font-weight:600;fill:#FFFFFF}
.mp-ts{font-family:"Lexend",sans-serif;font-size:8.6px;font-weight:600;fill:#0F172A}
.mp-s{font-family:"Source Sans 3",sans-serif;font-size:8.8px;fill:#334155}
.mp-sw{font-family:"Source Sans 3",sans-serif;font-size:8.8px;fill:#CBD5E1}
.mp-c{font-family:"JetBrains Mono",monospace;font-size:8.2px;fill:#1D4ED8}
.mp-cs{font-family:"JetBrains Mono",monospace;font-size:7.4px;fill:#1D4ED8}
.mp-cw{font-family:"JetBrains Mono",monospace;font-size:9px;font-weight:500;fill:#FFFFFF}
.mp-l{font-family:"Source Sans 3",sans-serif;font-size:8px;font-style:italic;fill:#64748B}
.mp-a{stroke:#64748B;stroke-width:1;fill:none}
.mp-grid{stroke:#E2E8F0;stroke-width:.6}.mp-gate{stroke:#94A3B8;stroke-width:.7;stroke-dasharray:2 2}.mp-diad{stroke:#2563EB;stroke-width:1.4}
.mp-bar{fill:#BFDBFE;stroke:#60A5FA;stroke-width:.5}.mp-ext{fill:#EEF2FF;stroke:#A5B4FC;stroke-width:.5;stroke-dasharray:2 1.5}
.mp-due{fill:#0F172A}.mp-pausa{fill:#FEF3C7;opacity:.75}.mp-band{fill:#F1F5F9}
table.mx th,table.mx td{padding:1.2pt 1.6pt}
table.mx td.k{text-align:center;font-family:var(--f-mono);font-size:.8em}
table.mx td.kE{background:#DBEAFE;color:#1E3A8A}table.mx td.kG{background:var(--ink);color:#FFFFFF;font-weight:600}
table.mx td.kU{background:#F1F5F9;color:#64748B}table.mx td.kI{background:#FEF3C7;color:#92400E}
tr.grupo td{background:var(--bg-2);font-family:var(--f-head);font-weight:600;font-size:.88em;color:var(--ink-2);padding-top:2.4pt}
tr.nuevo td:first-child{box-shadow:inset 2.4pt 0 0 #7C3AED}
.nv{color:#7C3AED;font-weight:600}
/* Árbol de carpetas */
.nw{white-space:nowrap}
.arbol{font-family:var(--f-mono);font-size:.8em;line-height:1.38;white-space:pre;background:var(--bg-2);border:.6pt solid var(--line-2);border-radius:2pt;padding:5pt 7pt;margin:2pt 0 4pt;color:var(--ink-2)}
.arbol b{color:var(--ink);font-weight:500}
.arbol i{font-style:normal;color:var(--muted)}
.sec + .sec{margin-top:6pt}
/* Tablas */
thead{display:table-header-group}
tr{break-inside:avoid;page-break-inside:avoid}
table{width:100%;border-collapse:collapse;font-size:.89em;line-height:1.22;margin:1pt 0 3pt}
th{background:var(--bg-3);text-align:left;font-family:var(--f-head);font-weight:600;font-size:.88em;color:var(--ink-2);border-bottom:.8pt solid var(--line-2);padding:2pt 3pt;vertical-align:bottom}
td{border-bottom:.4pt solid var(--line);padding:1.4pt 3pt;vertical-align:top}
td:first-child{font-weight:600;color:var(--ink-2)}
table.t-def td:first-child{width:30%}
table.plain td:first-child{font-weight:400;color:var(--ink)}
table.t-tl td:first-child{width:14%}
.c{text-align:center}
table.raci td{padding:1.5pt 2pt}
table.raci th.c,table.raci td.c{width:6.4%}
table.raci td.kA{background:#DBEAFE;color:#1E3A8A;font-weight:600}
table.raci td.kR{background:var(--ink);color:#fff;font-weight:600}
table.raci td.kC{color:var(--ink-2)}
table.raci td.kI{color:#94A3B8}
/* Flatplan */
.flatplan{display:grid;grid-template-columns:repeat(9,1fr);gap:3pt 4pt;margin:1pt 0 2pt}
.fp{display:grid;grid-template-columns:1fr 1fr;gap:1pt}
.fp.single{grid-template-columns:1fr;width:50%}
.fp.single.r{margin-left:50%}
.pg{height:21pt;border:.5pt solid var(--line-2);display:flex;flex-direction:column;justify-content:space-between;padding:1.4pt 2pt;font-family:var(--f-mono);font-size:.62em;line-height:1;color:var(--ink-2);background:#fff;overflow:hidden}
.pg .s{font-family:var(--f-head);font-size:.86em;font-weight:600;white-space:nowrap}
.pg.portada-c{background:var(--ink);color:#fff;border-color:var(--ink)}
.pg.pauta{background:repeating-linear-gradient(135deg,#E2E8F0 0 2pt,#F8FAFC 2pt 4pt);color:#334155}
.pg.auto{background:#DBEAFE;color:#1E3A8A}
.pg.sumario{background:#F1F5F9}.pg.pulso{background:#BFDBFE}.pg.lente{background:#C7D2FE}.pg.reportaje{background:#FDE68A}
.pg.fila{background:#FBCFE8}.pg.gamer{background:var(--carbon);color:#E2E8F0;border-color:var(--carbon)}.pg.business{background:#BBF7D0}
.pg.conexion{background:#FED7AA}.pg.ruta{background:#A5F3FC}.pg.cierre{background:#E7E5E4}
.leyenda{display:flex;flex-wrap:wrap;gap:2pt 8pt;font-size:.8em;color:var(--ink-2);margin:0 0 3pt}
.leyenda span{display:inline-flex;align-items:center;gap:3pt}
.leyenda i.pg{display:inline-block;width:8pt;height:8pt;padding:0;border-radius:1.5pt}
/* Cronograma */
.gantt{display:grid;grid-template-columns:auto repeat(8,1fr);gap:1.6pt 2pt;font-size:.8em;margin:1pt 0 2pt}
.gantt .h{font-family:var(--f-head);font-weight:600;color:var(--muted);text-align:center;border-bottom:.5pt solid var(--line-2)}
.gantt .l{font-family:var(--f-head);font-weight:600;color:var(--ink-2);white-space:nowrap;padding-right:3pt}
.gantt .b{height:9pt;border-radius:1.5pt;background:var(--bg-3);border:.4pt solid var(--line)}
.gantt .b.on{background:#BFDBFE;border-color:#93C5FD}
.gantt .b.on2{background:#FDE68A;border-color:#FCD34D}
.gantt .b.on3{background:#FBCFE8;border-color:#F9A8D4}
.gantt .b.g{background:var(--ink);border-color:var(--ink)}
/* Firmas */
.firma{margin-top:6pt;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12pt}
.firma div{border-top:.8pt solid var(--ink);padding-top:3pt;font-size:.86em;color:var(--muted)}
.firma b{display:block;color:var(--ink);font-family:var(--f-head)}
/* Impresión */
@page{size:A4;margin:12mm 11mm 12mm 11mm;
  @top-left{content:"__HEADER__";font:6.2pt "Lexend","Avenir Next",sans-serif;color:#64748B}
  @top-right{content:"__CODE__";font:6.2pt "JetBrains Mono",Menlo,monospace;color:#64748B}
  @bottom-left{content:"__FOOTER__";font:6.2pt "Source Sans 3","Avenir Next",sans-serif;color:#64748B}
  @bottom-right{content:"Página " counter(page) " de " counter(pages);font:6.2pt "Source Sans 3","Avenir Next",sans-serif;color:#64748B}
}
@media print{
  html{font-size:__FS__pt}
  body{line-height:1.22}
}
@media screen{
  body{background:#E9EDF2;padding:24px 12px}
  .hoja{max-width:1000px;margin:0 auto;background:#fff;padding:40px 44px;border-radius:4px;box-shadow:0 1px 2px rgba(15,23,42,.08),0 12px 36px rgba(15,23,42,.10)}
  .unidad{padding-top:18px;margin-top:18px;border-top:1px dashed var(--line-2)}
  .unidad:first-of-type{border-top:0;margin-top:0;padding-top:0}
  @media (max-width:760px){
    .hoja{padding:22px 16px}
    .g2,.g-roles,.g-ciclo{grid-template-columns:1fr}
    .g4{grid-template-columns:1fr 1fr}
    .doc-meta{grid-template-columns:1fr 1fr}
    ul.cols2{columns:1}
    .flatplan{grid-template-columns:repeat(5,1fr)}
    table{display:block;overflow-x:auto}
  }
}
"""


CSS_LECTURA = r"""
:root{
  --ink:#0F172A; --ink-2:#1E293B; --muted:#475569; --line:#E2E8F0; --line-2:#CBD5E1;
  --bg:#FFFFFF; --bg-2:#F8FAFC; --bg-3:#F1F5F9; --accent:#2563EB; --accent-ink:#1D4ED8; --accent-bg:#EFF6FF;
  --f-head:"Lexend","Avenir Next","Helvetica Neue",Arial,sans-serif;
  --f-body:"Source Sans 3","Avenir Next","Helvetica Neue",Arial,sans-serif;
  --f-mono:"JetBrains Mono","SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
html{font-size:11pt;-webkit-print-color-adjust:exact;print-color-adjust:exact;-webkit-text-size-adjust:100%;text-size-adjust:100%}
body{margin:0;background:#E9EDF2;color:var(--ink);font-family:var(--f-body);line-height:1.45;font-variant-numeric:tabular-nums;overflow-wrap:break-word}
main.hoja{max-width:680px;margin:0 auto;background:var(--bg);padding:20px}
h1,h2,h3,h4{font-family:var(--f-head);color:var(--ink);line-height:1.2;margin:0;break-after:avoid;page-break-after:avoid}
p{margin:0 0 .55em}
ul{margin:0 0 .7em;padding-left:1.15em}
li{margin:0 0 .3em}
b,strong{font-weight:600}
em{font-style:italic}
.mono{font-family:var(--f-mono);font-size:.95em;overflow-wrap:anywhere}
.small{font-size:.95em;color:var(--muted)}
.intro{color:var(--ink-2)}
.datos .mono,.small .mono,.meta-list .mono,.doc-top .mono,th .mono,.fase-card .meta .mono{font-size:1em}
/* Cabecera oficial */
.doc-cab{padding-bottom:.2em;margin-bottom:.4em}
.doc-top{font-family:var(--f-mono);font-size:.95em;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:.45em}
.doc-cab h1{font-size:1.85em;font-weight:600;letter-spacing:-.01em;margin:0 0 .6em}
.meta-list{list-style:none;margin:0 0 .8em;padding:0;border-top:1px solid var(--line-2)}
.meta-list li{display:flex;flex-wrap:wrap;gap:.1em .8em;margin:0;padding:.35em 0;border-bottom:1px solid var(--line)}
.meta-list b{flex:0 0 10em;font-family:var(--f-head);font-weight:600;color:var(--muted);font-size:.95em}
.meta-list span{flex:1 1 14em}
/* Secciones */
.sec{margin-top:1.8em}
h2{font-size:1.42em;font-weight:600;padding-top:.55em;border-top:2px solid var(--ink);margin:0 0 .55em}
h2 .n{display:block;font-family:var(--f-mono);font-size:.68em;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:.2em}
h3{font-size:1.12em;font-weight:600;margin:1.15em 0 .5em}
h3 .num{color:var(--accent);margin-right:.35em}
h4{font-size:1.02em;font-weight:600}
/* Tablas compactas */
table{width:100%;border-collapse:collapse;margin:.3em 0 .9em}
thead{display:table-header-group}
tr{break-inside:avoid;page-break-inside:avoid}
th{text-align:left;font-family:var(--f-head);font-weight:600;font-size:.95em;color:var(--ink-2);background:var(--bg-3);border-bottom:1px solid var(--line-2);padding:.42em .5em;vertical-align:bottom}
td{border-bottom:1px solid var(--line);padding:.42em .5em;vertical-align:top}
td.k{font-family:var(--f-head);font-weight:600;color:var(--ink-2);width:32%}
/* Estados */
.chip{display:inline-block;font-family:var(--f-head);font-size:.95em;font-weight:600;line-height:1.25;padding:.1em .6em;border-radius:1em;white-space:nowrap}
.chip.vig{background:#DCFCE7;color:#166534}
.chip.prog{background:#E0E7FF;color:#3730A3}
/* Arquitectura del sistema */
.nivel-t{font-family:var(--f-mono);font-size:.95em;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin:.9em 0 .4em}
.bloque{border:1px solid var(--line-2);border-radius:4px;margin:0 0 .6em;break-inside:avoid;page-break-inside:avoid;overflow:hidden;background:var(--bg)}
.bloque .bh{background:var(--accent);color:#FFFFFF;font-family:var(--f-head);font-weight:600;padding:.45em .8em}
.bloque .bh span{display:block;font-weight:400;font-size:.95em;opacity:.92}
.bloque.dir .bh{background:var(--ink)}
.bloque.ed .bh{background:var(--ink-2)}
.bloque ul{list-style:none;margin:0;padding:.5em .8em .3em}
.bloque li{margin:0 0 .3em}
.bloque li .mono{color:var(--accent-ink)}
.conector{text-align:center;color:var(--muted);font-family:var(--f-head);font-size:.95em;margin:.15em 0 .45em}
.conector::before{content:"";display:block;width:2px;height:14px;background:var(--line-2);margin:0 auto .2em}
/* Fichas */
.ficha{border:1px solid var(--line-2);border-left:4px solid var(--accent);border-radius:4px;padding:.7em .9em .55em;margin:0 0 .8em;background:var(--bg);break-inside:avoid;page-break-inside:avoid}
.ficha .fh{display:flex;flex-wrap:wrap;align-items:baseline;gap:.25em .6em;margin-bottom:.2em}
.ficha .n{font-family:var(--f-mono);font-size:.95em;color:var(--muted)}
.ficha .cod{font-family:var(--f-mono);font-weight:500;color:var(--accent-ink);overflow-wrap:anywhere}
.ficha .tit{display:block;font-family:var(--f-head);font-weight:600;font-size:1.06em;margin:0 0 .35em}
.datos{list-style:none;margin:0 0 .5em;padding:0;display:flex;flex-wrap:wrap;gap:.15em 1.1em;font-size:.95em;color:var(--ink-2)}
.datos li{margin:0}
.datos b{color:var(--muted);font-weight:600;margin-right:.25em}
.ficha p{margin:0 0 .4em}
/* Expediente por edición */
.fase{font-family:var(--f-head);font-weight:600;color:var(--ink-2);background:var(--bg-3);border-radius:4px;padding:.35em .7em;margin:1.1em 0 .2em;break-after:avoid;page-break-after:avoid}
.fase .mono{font-weight:400;color:var(--muted)}
.doc{border-bottom:1px solid var(--line);padding:.55em .1em;break-inside:avoid;page-break-inside:avoid}
.doc .dh{display:flex;flex-wrap:wrap;gap:.15em .6em;align-items:baseline}
.doc .cod{font-family:var(--f-mono);font-weight:500;color:var(--accent-ink)}
.doc .tit{font-family:var(--f-head);font-weight:600}
.doc .datos{margin:.2em 0 .25em}
.doc p{margin:0}
/* Ruta e insumos */
.fase-card{border:1px solid var(--line-2);border-left:4px solid var(--ink-2);border-radius:4px;padding:.65em .9em .45em;margin:0 0 .7em;background:var(--bg);break-inside:avoid;page-break-inside:avoid}
.fase-card h4{margin:0 0 .25em}
.fase-card .meta{font-family:var(--f-mono);font-size:.95em;color:var(--accent-ink);margin:0 0 .3em}
.fase-card ul{margin:.2em 0 .35em}
.item{border-bottom:1px solid var(--line);padding:.5em .1em;break-inside:avoid;page-break-inside:avoid}
.item .t{display:block;font-family:var(--f-head);font-weight:600;margin-bottom:.15em}
.item .datos{margin:0}
/* Repositorio */
.repo,.repo ul{list-style:none;padding-left:0;margin:0}
.repo ul{padding-left:1.1em;border-left:2px solid var(--line-2);margin:.3em 0 .3em .3em}
.repo li{margin:.3em 0}
.repo .mono{font-weight:500;color:var(--ink)}
.repo .d{color:var(--muted)}
/* Firmas */
.firma{margin-top:1.6em;break-inside:avoid;page-break-inside:avoid}
.firma div{border-top:1px solid var(--ink);padding:.35em 0 1.5em;color:var(--muted)}
.firma b{display:block;color:var(--ink);font-family:var(--f-head);font-weight:600}
@page{size:A4;margin:20mm 18mm 20mm 18mm;
  @top-left{content:"__HEADER__";font:9pt "Lexend","Avenir Next",sans-serif;color:#64748B}
  @top-right{content:"__CODE__";font:9pt "JetBrains Mono",Menlo,monospace;color:#64748B}
  @bottom-left{content:"__FOOTER__";font:9pt "Source Sans 3","Avenir Next",sans-serif;color:#64748B}
  @bottom-right{content:"Página " counter(page) " de " counter(pages);font:9pt "Source Sans 3","Avenir Next",sans-serif;color:#64748B}
}
@media screen and (min-width:720px){
  main.hoja{margin:24px auto;padding:36px;border-radius:6px;box-shadow:0 1px 2px rgba(15,23,42,.08),0 12px 36px rgba(15,23,42,.10)}
}
@media print{
  html{font-size:9.5pt}
  body{background:#FFFFFF}
  main.hoja{max-width:none;margin:0;padding:0;border-radius:0;box-shadow:none}
}
"""


CSS_MD = r"""
/* Documentos del corpus en Markdown */
.doc-obj{color:var(--ink-2)}
.doc-obj p{margin:0 0 .45em}
.sec h4{margin:1.1em 0 .35em}
ol{margin:0 0 .7em;padding-left:1.4em}
code{font-family:var(--f-mono);font-size:.95em;overflow-wrap:anywhere}
.meta-list code,th code,.small code,blockquote code{font-size:1em}
blockquote{margin:.5em 0 .9em;padding:.6em .9em;border-left:4px solid var(--accent);background:var(--accent-bg);border-radius:0 4px 4px 0;break-inside:avoid;page-break-inside:avoid}
blockquote p:last-child,blockquote ul:last-child,blockquote ol:last-child{margin-bottom:0}
.tabla{overflow-x:auto;margin:.3em 0 .9em;-webkit-overflow-scrolling:touch}
.tabla table{margin:0}
.tabla td:first-child{font-weight:600;color:var(--ink-2)}
th,td{-webkit-hyphens:auto;hyphens:auto}
@media (max-width:480px){
  .tabla table{font-size:.94em}
  .tabla th,.tabla td{padding:.4em .3em}
}
"""


def fuentes_css():
    partes = []
    for familia, estilo, pesos, archivo in FUENTES:
        ruta = os.path.join(AQUI, 'fuentes', archivo)
        b64 = base64.b64encode(open(ruta, 'rb').read()).decode('ascii')
        partes.append(
            f'@font-face{{font-family:"{familia}";font-style:{estilo};font-weight:{pesos};'
            f'font-display:swap;src:url(data:font/woff2;base64,{b64}) format("woff2")}}'
        )
    return '\n'.join(partes)


def verificar_paginas(pdf, esperadas):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print('     verificación de páginas omitida: PyMuPDF no disponible')
        return True
    n = fitz.open(pdf).page_count
    if esperadas and n != esperadas:
        print(f'     AVISO: {n} páginas; extensión obligatoria de {esperadas}. Ajustar contenido o el cuerpo (fs).')
        return False
    print(f'     {n} páginas' + (' · extensión conforme' if esperadas else ''))
    return True


def construir(doc, hacer_pdf=True):
    cuerpo = open(os.path.join(AQUI, 'src', doc['src']), encoding='utf-8').read()
    base = CSS_LECTURA if doc.get('estilo') == 'lectura' else CSS.replace('__FS__', str(doc['fs']))
    css = (base
              .replace('__HEADER__', doc['header'].replace('"', '\\"'))
              .replace('__CODE__', doc['code'])
              .replace('__FOOTER__', doc['footer'].replace('"', '\\"')))
    html = (
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        f'<title>{doc["title"]}</title>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="author" content="Proyecto Editorial SoyTechno">\n'
        f'<style>\n{fuentes_css()}\n{css}\n</style>\n</head>\n<body>\n{cuerpo}\n</body>\n</html>\n'
    )
    salida = os.path.join(RAIZ, doc['out'])
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    with open(salida + '.html', 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('HTML:', os.path.relpath(salida + '.html', RAIZ), f'({os.path.getsize(salida + ".html") // 1024} KB)')
    if not hacer_pdf:
        return True
    if not os.path.exists(CHROME):
        print('ERROR: Google Chrome no encontrado en', CHROME)
        sys.exit(1)
    perfil = tempfile.mkdtemp(prefix='chrome-docs-st-')
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
           '--run-all-compositor-stages-before-draw', '--virtual-time-budget=5000',
           f'--user-data-dir={perfil}', f'--print-to-pdf={salida}.pdf', pathlib.Path(salida + '.html').as_uri()]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
    finally:
        shutil.rmtree(perfil, ignore_errors=True)
    if r.returncode != 0 or not os.path.exists(salida + '.pdf'):
        print('ERROR Chrome:', r.returncode, r.stderr[-800:])
        sys.exit(1)
    print('PDF: ', os.path.relpath(salida + '.pdf', RAIZ), f'({os.path.getsize(salida + ".pdf") // 1024} KB)')
    return verificar_paginas(salida + '.pdf', doc['paginas'])


def _texto(fragmento):
    return htmlmod.unescape(re.sub(r'<[^>]+>', '', fragmento)).strip()


def md_a_cuerpo(texto):
    """Convierte el Markdown de un documento del corpus al cuerpo HTML de la plantilla de lectura."""
    import markdown
    h = markdown.markdown(texto, extensions=['tables', 'sane_lists'], output_format='html')
    corte = h.find('<h2>')
    cab, resto = (h[:corte], h[corte:]) if corte >= 0 else (h, '')
    m = re.search(r'<h1>(.*?)</h1>', cab, re.S)
    if not m:
        raise ValueError('falta el título de nivel 1')
    titulo = m.group(1).strip()
    cab = cab[:m.start()] + cab[m.end():]
    tipo = ''
    m = re.search(r'<p>(SoyTechno · Proyecto Editorial[^<]*)</p>', cab)
    if m:
        tipo = m.group(1).strip()
        cab = cab[:m.start()] + cab[m.end():]
    meta, items = {}, []
    m = re.search(r'<table>.*?</table>', cab, re.S)
    if m:
        for k, v in re.findall(r'<tr>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>', m.group(0), re.S):
            meta[_texto(k)] = _texto(v)
            items.append(f'<li><b>{k.strip()}</b><span>{v.strip()}</span></li>')
        cab = cab[:m.start()] + cab[m.end():]
    cabecera = (f'<header class="doc-cab">\n<div class="doc-top">{tipo}</div>\n<h1>{titulo}</h1>\n'
                f'<ul class="meta-list">\n' + '\n'.join(items) + '\n</ul>\n'
                f'<div class="doc-obj">\n{cab.strip()}\n</div>\n</header>')
    secciones = []
    for parte in re.split(r'(?=<h2>)', resto):
        if not parte.strip():
            continue
        m = re.match(r'<h2>\s*(\d+)\.\s*(.*?)</h2>', parte, re.S)
        if m:
            n = m.group(1)
            parte = f'<h2><span class="n">Sección {n}</span>{m.group(2).strip()}</h2>' + parte[m.end():]
            secciones.append(f'<section class="sec" id="s{n}">\n{parte.strip()}\n</section>')
        else:
            secciones.append(f'<section class="sec">\n{parte.strip()}\n</section>')
    cuerpo = '\n'.join(secciones)
    cuerpo = re.sub(r'<h3>\s*(\d+\.\d+(?:\.\d+)?)\s+(.*?)</h3>', r'<h3><span class="num">\1</span>\2</h3>', cuerpo, flags=re.S)

    def tabla(mt):
        t = mt.group(0)
        cab_t = [_texto(c) for c in re.findall(r'<th[^>]*>(.*?)</th>', t, re.S)]
        celdas = re.findall(r'<td[^>]*>(.*?)</td>', t, re.S)
        if cab_t == ['Elaboración', 'Revisión', 'Aprobación'] and len(celdas) == 3:
            return '<div class="firma">' + ''.join(
                f'<div><b>{a}</b>{b.strip()}</div>' for a, b in zip(cab_t, celdas)) + '</div>'
        return f'<div class="tabla">{t}</div>'
    cuerpo = re.sub(r'<table>.*?</table>', tabla, cuerpo, flags=re.S)
    return f'<main class="hoja">\n{cabecera}\n{cuerpo}\n</main>', meta, _texto(titulo), tipo


def localizar_md(codigo):
    rutas = sorted(glob.glob(os.path.join(CORPUS, '**', f'{codigo}_*_v*.md'), recursive=True))
    return rutas[-1] if rutas else None


def construir_md(ruta):
    ruta = os.path.abspath(ruta)
    try:
        cuerpo, meta, titulo, tipo = md_a_cuerpo(open(ruta, encoding='utf-8').read())
    except Exception as e:  # noqa: BLE001
        print('ERROR en', os.path.relpath(ruta, RAIZ), '·', e)
        return False
    codigo = meta.get('Código', '').strip() or os.path.basename(ruta).split('_')[0]
    version = meta.get('Versión · fecha', '1.0').split('·')[0].strip()
    tipo_corto = tipo.split('·')[-1].strip() if tipo else 'Documento'
    css = (CSS_LECTURA + CSS_MD)
    css = (css.replace('__HEADER__', f'Revista Corporativa SoyTechno · {tipo_corto}'.replace('"', '\\"'))
              .replace('__CODE__', f'{codigo} · v{version}')
              .replace('__FOOTER__', meta.get('Clasificación', 'Uso interno').replace('"', '\\"')))
    html = (
        '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        f'<title>{htmlmod.escape(titulo)} · Revista Corporativa SoyTechno</title>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="author" content="Proyecto Editorial SoyTechno">\n'
        f'<style>\n{fuentes_css()}\n{css}\n</style>\n</head>\n<body>\n{cuerpo}\n</body>\n</html>\n'
    )
    salida = os.path.splitext(ruta)[0] + '.html'
    with open(salida, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('HTML:', os.path.relpath(salida, RAIZ), f'({os.path.getsize(salida) // 1024} KB)')
    return True


if __name__ == '__main__':
    banderas = [a for a in sys.argv[1:] if a.startswith('--')]
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    pdf = '--solo-html' not in banderas
    ok = True
    if not args:
        if '--md' not in banderas:
            ok = all([construir(d, hacer_pdf=pdf) for d in DOCUMENTOS])
        for ruta in sorted(glob.glob(os.path.join(CORPUS, '**', '*_v*.md'), recursive=True)):
            ok = construir_md(ruta) and ok
    else:
        for a in args:
            doc = next((d for d in DOCUMENTOS if d['codigo'] == a), None)
            if doc:
                ok = construir(doc, hacer_pdf=pdf) and ok
                continue
            ruta = a if a.endswith('.md') and os.path.exists(a) else localizar_md(a)
            if not ruta:
                print('ERROR: documento no encontrado:', a)
                ok = False
                continue
            ok = construir_md(ruta) and ok
    sys.exit(0 if ok else 2)
