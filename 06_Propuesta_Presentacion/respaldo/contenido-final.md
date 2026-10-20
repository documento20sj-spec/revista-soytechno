# Contenido de la versión completa · «SoyTechno, la revista»

Guion de capítulos para la presentación final. Texto en español, registro impersonal; datos tomados del corpus vigente (rector `DIR-ED-ST-2026-01`, `PLA-FI`, `PLA-DI`, `PRO-RP`, `MAN-EV`, `GUI-NW`, `CAL-ED`, `MAN-MD`). Sin montos en moneda: solo porcentajes, índices, cantidades y fechas. La estructura de navegación depende de la dirección elegida; el contenido no.

## 0. Apertura

- Antetítulo: «Proyecto editorial · Propuesta para evaluación»
- Título: «SoyTechno, la revista»
- Bajada: «Medio propio de SoyTechno, gratuito y bimestral: la exhibición de productos convertida en contenido informativo, estilístico y aspiracional, con acceso a la compra mediante QR y NFC.»
- Promesa: «Tecnología explicada, probada y accesible.»
- Cifras: 6 ediciones al año · 52 páginas por edición · 5.000 ejemplares en la Edición 01 · QR por pieza y NFC por ejemplar · 19:30 del 21-ene-2027, hora cero de la Edición 01.
- Acción: «Abrir la revista»

## 1. El proyecto

- Título: «Un medio propio para una red de veinte tiendas»
- Texto: «SoyTechno opera una red de veinte tiendas especializadas en tecnología, con sedes de alto tráfico en la región capital y comercio electrónico nacional. La revista traslada esa vitrina a un formato coleccionable: contenido que informa, orienta la compra y devuelve tráfico a las tiendas y a la tienda en línea.»
- Ficha del producto (rector §1.2):
  - Naturaleza: medio propietario, multimarca, gratuito y bimestral.
  - Formato: 48 páginas interiores más cubiertas, 210 × 280 mm, estética de libro coleccionable.
  - Phygital: QR por pieza y etiqueta NFC por ejemplar; edición digital interactiva en la hora cero.
  - Extensiones: pódcast, video detrás de cámaras, piezas para redes, revelación de portada y evento de *networking* por edición.
- Cinco ejes comerciales (rector §1.1): Movilidad y telecomunicaciones · Cómputo y Zona Business · Hogar y línea blanca · Zona Gamer · Fidelización y facilidades de compra (Club SoyTechno y cuotas con plataformas aliadas).

## 2. Para quién

- Título: «Tres lectores, un mismo ecosistema»
- Perfiles (rector §1.5):
  - Entusiasta y *gamer* · 18 a 30 años · especificaciones de alto rendimiento, periféricos, puestos de juego y torneos · ADN Gamer, Bajo el Lente, Conexión en Vivo.
  - Profesional y ejecutivo · 28 a 50 años · productividad móvil, automatización, inteligencia artificial aplicada, finanzas para la empresa · Espacio Business, Reportaje Central, Ruta Inteligente.
  - Hogar y estilo de vida · 25 a 55 años · entretenimiento doméstico, domótica, ecosistema familiar, beneficios del Club · Bajo el Lente, Ruta Inteligente, En Primera Fila.
- Audiencias secundarias: comunidades digitales de las personas participantes; fabricantes y aliados; fuerza de ventas.
- Cuatro pilares (rector §2.1), presentes en cada edición y ninguno por encima del 40 % de las páginas editoriales: P1 Innovación, *hardware* y tendencias · P2 Personas, liderazgo y creadores · P3 Cultura digital, entretenimiento y eventos · P4 Finanzas, negocios y economía digital.

## 3. La revista (simulación)

