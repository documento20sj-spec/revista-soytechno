# Manual de Identidad Editorial, Retícula y Estilo Lingüístico

SoyTechno · Proyecto Editorial · Manual

| Campo | Valor |
|---|---|
| Código | `MAN-ID-ST-2026-01` |
| Versión · fecha | 1.0 · 18 de octubre de 2026 |
| Documento base | `DIR-ED-ST-2026-01` · `IND-ED-ST-2026-01` |
| Clasificación | Uso interno · difusión a diseño, redacción y proveedores creativos |
| Responsable | DA · Dirección de Arte y Maquetación |
| Colaboración | EC · Edición de Cierre y Corrección; CR · Coordinación de Redacción y Especialistas Tech |
| Aprobación | DE · Dirección Editorial |
| Base en el rector | §2.5, §2.6, §3.2 a §3.6 |
| Estándar de redacción | Normativo-impersonal · cero redundancia |

**Objeto:** sistema gráfico y lingüístico de la revista: retícula, tipografía, color, cabecera y portada, plantillas por sección, estilo de redacción y glosario normativo.

**Alcance:** aplicación obligatoria a diseño, redacción, corrección y proveedores creativos en las Ediciones 01 a 06.

**Precedencia:** Documento Rector e Índice Maestro sobre este documento; referencias al rector con el símbolo §.

## 1. Principios del sistema editorial

Sistema único para el impreso y la edición digital, con valores de retícula, tipografía y color iguales a los de §3.2 a §3.4.

### 1.1 Principios

- **Objeto coleccionable:** revista de 52 páginas (*bookazine*): 48 interiores y 4 de cubierta, en 210 × 280 mm.
- **Jerarquía clara:** cuatro niveles de lectura por página (titular, entradilla, cuerpo y apoyo de datos); sin elemento decorativo sin función.
- **Aire:** área libre mínima del 25 % por doble página (29.400 mm² sobre los 117.600 mm² del formato abierto), medida en páginas editoriales con pauta excluida.
- **Marca única:** la revista SoyTechno, con cabecera derivada del logotipo corporativo; azul institucional y logotipo conforme al manual de identidad corporativa (insumo de Mercadeo SoyTechno al 30-oct-2026).
- **Identificación del editor:** leyenda «Una publicación de SoyTechno» en portada y mancheta.
- **Separación editorial-comercial:** pauta y publirreportaje diferenciados de la diagramación editorial (§2.5).

### 1.2 Verificación por compuertas

Aplicación de los valores por DA en las plantillas de maquetación; archivos de diseño de cada edición en `DOC-E-12`. Verificación de identidad y estilo en cada ciclo, con las fechas de la Edición 01 como referencia y las de las demás ediciones conforme a `CAL-ED-ST-2027-01`.

| Compuerta (Ed. 01) | Verificación | Responsable | Registro |
|---|---|---|---|
| G0 · 20-nov-2026 | Portada con alternancia de persona y producto; mapa de paginación con aperturas, áreas libres y modo oscuro en 26-35 | DE · DA | `DOC-E-01`, `DOC-E-03` |
| G1 · 11-dic-2026 | Textos con firma, fotografías con crédito y fichas de reseña en estilo Datos, sin precio | CR · PF | `DOC-E-06`, `DOC-E-10` |
| G2 · 08-ene-2027 | Páginas conformes a retícula, línea base y tabla de estilos; sin viudas ni huérfanas; glosario aplicado en la doble corrección; sumario coincidente con títulos y páginas | DA · EC | `DOC-E-09`, `DOC-E-12` |
| G3 · 08-ene-2027 | Rótulo de pauta, publirreportaje conforme a la plantilla, separación de cuatro páginas y ausencia de precios | CC | `DOC-E-13`, `DOC-E-14` |
| G4 · 12-ene-2027 | Archivo de imprenta con zona de cabecera, zona de contacto NFC en C3, texto calado desde 9,5 pt y QR verificados sobre el ferro | DA | `DOC-E-15`, `DOC-E-16` |

Criterio de aceptación: cero incidencias abiertas al cierre de cada compuerta; incidencias y correcciones registradas en `DOC-E-05`.

### 1.3 Desviaciones

Desviación de cualquier valor del manual: aprobación escrita de DE y registro en `DOC-E-05`.

## 2. Formato, márgenes y retícula

### 2.1 Formato y márgenes

| Parámetro | Valor | Comprobación |
|---|---|---|
| Formato | 210 × 280 mm vertical; abierto 420 × 280 mm | Relación 3:4 |
| Sangrado | 3 mm perimetral | — |
| Márgenes | Interior 18 mm · exterior 15 mm · superior 15 mm · inferior 20 mm | 18 + 177 + 15 = 210 mm · 15 + 245 + 20 = 280 mm |
| Caja de texto | 177 × 245 mm | — |
| Zona del lomo | Texto, rostros, logotipos y códigos a 10 mm o más del lomo | Margen interior de 18 mm |
| Imágenes a doble página | Compensación de 3 mm por lado en la zona del lomo | Parámetros en `GUI-PP-ST-2026-01` |

### 2.2 Retícula de 12 columnas

