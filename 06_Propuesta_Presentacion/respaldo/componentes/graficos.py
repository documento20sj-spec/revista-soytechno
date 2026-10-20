#!/usr/bin/env python3
"""Gráficos de la presentación (HTML accesible, sin bibliotecas). Datos del corpus vigente.
Reglas: un solo acento por gráfico, etiquetas directas, barras de 24 px como máximo con extremo redondeado de 4 px,
rejilla de 1 px, tabla accesible en <details>, información emergente al pasar o enfocar."""
import os, html
AQUI = os.path.dirname(os.path.abspath(__file__))
e = html.escape

def tabla(titulo, cab, filas):
    th = ''.join(f'<th scope="col">{e(c)}</th>' for c in cab)
    tr = ''.join('<tr>' + ''.join(f'<td>{e(str(c))}</td>' for c in f) + '</tr>' for f in filas)
    return f'<details class="gr-tabla"><summary>Ver tabla de datos</summary><table><caption>{e(titulo)}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></details>'

def num(v):
    return f'{v:.1f}'.replace('.', ',') if isinstance(v, float) and not v.is_integer() else str(int(v)) if isinstance(v, float) else str(v)

def barras_h(id_, titulo, nota, datos, resalte=0, maximo=None, unidad=' %'):
    """datos: [(etiqueta, valor, detalle)] ordenados de mayor a menor."""
    mx = maximo or max(v for _, v, _ in datos)
    filas = ''
    for i, (et, v, det) in enumerate(datos):
        filas += (f'<div class="gr-fila{" res" if i == resalte else ""}" tabindex="0" data-tip="{e(et)}" data-val="{num(v)}{unidad}" data-det="{e(det)}">'
                  f'<span class="gr-et">{e(et)}</span><span class="gr-pista"><span class="gr-barra" style="--v:{v / mx:.4f}"></span>'
                  f'<span class="gr-val">{num(v)}{unidad}</span></span></div>')
    t = tabla(titulo, ['Concepto', 'Valor', 'Detalle'], [(et, f'{num(v)}{unidad}', det) for et, v, det in datos])
    return f'<figure class="gr gr-h" id="{id_}"><figcaption><b>{e(titulo)}</b><span>{e(nota)}</span></figcaption><div class="gr-cuerpo">{filas}</div>{t}</figure>'

def _plot(cols, techo, pasos_rej, meta):
    rej = ''.join(f'<i style="--y:{y / techo:.4f}"><b>{y} %</b></i>' for y in pasos_rej)
    return (f'<div class="gr-cuerpo"><div class="gr-plot"><div class="gr-rej" aria-hidden="true">{rej}</div>'
            f'<div class="gr-meta" style="--y:{meta / techo:.4f}" aria-hidden="true"></div><div class="gr-cols">{cols}</div></div></div>')

def _col(clase, tip, val, det, v, b, etiqueta, rotulo):
    return (f'<div class="gr-col {clase}" tabindex="0" data-tip="{e(tip)}" data-val="{e(val)}" data-det="{e(det)}" style="--v:{v:.4f};--b:{b:.4f}">'
            f'<span class="gr-cbar"></span><span class="gr-cval">{e(rotulo)}</span><span class="gr-cet">{e(etiqueta)}</span></div>')

def leyenda(meta_et):
    return f'<span class="gr-ley"><i aria-hidden="true"></i>{e(meta_et)}</span>'

def columnas(id_, titulo, nota, datos, meta, meta_et, techo=60, rej=(0, 20, 40, 60)):
    cols = ''.join(_col('', et, f'{num(v)} %', det or 'Cobertura de la edición', v / techo, 0, et, f'{num(v)} %') for et, v, det in datos)
    t = tabla(titulo, ['Edición', 'Cobertura', 'Detalle'], [(et, f'{num(v)} %', det) for et, v, det in datos] + [('Meta', f'{meta} %', meta_et)])
    return (f'<figure class="gr gr-c" id="{id_}"><figcaption><b>{e(titulo)}</b><span>{e(nota)}</span>{leyenda(meta_et)}</figcaption>'
            f'{_plot(cols, techo, rej, meta)}{t}</figure>')

