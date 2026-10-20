#!/usr/bin/env python3
"""Genera las páginas de la revista simulada (Edición 01) conforme a MAN-ID.
Salidas: revista-paginas.html (banco de revisión por pliegos) y revista-fragmento.html (solo páginas)."""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(BASE, 'herramientas'))
import qr

FOTO = lambda i, w=1200: f'https://images.unsplash.com/photo-{i}?w={w}&q=72&fm=webp'
IMG = {
 'portada': FOTO('1534528741775-53994a69daeb', 1600), 'reportaje': FOTO('1518770660439-4636190af475', 1600),
 'gamer': FOTO('1560253023-3ec5d502959f', 1600), 'esports': FOTO('1542751371-adc38448a05e'),
 'entrevista': FOTO('1506794778202-cad84cf45f1d', 1400), 'business': FOTO('1519085360753-af0119f7cbe7'),
 'pyme': FOTO('1556740758-90de374c12ad'), 'telefono': FOTO('1574944985070-8f3ebc6b79d2'),
 'portatil': FOTO('1588872657578-7efd1f1555ed'), 'tunel': FOTO('1512499617640-c74ae3a79d37'),
 'revelacion': FOTO('1492684223066-81342ee5ff30', 1600), 'publico': FOTO('1540575467063-178a50c2df87'),
 'mesas': FOTO('1528605248644-14dd04022da1'), 'podcast': FOTO('1590602847861-f357a9332bbc'),
 'networking': FOTO('1515187029135-18ee286d815b'), 'microfono': FOTO('1475721027785-f74eccf877e2'),
 'montaje': FOTO('1511578314322-379afb476865'),
}

def logo(nombre, color, recorte=None, clase=''):
    s = open(os.path.join(BASE, 'assets', 'logos', f'SoyTechno_{nombre}_{color}.svg'), encoding='utf-8').read()
    s = re.sub(r'<\?xml[^>]*>\s*', '', s)
    if recorte:
        s = re.sub(r'viewBox="[^"]*"', f'viewBox="{recorte}"', s, count=1)
    return s.replace('<svg ', f'<svg class="{clase}" aria-hidden="true" focusable="false" ', 1)

LOGOTIPO = '30.80 6.74 167.67 17.74'   # caja real de las letras (alto de la «S» = área de respeto)

def codigo(texto, nivel='M'):
    return qr.svg(texto, nivel)

def bloque_qr(micro, url, texto, nivel='M', extra=''):
    return (f'<div class="qr {extra}"><div class="cod">{codigo(texto, nivel)}</div>'
            f'<div><p class="micro">{micro}</p><p class="url">{url}</p></div></div>')

def guia(notas=()):
    cols = ''.join('<i></i>' for _ in range(12))
    ns = ''.join(f'<span class="nota" style="{css}">{t}</span>' for t, css in notas)
    return f'<div class="guia" aria-hidden="true"><div class="cols">{cols}</div><div class="base"></div></div>{ns}'

def ajustar_titulos(h):
    h = re.sub(r'<h1 class="pt-cabecera">(.*?)</h1>', r'<div class="pt-cabecera">\1</div>', h, flags=re.S)
    h = re.sub(r'<h[23] (class="st-titular[^"]*")>(.*?)</h[23]>', r'<h4 \1>\2</h4>', h, flags=re.S)
    h = re.sub(r'<h2 (class="st-cabecera[^"]*")>(.*?)</h2>', r'<h3 \1>\2</h3>', h, flags=re.S)
    return h

def pagina(id_, lado, contenido, clases='', etiqueta='', notas=()):
    return (f'<section class="pg {lado} {clases}" data-p="{id_}" aria-label="{etiqueta}">'
            f'<div class="lz">{ajustar_titulos(contenido)}{guia(notas)}</div></section>')

def folio(num, seccion):
    return f'<p class="folio">{num} · {seccion}</p>'

def pestana(i):
    return f'<span class="pestana" style="--i:{i}" aria-hidden="true"></span>'

P = {}
# ---------------------------------------------------------------- C1 · Portada
P['C1'] = pagina('C1', 'recto', f'''
<div class="ly ly-bg"><div class="pt-fondo" aria-hidden="true"></div></div>
<div class="ly ly-ph"><img class="pt-foto" src="{IMG['portada']}" alt="Retrato de referencia con iluminación azul de estudio"></div>
<div class="ly ly-veil"><div class="pt-velo" aria-hidden="true"></div></div>
<div class="ly ly-mast"><h1 class="pt-cabecera">{logo('logotipo','blanco',LOGOTIPO,'pt-logo')}<span class="sr">SoyTechno</span></h1></div>
<div class="ly ly-band"><p class="pt-cintillo"><span>Edición 01 · Enero-febrero 2027</span><span>Una publicación de SoyTechno</span></p></div>
<div class="ly ly-title"><div class="pt-bloque">
  <p class="pt-titular">Tecnología que ordena el año</p>
  <ul class="pt-llamados" aria-hidden="true"><li><i class="vineta"></i>Tres categorías a prueba</li><li><i class="vineta"></i>Cuotas con plataformas aliadas</li><li><i class="vineta"></i>Calendario de torneos 2027</li></ul>
</div></div>
<div class="ly ly-calls"><div class="pt-bloque">
  <p class="pt-titular" aria-hidden="true">Tecnología que ordena el año</p>
  <ul class="pt-llamados"><li><i class="vineta"></i>Tres categorías a prueba</li><li><i class="vineta"></i>Cuotas con plataformas aliadas</li><li><i class="vineta"></i>Calendario de torneos 2027</li></ul>
</div></div>
<div class="ly ly-credit"><p class="pt-credito">Imagen de referencia</p></div>''', 'portada cover', 'Portada C1',
 notas=(('Cabecera · zona superior 21,6 % · respeto = alto de la «S»','top:3%;left:9%'),
        ('Titular · Archivo Black 60 pt · fuera del rostro','top:63%;left:9%'),
        ('Llamados · Archivo Bold 14/18,75 pt · viñeta Azul SoyTechno','top:86%;left:9%')))

