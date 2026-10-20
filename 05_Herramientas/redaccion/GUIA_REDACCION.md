# Guía de redacción · Corpus documental de la Revista Corporativa SoyTechno

Guía obligatoria para redactar los documentos del catálogo del Índice Maestro IND-ED-ST-2026-01. Cada documento se entrega en **Markdown (.md)**, que es la fuente oficial. El constructor del proyecto genera a partir de él la versión **HTML** de lectura (una columna, apta para teléfono). No se generan otros formatos.

## 1. Fuentes obligatorias (leer antes de redactar)

| Fuente | Ruta (carpeta de esta guía) | Uso |
|---|---|---|
| Documento Rector (texto) | `referencias/RECTOR.txt` | Norma superior. Toda cifra, regla y nombre coincide con el rector. |
| Parámetros comunes | `PARAMETROS.md` | Cifras económicas, calendario 2027, roles, códigos, expediente DOC-E, fuente única. |
| Especificación del documento | `specs/<CÓDIGO>.md` | Ficha del índice, estructura de secciones y contenidos mínimos. |
| Investigación de soporte | `/Users/germanjaraba/Proyectos/Revista Carelis/04_Investigacion/` | Consulta opcional y selectiva. **Nunca se cita, se nombra ni se copia.** |

## 2. Registro lingüístico (obligatorio)

- Español de Venezuela, registro culto, estilo **normativo-impersonal**: estructuras nominales, infinitivos y pasiva refleja con «se». Ejemplos válidos: «Se fija…», «Entrega de materiales antes de G3», «Verificar la lectura en cuatro equipos», «Aprobación por parte de DE».
- **Prohibido**: primera persona (nosotros, nuestro), segunda persona (tú, usted, imperativos como «escanea», «visita», «descubre») y **oraciones con sujeto y verbo conjugado activo** («SoyTechno opera», «el documento establece», «la imprenta entrega», «el CE aprueba», «el plazo es de cinco días»). Reescritura nominal: «Operación de…», «Entrega por parte de la imprenta…», «Aprobación del CE…», «Plazo: cinco días».
- Evitar subordinadas con «que», «cuando», «donde», «quien», «cuyo». Alternativas: participios («equipos asignados»), preposiciones («ante filtración», «en caso de retraso», «con posterioridad a G4»), dos puntos y listas.
- Verbos conjugados admitidos solo con «se» antepuesto («se entrega», «se deberá verificar»). Futuro, «es», «son», «hay», «debe», «puede» sin «se»: prohibidos.
- Sin adjetivación hiperbólica ni lenguaje de venta («el mejor», «increíble», «imperdible», «revolucionario», «oferta», «aprovechar»).
- Extranjerismos (rector §2.6): cursiva sin equivalente de uso general (*hardware*, *software*, *router*, *streaming*, *influencer*, *networking*, *streamer*, *podcaster*); equivalente español cuando existe (pantalla, portátil, teléfono inteligente, en línea, configuración, detrás de cámaras); redonda en adaptaciones y siglas (pódcast, QLED, OLED, 4K, Wi-Fi 7, IA, NFC, QR). Denominaciones propias en redonda: Zona Gamer, ADN Gamer, Zona Business, Espacio Business.
- Cifras: unidades del Sistema Internacional con espacio (8 GB, 120 Hz, 25 mm), coma decimal (0,2 mm), punto de millares (5.000), porcentaje con espacio (50 %), multiplicación con × entre espacios (40 × 40 mm), fechas «20-nov-2026» en tablas y listas y «20 de noviembre de 2026» en prosa, horas en 24 h (19:30).
- Siglas de roles: DE, CR, DA, PF, CC, EC, PD, EV y CE; «Asesoría Legal de SoyTechno». Grafía de la marca: «SoyTechno».
- **Nombre de la revista: SoyTechno.** Denominación en los documentos: «la revista SoyTechno» o «la revista». Sin nombres alternativos ni candidatos.
- **Datos económicos solo en porcentajes.** Ningún monto en dólares, bolívares u otra moneda (tarifas, costos, presupuestos, umbrales, precios unitarios): estructuras, índices, coberturas, descuentos y condiciones en porcentaje, con los valores de PARAMETROS §8.

## 3. Contenido prohibido (el verificador lo rechaza)

- Nombres de medios, revistas, empresas o personas usados como referencia en la investigación. Solo se nombran SoyTechno, sus programas y sedes, las marcas de su catálogo citadas en el rector, Cashea, normas técnicas (ISO, FOGRA, NFC Forum, PDF/X) e instituciones (SAPI, Biblioteca Nacional de Venezuela, BCV).
- Entidades bancarias y tarjetas de crédito de marca compartida.
- Herramientas, rutas o entorno de trabajo: asistentes o modelos de IA, scripts, carpetas locales, «Claude», «agente».
- Marcas de borrador o carencia: «por definir», «pendiente», «TBD», «a confirmar», «borrador», «preliminar», «recomendado», historial de versiones, referencias a versiones anteriores o a discusiones previas.
- Montos en cualquier moneda; fórmulas con signos «$» o notación LaTeX; emoji; flechas; símbolos decorativos.
- Datos inventados presentados como hechos verificados. Una estimación se presenta como «valor de referencia» con su base; una decisión normativa, como decisión («Se fija…»).
- Nombres de proveedores, herramientas de software o plataformas comerciales no citados en el rector o en PARAMETROS (descripción genérica: «plataforma de enlaces de SoyTechno», «herramienta de analítica web del comercio electrónico»).

