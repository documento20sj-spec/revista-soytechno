# Guía Técnica de Pre-prensa, Impresión e Integración Phygital

SoyTechno · Proyecto Editorial · Guía técnica

| Campo | Valor |
|---|---|
| Código | `GUI-PP-ST-2026-01` |
| Versión · fecha | 1.0 · 18 de octubre de 2026 |
| Documento base | `DIR-ED-ST-2026-01` · `IND-ED-ST-2026-01` |
| Clasificación | Uso interno · difusión a imprenta y proveedores técnicos |
| Responsable | DA · Dirección de Arte y Maquetación |
| Colaboración | PD · Producción Digital y Datos; CC · Coordinación Comercial y Alianzas |
| Aprobación | DE · Dirección Editorial |
| Base en el rector | §3.1, §3.2, §3.6, §3.7, §4.3 |
| Estándar de redacción | Normativo-impersonal · cero redundancia |

**Objeto:** pliego de condiciones técnicas de la revista impresa para la imprenta, el proveedor de etiquetas interactivas y el equipo de maquetación: pre-prensa, impresión e integración *phygital* (códigos QR y etiqueta NFC), con criterios de verificación para G4 y de control de calidad del tiraje.

**Alcance:** aplicación a DA, PD y CC, a la imprenta seleccionada, al proveedor de etiquetas NFC y, en la sección 11, a los anunciantes; Ediciones 01 a 06 de 2027.

**Precedencia:** Documento Rector e Índice Maestro sobre este documento; referencias al rector con el símbolo §.

## 1. Especificación del producto impreso

Resumen operativo de §3.1 del rector, con remisión a las secciones de desarrollo. Ante discrepancia, prevalencia del rector.

### 1.1 Parámetros del producto

| Parámetro | Valor (§3.1) | Desarrollo |
|---|---|---|
| Formato | 210 × 280 mm vertical; abierto, 420 × 280 mm | Sección 2 |
| Paginación | 48 páginas interiores y 4 de cubierta en tres pliegos de 16; ampliaciones en múltiplos de 8 | Secciones 2 y 5 |
| Cubierta | Estucado mate de 250 g/m², 4/4, laminado mate exterior y barniz UV sectorizado | Secciones 4 y 5 |
| Tripa | Estucado mate de 115 g/m², 4/4 | Sección 3 |
| Encuadernación | Rústica fresada con cola PUR; lomo cuadrado de 3 mm en color plano, sin texto | Sección 5 |
| Tiraje | 5.000 ejemplares en la Edición 01; ajuste máximo del 20 % por edición según la distribución efectiva (§3.7) | Sección 10 |
| Integración *phygital* | Código QR por pieza y etiqueta NFC en C3 | Secciones 6 y 7 |

### 1.2 Ampliaciones y ancho de lomo

- **Ampliaciones:** en múltiplos de 8 páginas, con pliegos de 8 o 16 y pauta inferior al 25 % (§4.1); prioridad del ajuste de tiraje sobre el de paginación (§5.5).
- **Ancho de lomo:** 3 mm para 48 páginas interiores; ante ampliación o medida distinta en la maqueta en blanco, valor confirmado por escrito por la imprenta antes de G4 y registrado en `DOC-E-15`.

### 1.3 Insumos de la imprenta y maqueta en blanco

- **Insumo de la imprenta seleccionada (27-nov-2026):** perfil ICC de salida, formato PDF/X confirmado, especificaciones de máquina, papeles, laminado, barniz y encuadernación, y requisitos de entrega. Responsable: DA.
- **Perfil de referencia:** ISO Coated v2 300 %. La sustitución por el perfil de la imprenta se aplica a todo el documento, a la prueba de color y a la lista de verificación, con registro en la ficha de producción de `DOC-E-15`.
- **Maqueta en blanco:** papeles, laminado mate, encuadernación PUR y motivo de ensayo de barniz UV conforme a la cotización adjudicada (`PLI-PV-ST-2026-01`); aprobación por DA antes de la Edición 01 y antes del 11-dic-2026.
- **Mediciones en la maqueta:** ancho real del lomo, posición del hendido y del encolado lateral, adhesión del laminado y del barniz; registro en `DOC-E-15`.

## 2. Preparación de archivos

### 2.1 Formato de exportación