# ---------------------------------------------------------------- C2-01 · Doble premium (pauta)
def pauta(id_, lado, titulo, detalle, medida):
    return pagina(id_, lado, f'''
<p class="rotulo-pauta"><span>Publicidad</span></p>
<div class="pauta-reserva"><span class="esq e1"></span><span class="esq e2"></span><span class="esq e3"></span><span class="esq e4"></span>
  <p class="st-datos pauta-cod">{medida}</p>
  <p class="pauta-tit">{titulo}</p>
  <p class="pauta-det">{detalle}</p>
</div>''', 'pauta', f'Pauta {id_}')
P['C2'] = pauta('C2', 'verso', 'Doble página premium', 'Patrocinante principal · exclusividad de categoría · paquete Presenta con presentación del evento y experiencia NFC de la marca', 'C2-01 · 420 × 280 mm · pieza aprobada por la marca en G3')
P['01'] = pauta('01', 'recto', 'Espacio de la marca aliada', 'Rótulo «Publicidad» en cada página · sin precios impresos · QR del anunciante con parámetros asignados por Digital y Datos', 'Página 01 · continuación de la doble premium')

# ---------------------------------------------------------------- 02-03 · Sumario y créditos
SUMARIO = [('04','Pulso Techno','Tendencias, software y novedades en tiendas','tunel'),
 ('08','Bajo el Lente','Telefonía; televisión, audio y hogar; cómputo portátil','telefono'),
 ('16','Reportaje Central','La inteligencia artificial cambia de escala','reportaje'),
 ('20','En Primera Fila','Entrevista central y perfiles','entrevista'),
 ('28','ADN Gamer','El puesto de juego, pieza por pieza','gamer'),
 ('36','Espacio Business','Infraestructura y gestión para pymes','pyme'),
 ('40','Conexión en Vivo','Crónica del lanzamiento','revelacion'),
 ('44','Ruta Inteligente','Selección por perfil, cuotas y Club SoyTechno','portatil'),
 ('48','Última Página','El futuro tecnológico, en una columna','microfono')]
mods = ''
for n,(f,s,d,im) in enumerate(SUMARIO):
    mini = f'<img class="sm-img" src="{IMG[im]}" alt="" loading="lazy">' if im else '<span class="sm-img vacio" aria-hidden="true"></span>'
    mods += f'<li class="sm-mod">{mini}<span class="sm-f">{f}</span><span class="sm-s">{s}</span><span class="sm-d">{d}</span></li>'
P['02'] = pagina('02', 'verso', f'''{pestana(0)}
<div class="caja">
  <h2 class="st-cabecera c1-12">Sumario</h2>
  <p class="st-antetitulo c1-12 sm-ed">Edición 01 · Enero-febrero 2027 · 52 páginas</p>
  <ol class="sm-lista c1-12">{mods}<li class="sm-cifras" aria-label="Composición de la edición"><span><b>52</b>páginas</span><span><b>44</b>editoriales</span><span><b>7</b>de pauta · 13,5 %</span><span><b>1</b>de autopromoción</span></li></ol>
</div>{folio('02','Sumario')}''', '', 'Sumario, página 02',
 notas=(('Índice visual · módulos de 3 columnas','top:13%;left:8%'),('Folio · Archivo Medium 7 pt · margen inferior exterior','bottom:7%;left:8%')))

MANCHETA = [('Editor','SoyTechno'),('Dirección','Dirección Editorial'),('Contenido','Redacción y especialistas'),('Diseño','Arte y maquetación'),
 ('Imagen','Fotografía y audiovisual'),('Registro','Depósito legal e ISSN: en trámite'),('Tiraje','5.000 ejemplares'),('Leyenda','Una publicación de SoyTechno')]
manch = ''.join(f'<div><p class="st-datos mc-k">{k}</p><p class="st-datos"><b>{v}</b></p></div>' for k,v in MANCHETA)
P['03'] = pagina('03', 'recto', f'''
<div class="caja">
  <p class="st-antetitulo c1-12">Carta editorial</p>
  <h3 class="st-titular t24 c1-12 ce-tit">Una revista para decidir mejor</h3>
  <div class="st-cuerpo dos-col c1-12 ce-txt">
    <p>Cada edición de SoyTechno parte de una pregunta práctica: qué tecnología resuelve mejor una necesidad concreta y cómo se accede a ella. La respuesta se construye con pruebas de uso real de al menos cinco días, fichas contrastadas con la documentación de cada fabricante y veredictos sin intervención de las marcas.</p>
    <p>La revista no publica precios: el precio vigente, la disponibilidad y las condiciones de financiamiento se consultan mediante el código QR de cada pieza. La etiqueta NFC de la contraportada interior da acceso a la edición digital, al pódcast y a los beneficios del Club SoyTechno.</p>
    <p>Cada edición circula desde el día siguiente a su lanzamiento hasta el Día D de la siguiente, en las sedes de SoyTechno y en el Club, y queda disponible en edición digital desde la hora cero de su revelación.</p>
    <p class="ce-firma">Dirección Editorial · SoyTechno</p>
  </div>
  <div class="c1-12 mc">{manch}</div>
  <div class="c1-12 ix">
    <p class="st-antetitulo ix-t">Interacción</p>
    {bloque_qr('Acceso a ficha, precio vigente y video','Un código por pieza','SoyTechno · Edición 01 · Simulación de bloque QR por pieza')}
    <div class="ix-nfc"><span class="ix-anillo" aria-hidden="true"><span>NFC</span></span><div><p class="micro-nfc">Zona de contacto NFC</p><p class="st-datos">Contraportada interior · edición digital, pódcast y Club SoyTechno</p></div></div>
  </div>
</div>{folio('03','Sumario')}''', '', 'Carta editorial y créditos, página 03',
 notas=(('Carta · 2 columnas · justificado con partición','top:20%;left:12%'),('Mancheta · 4 columnas · estilo Datos','top:58%;left:12%'),('Bloque QR · 2 columnas · 26,16 mm','top:76%;left:12%')))

