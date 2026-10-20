# Manual de Medición, Indicadores y Atribución

SoyTechno · Proyecto Editorial · Manual

| Campo | Valor |
|---|---|
| Código | `MAN-MD-ST-2026-01` |
| Versión · fecha | 1.0 · 18 de octubre de 2026 |
| Documento base | `DIR-ED-ST-2026-01` · `IND-ED-ST-2026-01` |
| Clasificación | Uso interno |
| Responsable | PD · Producción Digital y Datos |
| Colaboración | CC · Coordinación Comercial y Alianzas; DE · Dirección Editorial |
| Aprobación | DE · Dirección Editorial |
| Base en el rector | §1.4, §3.6, §3.7, §4.4, §5.3, §5.4 |
| Estándar de redacción | Normativo-impersonal · cero redundancia |

**Objeto:** definición operativa de los indicadores del Documento Rector (§1.4); arquitectura de medición QR y NFC; modelo de atribución de ventas y afiliaciones; panel de control; formato del reporte de 72 horas (`DOC-E-25`) y del informe consolidado de edición (`DOC-E-26`).

**Alcance:** aplicación a PD, CC, DE, EV y EC en la medición, el cálculo y el reporte de las Ediciones 01 a 06 de 2027; a los proveedores técnicos con acceso a datos de medición; presentación de resultados al CE.

**Precedencia:** Documento Rector e Índice Maestro sobre este documento; referencias al rector con el símbolo §.

## 1. Principios de medición

Fuente única de la definición de indicadores y de la atribución, con remisión desde `KIT-CO-ST-2026-01`, `DOC-E-25` y `DOC-E-26`.

### 1.1 Principios

- **Definición única:** una definición por indicador; remisión desde los demás documentos por código.
- **Fórmula reproducible:** numerador, denominador, unidad de conteo, ventana y corte explícitos; resultado idéntico con los mismos datos de origen.
- **Fuente identificada:** registro de origen de cada dato; ninguna cifra sin origen trazable.
- **Medición agregada:** informes sin datos personales; etiqueta NFC sin datos personales; identificación del lector solo por registro voluntario en el Club SoyTechno (rector §3.6, §4.4).
- **Línea base y metas:** Edición 01 como primera medición de cada indicador con crecimiento; meta de cada edición igual al 110 % del valor de la anterior (crecimiento del 10 % por edición); metas del rector §1.4 en cada ficha, con ratificación o ajuste en la revisión anual posterior a la Edición 06.
- **Corte explícito:** todo valor con fecha y hora de corte, en hora oficial de Venezuela; hora cero (19:30 del Día D) como origen de la ventana de 72 horas.
- **Prueba separada de la medición:** lecturas de prueba y de personal marcadas y excluidas, sin eliminar el registro (sección 9).
- **Datos económicos:** porcentajes en los documentos permanentes; valores en la moneda de referencia del programa solo en los registros de edición (`DOC-E-04`, `DOC-E-13` y `DOC-E-26`).

### 1.2 Responsabilidades

- **Cálculo, consolidación y reporte:** PD; aprobación de DE; consulta a CR, CC y EV; información al CE (rector §4.2).
- **Datos de origen:** aporte del rol titular de cada registro, conforme a la fuente de cada ficha.
- **Dato no entregado en plazo:** registro como «no disponible» e incidencia en `DOC-E-05`, sin estimación.

## 2. Fichas de indicadores

Quince fichas, en el orden de los objetivos del rector §1.4. Reglas de conteo en la sección 3; frecuencia del panel en 5.2.

### 2.1 Alcance de la revelación a 72 h

- **Definición:** cuentas únicas alcanzadas por las publicaciones de la revelación de portada en las 72 horas posteriores a la hora cero.
- **Fórmula:** suma, por plataforma, del alcance único de cada publicación de la revelación (colaborativa de las 19:35, transmisión en directo, clips de D a D+3 y publicaciones de creadores autorizados); reproducciones aparte, sin sumarse.
- **Fuente:** estadísticas de las cuentas oficiales de SoyTechno y del perfil propio de la revista; de las cuentas del personaje y de creadores, aportadas por su titular conforme al acuerdo de participación (`REG-LG-ST-2026-01`).
- **Herramienta:** analítica nativa de cada plataforma social.
- **Frecuencia:** seguimiento diario de D a D+3; corte a las 19:30 de D+3.
- **Línea base:** Edición 01.
- **Meta:** crecimiento del 10 % por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-25`; `DOC-E-26`.

### 2.2 Lecturas digitales únicas

- **Definición:** lectores únicos de la edición digital, del PDF ligero y de los artículos de la edición en `soytechno.com`, con al menos una lectura digital válida (3.2).
- **Fórmula:** dispositivos únicos (identificador seudónimo) con una o más lecturas digitales válidas de la edición, sin duplicación entre HTML5, PDF ligero y artículos; valor a 72 horas y valor al corte.
- **Fuente:** analítica de la edición digital y del micrositio `soytechno.com/revista`.
- **Herramienta:** analítica web del comercio electrónico y analítica de la edición digital.
- **Frecuencia:** la del panel (5.2).
- **Línea base:** Edición 01.
- **Meta:** crecimiento del 10 % por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-25`; `DOC-E-26`.

