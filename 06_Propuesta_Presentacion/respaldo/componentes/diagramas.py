#!/usr/bin/env python3
"""Diagramas de la presentación: mapa de paginación, ciclo de ocho semanas, hora cero y calendario 2027 (datos del corpus)."""
import os, html, datetime as dt
AQUI = os.path.dirname(os.path.abspath(__file__))
e = html.escape

# ------------------------------------------------------------------ Mapa de paginación (rector §4.1)
SECC = [('C1','Portada','portada'),('C2','Pauta','pauta')] + [(str(i),'Pauta','pauta') for i in [1]] + \
  [(f'{i:02d}','Sumario','edit') for i in (2,3)] + [(f'{i:02d}','Pulso Techno','edit') for i in range(4,8)] + \
  [(f'{i:02d}','Bajo el Lente','edit') for i in range(8,14)] + [(f'{i:02d}','Pauta','pauta') for i in (14,15)] + \
  [(f'{i:02d}','Reportaje Central','edit') for i in range(16,20)] + [(f'{i:02d}','En Primera Fila','edit') for i in range(20,26)] + \
  [(f'{i:02d}','Pauta','pauta') for i in (26,27)] + [(f'{i:02d}','ADN Gamer','oscuro') for i in range(28,36)] + \
  [(f'{i:02d}','Espacio Business','edit') for i in range(36,40)] + [(f'{i:02d}','Conexión en Vivo','edit') for i in range(40,44)] + \
  [(f'{i:02d}','Ruta Inteligente','edit') for i in range(44,48)] + [('48','Última Página','edit'),('C3','Autopromoción · NFC','auto'),('C4','Pauta','pauta')]
SECC[2] = ('01','Pauta','pauta')
ABREV = {'Portada':'Portada','Pauta':'Pauta','Sumario':'Sumario','Pulso Techno':'Pulso','Bajo el Lente':'Lente','Reportaje Central':'Reportaje',
 'En Primera Fila':'P. Fila','ADN Gamer':'Gamer','Espacio Business':'Business','Conexión en Vivo':'Conexión','Ruta Inteligente':'Ruta',
 'Última Página':'Última','Autopromoción · NFC':'NFC'}
# pliegos de la simulación con su índice en el libro (para saltar desde el mapa)
EN_LIBRO = {'C1':0,'C2':1,'01':1,'02':2,'03':2,'04':3,'05':3,'08':4,'09':4,'16':5,'17':5,'20':6,'21':6,'28':7,'29':7,'36':8,'37':8,'40':9,'41':9,'44':10,'45':10,'48':11,'C3':11,'C4':12}

def mapa():
    assert len(SECC) == 52, len(SECC)
    pliegos = [[SECC[0]]] + [SECC[i:i+2] for i in range(1, 51, 2)] + [[SECC[51]]]
    celdas = ''
    for pl in pliegos:
        pags = ''
        for pg, sec, tipo in pl:
            k = EN_LIBRO.get(pg)
            # las páginas incluidas en la simulación abren su pliego: botón real; las demás solo informan (sin parada de tabulación)
            # nombre accesible = texto visible + sufijo oculto (la etiqueta visible queda al inicio del nombre)
            tag, atr, suf = ('button', f' type="button" data-pliego="{k}"', f'<span class="sr-only"> · {e(sec)} · abrir el pliego en la revista</span>') if k is not None else ('span', '', '')
            pags += (f'<{tag} class="mp-p {tipo}"{atr} data-tip="{e(sec)}" data-val="Página {e(pg)}" data-det="{"Incluida en la simulación" if k is not None else "Mapa de paginación"}">'
                     f'<b>{e(pg)}</b><i>{e(ABREV[sec])}</i>{suf}</{tag}>')
        celdas += f'<span class="mp-pl{" uno" if len(pl) == 1 else ""}">{pags}</span>'
    ley = ('<ul class="mp-ley"><li><i class="edit"></i>Editorial</li><li><i class="oscuro"></i>Editorial en modo oscuro · ADN Gamer</li>'
           '<li><i class="pauta"></i>Pauta · 7 páginas (13,5 %) en C2-01, 14-15, 26-27 y C4</li><li><i class="auto"></i>Autopromoción con zona NFC · C3</li></ul>')
    return (f'<figure class="dg mp" id="dg-mapa"><figcaption><b>Mapa de paginación · 52 páginas</b><span>44 editoriales · 7 de pauta · 1 de autopromoción · tres pliegos de 16</span></figcaption>'
            f'{ley}<div class="mp-reja">{celdas}</div></figure>')

