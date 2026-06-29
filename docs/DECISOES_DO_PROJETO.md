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

---

## 2026-06-23 — Card reutilizável como padrão da home

**Decisão:** A home passa a usar um componente `.semana-card` reutilizável como padrão para semanas publicadas. A primeira instância é a Semana 1.

**Valores iniciais aprovados (Semana 1):** capa de 280 px de altura, título em Lora 24 px, badge no topo esquerdo, chips de recursos, CTA amarelo em `<a>`. Estes valores são a implementação inicial compartilhada e podem ser ajustados globalmente no futuro alterando apenas as regras CSS das classes `.semana-*`.

**Regra permanente:** Nenhuma semana poderá criar variações locais de CSS ou markup para esse componente sem aprovação. A classe `disponivel` (sem acento) é o identificador de status aprovado no chip verde.

**Capa:** A área de capa (`.semana-cover-wrap`, 280 px) fica com fundo escuro (`#110E15`) até que uma capa ilustrada seja aprovada por Luca. Quando entregue, inserir `<img src="assets/capas/semana-XX.webp" alt="...">` dentro do wrapper, sem nenhum outro elemento. Não usar placeholders de arte — área vazia é o estado correto enquanto a capa não existe. A pasta `assets/capas/` deve ser criada somente na primeira entrega.

**Motivo:** Padronizar a estrutura visual e semântica de todas as cards de semanas, evitar CSS duplicado por semana e garantir que futura geração automática (Markdown → HTML) encontre um contrato estável.

---

## 2026-06-22 — Atlas v1 — dados cartográficos e arquitetura

**Decisão:** Os 6 SVGs do Atlas são gerados por `tools/gerar-mapas-atlas.py` a partir dos dados **Natural Earth 110m** (domínio público). Os arquivos SVG são armazenados em `assets/atlas/` e carregados via `<img>` no HTML. A página do Atlas está em `atlas/index.html`.

**Projeção:** Equiretangular (lon → x, lat → y) com bounding box por mapa e recorte via `<clipPath>` SVG.

**Rótulos:** Nomes em português brasileiro via mapeamento explícito no script (`PT` dict). Posições ajustadas manualmente para os países principais (`LABEL_OVERRIDE`).

**Atribuição exibida:** `Dados cartográficos: Natural Earth, domínio público. Rótulos e atividades didáticas: Cultura Geral Moderna.`

**Fonte completa:** `tools/ATRIBUICAO.md`

**Motivo:** Garante que os mapas funcionem completamente offline (GitHub Pages) sem dependência de APIs, tiles ou recursos remotos em tempo de execução. O download do Natural Earth é apenas build-time.

---

## 2026-06-28 — Contrato visual — capas e miniaturas das semanas

**Decisão:** Formalizar proporções e regras de recorte para todos os arquivos de capa.

### Capa grande / card principal da semana atual

```
Wrapper: .semana-cover-wrap
Proporção obrigatória: 9 / 16
Largura desktop: 300px → altura derivada ≈ 533 px
Largura mobile máxima: 360px → altura derivada ≈ 640 px
CSS crítico: overflow: hidden; object-fit: cover; object-position: center
```

A imagem nunca deve ser exibida em altura natural. Sempre preenche o wrapper via `object-fit: cover`.

### Miniatura da biblioteca

```
Wrapper: .lib-cover  (dentro de .lib-card)
Proporção obrigatória: 3 / 4
Largura visual: 132 px → altura derivada ≈ 176 px
CSS crítico: overflow: hidden; object-fit: cover; object-position: center
Mobile: duas colunas de 132 px
```

### Formato preferencial dos arquivos de capa

| Situação | Formato |
|---|---|
| Ilustração vetorial simples, mapa, ícone | SVG |
| Ilustração rica com gradientes, sombras, textura | PNG |

Não converter automaticamente PNG para SVG.

**Dimensão recomendada para PNG:** 1080 × 1920 px (proporção 9:16). Mínimo aceitável: 720 × 1280 px.

### Regra crítica: a capa é ilustração, não card completo

O card HTML já contém badge, título, chips e botão. A imagem de capa **não deve incluir área escura vazia** reservada para texto. Caso a imagem contenha faixa vazia inferior, usar `object-position: top center` para recortar.

**Motivo:** Problema visual identificado na Semana 2 (PNG com painel interno escuro que aparecia antes do painel HTML do card). A regra garante que futuras capas sejam produzidas como ilustrações recortáveis, não como cards completos.

---

