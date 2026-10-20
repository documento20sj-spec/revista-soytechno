# Seguimiento del proyecto · Revista SoyTechno

Documento interno de continuidad. Actualizado el 19-oct-2026, al cierre de la presentación (solo falta el envío por correo). Leer completo antes de retomar cualquier tarea.

## 1. Cómo retomar

1. Leer este archivo y la memoria del proyecto (`MEMORY.md`).
2. Comprobar el estado real de los archivos con los comandos de la sección 6. No asumir que lo marcado como «en curso» terminó.
3. Continuar por la sección 5 (el corpus de la sección 4 está cerrado).
4. Al cerrar cada paso, actualizar este archivo: marcar el paso y anotar fecha y resultado.

## 2. Estructura y herramientas

- `00_Indice_Documental/`: Índice Maestro IND-ED-ST-2026-01 (`_v1`), en HTML y PDF.
- `01_Documento_Rector/`: Documento Rector DIR-ED-ST-2026-01 (`_v1`), en HTML y PDF de 5 páginas. Cuerpos fuente en `05_Herramientas/src/`.
- `02_Corpus_Documental/B1…, B2…, B3…/<CÓDIGO>_<Titulo>/`: los 18 documentos del corpus. El `.md` es la fuente oficial; el `.html` se genera a su lado. Sin PDF, por decisión del usuario.
- `03_Ediciones/`: plantillas y expediente por edición (Bloque IV del índice), vacíos a propósito: plantillas PLT-DOC con fechas meta desde el 13-nov-2026 y expediente de la Edición 01 durante su ciclo, desde el 16-nov-2026.
- `06_Propuesta_Presentacion/`: presentación para Carelys Eljuri. Contiene el entregable `SoyTechno_Propuesta_Revista.html`, `LEEME.md` y `respaldo/` con todas sus fuentes y recursos. `respaldo/` estaba antes en `05_Herramientas/presentacion/` y se movió el 19-oct-2026.
- `04_Investigacion/`: material de investigación. Nunca se cita en entregables.
- `05_Herramientas/construir.py`: genera los HTML del corpus y el HTML y PDF del rector y del índice.
  - `construir.py <CÓDIGO>`: un documento.
  - `construir.py --md`: todo el corpus.
  - `construir.py IND-ED-ST-2026-01 DIR-ED-ST-2026-01`: dirección, con salida `_v1` ya configurada.
- `05_Herramientas/redaccion/`:
  - `GUIA_REDACCION.md`, `PARAMETROS.md` y `specs/`: base de redacción.
  - `revisar.py`: verificador de redacción.
  - `normalizar.py`: pone los códigos en monoespaciada.
  - `consistencia.py`: contrasta fechas e importes.
  - `verificar_movil.py`: lectura a 375 px.
  - `actualizar_indice.py`: pasa el índice a «Vigente».
  - `referencias/`: textos de apoyo.

## 3. Decisiones vigentes (no reabrir)

- **Nombre:** la revista se llama **SoyTechno**. Sin nombres alternativos. «Revista Corporativa SoyTechno» es la denominación institucional; «Una publicación de SoyTechno» es la leyenda de editor.
- **Datos económicos:** solo en porcentajes. Ningún monto en moneda en los documentos. Los montos van solo en los registros de cada edición y en las propuestas comerciales.
- **Contenidos excluidos:** sin BNC ni tarjeta de marca compartida. Sin nombres de terceros investigados, herramientas ni historial de cambios en los entregables.
- **Registro:** normativo-impersonal estricto (formas nominales, infinitivos y «se»).
- **Compuertas:** G0 el viernes de S1, en la sesión del CE; G1 el viernes de S4; G2 y G3 el viernes de S6; G4 el martes de S7, en la sesión del CE; Día D el jueves de S8; G5 en D+1.
- **Producción:** toda dentro de S7. Archivos el lunes; G4 e impresión el martes; laminado y barniz el miércoles; encuadernación el jueves; NFC, control y sellado el viernes. Entrega en almacén el lunes de S8 y despacho el miércoles de S8.
- **Contratación comercial:** pauta y paquetes Presenta y Afinidad antes de G0. Patrocinio del evento y paquete Comunidad antes de G1. Segundo pago el día hábil anterior a G4. Cancelación sin cargo hasta G0 (pauta) o G1 (evento).
- **Portadas 2027:** persona en las ediciones 01, 03 y 05; producto en las 02, 04 y 06 (`GUI-CR`).
- **Pedidos de etiquetas NFC:** 30-nov-2026, 08-mar-2027 y 02-jul-2027 (el 05-jul es feriado).
- **Índice:**
  - DOC-E-10: aprueba DA y colabora CR.
  - DOC-E-22: compuerta de G0 a G3.
  - Fichas de EXP-ID, KIT-CO y PLA-FI ajustadas por el script.