### 2.3 Distribución efectiva

- **Definición:** proporción de ejemplares asignados con entrega registrada. Complemento: quiebre de existencia.
- **Fórmula:** ejemplares entregados al público (al destinatario final, en los demás canales) ÷ ejemplares asignados al canal o a la sede × 100. Total de la edición: suma de entregas sobre suma de asignaciones, sin el canal de archivo y depósito legal. Asignación: entrega inicial más reserva de reposición. Quiebre de existencia: existencia final igual a cero en el acta semanal; reiterado, en dos actas consecutivas.
- **Fuente:** actas semanales y acta de cierre de CC; registros de entrega del evento, del Club SoyTechno y de aliados (`PLA-DI-ST-2027-01`, `DOC-E-24`).
- **Herramienta:** registro digital de actas de conteo.
- **Frecuencia:** semanal, con cierre por edición en el Día D siguiente.
- **Línea base:** Edición 01.
- **Meta:** igual o superior al 85 %.
- **Responsable:** PD.
- **Registro:** `DOC-E-24`; `DOC-E-26`.

### 2.4 Escaneo QR

- **Definición:** proporción de ejemplares con lectura QR, estimada por dispositivos únicos con al menos un escaneo único de pieza impresa de la edición (3.2).
- **Fórmula:** lectores QR únicos ÷ ejemplares del tiraje recibido (`DOC-E-17`) × 100. Escaneos de zonas de experiencia y de pantallas en tiendas, excluidos. Complemento: escaneos únicos por pieza, sección y página.
- **Fuente:** registros de la plataforma de enlaces con parámetros de medición (`GUI-PP-ST-2026-01`).
- **Herramienta:** plataforma de enlaces de SoyTechno.
- **Frecuencia:** la del panel (5.2).
- **Línea base:** Edición 01.
- **Meta:** igual o superior al 5 % de ejemplares (250 lectores QR únicos sobre 5.000 ejemplares en la Edición 01).
- **Responsable:** PD.
- **Registro:** `DOC-E-25`; `DOC-E-26`; `DOC-E-28` (por pieza).

### 2.5 Conversión *phygital*

- **Definición:** proporción de sesiones originadas en QR o NFC con al menos una acción de continuación (3.2).
- **Fórmula:** sesiones originadas en QR o NFC con acción de continuación ÷ sesiones originadas en QR o NFC × 100, tras exclusiones.
- **Fuente:** sesiones y acciones de la analítica del comercio electrónico; registros de la plataforma de enlaces y del servicio de redirección.
- **Herramienta:** herramienta de analítica web del comercio electrónico.
- **Frecuencia:** la del panel (5.2).
- **Línea base:** Edición 01.
- **Meta:** igual o superior al 60 % de sesiones.
- **Responsable:** PD.
- **Registro:** `DOC-E-25`; `DOC-E-26`.

### 2.6 Ventas atribuidas

