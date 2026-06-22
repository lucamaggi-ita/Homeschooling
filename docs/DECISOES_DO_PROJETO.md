# Decisões do Projeto

Registro de decisões de design e arquitetura do site. Mantido por Claude; mudanças em CLAUDE.md requerem aprovação de Luca.

---

## 2026-06-22 — Estrutura inicial do site

**Decisão:** Criar `semanas/01/index.html` e `semanas/01/ficha.html` como primeiras páginas de lição, seguindo a estrutura sugerida no CLAUDE.md.

**Motivo:** O `index.html` (homepage) já existia. O passo lógico era criar a página da lição da Semana 1 a partir do Markdown aprovado.

---

## 2026-06-22 — Identidade visual aprovada — Brasil & Açaí

**Decisão:** Paleta oficial aprovada por Luca em 22/06/2026. Aplicada a todas as páginas do site.

| Token | Valor | Uso |
|---|---|---|
| `--br-verde` | `#009B3A` | Verde Brasil — Atlas, missões Enzo |
| `--br-amarelo` | `#FFDF00` | Amarelo Brasil — accent principal, chip Felipe |
| `--br-azul` | `#002776` | Azul Brasil — conceitos-chave |
| `--acai-dark` | `#2C0E20` | Sidebar, hero, fundo escuro |
| `--acai-medium` | `#3B132B` | Cards escuros, biblioteca |
| `--acai-light` | `#5C2445` | Desafios Felipe, açaí claro |
| `--sb-bg` | `#2C0E20` | Fundo da sidebar |
| `--page-bg` | `#FAF9F5` | Fundo das páginas de leitura |
| `--section-world` | `#EAF4EE` | Fundo da seção "Explore o mundo" |

**Regra de contraste:** Amarelo (#FFDF00) usado apenas em fundos escuros ou como detalhe grande. Evitar texto pequeno amarelo sobre fundo claro.

**Chips dos alunos:** Enzo → verde (#39D072 sobre açaí); Felipe → amarelo (#FFDF00 sobre açaí).

**Fontes:** Sora (interface/UI) + Lora (títulos editoriais). Inalteradas.

---

## 2026-06-22 — Componentes HTML para blocos semânticos

**Decisão:** Mapeamento adotado para os blocos `:::` do Markdown:

| Bloco Markdown     | Classe HTML           | Cor de acento       |
|--------------------|-----------------------|---------------------|
| `:::conceito-chave` | `.bloco.conceito-chave` | Violet `#8B6FE8`   |
| `:::para-conversar` | `.bloco.para-conversar` | Gold `#E8B84B`     |
| `:::atlas`          | `.bloco.atlas-ref`      | Teal `#3DC6B4`     |
| `:::missao-enzo`    | `.bloco.missao-enzo`    | Teal `#3DC6B4`     |
| `:::desafio-felipe` | `.bloco.desafio-felipe` | Violet `#8B6FE8`   |
| `:::video`          | `.bloco.video`          | Dark card + coral  |

---

## 2026-06-22 — Vídeos: domínio privacy-enhanced

**Decisão:** Vídeos do YouTube incorporados via `youtube-nocookie.com/embed/` (domínio privacy-enhanced) com `loading="lazy"` e `allowfullscreen`.

**Motivo:** Reduz rastreamento de terceiros sem impedir a incorporação.

---

## 2026-06-22 — Ficha imprimível

**Decisão:** A ficha (`semanas/01/ficha.html`) é uma página HTML separada com `@media print` dedicado. Imprime em A4 com `margin: 12mm`.

**Motivo:** Simplicidade de implementação; não depende de PDF gerado por servidor.
