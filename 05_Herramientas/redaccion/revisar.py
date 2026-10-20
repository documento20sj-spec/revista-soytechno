#!/usr/bin/env python3
"""Verificador de estructura y redacción de los documentos Markdown del corpus SoyTechno.
Uso: python3 revisar.py archivo.md [más archivos]
Salida: incidencias por línea y «Verificación: sin incidencias» cuando no hay ninguna."""
import os, re, sys

CODIGOS = {'DIR-ED-ST-2026-01','IND-ED-ST-2026-01','MAN-ID-ST-2026-01','GUI-PP-ST-2026-01','PRO-PR-ST-2026-01',
 'KIT-CO-ST-2026-01','REG-LG-ST-2026-01','CAL-ED-ST-2027-01','PRO-RP-ST-2026-01','MAN-EV-ST-2026-01',
 'GUI-NW-ST-2026-01','GUI-CR-ST-2026-01','MAN-EX-ST-2026-01','EXP-ID-ST-2026-01','PLA-FI-ST-2027-01',
 'MAN-OR-ST-2026-01','MAN-MD-ST-2026-01','PLA-CM-ST-2027-01','PLA-DI-ST-2027-01','PLI-PV-ST-2026-01'}
SECC = {f'{u}.{s}' for u, n in ((1,5),(2,6),(3,7),(4,5),(5,5)) for s in range(1, n+1)}
CAMPOS = ['Código','Versión · fecha','Documento base','Clasificación','Responsable','Colaboración',
          'Aprobación','Base en el rector','Estándar de redacción']

PROHIBIDO = [
 (r'esta de show|carel[iy]s|eljuri|revista carelis', 'Nombre de tercero o antecedente no admitido'),
 (r'\bbnc\b|banco nacional de cr[eé]dito|marca compartida|co-?branded', 'Entidad bancaria o tarjeta de marca compartida'),
 (r'\.claude\b|construir\.py|revisar\.py|imprenta-pdf|design-md|\bclaude\b|\bsonnet\b|\bopus\b|chatgpt|\bgemini\b|copilot|midjourney|agentes? de ia', 'Herramienta o entorno de trabajo'),
 (r'por definir|a definir|\btbd\b|a confirmar|por confirmar|\bborrador|preliminar\b|\bpendientes?\b', 'Marca de borrador o carencia'),
 (r'\brecomendad[oa]s?\b|\brecomendable|auto-?auditor', 'Término de estado no normativo'),
 (r'versi[oó]n anterior|sustituye a la versi|reemplaza a la versi|cambio de idea', 'Referencia a versiones o discusiones previas'),
 (r'\$|\\text|\\frac|\blatex\b', 'Signo «$» o notación de fórmulas'),
 (r'(?-i:\bNodo\b)|SoyTechno Revista|nombre candidato|candidatos? de (nombre|cabecera)|cabecera aprobada conforme', 'Denominación alternativa: la revista se llama SoyTechno'),
 (r'[◆→←⇒⇨➜✓✔✗★☆•]', 'Símbolo no admitido'),
 (r'\bO-\d\d\b', 'Etiqueta de observación'),
 (r'</?[a-zA-Z][^>]*>', 'Etiqueta HTML no admitida'),
 (r'\b(Soytechno|SOYTECHNO|Soy Techno|soyTechno)\b', 'Grafía de marca: «SoyTechno»'),
 (r'\b(el mejor|la mejor|los mejores|las mejores|incre[ií]bles?|imperdibles?|revolucionari[oa]s?)\b', 'Lenguaje de venta'),
]
PERSONA = r'\b(nosotros|nosotras|nuestr[oa]s?|usted|ustedes|vosotros|tú|tu|tus|ti|contigo|te|yo|me|mi|mis|conmigo)\b'
IMPERATIVO = r'\b(escanea|escan[eé]al[oa]|visítanos|descubre|aprovecha|participa|reg[ií]strate|inscr[ií]bete|s[ií]guenos|cont[aá]ctanos|escr[ií]benos|ll[aá]manos|haz|toca|pulsa|obt[eé]n|disfruta|conoce|accede|ingresa|comparte|recuerda|aseg[uú]rate|acerca tu|acerque|acercar tu)\b'
VERBOS = (r'\b(establecen?|definen?|regulan?|aprueban?|reciben?|verifican?|coordinan?|supervisan?|garantizan?|aseguran?|'
 r'gestionan?|elaboran?|incluyen?|contienen?|describen?|permiten?|operan?|realizan?|deben?|pueden?|tienen?|requieren?|'
 r'corresponden?|validan?|revisan?|env[ií]an?|publican?|registran?|controlan?|asumen?|cubren?|utilizan?|usan?|implican?|'
 r'suponen?|representan?|constituyen?|aplican?|comprenden?|disponen?|necesitan?|ofrecen?|generan?|facilitan?|proporcionan?|'
 r'brindan?|indican?|señalan?|muestran?|exigen?|abarcan?|forman|integran|participan|firman|entregan|presentan|activan|fijan|'
 r'es|son|está|están|fue|fueron|eran|sea|sean|hay|había)\b')