Doce columnas de 11,08 mm con medianil de 4 mm: 12 × 11,08 + 11 × 4 = 176,96 mm, equivalentes a los 177 mm de la caja (diferencia de 0,04 mm por redondeo del ancho de columna).

| Combinación | Columnas de retícula por columna | Ancho de columna | Uso |
|---|---|---|---|
| 2 columnas | 6 | 86,48 mm | Ensayos |
| 3 columnas | 4 | 56,32 mm | Reseñas |
| 4 columnas | 3 | 41,24 mm | Breves y fichas |

Medianil de 4 mm constante en todas las combinaciones.

### 2.3 Línea base de 12,5 pt

- **Retícula de líneas base:** 12,5 pt (4,41 mm) con origen en el margen superior; 55 líneas completas por caja (687,5 pt; 242,5 mm), con remanente de 2,5 mm al pie.
- **Alineación:** todo texto sobre la línea base; interlineado en múltiplos de 12,5 pt o de 18,75 pt (1,5 líneas), este último con bloques de número par de líneas.
- **Estilos con interlineado distinto:** datos (10 pt) y pies (9,5 pt) con la primera línea anclada a la retícula y cierre del bloque en el múltiplo inmediato de 12,5 pt; bloques de datos de cinco líneas (50 pt) equivalentes a cuatro líneas base.
- **Imágenes y filetes:** alturas en múltiplos de 12,5 pt; anchos en columnas de retícula.
- **Portada:** caja, márgenes y columnas vigentes (sección 5).

## 3. Tipografía y hojas de estilo

### 3.1 Familias

Tres familias de licencia abierta (SIL OFL), incrustables sin licenciamiento adicional: Archivo (titulares, rótulos y folios), Source Serif 4 (texto) y JetBrains Mono (datos).

### 3.2 Tabla de estilos

| Estilo | Familia y peso | Cuerpo/interlineado | Uso |
|---|---|---|---|
| Antetítulo | Archivo Medium | 9/12,5 pt | Tema o sección sobre el titular |
| Titular | Archivo Bold o Black | 24 a 60 pt; interlineado en múltiplos de 12,5 pt (25 a 62,5 pt); *tracking* −15 desde 24 pt | Aperturas y piezas interiores; Black en aperturas de sección |
| Subtítulo o entradilla | Source Serif 4 Semibold | 13/18,75 pt | Resumen bajo el titular, de una a cuatro líneas |
| Cuerpo | Source Serif 4 Regular; Italic para extranjerismos y títulos de obras | 9,5/12,5 pt | Texto corrido |
| Destacado | Source Serif 4 Italic | 18/25 pt | Cita entre « »; uno por doble página como máximo |
| Ladillo | Source Serif 4 Semibold | 9,5/12,5 pt | Intertítulo con una línea base de separación previa |
| Pie de foto | Source Serif 4 Italic | 7,5/9,5 pt | Descripción nominal de la imagen, en Gris Texto |
| Crédito | Source Serif 4 Regular en versalitas | 6,5/9,5 pt | Autoría de fotografía e ilustración, en Gris Texto |
| Datos | JetBrains Mono Regular y Medium | 8/10 pt; mínimo 7,5 pt | Fichas, tablas y códigos; cifras tabulares |
| Folio | Archivo Medium | 7 pt | Número de página y nombre de sección, en mayúsculas |
| Cabecera de sección | Archivo Black | 24/25 pt | Nombre de sección en la primera página, en mayúsculas |

### 3.3 Reglas

- **Alineación:** justificado con partición controlada a 2 columnas; bandera izquierda a 3 y 4 columnas.
- **Partición controlada:** máximo de dos particiones consecutivas; tres letras como mínimo a cada lado del corte; sin partición de nombres propios, marcas, siglas ni cifras.
- **Viudas y huérfanas:** sin viudas (última línea de párrafo aislada al inicio de columna) ni huérfanas (primera línea aislada al pie de columna).
- **Mayúsculas:** solo en cabeceras (portada, cabeceras de sección y folios); titulares en mayúscula inicial.
- **Interletraje:** −15 (*tracking*) en titulares desde 24 pt; sin ajuste en cuerpo.
- **Texto calado** (claro sobre fondo oscuro): cuerpo mínimo de 9,5 pt y peso mínimo conforme a `GUI-PP`.
- **Pesos y estilos:** solo los de la tabla; sin negrita ni cursiva simuladas.
- **Licencia e incrustación:** SIL OFL; incrustación completa de las familias en el archivo de imprenta (`GUI-PP`).
- **Nomenclatura de estilos:** prefijo `ST-` seguido del nombre de la tabla (`ST-Titular`, `ST-Cuerpo`), idéntica en todas las plantillas.

## 4. Color

### 4.1 Paleta

| Color | Uso | Hex | CMYK |
|---|---|---|---|
| Blanco Puro | Estilo de vida, negocios y servicio | #FFFFFF | 0/0/0/0 |
| Gris Platino | Fondos secundarios, tablas y fichas | #F4F5F7 | 3/2/2/0 |
| Negro Carbón | Fondo de ADN Gamer y texto | #0D0E12 | 60/40/40/100 |
| Azul Profundo | Bloques y filetes de ADN Gamer | #0B1F3A | 100/85/35/40 |
| Azul SoyTechno | Navegación, folios y llamados | Valor del manual de identidad corporativa | Valor del manual de identidad corporativa |
| Gris Texto | Texto secundario y créditos | #5B6472 | 0/0/0/75 |