- **Definición:** ventas del comercio electrónico y de las tiendas atribuidas a la revista conforme al modelo de la sección 4.
- **Fórmula:** valor neto de impuestos, cancelaciones y devoluciones de los pedidos y operaciones atribuidos, por canal, pieza, sección, marca y edición. En documentos permanentes, variación porcentual respecto de la línea base (Edición 01 igual a 100 %); valores en la moneda de referencia solo en `DOC-E-26`.
- **Fuente:** pedidos con parámetros de la revista (comercio electrónico); operaciones con código `REV-E<ed>` o con vinculación con el Club SoyTechno (Operaciones de tiendas).
- **Herramienta:** herramienta de analítica web del comercio electrónico; sistema de punto de venta; sistema del Club SoyTechno.
- **Frecuencia:** la del panel (5.2); valor de cierre a los 30 días del Día D siguiente.
- **Línea base:** Edición 01.
- **Meta:** reporte por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-26`; uso interno, sin inclusión en `DOC-E-28`.

### 2.7 Activación NFC

- **Definición:** proporción de ejemplares etiquetados activados, con activación igual a la primera lectura NFC válida de un identificador (3.2).
- **Fórmula:** identificadores con primera lectura válida acumulada ÷ ejemplares etiquetados de la edición × 100, por lote (EV, CL, AL, SC y CM; desde la Edición 03, V01 a Vnn, AV y AR). Complemento: lecturas válidas por ejemplar etiquetado.
- **Fuente:** registros del servicio de redirección; reporte de identificadores de cada lote (`GUI-PP-ST-2026-01`); cantidades del acta de recepción (`DOC-E-17`).
- **Herramienta:** servicio de redirección de SoyTechno.
- **Frecuencia:** la del panel (5.2). Corte de decisión para el tiraje completo con NFC: 23:59 del último día hábil previo a la sesión del CE de G4 de la Edición 02 (01-mar-2027).
- **Línea base:** Edición 01.
- **Meta:** igual o superior al 10 % de ejemplares etiquetados (200 en la Edición 01).
- **Responsable:** PD.
- **Registro:** `DOC-E-25` (lecturas del Día D); `DOC-E-26`; `DOC-E-28` (por lote); `DOC-E-05` (decisión del CE).

### 2.8 Afiliaciones y activaciones atribuidas al Club SoyTechno

- **Definición:** registros voluntarios en el Club SoyTechno atribuidos a la revista: afiliaciones nuevas y activaciones de ejemplar (4.3).
- **Fórmula:** activaciones de ejemplar con canje del beneficio, una por identificador, más afiliaciones nuevas sin identificador NFC (4.3); un registro, una atribución. Desglose por lote, origen y miembro nuevo o existente.
- **Fuente:** registros del Club SoyTechno y de CRM SoyTechno, en conteos agregados por origen y lote; clics a la afiliación en los envíos al Club.
- **Herramienta:** sistema del Club SoyTechno y herramienta de envíos de correo electrónico.
- **Frecuencia:** la del panel (5.2); valor de cierre a los 30 días del Día D siguiente.
- **Línea base:** Edición 01.
- **Meta:** crecimiento del 10 % por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-26`.

### 2.9 Asistencia

- **Definición:** proporción de confirmados con ingreso acreditado al evento.
- **Fórmula:** personas con ingreso registrado (lectura válida del QR personal o verificación manual) ÷ confirmaciones vigentes al cierre de reposiciones en D-1 × 100, por grupo de credencial; personal de producción (credencial gris) fuera del cálculo.
- **Fuente:** padrón, acreditación y lista de espera (`DOC-E-23`), entregados por EV a PD en D+1 (`MAN-EV-ST-2026-01`).
- **Herramienta:** lectores de QR de acreditación del evento.
- **Frecuencia:** por edición; conteo en vivo desde las 18:00 y cierre en D+1.
- **Línea base:** Edición 01.
- **Meta:** igual o superior al 75 % de confirmados.
- **Responsable:** PD.
- **Registro:** `DOC-E-23`; `DOC-E-25`; `DOC-E-26`.

### 2.10 Contactos de negocio

- **Definición:** contactos efectivos de la rueda de negocios: cita realizada con interés registrado y siguiente paso distinto de «ninguno» (`GUI-NW-ST-2026-01`).
- **Fórmula:** registros de contacto con cita realizada igual a «sí», interés alto, medio o bajo y siguiente paso distinto de «ninguno», por grupo, mesa y ronda. Complementos: citas realizadas ÷ citas programadas × 100; oportunidades trasladadas a CC (interés alto con siguiente paso comercial).
- **Fuente:** registros de contacto de cada participante y agenda de citas (`DOC-E-23`), entregados por EV a PD en D+7 en informe agregado.
- **Herramienta:** enlace de registro de la agenda de citas.
- **Frecuencia:** por edición; registro hasta las 22:00 del Día D y recordatorio en D+1.
- **Línea base:** Edición 01.
- **Meta:** reporte por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-23`; `DOC-E-26`.

### 2.11 Audiencia del pódcast a 30 días

- **Definición:** reproducciones acumuladas del episodio de estudio y del episodio en vivo durante los 30 días posteriores a su publicación.
- **Fórmula:** suma de reproducciones contabilizadas por cada plataforma de audio y video y por el micrositio, desde las 19:35 del Día D hasta las 19:35 de D+30, con el criterio de cada plataforma y sin deduplicación entre ellas. Complemento: oyentes únicos, en las plataformas con ese dato.
- **Fuente:** estadísticas de las plataformas de audio y video; analítica del micrositio.
- **Herramienta:** analítica nativa de las plataformas de pódcast; analítica web del comercio electrónico.
- **Frecuencia:** la del panel (5.2); valor a 30 días en el anexo de cierre del `DOC-E-26`.
- **Línea base:** Edición 01.
- **Meta:** crecimiento del 10 % por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-26`.