- **Formato:** PDF/X-4 (ISO 15930-7), en páginas sueltas: una página impresa por página del PDF, en el orden del mapa de paginación (`DOC-E-03`).
- **Cajas de página:** TrimBox de 210 × 280 mm; BleedBox de 216 × 286 mm; MediaBox de 236 × 306 mm (10 mm adicionales por lado, fuera del sangrado, para las marcas).
- **Sangrado y marcas:** sangrado de 3 mm; marcas de corte y de registro fuera del sangrado, sin invadirlo.
- **Fuentes:** incrustación del 100 %; instancias estáticas de cada peso del rector §3.3; sin negrita ni cursiva sintéticas; texto convertido a curvas solo en logotipos.
- **Transparencias:** vivas, sin aplanado previo; efectos en espacio CMYK.
- **Condición de impresión:** declarada en el archivo (FOGRA39 o la de la imprenta), con perfil incrustado.
- **Exclusiones:** cifrado, comentarios, capas ocultas, objetos fuera de página y elementos RGB o Lab.

### 2.2 Imágenes y vectores

- **Resolución:** 300 ppp a tamaño final; mínimo admisible de 240 ppp; remuestreo a 300 ppp solo en imágenes de más de 450 ppp; sin ampliación por interpolación.
- **Compresión:** sin pérdida o JPEG de calidad máxima.
- **Vectores:** logotipos, filetes y códigos en vector, sin rasterizar; grosor mínimo de filete de 0,25 pt en positivo y de 0,5 pt en calado.

Referencia de píxeles por elemento a tamaño final con sangrado:

| Elemento | Tamaño | 300 ppp | 240 ppp (mínimo) |
|---|---|---|---|
| Página | 216 × 286 mm | 2.552 × 3.378 px | 2.041 × 2.703 px |
| Doble página | 426 × 286 mm | 5.032 × 3.378 px | 4.026 × 2.703 px |
| Cubierta exterior | 429 × 286 mm | 5.067 × 3.378 px | 4.054 × 2.703 px |

### 2.3 Cubiertas

- **Cubierta exterior:** pliego C4 + lomo de 3 mm + C1, de 423 × 280 mm de corte final y 429 × 286 mm con sangrado.
- **Cubierta interior:** pliego C2 + lomo + C3 del mismo formato, con el eje del lomo coincidente con el de la cubierta exterior.
- **Archivos:** un archivo por cara, en una sola página de PDF.

### 2.4 Nomenclatura, versiones y entrega

- **Nombre de archivo:** `ST-RV-E<ed>_<págs>_<sección>_v<n>`, con `<ed>` en dos dígitos (01 a 06), `<págs>` como rango de dos dígitos (`08-13`) o `C4-C1` y `C2-C3` en cubiertas, y `<sección>` con los identificadores de 6.3, `cubierta` o `pauta-<marca>`. Ejemplos: `ST-RV-E01_08-13_lente_v2` y `ST-RV-E01_C4-C1_cubierta_vFinal`.
- **Versiones:** versión candidata el lunes de S7; `vFinal` asignada en G4 sin cambio de contenido, con suma de verificación (SHA-256) idéntica a la de la candidata.
- **Entrega:** carpeta 05_PrePrensa, en `DOC-E-15`: archivos, informe de verificación previa del PDF/X-4 sin errores, ficha de producción (perfil, papeles, ancho de lomo), lista de verificación firmada (sección 8) y sumas de verificación. Canal de acceso restringido conforme a `PRO-RP-ST-2026-01`.
- **Responsable y plazo:** DA; lunes de S7.

## 3. Gestión del color

### 3.1 Perfil, conversión y cobertura

- **Perfil de salida:** CMYK con ISO Coated v2 300 % (FOGRA39) o el perfil de la imprenta; cobertura total máxima del 300 % en todo el archivo.
- **Conversión:** de RGB a CMYK en pre-prensa, una sola vez y desde el original en Adobe RGB (§3.5); intento de reproducción colorimétrico relativo con compensación del punto negro; intento perceptual solo por decisión de DA, con registro en `DOC-E-15`; sin conversiones sucesivas entre perfiles CMYK.
- **Paleta del rector (§3.4):** Negro Carbón (C60 M40 Y40 K100) con cobertura total de 240 % y Azul Profundo (C100 M85 Y35 K40) con 260 %, ambos dentro del límite de 300 %.

### 3.2 Negro, texto y calado

- **Texto negro:** 100 K puro (C0 M0 Y0 K100), con sobreimpresión de relleno y modo de sobreimpresión 1, ejecutada por el RIP de la imprenta; filetes en K puro.
- **Negro enriquecido:** C60 M40 Y40 K100 solo en fondos; prohibido en texto y filetes.
- **Texto calado sobre fondos oscuros:** desde 9,5 pt (§3.4), peso Regular o superior, sin trazos finos; reventado a cargo del RIP de la imprenta.
- **Prueba de color:** simulación de sobreimpresión activada.

### 3.3 Calibración y tolerancias

