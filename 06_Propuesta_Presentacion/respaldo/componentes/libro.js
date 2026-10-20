/* Libro · motor de paso de página (GSAP 3.13 + Draggable)
   Hojas con anverso (página impar o portada) y reverso (página par siguiente).
   API: Libro.crear(contenedor, paginas[], {alCambiar}) → {ir(k), siguiente(), anterior(), pliego(), total}
   Accesibilidad: teclado (←/→, Inicio, Fin), botones externos, aria-live con el pliego activo.
   Movimiento reducido: cambio de pliego sin giro. */
(function () {
  const reduce = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function crear(raiz, paginas, opciones = {}) {
    // paginas: [C1, C2, 01, 02, 03, …, C3, C4] como elementos .pg
    const una = !!opciones.unaPagina;            // teléfono: una página por vez, giro sobre el borde izquierdo
    const hojasDatos = [];
    if (una) paginas.forEach(p => hojasDatos.push([p, null]));
    else for (let i = 0; i < paginas.length; i += 2) hojasDatos.push([paginas[i], paginas[i + 1] || null]);
    const N = hojasDatos.length;                 // hojas
    const T = N + 1;                             // pliegos posibles: 0 (cerrado) … N (contraportada)
    raiz.classList.add('libro'); raiz.classList.toggle('una', una);
    raiz.innerHTML = '';
    const escena = document.createElement('div'); escena.className = 'libro-escena';
    const lomo = document.createElement('div'); lomo.className = 'libro-lomo'; lomo.setAttribute('aria-hidden', 'true');
    escena.appendChild(lomo);
    const hojas = hojasDatos.map(([a, b], i) => {
      const h = document.createElement('div'); h.className = 'hoja'; h.dataset.i = i;
      const f = document.createElement('div'); f.className = 'cara frente'; f.appendChild(a);
      const r = document.createElement('div'); r.className = 'cara dorso'; if (b) r.appendChild(b); else r.classList.add('vacia');
      const sf = document.createElement('i'); sf.className = 'sombra s-f'; f.appendChild(sf);
      const sr = document.createElement('i'); sr.className = 'sombra s-r'; r.appendChild(sr);
      h.append(f, r); escena.appendChild(h); return h;
    });
    const vivo = document.createElement('p'); vivo.className = 'libro-vivo'; vivo.setAttribute('aria-live', 'polite');
    raiz.append(escena, vivo);

    let k = 0;                                    // pliego visible: hojas < k están giradas
    let anim = null;
    const prog = hojas.map(() => 0);             // 0 = sin girar · 1 = girada

    function pintar(i) {
      const p = prog[i], ang = -180 * p;
      // elevación sutil durante el giro y sombra que cambia de cara
      // orden de pila sin coplanaridad: a la derecha, la primera hoja arriba; a la izquierda, la última girada arriba
      const base = (p > .5 ? i : (N - i)) * .6;
      const z = base + Math.sin(p * Math.PI) * 30;
      gsap.set(hojas[i], { rotationY: ang, z });
      const sf = hojas[i].querySelector('.s-f'), sr = hojas[i].querySelector('.s-r');
      sf.style.opacity = Math.min(1, p * 2) * .55;
      sr.style.opacity = Math.max(0, 1 - p) * .55;
    }
    function encuadre(conAnim) {
      // libro cerrado: portada centrada; contraportada sola: centrada a la izquierda
      const desp = una ? 0 : (k === 0 ? -25 : (k === N ? 25 : 0));
      if (conAnim && !reduce()) gsap.to(escena, { xPercent: desp, duration: .7, ease: 'power3.inOut' });
      else gsap.set(escena, { xPercent: desp });
      raiz.classList.toggle('cerrado', k === 0); raiz.classList.toggle('final', k === N);
    }
    function avisar() {
      vivo.textContent = (opciones.nombres && opciones.nombres[k]) || ('Pliego ' + k);
      opciones.alCambiar && opciones.alCambiar(k, T);
    }
    hojas.forEach((_, i) => pintar(i));
    encuadre(false);

    function ir(destino, rapido) {
      destino = Math.max(0, Math.min(N, destino));
      if (destino === k) return;
      anim && anim.progress(1).kill();
      const ida = destino > k;
      const indices = [];
      if (ida) for (let i = k; i < destino; i++) indices.push(i);
      else for (let i = k - 1; i >= destino; i--) indices.push(i);
      k = destino; avisar(); encuadre(true);
      if (reduce() || rapido) { indices.forEach(i => { prog[i] = ida ? 1 : 0; pintar(i); }); return; }
      anim = gsap.timeline();
      indices.forEach((i, n) => {
        const o = { p: prog[i] };
        anim.to(o, { p: ida ? 1 : 0, duration: indices.length > 1 ? .55 : .95, ease: 'power2.inOut',
          onUpdate: () => { prog[i] = o.p; pintar(i); } }, n * .12);
      });
    }
    const ultimo = una ? N - 1 : N;               // en una página no hay pliego vacío final
    const siguiente = () => ir(Math.min(ultimo, k + 1)), anterior = () => ir(k - 1);

    // Clic en la mitad derecha o izquierda del libro
    escena.addEventListener('click', e => {
      if (raiz.classList.contains('arrastrando')) return;
      const r = raiz.getBoundingClientRect();
      (e.clientX - r.left > r.width / 2) ? siguiente() : anterior();
    });
    // Teclado
    raiz.tabIndex = 0;
    raiz.addEventListener('keydown', e => {
      if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); siguiente(); }
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); anterior(); }
      else if (e.key === 'Home') { e.preventDefault(); ir(0); }
      else if (e.key === 'End') { e.preventDefault(); ir(ultimo); }
    });
    // Arrastre de la esquina (Draggable sobre un asa invisible)
    if (window.Draggable) {
      const asa = document.createElement('div'); asa.className = 'libro-asa'; asa.setAttribute('aria-hidden', 'true'); raiz.appendChild(asa);
      let i0 = -1, dir = 0, ancho = 1, x0 = 0;
      Draggable.create(asa, {
        type: 'x', trigger: escena, minimumMovement: 6, zIndexBoost: false,
        onPress(e) { const r = raiz.getBoundingClientRect(); ancho = una ? r.width : r.width / 2; x0 = this.pointerX;
          dir = una ? 0 : ((this.pointerX - r.left > r.width / 2) ? 1 : -1); i0 = dir > 0 ? k : k - 1; },
        onDragStart() { if (i0 < 0 || i0 >= N || reduce()) return; raiz.classList.add('arrastrando'); anim && anim.progress(1).kill(); },
        onDrag() {
          if (i0 < 0 || i0 >= N || reduce()) return;
          if (una && dir === 0) { dir = this.pointerX < x0 ? 1 : -1; i0 = dir > 0 ? k : k - 1; if (i0 < 0 || i0 >= ultimo + (dir > 0 ? 0 : 1)) return; }
          const d = (x0 - this.pointerX) / (ancho * 2) * 2;     // 0…1 a lo ancho de una página
          prog[i0] = gsap.utils.clamp(0, 1, dir > 0 ? d : 1 + d); pintar(i0);
        },
        onDragEnd() {
          if (i0 < 0 || i0 >= N || reduce()) { setTimeout(() => raiz.classList.remove('arrastrando'), 0); return; }
          const v = this.getDirection('velocity');
          const completar = dir > 0 ? (prog[i0] > .35 || v === 'left') : (prog[i0] < .65 || v === 'right');
          const meta = dir > 0 ? (completar ? 1 : 0) : (completar ? 0 : 1);
          const o = { p: prog[i0] }, i = i0;
          gsap.to(o, { p: meta, duration: .45, ease: 'power2.out', onUpdate: () => { prog[i] = o.p; pintar(i); } });
          if (completar) { k = dir > 0 ? i0 + 1 : i0; avisar(); encuadre(true); }
          gsap.set(asa, { x: 0 });
          setTimeout(() => raiz.classList.remove('arrastrando'), 0);
        }
      });
    }
    avisar();
    return { ir, siguiente, anterior, pliego: () => k, total: T };
  }
  window.Libro = { crear };
})();
