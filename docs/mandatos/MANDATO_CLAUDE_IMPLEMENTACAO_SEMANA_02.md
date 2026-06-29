# Mandato Claude - Implementacao da Semana 2 no site

## Objetivo

Implementar a **Semana 2** do Curso de Cultura Geral Moderna no site do projeto Homeschooling, usando os Markdown aprovados como fonte de verdade.

A Semana 2 deve entrar como continuidade natural da Semana 1, sem reconstruir a arquitetura do site e sem alterar sem necessidade os materiais ja aprovados.

## Fonte de verdade obrigatoria

Leia integralmente, antes de alterar codigo:

1. `CLAUDE.md`
2. `BRIEF_PARA_CLAUDE_SITE_LONGO_PRAZO.md`
3. `conteudo/Semana_02/SEMANA_02_CONTEUDO_SITE.md`
4. `conteudo/Semana_02/SEMANA_02_FICHA_IMPRIMIVEL.md`
5. `conteudo/Atlas/ATLAS_V1_CONTEUDO.md`, se o Atlas ja estiver integrado ou for chamado pela Semana 2

Os Markdown da Semana 2 sao fonte de verdade. Nao reescrever, resumir, corrigir ou completar a semantica do conteudo didatico dentro do HTML. Se houver problema de texto, reportar antes de modificar.

## Arquivos de conteudo a integrar

```text
conteudo/
  Semana_02/
    SEMANA_02_CONTEUDO_SITE.md
    SEMANA_02_FICHA_IMPRIMIVEL.md
```

Se o repositorio ainda estiver usando arquivos de Semana 1 na raiz, migrar ou referenciar de forma consistente, sem criar copias divergentes. A arquitetura desejada continua sendo por pastas semanais.

## Escopo autorizado

- Adicionar a Semana 2 a biblioteca/listagem de semanas.
- Criar a rota/pagina da Semana 2 conforme o padrao da Semana 1.
- Renderizar os blocos semanticos existentes no Markdown:
  - `:::conceito-chave`
  - `:::atlas`
  - `:::para-conversar`
  - `:::missao-enzo`
  - `:::desafio-felipe`
- Criar acesso claro a ficha imprimivel da Semana 2.
- Garantir que a ficha tenha visualizacao limpa e impressao adequada.
- Manter links entre home, biblioteca, Semana 1, Semana 2 e Atlas.
- Atualizar metadados, cards e estados de disponibilidade da biblioteca.

## Fora de escopo

- Publicar no GitHub Pages sem aprovacao explicita de Luca.
- Alterar conteudo pedagogico dos Markdown.
- Inventar novas semanas.
- Inserir videos ou links externos que nao estejam aprovados no Markdown.
- Criar rankings, notas, medalhas, pontos, barras de progresso escolar ou gamificacao falsa.
- Trocar a identidade visual inteira do site.
- Alterar a Semana 1 fora do minimo necessario para navegacao e consistencia estrutural.

## Direcao didatica da Semana 2

A Semana 2 deve parecer mais madura do que uma aula infantil de capitais. Felipe frequenta o **9º ano**; portanto a interface deve apoiar:

- leitura de mapas;
- raciocinio geografico;
- relacao entre geografia, economia e poder;
- matematica aplicada a orcamento publico;
- producao oral e escrita;
- frases praticas em ingles e italiano.

Evitar aparencia de jogo de memorizar bandeiras. Capitais aparecem como ferramenta para cultura geral, nao como fim unico.

## Requisitos visuais

- Card da Semana 2 na biblioteca com titulo: `Como ler o mundo no mapa`.
- Subtitulo/descricao curta: `Continentes, paises, capitais, rotas, poder e dinheiro publico`.
- A capa deve sugerir mapa, rotas, capitais ou leitura do mundo, sem caricatura infantil.
- Se usar asset SVG de capa, colocar em `assets/capas/` com nome estavel, por exemplo:

```text
assets/capas/semana-02-ler-o-mundo-no-mapa.svg
```

- Nao usar imagem decorativa generica de globo sem relacao com o conteudo.
- Garantir leitura confortavel no celular.

## Requisitos tecnicos

- Preservar Markdown como fonte de verdade.
- Nao duplicar a Semana 2 manualmente em HTML estatico se o site ja tiver renderizador Markdown.
- Se ainda houver lista manual de semanas, atualizar minimamente, mas registrar que a arquitetura futura deve ser orientada por metadados.
- Garantir URLs estaveis para Semana 2 e ficha.
- Garantir que caracteres acentuados aparecam corretamente em portugues, ingles e italiano.
- Verificar que tabelas extensas tenham scroll horizontal no celular, se necessario.
- Verificar que a impressao da ficha nao corte tabelas importantes.

## Verificacao obrigatoria

Antes de concluir, verificar concretamente:

1. A Semana 2 aparece na biblioteca.
2. O card da Semana 2 abre a pagina correta.
3. A pagina da Semana 2 renderiza titulo, metadados, capitulos, tabelas e blocos semanticos.
4. A ficha imprimivel da Semana 2 abre e imprime de forma legivel.
5. Links para Atlas funcionam ou ficam claramente sinalizados se o Atlas ainda nao estiver implementado.
6. Desktop e mobile foram verificados visualmente.
7. Nenhuma alteracao indevida foi feita na Semana 1.
8. `git diff --check` nao acusa problemas.

## Entrega esperada

No relatorio final, informar:

- arquivos criados e alterados;
- rota/URL local da Semana 2;
- rota/URL local da ficha imprimivel;
- como adicionar futuras semanas no mesmo padrao;
- resultado das verificacoes desktop/mobile/impressao;
- pendencias reais, se existirem.

Nao fazer commit nem push sem autorizacao explicita de Luca.
