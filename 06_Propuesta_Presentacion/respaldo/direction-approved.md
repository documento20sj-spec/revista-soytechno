# direction-approved · Presentación «SoyTechno, la revista»

Archivo de control del método (huashu-design, fase 5). Fecha: 19-oct-2026.

## Direcciones mostradas

| Dirección | Lógica | Archivo | Capturas |
|---|---|---|---|
| A · Escenario | Ruleta: `date +%S` = 53 sobre los cuatro estilos audaces compatibles → «Black Big-Number Stage»; referencia `apple` | `design-demos/A_escenario.html` | `capturas/A_p1.png`, `A_p2.png`, `A_p2b.png`, `A_p3.png`, `A_p1_movil.png`, `A_p2_giro.png` |
| B · Revista-objeto | Referencia real: WIRED (`design-md/wired`) | `design-demos/B_bookazine.html` | `capturas/B_p1.png`, `B_p2.png`, `B_p2b.png`, `B_p3.png`, `B_p1_movil.png`, `B_p2_giro.png` |
| C · Sistema | Mejor diseñador: Massimo Vignelli (manual del metro de Nueva York); referencia de contexto `hp` | `design-demos/C_sistema.html` | `capturas/C_p1.png`, `C_p2.png`, `C_p2b.png`, `C_p3.png`, `C_p1_movil.png`, `C_p2x.png` |

Hojas enviadas al usuario: `capturas/comparativa_direcciones.png` y `capturas/detalle_direcciones.png`.

## Elección del usuario (respuestas literales)

- «¿Qué dirección desarrollo para la versión final?» → «C · Sistema»
- «¿Autorizas descargar fotos, fuentes y GSAP para incrustarlos en el HTML final?» → «Sí, incrustar (Recomendado)»
- «Al terminar, ¿envío la propuesta como adjunto HTML a 03.83.gj@gmail.com?» → «Sí, enviármela»
- «¿La portada de la presentación lleva el nombre de la destinataria?» → «Con su nombre»

## Consecuencias para la ejecución

- Base visual y de navegación: C · Sistema (relato por desplazamiento, índice fijo, retícula visible, anotaciones técnicas, circuito de nodos, despiece).
- Revista: las 24 páginas de `componentes/` con el motor `libro.js`, integradas en el capítulo de la revista.
- Recursos incrustados: 26 fotos, 3 fuentes y 5 archivos de GSAP descargados a `descargas/` con `herramientas/descargar.py`.
- Apertura con «Preparado para Carelys Eljuri».
- Envío final por Gmail web en Chrome, como adjunto, a la dirección del usuario.
