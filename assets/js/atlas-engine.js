/* atlas-engine.js — Navegação multi-seção do Atlas
   Sem dependências externas. Cada .atlas-section é independente. */
(function () {
  'use strict';

  function initSection(section) {
    var tabs   = section.querySelectorAll('.atlas-tab');
    var panels = section.querySelectorAll('.atlas-panel');
    if (!tabs.length || !panels.length) return null;

    function activateMap(mapId) {
      tabs.forEach(function (t) {
        t.setAttribute('aria-selected', t.dataset.map === mapId ? 'true' : 'false');
      });
      panels.forEach(function (p) {
        if (p.dataset.map === mapId) {
          p.removeAttribute('hidden');
        } else {
          p.setAttribute('hidden', '');
        }
      });
    }

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        activateMap(this.dataset.map);
      });

      tab.addEventListener('keydown', function (e) {
        var all  = Array.from(tabs);
        var idx  = all.indexOf(this);
        var next = idx;
        if      (e.key === 'ArrowRight' || e.key === 'ArrowDown') next = (idx + 1) % all.length;
        else if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')   next = (idx - 1 + all.length) % all.length;
        else if (e.key === 'Home')  next = 0;
        else if (e.key === 'End')   next = all.length - 1;
        else return;
        e.preventDefault();
        all[next].focus();
        activateMap(all[next].dataset.map);
      });
    });

    section.querySelectorAll('.atlas-zoom-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var img = this.closest('.atlas-map-container').querySelector('.atlas-map');
        if (img && img.src) window.open(img.src, '_blank', 'noopener');
      });
    });

    /* Ativa o primeiro tab por padrão */
    if (tabs[0]) activateMap(tabs[0].dataset.map);

    return activateMap;
  }

  function init() {
    var sections = document.querySelectorAll('.atlas-section');
    var activators = {};

    sections.forEach(function (sec) {
      if (sec.id) activators[sec.id] = initSection(sec);
    });

    /* Links da sidebar com data-goto-section + data-goto-map */
    document.querySelectorAll('[data-goto-map]').forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        var mapId     = this.dataset.gotoMap;
        var sectionId = this.dataset.gotoSection;
        var section   = sectionId ? document.getElementById(sectionId) : sections[0];

        if (section) {
          if (activators[section.id]) activators[section.id](mapId);
          section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