> **Nota:** valores hexadecimal y CMYK del Azul SoyTechno tomados sin modificación del manual de identidad corporativa (subsección 1.1).

### 4.2 Contraste calculado

Relación de luminancia calculada con los valores hexadecimales; mínimo de 4,5:1 en texto corrido y de 3:1 en titulares (§3.4).

| Texto | Fondo | Relación | Aplicación |
|---|---|---|---|
| Negro Carbón | Blanco Puro | 19,29:1 | Texto corrido y titulares |
| Negro Carbón | Gris Platino | 17,68:1 | Tablas y fichas |
| Gris Texto | Blanco Puro | 5,98:1 | Texto secundario y créditos |
| Gris Texto | Gris Platino | 5,48:1 | Créditos sobre fichas |
| Blanco Puro | Negro Carbón | 19,29:1 | Texto calado en modo oscuro |
| Gris Platino | Negro Carbón | 17,68:1 | Texto secundario en modo oscuro |
| Blanco Puro | Azul Profundo | 16,52:1 | Texto calado sobre bloques |
| Gris Texto | Negro Carbón | 3,22:1 | Solo titulares; excluido del texto corrido |
| Gris Texto | Azul Profundo | 2,76:1 | Excluido |

### 4.3 Uso de la paleta

- **Modos:** claro en toda la revista, con Blanco Puro y Gris Platino; oscuro exclusivo de ADN Gamer (28-35) y su pauta contigua (26-27), con texto claro desde 9,5 pt.
- **Acento:** Azul SoyTechno limitado a navegación, folios y llamados; excluido de texto corrido y de fondos completos; verificación previa del contraste del valor oficial contra Blanco Puro y, con relación inferior a 4,5:1, texto de folio en Negro Carbón y azul reducido al filete.
- **Negro:** texto en 100 K con sobreimpresión; composición enriquecida (60/40/40/100) solo en fondos, con parámetros técnicos en `GUI-PP`.
- **Azul Profundo sobre Negro Carbón** (1,17:1): separación tonal sin función informativa; información siempre en texto claro.
- **Calibración:** valores CMYK de partida; ajuste en la prueba de color de la Edición 01 (ferro digital y pruebas físicas del lunes de S7, 11-ene-2027; aprobación en G4, 12-ene-2027) por DA, con aprobación de DE.

## 5. Cabecera y sistema de portada

### 5.1 Denominación y cabecera

- **Denominación:** SoyTechno, sin denominaciones alternativas; uso en los textos conforme al glosario (subsección 12.3).
- **Cabecera:** logotipo SoyTechno en versión editorial derivada del logotipo corporativo, sin alteración de proporciones ni del color corporativo.
- **Adopción y registro:** documentados en `EXP-ID-ST-2026-01`.
- **Leyenda del editor:** «Una publicación de SoyTechno», en portada y mancheta (§3.5).

### 5.2 Logotipo de cabecera

- **Origen:** archivos vectoriales del logotipo corporativo y de sus usos, conforme al manual de identidad corporativa (subsección 1.1); sin redibujo.
- **Derivación editorial:** selección de la composición y de la escala del logotipo para la portada; escalado proporcional; sin alteración de forma ni del color corporativo; sin degradados, biseles, sombras ni contornos añadidos.
- **Área de protección:** la del manual de identidad corporativa, con un mínimo de x en todo el perímetro (x: altura de la letra inicial del logotipo); sin texto, llamados, códigos ni detalle de imagen.
- **Tamaño fijo en portada:** ancho único para las seis ediciones, igual al mayor valor no superior a 177 mm (ancho de la caja) compatible con una ocupación máxima del 22 % de la altura (61,6 mm) por logotipo, área de protección y cintillo; altura resultante de las proporciones del logotipo.
- **Versiones:** positiva y negativa del manual de identidad corporativa; negativa sobre fondos oscuros y fotografía oscura; todas en vector.
- **Tamaño mínimo:** lectura inequívoca con la portada completa reducida a 30 mm de ancho (escala 1:7).
- **Barniz UV sectorizado:** sobre el logotipo y el elemento central de portada (§3.1); trazo mínimo, máscara y tolerancia de registro en `GUI-PP`.
- **Hito:** entrega de la cabecera (versión editorial del logotipo) con límite el 20-nov-2026 (G0 de la Edición 01), según el cronograma de `EXP-ID`.

### 5.3 Elementos fijos de portada

| Elemento | Ubicación | Norma |
|---|---|---|
| Cabecera | Zona superior, del 18 % al 22 % de la altura (50,4 a 61,6 mm) | Altura de la zona fijada una sola vez según el tamaño del logotipo; invariable en las seis ediciones |
| Titular | Zona de menor complejidad de la imagen, fuera del rostro | Uno por portada; Archivo Black o Bold de 36 a 60 pt |
| Llamados | Hasta tres, bajo el titular | Archivo Bold 14/18,75 pt; de una a seis palabras en forma nominal; viñeta en Azul SoyTechno |
| Número de edición | Cintillo bajo el logotipo, a la izquierda de la caja | «Edición 01»; Archivo Medium 9/12,5 pt |
| Bimestre | Mismo cintillo, tras el número de edición | «Enero-febrero 2027»; Archivo Medium 9/12,5 pt |
| Leyenda | Mismo cintillo, a la derecha de la caja | «Una publicación de SoyTechno»; Archivo Medium 9/12,5 pt |

