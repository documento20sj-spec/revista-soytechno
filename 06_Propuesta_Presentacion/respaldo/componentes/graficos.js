/* Información emergente de los gráficos: al pasar el puntero o al enfocar con teclado. Texto insertado con textContent. */
(function () {
  const tip = document.createElement('div'); tip.className = 'gr-tip'; tip.setAttribute('role', 'status');
  const fuerte = document.createElement('strong'), et = document.createElement('div'), det = document.createElement('span');
  tip.append(fuerte, et, det); document.addEventListener('DOMContentLoaded', () => document.body.appendChild(tip));
  function mostrar(el, x, y) {
    fuerte.textContent = el.dataset.val || ''; et.textContent = el.dataset.tip || ''; det.textContent = el.dataset.det || '';
    tip.classList.add('on');
    const w = tip.offsetWidth, h = tip.offsetHeight;
    tip.style.left = Math.min(innerWidth - w - 8, Math.max(8, x + 14)) + 'px';
    tip.style.top = Math.max(8, y - h - 12) + 'px';
  }
  const ocultar = () => tip.classList.remove('on');
  document.addEventListener('pointermove', e => {
    const el = e.target.closest && e.target.closest('[data-tip]');
    if (el && el.closest('.gr, .dg')) mostrar(el, e.clientX, e.clientY); else ocultar();
  });
  document.addEventListener('focusin', e => {
    const el = e.target.closest && e.target.closest('.gr [data-tip], .dg [data-tip]');
    if (el) { const r = el.getBoundingClientRect(); mostrar(el, r.left + r.width / 2, r.top); }
  });
  document.addEventListener('focusout', ocultar);

  /* Teclado: cada gráfico o diagrama es una sola parada de tabulación y las flechas recorren sus elementos
     (tabindex itinerante); con una parada por barra, punto o celda el recorrido sumaba un centenar de paradas */
  const ELEMENTOS = '.gr-fila, .gr-col, .ca-d, .hc-h, button.mp-p';
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.gr, .dg').forEach(caja => {
      const els = [...caja.querySelectorAll(ELEMENTOS)];
      if (els.length < 2) return;
      els.forEach((el, i) => el.setAttribute('tabindex', i ? '-1' : '0'));
      caja.addEventListener('keydown', e => {
        const i = els.indexOf(e.target); if (i < 0) return;
        const paso = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1, Home: -i, End: els.length - 1 - i }[e.key];
        if (paso === undefined) return;
        e.preventDefault(); e.stopPropagation();            // las flechas no pasan al libro ni al circuito
        const j = Math.max(0, Math.min(els.length - 1, i + paso));
        els[i].setAttribute('tabindex', '-1'); els[j].setAttribute('tabindex', '0'); els[j].focus();
      });
    });
  });
})();