# ------------------------------------------------------------------ Ciclo de ocho semanas (rector §5.1 y §4.3)
FASES = [('Planificación',1,1),('Producción',2,4),('Diseño y edición',5,6),('Pre-prensa e impresión',7,7),('Lanzamiento',8,8)]
OTRAS = [('Convocatoria',4,5,'Reserva de fecha en S4 · invitación en S5'),('Expectativa',6,7,'Campaña sin mostrar la portada')]
# (código, semana, día 0=lunes … 4=viernes, firma, criterio)
COMP = [('G0',1,4,'Consejo Editorial','Eje temático, personaje de portada, mapa de paginación, pauta comprometida, tiraje y evento'),
 ('G1',4,4,'DE','Textos firmados; fotografía, video y pódcast entregados; autorizaciones archivadas'),
 ('G2',6,4,'DE · EC','Páginas con doble corrección; cifras verificadas; QR y NFC configurados'),
 ('G3',6,4,'CC · EV','Pauta aprobada; cero precios impresos; revisión legal; patrocinio del evento ≥ 70 % del costo'),
 ('G4',7,1,'DE · DA · EV','Ferro y color aprobados; QR y NFC verificados; plan del evento cerrado'),
 ('G5',8,4,'PD · CC · EV','Portada revelada; edición digital y pódcast publicados; ejemplares en sedes')]
def ciclo():
    cab = ''.join(f'<span class="cg-s">S{s}</span>' for s in range(1, 9))
    filas = ''
    for nom, a, b in FASES:
        filas += f'<div class="cg-f"><span class="cg-n">{e(nom)}</span><span class="cg-pista"><span class="cg-b" style="--a:{a-1};--b:{b}"></span></span></div>'
    for nom, a, b, det in OTRAS:
        filas += f'<div class="cg-f sec"><span class="cg-n">{e(nom)}</span><span class="cg-pista"><span class="cg-b" style="--a:{a-1};--b:{b}" title="{e(det)}"></span></span></div>'
    marcas = ''
    for cod, s, d, firma, crit in COMP:
        x = (s - 1 + (d + .5) / 5) / 8
        doble = ' doble' if cod == 'G3' else ''
        marcas += (f'<button type="button" class="cg-g{doble}" style="--x:{x:.4f}" data-tip="{e(cod)} · {e(firma)}" data-val="{e(cod)}" data-det="{e(crit)}" '
                   f'aria-label="{e(cod)}, {["lunes","martes","miércoles","jueves","viernes"][d]} de S{s}, firma {e(firma)}: {e(crit)}"><span>{e(cod)}</span></button>')
    xd = (7 + 3.5 / 5) / 8
    marcas += f'<span class="cg-dia" style="--x:{xd:.4f}" aria-hidden="true"><span>Día D · jueves · 19:30</span></span>'
    s7 = ['Lunes · archivos, ferro y pruebas','Martes · G4 e impresión','Miércoles · laminado y barniz UV','Jueves · encuadernación PUR','Viernes · NFC, control 1/50 y sellado']
    s8 = ['Lunes · almacén','Miércoles · despacho','Jueves · Día D y revelación','Viernes · sedes y Club SoyTechno']
    det = (f'<div class="cg-det"><div><b>Semana 7 · producción</b><ol>{"".join(f"<li>{e(x)}</li>" for x in s7)}</ol></div>'
           f'<div><b>Semana 8 · lanzamiento</b><ol>{"".join(f"<li>{e(x)}</li>" for x in s8)}</ol></div></div>')
    return (f'<figure class="dg cg" id="dg-ciclo"><figcaption><b>Ciclo de ocho semanas y seis compuertas</b><span>Cada edición avanza solo con la compuerta anterior firmada</span></figcaption>'
            f'<div class="cg-reja"><div class="cg-cab"><span class="cg-n"></span><span class="cg-sem">{cab}</span></div>{filas}'
            f'<div class="cg-f marcas"><span class="cg-n">Compuertas</span><span class="cg-pista">{marcas}</span></div></div>{det}'
            f'<p class="cg-ed01">Edición 01 · S1 16-nov-2026 · G0 20-nov-2026 · G1 11-dic-2026 · pausa 21-dic-2026 a 03-ene-2027 · G2 y G3 08-ene-2027 · G4 12-ene-2027 · Día D 21-ene-2027</p></figure>')