- **Formato reducido del evento:** lo deciden CC y EV en G3, con informe al CE.

## 4. Corpus: cerrado el 18-oct-2026

- [x] 18 documentos redactados con agentes y revisados uno a uno con lectura completa (PRO-PR, MAN-ID, KIT-CO, MAN-EX, PLA-CM, PLA-DI, PRO-RP, GUI-CR, MAN-EV, GUI-NW, EXP-ID, REG-LG, CAL-ED, PLA-FI, GUI-PP, PLI-PV, MAN-OR y MAN-MD).
- [x] Índice actualizado con `actualizar_indice.py`: 20 documentos vigentes (DIR, IND y los 18 del corpus) y 1 programado (plantilla del expediente por edición).
- [x] Rector e índice emitidos con nombre `_v1`, en HTML y PDF: rector de 5 páginas («extensión conforme») e índice de 16 páginas.
- [x] Archivos antiguos sin `_v1` del rector y del índice movidos a `~/.Trash/Revista_Carelis_depuracion_2026-10-18/` y anotados en su `MANIFIESTO.tsv`.
- [x] Verificación final del conjunto:
  - `normalizar.py` y `revisar.py` sobre los 18 `.md`: sin incidencias.
  - `construir.py --md`: 18 HTML regenerados.
  - `verificar_movil.py`: 18 de 18 sin desplazamiento horizontal ni tablas desbordadas a 375 px; letra mínima de 13,1 px.
  - `consistencia.py`: sin importes; las fechas «no previstas» son derivadas y se comprobaron una a una (día de la semana, semana del ciclo, pausas y ajustes por feriado). Sin discrepancias.
- [x] Memoria actualizada: índice v1.0 con 20 vigentes y nombres `_v1`.

Entregables vigentes:

- `00_Indice_Documental/IND-ED-ST-2026-01_Indice_Maestro_v1.html` y `.pdf`
- `01_Documento_Rector/DIR-ED-ST-2026-01_Documento_Rector_v1.html` y `.pdf`
- `02_Corpus_Documental/B1…, B2…, B3…/<CÓDIGO>_<Titulo>/<CÓDIGO>_<Titulo>_v1.md` y `.html` (18 documentos)

## 5. Encargo siguiente: presentación de propuesta para Carelys Eljuri

Petición del usuario del 18-oct-2026. Presentación profesional en HTML del proyecto, para que Carelys Eljuri lo evalúe.

Orden fijado por el usuario: la presentación empieza solo cuando el corpus esté terminado, revisado y consolidado (sección 4 completa).

Identidad corporativa: carpeta `SoyTechno_logo_vector/` en la raíz del proyecto.
- Hoja de marca: `SoyTechno_hoja_de_marca.pdf`.
- Paquete `pack/` con lockup, logotipo, isotipo e icono, en SVG y PNG de 6000 px, en azul, negro y blanco.
- Paleta oficial:
  - `#0057A6` azul SoyTechno
  - `#1B6BD6` azul luz
  - `#001433` azul noche
  - `#0E0E12` negro
- Reglas de uso:
  - Área de respeto igual al ancho de la «O».
  - Sin deformar, inclinar ni recolorear fuera de la paleta.
  - Sobre foto, versión blanca con velo oscuro de al menos el 40 %.
  - Lockup de 120 px como mínimo en pantalla.
- Propuesta opcional para `MAN-ID` §4.1: incorporar `#0057A6` como valor del Azul SoyTechno, con ratificación del manual corporativo.

Estado del protocolo de diseño (18-oct-2026):