Pliegos seleccionados, con paso de página: C1 portada · C2-01 doble premium (pauta) · 02-03 Sumario y créditos · 04-05 Pulso Techno · 08-09 Bajo el Lente · 16-17 Reportaje Central · 20-21 En Primera Fila · 28-29 ADN Gamer · 36-37 Espacio Business · 40-41 Conexión en Vivo · 44-45 Ruta Inteligente · 48-C3 Última Página y zona NFC · C4 contraportada. Capa activable «Ver retícula» con las 12 columnas, la línea base y anotaciones de las reglas de `MAN-ID`. Nota discreta: «Simulación con imágenes y datos de referencia».

## 4. Arquitectura de 52 páginas

- Título: «52 páginas con lugar fijo para cada cosa»
- Mapa de paginación (rector §4.1): C1 Portada · C2 y 01 Pauta · 02-03 Sumario · 04-07 Pulso Techno · 08-13 Bajo el Lente · 14-15 Pauta · 16-19 Reportaje Central · 20-25 En Primera Fila · 26-27 Pauta · 28-35 ADN Gamer · 36-39 Espacio Business · 40-43 Conexión en Vivo · 44-47 Ruta Inteligente · 48 Última Página · C3 Autopromoción con zona NFC · C4 Pauta.
- Cifras: 52 páginas · 44 editoriales · 7 de pauta (13,5 %) · 1 de autopromoción. Tres pliegos de 16; ADN Gamer entre el segundo y el tercero.
- Reglas: portada no comercializable; cero precios impresos; máximo de 10 páginas de pauta; máximo del 35 % de las páginas pagadas por fabricante; separación mínima de cuatro páginas entre la pauta de una marca y la reseña de un producto propio o competidor.

## 5. Del papel al teléfono

- Título: «Cada página, una puerta a la compra»
- QR por pieza: ficha con precio vigente, video, afiliación al Club SoyTechno o condiciones de financiamiento; un código por pieza, sin reutilización; destino editable tras la impresión; medición `utm_source=revista · utm_medium=qr · utm_campaign=ed<n> · utm_content=p<pág>-<sección>-<pieza>`.
- NFC por ejemplar: edición digital, pódcast, detrás de cámaras, activación del ejemplar en el Club con beneficio canjeable una vez; etiqueta NTAG213 de 25 mm en la zona de contacto de C3; sin datos personales; bloqueo de escritura.
- Implantación: 2.000 ejemplares etiquetados en las Ediciones 01 y 02; tiraje completo desde la Edición 03 si la activación acumulada alcanza el 10 % (decisión del CE en G4 de la Edición 02, 02-mar-2027).
- Metas: escaneo QR ≥ 5 % de ejemplares · activación NFC ≥ 10 % de ejemplares etiquetados · conversión *phygital* ≥ 60 % de sesiones.

## 6. Cómo se hace

Igual que la pantalla 3 de `contenido-borradores.md` (fases, compuertas G0-G5 con criterios, semana 7, semana 8 y fechas de la Edición 01).

## 7. Hora cero

- Título: «19:30. La portada se descubre en escena»
- Secuencia (rector §5.3 y `PRO-RP` §6):
  - S1 a S4: selección del personaje con acuerdo de confidencialidad; sesión con fotografía, video y pódcast.
  - S6 y S7: campaña de expectativa sin mostrar la portada; ejemplares en cajas selladas.
  - 19:28: cuenta regresiva de 120 segundos en pantalla LED.
  - 19:30: descubrimiento en escena, con el personaje, en gran formato y en transmisión directa.
  - 19:35: publicación colaborativa simultánea; QR y NFC pasan de la página de espera al contenido; edición digital, pódcast y video detrás de cámaras liberados (bloque de 60 segundos como máximo).
  - 19:36 a 19:40: cuatro verificaciones (publicación visible, lectura QR y NFC en dos iOS y dos Android, carga de la edición digital, lecturas en la analítica).
  - 19:45: conversación en escena grabada como pódcast en vivo.
  - D+1 a D+7: exhibición en sedes, envío al Club, publicaciones de creadores e informe de alcance a 72 h.
- Confidencialidad: acuerdos con personaje, equipo, imprenta y proveedores; pruebas con marca de agua; ante filtración, adelanto controlado de la revelación digital sin mover la fecha del evento.

