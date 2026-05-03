#!/usr/bin/env python
# -*- coding: utf-8 -*-
path = 'C:/Users/LENOVO/OneDrive/Documents/C3 web/c3_arquitectura.html'
content = open(path, encoding='utf-8').read()

# === 1. CSS FIXES + TOPICS + SLIDER ===
new_css = """
  /* CURSOR FIX - mix-blend-mode invierte automatico en oscuro/claro */
  .cursor { background: #fff !important; mix-blend-mode: difference; }
  .cursor-ring { border-color: rgba(255,255,255,.6) !important; mix-blend-mode: difference; }

  /* NAV - hamburger blanco sobre hero, negro al scrollear */
  .hamburger span { background: #fff; transition: background .3s; }
  nav.scrolled .hamburger span { background: var(--black); }
  nav.scrolled { background: rgba(255,255,255,.96); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line); }

  /* FOOTER - negro como el nav */
  footer { background: var(--black) !important; }
  .ft-label { color: rgba(255,255,255,.35) !important; }
  .ft-line { color: rgba(255,255,255,.7) !important; }
  .ft-social a { color: rgba(255,255,255,.45) !important; }
  .ft-copy { color: rgba(255,255,255,.2) !important; }

  /* HERO SLIDER */
  .hero { position: relative; min-height: 100vh; overflow: hidden; background: #111; display: block !important; padding: 0 !important; }
  .hero::before { display: none; }
  .hero-slide { position: absolute; inset: 0; opacity: 0; transition: opacity 1s ease; background-size: cover; background-position: center; }
  .hero-slide.active { opacity: 1; }
  .hero-slide::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(0,0,0,.25) 0%, rgba(0,0,0,.6) 100%); }
  .hero-content { position: absolute; bottom: 90px; left: 52px; z-index: 10; }
  .hero-label-v { position: absolute; right: 48px; top: 50%; transform: translateY(-50%) rotate(90deg); font-size: 9px; letter-spacing: .3em; text-transform: uppercase; color: rgba(255,255,255,.4); z-index: 10; white-space: nowrap; transition: opacity .5s; }
  .hero-arrows { position: absolute; bottom: 40px; right: 52px; display: flex; gap: 16px; z-index: 10; }
  .hero-arrow { background: none; border: 1px solid rgba(255,255,255,.3); color: #fff; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 16px; transition: background .3s, border .3s; }
  .hero-arrow:hover { background: rgba(255,255,255,.1); border-color: rgba(255,255,255,.6); }
  .hero-dots { position: absolute; bottom: 52px; left: 52px; display: flex; gap: 10px; z-index: 10; }
  .hero-dot { width: 20px; height: 1px; background: rgba(255,255,255,.3); transition: background .4s, width .4s; cursor: pointer; }
  .hero-dot.active { background: #fff; width: 36px; }
  /* keep existing hero text classes working */
  .hero-left { position: relative; z-index: 10; padding: 0; border: none !important; background: none; display: block; }
  .hero-eyebrow, .hero-slogan, .hero-desc, .hero-cta { display: block; }
  .hero-right, .hero-bottom { display: none !important; }
  .slogan-c { color: #fff; }
  .slogan-word { color: rgba(255,255,255,.45); }
  .slogan-line { border-color: rgba(255,255,255,.12) !important; }
  .hero-eyebrow { color: rgba(255,255,255,.5); margin-bottom: 32px; }
  .hero-desc { color: rgba(255,255,255,.5); border-left-color: rgba(255,255,255,.15); }
  .hero-cta { color: #fff; }
  .hero-cta-line { background: #fff; }

  /* TOPICS SECTION */
  .topics { border-top: 1px solid var(--line); }
  .topics-grid { display: grid; grid-template-columns: 1fr 1fr; }
  .topic-item { padding: 48px 40px 40px; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); }
  .topic-item:nth-child(even) { border-right: none; }
  .topic-num { font-size: 9px; letter-spacing: .28em; color: var(--gray); text-transform: uppercase; margin-bottom: 20px; display: block; }
  .topic-title { font-size: clamp(22px,2.8vw,38px); font-weight: 300; color: #aaa; letter-spacing: -.02em; margin-bottom: 14px; }
  .topic-desc { font-size: 12px; color: #999; line-height: 1.85; font-weight: 300; margin-bottom: 28px; max-width: 380px; }
  .topic-img { width: 100%; aspect-ratio: 16/10; object-fit: cover; display: block; transition: transform .7s ease; overflow: hidden; }
  .topic-img-wrap { overflow: hidden; }
  .topic-img-wrap:hover .topic-img { transform: scale(1.04); }
"""
content = content.replace('</style>', new_css + '</style>', 1)
print('1. CSS done')

