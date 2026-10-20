# Especificación de diseño común · Presentación «SoyTechno, la revista»

Única entrada compartida por las tres direcciones. Leer completa junto con `brand-spec.md` y `contenido-borradores.md` (en esta misma carpeta).

## 1. Qué es

Presentación en HTML del proyecto editorial de la revista SoyTechno: un medio propio, gratuito y bimestral de la red minorista de tecnología SoyTechno (Venezuela), con 52 páginas, 5.000 ejemplares en la Edición 01, código QR por pieza, etiqueta NFC por ejemplar, revelación de portada a las 19:30 del Día D y evento de *networking* por edición. El proyecto está completamente documentado (Documento Rector, Índice Maestro y 18 documentos de aplicación). La presentación debe demostrar dos cosas a la vez: que la revista ya existe como objeto (se puede hojear) y que su operación está bajo control (ciclo, compuertas, responsables).

## 2. Para quién y en qué situación

- Una ejecutiva que evalúa el proyecto y decide si se ejecuta. Recibe el archivo por correo y lo abre sola, sin presentador, en un portátil (distancia de 1 m); puede proyectarlo en una reunión (10 m) o revisarlo en el teléfono.
- Expectativa no dicha: impresión de estudio editorial de primer nivel, no de plantilla; sensación de producto terminado; claridad inmediata sobre qué se aprueba y qué se obtiene.
- Tono: autoridad serena con un pico de entusiasmo en la revista y en la hora cero. Premium, tecnológico, preciso. Nada de exageración comercial («el mejor», «increíble», «revolucionario»).

## 3. Formato del borrador

- Un único archivo HTML autocontenido (CSS y JS en línea), salvo GSAP y las fuentes, que se cargan desde CDN.
- Tres pantallas representativas, con el contenido literal de `contenido-borradores.md`: (1) apertura con la portada de la revista, (2) simulación de la revista con paso de página, (3) ciclo de ocho semanas y compuertas.
- Tamaño de referencia: 1440 × 900 px (escritorio). Debe funcionar sin desbordes a 390 × 844 px (teléfono).
- Parámetros obligatorios de URL para revisión y capturas: `?pantalla=1|2|3` abre directamente esa pantalla; `?captura=1` desactiva animaciones de entrada y muestra estados finales; `?pantalla=2&pliego=0|1|2|3` abre la revista en la portada o en el pliego indicado.

## 4. Sistema obligatorio (no negociable)

- Paleta: la de `brand-spec.md`. Cero colores inventados fuera de ella, salvo transparencias de esos mismos colores. Sin degradados violeta; un degradado solo entre azules de la paleta.
- Tipografía: Archivo (titulares, rótulos, folios), Source Serif 4 (texto y entradillas), JetBrains Mono (datos y fichas). Cargar desde Google Fonts:
  `https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800;900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=JetBrains+Mono:wght@400;500&display=swap`
- Logotipos: incrustar el SVG real de `assets/logos/` (copiar el `<path>` en línea, con su `viewBox`). Prohibido redibujar, deformar o recolorear fuera de la paleta. Sobre foto, versión blanca con velo oscuro del 40 % como mínimo.
- Revista simulada fiel a `MAN-ID`: formato 3:4 (210 × 280 mm), pliego 420 × 280 mm, retícula de 12 columnas con medianil proporcional, folios en el margen inferior exterior, cabecera y cintillo de portada en las posiciones descritas, ADN Gamer en modo oscuro, cero precios, crédito en cada imagen.
- Legibilidad: texto de la presentación de 16 px o más; rótulos de 12 px o más; contraste de 4,5:1 en texto. Dentro de la revista simulada se acepta texto menor porque reproduce la página impresa a escala, pero el titular, la entradilla y los rótulos clave deben leerse en 1440 × 900.
- Accesibilidad: navegación completa con teclado (flechas, Inicio, Fin, Tab), foco visible, `aria-label` en controles sin texto, texto real (no imágenes de texto), `prefers-reduced-motion` con estados finales sin movimiento.
- Movimiento con GSAP 3.13.0 (sin otras bibliotecas):
  `https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js` y, si se usan, `ScrollTrigger.min.js`, `SplitText.min.js`, `Flip.min.js`, `Draggable.min.js`, `CustomEase.min.js` de la misma ruta. Todo movimiento con propósito: revelar jerarquía, simular el objeto, marcar progreso. El paso de página es una rotación 3D real alrededor del lomo, con sombra que cambia durante el giro, cara anterior y posterior, e interrumpible (clic, flechas y arrastre).
