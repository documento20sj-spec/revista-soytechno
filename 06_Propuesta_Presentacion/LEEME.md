# Propuesta de presentación · SoyTechno, la revista

Carpeta del entregable para Carelys Eljuri y de todo lo que lo respalda.

## Entregable

`SoyTechno_Propuesta_Revista.html` es un solo archivo de 4,47 MB. Lleva dentro las fotografías, las tipografías y GSAP, así que funciona sin conexión.

Cómo abrirlo:

- **En computador:** doble clic. Se abre en Chrome, Safari, Edge o Firefox con todas las animaciones.
- **En teléfono:** los visores de adjuntos no ejecutan JavaScript: Gmail, Archivos y Vista rápida en iPhone, y el visor HTML de Android. Por eso ahí no hay animaciones, la revista no aparece y las fotos no cargan. Para verla completa en el teléfono, el archivo tiene que abrirse desde una dirección web (http o https) en Safari o Chrome.

## Respaldo (`respaldo/`)

| Carpeta o archivo | Contenido |
|---|---|
| `construir_presentacion.py` | Ensamblador. Con `--incrustar` mete fotos, tipografías y GSAP en el HTML. |
| `final/` | Plantilla de la dirección C: `hacer_plantilla.py`, capítulos (`capitulos-a.html`, `capitulos-b.html`, `capitulos-c.html`, `capitulos.css`, `capitulos.js`) y `plantilla.html`, que se genera. |
| `componentes/` | Revista simulada: `construir_revista.py`, `revista.css`, `revista-paginas.css` y el banco de páginas `revista-paginas.html`. Gráficos (`graficos.py`, `graficos.css`, `graficos.js`) y diagramas (`diagramas.py`, `diagramas.css`). `libro.*` y `construir_prueba.py` son un motor anterior y no se usan. |
| `descargas/fotos/` | 26 fotografías WebP de Unsplash, de las que 16 se usan en el entregable. |
| `descargas/fuentes/` | Archivo, Source Serif 4 y JetBrains Mono en WOFF2, con `LICENCIAS.md` (OFL). |
| `descargas/gsap/` | GSAP 3.13.0 y sus plugins. El entregable usa gsap, ScrollTrigger y SplitText. |
| `assets/logos/` | Logotipos de SoyTechno en SVG: lockup, logotipo, isotipo e icono. |
| `herramientas/` | `qr.py` (genera los códigos QR), `leerqr.swift` (los verifica), `descargar.py` y `hoja_direcciones.py`. |
| `design-demos/`, `capturas/` | Las tres direcciones propuestas (A Escenario, B Bookazine, C Sistema) y sus capturas. |
| `_fotos/` | Hojas de contacto y catálogo de fotografías. |
| `brand-spec.md`, `design-spec.md`, `contenido-borradores.md`, `contenido-final.md`, `direction-approved.md` | Especificaciones de marca y diseño, guion de contenidos y decisiones aprobadas. |

## Reconstruir

Desde esta carpeta, en este orden:

```bash
python3 respaldo/final/hacer_plantilla.py
python3 respaldo/construir_presentacion.py --incrustar
```

El HTML de salida se escribe aquí mismo. No hay que editarlo a mano: los cambios se hacen en `respaldo/final/` y `respaldo/componentes/`.

## Licencias

- **Tipografías:** SIL Open Font License 1.1.
- **GSAP:** licencia estándar de GSAP, gratuita también para uso comercial.
- **Fotografías:** licencia de Unsplash. En la revista simulada figuran como «imagen de referencia».