## 4. Plantilla Markdown obligatoria

```markdown
# {Título completo del documento}

SoyTechno · Proyecto Editorial · {Tipo documental}

| Campo | Valor |
|---|---|
| Código | `{CÓDIGO}` |
| Versión · fecha | 1.0 · 18 de octubre de 2026 |
| Documento base | `DIR-ED-ST-2026-01` · `IND-ED-ST-2026-01` |
| Clasificación | {Clasificación} |
| Responsable | {R con denominación completa} |
| Colaboración | {C} |
| Aprobación | {A} |
| Base en el rector | {§…} |
| Estándar de redacción | Normativo-impersonal · cero redundancia |

**Objeto:** {una o dos frases nominales}

**Alcance:** {a quién y a qué se aplica}

**Precedencia:** Documento Rector e Índice Maestro sobre este documento; referencias al rector con el símbolo §.

## 1. {Título de la sección}

{Párrafo de entrada opcional.}

### 1.1 {Subsección}

{Contenido.}

## N. Control del documento

### N.1 Relación con otros documentos

{Contenidos de los que este documento es fuente única y remisiones a otros documentos.}

### N.2 Revisión y actualización

{Periodicidad, disparadores de revisión, responsable y registro.}

### N.3 Firmas

| Elaboración | Revisión | Aprobación |
|---|---|---|
| {R} · nombre, cargo y fecha | Nombre, cargo y fecha | {A} · fecha |
```

Reglas de formato:

- Un solo título `#` en la primera línea. Secciones `## N. Título` numeradas de forma consecutiva desde 1; subsecciones `### N.M Título` consecutivas dentro de cada sección. Niveles `####` admitidos para fichas o elementos; sin niveles inferiores.
- La última sección se titula exactamente «Control del documento» y contiene la tabla de firmas con las columnas Elaboración, Revisión y Aprobación.
- Tablas con encabezado y **cuatro columnas como máximo**, sin el carácter «|» dentro de las celdas. Una línea en blanco antes y después de cada tabla, lista o bloque de cita.
- Listas con «-» o «1.»; sin listas anidadas (si son imprescindibles, sangría de cuatro espacios).
- Negrita para etiquetas al inicio de un elemento («**Plazo:** …»); cursiva solo para extranjerismos y títulos de obras; acento grave para códigos (`DOC-E-07`, `GUI-PP-ST-2026-01`).
- Notas destacadas en bloque de cita: `> **Nota:** …`.
- Sin HTML, sin imágenes, sin enlaces externos, sin notas al pie, sin líneas horizontales.
- Modelos de texto (cláusulas, avisos, microtextos) como bloque de cita o lista, siempre en registro impersonal.

## 5. Calidad profesional exigida

- Desarrollo completo de la ficha del índice y de la especificación: procedimientos, responsables (siglas de rol), plazos ligados a compuertas (G0 a G5) y semanas (S1 a S8), criterios de aceptación, registros asociados (DOC-E-NN) y fechas de 2027 tomadas de PARAMETROS.
- Coherencia exacta con el rector y con PARAMETROS. Cero redundancia: el contenido de otro documento se cita por código («conforme a GUI-PP-ST-2026-01», «modelo en REG-LG») sin reproducirlo.
- Extensión: la indicada en la especificación. Densidad técnica, sin relleno ni introducciones genéricas.
- Tablas solo cuando aportan comparación; fichas con `####` y listas para elementos repetidos.

## 6. Flujo de trabajo y autocontrol

1. Leer `GUIA_REDACCION.md`, `PARAMETROS.md`, `RECTOR.txt` y `specs/<CÓDIGO>.md`.
2. Escribir el documento en la ruta indicada por la especificación (UTF-8). **No modificar ni crear ningún otro archivo del proyecto**, salvo el HTML que genera el constructor.
3. Ejecutar el verificador y corregir **todo** lo que marque:

    python3 "<carpeta de esta guía>/revisar.py" "<ruta del .md>"

4. Generar el HTML:

    cd "/Users/germanjaraba/Proyectos/Revista Carelis" && python3 05_Herramientas/construir.py <CÓDIGO>

5. Repetir 3 y 4 hasta obtener «Verificación: sin incidencias» y el HTML generado sin errores.
6. Informe final breve (máximo 150 palabras): ruta del .md, palabras, resultado del verificador, decisiones normativas tomadas por criterio propio e inconsistencias detectadas en el rector o en PARAMETROS (sin corregirlas).