### 2.12 Satisfacción de marcas

- **Definición:** valoración de la relación con SoyTechno por las marcas con pauta o patrocinio en el semestre, en escala de 1 a 5 (sección 8).
- **Fórmula:** media aritmética de las respuestas válidas a la valoración global; respuestas «sin opinión» fuera del cálculo. Tasa de respuesta: marcas respondientes ÷ marcas invitadas × 100.
- **Fuente:** encuesta semestral a las marcas con pauta o patrocinio (sección 8).
- **Herramienta:** herramienta de encuestas en línea.
- **Frecuencia:** semestral, tras las Ediciones 03 y 06.
- **Línea base:** primera medición, tras la Edición 03.
- **Meta:** igual o superior a 4 sobre 5.
- **Responsable:** CC (aplicación) y PD (procesamiento y reporte).
- **Registro:** `DOC-E-26`.

### 2.13 Cobertura de ingresos

- **Definición:** porcentaje del costo total de edición y evento cubierto por los ingresos netos de pauta y patrocinio, sin montos en documentos permanentes.
- **Fórmula:** ingreso neto (después de descuentos, sin IVA) de pauta y patrocinio ÷ costo total de edición y evento con contingencia × 100 (`PLA-FI-ST-2027-01`). Plan en G0 y G3: ingreso comprometido sobre costo total aprobado (costo base más contingencia del 10 %). Final en `DOC-E-26`: ingreso neto facturado sobre costo real, con la contingencia utilizada. Anual: suma de ingresos netos sobre suma de costos totales de las seis ediciones.
- **Fuente:** ingresos de `DOC-E-13`; costos de `DOC-E-04`; costo real con datos de DE (edición) y EV (evento).
- **Herramienta:** registros presupuestarios de cada edición.
- **Frecuencia:** G0, G3 y cierre en S4 del ciclo siguiente.
- **Línea base:** plan base de `PLA-FI`: 52,0 % (Ediciones 01 y 02), 54,4 % (03 a 05) y 55,0 % (06); 53,8 % anual.
- **Meta:** igual o superior al 50 % en el primer año y al 70 % desde el segundo (cobertura anual).
- **Responsable:** PD.
- **Registro:** `DOC-E-04`; `DOC-E-13`; `DOC-E-26`.

### 2.14 Erratas posteriores a la impresión

- **Definición:** errores de hecho, cifra, nombre, crédito o grafía comprobados en la edición impresa o digital con posterioridad a `vFinal` (G4) y registrados en la fe de erratas.
- **Fórmula:** número de erratas distintas desde G4 hasta el Día D siguiente; error repetido en varios soportes, una sola errata. Exclusión: cambios de destino o de vigencia en QR y NFC, editables sin reimpresión.
- **Fuente:** registro de verificación y fe de erratas (`DOC-E-09`), a cargo de EC.
- **Herramienta:** registro de verificación de EC.
- **Frecuencia:** continua; cierre por edición en el Día D siguiente.
- **Línea base:** Edición 01.
- **Meta:** igual o inferior a 3 por edición.
- **Responsable:** PD.
- **Registro:** `DOC-E-09`; `DOC-E-26`.

### 2.15 Días D en fecha

- **Definición:** ediciones con revelación de portada y evento realizados en la fecha del Día D fijada en `CAL-ED-ST-2027-01`.
- **Fórmula:** número de ediciones con Día D realizado en la fecha fijada, sobre seis ediciones del año. Desplazamiento de la hora cero dentro de la tolerancia de `PRO-RP-ST-2026-01` (10 minutos): sin efecto sobre el indicador.
- **Fuente:** registro de compuertas, cambios e incidencias (`DOC-E-05`) y plan operativo del evento (`DOC-E-21`).
- **Herramienta:** registro de compuertas de la edición.
- **Frecuencia:** por edición, en G5 (D+1).
- **Línea base:** Edición 01.
- **Meta:** seis de seis.
- **Responsable:** PD.
- **Registro:** `DOC-E-05`; `DOC-E-26`.