# ---------------------------------------------------------------- 04-05 · Pulso Techno
P['04'] = pagina('04', 'verso', f'''{pestana(1)}
<div class="caja">
  <h2 class="st-cabecera c1-12">Pulso Techno</h2>
  <p class="st-antetitulo c1-12 pu-ante">Tendencias · Software · Tiendas</p>
  <article class="c1-6 pu-breve">
    <p class="st-antetitulo pu-tema">Normativa</p>
    <h3 class="st-titular t24">El cargador común ya es norma en Europa</h3>
    <div class="st-cuerpo"><p>Desde el 28-dic-2024, los teléfonos, tabletas, cámaras, auriculares y consolas portátiles vendidos en la Unión Europea incorporan puerto USB-C; los portátiles se suman desde el 28-abr-2026. Consecuencia práctica: un solo cable para la mayoría de los equipos.</p></div>
  </article>
  <article class="c7-12 pu-breve">
    <p class="st-antetitulo pu-tema">Conectividad</p>
    <h3 class="st-titular t24">Wi-Fi 7, la tercera banda en casa</h3>
    <div class="st-cuerpo"><p>El estándar IEEE 802.11be, comercializado como Wi-Fi 7, admite canales de hasta 320 MHz en la banda de 6 GHz y la operación simultánea en varias bandas. Requisito para aprovecharlo: enrutador y equipos compatibles.</p></div>
  </article>
  <figure class="c1-12 pu-foto"><img src="{IMG['tunel']}" alt="Teléfono inteligente en mano bajo luz azul" loading="lazy"><figcaption class="st-pie">Funciones de inteligencia artificial ejecutadas en el propio equipo. <span class="st-credito">Imagen de referencia</span></figcaption></figure>
  <article class="c1-12 pu-breve pu-ia">
    <p class="st-antetitulo pu-tema">Inteligencia artificial</p>
    <h3 class="st-titular t24">Funciones de IA sin conexión</h3>
    <div class="st-cuerpo pu-3"><p>Los procesadores recientes de gama media y alta integran unidades de procesamiento neuronal (NPU) capaces de ejecutar traducción, transcripción y edición de imagen en el propio equipo, sin enviar datos a la nube. En la ficha técnica, la presencia de NPU y la memoria disponible pasan a ser criterios de compra.</p></div>
  </article>
</div>{folio('04','Pulso Techno')}''', '', 'Pulso Techno, página 04',
 notas=(('Breves · titular Archivo Bold 24 pt','top:21%;left:8%'),('Pie · Source Serif 4 Italic 7,5/9,5 pt','top:72%;left:8%')))

P['05'] = pagina('05', 'recto', f'''
<div class="caja">
  <section class="c1-12 pu-info" aria-label="Infografía">
    <p class="st-antetitulo">Infografía</p>
    <h3 class="st-titular t36">Del papel al teléfono, en tres pasos</h3>
    <ol class="pu-pasos">
      <li><span class="pu-n">1</span><b>Escaneo del QR de la pieza</b><span>Un código por reseña, ficha o cobertura; sin reutilización entre ediciones.</span></li>
      <li><span class="pu-n">2</span><b>Ficha con precio vigente y video</b><span>Destino editable después de la impresión: el precio nunca queda desactualizado en papel.</span></li>
      <li><span class="pu-n">3</span><b>Compra en tienda o en línea</b><span>Con la opción de cuotas mediante plataformas aliadas.</span></li>
    </ol>
    <p class="st-pie pu-fuente">Fuente: Documento Rector SoyTechno, §3.6.</p>
  </section>
  <article class="c1-6 pu-breve">
    <p class="st-antetitulo pu-tema">Pagos</p>
    <h3 class="st-titular t24">La tecnología de la contraportada interior</h3>
    <div class="st-cuerpo"><p>Los pagos sin contacto con teléfono utilizan NFC, comunicación de campo cercano que opera a pocos centímetros. La zona de contacto de esta revista aplica el mismo principio para abrir la edición digital y el pódcast.</p></div>
  </article>
  <aside class="c7-12 pu-modulo">
    <p class="st-antetitulo">Ventana comercial de la edición</p>
    <p class="pu-cifra">14-feb</p>
    <p class="st-cuerpo">San Valentín. Día D de la Edición 01 fijado al menos diez días antes de la fecha comercial principal de su ventana.</p>
  </aside>
</div>{folio('05','Pulso Techno')}''', '', 'Pulso Techno, página 05',
 notas=(('Infografía · fuente identificada en el pie','top:8%;left:12%'),('Módulo de apoyo · Gris Platino','top:66%;left:56%')))

# ---------------------------------------------------------------- 08-09 · Bajo el Lente · Telefonía
P['08'] = pagina('08', 'verso', f'''{pestana(2)}
<figure class="bl-bodegon"><img src="{IMG['telefono']}" alt="Bodegón de teléfono inteligente sobre fondo claro" loading="lazy"></figure>
<div class="caja">
  <h2 class="st-cabecera c1-12">Bajo el Lente</h2>
  <div class="c1-12 bl-espacio" aria-hidden="true"></div>
  <p class="st-antetitulo c1-12">Telefonía · gama alta</p>
  <h3 class="st-titular t36 c1-12">Cinco días con un teléfono de gama alta</h3>
  <p class="st-entradilla c1-12 bl-entr">Uso real, sin laboratorio de marca: cámara, pantalla, autonomía y software evaluados con la ficha común de la categoría.</p>
  <p class="st-pie c1-12">Bodegón sobre fondo Gris Platino. <span class="st-credito">Imagen de referencia</span></p>
</div>{folio('08','Bajo el Lente')}''', '', 'Bajo el Lente, página 08',
 notas=(('Bodegón · fondo Gris Platino','top:16%;left:8%'),('Titular · Archivo Bold 36 pt','top:63%;left:8%')))