## 8. El evento

- Título: «Una noche para conectar marcas, clientes y creadores»
- Formato: Día D de 18:00 a 22:00; 150 a 200 invitados (Ediciones 01 a 05); gala de 250 a 300 con balance del año (Edición 06); acceso con invitación nominativa y QR; sin venta de entradas.
- Invitados: 30 % clientes de alto valor y Club SoyTechno · 20 % empresas · 20 % marcas y proveedores · 20 % creadores, *influencers* y prensa · 10 % personaje, entrevistados, equipo e institucionales.
- Agenda: 18:00 acreditación y zonas de experiencia · 18:45 *networking* en mesas de afinidad · 19:30 revelación · 19:45 conversación en escena (pódcast en vivo) · 20:20 rueda de negocios y demostraciones · 21:00 entrega de ejemplares con NFC y sorteos · 22:00 cierre y encuesta.
- Relación: credencial por grupo con nombre, empresa e interés; cinco mesas de afinidad (Business, Gamer, Hogar, Creadores, Finanzas); citas de diez minutos preagendadas; directorio digital con consentimiento durante dos semanas; seguimiento en la semana siguiente.
- Patrocinio: tres a cinco zonas de experiencia con guion aprobado; sin venta en el evento; confirmación en G3 con el 70 % del costo cubierto o formato reducido de 80 a 100 invitados.

## 9. Calendario 2027

| Edición | Bimestre | Día D | Foco temático | Evento |
|---|---|---|---|---|
| 01 | Enero-febrero | 21-ene-2027 | Novedades del año; productividad, finanzas personales y organización | Estándar |
| 02 | Marzo-abril | 11-mar-2027 | Movilidad, fotografía móvil, vestibles, creadores de viaje | Estándar |
| 03 | Mayo-junio | 29-abr-2027 | Hogar: televisión, audio, línea blanca, domótica | Estándar |
| 04 | Julio-agosto | 01-jul-2027 | Universo *gamer*, deportes electrónicos, *streaming* | Estándar |
| 05 | Septiembre-octubre | 26-ago-2027 | Cómputo, educación, emprendimiento, pymes | Estándar |
| 06 | Noviembre-diciembre | 04-nov-2027 | Guía de regalos, financiamiento responsable, personalidades del año | Gala |

Regla: cada Día D al menos diez días antes de la fecha comercial principal de su ventana. Pausas operativas: 21-dic-2026 a 03-ene-2027 y 31-may a 13-jun-2027, sin mover ningún Día D.

## 10. Distribución

- Título: «5.000 ejemplares donde está el cliente»
- Reparto (rector §3.7 y `PLA-DI` §1.1): 58 % sedes VIP (2.900) · 15 % compras de alto valor (750) · 12 % Club SoyTechno de mayor nivel (600) · 6 % evento (300) · 6 % aliados, fuerza de ventas, entrevistados y prensa (300) · 3 % archivo y depósito legal (150).
- Sedes VIP: dos criterios como mínimo entre tráfico en el cuartil superior, zona de marca o categoría y ticket superior a la media; Sambil Chacao y City Market fijas; exhibición desde D+1 con reposición y acta semanal de conteo.
- Ajuste: tiraje con variación máxima del 20 % por edición según la distribución efectiva (meta ≥ 85 %).
- Circulación: de D+1 al Día D siguiente (de 7 a 11 semanas según la edición).

## 11. Modelo comercial

- Título: «Pauta con reglas claras, patrocinio con retorno medible»
- Posiciones: C2-01 doble premium del patrocinante principal (exclusividad de categoría y paquete del evento) · 14-15 pauta I (movilidad, cómputo o televisión) · 26-27 pauta II (*gamer* o alto rendimiento) · C4 marca aliada de línea blanca o televisión.
- Paquetes (índice de tarifa, Presenta = 100; `PLA-FI` §5.2): Presenta 100,0 (gala 155,6) · Afinidad 44,4 (gala 60,0) · Comunidad 13,3.
- Composición del ingreso potencial: revista 34,9 % · evento 65,1 %.
- Independencia: sin intervención de marcas en selección de productos, textos ni veredictos; rótulo «Publicidad» o «Contenido patrocinado» en toda página pagada.

