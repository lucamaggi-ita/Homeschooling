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

O `.lib-cover-inner` deve ter `overflow: hidden` para que transformações (ex.: `scale`) aplicadas à imagem sejam cortadas pelo wrapper — necessário para recortes locais de borda controlados por CSS.

**Cards disponíveis vs. em breve:**
- Semana disponível: `<a href="semanas/XX/index.html" class="lib-card" style="text-decoration:none;">` — link real, funcional.
- Semana futura / "em breve": `<div class="lib-card" style="opacity:0.35; pointer-events:none; cursor:default;" aria-hidden="true">` — não clicável.
- Não usar `<div>` para semana disponível; não usar `<a href="#">` como placeholder.

**Zoom local por imagem:** se uma capa tiver borda lateral baked no PNG, aplicar `transform: scale(X)` via classe específica do card (ex.: `.lib-card--semana-02 .lib-cover-image`), nunca globalmente em `.lib-cover-image` sem verificação visual de todos os cards. Classe de exceção deve ser adicionada ao elemento `<a class="lib-card ...">` correspondente.

**Regra definitiva:** A imagem de capa deve ser apenas ilustração do tema. Nunca deve conter título, chips, botão, painel vazio reservado para texto, nem margens brancas/claras externas — a ilustração deve preencher todo o canvas do arquivo. Se uma imagem gerada vier com margem externa ou painel vazio, ela deve ser normalizada (cropada) antes de entrar no repositório. `object-fit: cover` não elimina defeitos baked no próprio PNG.

**Nota Semana 2 (pendente):** O arquivo `assets/capas/semana-02-ler-mundo-mapa.png` apresentou duas versões com problema: (1) proporção 9:16 com painel escuro inferior (não removível via CSS quando wrapper é também 9:16); (2) versão recortada mas com margens brancas laterais baked no PNG (visíveis na miniatura da biblioteca). A versão normalizada sem margens deve ser fornecida pelo autor.

### Alinhamento da biblioteca

Para garantir que o status "Disponível" fique sempre na mesma linha horizontal em todos os cards da biblioteca (independentemente do número de linhas do título), os três elementos devem usar o seguinte padrão flex:

- `.lib-card`: `display: flex; flex-direction: column; height: 100%;`
- `.lib-body`: `display: flex; flex-direction: column; flex-grow: 1;`
- `.lib-status`: `margin-top: auto; padding-top: 8px;`

Este padrão foi aplicado em 2026-06-28 após constatar que Semana 1 (título de 3 linhas) e Semana 2 (título de 2 linhas) mostravam "Disponível" em alturas diferentes.

---

## 2026-06-29 — Páginas internas das semanas: sem hero image

**Decisão:** As páginas internas das lições (`semanas/XX/index.html`) não devem exibir imagem grande ou hero visual após o cabeçalho e antes do texto introdutório.

A imagem de capa pertence exclusivamente a:
- card grande da home (`.semana-cover-wrap`);
- miniatura da biblioteca (`.lib-cover`).

**Estrutura correta da página interna:**

1. `<header class="lesson-hero">` — breadcrumb, título, subtítulo, chips
2. `<article class="lesson-article">` — conteúdo textual introdutório
3. blocos didáticos / atividades

**O que não fazer:** inserir `<div class="lesson-cover">` ou qualquer `<img>` de capa entre o `</header>` e o `<article>`, salvo autorização explícita de Luca.

**Motivo:** Problema identificado na Semana 2, onde uma imagem grande aparecia entre o cabeçalho e o texto introdutório. A Semana 1 foi a referência correta: sem hero image na página interna. A capa é um ativo de navegação/card, não um hero interno da lição.

**CSS removido:** `.lesson-cover` e `.lesson-cover img` eram usados apenas por esse bloco e foram removidos de `assets/css/lesson.css` junto com a remoção do HTML correspondente em `semanas/02/index.html`.

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
