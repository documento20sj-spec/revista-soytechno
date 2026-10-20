#!/usr/bin/env python3
"""Actualiza el cuerpo del Índice Maestro tras la emisión de los 18 documentos del corpus."""
import glob, os, re, shutil
RAIZ = '/Users/germanjaraba/Proyectos/Revista Carelis'
SRC = os.path.join(RAIZ, '05_Herramientas/src/indice_maestro.body.html')
shutil.copy(SRC, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'referencias', 'indice.antes_emision.html'))
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a[:80], c)
    s = s.replace(a, b)
docs = sorted(glob.glob(os.path.join(RAIZ, '02_Corpus_Documental', '*', '*', '*_v1.md')))
assert len(docs) == 18, len(docs)
for ruta in docs:
    cod = os.path.basename(ruta).split('_')[0]
    md = open(ruta, encoding='utf-8').read()
    base = re.search(r'^\| Base en el rector \| (.*?) \|$', md, re.M).group(1).strip()
    carpeta = os.path.relpath(os.path.dirname(ruta), os.path.join(RAIZ, '02_Corpus_Documental'))
    i = s.find(f'<span class="cod">{cod}</span>')
    assert i > 0, cod
    j = s.find('</div>', s.find('<p><b>Contenido y alcance:</b>', i)) + 6
    f = s[i:j]
    f2 = f.replace('<span class="chip prog">Programado</span>', '<span class="chip vig">Vigente</span>')
    f2 = re.sub(r'<li><b>Base en el rector</b>.*?</li>', f'<li><b>Base en el rector</b>{base}</li>', f2)
    f2 = re.sub(r'<li><b>Fecha meta</b>.*?</li>', '<li><b>Emisión</b>18-oct-2026 · v1.0</li>', f2)
    f2 = re.sub(r'<li><b>Ubicación</b>.*?</li>',
                f'<li><b>Ubicación</b><span class="mono">{carpeta}</span></li><li><b>Formatos</b>Markdown (fuente) · HTML</li>', f2)
    assert f2 != f and 'Vigente' in f2, cod
    s = s[:i] + f2 + s[j:]
# Documento Rector
rep('<li><b>Fecha meta</b>Emisión 18-oct-2026</li><li><b>Ubicación</b><span class="mono">01_Documento_Rector</span></li>',
    '<li><b>Emisión</b>18-oct-2026 · v1.0</li><li><b>Ubicación</b><span class="mono">01_Documento_Rector</span></li><li><b>Formatos</b>HTML · PDF</li>')
# Convenciones
rep('en documentos de edición; patrón de §4.5 del rector en archivos de producción.</td></tr>',
    'en documentos de edición; patrón de §4.5 del rector en archivos de producción.</td></tr>\n'
    '<tr><td class="k">Formatos</td><td>Markdown como fuente oficial y HTML de lectura en los documentos de los Bloques I a III; HTML y PDF en el Documento Rector y en este índice.</td></tr>')
rep('<td>Documento emitido y de aplicación: DIR-ED-ST-2026-01 e IND-ED-ST-2026-01.</td>',
    '<td>Documento emitido y de aplicación: Documento Rector, Índice Maestro y los dieciocho documentos de los Bloques I a III (emisión del 18-oct-2026).</td>')
rep('<td>Documento en desarrollo conforme a la ruta de implementación por fases (sección 6), con responsable y fecha meta.</td>',
    '<td>Plantilla del expediente por edición en desarrollo conforme a la ruta de la sección 6, con responsable y fecha meta.</td>')
# Ruta por fases
rep('<h3><span class="num">6.3</span>Ruta de implementación por fases</h3>',
    '<h3><span class="num">6.3</span>Ruta de implementación y dependencias</h3>')
rep('<p class="intro">Elaboración ordenada y sin solapamientos, con disponibilidad de cada documento antes de su fase de uso en la Edición 01.</p>',
    '<p class="intro">Corpus de los Bloques I a III emitido el 18-oct-2026 (v1.0), con aplicación en el orden de dependencias de las fases 0 a 4; plantillas del expediente por edición con fecha meta anterior a su fase de uso en la Edición 01.</p>')
for a in ['<div class="meta">Fecha meta 30-oct-2026</div>', '<div class="meta">Fechas meta 06 a 13-nov-2026</div>',
          '<div class="meta">Fechas meta 13 a 20-nov-2026</div>', '<div class="meta">Fechas meta 27-nov a 04-dic-2026</div>',
          '<div class="meta">Fechas meta 11-dic-2026 a 08-ene-2027</div>']:
    rep(a, '<div class="meta">Vigente · emisión 18-oct-2026</div>')