## 3. Arquitectura de medición QR y NFC

Especificación del código QR, parámetros UTM y etiqueta NFC en `GUI-PP-ST-2026-01`, sin reproducción en este manual.

### 3.1 Flujo de datos de cada lectura

| Etapa | Código QR | Etiqueta NFC |
|---|---|---|
| Lectura | Escaneo de la dirección corta de la pieza | Aproximación a la zona de contacto de C3 |
| Registro | Plataforma de enlaces: pieza, marca de tiempo y dispositivo seudónimo | Servicio de redirección: UID, contador, lote y marca de tiempo |
| Redirección | Destino de la pieza, con parámetros UTM | Destino del lote, con parámetros UTM |
| Destino | Página de pieza, ficha de compra, video o afiliación al Club SoyTechno | Edición digital, pódcast, detrás de cámaras o activación en el Club SoyTechno |

Hasta las 19:35 del Día D, destino único de todas las lecturas: página de espera (`PRO-RP-ST-2026-01`). Analítica común: sesiones, acciones y pedidos en la analítica web del comercio electrónico.

### 3.2 Reglas de conteo

- **Escaneo único:** un dispositivo, una pieza y un día natural (hora oficial de Venezuela); repeticiones del día, sin conteo.
- **Lector QR único:** dispositivo con al menos un escaneo único de pieza impresa de la edición.
- **Lectura NFC válida:** identificador registrado en el reporte del lote; contador superior a la línea base de ese identificador; par identificador-contador no registrado antes; fuera de exclusiones.
- **Activación NFC:** primera lectura NFC válida de un identificador.
- **Activación en el Club:** registro voluntario en el Club SoyTechno con identificador de etiqueta y canje único del beneficio (`REG-LG-ST-2026-01`).
- **Sesión originada en QR o NFC:** sesión con primer acceso portador de `utm_source=revista` y de `utm_medium` igual a `qr` o `nfc`.
- **Acción de continuación:** clic a la ficha de compra o a condiciones de financiamiento; reproducción de video; inicio de afiliación al Club SoyTechno; lectura de una segunda página de la edición digital.
- **Lectura digital válida:** carga completa de una página de la edición digital, descarga completada del PDF ligero o visita a un artículo de la edición, tras el filtrado de 3.3.

### 3.3 Exclusiones y marcado

- **Lecturas de prueba previas al lanzamiento:** toda lectura anterior a las 19:35 del Día D (página de espera como destino único, `PRO-RP`) y las de los equipos de verificación de la hora cero. Ante adelanto controlado o desplazamiento de la hora cero, límite de marcado en la hora efectiva de cambio de destinos, registrada en `DOC-E-05`.
- **Personal:** equipos y redes de la lista de exclusión de PD (roles del rector §4.2 y proveedores técnicos), actualizada en G4 y en D-1; fuerza de ventas, destinataria del lote AL, fuera de la lista.
- **Tráfico no humano:** rastreadores, vistas previas de aplicaciones de mensajería y solicitudes automatizadas.
- **Marcado:** registros marcados y conservados, sin eliminación; volumen marcado visible en el panel.

### 3.4 Parámetros de medición

- **QR y NFC:** `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` y plantilla de URL de la etiqueta, por remisión a `GUI-PP` (secciones 6.2 y 7.2).
- **Otros canales:** `utm_source=revista`, `utm_campaign=ed<n>` y `utm_content` por pieza en todo enlace; `utm_medium` según la tabla siguiente, asignado por PD y registrado en `DOC-E-20`. Sin parámetros en enlaces internos de `soytechno.com`, para conservar el origen del primer acceso.
- **Tienda:** código de campaña `REV-E<ed>` (ejemplo: `REV-E01`), conforme a 4.2.
- **Zonas de experiencia:** `qr` con `utm_content` de zona (`GUI-PP`); fuera del escaneo QR (2.4), dentro del registro de zonas de `DOC-E-28`.

| Tipo de canal | `utm_medium` |
|---|---|
| Cuentas oficiales de SoyTechno y perfil propio de la revista | `social` |
| Personaje de portada y creadores | `colaboracion` |
| Envíos al Club SoyTechno y a suscriptores | `correo` |
| Pantallas en tiendas | `pantalla` |
| Plataformas de pódcast | `podcast` |

