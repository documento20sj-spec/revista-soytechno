#!/usr/bin/env python3
"""Convierte design-demos/C_sistema.html (dirección elegida) en final/plantilla.html: 11 capítulos y revista de 13 pliegos."""
import os, re
F = os.path.dirname(os.path.abspath(__file__))
P = os.path.dirname(F)
s = open(os.path.join(P, 'design-demos', 'C_sistema.html'), encoding='utf-8').read()
leer = lambda n: open(os.path.join(F, n), encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c >= 1, 'no encontrado: ' + a[:90]
    if n == 1: assert c == 1, f'{c} coincidencias: ' + a[:90]
    s = s.replace(a, b)

def cortar(ini, fin, nuevo=''):
    """Sustituye desde la marca ini (incluida) hasta la marca fin (excluida)."""
    global s
    i = s.index(ini); j = s.index(fin, i)
    s = s[:i] + nuevo + s[j:]

# ---------------------------------------------------------------- cabecera
rep('<title>SoyTechno, la revista · Propuesta para evaluación</title>', '<title>SoyTechno, la revista · Propuesta del proyecto editorial</title>')
rep('content="Proyecto editorial SoyTechno: la revista como objeto hojeable y el ciclo de ocho semanas con seis compuertas de control."',
    'content="Propuesta del proyecto editorial SoyTechno para Carelys Eljuri: la revista hojeable, el ciclo de ocho semanas, la hora cero, el evento, la economía en porcentajes y el sistema documental."')
rep("var m=q.match(/[?&]pantalla=([123])/)", "var m=q.match(/[?&]pantalla=([0-9]+)/)")

# ---------------------------------------------------------------- CSS: la barra superior del teléfono se acota a header.bar
# .bar también nombra las líneas de texto de las páginas en tránsito y las barras de los paquetes del capítulo 9:
# sin acotar, en escritorio quedaban ocultas y en teléfono heredaban position:fixed
rep('.bar{display:none}', 'header.bar{display:none}')
rep('  .bar{display:flex;position:fixed;', '  header.bar{display:flex;position:fixed;')
rep('@supports (backdrop-filter:blur(1px)){.bar{', '@supports (backdrop-filter:blur(1px)){header.bar{')
rep('@media (prefers-reduced-transparency:reduce){.bar{', '@media (prefers-reduced-transparency:reduce){header.bar{')

# ---------------------------------------------------------------- teléfono: con 13 pliegos las etiquetas de los pasos se pisan (27 px por paso a 390);
# el nombre del pliego ya está en el indicador de cabecera, así que en teléfono los pasos quedan como puntos
rep('.step{padding-right:4px}.step b{font-size:12px;line-height:16px}', '.step{padding-right:4px}.step b{font-size:12px;line-height:16px}.step span{display:none}')

# ---------------------------------------------------------------- tipografía: cifra y unidad con espacio duro también en el texto que escribe el script
rep('Cifras · Archivo Black · ${fs} px · tabulares', 'Cifras · Archivo Black · ${fs}\\u00a0px · tabulares')

# ---------------------------------------------------------------- accesibilidad: el logotipo dentro de un enlace con nombre propio es decorativo
rep('<a href="#c1" aria-label="SoyTechno · inicio"><svg class="logo" viewBox="0 0 204 30" role="img" aria-label="SoyTechno" fill="currentColor">',
    '<a href="#c1" aria-label="SoyTechno · inicio"><svg class="logo" viewBox="0 0 204 30" aria-hidden="true" focusable="false" fill="currentColor">', n=2)

# ---------------------------------------------------------------- notas: los desplazamientos pueden seguir la escala del libro (k)
# en px fijos, la distancia entre la nota y su ancla no acompaña a la página cuando el escenario es más bajo y aparecen choques
rep("con w y h = tamaño de la nota. */", "con w y h = tamaño de la nota y k = escala del libro (1 con 676 px de escenario). */")
rep("Function('w', 'h', 'return ' + e)(w, h)", "Function('w', 'h', 'k', 'return ' + e)(w, h, K)")

# ---------------------------------------------------------------- CSS: portada propia en capas (despiece) y pautas de páginas en tránsito
cortar('/* ---------- C1 · Portada (MAN-ID §5) ---------- */', '/* ---------- 02 · Sumario ---------- */', '''/* ---------- C1 · Portada en capas (despiece) ---------- */
.pg.cover{overflow:visible;transform-style:preserve-3d}
.pg.cover .lz{transform-style:preserve-3d}
.cover .ly{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;
  transform:translateZ(calc(var(--e,0)*var(--z,0px)*var(--k,1)));box-shadow:inset 0 0 0 calc(var(--r,0)*1.5px) var(--azul-40)}
.ly-bg{--z:0px}.ly-ph{--z:34px}.ly-veil{--z:68px}.ly-mast{--z:102px}.ly-band{--z:136px}.ly-title{--z:170px}.ly-calls{--z:204px}.ly-credit{--z:238px}

/* ---------- Páginas en tránsito: pauta ---------- */
.gpauta{background:var(--platino)}
.gpauta .rotulo{position:absolute;top:calc(10*var(--mm));left:0;right:0;text-align:center;font:500 calc(7*var(--pt))/calc(7*var(--pt)) var(--f-d);color:var(--gris)}
.gpauta .slot{position:absolute;left:calc(18*var(--mm));right:calc(15*var(--mm));top:calc(15*var(--mm));bottom:calc(20*var(--mm));
  border:1px dashed var(--gris);display:grid;place-items:center;text-align:center;color:var(--gris);padding:calc(8*var(--mm))}
.verso.gpauta .slot{left:calc(15*var(--mm));right:calc(18*var(--mm))}
.gpauta .slot span{font:400 calc(8*var(--pt))/calc(10*var(--pt)) var(--f-m)}
.pg-dark.gpauta{background:var(--profundo)}
.pg-dark.gpauta .rotulo,.pg-dark.gpauta .slot{color:var(--platino);border-color:rgba(244,245,247,.5)}

''')
cortar('/* ---------- 02 · Sumario ---------- */', '/* ---------- Páginas en tránsito (estructura de retícula, sin texto inventado) ---------- */')
# la caja de texto de las páginas de C (.pg) chocaba con la raíz de las páginas propias (.pg): se elimina
rep('''/* Caja de texto y elementos fijos */
.pg{position:absolute;top:calc(15*var(--mm));bottom:calc(20*var(--mm))}
.recto .pg{left:calc(18*var(--mm));right:calc(15*var(--mm))}
.verso .pg{left:calc(15*var(--mm));right:calc(18*var(--mm))}
.folio{position:absolute;bottom:calc(11.4*var(--mm))}
.recto .folio{right:calc(15*var(--mm))}
.verso .folio{left:calc(15*var(--mm))}
.tab{position:absolute;width:calc(3*var(--mm));height:calc(24*var(--mm));background:var(--azul);top:calc((15 + 24*var(--k,0))*var(--mm))}
.verso .tab{left:0}.recto .tab{right:0}''', '''/* Elementos fijos de las páginas en tránsito */
.page .folio{position:absolute;bottom:calc(11.4*var(--mm))}
.page.recto .folio{right:calc(15*var(--mm))}
.page.verso .folio{left:calc(15*var(--mm))}''')
rep('.show-pgrid .page::after{display:block}', '.show-pgrid .page::after{display:block}\n.show-pgrid .pg .guia{display:block}\n.pg .nota{display:none!important}')
# capítulos para captura
rep('html[data-only="1"] #c2,html[data-only="1"] #c3,html[data-only="2"] #c1,html[data-only="2"] #c3,html[data-only="3"] #c1,html[data-only="3"] #c2{display:none}',
    ''.join(f'html[data-only]:not([data-only="{n}"]) #c{n}{{display:none}}' for n in range(1, 12)))
# pasos: 13 pliegos
rep('.steps{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}', '.steps{position:relative;display:grid;grid-template-columns:repeat(var(--ns,4),minmax(0,1fr))}')
rep('.step span{display:block;font:400 12px/16px var(--f-m);letter-spacing:.04em}', '.step span{display:block;font:500 12px/16px var(--f-m);letter-spacing:.02em;white-space:nowrap}\n.step b{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}')
# riel más compacto para 11 capítulos
rep('.rail-nav{margin-top:var(--s6)}', '.rail-nav{margin-top:var(--s4)}')
rep('.rail-list a{display:block;padding:var(--s2) 0;', '.rail-list a{display:block;padding:7px 0;')
rep(".rail-list li::before{content:'';position:absolute;left:calc(-1*var(--s3));top:18px;", ".rail-list li::before{content:'';position:absolute;left:calc(-1*var(--s3));top:12px;")
rep('.rail-list .t{display:block;font:500 16px/20px var(--f-d)}', '.rail-list .t{display:block;font:500 14px/18px var(--f-d)}')
rep('@media (max-width:899px){\n  :root{--rail:0px;--m:16px;--g:8px}', '@media (max-height:820px) and (min-width:900px){.rail-foot .tag{display:none}.rail-list a{padding:5px 0}.rail-list li::before{top:10px}}\n@media (max-width:899px){\n  :root{--rail:0px;--m:16px;--g:8px}')
rep('  .bar-nav{display:flex;gap:4px;align-items:center}', '  .bar-nav{display:flex;gap:4px;align-items:center;overflow-x:auto;scrollbar-width:none;max-width:calc(100vw - 160px);scroll-snap-type:x proximity}\n  .bar-nav::-webkit-scrollbar{display:none}\n  .bar-nav a{flex:none;scroll-snap-align:center}')
rep('/* ---------- Estados de entrada: solo si hay movimiento ---------- */', leer('capitulos.css') + '\n/*CSS_COMPONENTES*/\n\n/* ---------- Estados de entrada: solo si hay movimiento ---------- */')

# ---------------------------------------------------------------- HTML: riel y barra con 11 capítulos
CAP = [('01','Apertura','Apertura'),('02','La revista','Revista'),('03','El proyecto','Proyecto'),('04','Arquitectura','52 páginas'),('05','Del papel al teléfono','QR y NFC'),
       ('06','Ciclo de ocho semanas','Ciclo'),('07','Hora cero y evento','Hora cero'),('08','Año editorial','2027'),('09','Economía','Economía'),('10','Control','Control'),('11','Próximos pasos','Pasos')]
ON, CUR = ' class="on"', ' aria-current="true"'
rail = ''.join('        <li data-ch="%d"%s><a href="#c%d"%s><span class="n">%s</span><span class="t">%s</span></a></li>\n' % (int(n), ON if n == '01' else '', int(n), CUR if n == '01' else '', n, t) for n, t, _ in CAP)
cortar('        <li data-ch="1" class="on"><a href="#c1" aria-current="true"><span class="n">01</span><span class="t">Apertura</span></a></li>', '      </ol>', rail)
bar = ''.join('    <a href="#c%d" data-ch="%d"%s>%s<span class="tt">%s</span></a>\n' % (int(n), int(n), (ON + CUR) if n == '01' else '', n, c) for n, _, c in CAP)
cortar('    <a href="#c1" data-ch="1" class="on" aria-current="true">01<span class="tt">Apertura</span></a>', '  </nav>', bar)
# apertura: destinataria
rep('        <p class="eyebrow rv">Proyecto editorial · Propuesta para evaluación</p>', '        <p class="para rv">Preparado para Carelys Eljuri</p>\n        <p class="eyebrow rv">Proyecto editorial · Propuesta para evaluación</p>')
# capítulo 2: pasos y grupos de anotación los genera el script
cortar('          <button class="step on" type="button" data-k="0">', '          <i class="fill" id="stepFill" aria-hidden="true"></i>', '')
rep('<div class="ann-g" data-g="x"></div><div class="ann-g" data-g="0"></div><div class="ann-g" data-g="1"></div><div class="ann-g" data-g="2"></div><div class="ann-g" data-g="3"></div>', '')
# capítulo del ciclo: pasa a ser el 06 y se insertan los nuevos
rep('<section id="c3" class="ch c3" data-ch="3" aria-labelledby="t3">', leer('capitulos-a.html') + '\n<!-- =============== CAPÍTULO 6 · CICLO DE OCHO SEMANAS =============== -->\n<section id="c6" class="ch c3" data-ch="6" aria-labelledby="t3">')
rep('<p class="kicker rv">03 · Ciclo de ocho semanas y compuertas</p>', '<p class="kicker rv">06 · Ciclo de ocho semanas y compuertas</p>')
rep('</section>\n</main>', '</section>\n' + leer('capitulos-b.html') + '\n' + leer('capitulos-c.html') + '\n</main>')
# plantillas de C → fuente de páginas propias
cortar('<!-- ============ PÁGINAS DE LA REVISTA (plantillas inertes, texto literal del contenido) ============ -->', '<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>',
       '<!-- Páginas de la revista (fuente): el motor las coloca en las hojas -->\n<div id="revista-fuente" hidden><!--REVISTA--></div>\n<script>/*FOTOS*/</script>\n\n')
rep('<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>\n<script>/*JS_COMPONENTES*/</script>')

open(os.path.join(F, 'plantilla-paso1.html'), 'w', encoding='utf-8').write(s)
print('paso 1 listo', len(s))

# =========================================================================================== PASO 2 · JAVASCRIPT
# páginas en tránsito: clase de pauta propia
rep("const page = el('div', `page ${verso ? 'verso hinge-l' : 'recto hinge-r'} gen${dark ? ' pg-dark' : ''}${sec.pauta ? ' pauta' : ''}`);",
    "const page = el('div', `page ${verso ? 'verso hinge-l' : 'recto hinge-r'} gen${dark ? ' pg-dark' : ''}${sec.pauta ? ' gpauta' : ''}`);")
# hojas con las páginas propias (24 diseñadas) y estructura en tránsito para el resto
cortar("const KNOWN = { 1: 'tpl-p01', 2: 'tpl-p02', 3: 'tpl-p03', 16: 'tpl-p16', 17: 'tpl-p17', 28: 'tpl-p28', 29: 'tpl-p29' };", "const decorate = page =>", '''const NL = 26;
const FUENTE = $('#revista-fuente');
const PID = (i, side) => i === 0 ? (side === 'front' ? 'C1' : 'C2') : i === NL - 1 ? (side === 'front' ? 'C3' : 'C4') : String(side === 'front' ? 2 * i - 1 : 2 * i).padStart(2, '0');
function pageFor(i, side) {                                 // página diseñada si existe; si no, estructura de retícula
  const id = PID(i, side), p = FUENTE.querySelector(`.pg[data-p="${id}"]`);
  if (p) { p.classList.add(p.classList.contains('verso') ? 'hinge-l' : 'hinge-r'); return p; }
  return genPage(parseInt(id, 10));
}
const coverSrc = FUENTE.querySelector('.pg[data-p="C1"]').cloneNode(true);   // copia para la apertura, antes de montar las hojas
''')
rep("""const cover1 = tpl('tpl-cover'); cover1.style.setProperty('--e', '.22'); $('#tilt1').append(cover1);
$('.ph', cover1).setAttribute('fetchpriority', 'high');                       // portada de la apertura: imagen crítica""",
"""const cover1 = coverSrc; cover1.style.setProperty('--e', '.22'); $('#tilt1').append(cover1);
const ph1 = $('.pt-foto', cover1); if (ph1) ph1.setAttribute('fetchpriority', 'high');   // portada de la apertura: imagen crítica""")
rep("const coverEl = $('.page.cover', leaves[0].front);", "const coverEl = $('.pg.cover', leaves[0].front);")
rep("const S = { E: 1, shift: 1 };", "const S = { E: 1, shift: 1, shiftB: 0 };")
rep("""  pos.style.transform = `translateX(${(-25 * S.shift).toFixed(3)}%) scale(${(1 + (closedScale() - 1) * S.shift * (1 - E)).toFixed(4)})`;""",
    """  pos.style.transform = `translateX(${(-25 * S.shift + 25 * S.shiftB).toFixed(3)}%) scale(${(1 + (closedScale() - 1) * (S.shift + S.shiftB) * (1 - E)).toFixed(4)})`;""")
rep("""  underL.style.opacity = clamp((L[0].t - .5) * 4, 0, 1).toFixed(3);                  // la sombra izquierda asoma solo cuando la portada aterriza""",
    """  underL.style.opacity = clamp((L[0].t - .5) * 4, 0, 1).toFixed(3);                  // la sombra izquierda asoma solo cuando la portada aterriza
  underR.style.opacity = clamp((.5 - L[NL - 1].t) * 4, 0, 1).toFixed(3);              // y la derecha se retira al cerrar la contraportada""")
cortar("/* Pliegos: portada → 02-03 → 16-17 → 28-29 */", "render();\n\n/* =====================================================================\n   4 · ANOTACIONES", '''/* Trece pliegos de la Edición 01 (hojas giradas en cada uno) */
const TURNED = [0, 1, 2, 3, 5, 9, 11, 15, 19, 21, 23, 25, 26];
const NAMES = ['C1 · Portada', 'C2-01 · Doble premium', '02-03 · Sumario y créditos', '04-05 · Pulso Techno', '08-09 · Bajo el Lente', '16-17 · Reportaje Central',
  '20-21 · En Primera Fila', '28-29 · ADN Gamer', '36-37 · Espacio Business', '40-41 · Conexión en Vivo', '44-45 · Ruta Inteligente', '48-C3 · Última Página y zona NFC', 'C4 · Contraportada'];
const SHORT = ['C1', 'C2-01', '02-03', '04-05', '08-09', '16-17', '20-21', '28-29', '36-37', '40-41', '44-45', '48-C3', 'C4'];
const NS = TURNED.length;
function setStop(k, E = 0) {
  S.E = E; S.shift = k === 0 ? 1 : 0; S.shiftB = k === NS - 1 ? 1 : 0;
  L.forEach((o, i) => { o.t = i < TURNED[k] ? 1 : 0; });
  render();
}
''')
# anotaciones: definición nueva para las páginas propias
cortar("const ANN = {", "const groups = {};", '''const ANN = {
  x: [  // vista despiezada · el ancla sale del propio elemento 3D
    { t: 'Crédito · imagen de referencia',                   el: '.ly-credit .pt-credito', c: [79, 13], s: 'r' },
    { t: 'Llamados · Archivo Bold 14/18,75 pt',              el: '.ly-calls .pt-llamados', c: [79, 27], s: 'r' },
    { t: 'Titular · Archivo Black 56 pt',                    el: '.ly-title .pt-titular',  c: [79, 41], s: 'r' },
    { t: 'Velo azul noche · 40 % como mínimo',               el: '.ly-veil',               c: [79, 55], s: 'r' },
    { t: 'Cintillo · Archivo Medium 9/12,5 pt',              el: '.pt-cintillo',           c: [21, 15], s: 'l' },
    { t: 'Cabecera · logotipo vectorial sin deformar',       el: '.pt-logo',               c: [21, 27], s: 'l' },
    { t: 'Fotografía · retrato 3:4 · sin precios',           el: '.pt-foto',               c: [21, 50], s: 'l' },
    { t: 'Fondo · extensión del color de la foto',           el: '.pt-fondo',              c: [21, 66], s: 'l' }
  ],
  0: [
    { t: 'Formato 210 × 280 mm · sangrado 3 mm',   a: cov(210, 6),    c: [76.8, 3],  s: 'r' },
    { t: 'Cabecera · 21,6 % de la altura',         a: cov(17, 24),    c: [23.2, 8],  s: 'l' },
    { t: 'Zona libre superior 20 %',               a: cov(210, 56),   c: [76.8, 14], s: 'r' },
    { t: 'Cintillo · Archivo Medium 9/12,5 pt',    a: cov(17, 58),    c: [23.2, 20], s: 'l' },
    { t: 'Fotografía · 3:4 · fondo extendido',     a: cov(160, 110),  c: [76.8, 36], s: 'r' },
    { t: 'Titular · Archivo Black · 56 pt',        a: cov(17, 200),   c: [23.2, 72], s: 'l' },
    { t: 'Sin precios ni logotipos de terceros',   a: cov(201, 192),  c: [76.8, 62], s: 'r' },
    { t: 'Llamados · Archivo Bold 14/18,75 pt',    a: cov(16, 247),   c: [23.2, 89], s: 'l' },
    { t: 'Crédito vertical · imagen de referencia', a: cov(205, 236), c: [76.8, 88], s: 'r' }
  ],
  2: [
    { t: 'Cabecera · Archivo Black 24/25 pt\\nFilete · 1 pt · Azul SoyTechno', face: [1, 'back'], el: '.st-cabecera', rng: 1, at: 't', f: .15, o: ['-16*k', '-h-10*k'] },   // sobre la cabecera: a su derecha cruzaba el lomo con escenarios bajos
    { t: 'Índice · módulos de 3 columnas',                        face: [1, 'back'], el: '.sm-mod:nth-child(8)', at: 'b', f: .5, o: ['-w+50*k', '40*k'] },   // bajo la segunda fila, alineada al borde de la retícula: a la derecha cruzaba el lomo y tapaba la carta
    { t: 'Folio · margen inferior exterior',                      face: [1, 'back'], el: '.folio', rng: 1, at: 'r', o: ['14*k', '-h/2'] },
    { t: 'Carta · 2 columnas · 9,5/12,5 pt',                      face: [2, 'front'], el: '.ce-tit', rng: 1, at: 't', f: 1, o: ['-w', '-h-24*k'] },   // encima del titular, alineada a su final: a la derecha salía de la pantalla en 1280 px
    { t: 'Mancheta · 4 columnas · JetBrains Mono 8/10 pt',        face: [2, 'front'], el: '.mc', at: 'b', f: .3, o: ['-24*k', '24*k'] },
    { t: 'QR real · 2 columnas (26,16 mm) · un código por pieza', face: [2, 'front'], el: '.ix .cod', at: 't', f: .5, o: ['-40*k', '-h-30*k'] }
  ],
  4: [
    { t: 'Bodegón · fondo Gris Platino',                          face: [4, 'back'], el: '.bl-bodegon', at: 'b', f: .78, o: ['-w/2', '-h-36*k'] },   // sobre la propia foto: debajo tapaba el titular
    { t: 'Titular\\nArchivo Bold 36 pt',                          face: [4, 'back'], el: '.st-titular', rng: 1, at: 'r', o: ['16*k', '-h/2'] },
    { t: 'Ficha · JetBrains Mono 8/10 pt\\nGama en lugar de precio', face: [5, 'front'], el: '.bl-ficha', at: 'b', f: .5, o: ['-w+68*k', '24*k'] },   // bajo la ficha, en el blanco de la página: a la izquierda tapaba el cuerpo
    { t: 'Veredicto sin revisión\\nde la marca',                   face: [5, 'front'], el: '.bl-veredicto', at: 't', f: .9, o: ['-w+24*k', '-h-22*k'] },   // a la derecha del bloque: más a la izquierda chocaba con el titular por debajo de 1440 px
    { t: 'QR real por pieza',                                     face: [5, 'front'], el: '.bl-qr .cod', at: 't', f: .5, o: ['-w/2+30*k', '-h-14*k'] }   // encima del código, a la derecha del veredicto: a la izquierda tapaba los criterios
  ],
  7: [
    { t: 'Modo oscuro · Negro Carbón\\nsolo en ADN Gamer', face: [14, 'back'], el: '.ag-cab', rng: 1, at: 'r', o: ['18*k', '-h/2-4*k'] },   // corta: con k 0,73 solo quedan 229 px entre la cabecera y el lomo
    { t: 'Titular · Archivo Black 48 pt · Blanco Puro',           face: [14, 'back'], el: '.st-titular', rng: 1, at: 'r', o: ['-40*k', '53*k'] },   // bajo el titular, a la derecha de la entradilla: a su lado dejaba sitio libre en la página 29 para el QR
    { t: 'Ficha · JetBrains Mono Medium\\n9,5/12,5 pt · Bloque Azul Profundo', face: [15, 'front'], el: '.ag-ficha', at: 't', f: .5, o: ['-w/2+40*k', '-h-14*k'] },   // sobre el margen superior: debajo tapaba la agenda
    { t: 'QR sobre fondo oscuro\\nrecuadro claro · corrección Q', face: [15, 'front'], el: '.ag-qr .cod', at: 'b', f: .5, o: ['-w/2', '20*k'] },   // bajo el código: a la izquierda tapaba la fotografía
    { t: 'Folio · Blanco Puro 9,5 pt',                            face: [14, 'back'], el: '.folio', rng: 1, at: 'r', o: ['16*k', '-h/2'] }
  ],
  11: [
    { t: 'Firma por cargo directivo',                             face: [24, 'back'], el: '.up-firma', rng: 1, at: 'l', o: ['-w-8*k', '6*k'] },   // a la izquierda, en el hueco bajo la primera columna: a la derecha cruzaba el lomo
    { t: 'Adelanto sin portada ni personaje',                     face: [24, 'back'], el: '.up-adelanto', at: 'b', f: .5, o: ['-w/2-30*k', '24*k'] },
    { t: 'Zona de contacto NFC · 40 × 40 mm\\n≥ 30 mm del lomo · ≥ 20 mm de los cortes', face: [25, 'front'], el: '.nfc-zona', at: 't', f: .95, o: ['-w/2', '-h-30*k'] },   // ancla a la derecha del rótulo «Zona de contacto NFC»: en el centro la guía lo atravesaba
    { t: 'QR equivalente adyacente',                              face: [25, 'front'], el: '.nfc-qr .cod', at: 'r', o: ['22*k', '-h-2*k'] },   // por encima del rótulo del QR, que empieza a media altura del código
    { t: 'Etiqueta NTAG213 · 25 mm · escritura bloqueada',        face: [25, 'front'], el: '.nfc-etq', at: 'b', f: .5, o: ['-w/2', '46*k'] }
  ]
};
Object.keys(ANN).forEach(k => { const g = el('div', 'ann-g', $('#ann')); g.dataset.g = k; });
''')
rep("""const stateOf = k => () => { S.E = k === 'x' ? 1 : 0; S.shift = (k === 'x' || k === 0) ? 1 : 0; L.forEach((o, i) => { o.t = k === 'x' ? 0 : (i < TURNED[k] ? 1 : 0); }); };""",
    """const stateOf = k => () => { S.E = k === 'x' ? 1 : 0; S.shift = (k === 'x' || +k === 0) ? 1 : 0; S.shiftB = +k === NS - 1 ? 1 : 0; L.forEach((o, i) => { o.t = k === 'x' ? 0 : (i < TURNED[+k] ? 1 : 0); }); };""")
rep("""  const keep = { E: S.E, shift: S.shift, t: L.map(o => o.t) };""", """  const keep = { E: S.E, shift: S.shift, shiftB: S.shiftB, t: L.map(o => o.t) };""")
rep("""finally { S.E = keep.E; S.shift = keep.shift; L.forEach""", """finally { S.E = keep.E; S.shift = keep.shift; S.shiftB = keep.shiftB; L.forEach""")
rep("""  ['x', 0, 1, 2, 3].forEach(k => { anch[k] = withState(stateOf(k), () => (ANN[k] || []).map(c => anchorOf(c, sr, W, H))); });""",
    """  Object.keys(ANN).forEach(k => { anch[k] = withState(stateOf(k), () => (ANN[k] || []).map(c => anchorOf(c, sr, W, H))); });""")
# pasos generados
rep("""const indEl = $('#t2'), prevBtn = $('#prev'), nextBtn = $('#next'), stepBtns = $$('.step'), rulesEl = $('#rules'), stepFill = $('#stepFill');""",
    """(() => { const box = $('#steps'), fill = $('#stepFill'); box.style.setProperty('--ns', NS);
  SHORT.forEach((s, k) => { const b = document.createElement('button'); b.className = 'step' + (k === 0 ? ' on' : ''); b.type = 'button'; b.dataset.k = k;
    b.setAttribute('aria-label', NAMES[k]); b.title = NAMES[k]; b.innerHTML = `<span>${s}</span><b>${NAMES[k]}</b>`; box.insertBefore(b, fill); }); })();
const indEl = $('#t2'), prevBtn = $('#prev'), nextBtn = $('#next'), stepBtns = $$('.step'), rulesEl = $('#rules'), stepFill = $('#stepFill');""")
rep("prevBtn.disabled = k === 0; nextBtn.disabled = k === 3;", "prevBtn.disabled = k === 0; nextBtn.disabled = k === NS - 1;")
rep("""  const a = Math.floor(clamp(f, 0, 3)), b = Math.min(3, a + 1), fr = clamp(f, 0, 3) - a;""", """  const a = Math.floor(clamp(f, 0, NS - 1)), b = Math.min(NS - 1, a + 1), fr = clamp(f, 0, NS - 1) - a;""")
rep("  k = clamp(k, 0, 3); const fade =", "  k = clamp(k, 0, NS - 1); const fade =")
# riel generalizado a 11 capítulos
rep("""  const i = Math.min(2, Math.floor(pos)), fr = pos - i, y = railYs[i] + ((i < 2 ? railYs[i + 1] : railEnd) - railYs[i]) * fr;""",
    """  const NCH = chEls.length, i = Math.min(NCH - 1, Math.floor(pos)), fr = pos - i, y = railYs[i] + ((i < NCH - 1 ? railYs[i + 1] : railEnd) - railYs[i]) * fr;""")
rep("  barProg.style.transform = `scaleX(${clamp(pos / 3, 0, 1).toFixed(4)})`;", "  barProg.style.transform = `scaleX(${clamp(pos / chEls.length, 0, 1).toFixed(4)})`;")
rep("(mqPhone.matches && n === 3 ? 56 : 0)", "(mqPhone.matches && n === 6 ? 56 : 0)")
# línea de tiempo del libro: 13 pliegos
cortar("const STOPS = [1.3, 2.85, 4.4, 5.95], TOTAL = 6.25;", "let bookTL = null, bookST = null, dragging = false;", '''const STOPS = [1.3], SEGS = [];                              // reposo de cada pliego en la línea de tiempo
for (let k = 1; k < NS; k++) { const n = TURNED[k] - TURNED[k - 1], d = n > 1 ? .5 + (n - 1) * .08 : .7, t0 = STOPS[k - 1] + .2; SEGS.push([t0, n, d]); STOPS.push(t0 + d + .35); }
const TOTAL = STOPS[NS - 1] + .3;
''')
rep("""  for (let i = 1; i < 4; i++) if (Math.abs(t - STOPS[i]) < Math.abs(t - STOPS[k])) k = i;""", """  for (let i = 1; i < NS; i++) if (Math.abs(t - STOPS[i]) < Math.abs(t - STOPS[k])) k = i;""")
rep("""  if (t >= STOPS[3]) f = 3; else if (t > STOPS[0]) { let a = 0; while (a < 2 && t > STOPS[a + 1]) a++; f = a + (t - STOPS[a]) / (STOPS[a + 1] - STOPS[a]); }""",
    """  if (t >= STOPS[NS - 1]) f = NS - 1; else if (t > STOPS[0]) { let a = 0; while (a < NS - 2 && t > STOPS[a + 1]) a++; f = a + (t - STOPS[a]) / (STOPS[a + 1] - STOPS[a]); }""")
cortar("  tl.to(S, { shift: 0, duration: .7, ease: 'power2.inOut' }, 1.5);", "  tl.to({}, { duration: .01 }, TOTAL - .01);", '''  SEGS.forEach(([t0, n, d], j) => {                                                       // cada pliego: hojas en cascada
    const k = j + 1, a = TURNED[k - 1];
    if (k === 1) tl.to(S, { shift: 0, duration: .7, ease: 'power2.inOut' }, t0);           // la portada se abre y el libro se centra
    if (k === NS - 1) tl.to(S, { shiftB: 1, duration: .7, ease: 'power2.inOut' }, t0);     // la contraportada cierra el libro
    for (let i = 0; i < n; i++) tl.to(L[a + i], { t: 1, duration: n > 1 ? .5 : .7, ease: 'power2.inOut' }, t0 + i * .08);
  });
''')
rep("""  STOPS.forEach((s, k) => {
    tl.fromTo(groups[k], { autoAlpha: 0 }, { autoAlpha: 1, duration: .2 }, s - .3);
    if (k < 3) tl.to(groups[k], { autoAlpha: 0, duration: .2 }, s + .12);
  });""", """  STOPS.forEach((s, k) => {
    const g = groups[k]; if (!g) return;
    tl.fromTo(g, { autoAlpha: 0 }, { autoAlpha: 1, duration: .2 }, s - .3);
    if (k < NS - 1) tl.to(g, { autoAlpha: 0, duration: .2 }, s + .12);
  });""")
rep("    trigger: '#c2', start: 'top top', end: () => '+=' + Math.round(innerHeight * TOTAL * .72),", "    trigger: '#c2', start: 'top top', end: () => '+=' + Math.round(innerHeight * TOTAL * .42),")
rep("""function goStop(k) {
  k = clamp(k, 0, 3);""", """function goStop(k) {
  k = clamp(k, 0, NS - 1);""")
rep("const k0 = drag.k0, fr = clamp(-dx / (stage.clientWidth / 2 * .85), -1, 1), tgt = clamp(k0 + (fr > 0 ? 1 : -1), 0, 3), lim = tgt === k0 ? .1 : 1;",
    "const k0 = drag.k0, fr = clamp(-dx / (stage.clientWidth / 2 * .85), -1, 1), tgt = clamp(k0 + (fr > 0 ? 1 : -1), 0, NS - 1), lim = tgt === k0 ? .1 : 1;")
# teclado y URL con 11 capítulos (el ciclo es el 6)
rep("  else if ((e.key === 'ArrowRight' || e.key === 'ArrowLeft') && activeCh === 3) { e.preventDefault(); gateStep(e.key === 'ArrowRight' ? 1 : -1); }",
    "  else if ((e.key === 'ArrowRight' || e.key === 'ArrowLeft') && activeCh === 6) { e.preventDefault(); gateStep(e.key === 'ArrowRight' ? 1 : -1); }")
rep("  else if (/^[123]$/.test(e.key)) goChapter(+e.key);", "  else if (/^[1-9]$/.test(e.key)) goChapter(+e.key);")
rep("      if (activeCh === 3 && selId) q.set('compuerta', selId);", "      if (activeCh === 6 && selId) q.set('compuerta', selId);")
rep("    circST = ScrollTrigger.create({ trigger: '#c3', start: 'top top',", "    circST = ScrollTrigger.create({ trigger: '#c6', start: 'top top',")
rep("  const k0 = clamp(parseInt(qs.get('pliego') || '0', 10) || 0, 0, 3);", "  const k0 = clamp(parseInt(qs.get('pliego') || '0', 10) || 0, 0, NS - 1);")
rep("    if (n === 2 && k !== null && bookST) scrollToY(yOfTime(STOPS[clamp(parseInt(k, 10) || 0, 0, 3)]), 0);", "    if (n === 2 && k !== null && bookST) scrollToY(yOfTime(STOPS[clamp(parseInt(k, 10) || 0, 0, NS - 1)]), 0);")
rep("    else if (n === 3 && gate && circST && (circ.h || circ.v)) {", "    else if (n === 6 && gate && circST && (circ.h || circ.v)) {")
rep("    else if (n >= 1 && n <= 3) scrollToY(chapterY(n), 0);", "    else if (n >= 1 && n <= 11) scrollToY(chapterY(n), 0);")
rep("    const n = parseInt(qs.get('pantalla') || '0', 10); if (n >= 1 && n <= 3) scrollToY(chapterY(n), 0);", "    const n = parseInt(qs.get('pantalla') || '0', 10); if (n >= 1 && n <= 11) scrollToY(chapterY(n), 0);")
# arranque: fijaciones primero (orden de la página), después revelados y capítulos nuevos
rep("""  introHero(); coverTilt(); reveals();
  render(); showGroup('x');
  bookTL = buildBookTL(); buildBookST(); onBookUpdate();      // estado inicial del indicador y de los pasos
  circuitST(); stripsST();""", """  introHero(); coverTilt();
  render(); showGroup('x');
  bookTL = buildBookTL(); buildBookST(); onBookUpdate();      // estado inicial del indicador y de los pasos
  circuitST(); stripsST();
  reveals(); extrasAnimados();                               // ScrollTrigger en orden de página: fijaciones antes que revelados""")
rep("""  setCircuit(parseFloat(qs.get('circuito') || '1'), false);
  strips.forEach(s => setStrip(s, 1));
}""", """  setCircuit(parseFloat(qs.get('circuito') || '1'), false);
  strips.forEach(s => setStrip(s, 1));
  extrasEstaticos();
}""")
rep("/* =====================================================================\n   10 · ARRANQUE", leer('capitulos.js') + "\n/* =====================================================================\n   10 · ARRANQUE")
open(os.path.join(F, 'plantilla.html'), 'w', encoding='utf-8').write(s)
print('plantilla lista', len(s))