- **Calibración de referencia:** prueba de color de la Edición 01 (§3.4), con los valores medidos de la tira de control archivados en `DOC-E-16` como referencia de las ediciones siguientes.
- **Tolerancia del impreso:** ΔE*ab igual o inferior a 5 en los sólidos de la tira de control frente a la prueba certificada (sección 10).

## 4. Barniz UV sectorizado

Aplicación sobre el logotipo de cabecera y el elemento central de la portada (C1), conforme al sistema gráfico de `MAN-ID-ST-2026-01`.

### 4.1 Archivo y plancha

- **Plancha:** independiente de la cuatricromía.
- **Máscara:** vectorial, en tinta plana denominada «UV» al 100 % y en sobreimpresión; color alterno de visualización sin efecto en la salida; sin tramados ni degradados.
- **Geometría:** trazo mínimo de 0,3 mm; separación mínima de 0,5 mm entre áreas barnizadas; retiro de 3 mm respecto del corte y de 10 mm respecto del lomo.
- **Registro:** tolerancia de 0,3 mm entre barniz e impresión.

### 4.2 Sustrato y secuencia

- **Secuencia:** impresión, laminado mate exterior y barniz UV (miércoles de S7).
- **Compatibilidad:** tintas, película de laminado y barniz verificados en la maqueta en blanco con el motivo de ensayo; adhesión comprobada con cinta, sin desprendimiento.
- **Exclusiones:** C3 y cara interior de la cubierta, sin laminado ni barniz.

## 5. Encuadernación PUR y zona del lomo

### 5.1 Zona del lomo

- **Distancias de seguridad (§3.1):** texto, rostros, logotipos y códigos a 10 mm o más del lomo, en cada página.
- **Imágenes a doble página:** compensación de 3 mm por lado: cada página repite 3 mm de la imagen vecina sobre el eje central (6 mm repetidos en total); aplicación por DA en la maquetación, sin alterar la imagen original.

### 5.2 Cubierta y lomo

- **Lomo:** 3 mm en color plano continuo, sin degradados, imágenes ni texto, con prolongación de 3 mm del color hacia C1 y C4 como tolerancia de plegado.
- **Hendido y encolado lateral:** posición y medidas de la maqueta en blanco aprobada, registradas en `DOC-E-15`; sin barniz ni elementos críticos en la franja de encolado.
- **Tolerancias:** corte, 1 mm; plegado de la cubierta respecto del eje del lomo, 1 mm.
- **Secuencia:** encuadernación PUR el jueves de S7, previa a la aplicación de etiquetas NFC.

## 6. Códigos QR

### 6.1 Principios

- **Tecnología:** QR dinámico de la plataforma de enlaces de SoyTechno; un código por pieza, sin reutilización entre ediciones.
- **Contenido codificado:** dirección corta de la pieza, `https://soytechno.com/r/e<ed>p<pág><letra>` (31 caracteres; versión 3 del símbolo, de 29 × 29 módulos). Los parámetros UTM se anexan en la redirección y no se imprimen.
- **Destino:** editable tras la impresión; destino de contingencia: página común de la edición en soytechno.com/revista.

### 6.2 Parámetros de medición

| Parámetro | Valor | Regla |
|---|---|---|
| `utm_source` | `revista` | Fijo en todas las piezas |
| `utm_medium` | `qr` | Fijo en todos los códigos QR |
| `utm_campaign` | `ed<n>` | De `ed01` a `ed06`, según la edición |
| `utm_content` | `p<pág>-<sección>-<pieza>` | Página, sección y pieza del código |

- **`<pág>`:** dos dígitos (`02` a `48`) o `c2`, `c3` y `c4` en cubiertas.
- **`<sección>`:** identificador de 6.3.
- **`<pieza>`:** letra `a`, `b`, `c`… por orden de lectura en la página.
- **Dirección corta de respaldo:** `soytechno.com/r/e<ed>p<pág><letra>`, con la misma página y la misma letra (ejemplo: `soytechno.com/r/e01p08a` para `utm_content=p08-lente-a`).

### 6.3 Identificadores de sección

Identificadores en minúscula, sin acentos ni espacios, asignados por PD.

| Identificador | Sección | Páginas |
|---|---|---|
| `sumario` | Sumario y créditos | 02-03 |
| `pulso` | Pulso Techno | 04-07 |
| `lente` | Bajo el Lente | 08-13 |
| `reportaje` | Reportaje Central | 16-19 |
| `primerafila` | En Primera Fila | 20-25 |
| `gamer` | ADN Gamer | 28-35 |
| `business` | Espacio Business | 36-39 |
| `conexion` | Conexión en Vivo | 40-43 |
| `ruta` | Ruta Inteligente | 44-47 |
| `ultima` | Última Página | 48 |
| `c3` | Autopromoción con zona de contacto NFC | C3 |
| `pauta` | Páginas de pauta | C2-01, 14-15, 26-27 y C4 |