**Bimestres de portada:** «Enero-febrero 2027» (Edición 01), «Marzo-abril 2027» (02), «Mayo-junio 2027» (03), «Julio-agosto 2027» (04), «Septiembre-octubre 2027» (05) y «Noviembre-diciembre 2027» (06).

### 5.4 Imagen de portada

- **Encuadre:** relación 3:4, con reserva de sangrado de 3 mm.
- **Margen superior libre:** no inferior al 20 % de la altura (56 mm) ni a la altura de la zona de cabecera fijada, con valor de captura entregado a PF antes de la sesión de portada (`PRO-PR`); sin solapamiento de la cabecera con rostros ni con el producto insignia.
- **Contraste:** cabecera con relación de 4,5:1 o superior contra la imagen; titular y llamados de 3:1 o superior (§3.4); sin sombras ni contornos de compensación; ante contraste insuficiente, cambio de fotografía o de encuadre.
- **Alternancia:** persona y producto insignia alternados entre ediciones consecutivas; verificación en G0 (`DOC-E-01`).
- **Portada no comercializable:** sin marcas patrocinantes, sellos ni logotipos de terceros (§2.5).
- **Confidencialidad y derechos:** reserva hasta la revelación (§5.3); cesión y autorización de imagen conforme a `REG-LG-ST-2026-01`; tratamiento fotográfico conforme a `PRO-PR-ST-2026-01`.
- **Inteligencia artificial:** imagen generada excluida de portada (sección 13).

### 5.5 Batería de pruebas

Pruebas previas a la aprobación de la versión editorial del logotipo y de la plantilla de portada:

1. Diez fotografías distintas (claras y oscuras, de fondo plano y complejo) con la cabecera en posición fija, en versión positiva o negativa según el fondo.
2. Miniatura de 30 mm de ancho (escala 1:7).
3. Versión a una tinta (100 K), solo como prueba de legibilidad y sin uso en portada.

Criterio de aceptación: lectura inequívoca de la denominación en las tres pruebas, con contraste de 4,5:1 o superior. Registro de resultados y archivos en `DOC-E-12`; aprobación de DE.

## 6. Plantillas por sección

### 6.1 Criterios comunes

- **Aperturas:** doble página real o página impar (§4.1).
- **Columnas y modo:** columnas conforme a la subsección 2.2; modo oscuro solo conforme a la subsección 4.3.
- **Firma, crédito y QR:** firma en todo artículo y crédito en toda fotografía (§2.6); bloque QR normalizado (sección 9) junto a reseña, cobertura, ficha y autopromoción; cero precios impresos (§2.5).

### 6.2 Familias de página

Tres familias para el ritmo de lectura de la revista:

- **Calma:** un elemento dominante y área libre amplia (Última Página, páginas de cita).
- **Ritmo:** texto y fotografía en 3 o 4 columnas (reseñas, breves, fichas y perfiles).
- **Impacto:** fotografía a sangre con titular o cita (aperturas de Reportaje Central, En Primera Fila y ADN Gamer).

Asignación de la familia de cada página en el mapa de paginación (`DOC-E-03`).

### 6.3 Fichas de sección

#### Sumario y créditos

- **Páginas:** 02-03, doble página.
- **Columnas:** índice visual en módulos de 3 columnas de retícula; carta editorial a 2 columnas; mancheta a 4.
- **Elementos fijos:** índice por bloques con folios, carta editorial con firma del cargo directivo, mancheta e instrucciones de interacción QR y NFC.
- **Reglas:** contenido de la mancheta conforme a `REG-LG`; sumario coincidente con títulos y páginas en G2.

#### Pulso Techno

- **Páginas:** 04-07.
- **Columnas:** 3 y 4, en breves e infografías.
- **Elementos fijos:** antetítulo de tema, breves con titular de 24 pt, infografías con fuente identificada y recortes de catálogo con crédito (admitidos solo en esta sección y en pauta).
- **Reglas:** modo claro; módulos de apoyo en Gris Platino; un destacado por doble página como máximo.

#### Bajo el Lente

- **Páginas:** 08-13: telefonía (08-09), televisión, audio y hogar (10-11), cómputo portátil (12-13).
- **Columnas:** 3.
- **Elementos fijos:** bodegón sobre fondo Gris Platino; ficha técnica en monoespaciada (estilo Datos) sobre recuadro Gris Platino; gama de entrada, media o alta en lugar de precio; veredicto conforme a `PRO-PR`; declaración de origen del equipo; bloque QR por pieza (sección 9); firma del especialista y crédito fotográfico.
- **Reglas:** cero precios impresos; separación de cuatro páginas como mínimo respecto de la pauta de la misma marca o de un competidor directo (§2.5), verificada en el mapa de paginación (`DOC-E-03`) y en G3; veredicto sin superlativos comerciales.

