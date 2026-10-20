#!/usr/bin/env python3
"""Ensambla la presentación final en un único HTML.
Entradas: plantilla de la dirección elegida (plantilla.html con marcadores), componentes de la revista, gráficos y diagramas.
Marcadores en la plantilla: <!--REVISTA-->, <!--GRAFICO:clave-->, <!--DIAGRAMA:clave-->, /*CSS_COMPONENTES*/, /*JS_COMPONENTES*/.
Modo --incrustar: sustituye las URL remotas (Unsplash, Google Fonts, jsDelivr) por datos base64 desde descargas/ (solo si existen)."""
import os, re, sys, base64, json
BASE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.join(BASE, 'componentes')
DESC = os.path.join(BASE, 'descargas')
SALIDA = os.path.dirname(BASE)                    # 06_Propuesta_Presentacion: el respaldo vive dentro de la carpeta del entregable
sys.path.insert(0, COMP)
leer = lambda *p: open(os.path.join(*p), encoding='utf-8').read()

def ensamblar(plantilla, incrustar=False):
    import graficos, diagramas
    sys.path.insert(0, os.path.join(BASE, 'herramientas')); import qr
    html = leer(plantilla)
    html = html.replace('<!--REVISTA-->', leer(COMP, 'revista-fragmento.html'))
    g, d = graficos.todos(), diagramas.todos()
    html = re.sub(r'<!--GRAFICO:(\w+)-->', lambda m: g[m.group(1)], html)
    html = re.sub(r'<!--DIAGRAMA:(\w+)-->', lambda m: d[m.group(1)], html)
    html = html.replace('<div class="phy-qr" id="phyQR" aria-hidden="true"></div>',
        '<div class="phy-qr" id="phyQR" aria-hidden="true">' + qr.svg('SoyTechno, la revista · Propuesta del proyecto editorial · QR de muestra: un código por pieza') + '</div>')
    html = espacios_duros(html)
    css = leer(COMP, 'revista.css') + leer(COMP, 'revista-paginas.css') + leer(COMP, 'graficos.css') + leer(COMP, 'diagramas.css')
    html = html.replace('/*CSS_COMPONENTES*/', css).replace('/*JS_COMPONENTES*/', leer(COMP, 'graficos.js'))
    html = registro_fotos(html, incrustar)
    if incrustar:
        html = incrustar_recursos(html)
    return html

UNIDAD = re.compile(r'(\d) (%|h|mm|pt|px|min|cm|in|Hz|GB|MB|mAh|dpi)(?![\wÀ-ÿ])')
SIGNO = re.compile(r'([≥≤±×]) (?=\d)|(\d) (?=×)')

def _duro(t):
    t = UNIDAD.sub('\\1\u00a0\\2', t)
    return SIGNO.sub(lambda m: (m.group(1) or m.group(2)) + '\u00a0', t)

def espacios_duros(html):
    """Cifra y unidad (24 px, 6 %, 72 h) y signo y cifra (≥ 5, 210 × 280) quedan unidos con espacio duro para que no se partan
    entre líneas. Solo en el texto visible: etiquetas, atributos, scripts y estilos no se tocan. Las notas del libro son texto
    de script, así que su tabla (const ANN) se trata aparte: en teléfono se leen como lista y también pueden partirse."""
    partes = re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<[^>]+>)', html, flags=re.S)
    for i in range(0, len(partes), 2):
        partes[i] = _duro(partes[i])
    html = ''.join(partes)
    i = html.find('const ANN = {'); j = html.find('\n};', i)
    return html[:i] + _duro(html[i:j]) + html[j:] if i >= 0 and j > i else html