FICHA_TEL = [('Pantalla','6,7 in OLED · 120 Hz'),('Procesador','8 núcleos · NPU integrada'),('Memoria','12 GB + 256 GB'),('Batería','5.000 mAh'),
 ('Carga','USB-C'),('Cámaras','50 MP principal + ultra gran angular + teleobjetivo'),('Gama','Alta')]
fich = ''.join(f'<div class="fila st-datos"><span>{k}</span><b>{v}</b></div>' for k,v in FICHA_TEL)
P['09'] = pagina('09', 'recto', f'''
<div class="caja">
  <div class="st-cuerpo c1-8 bl-texto">
    <p>La prueba se extiende durante cinco días de uso cotidiano: mensajería, navegación, fotografía diurna y nocturna, videollamadas y juego. Cada jornada se registra la autonomía con brillo automático y la temperatura en sesiones de juego de 30 minutos.</p>
    <p class="st-ladillo">Pantalla y cámara</p>
    <p>La pantalla se mide en exterior a mediodía y en interior con luz cálida. La cámara se evalúa en tres escenas fijas por categoría, repetidas en todos los equipos del año para permitir la comparación entre ediciones.</p>
    <p class="st-ladillo">Autonomía</p>
    <p>Se mide con un ciclo fijo de navegación, video y llamadas, con brillo automático y datos móviles activos. El resultado se expresa en horas de uso real, no en cifras de laboratorio.</p>
    <p class="st-ladillo">Software</p>
    <p>Se revisan la política de actualizaciones publicada por el fabricante, la cantidad de aplicaciones preinstaladas y las funciones de inteligencia artificial disponibles sin conexión.</p>
  </div>
  <aside class="c9-12 ficha bl-ficha"><p class="st-antetitulo">Ficha de referencia de la categoría</p>{fich}</aside>
  <section class="c1-8 bl-veredicto"><p class="st-antetitulo">Veredicto</p>
    <p class="st-cuerpo">Se emite al cierre de los cinco días, bajo responsabilidad de Redacción, sin revisión de la marca. Escala de 1 a 5 por criterio.</p>
    <ul class="bl-criterios st-datos"><li>Rendimiento</li><li>Pantalla</li><li>Autonomía</li><li>Construcción</li><li>Software</li><li>Experiencia de uso</li></ul>
    <p class="st-datos bl-origen"><b>Origen del equipo:</b> unidad de préstamo, devuelta al cierre de la prueba.</p>
  </section>
  <div class="c9-12 bl-qr">{bloque_qr('Acceso a ficha, precio vigente y video','soytechno.com/r/e01p08a','SoyTechno · Edición 01 · pág. 08 · Simulación de QR por pieza','M','v')}</div>
  <p class="st-credito c1-12 bl-firma">Texto y pruebas: especialista de telefonía · Fotografía: imagen de referencia</p>
</div>{folio('09','Bajo el Lente')}''', '', 'Bajo el Lente, página 09',
 notas=(('Ficha · JetBrains Mono 8/10 pt sobre Gris Platino','top:6%;left:66%'),('Gama en lugar de precio','top:44%;left:66%'),('QR por pieza','top:74%;left:66%')))

# ---------------------------------------------------------------- 16-17 · Reportaje Central
P['16'] = pagina('16', 'verso', f'''{pestana(3)}
<div class="sangre rc-img" style="background-image:url('{IMG['reportaje']}')" role="img" aria-label="Placa de circuito iluminada en azul"></div>
<div class="rc-velo" aria-hidden="true"></div>
<div class="caja rc-caja">
  <p class="st-antetitulo c1-12 rc-ante">Reportaje Central · Tendencias</p>
  <h2 class="st-titular negra t48 c1-12 rc-tit">La inteligencia artificial cambia de escala</h2>
</div>''', 'oscuro-foto', 'Reportaje Central, página 16',
 notas=(('Apertura a sangre · sin folio','top:5%;left:8%'),('Titular · Archivo Black 60 pt','top:58%;left:8%')))

P['17'] = pagina('17', 'recto', f'''
<div class="caja">
  <p class="st-entradilla c1-12 rc-entr">Del centro de datos al teléfono: los asistentes y las funciones de inteligencia artificial pasan a ejecutarse en el propio dispositivo, con efectos en la autonomía, la privacidad y la elección del próximo equipo.</p>
  <p class="st-credito c1-12 rc-firma">Texto: Redacción SoyTechno · Imagen de referencia</p>
  <div class="st-cuerpo dos-col c1-12 rc-txt">
    <p>El procesamiento local de modelos de lenguaje y de imagen exige unidades neuronales dedicadas, más memoria y una gestión térmica distinta. En la decisión de compra, la consecuencia es concreta: la memoria y el procesador pesan tanto como la cámara.</p>
    <p class="st-ladillo">Qué cambia en la ficha técnica</p>
    <p>La guía de esta edición compara tres perfiles de uso (estudio, trabajo y creación de contenido) y señala qué especificaciones conviene priorizar en cada caso.</p>
    <p>Las funciones que antes dependían de una conexión estable, como la transcripción de reuniones o la traducción simultánea, quedan disponibles sin red. El costo se traslada al equipo: más memoria, más energía y más calor que disipar.</p>
  </div>
  <blockquote class="st-destacado c2-12 rc-dest">«La pregunta ya no es si un equipo tiene inteligencia artificial, sino dónde se ejecuta.»</blockquote>
</div>{folio('17','Reportaje Central')}''', '', 'Reportaje Central, página 17',
 notas=(('Entradilla · Source Serif 4 Semibold 13/18,75 pt','top:5%;left:12%'),('Texto · 2 columnas · 9,5/12,5 pt','top:34%;left:12%'),('Destacado · uno por doble página','top:76%;left:12%')))

# ---------------------------------------------------------------- 20-21 · En Primera Fila
P['20'] = pagina('20', 'verso', f'''{pestana(4)}
<div class="sangre pf-img" style="background-image:url('{IMG['entrevista']}')" role="img" aria-label="Retrato de referencia sobre fondo negro"></div>
<div class="caja">
  <h2 class="st-cabecera c1-6 pf-cab">En Primera Fila</h2>
</div>
<p class="st-credito pf-cred">Retrato: imagen de referencia</p>''', 'oscuro-foto', 'En Primera Fila, página 20',
 notas=(('Retrato · profundidad de campo reducida','top:40%;left:8%'),))

