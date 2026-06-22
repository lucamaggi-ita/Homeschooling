/* ficha-engine.js — Motor interativo das fichas do Cultura Geral Moderna
   Responsabilidades:
   - Carrega respostas salvas (localStorage) ao abrir a ficha
   - Salva automaticamente com debounce de 500 ms
   - Exibe indicador visual "Salvo neste navegador"
   - Exportar respostas (JSON), Limpar respostas, Imprimir (com/sem respostas)
   - Auto-redimensiona textareas mantendo alinhamento das linhas de caderno */

(function () {
  'use strict';

  var STORAGE_KEY;
  var debounceTimer;

  /* ── Helpers ─────────────────────────────────────── */

  function getStorageKey() {
    return (document.body.dataset && document.body.dataset.fichaKey)
      ? document.body.dataset.fichaKey
      : 'ficha:v1:unknown';
  }

  function getFields() {
    return Array.prototype.slice.call(
      document.querySelectorAll('[data-field-id]')
    );
  }

  /* Expande textarea para exibir todo o conteúdo.
     scrollHeight é sempre múltiplo de line-height (28px) porque o
     background-gradient está alinhado a esse valor, portanto as
     linhas de caderno permanecem alinhadas ao expandir. */
  function autoResize(ta) {
    ta.style.height = 'auto';
    ta.style.height = ta.scrollHeight + 'px';
  }

  /* ── Persistência ────────────────────────────────── */

  function loadAnswers() {
    var raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return;
    var data;
    try { data = JSON.parse(raw); } catch (e) { return; }
    getFields().forEach(function (field) {
      var id = field.dataset.fieldId;
      if (data[id] === undefined) return;
      if (field.type === 'checkbox') {
        field.checked = !!data[id];
      } else {
        field.value = data[id];
        if (field.tagName === 'TEXTAREA') autoResize(field);
      }
    });
  }

  function collectAnswers() {
    var data = {};
    getFields().forEach(function (field) {
      var id = field.dataset.fieldId;
      data[id] = (field.type === 'checkbox') ? field.checked : field.value;
    });
    return data;
  }

  function saveAnswers() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(collectAnswers()));
      showSaveIndicator();
    } catch (e) {
      /* localStorage indisponível (modo privado restrito) — ignorar silenciosamente */
    }
  }

  /* ── Indicador visual ────────────────────────────── */

  function showSaveIndicator() {
    var el = document.getElementById('ficha-save-status');
    if (!el) return;
    el.classList.add('visible');
    clearTimeout(el._hideTimer);
    el._hideTimer = setTimeout(function () {
      el.classList.remove('visible');
    }, 2000);
  }

  /* ── Ações dos botões ────────────────────────────── */

  function exportAnswers() {
    var data = collectAnswers();
    var json = JSON.stringify(data, null, 2);
    var blob = new Blob([json], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = STORAGE_KEY.replace(/:/g, '-') + '.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  }

  function clearAnswers() {
    if (!window.confirm('Apagar todas as respostas desta ficha neste navegador?')) return;
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
    getFields().forEach(function (field) {
      if (field.type === 'checkbox') {
        field.checked = false;
      } else {
        field.value = '';
        if (field.tagName === 'TEXTAREA') autoResize(field);
      }
    });
    showSaveIndicator();
  }

  function printWithAnswers() {
    window.print();
  }

  /* Adiciona .print-blank antes de imprimir e remove logo após.
     Usa o evento afterprint como caminho principal e um setTimeout
     como fallback para navegadores que não disparam afterprint. */
  function printBlank() {
    var restored = false;

    function restore() {
      if (restored) return;
      restored = true;
      document.body.classList.remove('print-blank');
    }

    window.addEventListener('afterprint', function handler() {
      restore();
      window.removeEventListener('afterprint', handler);
    });

    document.body.classList.add('print-blank');
    window.print();
    setTimeout(restore, 1500);
  }

  /* ── Listeners de campo ──────────────────────────── */

  function onInput(e) {
    var field = e.target;
    if (field.tagName === 'TEXTAREA') autoResize(field);
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(saveAnswers, 500);
  }

  function onChange() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(saveAnswers, 500);
  }

  /* ── Inicialização ───────────────────────────────── */

  function init() {
    STORAGE_KEY = getStorageKey();
    loadAnswers();

    getFields().forEach(function (field) {
      field.addEventListener('input', onInput);
      field.addEventListener('change', onChange);
    });

    document.querySelectorAll('[data-action]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var action = btn.dataset.action;
        if      (action === 'print')       printWithAnswers();
        else if (action === 'print-blank') printBlank();
        else if (action === 'export')      exportAnswers();
        else if (action === 'clear')       clearAnswers();
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
