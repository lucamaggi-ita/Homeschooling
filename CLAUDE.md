# CLAUDE.md — Curso de Cultura Geral Moderna

Documento permanente de orientação do projeto. Deve ser lido no início de cada sessão de desenvolvimento.

---

## 1. Missão do projeto

Este é um curso HTML-first de cultura geral moderna desenvolvido para estudo em família.

**Alunos:** Enzo (11 anos) e Felipe (15 anos).

O curso funciona com **uma lição comum com níveis internos** — não são dois cursos separados. O mesmo tema é apresentado para os dois, com missões e desafios calibrados para cada idade dentro da mesma lição.

**Objetivo:** desenvolver compreensão do mundo real, pensamento crítico, curiosidade intelectual e capacidade de conectar geografia, história, economia, ciência, sociedade e atualidade.

---

## 2. Divisão de responsabilidades

| Papel | Responsabilidade |
|---|---|
| **Luca** | Aprova decisões relevantes, conteúdos e publicação. Autoridade final sobre qualquer mudança de substância. |
| **ChatGPT** | Autor e editor didático dos conteúdos em Markdown. Responsável pela consistência pedagógica, tom, estrutura das lições e fichas. |
| **Claude** | Responsável pelo site: arquitetura, HTML, CSS, componentes, navegação, responsividade, acessibilidade, conversão Markdown → HTML e integração de vídeo. |

**Regra crítica:** Claude não deve reescrever, resumir, simplificar, cortar ou alterar o sentido de conteúdos Markdown aprovados por Luca, sem autorização expressa.

---

## 3. Princípios didáticos

- Tom profissional, claro, narrativo e concreto. Não infantil.
- Profundidade sem linguagem acadêmica desnecessária.
- Não ideológico, sem preconceitos, sem explicações deterministas ou simplistas.
- O curso distingue explicitamente: **fatos**, **interpretações**, **hipóteses** e **perguntas em aberto**.
- Dados usados no site devem ter **fonte, ano e definição** quando relevantes.

---

## 4. Contrato dos conteúdos Markdown

Cada semana terá, em regra, dois arquivos entregues pelo ChatGPT e aprovados por Luca:

- `SEMANA_XX_CONTEUDO_SITE.md` — lição completa para o site
- `SEMANA_XX_FICHA_IMPRIMIVEL.md` — ficha curta para atividades presenciais

Quando aprovada, cada semana publicada também terá uma cover ilustrada em `assets/capas/`. A cover é um ativo visual do curso; ela não substitui o conteúdo Markdown e Claude não deve escolhê-la, substituí-la ou gerar uma alternativa sem autorização.

### Frontmatter obrigatório

Todo Markdown semanal deve ter frontmatter YAML. Os nomes, valores e tipos dos campos são dados editoriais definidos pelo autor; Claude deve preservá-los exatamente como recebidos, sem impor enumerações, converter formatos ou normalizá-los silenciosamente.

**Campos esperados em ambos os tipos de arquivo:** `semana`, `titulo`, `idade_alvo`, `formato`, `status`. O campo `tema` é opcional.

**Campos adicionais esperados em `SEMANA_XX_CONTEUDO_SITE.md`:** `subtitulo`, `atlas`, `ficha_imprimivel`.

**Campo adicional esperado em `SEMANA_XX_FICHA_IMPRIMIVEL.md`:** `paginas_alvo`.

Em particular:
- `ficha_imprimivel` pode ser booleano ou referência a arquivo — aceitar como fornecido.
- `paginas_alvo` pode ser intervalo textual ou número — aceitar como fornecido.
- `idade_alvo`, `formato`, `semana` e `status` devem ser aceitos exatamente como fornecidos pelo autor.

Se um campo esperado estiver ausente ou houver ambiguidade real, sinalizar e pedir instrução antes de qualquer alteração no conteúdo.

### Blocos semânticos