### 3.5 Medición por sede

- **Sedes con etiqueta:** lecturas y activaciones NFC por lote (SC y CM en las Ediciones 01 y 02; V01 a Vnn desde la Edición 03), conforme a `PLA-DI-ST-2027-01`.
- **Sedes sin etiqueta (Ediciones 01 y 02):** escaneo QR por pieza para el conjunto de la edición y operaciones con código `REV-E<ed>` por sede; QR común a todos los ejemplares: sin identificación de sede.
- **Traslado excepcional de ejemplares etiquetados:** nota en el análisis, con registro en el acta (`PLA-DI`).

## 4. Modelo de atribución

Atribución por medios observables, sin identificación personal; valores de referencia sobre el aporte de la revista, no medida de efecto causal.

### 4.1 Comercio electrónico

- **Ventana:** 30 días desde el primer acceso con parámetros de la revista (`utm_source=revista`) en el mismo dispositivo.
- **Regla:** último clic no directo. Atribución del pedido con último acceso no directo previo a la compra con parámetros de la revista, dentro de la ventana; accesos directos posteriores, sin efecto; acceso no directo posterior de otra fuente, sin atribución.
- **Valor:** pedido pagado, neto de impuestos, cancelaciones y devoluciones; cierre 30 días después del Día D siguiente (7.3).

### 4.2 Tienda física

- **Código de campaña:** `REV-E<ed>`, declarado por el cliente y registrado en caja; visible en las fichas de compra y en la página de activación; comunicación al personal de caja por Operaciones de tiendas antes de D+1. Vigencia: de la hora cero a 30 días después del Día D siguiente.
- **Vinculación voluntaria con el Club SoyTechno:** operación de un miembro con consentimiento y primer acceso con parámetros de la revista en los 30 días previos; atribución aun sin código; datos a PD en conteos agregados.
- **Operaciones sin código ni vinculación:** sin atribución.

### 4.3 Etiqueta NFC y Club SoyTechno

- **Canje del beneficio de activación:** uno por identificador (`REG-LG`); atribución al lote, a la sede o canal y a la edición del identificador. Canje con miembro nuevo: afiliación atribuida; con miembro existente: activación atribuida.
- **Afiliación sin etiqueta:** registro nuevo con primer acceso con parámetros de la revista en la ventana de 30 días; atribución por `utm_content` y `utm_medium`.
- **Sin doble conteo:** un registro, una atribución; prevalencia del identificador NFC. Ventas posteriores al canje: modelos de 4.1 y 4.2.

### 4.4 Granularidad

- **Pieza, sección y marca:** `utm_content` del acceso atribuido e identificador de sección de `GUI-PP` (6.3); marca del producto del pedido o de la operación; en tienda, pieza y sección solo con vinculación con el Club.
- **Edición, lote y sede:** `utm_campaign` o código `REV-E<ed>`; en NFC, `utm_content` con los códigos EV, CL, AL, SC, CM, V01 a Vnn, AV y AR.

### 4.5 Limitaciones declaradas

- Compra en dispositivo distinto del primer acceso, sin sesión iniciada, y navegación sin identificador seudónimo: fuera de la medición.
- Último clic no directo: infravaloración del primer contacto; ventas sin parámetros ni código, no medidas.
- Código de tienda declarado por el cliente: subregistro por omisión en caja.
- QR común a todos los ejemplares: sin identificación de ejemplar ni de sede.
- Identificador y contador NFC sin autenticación criptográfica (`GUI-PP`, 7.8): lecturas replicadas posibles, mitigadas por el par identificador-contador y el canje único.
- Alcance y audiencia sin deduplicación entre plataformas; atribución sin demostración de efecto incremental.

## 5. Panel de control

### 5.1 Vistas

| Vista | Contenido | Acceso |
|---|---|---|
| Edición | Indicadores frente a metas, embudo *phygital* y estado de los datos | PD, DE, CC, EV y CR; CE en lectura |
| Pieza | Escaneos únicos, clics a ficha, conversión y ventas por pieza y sección | PD, DE, CR, DA y CC |
| Marca | Métricas QR y NFC por pieza y lote; registro de zonas (`DOC-E-28`) | PD y CC |
| Evento y *networking* | Asistencia, lecturas NFC del Día D, citas y contactos efectivos | PD, EV, DE y CC |
| Pódcast | Reproducciones por episodio y plataforma; audiencia a 30 días | PD, CR, EV y DE |