# === 2. RESTRUCTURE HERO - add slides ===
hero_start = content.find('<div class="hero">')
# Find end of hero div (hero-bottom closing div)
# The hero ends before <div class="divider">
divider_pos = content.find('<div class="divider">')
# Extract original hero-left content
hero_left_s = content.find('<div class="hero-left">', hero_start)
hero_left_e = content.find('</div>', content.find('</div>', content.find('</div>', content.find('</div>', hero_left_s + 100) + 1) + 1) + 1) + 6

# Get the original hero-left inner content
hero_left_inner = content[hero_left_s:hero_left_e]

new_hero = (
    '<div class="hero" id="hero">\n'
    '  <!-- SLIDES -->\n'
    '  <div class="hero-slide active" style="background-image:url(\'img/RENDERS SEPARADOS/Fachada _ Peatonal.jpg\')"></div>\n'
    '  <div class="hero-slide" style="background-image:url(\'img/RENDERS SEPARADOS/ai-render-7081684.jpg\')"></div>\n'
    '  <!-- CONTENT -->\n'
    '  <div class="hero-content">\n'
    '    <div class="hero-eyebrow reveal">Buenos Aires · Argentina</div>\n'
    '    <div class="hero-slogan reveal d1">\n'
    '      <div class="slogan-line"><span class="slogan-c">C</span><span class="slogan-word">riterio</span></div>\n'
    '      <div class="slogan-line"><span class="slogan-c">C</span><span class="slogan-word">alidad</span></div>\n'
    '      <div class="slogan-line"><span class="slogan-c">C</span><span class="slogan-word">onstrucción</span></div>\n'
    '    </div>\n'
    '    <p class="hero-desc reveal d2">Diseño, visualización y desarrollo inmobiliario.<br>Buenos Aires, Argentina.</p>\n'
    '    <a class="hero-cta reveal d3" href="#topics" onclick="goTo(\'topics\');return false;">\n'
    '      <span class="hero-cta-line"></span>Explorar\n'
    '    </a>\n'
    '  </div>\n'
    '  <!-- LABEL VERTICAL -->\n'
    '  <div class="hero-label-v" id="heroLabel">EL ESTUDIO</div>\n'
    '  <!-- ARROWS -->\n'
    '  <div class="hero-arrows">\n'
    '    <button class="hero-arrow" onclick="slideHero(-1)">&#8249;</button>\n'
    '    <button class="hero-arrow" onclick="slideHero(1)">&#8250;</button>\n'
    '  </div>\n'
    '  <!-- DOTS -->\n'
    '  <div class="hero-dots">\n'
    '    <div class="hero-dot active" onclick="goSlide(0)"></div>\n'
    '    <div class="hero-dot" onclick="goSlide(1)"></div>\n'
    '  </div>\n'
    '</div>\n'
)

# Replace from <div class="hero"> to before <div class="divider">
hero_full_end = content.find('<div class="divider">')
content = content[:hero_start] + new_hero + content[hero_full_end:]
print('2. Hero slider done')