QA = [('¿Qué parte del trabajo no se ve en pantalla?','La preparación. Cada pieza de un minuto lleva horas de guion, prueba de sonido y edición.'),
 ('¿Qué equipo resulta imprescindible al empezar?','Un teléfono con buena estabilización, un micrófono externo y luz suave. Lo demás puede esperar.'),
 ('¿Cómo se mide si una pieza funcionó?','Por lo que la audiencia hace después: guardar, compartir o preguntar dónde conseguir algo.'),
 ('¿Qué papel tiene la tienda física en una audiencia digital?','Es donde la gente toca el equipo. La recomendación empieza en línea, pero la decisión muchas veces se toma en el mostrador.'),
 ('¿Qué hábito sostiene una carrera de creación?','Publicar con constancia y medir con honestidad. Un formato que funciona se repite; uno que no, se cambia sin nostalgia.')]
qa = ''.join(f'<p class="st-ladillo pf-q">{q}</p><p class="pf-r">«{r}»</p>' for q,r in QA)
P['21'] = pagina('21', 'recto', f'''
<div class="caja">
  <p class="st-antetitulo c1-12">Entrevista central · Edición 01</p>
  <h3 class="st-titular t48 c1-12 pf-tit">Crear contenido también es un oficio técnico</h3>
  <p class="st-entradilla c1-12 pf-entr">Método de trabajo, equipos de producción y relación con la audiencia de una creadora de contenido de tecnología, con la conversación completa en el pódcast.</p>
  <div class="st-cuerpo dos-col c1-12 pf-qa">{qa}</div>
  <blockquote class="st-destacado c1-12 pf-dest">«La recomendación empieza en línea, pero la decisión se toma en el mostrador.»</blockquote>
  <div class="c1-8 pf-qr">{bloque_qr('Acceso al episodio completo del pódcast','soytechno.com/r/e01p21a','SoyTechno · Edición 01 · pág. 21 · Simulación de QR al pódcast')}</div>
  <p class="st-credito c9-12 pf-nota">Entrevista de muestra · preguntas en forma impersonal y respuestas en cita textual</p>
</div>{folio('21','En Primera Fila')}''', '', 'En Primera Fila, página 21',
 notas=(('Preguntas · Source Serif 4 Semibold','top:46%;left:12%'),('Respuestas · cita textual entre « »','top:52%;left:56%')))

# ---------------------------------------------------------------- 28-29 · ADN Gamer (modo oscuro)
P['28'] = pagina('28', 'verso', f'''{pestana(5)}
<figure class="ag-img"><img src="{IMG['gamer']}" alt="Jugador en penumbra con luz azul ante la pantalla" loading="lazy"></figure>
<div class="caja">
  <h2 class="st-cabecera c1-12 ag-cab">ADN Gamer</h2>
  <div class="c1-12 ag-esp" aria-hidden="true"></div>
  <h3 class="st-titular negra t48 c1-12">El puesto de juego, pieza por pieza</h3>
  <p class="st-entradilla c1-10 ag-entr">Pantalla, periféricos y mobiliario definen el rendimiento tanto como el procesador gráfico. Guía de configuración por nivel de exigencia.</p>
  <p class="st-pie c1-12 ag-pie">Puesto de juego con iluminación ambiental. <span class="st-credito">Imagen de referencia</span></p>
</div>{folio('28','ADN Gamer')}''', 'oscuro', 'ADN Gamer, página 28',
 notas=(('Modo oscuro · Negro Carbón','top:3%;left:8%'),('Titular · Archivo Black en Blanco Puro','top:62%;left:8%'),('Folio · Blanco Puro 9,5 pt','bottom:7%;left:8%')))

FICHA_PJ = [('Pantalla','27 in · 165 Hz o más'),('Respuesta','1 ms (GtG)'),('Resolución','2.560 × 1.440'),('Ratón','8.000 dpi o más'),('Silla','ajuste lumbar y de brazos'),('Gama','media o alta')]
fpj = ''.join(f'<div class="fila"><span>{k}</span><b>{v}</b></div>' for k,v in FICHA_PJ)
P['29'] = pagina('29', 'recto', f'''
<div class="caja">
  <aside class="c1-6 ficha ag-ficha"><p class="st-antetitulo">Puesto de referencia · nivel competitivo</p>{fpj}</aside>
  <div class="st-cuerpo c7-12 ag-txt">
    <p>La frecuencia de actualización de la pantalla limita lo que el procesador gráfico puede mostrar: un monitor de 60 Hz no refleja más de 60 imágenes por segundo, aunque el equipo genere el doble.</p>
    <p class="st-ladillo">Periféricos</p>
    <p>En títulos competitivos, la latencia total suma la del ratón, la del sistema y la de la pantalla. Cada componente cuenta.</p>
    <p class="st-ladillo">Mobiliario</p>
    <p>Sesiones largas exigen apoyo lumbar y reposabrazos a la altura del escritorio: la postura también es rendimiento.</p>
  </div>
  <section class="c1-12 ag-agenda" aria-label="Agenda de la comunidad">
    <p class="st-antetitulo">Agenda de la comunidad · Edición 01</p>
    <ul class="st-datos"><li><b>21-ene-2027 · 18:45</b><span>Mesa de afinidad Gamer en el evento de lanzamiento</span></li>
      <li><b>21-ene-2027 · 20:20</b><span>Demostraciones en la zona de experiencia</span></li>
      <li><b>21-ene-2027 · 21:00</b><span>Sorteos con lectura NFC del ejemplar</span></li></ul>
  </section>
  <div class="c7-12 ag-qr">{bloque_qr('Acceso a ficha, precio vigente y video','soytechno.com/r/e01p29a','SoyTechno · Edición 01 · pág. 29 · Simulación de QR sobre fondo oscuro','Q')}</div>
</div>{folio('29','ADN Gamer')}''', 'oscuro', 'ADN Gamer, página 29',
 notas=(('Ficha de hardware · JetBrains Mono Medium 9,5/12,5 pt · bloque Azul Profundo','top:5%;left:12%'),('QR sobre fondo oscuro · recuadro claro · corrección Q','top:80%;left:52%')))