### 5.2 Actualización y acceso

- **Diaria de D a D+7:** corte a las 23:59 del día anterior; el Día D, lectura de control a las 19:39 (`PRO-RP`).
- **Semanal hasta el Día D siguiente:** actualización el lunes, con corte del domingo anterior.
- **Acceso por rol:** solo lectura, salvo PD; revisión al cierre de cada edición (`DOC-E-27`); marcas aliadas únicamente con el certificado `DOC-E-28`.

## 6. Reporte de 72 horas (`DOC-E-25`)

### 6.1 Plazo y entrega

- **Documento de edición:** responsable PD; colaboración de EV; aprobación de DE; carpeta `08_Cierre`; archivo `ST-RV-E<ed>_DOC-25_<Titulo>_v<n>`.
- **Corte:** 19:30 de D+3, 72 horas después de la hora cero (Edición 01: 24-ene-2027); ante desplazamiento de la hora cero (`PRO-RP`), 72 horas después de la hora efectiva.
- **Entrega:** el mismo día, a más tardar a las 23:59, a DE, CC y EV, por canal de acceso restringido; fechas por edición en `CAL-ED-ST-2027-01`.

### 6.2 Estructura

1. **Identificación:** edición, Día D, hora cero, corte y responsable.
2. **Reproducciones de la revelación:** transmisión en directo y video; alcance a 72 h (2.1).
3. **Publicaciones colaborativas:** alcance y reproducciones por cuenta.
4. **Asistencia efectiva:** por grupo de credencial (2.9).
5. **Lecturas NFC del Día D:** válidas y activaciones por lote (2.7).
6. **Escaneos QR:** escaneos únicos por pieza y lectores QR únicos (2.4).
7. **Lecturas digitales:** lectores únicos (2.2).
8. **Referencias:** línea base, meta, lecturas marcadas e incidencias de medición.

## 7. Informe consolidado de edición (`DOC-E-26`)

### 7.1 Plazo y presentación

- **Documento de edición:** responsable PD; colaboración de CC y EV; aprobación de DE; carpeta `08_Cierre`; archivo `ST-RV-E<ed>_DOC-26_<Titulo>_v<n>`.
- **Corte:** 23:59 del domingo de S3 del ciclo siguiente.
- **Entrega:** en S4 del ciclo siguiente, a más tardar el viernes (Edición 01: 12-feb-2027), con el certificado `DOC-E-28`.
- **Presentación al CE:** sesión de G4 del ciclo de entrega (Edición 01: 02-mar-2027), con PD como invitado.

### 7.2 Estructura

1. **Cumplimiento:** indicadores del rector §1.4 frente a metas, con valor al corte, estado de la meta (cumplida, no cumplida o línea base) y valor de referencia de la distribución efectiva.
2. **Embudo *phygital*:** ejemplares entregados, lectores QR únicos y activaciones NFC, sesiones, acciones de continuación, clics a ficha y ventas atribuidas.
3. **Ventas atribuidas:** por canal, pieza, sección, marca y edición.
4. **Club SoyTechno y pódcast:** afiliaciones y activaciones atribuidas; resultados de los envíos; audiencia del pódcast al corte, por plataforma.
5. **Evento y rueda de negocios:** asistencia por grupo, citas, contactos efectivos y oportunidades trasladadas a CC, con su seguimiento.
6. **Encuestas:** salida del evento y satisfacción de aliados (tras las Ediciones 03 y 06).
7. **Balance económico:** costo real por partida frente a `DOC-E-04`, en desviación porcentual; contingencia utilizada; cobertura final.
8. **Calidad y ajustes:** erratas, Días D en fecha, incidencias de medición y propuestas de ajuste, con responsable y plazo.

### 7.3 Valores y anexo de cierre

- **Tipos de valor:** valor al corte, acumulado desde la hora cero hasta el corte; valor de referencia, proyección de la distribución efectiva en circulación (`PLA-DI-ST-2027-01`); valor de cierre, acumulado al cierre de la ventana de cada indicador.
- **Ventanas abiertas al corte:** distribución efectiva, escaneo QR, conversión, activación NFC y lecturas digitales (cierre en el Día D siguiente); audiencia del pódcast (D+30); ventas y afiliaciones atribuidas (30 días después del Día D siguiente).
- **Anexo de cierre:** valores de cierre, a cargo de PD, dentro de los diez días hábiles siguientes al último cierre; diferencia superior al 10 % respecto del valor al corte, con aviso al CE en su sesión siguiente.