### 6.4 Composición y legibilidad

- **Tamaño:** lado mínimo del símbolo de 18 mm (módulo de 0,62 mm en la versión 3); silencio de cuatro módulos (2,5 mm).
- **Corrección de errores:** nivel M; nivel Q sobre fondo oscuro, con recuadro claro (Blanco Puro o Gris Platino, §3.4) extendido sobre el silencio.
- **Color y forma:** exportación vectorial al 100 % de negro (K 100); módulos oscuros sobre fondo claro, sin inversión ni logotipos interiores.
- **Microtexto y respaldo:** «Acceso a ficha, precio vigente y video» y dirección corta de respaldo junto a cada código; composición gráfica conforme a `MAN-ID`.
- **Distancia al lomo:** 10 mm o más (5.1).

### 6.5 Generación, pruebas y control

- **Generación y registro:** PD, desde S5, en la matriz maestra `DOC-E-18` (código corto, página, sección, pieza, destino, parámetros, responsable del destino, estado y fecha de verificación); colocación del código vectorial por DA en la maquetación; QR y destinos configurados en G2.
- **Destino previo a la hora cero:** página de espera de la edición; cambio al contenido definitivo en la hora cero conforme a `PRO-RP`.
- **Prueba en G4:** lectura sobre el ferro impreso a escala 100 % en cuatro equipos (dos iOS y dos Android, de gamas distintas) con la aplicación de cámara del sistema. Criterio de aceptación: lectura de cada código en una captura, con apertura del destino correcto y de sus parámetros. Registro en `DOC-E-16`.
- **Revisión semanal de destinos:** PD, desde G2 hasta el Día D de la edición siguiente: respuesta correcta del destino, coincidencia con `DOC-E-18` y vigencia de precios y condiciones (§2.5); corrección en la plataforma, sin reimpresión.

## 7. Etiqueta NFC

### 7.1 Chip y etiqueta

- **Chip:** NTAG213 o equivalente NFC Forum Tipo 2 (ISO/IEC 14443 Tipo A, 13,56 MHz), con 144 bytes de memoria de usuario, identificador único (UID) de 7 bytes, contador de lecturas de 24 bits, réplica (espejo) del UID y del contador en la URL, y bloqueo permanente de escritura.
- **Etiqueta:** adhesiva, de papel, de 25 mm de diámetro y espesor inferior a 0,2 mm; adhesivo permanente apto para estucado mate.
- **Datos:** un solo registro NDEF de tipo URI; ausencia de datos personales.

### 7.2 Registro NDEF y plantilla de URL

- **Plantilla:** `https://soytechno.com/n/e<ed>/<lote>?t=` seguida de 21 caracteres de espejo: UID de 14 caracteres hexadecimales, `x` y contador de 6 caracteres hexadecimales. Lectura de ejemplo: `https://soytechno.com/n/e01/EV?t=04A1B2C3D4E5F6x00002A`.
- **Parte estática:** edición en dos dígitos y código de lote de 7.7; prefijo `https://` abreviado con el código de URI `0x04`.
- **Verificación de longitud:** mensaje NDEF con TLV de 144 bytes como máximo; plantilla de referencia (lote `EV`) de 54 bytes, con el espejo íntegro dentro de la memoria de usuario. Posición del espejo calculada para cada plantilla (referencia: página de memoria 12, byte 0; lotes de tres caracteres: página de memoria 12, byte 1).
- **Redirección:** servicio de redirección de SoyTechno con destino editable por PD; anexión de `utm_source=revista`, `utm_medium=nfc`, `utm_campaign=ed<n>` y `utm_content=<lote>`; destino previo a la hora cero conforme a `PRO-RP`.

### 7.3 Codificación y bloqueo por el proveedor

1. Escritura del registro NDEF con la plantilla del lote y 21 caracteres `0` de relleno en la posición del espejo.
2. Configuración del espejo (UID y contador) en esa posición y habilitación del contador de lecturas.
3. Lectura de verificación de la URL completa, del UID replicado y del incremento del contador.
4. Bloqueo permanente: contenedor de capacidad en solo lectura (cuarto byte `0F`), bits de bloqueo estáticos y dinámicos de las páginas de usuario y bloqueo de la configuración de espejo y contador.
5. Prueba del bloqueo: intento de escritura rechazado.
6. Registro, en el reporte del lote, del valor del contador en la última lectura de verificación como línea base de cada UID.

### 7.4 Reporte y entrega por lote