- Prohibido: emoji, iconos decorativos en cada título, tarjetas redondeadas con borde lateral de color, SVG que dibuje personas u objetos, datos inventados, montos en moneda, logotipos de terceros, menciones de bancos, primera y segunda persona en los textos.

## 5. Imágenes (reales, compartidas por las tres direcciones)

Fotografías de Unsplash por enlace directo (licencia Unsplash, uso libre). Añadir `?w=<ancho>&q=80&auto=format` según el tamaño de uso. Crédito «Imagen de referencia».

| Clave | URL base | Uso sugerido |
|---|---|---|
| portada | `https://images.unsplash.com/photo-1534528741775-53994a69daeb` | Retrato con luz azul (4:5). Portada C1. Extender el fondo azul lavanda hacia arriba para liberar el 20 % superior de la cabecera |
| reportaje | `https://images.unsplash.com/photo-1512499617640-c74ae3a79d37` | Teléfono en mano con túnel de luz azul (4:3). Apertura 16-17 |
| gamer | `https://images.unsplash.com/photo-1560253023-3ec5d502959f` | Jugador en penumbra azul (3:2). Apertura 28-29 |
| esports | `https://images.unsplash.com/photo-1542751371-adc38448a05e` | Puesto competitivo con pantallas (3:2). Alternativa gamer |
| circuito | `https://images.unsplash.com/photo-1518770660439-4636190af475` | Placa de circuito azul (3:2). Fondo técnico |
| revelacion | `https://images.unsplash.com/photo-1492684223066-81342ee5ff30` | Confeti sobre público (3:2). Hora cero |
| publico | `https://images.unsplash.com/photo-1540575467063-178a50c2df87` | Auditorio en penumbra (3:2). Evento |
| networking | `https://images.unsplash.com/photo-1528605248644-14dd04022da1` | Conversación en evento (3:2). Networking |
| podcast | `https://images.unsplash.com/photo-1590602847861-f357a9332bbc` | Micrófono de estudio (2:3). Pódcast |
| retrato2 | `https://images.unsplash.com/photo-1506794778202-cad84cf45f1d` | Retrato masculino, fondo oscuro (2:3). Entrevista |
| business | `https://images.unsplash.com/photo-1519085360753-af0119f7cbe7` | Retrato ejecutivo, fondo oscuro (2:3) |
| pyme | `https://images.unsplash.com/photo-1556740758-90de374c12ad` | Comercio con tableta (3:2). Espacio Business |

## 6. Motivos visuales disponibles (derivados del contenido)

- El objeto revista: proporción 3:4, pliego abierto, lomo, grosor de 52 páginas, sombra real sobre una superficie.
- La retícula de 12 columnas y la línea base: visibles como guía técnica o como capa activable.
- El isotipo de nodos: trazos de circuito con terminales circulares. Las compuertas G0-G5 pueden leerse como nodos de un mismo circuito («una sola red»).
- La hora cero: 19:30, el instante de la revelación.
- El contacto: la zona NFC circular de 25 mm y el bloque QR por pieza.
- Las pestañas de navegación de la revista: rectángulos azules de 3 × 24 mm escalonados por sección en el borde exterior.

## 7. Entrega de cada dirección

1. `design-demos/<direccion>.html`.
2. Capturas en `capturas/` con Chrome sin interfaz, por ejemplo:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1440,900 --virtual-time-budget=8000 --screenshot="<ruta>.png" "file://<ruta html>?pantalla=1&captura=1"`
   Capturas: pantallas 1, 2 (portada y pliego 1) y 3 a 1440 × 900, y pantalla 1 a 390 × 844.
3. Verificar en las capturas que las imágenes cargan, que no hay desbordes ni textos cortados y que la consola no registra errores.
4. Informe final de 10 líneas como máximo: lógica, referencia o estilo usado, origen de la forma en el contenido, decisiones de movimiento y limitaciones conocidas.