# ---------------------------------------------------------------- 36-37 · Espacio Business
P['36'] = pagina('36', 'verso', f'''{pestana(6)}
<div class="caja">
  <h2 class="st-cabecera c1-12">Espacio Business</h2>
  <p class="st-antetitulo c1-12 eb-ante">Infraestructura y gestión para pymes</p>
  <h3 class="st-titular t48 c1-12">La oficina que no se detiene</h3>
  <p class="st-entradilla c1-12 eb-entr">Conectividad, respaldo de datos y cobro digital: tres decisiones de infraestructura con efecto directo en la continuidad del negocio.</p>
  <div class="st-cuerpo c1-8 eb-txt">
    <p>Una interrupción de la conexión o la pérdida de un equipo detienen la facturación el mismo día. La infraestructura de una pyme se mide por el tiempo que tarda en recuperarse.</p>
    <p class="st-ladillo">Respaldo</p>
    <p>La regla de respaldo más difundida resume el criterio: tres copias de los datos, en dos soportes distintos, con una fuera de la oficina.</p>
    <p class="st-ladillo">Cobro digital</p>
    <p>El cobro con QR o por proximidad reduce el manejo de efectivo y deja registro inmediato de cada operación. La elección del medio depende del volumen de transacciones y de su compatibilidad con el sistema de facturación.</p>
  </div>
  <aside class="c9-12 eb-modulos">
    <div class="ficha"><p class="eb-n">3-2-1</p><p class="st-datos">Tres copias · dos soportes · una fuera de la oficina</p></div>
    <div class="ficha"><p class="eb-n">6 GHz</p><p class="st-datos">Wi-Fi 7 · canales de hasta 320 MHz</p></div>
    <div class="ficha"><p class="eb-n">NFC</p><p class="st-datos">Cobro por proximidad con teléfono</p></div>
  </aside>
</div>{folio('36','Espacio Business')}''', '', 'Espacio Business, página 36',
 notas=(('Fichas · Gris Platino · 4 columnas','top:52%;left:66%'),))

TB = [('Falla del equipo','Sí','Sí','Sí'),('Incidente en la oficina','No','Sí','Sí'),('Recuperación sin conexión','Sí','No','Sí'),('Control físico de los datos','Total','Del proveedor','Compartido')]
tb = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in TB)
P['37'] = pagina('37', 'recto', f'''
<div class="caja">
  <figure class="c1-6 eb-retrato"><img src="{IMG['business']}" alt="Retrato ejecutivo de referencia" loading="lazy"><figcaption class="st-credito">Imagen de referencia</figcaption></figure>
  <section class="c7-12 eb-caso">
    <p class="st-antetitulo">Caso de éxito</p>
    <blockquote class="st-destacado">«El respaldo automático dejó de ser un gasto el día que un corte eléctrico borró la facturación de una jornada.»</blockquote>
    <p class="st-credito">Gerencia de operaciones de una pyme de distribución · caso de muestra</p>
  </section>
  <section class="c1-12 eb-tabla">
    <p class="st-antetitulo">Opciones de respaldo para pymes</p>
    <table class="tb"><thead><tr><th>Protección ante…</th><th>Local</th><th>Nube</th><th>Híbrido</th></tr></thead><tbody>{tb}</tbody></table>
    <p class="st-pie">Tabla vectorial: filetes de 0,5 pt, encabezado Archivo Medium 8 pt y cebrado en Gris Platino.</p>
  </section>
</div>{folio('37','Espacio Business')}''', '', 'Espacio Business, página 37',
 notas=(('Caso de éxito · retrato y cita firmada','top:5%;left:58%'),('Tabla comparativa vectorial','top:58%;left:12%')))

# ---------------------------------------------------------------- 40-41 · Conexión en Vivo (pliego de muestra para la Edición 02)
P['40'] = pagina('40', 'verso', f'''{pestana(7)}
<div class="caja">
  <h2 class="st-cabecera c1-12">Conexión en Vivo</h2>
  <p class="st-antetitulo c1-12 cv-ante">Crónica del lanzamiento de la Edición 01 · pliego de muestra para la Edición 02</p>
  <figure class="c1-12 cv-g12"><img src="{IMG['revelacion']}" alt="Público bajo una lluvia de confeti en el momento de la revelación" loading="lazy"></figure>
  <p class="st-pie c1-4">Revelación de la portada en escena, 21-ene-2027, 19:30. <span class="st-credito">Imagen de referencia</span></p>
  <p class="st-pie c5-8">Cuenta regresiva de 120 segundos en pantalla LED, 21-ene-2027, 19:28.</p>
  <p class="st-pie c9-12">Publicación colaborativa simultánea, 21-ene-2027, 19:35.</p>
</div>{folio('40','Conexión en Vivo')}''', '', 'Conexión en Vivo, página 40',
 notas=(('Galería · módulos de 3, 6 y 12 columnas','top:16%;left:8%'),('Pies · 4 columnas · fecha «21-ene-2027»','top:80%;left:8%')))

