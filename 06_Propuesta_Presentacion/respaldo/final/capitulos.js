/* =====================================================================
   9 bis · CAPÍTULOS 3 A 11: mapa → revista, gráficos, NFC y simulación de la hora cero
   ===================================================================== */
/* Mapa de paginación: cada página incluida en la simulación abre su pliego (botones reales: Intro y Espacio ya los activan) */
$$('.mp-p[data-pliego]').forEach(c => c.addEventListener('click', () => { const k = +c.dataset.pliego; if (bookST) goStop(k); else { stopStatic(k); goChapter(2); } }));

/* Simulación de la hora cero: 19:28:00 → 19:30:00 (descubrimiento) → 19:35:00 (bloque digital) */
const hz = { hora: $('#hzHora'), fase: $('#hzFase'), btn: $('#hzBtn'), velo: $('#hzVelo'), img: $('#hzMarco img'), chips: $$('#hzChips li'), tl: null, hecho: false };
const hzFmt = s => `19:${String(Math.floor(s / 60) - 1140).padStart(2, '0')}:${String(Math.floor(s % 60)).padStart(2, '0')}`;   // s: segundos desde las 00:00 (19:28 = 70080)
const FASES_HZ = { ini: 'Cuenta regresiva en pantalla LED · 120 segundos', cero: 'Descubrimiento en escena · transmisión en directo', bloque: 'Bloque de las 19:35 · edición digital, pódcast, QR y NFC activos en 60 segundos' };
function hzEstado(final) {
  if (!hz.hora) return;
  hz.hora.textContent = final ? '19:35:00' : '19:28:00';
  hz.hora.classList.toggle('cero', final);
  hz.fase.textContent = final ? FASES_HZ.bloque : FASES_HZ.ini;
  hz.chips.forEach(c => c.classList.toggle('on', final));
  if (HAS_GSAP) { gsap.set(hz.velo, { yPercent: final ? -100 : 0 }); gsap.set(hz.chips, { clearProps: 'all' }); }
  else hz.velo.style.transform = final ? 'translateY(-100%)' : '';
}
function hzSimular() {
  if (!hz.hora) return;
  if (!HAS_GSAP || REDUCED) { hzEstado(true); return; }
  if (hz.tl) hz.tl.kill();
  hzEstado(false);
  const o = { s: 70080 };                                   // 19:28:00
  hz.btn.firstChild.textContent = 'Ver el resultado ';      // mientras corre, el botón la detiene en su estado final
  // menos de 5 s en total: el movimiento que arranca solo y dura más necesitaría control de pausa (WCAG 2.2.2)
  hz.tl = gsap.timeline({ onComplete: () => { hz.btn.firstChild.textContent = 'Repetir la simulación '; } })
    .to(o, { s: 70200, duration: 2.4, ease: 'none', onUpdate: () => { hz.hora.textContent = hzFmt(o.s); } }, 0)         // 120 s comprimidos
    .call(() => { hz.hora.classList.add('cero'); hz.fase.textContent = FASES_HZ.cero; }, null, 2.4)
    .to(hz.velo, { yPercent: -100, duration: .8, ease: 'expo.inOut' }, 2.4)
    .fromTo(hz.img, { scale: 1.08 }, { scale: 1, duration: 1.2, ease: 'power3.out' }, 2.4)
    .to(o, { s: 70500, duration: 1, ease: 'power1.inOut', onUpdate: () => { hz.hora.textContent = hzFmt(o.s); } }, 3.4)  // hasta las 19:35
    .call(() => { hz.fase.textContent = FASES_HZ.bloque; }, null, 4.4)
    .to(hz.chips, { opacity: 1, backgroundColor: 'rgba(27,107,214,.35)', borderColor: '#1B6BD6', duration: .25, ease: 'power1.out', stagger: .15 }, 4.4);   // termina a los 4,95 s
}
if (hz.btn) hz.btn.addEventListener('click', () => { if (hz.tl && hz.tl.isActive()) hz.tl.progress(1); else hzSimular(); });

/* Gráficos: las barras parten de su línea base y crecen al entrar en pantalla (una vez).
   El estado inicial se fija al arrancar: con from() las barras se verían completas, saltarían a cero y luego crecerían. */
function graficosST() {
  gsap.set($$('.gr .gr-barra, .paq .bar'), { scaleX: 0 });
  gsap.set($$('.gr .gr-cbar'), { scaleY: 0 });
  const crecer = g => {
    if (g.dataset.crecido) return; g.dataset.crecido = '1';
    const hb = $$('.gr-barra, .bar', g), cb = $$('.gr-cbar', g);
    if (hb.length) gsap.to(hb, { scaleX: 1, duration: .7, ease: 'power3.out', stagger: .05 });
    if (cb.length) gsap.to(cb, { scaleY: 1, duration: .7, ease: 'power3.out', stagger: .06 });
  };
  ScrollTrigger.batch('.gr, .paq', {
    start: 'top 85%', once: true,
    onEnter: els => els.forEach(crecer),
    onLeave: els => els.forEach(crecer)                     // salto por el carril o el teclado: el gráfico ya pasado queda completo
  });
}
function extrasAnimados() {
  graficosST();
  const onda = $('#nfcOnda');
  if (onda) gsap.fromTo(onda, { scale: 1, opacity: .9 }, { scale: 1.9, opacity: 0, duration: 1.8, ease: 'power2.out', repeat: 1, repeatDelay: .6,   // dos pulsos (4,2 s) cada vez que entra en pantalla: sin bucle que pida control de pausa
    scrollTrigger: { trigger: '.phy', start: 'top 85%', end: 'bottom 15%', toggleActions: 'restart none restart none' } });
  if (hz.hora) ScrollTrigger.create({ trigger: '#hzSim', start: 'top 65%', once: true, onEnter: () => { if (!hz.hecho) { hz.hecho = true; hzSimular(); } } });
}
function extrasEstaticos() { hzEstado(true); }