- **Alcance:** codificación y verificación al 100 % de las etiquetas por el proveedor; etiquetas rechazadas, fuera del lote entregado.
- **Reporte de identificadores:** un archivo CSV (UTF-8) por lote, con lote, edición, UID, contador de la última lectura de verificación y resultado.
- **Entrega rotulada:** cada unidad de embalaje (rollo o lámina) con lote, edición y cantidad; sin mezcla de lotes.
- **Seguridad:** sin claves ni datos personales en los archivos; transferencia por canal de acceso restringido.

### 7.5 Ensayo de verificación

Ensayo único para la recepción del lote, la verificación de G4 y el muestreo de `DOC-E-17`. Criterio de aceptación: cero fallos.

| Control | Criterio |
|---|---|
| Lectura | Apertura del destino al aproximar el equipo a la zona, sin aplicación adicional |
| URL | Dominio, ruta, edición y lote coincidentes con la rotulación del embalaje |
| Identificador | UID replicado igual al del reporte del lote y único en el grupo de muestreo |
| Contador | Incremento de una unidad entre dos lecturas separadas; valor coherente con la línea base del reporte |
| Bloqueo | Intento de escritura rechazado |

- **Equipos:** lector de referencia designado por PD en la recepción del lote y en `DOC-E-17`; dos iOS y dos Android, de gamas distintas y con NFC activado, en G4.
- **Lecturas de prueba:** marcadas y excluidas de la medición (`MAN-MD-ST-2026-01`).

### 7.6 Ubicación y aplicación

- **Zona de contacto:** 40 × 40 mm en C3, con la etiqueta de 25 mm en el centro; a 30 mm o más del lomo y a 20 mm o más de los cortes; guía circular impresa de 28 mm de diámetro y trazo de 0,5 pt en 100 K, con tolerancia de colocación de 1,5 mm.
- **Interferencias:** sin tintas metálicas ni estampados en caliente en la zona de C3 ni en su proyección sobre C4; sin laminado ni barniz en la zona.
- **Composición gráfica:** símbolo N del NFC Forum, rótulo «Zona de contacto NFC» y QR equivalente adyacente conforme a `MAN-ID`.
- **Aplicación:** manual, por la imprenta, tras la encuadernación (viernes de S7), en línea de acabado con guía de registro; adhesión permanente comprobada en la maqueta en blanco con prueba de despegue a las 24 horas (rotura de fibra del papel).

### 7.7 Lotes y calendario de pedidos

| Código | Canal o sede | Ediciones |
|---|---|---|
| `EV` | Evento | 01 a 06 |
| `CL` | Club SoyTechno | 01 a 06 |
| `AL` | Aliados, fuerza de ventas, entrevistados y prensa | 01 a 06 |
| `SC` | Sambil Chacao | 01 a 06 |
| `CM` | City Market | 01 a 06 |
| `V01` a `Vnn` | Sede VIP adicional, un código por sede | 03 a 06 |
| `AV` | Compras de alto valor | 03 a 06 |
| `AR` | Archivo | 03 a 06 |

Cantidades por lote: `PLA-DI-ST-2027-01`.

| Lote de ediciones | Pedido | Recepción límite en la imprenta |
|---|---|---|
| 01 y 02 | 30-nov-2026 | 11-ene-2027 |
| 03 y 04 | 08-mar-2027 | 16-abr-2027 |
| 05 y 06 | 02-jul-2027 (viernes previo al feriado del 05-jul) | 16-ago-2027 |

- **Plazo de suministro:** de tres a seis semanas. Recepción límite: último día hábil previo a G4 de la primera edición del lote (lunes de S7, salvo el feriado del 19-abr-2027).
- **Tiraje completo con NFC desde la Edición 03:** decisión del CE en G4 de la Edición 02 (02-mar-2027), con la activación acumulada de la Edición 01 (umbral del 10 %); pedido del 08-mar-2027 condicionado a esa decisión.
- **Contratación y aceptación del lote:** `PLI-PV`.

### 7.8 Límite de la tecnología

> **Nota:** UID y contador replicados sin autenticación criptográfica; control de un único canje por identificador en el servidor, con los términos del beneficio en `REG-LG-ST-2026-01`.

## 8. Lista de verificación previa a imprenta (criterio de G4)

Lista de 33 puntos sobre el archivo definitivo (§3.1 y §3.2), con resultado «conforme» o «no conforme» por punto. Bloqueo de G4 ante cualquier punto en «no conforme». Firma de DA (puntos 1 a 33) y visado de PD (puntos 21 a 28); archivo en `DOC-E-15`.

### 8.1 Archivo