Claude deve reconhecer e transformar os seguintes blocos em componentes HTML consistentes, sem perder texto ou significado:

| Bloco Markdown | Componente no site |
|---|---|
| `:::conceito-chave` | Destaque visual de conceito central |
| `:::para-conversar` | Caixa de perguntas para discussão em família |
| `:::atlas` | Referência ao Atlas (link ou mapa integrado) |
| `:::missao-enzo` | Missão calibrada para 11 anos |
| `:::desafio-felipe` | Desafio calibrado para 15 anos |
| `:::video` | Bloco de vídeo incorporado com título, objetivo e perguntas pós-vídeo |

Tratamento de blocos não reconhecidos:
- **Em desenvolvimento:** sinalizar claramente no console com nome do arquivo e número da linha onde o bloco foi encontrado.
- **Na renderização:** preservar o texto do bloco de forma visível no HTML (ex.: elemento `<div>` com classe `bloco-desconhecido`). Nunca descartar o conteúdo silenciosamente.

---

## 5. Atlas, vídeos e ficha imprimível

### Atlas

- O Atlas é uma seção separada do site, não embutida nas lições.
- As lições **fazem referência** ao Atlas (link ou mapa contextual), mas não o duplicam.
- O conteúdo do Atlas é mantido independentemente das semanas.
- Um link, card ou placeholder não constitui um Atlas implementado. Para uma semana ser estudável, os mapas especificamente solicitados por ela devem estar disponíveis no Atlas.
- Para a Semana 1, o Atlas v1 deve permitir consultar ao menos mapa-múndi com nomes, mapa-múndi mudo e mapas com nomes de Europa, África, Ásia e América do Sul.

### Vídeos

- Vídeos devem ser incorporáveis (iframe ou player nativo do YouTube).
- Cada bloco `:::video` deve conter: título do vídeo, URL, objetivo pedagógico e pelo menos uma pergunta pós-vídeo.
- Claude não escolhe vídeos; apenas integra os vídeos definidos no Markdown aprovado.
- Os canais atualmente aprovados como fontes preferenciais são **BBC News Brasil** e **CNN Brasil / CNN Prime Time**. Eles não dispensam aprovação editorial por vídeo.
- Fluxo obrigatório: ChatGPT propõe vídeos separadamente; Luca aprova explicitamente; somente depois o URL e seus dados podem entrar em um Markdown semanal. Não inserir vídeos em rascunhos de lição como se já estivessem aprovados.

### Ficha imprimível

- A ficha é curta, focada em atividades para preencher.
- Não deve repetir textos longos da lição — apenas referências, perguntas e espaços de resposta.
- Deve ser renderizável como página para impressão (`@media print`) com CSS adequado.

### Fichas interativas

- Os arquivos Markdown continuam sendo a única fonte de verdade: a estrutura HTML interativa e seus campos devem derivar de marcadores ou blocos semânticos do Markdown, nunca de conversões manuais feitas semana a semana.
- Cada campo interativo deve usar elementos HTML reais e acessíveis (`form`, `label`, `input`, `textarea`, `input type="checkbox"` quando aplicável) e ter um `data-field-id` determinístico, legível e estável entre atualizações da mesma ficha. O identificador deve expressar a semana, o módulo e o nome semântico do campo; não usar contadores aleatórios ou dependentes da ordem de renderização.
- As respostas podem ser salvas somente no navegador, em chave `localStorage` estável e versionada por ficha, por exemplo `ficha:v1:semana-01`. Uma alteração incompatível exige uma nova versão da chave ou uma migração explícita; nunca pode apagar respostas silenciosamente. Esse armazenamento não é backup nem sincronização entre dispositivos.
- `Exportar respostas` deve baixar um JSON que contenha ao menos a versão, a semana e as respostas. `Limpar respostas` deve pedir confirmação antes de apagar os dados locais.
- A ação `Imprimir em branco` deve ocultar somente os valores preenchidos. Campos, rótulos, linhas e espaços de escrita permanecem visíveis na impressão; após imprimir, a tela deve restaurar imediatamente as respostas do aluno.
- A ficha deve funcionar em ambiente HTTP, incluindo GitHub Pages. O uso direto por `file://` não é um requisito suportado.