- Fase 1 (`ui-ux-pro-max`) hecha. Base local: producto «Magazine» con estilo Swiss Modernism 2.0 + Motion-Driven y patrón «Scroll-Triggered Storytelling»; estilos «Editorial Grid / Magazine», «Minimalism & Swiss», «Parallax Storytelling»; tríada tipográfica serif + mono validada (se mantiene Archivo / Source Serif 4 / JetBrains Mono del `MAN-ID`); presets GSAP (SplitText por caracteres con expo.out 0,6 s y stagger 0,015 s; revelado al desplazar con y 12 px y 0,35 s; fijación con scrub 1 y como máximo dos secciones; transición con Flip expo.inOut 0,6 s); UX: teclado, foco visible, movimiento reducido, carga diferida; gráficos: parte del todo en anillo o barra 100 % con etiquetas. Sin coincidencia en la base para contadores numéricos (se usa criterio general).
- Fase 2 (`huashu-design`) hecha: el usuario eligió la dirección C. Carpeta de trabajo, hoy `06_Propuesta_Presentacion/respaldo/`:
  - `brand-spec.md`, `design-spec.md`, `contenido-borradores.md`, `assets/logos/`.
  - Tres direcciones en `design-demos/`, con capturas en `capturas/`:
    - A «Escenario»: ruleta, `date +%S` = 53, estilo «Black Big-Number Stage», diapositivas.
    - B «Bookazine»: referencia real verificada, la revista como objeto.
    - C «Sistema»: mejor diseñador, relato por desplazamiento.
  - 19-oct-2026: tres agentes relanzados con referencias distintas de la biblioteca local `design-md`: A con `apple`, B con `wired` y C con `hp`.
  - 19-oct-2026: revista simulada construida en `respaldo/componentes/`, válida para cualquier dirección.
    - Generador `construir_revista.py` con hojas `revista.css` y `revista-paginas.css`.
    - 24 páginas en 13 pliegos fieles al `MAN-ID`: medidas en mm, retícula de 12 columnas, estilos `ST-`, folios, pestañas, QR reales y zona NFC en C3.
    - Banco de revisión `revista-paginas.html` y fragmento `revista-fragmento.html`.
  - Motor de paso de página `libro.js` y `libro.css` (GSAP + Draggable): hojas 3D con anverso y reverso, sombra dinámica, arrastre, teclado y modo de una página en teléfono. Probado con `construir_prueba.py` y `libro-prueba.html`.
  - 19-oct-2026: las tres direcciones se mostraron al usuario (`capturas/comparativa_direcciones.png`). Respuestas del usuario:
    - Dirección: **C · Sistema** (Vignelli).
    - Descargas: autorizadas y hechas en `respaldo/descargas/`: 26 fotos, 3 fuentes y 5 archivos de GSAP, con firmas verificadas.
    - Envío: sí, a su correo, como adjunto desde Gmail web.
    - Portada: con «Preparado para Carelys Eljuri».
    - Registro en `respaldo/direction-approved.md`.
  - Construcción final: plantilla basada en `design-demos/C_sistema.html` más los componentes, con el ensamblador `respaldo/construir_presentacion.py` (`--incrustar`). Salida: `06_Propuesta_Presentacion/SoyTechno_Propuesta_Revista.html`.

Estado al 19-oct-2026: presentación terminada y verificada; falta solo el envío por correo.

- Reconstruir siempre en este orden, desde `06_Propuesta_Presentacion/` (detalle en su `LEEME.md`):
  - `python3 respaldo/final/hacer_plantilla.py`: convierte `design-demos/C_sistema.html` en `final/plantilla.html`, con los capítulos `final/capitulos-a/b/c.html`, `capitulos.css` y `capitulos.js`.
  - `python3 respaldo/construir_presentacion.py --incrustar`: genera el entregable con todo en línea. Pesa 4,47 MB, no pide nada a la red y tiene 16 fotos únicas.
  - Para verlo en el panel del navegador: servidor `propuesta` de `.claude/launch.json` (puerto 8765). Un `file://` de más de 2 MB no abre en el panel.
- Fase 3 (movimiento) hecha. Barras de los gráficos fijadas en cero al arrancar y crecidas con `to()` (con `from()` saltaban). Con un salto por el carril o el teclado, el gráfico ya pasado queda completo. SplitText del titular y arrastre propio del libro revisados sin cambios; Draggable y CustomEase no se cargan.
- Revisión (QA), correcciones:
  - Notas del libro: desplazamientos en escala del libro (`k` = alto del escenario / 676) y recolocadas en 02-03, 08-09, 28-29 y 48-C3. Sin choques con texto, imágenes ni otras notas de 1280×720 a 2560×1440.
  - `.bar` acotado a `header.bar`: las líneas de texto simulado de las páginas de relleno se ven en escritorio, y en teléfono las barras de los paquetes ya no heredan `position: fixed`.
  - Agenda del evento: descripción envuelta en `<span>` (la fila de las 18:45 se partía).
  - Calendario: en pantallas estrechas, la fecha del Día D de la Ed. 06 va a la izquierda del punto (desbordaba 30 px a 390). Sin desplazamiento horizontal de 360 a 1100 px.
  - Teléfono: los pasos del libro quedan como puntos, sin etiquetas.