P['41'] = pagina('41', 'recto', f'''
<div class="caja">
  <figure class="c1-6 cv-g6"><img src="{IMG['mesas']}" alt="Conversación entre invitados en una mesa de afinidad" loading="lazy"></figure>
  <figure class="c7-12 cv-g6"><img src="{IMG['microfono']}" alt="Micrófono en escena durante la conversación" loading="lazy"></figure>
  <p class="st-pie c1-6">Mesas de afinidad con anfitrión, 21-ene-2027, 18:45. <span class="st-credito">Imagen de referencia</span></p>
  <p class="st-pie c7-12">Conversación en escena grabada como pódcast en vivo, 21-ene-2027, 19:45. <span class="st-credito">Imagen de referencia</span></p>
  <figure class="c1-3 cv-g3"><img src="{IMG['publico']}" alt="Auditorio en penumbra" loading="lazy"></figure>
  <figure class="c4-6 cv-g3"><img src="{IMG['networking']}" alt="Invitados conversando en el evento" loading="lazy"></figure>
  <figure class="c7-9 cv-g3"><img src="{IMG['montaje']}" alt="Salón con mesas redondas preparado para el evento" loading="lazy"></figure>
  <figure class="c10-12 cv-g3"><img src="{IMG['podcast']}" alt="Micrófono de estudio de la cabina de contenido" loading="lazy"></figure>
  <p class="st-pie c1-6">Acreditación con el QR de la invitación desde las 18:00; rueda de negocios a las 20:20.</p>
  <p class="st-pie c7-12">Entrega de ejemplares con NFC y sorteos, 21:00. Cierre y encuesta, 22:00.</p>
</div>{folio('41','Conexión en Vivo')}''', '', 'Conexión en Vivo, página 41')

# ---------------------------------------------------------------- 44-45 · Ruta Inteligente
MATRIZ = [('Memoria','8-16 GB','16 GB','16-32 GB','16-32 GB'),('Almacenamiento','256 GB','512 GB','1 TB','1 TB'),
 ('Pantalla','13-14 in','14-16 in','16 in · color amplio','144 Hz o más'),('Prioridad','Autonomía','Teclado y cámara','Pantalla y gráficos','Refresco y refrigeración')]