FUTURO = r'\b[a-záéíóúñ]{2,}rán?\b'
SUBORD = r'\b(que|cuando|donde|quien|quienes|cuyo|cuya|cuyos|cuyas)\b'

def limpiar(linea):
    linea = re.sub(r'`[^`]*`', ' CODIGO ', linea)
    return linea

def revisar(ruta):
    inc = []
    def add(n, tipo, msg, frag=''):
        inc.append((n, tipo, msg, frag.strip()[:90]))
    txt = open(ruta, encoding='utf-8').read()
    lineas = txt.split('\n')
    base = os.path.basename(ruta)
    m = re.match(r'([A-Z]{3}-[A-Z]{2}-ST-\d{4}-\d{2})_', base)
    codigo = m.group(1) if m else None
    # ---------- Estructura ----------
    if not lineas or not lineas[0].startswith('# '):
        add(1, 'ESTRUCTURA', 'Primera línea distinta del título «# …»')
    if sum(1 for l in lineas if re.match(r'#\s', l)) != 1:
        add(1, 'ESTRUCTURA', 'Debe existir un único título de nivel 1')
    if not any(l.startswith('SoyTechno · Proyecto Editorial · ') for l in lineas[:6]):
        add(2, 'ESTRUCTURA', 'Falta la línea «SoyTechno · Proyecto Editorial · {Tipo}» tras el título')
    h2_idx = next((i for i, l in enumerate(lineas) if l.startswith('## ')), len(lineas))
    cab = lineas[:h2_idx]
    filas = [l for l in cab if l.startswith('|')]
    if not filas or not re.match(r'\|\s*Campo\s*\|\s*Valor\s*\|', filas[0]):
        add(3, 'ESTRUCTURA', 'Falta la tabla de control con encabezado «| Campo | Valor |»')
    claves = [re.split(r'\s*\|\s*', f.strip('| '))[0] for f in filas[2:]]
    if claves != CAMPOS:
        add(3, 'ESTRUCTURA', 'Campos de la tabla de control distintos de: ' + ' / '.join(CAMPOS), ' / '.join(claves))
    for f in filas[2:]:
        if f.strip('| ').startswith('Código') and codigo and codigo not in f:
            add(3, 'ESTRUCTURA', f'El código de la tabla no coincide con el archivo ({codigo})', f)
        if f.strip('| ').startswith('Versión · fecha') and '1.0 · 18 de octubre de 2026' not in f:
            add(3, 'ESTRUCTURA', 'Versión · fecha distinta de «1.0 · 18 de octubre de 2026»', f)
    for et in ('**Objeto:**', '**Alcance:**', '**Precedencia:**'):
        if not any(l.startswith(et) for l in cab):
            add(h2_idx, 'ESTRUCTURA', f'Falta el párrafo de cabecera que empieza por {et}')
    h2 = [(i, l) for i, l in enumerate(lineas) if l.startswith('## ')]
    esperado = 1
    for i, l in h2:
        mm = re.match(r'## (\d+)\. \S', l)
        if not mm or int(mm.group(1)) != esperado:
            add(i+1, 'ESTRUCTURA', f'Sección mal numerada (se espera «## {esperado}. Título»)', l)
            if mm: esperado = int(mm.group(1))
        esperado += 1
    if h2 and not re.match(r'## \d+\. Control del documento\s*$', h2[-1][1]):
        add(h2[-1][0]+1, 'ESTRUCTURA', 'La última sección debe titularse «Control del documento»', h2[-1][1])
    sec = 0; sub = 0
    for i, l in enumerate(lineas):
        mm = re.match(r'## (\d+)\.', l)
        if mm: sec = int(mm.group(1)); sub = 0; continue
        if l.startswith('### '):
            m3 = re.match(r'### (\d+)\.(\d+) \S', l)
            sub += 1
            if not m3 or int(m3.group(1)) != sec or int(m3.group(2)) != sub:
                add(i+1, 'ESTRUCTURA', f'Subsección mal numerada (se espera «### {sec}.{sub} Título»)', l)
                if m3 and int(m3.group(1)) == sec: sub = int(m3.group(2))
        if re.match(r'#{5,}\s', l):
            add(i+1, 'ESTRUCTURA', 'Nivel de título no admitido (máximo ####)', l)
    if not any(re.match(r'\|\s*Elaboración\s*\|\s*Revisión\s*\|\s*Aprobación\s*\|', l) for l in lineas[h2[-1][0]:] if h2):
        add(len(lineas), 'ESTRUCTURA', 'Falta la tabla de firmas «| Elaboración | Revisión | Aprobación |» en Control del documento')
    # ---------- Formato de bloques ----------
    en_codigo = False
    for i, l in enumerate(lineas):
        if l.startswith('```'):
            en_codigo = not en_codigo; add(i+1, 'FORMATO', 'Bloque de código no admitido en el documento'); continue
        prev = lineas[i-1] if i else ''
        if re.match(r'(- |\d+\. )', l) and prev.strip() and not re.match(r'(- |\d+\. |\s{4})', prev):
            add(i+1, 'FORMATO', 'Falta línea en blanco antes de la lista', l)
        if l.startswith('|') and prev.strip() and not prev.startswith('|'):
            add(i+1, 'FORMATO', 'Falta línea en blanco antes de la tabla', l)
        if l.startswith('>') and prev.strip() and not prev.startswith('>'):
            add(i+1, 'FORMATO', 'Falta línea en blanco antes del bloque de cita', l)
        if re.match(r' {1,3}[-*] |\t', l):
            add(i+1, 'FORMATO', 'Lista anidada con sangría distinta de cuatro espacios', l)
        if l.startswith('|') and re.match(r'\|[\s:-]+\|', l):
            cols = l.strip().strip('|').count('|') + 1
            if cols > 4:
                add(i+1, 'FORMATO', f'Tabla de {cols} columnas (máximo 4)', prev)
        if re.match(r'^(\*\*\*|---|___)\s*$', l):
            add(i+1, 'FORMATO', 'Línea horizontal no admitida', l)
        if re.search(r'!\[|\]\(http', l):
            add(i+1, 'FORMATO', 'Imagen o enlace externo no admitido', l)
    # ---------- Contenido ----------
    for i, raw in enumerate(lineas):
        n = i + 1
        if raw.startswith('|') and i < h2_idx:
            continue  # tabla de control
        l = limpiar(raw)
        for pat, msg in PROHIBIDO:
            for mm in re.finditer(pat, l, re.I if 'Soytechno' not in pat else 0):
                add(n, 'PROHIBIDO', msg, mm.group(0))
        for mm in re.finditer(PERSONA, l, re.I):
            if mm.group(0).isupper() and len(mm.group(0)) <= 3: continue
            add(n, 'REGISTRO', 'Primera o segunda persona', l[max(0, mm.start()-30):mm.end()+30])
        for mm in re.finditer(IMPERATIVO, l, re.I):
            add(n, 'REGISTRO', 'Imperativo o apelación al lector', l[max(0, mm.start()-30):mm.end()+30])
        for pat, msg in ((VERBOS, 'Verbo conjugado sin «se»'), (FUTURO, 'Futuro sin «se»')):
            for mm in re.finditer(pat, l, re.I):
                w = mm.group(0).lower()
                antes = l[:mm.start()]
                if re.search(r'\bse\s+(?:le\s+|les\s+|lo\s+|la\s+|los\s+|las\s+)?$', antes, re.I): continue
                if w == 'es' and re.match(r'\s+decir', l[mm.end():]): continue
                add(n, 'REGISTRO', msg + f': «{mm.group(0)}»', l[max(0, mm.start()-35):mm.end()+35])
        for mm in re.finditer(SUBORD, l, re.I):
            add(n, 'REGISTRO', f'Subordinada con «{mm.group(0)}»', l[max(0, mm.start()-35):mm.end()+35])
        # Cifras y unidades
        for mm in re.finditer(r'\d\s?%', l):
            if not re.match(r'\d %', mm.group(0)):
                add(n, 'CIFRAS', 'Porcentaje sin espacio («50 %»)', mm.group(0))
        for mm in re.finditer(r'(?<![\w#.,/:-])\d{4,}(?![\w.,/-])', l):
            v = mm.group(0); ctx = l[max(0, mm.start()-5):mm.start()]
            if len(v) == 4 and v.startswith(('19', '20')): continue
            if re.search(r'ISO\s*$|IEC\s*$', ctx): continue
            add(n, 'CIFRAS', 'Cifra sin punto de millares', v)
        for mm in re.finditer(r'\d\s?[xX]\s?\d', l):
            add(n, 'CIFRAS', 'Usar «×» con espacios en dimensiones', mm.group(0))
        for mm in re.finditer(r'\d\s?(a\.\s?m\.|p\.\s?m\.|am\b|pm\b)', l, re.I):
            add(n, 'CIFRAS', 'Hora en formato de 24 h', mm.group(0))
        for mm in re.finditer(r'\d(GB|MB|KB|TB|Hz|kHz|mm|cm|kg|ppp|px|pt|mAh|USD)\b', l):
            add(n, 'CIFRAS', 'Unidad sin espacio', mm.group(0))
        for mm in re.finditer(r'(\d[\d.,]*\s?(USD|US\$|dólar(es)?|bolívar(es)?|Bs\.?|VES|€|euros?)\b)|((USD|US\$|Bs\.?)\s?\d)', l, re.I):
            add(n, 'PROHIBIDO', 'Monto monetario: datos económicos solo en porcentajes', mm.group(0))
        # Códigos y referencias
        for mm in re.finditer(r'\b[A-Z]{3}-[A-Z]{2}-ST-\d{4}-\d{2}\b', raw):
            if mm.group(0) not in CODIGOS:
                add(n, 'CÓDIGOS', 'Código documental inexistente', mm.group(0))
        for mm in re.finditer(r'\b(?:DOC-E|DOC-E\d\d|PLT-DOC)-(\d\d)\b', raw):
            if not 1 <= int(mm.group(1)) <= 28:
                add(n, 'CÓDIGOS', 'Número de documento de edición fuera de 01 a 28', mm.group(0))
        for mm in re.finditer(r'§\s?(\d+\.\d+)', raw):
            if mm.group(1) not in SECC:
                add(n, 'CÓDIGOS', 'Referencia a una sección inexistente del rector', mm.group(0))
    palabras = len(re.findall(r'\w+', re.sub(r'`[^`]*`', ' ', txt)))
    return inc, palabras

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    total = 0
    for ruta in sys.argv[1:]:
        inc, pal = revisar(ruta)
        print(f'Archivo: {ruta}\nPalabras: {pal}')
        orden = ['ESTRUCTURA', 'FORMATO', 'PROHIBIDO', 'CÓDIGOS', 'CIFRAS', 'REGISTRO']
        for n, tipo, msg, frag in sorted(inc, key=lambda x: (orden.index(x[1]), x[0])):
            print(f'[{tipo}] línea {n} · {msg}' + (f' · «{frag}»' if frag else ''))
        cuenta = {}
        for _, t, _, _ in inc: cuenta[t] = cuenta.get(t, 0) + 1
        print('Resumen: ' + (' · '.join(f'{k} {v}' for k, v in cuenta.items()) if inc else '0 incidencias'))
        print('Verificación: sin incidencias' if not inc else 'Verificación: corregir y repetir')
        total += len(inc)
    sys.exit(0 if total == 0 else 2)

if __name__ == '__main__':
    main()