## Contrato visual — cards semanais e miniaturas

### Estrutura obrigatória do card grande

O card grande da semana **não é uma imagem única**. É sempre composto por duas partes:

1. `.semana-cover-wrap` — área da ilustração
2. `.semana-card-body` — área textual inferior

A imagem da capa fica **apenas** dentro de `.semana-cover-wrap`. Badge, título, chips e botão são sempre HTML no `.semana-card-body`. Nunca embutir esses elementos na imagem.

### `.semana-cover-wrap`

| Propriedade | Valor |
|---|---|
| `position` | `relative` |
| `width` | `100%` |
| `aspect-ratio` | `9 / 16` |
| `background` | `#110E15` |
| `overflow` | `hidden` |

Imagem interna: `width: 100%; height: 100%; object-fit: cover; object-position: center; display: block`.

Se a imagem contiver painel escuro vazio na parte inferior **e** a proporção da imagem for diferente de 9:16, usar `object-position: top center` para excluir o painel do recorte. Se a proporção for idêntica ao wrapper (9:16), `object-position` não produz recorte — o arquivo deve ser cropado pelo autor.

### `.badge-semana-top`

HTML sobreposto via `position: absolute; top: 16px; left: 16px`. Fundo escuro translúcido com `backdrop-filter: blur(4px)`. Texto `#FFDF00`, fonte Sora, peso 800, uppercase, `letter-spacing: 0.06em`.

### `.semana-card-body`

`padding: 28px 24px 24px; display: flex; flex-direction: column; flex-grow: 1; gap: 16px`.

Conteúdo obrigatório em ordem:

| Elemento | Classe | Especificação |
|---|---|---|
| Meta superior | `.semana-meta-top` | Sora 12px 700, `#FFDF00`, uppercase, `letter-spacing: 0.08em` |
| Título | `.semana-card-title` | Lora 24px 600, `#FFFFFF`, `line-height: 1.35` |
| Grupo de chips | `.semana-chips-group` | flex-wrap, gap 8px |
| Botão CTA | `.semana-btn-action` | `<a>` amarelo `#FFDF00`, `margin-top: auto`, `border-radius: 10px`, `padding: 14px 20px` |

Chip padrão: fundo translúcido, Sora 11px 700, uppercase. Chip `disponivel`: fundo `rgba(0,155,58,0.2)`, texto `#4AF287`, borda `rgba(0,155,58,0.3)`.

### Miniaturas da biblioteca

Wrapper `.lib-cover` com `aspect-ratio: 3 / 4` dentro de `.lib-card`. Imagem com classe `.lib-cover-image`: `object-fit: cover; object-position: center`. O `.lib-body` contém número da semana, título e status em HTML — nunca embutidos na imagem.

**Regra definitiva:** A imagem de capa deve ser apenas ilustração do tema. Nunca deve conter título, chips, botão ou painel vazio reservado para texto.

**Nota Semana 2 (pendente):** O arquivo `assets/capas/semana-02-ler-mundo-mapa.png` tem proporção 9:16 igual ao wrapper, portanto o painel escuro inferior não pode ser removido por CSS. O arquivo precisa ser cropado pelo autor para eliminar o painel vazio.

---

## Contrato visual — cabeçalhos de seção

Toda seção principal do site deve usar o padrão `.section-header`:

```html
<div class="section-header">
  <div class="section-eyebrow" style="color: COR_TEMATICA">
    LABEL DA SEÇÃO
  </div>
  <h2 class="section-title" id="id-da-secao">
    Título da seção
  </h2>
</div>
```

### `.section-header`

`margin-bottom: 28px`. Contêiner da label pequena + título principal. Deve aparecer antes do conteúdo principal da seção. Não substituir por títulos soltos fora do padrão.

### `.section-eyebrow`

`font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; margin-bottom: 6px`. Texto curto de orientação visual (categoria ou contexto da seção).

Cores temáticas aprovadas (aplicadas via `style="color: ..."` diretamente no HTML — não refatorar para classes sem autorização explícita):

| Seção | Cor |
|---|---|
| Semana atual ("Nesta semana") | `#B87820` |
| Explore o mundo | `#187868` |
| Biblioteca de semanas | `var(--accent-violet)` |

### `.section-title`

`font-size: 22px; font-weight: 800; line-height: 1.2; color: inherit`. Na seção biblioteca: `color: var(--text-primary)` via regra `.section-library .section-title`.

**Regra:** Não criar títulos de seção fora deste padrão sem autorização.