- Fase 4 (`web-design-guidelines`) hecha:
  - Celdas del mapa que abren pliegos: `<button>` con nombre accesible que empieza por el texto visible.
  - Tabindex itinerante en gráficos y diagramas: de unas 150 paradas de tabulación a 47.
  - Foco visible en barras y columnas.
  - Logotipos en enlaces con nombre: `aria-hidden`.
  - Hora cero en 4,95 s, con «Ver el resultado» para detenerla. Onda NFC de dos pulsos por entrada.
  - Sin transición CSS en los chips que anima GSAP.
  - Espacio duro entre cifra y unidad o signo, aplicado en el ensamblado (`espacios_duros`).
- Envío: hecho el 19-oct-2026 a las 15:50 a 03.83.gj@gmail.com desde Gmail web, con el HTML adjunto (verificado en la bandeja de entrada).
- Teléfono (19-oct-2026): los visores de adjuntos (Gmail, Archivos y Vista rápida en iPhone, visor HTML de Android) no ejecutan JavaScript. En esa vista no hay GSAP, la revista no se construye y las fotos no cargan, porque se insertan por script. Comprobado con una copia sin scripts a ancho de teléfono. Para verla completa hace falta abrirla desde una dirección web en Safari o Chrome. Pendiente: que el usuario decida si se publica y si se prepara una vista sin JavaScript que muestre fotos y páginas.
- Preparado y verificado:
  - `contenido-final.md`: guion de 16 capítulos con datos del corpus.
  - `_fotos/catalogo.md`: unas 40 fotos revisadas.
  - `herramientas/qr.py`: codificador QR propio, validado con Vision (`leerqr.swift`).
- Envío final: el Gmail MCP exige el adjunto en base64, inviable para el HTML. Plan: adjuntar el archivo (menos de 10 MB) desde Gmail web en Chrome (`file_upload`), con confirmación previa del usuario.
- Fotografías, fuentes y GSAP: descargados con permiso del usuario en `respaldo/descargas/` e incrustados en el entregable. El buscador de Unsplash exige verificación antirrobots: no usarlo. Cualquier descarga nueva requiere permiso, indicando nombre, origen y tamaño.
- Hecho verificado: vigésima sucursal de SoyTechno en dic-2024 (DPL News, 16-dic-2024).

Requisitos:

- **Identidad:** logo de SoyTechno e identidad corporativa. Logos en `04_Investigacion/INV-05_SoyTechno/fuentes/identidad/` (`SoyTechno-Logo.jpg`, `logo-blanco.png`, `logo-blanco-sobre-azul.png`, `favicon.webp`).
- **Portada y simulación de la revista:** portada de la revista y simulación completa como si fuera la revista real, fiel a lo redactado en el corpus. Retícula, tipografías Archivo, Source Serif 4 y JetBrains Mono, paleta, secciones y mapa de paginación según `MAN-ID`, el rector §2.2 y §4.1, QR y zona NFC.
- **Animación:** GSAP en la simulación, con paso de página tipo revista, textos animados y secciones interactivas. Alto impacto.
- **Imágenes:** muchas, de referencia, de alta calidad e hiperrealistas. Antes de descargar cualquier archivo, pedir permiso indicando nombre, origen y tamaño. Evaluar recursos disponibles: fuentes con licencia, renders o composiciones propias.
- **Contenido del proyecto en forma visual:** ciclo de 8 semanas, compuertas, revelación de portada, evento y networking, phygital QR/NFC, calendario 2027, distribución, indicadores, gobernanza y estructura documental. Solo porcentajes.
- **Alcance:** el criterio es mío; se puede agregar o quitar contenido.
- **Entrega:** HTML. Al terminar, enviarla por correo electrónico al usuario. Verificar antes el tamaño del adjunto; si es excesivo, enviar enlace o versión ligera.

Protocolo obligatorio (CLAUDE.md del usuario), en este orden:

1. `design-proposal`.
2. `ui-ux-pro-max`.
3. `huashu-design`: tres direcciones para que el usuario elija.
4. `apple-design`, `emil-design-eng` y `animate`, más los skills de GSAP (`gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`, `gsap-utils`, `gsap-performance`).
5. `web-design-guidelines`: auditoría final.

Cualquier fase omitida se informa expresamente.

Ubicación propuesta del entregable: `06_Propuesta_Presentacion/` en la raíz del proyecto.

## 6. Comprobaciones rápidas

```bash
cd "/Users/germanjaraba/Proyectos/Revista Carelis"
ls 02_Corpus_Documental/*/*/*_v1.md | wc -l
for f in 02_Corpus_Documental/*/*/*_v1.md; do python3 05_Herramientas/redaccion/revisar.py "$f" | tail -1; done
python3 05_Herramientas/redaccion/verificar_movil.py
python3 05_Herramientas/construir.py --md
```