#### Reportaje Central

- **Páginas:** 16-19.
- **Columnas:** 2 en texto; apertura a doble página (16-17).
- **Elementos fijos:** imagen de apertura a sangre, titular Archivo Black de 48 a 60 pt, entradilla, firma, ladillos y un destacado por doble página.
- **Reglas:** compensación de 3 mm por lado en la imagen a doble página; área libre del 25 % por doble página; infografía conforme a la sección 10.

#### En Primera Fila

- **Páginas:** 20-25: entrevista central (20-23) y perfiles (24-25).
- **Columnas:** 2 en la entrevista; 3 en los perfiles.
- **Elementos fijos:** apertura a doble página (20-21) con retrato, titular, entradilla y crédito; preguntas en Source Serif 4 Semibold; respuestas en cita textual entre « »; de dos a cuatro perfiles (§2.3) con retrato, titular de 24 pt y firma.
- **Reglas:** preguntas en forma impersonal; ampliación en el pódcast mediante QR; retrato con profundidad de campo reducida conforme a `PRO-PR`; autorizaciones de imagen archivadas en `DOC-E-11`.

#### ADN Gamer

- **Páginas:** 28-35, entre el segundo y el tercer pliego (28-32 y 33-35).
- **Columnas:** 3 y 4, con bandera izquierda.
- **Elementos fijos:** fondo Negro Carbón; bloques y filetes Azul Profundo; titulares Archivo Black en Blanco Puro; fichas de *hardware* en bloque Azul Profundo con JetBrains Mono Medium 9,5/12,5 pt; calendario de torneos; QR sobre fondo oscuro con recuadro claro.
- **Reglas:** modo oscuro (subsección 4.3); pies, créditos y folios elevados a 9,5 pt o compuestos sobre recuadro Gris Platino.

#### Espacio Business

- **Páginas:** 36-39.
- **Columnas:** 3 en texto; 4 en tablas y fichas.
- **Elementos fijos:** módulos de infraestructura y gestión en fichas Gris Platino, caso de éxito con retrato y cita textual firmada, tabla comparativa vectorial.
- **Reglas:** modo claro; cifras y gráficos conforme a las secciones 10 y 11; denominación «Espacio Business» en redonda.

#### Conexión en Vivo

- **Páginas:** 40-43.
- **Columnas:** galería sobre 12 columnas, con módulos de 3, 6 y 12; pies a 4 columnas.
- **Elementos fijos:** crónica visual del lanzamiento anterior; pie de foto y crédito en toda imagen; fechas en formato «20-nov-2026» en pies.
- **Reglas:** autorizaciones de imagen y voz archivadas (`DOC-E-11`); toda página pagada con rótulo (§2.5).

#### Ruta Inteligente

- **Páginas:** 44-47.
- **Columnas:** 3 y 4.
- **Elementos fijos:** matriz de selección por perfil de uso (tabla vectorial sobre Gris Platino); guía de financiamiento por cuotas con plataformas aliadas; beneficios del Club SoyTechno; directorio de sedes en estilo Datos; bloques QR de afiliación y de condiciones de financiamiento.
- **Reglas:** cero precios; leyenda de vigencia en toda mención de descuentos, cuotas o beneficios (§2.5); condiciones de financiamiento certificadas en G3 (§4.3).

#### Última Página

- **Páginas:** 48, enfrentada a C3 (autopromoción con la zona de contacto NFC).
- **Columnas:** 2.
- **Elementos fijos:** columna firmada con el cargo directivo, QR de suscripción digital y adelanto de la siguiente edición (número, bimestre y eje temático).
- **Reglas:** redacción institucional impersonal; adelanto sin portada ni personaje hasta la hora cero de la edición siguiente (§5.3).

## 7. Folios, cabeceras de sección y navegación

### 7.1 Folio

- **Ubicación:** margen inferior exterior; línea base a 8 mm bajo la caja (12 mm del corte inferior); folio y nombre de sección en una sola línea (ejemplo: «28 · ADN GAMER»).
- **Estilo:** Archivo Medium de 7 pt en mayúsculas; Azul SoyTechno sobre fondo claro, con la verificación de contraste de la subsección 4.3; Blanco Puro de 9,5 pt sobre fondo oscuro.
- **Numeración:** continua desde la página 1; sin folio visible en portada, aperturas a sangre y pauta, con páginas igualmente contadas.

### 7.2 Cabeceras de sección y navegación

- **Cabecera de sección:** primera página de cada sección, con el estilo de la subsección 3.2 y filete de 1 pt en Azul SoyTechno.
- **Pestaña de navegación:** 3 mm × 24 mm en Azul SoyTechno, a sangre en el borde exterior, con posición vertical escalonada según el orden de las diez secciones.

## 8. Publirreportaje

### 8.1 Plantilla diferenciada

