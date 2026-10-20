#!/usr/bin/env python3
"""Comprueba a 375 px (Chrome sin interfaz, marco de 375 px) los HTML del corpus: desplazamiento horizontal,
tablas desbordadas y cuerpo mínimo de letra. Uso: python3 verificar_movil.py [CÓDIGO ...]"""
import glob, html, os, re, shutil, subprocess, sys, tempfile
RAIZ = '/Users/germanjaraba/Proyectos/Revista Carelis'
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
JS = ("<script>window.addEventListener('load',()=>{setTimeout(()=>{const els=[...document.querySelectorAll('body *')]"
      ".filter(e=>[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()));const min=Math.min(...els.map(e=>"
      "parseFloat(getComputedStyle(e).fontSize)));const t=[...document.querySelectorAll('.tabla')].map(x=>x.scrollWidth-"
      "x.clientWidth).filter(v=>v>1);parent.postMessage(JSON.stringify({vw:innerWidth,sw:document.documentElement.scrollWidth,"
      "min:+min.toFixed(1),tablasDesbordadas:t}),'*');},300)});</script>")
sel = sys.argv[1:]
tmp = tempfile.mkdtemp(prefix='movil-')
for f in sorted(glob.glob(os.path.join(RAIZ, '02_Corpus_Documental', '*', '*', '*_v1.html'))):
    cod = os.path.basename(f)[:17]
    if sel and cod not in sel:
        continue
    doc = os.path.join(tmp, cod + '.html')
    open(doc, 'w', encoding='utf-8').write(open(f, encoding='utf-8').read().replace('</body>', JS + '</body>'))
    marco = os.path.join(tmp, cod + '.marco.html')
    open(marco, 'w', encoding='utf-8').write(
        f'<!doctype html><html><body style="margin:0"><iframe src="{cod}.html" style="width:375px;height:812px;border:0">'
        "</iframe><script>window.addEventListener('message',e=>{const p=document.createElement('pre');p.id='m';"
        "p.textContent=e.data;document.body.appendChild(p);});</script></body></html>")
    perfil = tempfile.mkdtemp(prefix='chrome-movil-')
    r = subprocess.run([CH, '--headless=new', '--disable-gpu', '--window-size=500,900', '--allow-file-access-from-files',
                        '--virtual-time-budget=6000', f'--user-data-dir={perfil}', '--dump-dom', 'file://' + marco],
                       capture_output=True, text=True)
    shutil.rmtree(perfil, ignore_errors=True)
    m = re.search(r'<pre id="m">(.*?)</pre>', r.stdout)
    print(cod, html.unescape(m.group(1)) if m else 'sin medida')
shutil.rmtree(tmp, ignore_errors=True)