def registro_fotos(html, incrustar):
    """Cada fotografía se guarda una sola vez (window.FOTOS) y se asigna a todas sus apariciones."""
    ids = []
    def ver(i):
        if i not in ids: ids.append(i)
        return i
    html = re.sub(r'src="https://images\.unsplash\.com/photo-([0-9a-f-]+)\?[^"]*"', lambda m: f'data-foto="{ver(m.group(1))}"', html)
    html = re.sub(r'srcset="[^"]*images\.unsplash\.com[^"]*"', '', html)
    html = re.sub(r"style=\"background-image:url\('https://images\.unsplash\.com/photo-([0-9a-f-]+)\?[^']*'\)\"", lambda m: f'data-foto-bg="{ver(m.group(1))}"', html)
    for i in re.findall(r'data-foto="([0-9a-f-]+)"', html): ver(i)
    fotos = {}
    for i in ids:
        ruta = os.path.join(DESC, 'fotos', i + '.webp')
        fotos[i] = b64(ruta, 'image/webp') if (incrustar and os.path.exists(ruta)) else f'https://images.unsplash.com/photo-{i}?w=1600&q=72&fm=webp'
    js = ('window.FOTOS=' + json.dumps(fotos) + ';'
          'document.querySelectorAll("[data-foto]").forEach(function(i){var u=FOTOS[i.dataset.foto];if(u)i.src=u;});'
          'document.querySelectorAll("[data-foto-bg]").forEach(function(e){var u=FOTOS[e.dataset.fotoBg];if(u)e.style.backgroundImage="url("+u+")";});')
    print(f'fotografías únicas: {len(ids)}', file=sys.stderr)
    return html.replace('/*FOTOS*/', js)

def b64(ruta, mime):
    return f'data:{mime};base64,' + base64.b64encode(open(ruta, 'rb').read()).decode()

def incrustar_recursos(html):
    faltan = []
    # Fotografías: photo-<id>?w=… → descargas/fotos/<id>.webp
    def foto(m):
        ruta = os.path.join(DESC, 'fotos', m.group(1) + '.webp')
        if os.path.exists(ruta): return b64(ruta, 'image/webp')
        faltan.append(m.group(0)); return m.group(0)
    html = re.sub(r'https://images\.unsplash\.com/photo-([0-9a-f-]+)\?[^"\')\s]*', foto, html)
    # Scripts GSAP: <script src="…/gsap@3.13.0/dist/X.min.js"></script> → en línea
    def scr(m):
        ruta = os.path.join(DESC, 'gsap', m.group(1))
        if os.path.exists(ruta): return '<script>' + open(ruta, encoding='utf-8').read() + '</script>'
        faltan.append(m.group(1)); return m.group(0)
    html = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/gsap@3\.13\.0/dist/([\w.]+\.js)"></script>', scr, html)
    # Fuentes: enlace de Google Fonts → @font-face con woff2 local
    caras = [('Archivo', 'normal', '400 900', 'Archivo-variable.woff2'), ('Source Serif 4', 'normal', '400 700', 'SourceSerif4-variable.woff2'),
             ('Source Serif 4', 'italic', '400 700', 'SourceSerif4-italic-variable.woff2'), ('JetBrains Mono', 'normal', '100 800', 'JetBrainsMono-variable.woff2')]
    ff = ''
    for fam, est, pes, arch in caras:
        ruta = os.path.join(DESC, 'fuentes', arch)   # las cuatro familias viven en respaldo/descargas/fuentes: la carpeta no depende de nada externo
        if os.path.exists(ruta):
            ff += f'@font-face{{font-family:"{fam}";font-style:{est};font-weight:{pes};font-display:swap;src:url({b64(ruta, "font/woff2")}) format("woff2")}}\n'
        else: faltan.append(arch)
    if ff:
        html = re.sub(r'<link[^>]+fonts\.googleapis\.com[^>]*>', '', html)
        html = re.sub(r'<link rel="preconnect"[^>]+>', '', html)
        html = html.replace('<style>', '<style>\n' + ff, 1)
    if faltan: print('Sin copia local (quedan enlazados):', len(faltan), file=sys.stderr)
    return html

if __name__ == '__main__':
    plantilla = next((a for a in sys.argv[1:] if not a.startswith('--')), os.path.join(BASE, 'final', 'plantilla.html'))
    incr = '--incrustar' in sys.argv
    os.makedirs(SALIDA, exist_ok=True)
    out = os.path.join(SALIDA, 'SoyTechno_Propuesta_Revista.html')
    html = ensamblar(plantilla, incr)
    open(out, 'w', encoding='utf-8').write(html)
    print(out, f'{len(html.encode("utf-8")) / 1024 / 1024:.2f} MB')