# === 3. TOPICS SECTION - insert before divider ===
topics_section = (
    '<section class="topics" id="topics">\n'
    '  <div class="topics-grid">\n'

    '    <div class="topic-item reveal">\n'
    '      <span class="topic-num">01 — La Ciudad</span>\n'
    '      <h3 class="topic-title">La Ciudad.</h3>\n'
    '      <p class="topic-desc">C3 lee la ciudad antes de proyectar. Cada intervención dialoga con su entorno, su escala y su tiempo. Proyectamos desde adentro hacia afuera, entendiendo que la buena arquitectura no sólo ocupa un lote: construye ciudad.</p>\n'
    '      <div class="topic-img-wrap"><img class="topic-img" src="img/CIUDAD.jpg" alt="La Ciudad" loading="lazy"></div>\n'
    '    </div>\n'

    '    <div class="topic-item reveal d1">\n'
    '      <span class="topic-num">02 — Lo Material</span>\n'
    '      <h3 class="topic-title">Lo Material.</h3>\n'
    '      <p class="topic-desc">Elegimos los materiales con criterio. La textura, el peso y la durabilidad no son datos técnicos: son decisiones proyectuales que definen la experiencia del espacio. Cada elección tiene un porqué.</p>\n'
    '      <div class="topic-img-wrap"><img class="topic-img" src="img/material 1.jpg" alt="Lo Material" loading="lazy"></div>\n'
    '    </div>\n'

    '    <div class="topic-item reveal">\n'
    '      <span class="topic-num">03 — El Proyecto</span>\n'
    '      <h3 class="topic-title">El Proyecto.</h3>\n'
    '      <p class="topic-desc">Cada encargo empieza con escucha. Formalizamos ideas en geometrías precisas, donde la funcionalidad y la estética no compiten: se potencian. Visualizamos con precisión antes de construir con convición.</p>\n'
    '      <div class="topic-img-wrap"><img class="topic-img" src="img/proyecto.jpg" alt="El Proyecto" loading="lazy"></div>\n'
    '    </div>\n'

    '    <div class="topic-item reveal d1">\n'
    '      <span class="topic-num">04 — Lo Inmobiliario</span>\n'
    '      <h3 class="topic-title">Lo Inmobiliario.</h3>\n'
    '      <p class="topic-desc">La doble mirada —arquitectónica e inmobiliaria— es lo que distingue a C3. Entendemos el valor del metro cuadrado porque entendemos el espacio que lo habita. Asesoramos en compra, venta e inversión con criterio de arquitecto.</p>\n'
    '      <div class="topic-img-wrap"><img class="topic-img" src="img/INMOBILIARIO.jpg" alt="Lo Inmobiliario" loading="lazy"></div>\n'
    '    </div>\n'

    '    <div class="topic-item reveal" style="grid-column: 1 / -1; max-width: 50%; border-right: none;">\n'
    '      <span class="topic-num">05 — Lo Académico</span>\n'
    '      <h3 class="topic-title">Lo Académico.</h3>\n'
    '      <p class="topic-desc">Nos formamos en la UBA–FADU y seguimos aprendiendo. La disciplina se nutre de la reflexión académica, y esa base rigurosa es la que sostiene cada decisión proyectual. Estudiar es también una forma de proyectar.</p>\n'
    '      <div class="topic-img-wrap"><img class="topic-img" src="img/ACADEMICO.jpg" alt="Lo Académico" loading="lazy"></div>\n'
    '    </div>\n'

    '  </div>\n'
    '</section>\n'
)

# Insert topics before the services section
services_pos = content.find('<section class="section" id="servicios">')
content = content[:services_pos] + topics_section + content[services_pos:]
print('3. Topics done')

# === 4. JS - slider + toggleMenu ===
slider_js = """
  // Hero slider
  var _slides = document.querySelectorAll('.hero-slide');
  var _dots = document.querySelectorAll('.hero-dot');
  var _labels = ['EL PROYECTO', 'EL RENDER'];
  var _cur = 0;
  var _sliderTimer;

  function goSlide(n) {
    _slides[_cur].classList.remove('active');
    _dots[_cur].classList.remove('active');
    _cur = (n + _slides.length) % _slides.length;
    _slides[_cur].classList.add('active');
    _dots[_cur].classList.add('active');
    var lbl = document.getElementById('heroLabel');
    if (lbl && _labels[_cur]) lbl.textContent = _labels[_cur];
    clearInterval(_sliderTimer);
    _sliderTimer = setInterval(function(){ goSlide(_cur + 1); }, 6000);
  }
  function slideHero(dir) { goSlide(_cur + dir); }
  _sliderTimer = setInterval(function(){ goSlide(_cur + 1); }, 6000);

  function toggleMenu() {
    document.getElementById('navMenu').classList.toggle('open');
  }
"""
last_s = content.rfind('</script>')
content = content[:last_s] + slider_js + '\n</script>' + content[last_s+9:]
print('4. JS done')

open(path, 'w', encoding='utf-8').write(content)
print('GUARDADO OK')