## 8. Encuestas

Escala de 1 a 5 (1, muy insatisfecho; 5, muy satisfecho); «sin opinión» fuera del cálculo; código de un solo uso por invitación, separado de las respuestas; resultados por marca de acceso restringido a CC y DE.

### 8.1 Encuesta de salida del evento

- **Aplicación:** desde las 21:50 del Día D, por QR en pantalla y señalética, con recordatorio en D+1 a los asistentes sin respuesta (`MAN-EV-ST-2026-01`); aplicación a cargo de EV y procesamiento por PD.
- **Preguntas mínimas (aspectos valorados):** acreditación; mesas de afinidad, rueda de negocios y utilidad de los contactos (módulo de *networking*, `GUI-NW-ST-2026-01`); zonas de experiencia; revelación y conversación en escena; entrega de ejemplares y sorteos; valoración global.
- **Tasa de respuesta objetivo:** igual o superior al 50 % de los asistentes acreditados.

### 8.2 Encuesta semestral de satisfacción de marcas

- **Población y momento:** marcas con orden de inserción o contrato de patrocinio en el semestre; tras las Ediciones 03 y 06, de D+4 al corte del `DOC-E-26`; aplicación a cargo de CC y procesamiento por PD.
- **Preguntas mínimas (aspectos valorados):** visibilidad y ubicación de la pauta; ejecución de zonas y activaciones; comunicación y plazos; utilidad del certificado; independencia editorial; valoración global; intención de renovación.
- **Tasa de respuesta objetivo:** igual o superior al 80 % de las marcas invitadas.
- **Registro por edición:** satisfacción del patrocinante posterior al evento (`MAN-EX-ST-2026-01`), evidencia de `DOC-E-28` sin valor de indicador.

## 9. Calidad de datos y privacidad

### 9.1 Validación y filtrado

- **Conciliación:** sesiones originadas en QR y NFC entre las fuentes de registro y la analítica del comercio electrónico, con tolerancia del 2 %; diferencia mayor, incidencia en `DOC-E-05`.
- **Recálculo:** por persona distinta del autor antes de cada informe.
- **Filtrado y marcado:** tráfico no humano, tráfico interno y lecturas de prueba previas al lanzamiento conforme a 3.3, con criterios idénticos en todas las ediciones; cambio de criterio con registro en `DOC-E-05` y recálculo de la línea base.

### 9.2 Consentimiento, conservación y reporte

- **Consentimiento:** identificador seudónimo sin vinculación con personas; consentimientos y avisos conforme a `REG-LG-ST-2026-01`.
- **Conservación:** registros de lectura en bruto, 12 meses desde el Día D siguiente y luego solo agregados; `DOC-E-25` y `DOC-E-26`, cinco años (rector §4.5).
- **Informes agregados:** sin cifras desagregadas con menos de cinco registros ni datos personales en `DOC-E-25`, `DOC-E-26` y `DOC-E-28`.

## 10. Control del documento

### 10.1 Relación con otros documentos

- **Fuente única:** definición de indicadores y atribución, con remisión desde `KIT-CO`, `DOC-E-25` y `DOC-E-26`.
- **Remisiones:** `GUI-PP` (QR, UTM y NFC), `GUI-NW` (citas y contactos), `PLA-DI` (actas y lotes), `PLA-FI` (costos y cobertura), `PLA-CM` (canales), `PRO-RP` (hora cero), `MAN-EV` y `MAN-EX` (evento y evidencia), `REG-LG` (datos) y `CAL-ED` (fechas).

### 10.2 Revisión y actualización

- **Periodicidad:** anual, tras la Edición 06, con ratificación o ajuste de metas (rector §1.4).
- **Disparadores:** cambio de plataforma de enlaces, de analítica o de punto de venta; modificación del rector §1.4 o §3.6; decisión del CE sobre el tiraje completo con NFC; cambio normativo en datos personales.
- **Responsable y registro:** PD, con aprobación de DE; nueva versión en el Índice Maestro; cambio de definición con recálculo de la serie.

### 10.3 Firmas

| Elaboración | Revisión | Aprobación |
|---|---|---|
| PD · nombre, cargo y fecha | Nombre, cargo y fecha | DE · fecha |