for a, b in [(' · Nombre y cabecera · 30-oct', ' · Nombre y cabecera'), (' · Plan económico · 30-oct', ' · Plan económico'),
             (' · Calendario editorial 2027 · 30-oct', ' · Calendario editorial 2027'), (' · Kit comercial · 06-nov', ' · Kit comercial'),
             (' · Zonas de experiencia · 06-nov', ' · Zonas de experiencia'), (' · Compendio legal · 06-nov', ' · Compendio legal'),
             (' · Pliegos de proveedores · 06-nov', ' · Pliegos de proveedores'), (' · Organización y Consejo Editorial · 13-nov', ' · Organización y Consejo Editorial'),
             (' · Creadores y personaje de portada · 13-nov', ' · Creadores y personaje de portada'),
             (' · Producción del evento · 13-nov; completo 07-dic', ' · Producción del evento'),
             (' · Identidad y estilo · 20-nov', ' · Identidad y estilo'), (' · Laboratorio y fotografía · 20-nov', ' · Laboratorio y fotografía'),
             (' · Pre-prensa e integración phygital · 27-nov; completo 14-dic', ' · Pre-prensa e integración phygital'),
             (' · Medición e indicadores · 04-dic', ' · Medición e indicadores'), (' · Networking y rueda de negocios · 11-dic', ' · Networking y rueda de negocios'),
             (' · Revelación de portada · 18-dic', ' · Revelación de portada'), (' · Canales digitales y difusión · 18-dic', ' · Canales digitales y difusión'),
             (' · Distribución y sedes VIP · 08-ene', ' · Distribución y sedes VIP')]:
    rep(a, b)
# Reglas de control documental
rep('<li><b>Nomenclatura:</b> códigos y nombres de archivo conforme a 1.1.</li>',
    '<li><b>Nomenclatura:</b> códigos y nombres de archivo conforme a 1.1.</li>\n'
    '<li><b>Formatos:</b> fuente oficial en Markdown y versión HTML generada a partir de ella en los Bloques I a III; ninguna edición manual del HTML.</li>')
# Denominación SoyTechno y datos económicos en porcentajes
rep('<p><b>Propósito:</b> Definición y protección legal del nombre de la revista y de su cabecera.</p>',
    '<p><b>Propósito:</b> Adopción y protección legal de la denominación SoyTechno y de su cabecera.</p>')
rep('<p><b>Contenido y alcance:</b> Propuestas de nombre y criterios de evaluación; búsqueda de antecedentes registrales y de dominios; decisión del Consejo Editorial; solicitud de registro ante el SAPI en las clases 16, 35 y 41; dominio, micrositio y cuentas digitales; base del logotipo de cabecera (MAN-ID), de la mancheta, del ISSN y del depósito legal (REG-LG).</p>',
    '<p><b>Contenido y alcance:</b> Denominación de la revista, SoyTechno, y sus fundamentos; cabecera derivada del logotipo corporativo; verificación de la cobertura registral de la marca SoyTechno en las clases 16, 35 y 41 y solicitudes ante el SAPI; ratificación del Consejo Editorial; dominio, micrositio y cuentas digitales; base de la cabecera (MAN-ID), de la mancheta, del ISSN y del depósito legal (REG-LG).</p>')
rep('tarifas por posición y paquete en dólares sobre la base de PLA-FI, con condiciones de pago, reserva y cancelación;',
    'propuesta comercial individual sobre la base tarifaria de PLA-FI, con condiciones de pago, reserva, descuentos y cancelación;')
rep('<p><b>Contenido y alcance:</b> Estructura de costos de impresión, etiquetas NFC, producción editorial y audiovisual, equipo, distribución y eventos; ingresos por posición publicitaria, paquete y patrocinio; punto de equilibrio por edición;',
    '<p><b>Contenido y alcance:</b> Estructura porcentual de costos de impresión, etiquetas NFC, producción editorial y audiovisual, equipo, distribución y eventos; índice tarifario e ingresos por posición publicitaria, paquete y patrocinio; punto de equilibrio y escenarios de cobertura por edición;')
rep('<b>Dependencia determinante:</b> Nombre de la cabecera para el ISSN y la portada;',
    '<b>Dependencia determinante:</b> Cabecera SoyTechno y cobertura registral para el ISSN y la portada;')
rep('<li><b>Fuente única:</b>',
    '<li><b>Datos económicos:</b> expresión en porcentajes en los documentos del corpus; montos solo en los registros de cada edición (DOC-E-04, DOC-E-13, DOC-E-26) y en las propuestas comerciales individuales.</li>\n<li><b>Fuente única:</b>')
# Ajustes de registros de edición detectados en la revisión
rep('<span class="cod">DOC-E-10</span><span class="tit">Catálogo fotográfico y audiovisual</span></div><ul class="datos"><li><b>R</b>PF</li><li><b>C</b>DA</li><li><b>A</b>DE</li>',
    '<span class="cod">DOC-E-10</span><span class="tit">Catálogo fotográfico y audiovisual</span></div><ul class="datos"><li><b>R</b>PF</li><li><b>C</b>CR</li><li><b>A</b>DA</li>')
rep('<li><b>Compuerta</b>G1 · G3</li></ul><p>Verificación previa de creadores e invitados y acuerdos firmados por personaje, imprenta y proveedores.</p>',
    '<li><b>Compuerta</b>G0 a G3</li></ul><p>Verificación previa del personaje de portada antes de G0 y de creadores e invitados antes de su invitación; acuerdos firmados por personaje, imprenta y proveedores, verificados en G3.</p>')
open(SRC, 'w', encoding='utf-8').write(s)
print('Índice actualizado:', s.count('chip vig'), 'documentos vigentes ·', s.count('chip prog'), 'programados')
