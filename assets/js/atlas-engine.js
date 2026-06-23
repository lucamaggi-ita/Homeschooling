/* atlas-engine.js — Navegação entre os 6 mapas do Atlas v1
   Sem dependências externas. */
(function () {
  'use strict';

  function init() {
    var tabs   = document.querySelectorAll('.atlas-tab');
    var panels = document.querySelectorAll('.atlas-panel');

    if (!tabs.length || !panels.length) return;

    /* ── Trocar mapa ────────────────────────────────────────── */
    function activateMap(mapId) {
      tabs.forEach(function (t) {
        var active = t.dataset.map === mapId;
        t.setAttribute('aria-selected', active ? 'true' : 'false');
      });
      panels.forEach(function (p) {
        if (p.id === 'panel-' + mapId) {
          p.removeAttribute('hidden');
        } else {
          p.setAttribute('hidden', '');
        }
      });
      /* Persiste seleção no hash para o botão voltar do browser */
      try { history.replaceState(null, '', '#' + mapId); } catch (e) {}
    }

    /* ── Eventos dos tabs ───────────────────────────────────── */
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        activateMap(this.dataset.map);
      });

      /* Navegação por teclado (← → Home End) */
      tab.addEventListener('keydown', function (e) {
        var all  = Array.from(tabs);
        var idx  = all.indexOf(this);
        var next = idx;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          next = (idx + 1) % all.length;
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          next = (idx - 1 + all.length) % all.length;
        } else if (e.key === 'Home') {
          next = 0;
        } else if (e.key === 'End') {
          next = all.length - 1;
        } else {
          return;
        }
        e.preventDefault();
        all[next].focus();
        activateMap(all[next].dataset.map);
      });
    });

    /* ── Botões de ampliação ────────────────────────────────── */
    document.querySelectorAll('.atlas-zoom-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var container = this.closest('.atlas-map-container');
        if (!container) return;
        var img = container.querySelector('.atlas-map');
        if (img && img.src) {
          window.open(img.src, '_blank', 'noopener');
        }
      });
    });

    /* ── Sidebar links para mapas ───────────────────────────── */
    document.querySelectorAll('[data-goto-map]').forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        var id = this.dataset.gotoMap;
        activateMap(id);
        var section = document.getElementById('atlas-mapas');
        if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });

    /* ── Restaurar do hash (link direto ou voltar) ──────────── */
    var hash = location.hash.replace('#', '');
    var valid = Array.from(tabs).some(function (t) { return t.dataset.map === hash; });
    activateMap(valid ? hash : (tabs[0] && tabs[0].dataset.map));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