## 12. Sostenibilidad

- Título: «Inversión de mercadeo con cobertura creciente»
- Estructura del costo base de una edición estándar con NFC completo (`PLA-FI` §2.2): evento 35,3 % · impresión 25,9 % · equipo y coordinación 15,3 % · contenido y corrección 6,6 % · fotografía y audiovisual 4,7 % · distribución 4,7 % · diseño 3,3 % · etiquetas NFC 2,8 % · producción digital 1,4 %.
- Cobertura del plan anual base 2027 (ingreso de pauta y patrocinio sobre el costo total con contingencia): Ed. 01 52,0 % · Ed. 02 52,0 % · Ed. 03 54,4 % · Ed. 04 54,4 % · Ed. 05 54,4 % · Ed. 06 55,0 % · total 53,8 % (meta del primer año: 50 %). Aporte de SoyTechno: 46,2 %.
- Trayectoria de referencia hacia el 70 % desde el segundo año: 53,8 % → 54,8 % (fin de la tarifa de lanzamiento) → 63,7 % (inventario completo del evento) → 65,9 % (ampliaciones con pauta) → 71,4 % (actualización tarifaria del 10 %).
- Conclusión: programa sostenido como inversión de mercadeo de SoyTechno, con metas de cobertura del 50 % el primer año y del 70 % desde el segundo.

## 13. Indicadores

Rector §1.4:
- Posicionamiento: alcance de la revelación a 72 h y lecturas digitales únicas, con crecimiento del 10 % por edición.
- Activación comercial: distribución efectiva ≥ 85 % · escaneo QR ≥ 5 % · conversión *phygital* ≥ 60 % · ventas atribuidas por edición.
- Fidelización: activación NFC ≥ 10 % · afiliaciones al Club con crecimiento del 10 % por edición.
- Comunidad: asistencia ≥ 75 % de confirmados · contactos de negocio · audiencia del pódcast a 30 días con crecimiento del 10 %.
- Fabricantes: satisfacción ≥ 4 sobre 5.
- Sostenibilidad: ingresos de pauta y patrocinio ≥ 50 % del costo el primer año y ≥ 70 % desde el segundo.
- Calidad: erratas posteriores a la impresión ≤ 3 por edición · seis de seis Días D en fecha.
Reporte de 72 h en D+3 e informe consolidado en la semana 4 del ciclo siguiente.

## 14. Gobierno y documentación

- Consejo Editorial: Dirección Editorial (presidencia), Gerencia de Mercadeo, Coordinación Comercial y Alianzas, Gerencia de Compras o Categorías; sesiones en S1 (G0) y en G4.
- Ocho roles con un único responsable por entregable: DE, CR, DA, PF, CC, EC, PD, EV.
- Sistema documental vigente desde el 18-oct-2026: Documento Rector e Índice Maestro; Bloque I Corpus permanente (MAN-ID, GUI-PP, PRO-PR, KIT-CO, REG-LG, CAL-ED); Bloque II Programa de lanzamiento (PRO-RP, MAN-EV, GUI-NW, GUI-CR, MAN-EX); Bloque III Gestión del programa (EXP-ID, PLA-FI, MAN-OR, MAN-MD, PLA-CM, PLA-DI, PLI-PV); Bloque IV expediente por edición (DOC-E-01 a DOC-E-28).

## 15. Próximos pasos

- Aprobación del proyecto y del presupuesto anual por el Consejo Editorial.
- Registro de la marca y cabecera (EXP-ID) y contratación de proveedores (PLI-PV) en noviembre de 2026.
- G0 de la Edición 01: 20-nov-2026.
- Día D de la Edición 01: jueves 21-ene-2027, 19:30.