| N.º | Punto | Criterio |
|---|---|---|
| 1 | Formato | PDF/X-4 (ISO 15930-7) en páginas sueltas; informe de verificación previa sin errores |
| 2 | Cajas de página | TrimBox de 210 × 280 mm y BleedBox de 216 × 286 mm en todas las páginas |
| 3 | Sangrado y marcas | Sangrado de 3 mm en todo elemento al corte; marcas fuera del sangrado |
| 4 | Fuentes | Incrustadas al 100 %, sin estilos sintéticos |
| 5 | Nomenclatura | Nombre conforme a 2.4; suma de verificación registrada en `DOC-E-15` |

### 8.2 Color

| N.º | Punto | Criterio |
|---|---|---|
| 6 | Perfil | ISO Coated v2 300 % o el de la imprenta, declarado como condición de impresión |
| 7 | Cobertura | Máximo del 300 % en toda la página |
| 8 | Espacios de color | Ningún objeto, imagen ni transparencia en RGB o Lab |
| 9 | Texto negro | 100 K puro con sobreimpresión (modo 1) |
| 10 | Negro enriquecido | C60 M40 Y40 K100 solo en fondos |
| 11 | Texto calado | Desde 9,5 pt y peso Regular o superior |

### 8.3 Imágenes, retícula y tipografía

| N.º | Punto | Criterio |
|---|---|---|
| 12 | Resolución | 300 ppp a tamaño final; ninguna imagen por debajo de 240 ppp |
| 13 | Vectores | Logotipos, filetes y códigos sin rasterizar; filetes desde 0,25 pt |
| 14 | Márgenes y caja | Interior 18 mm, exterior 15 mm, superior 15 mm, inferior 20 mm; caja de 177 × 245 mm (§3.2) |
| 15 | Área libre, folio y sección | Área libre mínima del 25 % por doble página; folio y sección en el margen inferior exterior (§3.2) |

### 8.4 Lomo, cubierta y barniz

| N.º | Punto | Criterio |
|---|---|---|
| 16 | Zona del lomo | Texto, rostros, logotipos y códigos a 10 mm o más |
| 17 | Doble página | Compensación de 3 mm por lado aplicada |
| 18 | Cubierta y lomo | Exterior de 429 × 286 mm con sangrado e interior del mismo formato; lomo de 3 mm en color plano, sin texto |
| 19 | Barniz UV | Separación «UV» al 100 % en sobreimpresión, vectorial, con trazo mínimo de 0,3 mm |
| 20 | Laminado y zona NFC | Laminado mate solo en la cara exterior; C3 sin laminado ni barniz |

### 8.5 Códigos QR y etiqueta NFC

| N.º | Punto | Criterio |
|---|---|---|
| 21 | Unicidad y tamaño | Un código por pieza, sin reutilización; lado de 18 mm o más y silencio de cuatro módulos |
| 22 | Corrección y contraste | Nivel M, o Q con recuadro claro sobre fondo oscuro; módulos en 100 K |
| 23 | Microtexto | «Acceso a ficha, precio vigente y video» y dirección corta junto a cada código |
| 24 | Matriz y destinos | Códigos y destinos coincidentes con `DOC-E-18`; destinos activos |
| 25 | Zona NFC | 40 × 40 mm en C3, a 30 mm o más del lomo y 20 mm o más de los cortes, con guía circular, símbolo N y rótulo |
| 26 | Interferencias | Sin tintas metálicas ni estampados en caliente en la zona ni en su proyección sobre C4 |
| 27 | Lectura QR | Cuatro equipos sobre el ferro, sin fallos (`DOC-E-16`) |
| 28 | Etiquetas NFC | Ensayo de verificación del grupo de muestreo sin fallos (`DOC-E-16`) |

### 8.6 Contenido y pruebas

| N.º | Punto | Criterio |
|---|---|---|
| 29 | Mancheta | Completa conforme a `REG-LG-ST-2026-01` |
| 30 | Sumario | Títulos y páginas coincidentes con el mapa de paginación y el archivo |
| 31 | Rotulado de pauta | «Publicidad» o «Contenido patrocinado» en toda página pagada; separación de cuatro páginas verificada |
| 32 | Cero precios | Ningún precio impreso; leyenda de vigencia en toda mención de descuentos, cuotas o beneficios |
| 33 | Pruebas | Ferro digital y prueba de color aprobados (sección 9) |

## 9. Pruebas de preimpresión

### 9.1 Pruebas y verificaciones