def cascada(id_, titulo, nota, base, pasos, meta, meta_et, techo=80, rej=(0, 20, 40, 60, 80)):
    acum = base[1]
    cols = _col('base', base[0], f'{num(base[1])} %', 'Punto de partida', base[1] / techo, 0, base[0], f'{num(base[1])} %')
    filas = [(base[0], f'{num(base[1])} %', '—')]
    for et, inc, det in pasos:
        ini = acum; acum = round(acum + inc, 1)
        cols += _col('paso', et, f'+{num(inc)} puntos', f'{det} · acumulado {num(acum)} %', inc / techo, ini / techo, et, f'+{num(inc)}')
        filas.append((et, f'+{num(inc)}', f'{num(acum)} %'))
    cols += _col('total', 'Cobertura de referencia', f'{num(acum)} %', 'Trayectoria desde el segundo año', acum / techo, 0, 'Resultado', f'{num(acum)} %')
    t = tabla(titulo, ['Palanca', 'Aporte', 'Acumulado'], filas)
    return (f'<figure class="gr gr-c gr-casc" id="{id_}"><figcaption><b>{e(titulo)}</b><span>{e(nota)}</span>{leyenda(meta_et)}</figcaption>'
            f'{_plot(cols, techo, rej, meta)}{t}</figure>')

# ------------------------------------------------------------------ datos (corpus vigente)
DIST = [('Sedes VIP', 58, '2.900 ejemplares · exhibición desde D+1'), ('Compras de alto valor', 15, '750 ejemplares'), ('Club SoyTechno de mayor nivel', 12, '600 ejemplares'),
        ('Evento de lanzamiento', 6, '300 ejemplares'), ('Aliados, fuerza de ventas y prensa', 6, '300 ejemplares'), ('Archivo y depósito legal', 3, '150 ejemplares')]
INVITADOS = [('Clientes de alto valor y Club', 30, 'Ediciones 01 a 05: 150 a 200 invitados'), ('Empresas', 20, 'Mesas Business y rueda de negocios'), ('Marcas y proveedores', 20, 'Zonas de experiencia'),
             ('Creadores, influencers y prensa', 20, 'Cabina de contenido'), ('Personaje, entrevistados, equipo e institucionales', 10, 'Escena y conversación')]
COSTOS = [('Evento', 35.3, 'Sede, producción técnica, registro, alimentos, personal'), ('Impresión', 25.9, 'Tiraje de 5.000 ejemplares'), ('Equipo y coordinación', 15.3, 'Ocho roles'),
          ('Contenido y corrección', 6.6, ''), ('Fotografía y audiovisual', 4.7, ''), ('Distribución', 4.7, ''), ('Diseño', 3.3, ''), ('Etiquetas NFC', 2.8, 'Tiraje completo desde la Edición 03'),
          ('Producción digital', 1.4, '')]
COBERTURA = [('Ed. 01', 52.0, 'Tarifa de lanzamiento'), ('Ed. 02', 52.0, 'Tarifa de lanzamiento'), ('Ed. 03', 54.4, ''), ('Ed. 04', 54.4, ''), ('Ed. 05', 54.4, ''), ('Ed. 06', 55.0, 'Gala')]
TRAYECTO = [('Fin de la tarifa de lanzamiento', 1.0, 'Descuento medio del 15 %'), ('Inventario completo del evento', 8.9, 'Cinco zonas y cinco mesas'),
            ('Ampliaciones con pauta', 2.2, 'Dos ediciones con 16 páginas más'), ('Actualización tarifaria', 5.5, 'Referencia del 10 %')]

def todos():
    return {
      'distribucion': barras_h('gr-dist', 'Reparto del tiraje de la Edición 01', '5.000 ejemplares, distribución gratuita', DIST, 0),
      'invitados': barras_h('gr-inv', 'Composición de invitados del evento', 'Porcentaje sobre el padrón de cada edición', INVITADOS, 0),
      'costos': barras_h('gr-cost', 'Estructura del costo base de una edición', 'Edición estándar con NFC completo · costo base = 100 %', COSTOS, 0),
      'cobertura': columnas('gr-cob', 'Cobertura de pauta y patrocinio por edición', 'Plan anual base 2027 · total anual 53,8 %', COBERTURA, 50, 'Meta del primer año · 50 %'),
      'trayecto': cascada('gr-tray', 'Trayectoria de referencia hacia el 70 %', 'Desde el segundo año, a tarifas de 2027', ('Plan base 2027', 53.8), TRAYECTO, 70, 'Meta desde el segundo año · 70 %', 80),
    }

if __name__ == '__main__':
    g = todos()
    open(os.path.join(AQUI, 'graficos-fragmento.html'), 'w', encoding='utf-8').write('\n'.join(f'<!-- {k} -->\n{v}' for k, v in g.items()))
    print('gráficos:', ', '.join(g))
