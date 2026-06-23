# Atribuição cartográfica — Atlas v1

## Fonte

**Natural Earth**
- URL: https://www.naturalearthdata.com
- Repositório de dados vetoriais: https://github.com/nvkelso/natural-earth-vector
- Resolução usada: 110m (1:110 milhões), escala adequada para mapas escolares mundiais e regionais.
- Versão/commit: branch `master` do repositório, baixado em 2026-06-22.
- Licença: **domínio público** — sem restrições de uso, adaptação ou redistribuição.

## Como os mapas foram gerados

O script `tools/gerar-mapas-atlas.py` realiza as seguintes etapas:

1. Baixa `ne_110m_admin_0_countries.geojson` do repositório Natural Earth (apenas na primeira execução; o arquivo é armazenado em cache em `tools/`).
2. Projeta as coordenadas geográficas usando projeção **equiretangular** (lon → x, lat → y), recortada ao bounding box de cada mapa.
3. Converte os polígonos em caminhos SVG (`<path>`).
4. Aplica nomes em **português brasileiro** via mapeamento local explícito (`PT` no script).
5. Salva os 6 SVGs em `assets/atlas/`.

## Arquivos gerados

| Arquivo | Descrição |
|---|---|
| `mapa-mundi-nomes.svg` | Mapa-múndi com nomes em português |
| `mapa-mundi-mudo.svg` | Mapa-múndi sem nomes (exercício) |
| `europa-nomes.svg` | Europa com nomes — foco na Noruega |
| `africa-nomes.svg` | África com nomes — foco na Nigéria |
| `asia-nomes.svg` | Leste da Ásia com nomes — foco na Coreia do Sul |
| `america-do-sul-nomes.svg` | América do Sul com nomes — foco no Brasil, com marcador de Salvador (BA) |

## Rodapé exibido no site

> Dados cartográficos: Natural Earth, domínio público. Rótulos e atividades didáticas: Cultura Geral Moderna.

## Regenerar os mapas

```
py tools/gerar-mapas-atlas.py
```

O GeoJSON é mantido em cache local após o primeiro download. Para forçar um novo download, apague `tools/ne_110m_countries.geojson`.