---

## 6. Experiência do site

O site é uma **ferramenta de estudo**, não uma página de marketing.

**Prioridades:**
- Leitura confortável em desktop e celular
- Navegação clara por semanas com progresso visível
- Acessibilidade (contraste, semântica HTML, navegação por teclado)
- Estabilidade visual — nada que pise no conteúdo ou quebre o layout entre semanas
- Identidade visual atual: paleta inspirada em açaí e nas cores do Brasil; sidebar e Biblioteca podem usar açaí escuro, enquanto áreas de estudo devem conservar superfícies claras e coloridas para leitura confortável.

**Vedações:**
- Visual infantil ou interface excessivamente decorativa
- Conteúdos essenciais escondidos atrás de interações desnecessárias (acordeões, tabs, modais) sem justificativa clara
- Animações que interfiram na leitura

---

## 7. Autonomia e limites de Claude

**Claude pode decidir autonomamente:**
- Detalhes técnicos de HTML, CSS, JavaScript
- Escolhas visuais compatíveis com estas regras (tipografia, espaçamento)
- Propor uma paleta coerente para apreciação de Luca — mas a identidade visual inicial só se torna padrão do curso após aprovação explícita; após aprovada, Claude pode aplicá-la autonomamente
- Refatorações de código que não alteram comportamento visível

**Claude deve pedir aprovação antes de:**
- Mudar estrutura didática ou currículo
- Alterar, resumir ou complementar conteúdo Markdown aprovado
- Escolher ou substituir fontes, vídeos ou imagens
- Renomear ou reorganizar semanas
- Qualquer decisão que altere a substância ou sequência do curso

**Antes de integrar uma semana**, Claude deve verificar:
- [ ] Frontmatter presente e completo
- [ ] Todos os blocos semânticos reconhecidos
- [ ] Links internos e externos funcionando
- [ ] Layout responsivo testado em viewport mobile e desktop
- [ ] Ficha imprimível renderiza corretamente

### Contrato visual das capas

Toda capa inserida no site deve respeitar o contrato registrado em `docs/DECISOES_DO_PROJETO.md` (seção 2026-06-28). Resumo obrigatório:

| Contexto | Wrapper | Proporção | CSS crítico |
|---|---|---|---|
| Card principal ("Nesta semana") | `.semana-cover-wrap` | `9 / 16` | `overflow:hidden; object-fit:cover; object-position:center` |
| Miniatura da biblioteca | `.lib-cover` | `3 / 4` | `overflow:hidden; object-fit:cover; object-position:center` |

**A capa é sempre tratada como conteúdo recortável.** A imagem nunca deve ser exibida em altura natural. Se a imagem contiver área escura/vazia interna destinada a texto, usar `object-position: top center` para excluí-la do recorte — ou devolver ao autor para correção do arquivo.

**Formato:** SVG para vetores simples; PNG para ilustrações ricas. Dimensão recomendada para PNG: 1080 × 1920 px (9:16). Nunca converter automaticamente.

**Antes de criar ou inserir uma nova capa semanal:** verificar o contrato em `docs/DECISOES_DO_PROJETO.md` (seção "Contrato visual — cards semanais e miniaturas"). A imagem deve ser apenas ilustração — número da semana, título, chips e botão pertencem ao HTML do card, nunca à imagem. Verificar também se o arquivo não contém margens brancas/claras externas nem painel vazio interno — `object-fit: cover` não elimina defeitos baked no PNG. Se a imagem vier com margem externa ou painel vazio, normalizar (cropar) antes de entrar no repositório. Se a proporção for idêntica ao wrapper (9:16), CSS não resolve — devolver ao autor para crop. O alinhamento de "Disponível" na biblioteca depende do padrão flex de `.lib-card`/`.lib-body`/`.lib-status`. Não gerar imagem-card completa.

