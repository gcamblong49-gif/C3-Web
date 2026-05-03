#!/usr/bin/env python
# -*- coding: utf-8 -*-
path = 'C:/Users/LENOVO/OneDrive/Documents/C3 web/c3_arquitectura.html'
content = open(path, encoding='utf-8').read()

# === 1. CSS OVERRIDES ===
new_css = """
  /* === ATV-STYLE OVERRIDES === */
  .nav-logo img { display: none !important; }
  .nav-logo { line-height: 1.2; text-decoration: none; }
  .nav-logo-text { font-size: 9px; font-weight: 500; letter-spacing: .22em; text-transform: uppercase; color: var(--black); display: block; }
  .nav-links { display: none !important; }
  nav { padding: 24px 40px; }
  .hamburger { display: flex; flex-direction: column; gap: 6px; cursor: pointer; background: none; border: none; padding: 4px; }
  .hamburger span { display: block; width: 24px; height: 1px; background: var(--black); transition: background .3s; }
  .nav-menu { position: fixed; top: 0; right: -100%; width: 280px; height: 100vh; background: var(--black); z-index: 200; padding: 0 48px; transition: right .4s ease; display: flex; flex-direction: column; justify-content: center; }
  .nav-menu.open { right: 0; }
  .nav-menu ul { list-style: none; }
  .nav-menu ul li { padding: 20px 0; border-bottom: 1px solid rgba(255,255,255,.08); }
  .nav-menu ul li a { color: var(--white); text-decoration: none; font-size: 11px; letter-spacing: .22em; text-transform: uppercase; font-weight: 400; cursor: pointer; }
  .nav-menu-close { background: none; border: none; color: var(--white); font-size: 28px; cursor: pointer; position: absolute; top: 24px; right: 36px; font-weight: 200; line-height: 1; }

  .hero { background: #1a1a1a; grid-template-columns: unset !important; min-height: 100vh; display: flex; align-items: flex-end; padding-bottom: 90px; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(0,0,0,.2) 0%, rgba(0,0,0,.55) 100%); z-index: 1; }
  .hero-left { z-index: 2; padding: 0 52px; border-right: none !important; justify-content: flex-end; }
  .hero-right { display: none !important; }
  .hero-bottom { z-index: 2; }
  .slogan-c { color: #fff; }
  .slogan-word { color: rgba(255,255,255,.45); }
  .slogan-line { border-color: rgba(255,255,255,.12) !important; }
  .hero-eyebrow { color: rgba(255,255,255,.5); }
  .hero-desc { color: rgba(255,255,255,.5); border-left-color: rgba(255,255,255,.15); }
  .hero-cta { color: #fff; }
  .hero-cta-line { background: #fff; }
  .hero-bottom { color: rgba(255,255,255,.4); }
  .scroll-line { background: rgba(255,255,255,.3); }
  .hero-label-v { position: absolute; right: 48px; top: 50%; transform: translateY(-50%) rotate(90deg); font-size: 9px; letter-spacing: .3em; text-transform: uppercase; color: rgba(255,255,255,.35); z-index: 2; white-space: nowrap; }

  .proj-grid { grid-template-columns: repeat(2,1fr) !important; gap: 0 !important; margin-top: 0 !important; }
  .proj-item { padding: 40px 32px 32px; border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); }
  .proj-item:nth-child(even) { border-right: none; }
  .proj-item-title { font-size: clamp(20px,2.5vw,32px); font-weight: 300; color: #aaa; letter-spacing: -.01em; margin-bottom: 10px; }
  .proj-item-sub { font-size: 11px; color: #bbb; letter-spacing: .04em; line-height: 1.6; margin-bottom: 18px; }
  .proj-item-link { font-size: 9px; letter-spacing: .2em; text-transform: uppercase; color: var(--black); text-decoration: none; display: inline-flex; align-items: center; gap: 8px; transition: gap .3s; margin-bottom: 24px; cursor: none; }
  .proj-item-link:hover { gap: 14px; }
  .proj-card { aspect-ratio: 4/3; background: #dddcd8; overflow: hidden; position: relative; }
  .proj-card img { width: 100%; height: 100%; object-fit: cover; transition: transform .7s ease; display: block; }
  .proj-card:hover img { transform: scale(1.04); }
  .proj-over { display: none !important; }

  footer { background: #888 !important; padding: 52px !important; display: grid !important; grid-template-columns: 1fr 1fr 1fr !important; gap: 40px !important; align-items: start !important; border-top: none !important; }
  .ft-label { font-size: 9px; letter-spacing: .22em; text-transform: uppercase; color: rgba(255,255,255,.45); display: block; margin-bottom: 16px; font-weight: 500; }
  .ft-line { font-size: 11px; color: rgba(255,255,255,.8); display: block; line-height: 2.2; }
  .ft-social { display: flex; gap: 16px; margin-top: 16px; }
  .ft-social a { color: rgba(255,255,255,.6); text-decoration: none; font-size: 10px; letter-spacing: .15em; text-transform: uppercase; transition: color .3s; cursor: none; }
  .ft-social a:hover { color: #fff; }
  .ft-copy { font-size: 9px; letter-spacing: .1em; color: rgba(255,255,255,.3); margin-top: 32px; display: block; }

  .wa-btn { position: fixed; bottom: 28px; right: 28px; width: 52px; height: 52px; background: #25D366; border-radius: 50%; display: flex; align-items: center; justify-content: center; z-index: 500; text-decoration: none; box-shadow: 0 4px 16px rgba(37,211,102,.4); transition: transform .3s; cursor: none; }
  .wa-btn:hover { transform: scale(1.08); }
  .wa-btn svg { width: 26px; height: 26px; fill: white; }
"""
content = content.replace('</style>', new_css + '</style>', 1)
print('1. CSS done')