- **Ferro digital contractual:** imposición de los tres pliegos de 16 y de la cubierta a partir de `DOC-E-15`, con marcas, tira de control y orden del mapa de paginación; impresión de verificación a escala 100 % para la lectura de QR y la revisión del lomo.
- **Prueba física:** cubierta (exterior e interior), pliego 1-16 y pliego 17-32 con ADN Gamer en modo oscuro, sobre soporte de prueba con tira de control.
- **Prueba de color certificada:** conforme a ISO 12647-7, con tira de control, valores medidos adjuntos y cumplimiento de las tolerancias de la norma frente a la caracterización de referencia.
- **Lectura QR:** sobre el ferro, en cuatro equipos (6.5).
- **Etiquetas NFC:** ensayo de verificación (7.5) de 20 etiquetas del lote, aplicadas sobre la prueba de C3 y leídas en cuatro equipos.
- **Acta `DOC-E-16`:** equipos y versiones, resultado por código, mediciones de color, incidencias y firmas de DA y PD.

### 9.2 Secuencia de S7 y S8

| Día | Actividad | Responsable | Registro |
|---|---|---|---|
| Lunes de S7 | Archivos definitivos (versión candidata); ferro digital y pruebas físicas; lectura QR y ensayo NFC | DA · PD | `DOC-E-15`, `DOC-E-16` |
| Martes de S7 | G4 por la mañana; asignación de `vFinal`; inicio de impresión con aprobación de arranque de cubierta y pliegos frente a la prueba | DE · DA · EV | `DOC-E-05`, `DOC-E-15` |
| Miércoles de S7 | Fin de impresión de tripa y cubierta; laminado mate y barniz UV | Imprenta | — |
| Jueves de S7 | Encuadernación PUR | Imprenta | — |
| Viernes de S7 | Aplicación de etiquetas NFC; control de calidad; muestreo NFC 1/50; sellado de cajas por canal y sede | Imprenta · DA · PD | `DOC-E-17` |
| Lunes de S8 | Entrega en almacén central antes de las 12:00; recepción | Imprenta · DA · CC | `DOC-E-17` |
| Lunes a miércoles de S8 | Holgura de producción | DA | `DOC-E-05` |
| Miércoles de S8 (D-1) | Despacho a sedes en cajas selladas y al evento | CC | `DOC-E-24` |

Ajustes por feriado (lunes de S7 de la Edición 03 y jueves de S7 de la Edición 04) conforme a `CAL-ED-ST-2027-01`, con apoyo en la holgura de producción.

## 10. Control de calidad del tiraje (`DOC-E-17`)

Responsable: DA; muestreo NFC a cargo de PD. Control en la imprenta el viernes de S7, recepción el lunes de S8 y acta previa a G5.

### 10.1 Controles en la imprenta

Inspección de 50 ejemplares tomados de cajas y posiciones distintas de la tirada (inicio, mitad y final).

| Control | Criterio de aceptación |
|---|---|
| Conteo | Ejemplares por caja y total iguales a la orden |
| Encuadernación | Apertura plana en págs. 2-3, 24-25 y 46-47 de cinco ejemplares y tracción manual de hojas, sin desprendimiento ni fisura del lomo |
| Corte | 210 × 280 mm, con tolerancia de 1 mm |
| Registro | Desviación máxima de 0,1 mm entre separaciones |
| Color | ΔE*ab igual o inferior a 5 en los sólidos de la tira, frente a la prueba, bajo luz D50 (ISO 3664) |
| Cubierta | Laminado sin burbujas ni desprendimientos; barniz UV con registro de 0,3 mm y adhesión conforme (4.2) |
| Etiqueta | Posición dentro de la guía circular y adhesión permanente |

### 10.2 Muestreo NFC (uno por cada cincuenta)

- **Cantidad:** un ejemplar por cada cincuenta etiquetados de cada caja, con mínimo de uno por caja y selección al azar (referencia: 40 ejemplares por edición con 2.000 etiquetados; 100 con tiraje completo de 5.000).
- **Ensayo:** los cinco controles de 7.5, a cargo de PD con el lector de referencia.
- **Criterio de aceptación:** cero fallos en el grupo de muestreo.
- **Ante un fallo:** verificación del 100 % de la caja; retiro de la etiqueta defectuosa; sustitución por otra verificada del repuesto del lote o, sin repuesto, entrega del ejemplar sin NFC con registro del faltante por lote; aviso al proveedor para la reposición (`PLI-PV`).

### 10.3 Sellado, custodia y recepción

- **Sellado:** cajas selladas por canal y sede, con precinto numerado y rótulo (edición, canal, sede, cantidad y lote NFC), sin imagen de portada.
- **Custodia confidencial:** acceso restringido en la imprenta entre el sellado (viernes de S7) y la entrega (lunes de S8); cajas selladas hasta la hora cero; ejemplares del evento entregados tras la hora cero (§5.3).
- **Recepción en almacén central (lunes de S8, antes de las 12:00):** conteo por caja frente al rótulo, integridad de los precintos y cantidad total; DA con CC.
- **Rechazo parcial:** repetición de los trabajos dentro de la holgura de producción (lunes a miércoles de S8), con despacho no posterior al miércoles de S8 (D-1).