# ------------------------------------------------------------------ Hora cero (PRO-RP §6)
HORA = [('19:20','Llamado a la zona escénica y transmisión con escena de espera','EV · PD',0),('19:25','Decisión de ejecución de la hora cero','DE · EV',0),
 ('19:28','Cuenta regresiva de 120 segundos en pantalla LED','DA',0),('19:30','Descubrimiento: velo retirado, portada en pantalla, luz, sonido y transmisión','EV · DA · PD',2),
 ('19:35','Publicación colaborativa, QR y NFC activos, edición digital y pódcast liberados','PD',1),('19:40','Informe de verificaciones al canal de coordinación','PD · EV',0),
 ('19:45','Conversación en escena grabada como pódcast en vivo','CR · EV',0)]
def hora_cero():
    m0 = 20 * 60 + 0
    hitos = ''
    for h, acc, rol, peso in HORA:
        hh, mm = map(int, h.split(':')); x = ((hh * 60 + mm) - (19 * 60 + 20)) / 25
        hitos += (f'<li class="hc-h p{peso}" style="--x:{x:.4f}" tabindex="0" data-tip="{e(rol)}" data-val="{e(h)}" data-det="{e(acc)}">'
                  f'<span class="hc-t">{e(h)}</span><span class="hc-a">{e(acc)}</span></li>')
    return (f'<figure class="dg hc" id="dg-hora"><figcaption><b>Hora cero · minuto a minuto</b><span>Bloque de las 19:35 en 60 segundos como máximo; cuatro verificaciones antes de las 19:40</span></figcaption>'
            f'<ol class="hc-eje">{hitos}</ol></figure>')

# ------------------------------------------------------------------ Calendario 2027 (CAL-ED)
EDS = [('01','2026-11-16','2027-01-21','Enero-febrero','Estándar'),('02','2027-01-18','2027-03-11','Marzo-abril','Estándar'),('03','2027-03-08','2027-04-29','Mayo-junio','Estándar'),
 ('04','2027-04-26','2027-07-01','Julio-agosto','Estándar'),('05','2027-07-05','2027-08-26','Septiembre-octubre','Estándar'),('06','2027-09-13','2027-11-04','Noviembre-diciembre','Gala')]
PAUSAS = [('2026-12-21','2027-01-03'),('2027-05-31','2027-06-13')]
MES = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
def calendario():
    i0, i1 = dt.date(2026, 11, 1), dt.date(2027, 12, 1)
    tot = (i1 - i0).days
    pos = lambda d: (dt.date.fromisoformat(d) - i0).days / tot
    meses = ''
    d = i0
    while d < i1:
        meses += f'<span class="ca-m" style="--x:{(d - i0).days / tot:.4f}">{MES[d.month-1]}{" " + str(d.year) if d.month == 1 or d == i0 else ""}</span>'
        d = dt.date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    pau = ''.join(f'<span class="ca-pausa" style="--a:{pos(a):.4f};--b:{pos(b):.4f}" title="Pausa operativa"></span>' for a, b in PAUSAS)
    filas = ''
    for ed, s1, dd, bim, ev in EDS:
        f = dt.date.fromisoformat(dd); etiqueta = f'{f.day:02d}-{MES[f.month-1]}'
        filas += (f'<div class="ca-f"><span class="ca-n">Ed. {ed}</span><span class="ca-pista">{pau}<span class="ca-b{" gala" if ev == "Gala" else ""}" style="--a:{pos(s1):.4f};--b:{pos(dd):.4f}"></span>'
                  f'<span class="ca-d{" fin" if pos(dd) > .85 else ""}" style="--x:{pos(dd):.4f}" tabindex="0" data-tip="Edición {ed} · {e(bim)} 2027" data-val="Día D {etiqueta}" data-det="Evento {e(ev.lower())} · revelación a las 19:30"><b>{etiqueta}</b></span></span></div>')
    return (f'<figure class="dg ca" id="dg-cal"><figcaption><b>Calendario editorial 2027</b><span>Seis ediciones, cada Día D al menos diez días antes de su fecha comercial; dos pausas sin mover ningún Día D</span></figcaption>'
            f'<div class="ca-reja"><div class="ca-meses">{meses}</div>{filas}</div></figure>')

def todos():
    return {'mapa': mapa(), 'ciclo': ciclo(), 'hora': hora_cero(), 'calendario': calendario()}

if __name__ == '__main__':
    g = todos()
    open(os.path.join(AQUI, 'diagramas-fragmento.html'), 'w', encoding='utf-8').write('\n'.join(f'<!-- {k} -->\n{v}' for k, v in g.items()))
    print('diagramas:', ', '.join(g))