- **Formato:** doble página (14-15 o 26-27, o ampliación en múltiplos de 8; §4.1) en plantilla propia.
- **Rótulo:** «Publicidad» o «Contenido patrocinado» en la parte superior de cada página, centrado, Archivo Medium de 7 pt, con línea base a 10 mm del corte superior; recuadro Blanco Puro bajo el rótulo en caso de fondo con relación inferior a 4,5:1.
- **Tipografía:** cuerpo en Archivo Regular 9/12,5 pt, con bandera izquierda; titular en Archivo Medium de 24 a 36 pt.
- **Fondo:** Gris Platino en toda la caja.
- **Retícula:** 8 + 4 columnas (116,64 y 56,32 mm), exclusiva de la plantilla y excluida de las secciones editoriales.
- **Marca del anunciante:** visible en la columna lateral, conforme a sus guías.
- **Folio:** sin folio ni nombre de sección.
- **Firma:** «Contenido producido por la marca anunciante»; sin firma de redactores editoriales.
- **Prohibición de imitación:** sin Source Serif 4 en texto corrido, sin destacados con comillas angulares y sin titulares Archivo Black.
- **Reglas comunes:** cero precios, leyenda de vigencia y separación de cuatro páginas (§2.5); aprobación escrita de la marca en G3; QR del anunciante con parámetros asignados por PD (`GUI-PP`).

## 9. Zona de contacto NFC y bloque QR

### 9.1 Bloque QR

- **Composición:** QR, microtexto «Acceso a ficha, precio vigente y video» y dirección corta de respaldo (ejemplo: soytechno.com/r/e01p08a).
- **Variantes de microtexto:** «Afiliación al Club SoyTechno»; «Condiciones de financiamiento vigentes».
- **Tipografía:** microtexto en Archivo Medium de 7 pt; dirección corta en estilo Datos.
- **Retícula:** QR sobre 2 columnas (26,16 mm); microtexto y dirección alineados a la línea base, a la derecha o bajo el QR.
- **Fondo oscuro:** recuadro claro (Gris Platino o Blanco Puro) con el silencio incluido.
- **Un código por pieza:** sin reutilización entre ediciones.
- **Parámetros técnicos:** tamaño mínimo, silencio, corrección de errores y tintas en `GUI-PP`.

### 9.2 Zona de contacto NFC

- **Ubicación:** C3, zona de 40 × 40 mm a 30 mm o más del lomo y 20 mm o más de los cortes (§3.6); posición idéntica en las seis ediciones.
- **Composición:** etiqueta de 25 mm centrada en la zona (7,5 mm libres por lado), con guía circular de aplicación concéntrica; símbolo N del NFC Forum y rótulo «Zona de contacto NFC» sobre la zona, alineados a su borde izquierdo; QR equivalente adyacente a la derecha, con el bloque de la subsección 9.1.
- **Área libre:** fondo Blanco Puro o Gris Platino; sin tintas metálicas ni estampados en caliente (§3.6).
- **Parámetros técnicos:** diámetro y trazo de la guía en `GUI-PP`.

## 10. Infografía e iconografía

- **Iconos:** lineales, en módulos de 12,5 pt (4,41 mm) y 25 pt (8,82 mm), múltiplos de la línea base; trazo único de 0,75 pt; extremos y uniones redondeados; sin relleno, sombras, degradados ni perspectiva.
- **Gráficos:** título descriptivo; fuente identificada en el pie («Fuente: …»); ejes con magnitud y unidad del Sistema Internacional; eje cero en barras; colores de la paleta, con un solo color de resalte por gráfico; etiquetas directas, sin depender del color.
- **Tablas:** objetos vectoriales; filetes de 0,5 pt; encabezado en Archivo Medium de 8 pt; celdas en estilo Datos; cebrado alterno en Gris Platino.
- **Edición digital:** texto real y descripción alternativa en gráficos y tablas (§3.7).
- **Verificación:** contraste de cifras con fuente identificable antes de G2 (§2.6); archivos de infografías en `DOC-E-12`.

## 11. Estilo lingüístico

### 11.1 Registro impersonal

Registro culto del español de Venezuela, impersonal en toda la publicación (§2.6): estructuras nominales, infinitivos y construcciones con «se»; sin primera ni segunda persona, sin apelaciones coloquiales y sin oraciones con sujeto y verbo conjugado activo. Verbos conjugados admitidos solo con «se» antepuesto («se entrega», «se deberá verificar»). Subordinadas introducidas por `que`, `cuando`, `donde`, `quien` o `cuyo` sustituidas por participios, preposiciones, dos puntos y listas.

| Redacción por evitar | Redacción normativa | Recurso |
|---|---|---|
| `Descubre el nuevo portátil` | «Nuevo portátil: resultados de cinco días de uso real» | Frase nominal |
| `Escanea el código y mira el precio` | «Acceso a ficha, precio vigente y video» | Microtexto nominal |
| `Nosotros probamos el equipo cinco días` | «Prueba del equipo durante cinco días de uso real» | Nominalización |
| `Usted puede pagar en cuotas` | «Pago en cuotas con plataformas aliadas; condiciones vigentes mediante QR» | Nominalización con remisión |
| `Aquí vemos el televisor en la sala de pruebas` | «Televisor QLED de 65 pulgadas (165 cm) en la sala de pruebas» | Pie de foto nominal |
| `¿Cómo empezaste en los deportes electrónicos?` | «Primeros pasos en los deportes electrónicos» | Pregunta nominal |
| `La redacción verifica las cifras` | «Se verifican las cifras con fuente identificable antes de G2» | Construcción con «se» |