# === 2. NAV HTML ===
nav_s = content.find('<nav id="nav">')
nav_e = content.find('</nav>') + 6
new_nav = (
    '<nav id="nav">\n'
    '  <a class="nav-logo" href="#hero" onclick="goTo(\'hero\');return false;">\n'
    '    <span class="nav-logo-text">C3</span>\n'
    '    <span class="nav-logo-text">ARQU</span>\n'
    '    <span class="nav-logo-text">ITEC</span>\n'
    '    <span class="nav-logo-text">TURA</span>\n'
    '  </a>\n'
    '  <button class="hamburger" onclick="toggleMenu()" aria-label="Menu">\n'
    '    <span></span><span></span>\n'
    '  </button>\n'
    '</nav>\n'
    '<div class="nav-menu" id="navMenu">\n'
    '  <button class="nav-menu-close" onclick="toggleMenu()">&#215;</button>\n'
    '  <ul>\n'
    '    <li><a href="#servicios" onclick="goTo(\'servicios\');toggleMenu();return false;">Servicios</a></li>\n'
    '    <li><a href="#nosotros" onclick="goTo(\'nosotros\');toggleMenu();return false;">Nosotros</a></li>\n'
    '    <li><a href="#proyectos" onclick="goTo(\'proyectos\');toggleMenu();return false;">Proyectos</a></li>\n'
    '    <li><a href="#contacto" onclick="goTo(\'contacto\');toggleMenu();return false;">Contacto</a></li>\n'
    '  </ul>\n'
    '</div>'
)
content = content[:nav_s] + new_nav + content[nav_e:]
print('2. Nav done')

# === 3. HERO - add vertical label ===
hero_left = content.find('<div class="hero-left">')
insert_after = content.rfind('>', 0, hero_left) + 1
content = content[:insert_after] + '\n  <div class="hero-label-v">EL ESTUDIO</div>' + content[insert_after:]
print('3. Hero label done')

# === 4. FOOTER REPLACE ===
foot_s = content.find('<footer>')
foot_e = content.find('</footer>') + 9
new_footer = (
    '<footer>\n'
    '  <div>\n'
    '    <span class="ft-label">Contacto</span>\n'
    '    <span class="ft-line">info@c3arquitectura.ar</span>\n'
    '    <span class="ft-line">+54 11 5578 2599</span>\n'
    '    <div class="ft-social">\n'
    '      <a href="#">IG</a>\n'
    '      <a href="#">LI</a>\n'
    '      <a href="#">WA</a>\n'
    '    </div>\n'
    '    <span class="ft-copy">&copy; 2025 C3 Arquitectura. Todos los derechos reservados.</span>\n'
    '  </div>\n'
    '  <div>\n'
    '    <span class="ft-label">Newsletter</span>\n'
    '    <span class="ft-line" style="color:rgba(255,255,255,.4);">Pronto disponible</span>\n'
    '  </div>\n'
    '  <div>\n'
    '    <span class="ft-label">Estudio</span>\n'
    '    <span class="ft-line">Buenos Aires</span>\n'
    '    <span class="ft-line">Argentina</span>\n'
    '    <span class="ft-line" style="margin-top:16px;">C3 Arquitectura</span>\n'
    '  </div>\n'
    '</footer>'
)
content = content[:foot_s] + new_footer + content[foot_e:]
print('4. Footer done')

# === 5. WHATSAPP BUTTON ===
wa = (
    '<a class="wa-btn" href="https://api.whatsapp.com/send/?phone=541155782599&amp;text=Hola%2C+me+interesa+C3+Arquitectura" target="_blank" aria-label="WhatsApp">\n'
    '  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">'
    '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>'
    '</svg>\n'
    '</a>'
)
content = content.replace('</body>', wa + '\n</body>')
print('5. WA done')

# === 6. EXTRA JS ===
extra_js = """
  function toggleMenu() {
    document.getElementById('navMenu').classList.toggle('open');
  }
  document.addEventListener('DOMContentLoaded', function() {
    var grid = document.querySelector('.proj-grid');
    if (!grid) return;
    var cards = Array.from(grid.querySelectorAll('.proj-card'));
    grid.innerHTML = '';
    cards.forEach(function(card) {
      var over = card.querySelector('.proj-over');
      var title = over && over.querySelector('h3') ? over.querySelector('h3').textContent : '';
      var sub = over && over.querySelector('p') ? over.querySelector('p').textContent : '';
      var item = document.createElement('div');
      item.className = 'proj-item';
      if (title) {
        var meta = document.createElement('div');
        meta.innerHTML = '<p class="proj-item-title">' + title + '</p>' +
          (sub ? '<p class="proj-item-sub">' + sub + '</p>' : '') +
          '<a class="proj-item-link" href="#">ver m&#225;s &#8250;</a>';
        item.appendChild(meta);
      }
      item.appendChild(card);
      grid.appendChild(item);
    });
  });
"""
last_s = content.rfind('</script>')
content = content[:last_s] + extra_js + '\n</script>' + content[last_s+9:]
print('6. JS done')

open(path, 'w', encoding='utf-8').write(content)
print('GUARDADO OK')