### 10.4 Acta de recepción y control

- **Contenido:** fecha y hora, cantidades, resultado de cada control, muestreo NFC (UID y contadores), incidencias, acciones y firmas de DA y del representante de la imprenta.
- **Efectos:** acta conforme como condición del segundo pago a la imprenta (`PLI-PV`); conteo por canal y sede como insumo de `DOC-E-24`.

## 11. Especificación de materiales para anunciantes

Ficha técnica completa de la síntesis de `KIT-CO-ST-2026-01`, para las piezas de pauta (C2-01, 14-15, 26-27 y C4) y los publirreportajes.

### 11.1 Formatos

| Formato | Corte final | Con sangrado | Zona segura |
|---|---|---|---|
| Página | 210 × 280 mm | 216 × 286 mm | 190 × 260 mm |
| Doble página | 420 × 280 mm | 426 × 286 mm | Dos de 190 × 260 mm |

- **Zona segura:** 10 mm de los cortes y del lomo para texto, rostros, logotipos y códigos.
- **Doble página:** entrega como una sola página; partición y compensación de 3 mm por lado en el lomo por DA.

### 11.2 Archivo y color

- **Formato:** PDF/X-4 con TrimBox y BleedBox definidos; sin marcas de impresión (corte, registro, tiras) dentro del formato.
- **Imágenes y fuentes:** 300 ppp a tamaño final (mínimo, 240 ppp); fuentes incrustadas; transparencias vivas admitidas.
- **Color:** CMYK FOGRA39 con cobertura máxima del 300 %; tintas planas convertidas a CMYK; texto negro 100 K con sobreimpresión; negro enriquecido (C60 M40 Y40 K100) solo en fondos.
- **Fondo oscuro:** admitido en 26-27 (pauta contigua a ADN Gamer), con texto claro desde 9,5 pt (§3.4).
- **Rotulado:** banda libre de 6 mm en el borde superior de la zona segura, para el rótulo «Publicidad» o «Contenido patrocinado» incorporado por DA en cada página (§2.5).

### 11.3 Restricciones de contenido

- **Precios y financiamiento:** cero precios impresos; leyenda de vigencia (texto tipo de `REG-LG`) en toda mención de descuentos, cuotas o beneficios, con cuerpo mínimo de 7 pt; aprobación vigente de la plataforma aliada en menciones de financiamiento (§4.4).
- **C4:** proyección de la zona NFC de C3 sin tintas metálicas ni estampados en caliente (7.6).
- **QR del anunciante:** solo con parámetros y archivo vectorial asignados por PD (sección 6); destino aprobado en G3; sin códigos propios ni acortadores externos.

### 11.4 Entrega y aprobación

- **Entrega:** lunes de S6 (fechas por edición en `KIT-CO` y `CAL-ED`), por conducto de CC.
- **Verificación técnica:** DA, con informe al anunciante el miércoles de S6 y reenvío corregido el jueves de S6.
- **Aprobación:** escrita de cada marca en G3; archivo en `DOC-E-13`; integración en `DOC-E-15`.
- **Nombre de archivo:** `ST-RV-E<ed>_<págs>_pauta-<marca>_v<n>`, con `<marca>` en minúscula, sin acentos ni espacios.

## 12. Control del documento

### 12.1 Relación con otros documentos

- **Fuente única:** especificación del código QR, parámetros UTM, etiqueta NFC y ensayo de verificación NFC; remisión desde `KIT-CO`, `MAN-EX-ST-2026-01`, `MAN-MD`, `MAN-ID` y `DOC-E-18`.
- **Remisiones:** `MAN-ID` (composición gráfica), `PLI-PV` (contratación y condiciones comerciales de proveedores), `REG-LG` (contratos, textos legales tipo y términos del beneficio NFC), `PRO-RP` (confidencialidad y hora cero), `PLA-DI-ST-2027-01` (cantidades por lote) y `CAL-ED` (fechas de ciclo).
- **Registros:** `DOC-E-15`, `DOC-E-16`, `DOC-E-17` y `DOC-E-18`.

### 12.2 Revisión y actualización

- **Periodicidad:** anual, tras la Edición 06.
- **Disparadores:** cambio de imprenta, cambio de proveedor NFC y modificación de §3.1 o §3.6.
- **Responsable y registro:** DA, con PD; nueva versión en el Índice Maestro y aprobación de DE.

### 12.3 Firmas

| Elaboración | Revisión | Aprobación |
|---|---|---|
| DA · nombre, cargo y fecha | Nombre, cargo y fecha | DE · fecha |