### 11.2 Textos institucionales y entrevistas

- **Carta editorial y Última Página:** redacción institucional impersonal, con firma del cargo directivo («Dirección Editorial»).
- **Entrevistas y pódcast:** preguntas y conducción en forma impersonal (nominal o infinitiva); respuestas en cita textual de la persona entrevistada, entre « »; texto final sin aprobación de la persona entrevistada, salvo verificación de citas textuales (§2.3).
- **Microtextos:** formulación nominal o en infinitivo («Acceso a ficha, precio vigente y video»; «Zona de contacto NFC»).
- **Firma y crédito:** firma en todo artículo; crédito en toda fotografía y página con fotografía (§3.5).

### 11.3 Composición de textos

- **Titulares:** mayúscula inicial en la primera palabra y en los nombres propios; sin punto final.
- **Comillas:** angulares « » en citas, títulos de piezas y denominaciones; inglesas “ ” anidadas dentro de las angulares; signo de puntuación después de la comilla de cierre; sin comillas rectas.
- **Cursiva:** extranjerismos sin equivalente de uso general y títulos de obras; redonda en nombres propios, adaptaciones y siglas.
- **Siglas:** sin puntos ni espacios; plural invariable (los QR); desarrollo en la primera mención de cada pieza, salvo QR, NFC, 4K, OLED y QLED.
- **Números:** coma decimal (0,2 mm); punto de millares (5.000); años, páginas y códigos sin separador; unidades del Sistema Internacional con espacio de no separación (8 GB, 120 Hz, 25 mm); porcentaje con espacio (50 %); multiplicación con × entre espacios (40 × 40 mm).
- **Fechas y horas:** «20-nov-2026» en tablas, fichas y listas; «20 de noviembre de 2026» en prosa; horas en formato de 24 h (19:30); «Edición 01» en texto y «Ed. 01» solo en tablas.
- **Moneda y datos económicos:** código de moneda detrás de la cifra, separado por espacio y sin el signo `$`; precios de producto excluidos de la publicación (§2.5); datos económicos del programa expresados en porcentaje.
- **Marcas:** grafía oficial de fabricantes (ASUS, HP, LG, TCL); denominaciones «Club SoyTechno», «Zona Gamer», «Zona Business» y «Zona Samsung» en redonda.
- **Productos:** denominación comercial con la grafía oficial del fabricante; variante y código de modelo en estilo Datos (`PRO-PR`).

### 11.4 Neutralidad comercial

- **Valor demostrado:** datos de rendimiento, materiales, casos de uso y especificaciones verificables; comparaciones solo con base en medición (`PRO-PR`).
- **Términos excluidos, salvo cita textual:** `el mejor`, `la mejor`, `increíble`, `imperdible`, `revolucionario`, `oferta`, `aprovechar`, `ganga`, `espectacular`, `el único`, `sin competencia`, `lo último en`.
- **Ofertas y promociones:** exclusión del contenido editorial, con remisión solo mediante QR y NFC (§1.3).

## 12. Glosario normativo

Fuente única del glosario, con remisión desde todos los textos y `DOC-E-09`; criterio de cursiva y de redonda en la subsección 11.3.

### 12.1 Extranjerismos y equivalentes

| Término | Forma normativa | Tratamiento |
|---|---|---|
| *hardware* | *hardware* | Cursiva; plural invariable |
| *software* | *software* | Cursiva; plural invariable |
| *router* | *router* | Cursiva; plural *routers* |
| *streaming* | *streaming* | Cursiva |
| *streamer* | *streamer* | Cursiva; plural *streamers* |
| *podcaster* | *podcaster* | Cursiva; plural *podcasters* |
| *influencer* | *influencer* | Cursiva; plural *influencers* |
| *networking* | *networking* | Cursiva |
| *gamer* | *gamer* | Cursiva; redonda en «Zona Gamer» y «ADN Gamer» |
| *gaming* | *gaming* | Cursiva |
| *bookazine* | *bookazine* | Cursiva; limitada a la definición del formato |
| *smartphone* | teléfono inteligente | Equivalente español |
| *smartwatch* | reloj inteligente | Equivalente español |
| *laptop*, *notebook* | portátil | Equivalente español |
| *online* | en línea | Equivalente español |
| *setup* | configuración; puesto de juego | Equivalente según el contexto |
| *backstage*, *making of* | detrás de cámaras | Equivalente español |
| *esports*, *e-sports* | deportes electrónicos | Equivalente español |
| *wearable* | dispositivo vestible | Equivalente español |
| *smart home* | hogar inteligente | Equivalente español |
| *flatplan* | mapa de paginación | Equivalente español; *flatplan* entre paréntesis en documentos internos |
| *podcast* | pódcast | Adaptación en redonda, con tilde |
| *wifi*, *WiFi* | Wi-Fi | Redonda; con guion y numeración (Wi-Fi 7) |

### 12.2 Siglas y unidades