mz = ''.join(f'<tr><td><b>{r[0]}</b></td>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in MATRIZ)
P['44'] = pagina('44', 'verso', f'''{pestana(8)}
<div class="caja">
  <h2 class="st-cabecera c1-12">Ruta Inteligente</h2>
  <h3 class="st-titular t48 c1-12 ri-tit">Elegir por uso, pagar por partes</h3>
  <p class="st-entradilla c1-12 ri-entr">Matriz de selección por perfil, guía de cuotas con plataformas aliadas y beneficios del Club SoyTechno.</p>
  <section class="c1-12 ri-matriz">
    <p class="st-antetitulo">Matriz de selección · cómputo portátil</p>
    <table class="tb"><thead><tr><th></th><th>Estudio</th><th>Trabajo</th><th>Creación</th><th>Juego</th></tr></thead><tbody>{mz}</tbody></table>
    <p class="st-pie">Valores de referencia por perfil de uso. Precio vigente y disponibilidad mediante QR.</p>
  </section>
  <section class="c1-12 ri-cuotas">
    <p class="st-antetitulo">Guía de cuotas con plataformas aliadas</p>
    <ol class="ri-pasos"><li><b>1</b>Elección del equipo en tienda o en línea</li><li><b>2</b>Solicitud con la plataforma aliada</li><li><b>3</b>Inicial y cuotas según condiciones vigentes</li><li><b>4</b>Retiro del equipo</li></ol>
    <p class="st-pie ri-vig">Condiciones sujetas a vigencia y a la aprobación de cada plataforma aliada; certificadas en G3.</p>
  </section>
</div>{folio('44','Ruta Inteligente')}''', '', 'Ruta Inteligente, página 44',
 notas=(('Matriz · tabla vectorial sobre Gris Platino','top:36%;left:8%'),('Leyenda de vigencia obligatoria','top:86%;left:8%')))

P['45'] = pagina('45', 'recto', f'''
<div class="caja">
  <section class="c1-12 ri-club">
    <p class="st-antetitulo">Club SoyTechno</p>
    <h3 class="st-titular t36">Puntos, niveles y un beneficio en la contraportada interior</h3>
    <ul class="ri-ben st-cuerpo"><li><b>Acumulación y canje</b> de puntos en compras en tienda y en línea.</li><li><b>Beneficios por nivel</b>, con prioridad en lanzamientos y eventos.</li><li><b>Activación del ejemplar</b> con la etiqueta NFC: beneficio canjeable una vez.</li></ul>
  </section>
  <div class="c1-6 ri-q">{bloque_qr('Afiliación al Club SoyTechno','soytechno.com/r/e01p45a','SoyTechno · Edición 01 · pág. 45 · Simulación de QR de afiliación')}</div>
  <div class="c7-12 ri-q">{bloque_qr('Condiciones de financiamiento vigentes','soytechno.com/r/e01p45b','SoyTechno · Edición 01 · pág. 45 · Simulación de QR de financiamiento')}</div>
  <section class="c1-12 ri-sedes">
    <p class="st-antetitulo">Directorio de sedes</p>
    <div class="st-datos ri-dir"><p><b>Sambil Chacao</b> Caracas · sede VIP</p><p><b>City Market</b> Caracas · sede VIP</p><p><b>Tienda en línea</b> envíos a todo el país</p><p><b>Red de tiendas</b> horarios y direcciones mediante QR</p></div>
  </section>
  <p class="st-pie c1-12">Toda mención de descuentos, cuotas o beneficios se publica con leyenda de vigencia.</p>
</div>{folio('45','Ruta Inteligente')}''', '', 'Ruta Inteligente, página 45',
 notas=(('Variantes de microtexto QR · MAN-ID §9.1','top:52%;left:12%'),('Directorio · estilo Datos','top:72%;left:12%')))

# ---------------------------------------------------------------- 48 · Última Página  +  C3 · Autopromoción con zona NFC
P['48'] = pagina('48', 'verso', f'''{pestana(9)}
<div class="caja">
  <h2 class="st-cabecera c1-12">Última Página</h2>
  <h3 class="st-titular t36 c1-12 up-tit">La próxima pantalla</h3>
  <div class="st-cuerpo dos-col c1-12 up-txt">
    <p>La siguiente transformación de la tecnología de consumo no se medirá en pulgadas ni en megapíxeles, sino en el trabajo que cada equipo resuelve sin intervención: ordenar la agenda, traducir una llamada, recordar una garantía.</p>
    <p>Esa transición exige criterio de compra. Elegir por uso, comprobar en pruebas reales y acceder con facilidades claras es la razón de ser de esta revista, edición tras edición.</p>
    <p>La revista acompaña esa transición con un compromiso verificable: cada cifra con su fuente, cada reseña con su prueba y cada condición de compra con su vigencia.</p>
    <p class="up-firma">Dirección Editorial · SoyTechno</p>
  </div>
  <div class="c1-6 up-qr">{bloque_qr('Suscripción a la edición digital','soytechno.com/revista','SoyTechno · Edición 01 · pág. 48 · Simulación de QR de suscripción')}</div>
  <aside class="c7-12 up-adelanto">
    <p class="st-antetitulo">Próxima edición</p>
    <p class="up-ed">Edición 02</p>
    <p class="st-datos">Marzo-abril 2027 · movilidad, fotografía móvil y creadores de viaje · Día D 11-mar-2027</p>
  </aside>
</div>{folio('48','Última Página')}''', '', 'Última Página, página 48',
 notas=(('Columna firmada · cargo directivo','top:22%;left:8%'),('Adelanto sin portada ni personaje','top:74%;left:52%')))

P['C3'] = pagina('C3', 'recto', f'''
<div class="caja">
  <p class="st-antetitulo c1-12">SoyTechno digital</p>
  <h2 class="st-titular negra t48 c1-12 c3-tit">Esta revista también se lee en el teléfono</h2>
  <p class="st-entradilla c1-10 c3-entr">La etiqueta NFC de esta página abre la edición digital, el pódcast y el video detrás de cámaras, y activa un beneficio del Club SoyTechno canjeable una vez.</p>
  <ol class="c1-12 c3-pasos"><li><b>1</b>Desbloquear el teléfono</li><li><b>2</b>Acercar la parte superior del teléfono a la zona de contacto</li><li><b>3</b>Abrir el enlace: edición digital, pódcast y beneficio del Club</li></ol>
</div>
<div class="nfc-zona" aria-label="Zona de contacto NFC de 40 por 40 milímetros">
  <p class="nfc-rot"><span class="nfc-n" aria-hidden="true">NFC</span>Zona de contacto NFC</p>
  <span class="nfc-guia" aria-hidden="true"></span><span class="nfc-etq" aria-hidden="true"></span>
</div>
<div class="nfc-qr">{bloque_qr('Acceso a la edición digital, al pódcast y al beneficio del Club SoyTechno','soytechno.com/revista','SoyTechno · Edición 01 · C3 · Simulación del QR equivalente a la zona NFC')}</div>
<p class="c3-pie st-datos">Etiqueta NTAG213 de 25 mm · sin datos personales · escritura bloqueada</p>''', 'platino', 'Contraportada interior C3 con zona de contacto NFC',
 notas=(('Zona NFC · 40 × 40 mm · ≥ 30 mm del lomo · ≥ 20 mm de los cortes','top:56%;left:12%'),('QR equivalente adyacente a la derecha','top:56%;left:58%')))

# ---------------------------------------------------------------- C4 · Contraportada (pauta)
P['C4'] = pauta('C4', 'verso', 'Contraportada C4', 'Marca aliada de línea blanca o televisión · rótulo «Publicidad» · sin precios impresos', 'C4 · 210 × 280 mm')

ORDEN = [['C1'], ['C2','01'], ['02','03'], ['04','05'], ['08','09'], ['16','17'], ['20','21'], ['28','29'], ['36','37'], ['40','41'], ['44','45'], ['48','C3'], ['C4']]
NOMBRES = ['C1 · Portada','C2-01 · Doble premium','02-03 · Sumario y créditos','04-05 · Pulso Techno','08-09 · Bajo el Lente','16-17 · Reportaje Central',
 '20-21 · En Primera Fila','28-29 · ADN Gamer','36-37 · Espacio Business','40-41 · Conexión en Vivo','44-45 · Ruta Inteligente','48-C3 · Última Página y zona NFC','C4 · Contraportada']

if __name__ == '__main__':
    css = open(os.path.join(AQUI, 'revista.css'), encoding='utf-8').read() + open(os.path.join(AQUI, 'revista-paginas.css'), encoding='utf-8').read()
    pliegos = ''.join(f'<figure class="banco-pliego" id="p{i}"><figcaption>{NOMBRES[i]}</figcaption><div class="banco-par n{len(p)}">' + ''.join(P[x] for x in p) + '</div></figure>' for i, p in enumerate(ORDEN))
    fuentes = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400..900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
    banco = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Banco de páginas · SoyTechno Edición 01</title>{fuentes}
<style>{css}
body{{margin:0;background:#C9CCD2;font-family:Archivo,sans-serif}} .banco{{display:grid;gap:48px;padding:40px}}
.banco-pliego{{margin:0}} .banco-pliego figcaption{{font:600 14px/1 Archivo;margin:0 0 10px;color:#0D0E12}}
.banco-par{{display:grid;grid-template-columns:repeat(2,1fr);width:min(100%,1400px);box-shadow:0 20px 50px rgba(13,14,18,.25)}} .banco-par.n1{{grid-template-columns:1fr;width:min(50%,700px)}}
.barra{{position:sticky;top:0;z-index:50;background:#0D0E12;color:#fff;padding:10px 40px;font:500 14px Archivo}} .barra button{{font:inherit;margin-left:12px}}
</style></head><body><div class="barra">Banco de páginas · Edición 01 <button onclick="document.querySelector('.revista').classList.toggle('reticula')">Ver retícula</button></div>
<main class="banco revista{' reticula' if '--reticula' in sys.argv else ''}">{pliegos}</main></body></html>'''
    open(os.path.join(AQUI, 'revista-paginas.html'), 'w', encoding='utf-8').write(banco)
    open(os.path.join(AQUI, 'revista-fragmento.html'), 'w', encoding='utf-8').write('\n'.join(P[x] for p in ORDEN for x in p))
    print('páginas:', sum(len(p) for p in ORDEN), '· pliegos:', len(ORDEN))