### Páginas internas das semanas

Páginas internas das semanas (`semanas/XX/index.html`) não usam hero image inicial.
As capas ficam na home (`.semana-cover-wrap`) e na biblioteca (`.lib-cover`).
Na página da lição, depois do cabeçalho (`<header class="lesson-hero">`), entra diretamente o `<article>` com o conteúdo textual.
Não inserir `<div class="lesson-cover">` nem nenhum `<img>` de capa entre o `</header>` e o `<article>`, salvo autorização explícita de Luca.

### Cards das semanas

Toda semana publicada na home deve usar o mesmo componente reutilizável de card:

- capa já aprovada, sem imagens-placeholder ou geração automática;
- badge da semana;
- metadados curtos;
- título da semana;
- chips para recursos realmente disponíveis, como Atlas e Ficha;
- CTA em `<a>` para a lição real, nunca botão sem destino;
- comportamento responsivo e foco visível por teclado.

A estrutura HTML e as classes CSS são compartilhadas entre todas as semanas.
Não criar CSS ou markup específico por semana para esse componente.
Quando a informação existir no Markdown aprovado, título, metadados, recursos e destino da card devem derivar dele.

### Cabeçalhos de seção

Antes de criar uma nova seção visual, reutilizar o padrão `.section-header` + `.section-eyebrow` + `.section-title` (ver contrato em `docs/DECISOES_DO_PROJETO.md`). A label pequena usa 11px, uppercase, font-weight 700 e letter-spacing 0.14em. O título usa `.section-title`. Não criar títulos manuais fora do contrato visual.

### Critério de implementação de uma semana

Uma semana **não está implementada** quando existe apenas uma card, resumo ou link na home. Ela só está implementada quando:

- a página da lição renderiza integralmente todas as seções do Markdown aprovado;
- todos os blocos semânticos são visíveis e funcionais;
- os vídeos aprovados estão integrados com título, objetivo e perguntas;
- os links para Atlas e ficha funcionam;
- a ficha abre e imprime corretamente;
- desktop e celular foram verificados.

---

## 8. Memória e mudanças futuras

- Este `CLAUDE.md` deve permanecer **estável e conciso**.
- Novas decisões específicas (escolhas de paleta, plugins usados, convenções de slug, etc.) devem ser registradas em `docs/DECISOES_DO_PROJETO.md`, com data e motivo.
- Mudanças em `CLAUDE.md` requerem aprovação de Luca e devem ser registradas em `docs/DECISOES_DO_PROJETO.md`.
- Nunca alterar silenciosamente decisões anteriores sem registro explícito.

### Estrutura de pastas sugerida (não criar agora)

```
/
├── CLAUDE.md
├── index.html
├── docs/
│   └── DECISOES_DO_PROJETO.md
├── semanas/
│   ├── 01/
│   │   ├── index.html
│   │   └── ficha.html
│   └── ...
├── atlas/
│   └── index.html
├── assets/
│   ├── css/
│   ├── js/
│   ├── img/
│   └── capas/
│       ├── semana-01.webp
│       └── ...
└── conteudo/
    ├── Semana_01/
    │   ├── SEMANA_01_CONTEUDO_SITE.md
    │   └── SEMANA_01_FICHA_IMPRIMIVEL.md
    ├── Semana_02/
    │   ├── SEMANA_02_CONTEUDO_SITE.md
    │   └── SEMANA_02_FICHA_IMPRIMIVEL.md
    └── ...
```

A pasta `conteudo/` guarda os Markdown originais aprovados, como fonte de verdade. Os arquivos HTML em `semanas/` são gerados a partir deles.