| Término | Forma normativa | Tratamiento |
|---|---|---|
| *AI* | IA | Sigla en redonda; desarrollo «inteligencia artificial (IA)» en la primera mención |
| código QR | QR | Sigla en redonda; plural invariable |
| NFC | NFC | Sigla en redonda; «etiqueta NFC» |
| QLED, OLED | QLED; OLED | Siglas en redonda y mayúsculas |
| 4k | 4K | Redonda; K mayúscula |
| gb, Gb, tb | GB; TB | Mayúsculas; espacio de no separación (8 GB, 1 TB) |
| hz | Hz | H mayúscula (120 Hz) |
| mah | mAh | Grafía del símbolo (5.000 mAh) |
| *watts* | W | Mayúscula (65 W) |
| *dpi* | ppp | Puntos por pulgada; solo en impresión (300 ppp) |
| pulgadas, comillas dobles | pulgadas | Equivalencia en centímetros en la primera mención: «65 pulgadas (165 cm)» |
| *Mbps* | Mbit/s | Unidad con barra (200 Mbit/s) |
| *nits* | cd/m² | Candela por metro cuadrado (1.000 cd/m²) |

### 12.3 Denominaciones de SoyTechno

| Término | Forma normativa | Tratamiento |
|---|---|---|
| `Soytechno`, `Soy Techno`, `SOYTECHNO` | SoyTechno | Redonda; grafía oficial de la marca |
| Denominación de la publicación | la revista SoyTechno; la revista | Redonda; «Revista Corporativa SoyTechno» reservada a la denominación institucional del proyecto |
| `Club Soytechno` | Club SoyTechno | Redonda; mayúscula en cada palabra |
| Zona Gamer | Zona Gamer | Redonda |
| Zona Business | Zona Business | Redonda |
| Zona Samsung | Zona Samsung | Redonda |
| SoyTechno Hogar | SoyTechno Hogar | Redonda |
| ADN Gamer | ADN Gamer | Redonda; sección en modo oscuro |
| Espacio Business | Espacio Business | Redonda |
| Secciones | Pulso Techno; Bajo el Lente; Reportaje Central; En Primera Fila; Conexión en Vivo; Ruta Inteligente; Última Página | Redonda; mayúscula inicial en cada palabra significativa |
| día D, Día-D | Día D | Redonda; mayúscula en la D (D+1) |

## 13. Política de uso de inteligencia artificial

### 13.1 Usos

| Uso | Condición | Registro |
|---|---|---|
| Transcripción de entrevistas y pódcast | Admitido, con verificación humana íntegra | `DOC-E-09` |
| Corrección asistida de ortografía y estilo | Admitido, con decisión final de EC | `DOC-E-09` |
| Documentación y organización de fuentes | Admitido, con fuentes contrastadas | `DOC-E-09` |
| Ilustración conceptual | Admitida con autorización previa de DE y rótulo «Ilustración generada con IA» en el crédito (estilo Crédito) | `DOC-E-09` |
| Fotografía de producto, retratos y portada, con inclusión del retoque generativo | Prohibida | — |
| Autoría de textos, titulares y veredictos | Prohibida; firma de la persona responsable (§2.6) | — |
| Carga de contenidos confidenciales o de portada en servicios externos | Prohibida | — |

### 13.2 Reglas

- **Contenido confidencial:** textos inéditos, portada, pruebas con marca de agua, datos de participantes e información de pauta excluidos de servicios externos.
- **Verificación humana:** toda cifra, cita y nombre contrastados con fuente identificable antes de G2 (§2.6).
- **Retoque:** sin alteración de color, proporciones, pantallas ni rasgos (§3.5); relleno, ampliación y reconstrucción generativos con IA excluidos; tratamiento conforme a `PRO-PR`.
- **Cesiones:** declaración de uso de IA en la cesión de derechos, con modelo en `REG-LG`.
- **Servicios:** sin mención de nombres comerciales en documentos ni publicaciones.
- **Registro:** uso, finalidad y verificación en `DOC-E-09`, a cargo de EC.

## 14. Control del documento

### 14.1 Relación con otros documentos

- **Fuente única:** estilo lingüístico y glosario normativo, con remisión desde todos los textos y `DOC-E-09`.
- **Remisiones:** `GUI-PP` (parámetros técnicos de color, barniz, QR y NFC); `PRO-PR` (fotografía, ficha y veredicto); `REG-LG` (mancheta, cesiones y autorizaciones); `EXP-ID` (adopción de la denominación y de la cabecera; protección registral); `PLA-CM-ST-2027-01` (tono y estilo de microtextos); `DOC-E-12` (archivos de diseño).

### 14.2 Revisión y actualización

- **Periodicidad:** revisión anual tras la Edición 06, en el intervalo sin ciclo activo del 08-nov-2027 al 14-nov-2027.
- **Disparadores:** cambio de la identidad corporativa de SoyTechno; modificación de §2.5, §2.6 o §3.2 a §3.6 del rector; ajuste de valores CMYK tras la prueba de color de la Edición 01.
- **Responsable y registro:** DA, con aprobación de DE; cambios registrados en `DOC-E-05` y difundidos a diseño, redacción y proveedores creativos en la S1 del ciclo siguiente.

### 14.3 Firmas

| Elaboración | Revisión | Aprobación |
|---|---|---|
| DA · nombre, cargo y fecha | Nombre, cargo y fecha | DE · fecha |
