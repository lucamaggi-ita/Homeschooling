#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gerar-mapas-atlas.py
Gera os 6 SVG do Atlas v1 a partir dos dados Natural Earth 110m (domínio público).

Uso:
    py tools/gerar-mapas-atlas.py

O script baixa ne_110m_admin_0_countries.geojson na primeira execução e
o armazena em cache em tools/. Os SVGs são salvos em assets/atlas/.

Atribuição obrigatória:
    Dados cartográficos: Natural Earth, domínio público.
    https://www.naturalearthdata.com
"""

import json, math, os, sys, urllib.request, urllib.error

# ── Caminhos ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT       = os.path.dirname(SCRIPT_DIR)
CACHE_FILE = os.path.join(SCRIPT_DIR, "ne_110m_countries.geojson")
OUT_DIR    = os.path.join(ROOT, "assets", "atlas")

NE_URL = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector"
    "/master/geojson/ne_110m_admin_0_countries.geojson"
)

# ── Nomes em português brasileiro ────────────────────────────────────────────
PT = {
    # Europa
    "Norway": "Noruega", "Sweden": "Suécia", "Finland": "Finlândia",
    "Denmark": "Dinamarca", "Iceland": "Islândia",
    "United Kingdom": "Reino Unido", "Russia": "Rússia",
    "Germany": "Alemanha", "France": "França", "Spain": "Espanha",
    "Portugal": "Portugal", "Italy": "Itália",
    "Netherlands": "Países Baixos", "Belgium": "Bélgica",
    "Switzerland": "Suíça", "Austria": "Áustria",
    "Poland": "Polônia", "Czechia": "Tchéquia", "Czech Republic": "Tchéquia",
    "Slovakia": "Eslováquia", "Hungary": "Hungria", "Romania": "Romênia",
    "Bulgaria": "Bulgária", "Greece": "Grécia", "Serbia": "Sérvia",
    "Croatia": "Croácia", "Bosnia and Herz.": "Bósnia e Herz.",
    "Bosnia and Herzegovina": "Bósnia e Herz.",
    "Albania": "Albânia", "N. Macedonia": "Macedônia do Norte",
    "North Macedonia": "Macedônia do Norte",
    "Montenegro": "Montenegro", "Kosovo": "Kosovo",
    "Estonia": "Estônia", "Latvia": "Letônia", "Lithuania": "Lituânia",
    "Belarus": "Bielorrússia", "Ukraine": "Ucrânia",
    "Moldova": "Moldova", "Ireland": "Irlanda", "Luxembourg": "Luxemburgo",
    "Slovenia": "Eslovênia", "Lithuania": "Lituânia",
    # África
    "Nigeria": "Nigéria", "Benin": "Benim", "Niger": "Níger",
    "Chad": "Chade", "Cameroon": "Camarões", "Ghana": "Gana",
    "Togo": "Togo", "Burkina Faso": "Burkina Faso", "Mali": "Mali",
    "Senegal": "Senegal", "Guinea": "Guiné", "Guinea-Bissau": "Guiné-Bissau",
    "Sierra Leone": "Serra Leoa", "Liberia": "Libéria",
    "Ivory Coast": "Costa do Marfim", "Côte d'Ivoire": "Costa do Marfim",
    "Mauritania": "Mauritânia", "Morocco": "Marrocos",
    "Algeria": "Argélia", "Tunisia": "Tunísia", "Libya": "Líbia",
    "Egypt": "Egito", "Sudan": "Sudão", "South Sudan": "Sudão do Sul",
    "S. Sudan": "Sudão do Sul", "Ethiopia": "Etiópia",
    "Eritrea": "Eritreia", "Somalia": "Somália",
    "Kenya": "Quênia", "Uganda": "Uganda", "Tanzania": "Tanzânia",
    "Rwanda": "Ruanda", "Burundi": "Burundi",
    "Dem. Rep. Congo": "R. D. Congo", "Congo": "Congo",
    "Central African Rep.": "R. Centro-Africana",
    "Gabon": "Gabão", "Eq. Guinea": "Guiné Equatorial",
    "Angola": "Angola", "Zambia": "Zâmbia", "Zimbabwe": "Zimbábue",
    "Mozambique": "Moçambique", "Malawi": "Malauí",
    "Madagascar": "Madagáscar", "Botswana": "Botsuana",
    "Namibia": "Namíbia", "South Africa": "África do Sul",
    "Lesotho": "Lesoto", "eSwatini": "Essuatíni",
    "Mauritius": "Maurício", "Comoros": "Comores",
    "Cape Verde": "Cabo Verde", "Djibouti": "Djibuti",
    # Ásia
    "South Korea": "Coreia do Sul", "North Korea": "Coreia do Norte",
    "China": "China", "Japan": "Japão", "Mongolia": "Mongólia",
    "Taiwan": "Taiwan", "Philippines": "Filipinas",
    "Vietnam": "Vietnã", "Thailand": "Tailândia",
    "Myanmar": "Mianmar", "Cambodia": "Camboja",
    "Laos": "Laos", "Malaysia": "Malásia",
    "Indonesia": "Indonésia", "India": "Índia",
    "Pakistan": "Paquistão", "Bangladesh": "Bangladesh",
    "Nepal": "Nepal", "Bhutan": "Butão", "Sri Lanka": "Sri Lanka",
    "Afghanistan": "Afeganistão", "Iran": "Irã", "Iraq": "Iraque",
    "Saudi Arabia": "Arábia Saudita", "Turkey": "Turquia",
    "Türkiye": "Turquia",
    "Kazakhstan": "Cazaquistão", "Uzbekistan": "Uzbequistão",
    "Kyrgyzstan": "Quirguistão", "Tajikistan": "Tadjiquistão",
    "Turkmenistan": "Turcomenistão",
    # América do Sul
    "Brazil": "Brasil", "Argentina": "Argentina",
    "Chile": "Chile", "Uruguay": "Uruguai", "Paraguay": "Paraguai",
    "Bolivia": "Bolívia", "Peru": "Peru", "Ecuador": "Equador",
    "Colombia": "Colômbia", "Venezuela": "Venezuela",
    "Guyana": "Guiana", "Suriname": "Suriname",
    "Fr. Guiana": "Guiana Francesa", "French Guiana": "Guiana Francesa",
    "Trinidad and Tobago": "Trinidad e Tobago",
    # América do Norte e Central
    "Mexico": "México", "Guatemala": "Guatemala",
    "Honduras": "Honduras", "Nicaragua": "Nicarágua",
    "Costa Rica": "Costa Rica", "Panama": "Panamá",
    "Cuba": "Cuba", "Haiti": "Haiti",
    "Dominican Rep.": "Rep. Dominicana",
    "United States of America": "Estados Unidos", "Canada": "Canadá",
    # Oceania
    "Australia": "Austrália", "New Zealand": "Nova Zelândia",
    "Papua New Guinea": "Papua Nova Guiné",
}

# ── Posições de rótulo ajustadas manualmente (lon, lat) ──────────────────────
LABEL_OVERRIDE = {
    "Noruega":          (10.0,  65.5),
    "Suécia":           (16.5,  62.5),
    "Finlândia":        (26.0,  64.5),
    "Dinamarca":        (10.0,  56.0),
    "Islândia":         (-18.5, 65.0),
    "Reino Unido":      (-2.5,  53.5),
    "Rússia":           (55.0,  62.0),
    "Nigéria":          (8.5,    9.5),
    "Benim":            (2.3,    9.5),
    "Níger":            (9.0,   17.0),
    "Chade":            (18.5,  15.5),
    "Camarões":         (12.5,   5.5),
    "Coreia do Sul":    (127.5,  36.0),
    "Coreia do Norte":  (126.5,  40.5),
    "China":            (104.0,  36.0),
    "Japão":            (138.0,  37.0),
    "Brasil":           (-52.0, -10.0),
    "Argentina":        (-65.0, -35.0),
    "Chile":            (-71.0, -35.0),
    "Uruguai":          (-56.0, -32.5),
    "Paraguai":         (-58.0, -23.0),
    "Bolívia":          (-64.0, -16.0),
    "Peru":             (-75.0, -10.0),
    "Equador":          (-78.0,  -1.5),
    "Colômbia":         (-74.0,   4.5),
    "Venezuela":        (-66.0,   8.0),
    "Guiana":           (-58.5,   5.0),
    "Suriname":         (-56.0,   4.0),
    "Guiana Francesa":  (-53.0,   3.5),
    "África do Sul":    (25.0,  -30.0),
    "Namíbia":          (18.0,  -22.0),
    "Botsuana":         (24.0,  -22.5),
    "Moçambique":       (35.5,  -18.0),
    "Tanzânia":         (35.0,   -6.5),
    "Quênia":           (38.0,    0.5),
    "Etiópia":          (40.0,    9.0),
    "Sudão":            (30.0,   15.0),
    "Egito":            (29.5,   27.0),
    "Líbia":            (17.0,   27.0),
    "Argélia":          (3.0,   28.0),
    "Mauritânia":       (-10.0,  20.0),
    "Mali":             (-2.0,   18.0),
    "Marrocos":         (-5.5,   32.0),
    "Alemanha":         (10.5,   51.0),
    "França":           (2.5,   46.5),
    "Espanha":          (-3.5,  40.0),
    "Polônia":          (19.5,  52.0),
    "Ucrânia":          (32.0,  49.0),
    "Turquia":          (35.5,  39.0),
    "Irã":              (53.0,  32.5),
    "Índia":            (79.0,  22.0),
    "Estados Unidos":   (-96.0, 38.0),
    "Canadá":           (-96.0, 57.0),
    "México":           (-102.0, 24.0),
    "Austrália":        (134.0, -27.0),
    "Cazaquistão":      (68.0,  48.0),
    "Mongólia":         (104.0, 46.5),
    "Indonésia":        (117.0,  -2.0),
}

# ── Rótulos de massas d'água (lon, lat, texto, cor-opcional) ──────────────────
WATER_LABELS = {
    "world": [
        (-30.0,  15.0, "Oceano Atlântico"),
        (-150.0,  0.0, "Oceano Pacífico"),
        ( 75.0, -30.0, "Oceano Índico"),
        (  0.0,  82.0, "Oceano Ártico"),
        (-60.0, -65.0, "Oceano Antártico"),
    ],
    "europa": [
        (-24.0,  57.0, "Atlântico Norte"),
        (  5.5,  65.0, "Mar da Noruega"),
        (  3.5,  56.5, "Mar do Norte"),
        ( 20.0,  40.0, "Mar Mediterrâneo"),
        ( 32.0,  44.5, "Mar Negro"),
    ],
    "africa": [
        (  3.0,  -2.0, "Golfo da Guiné"),
        (-17.0,  10.0, "Oceano Atlântico"),
        ( 45.0,  10.0, "Oceano Índico"),
    ],
    "asia": [
        (121.0,  32.5, "Mar Amarelo"),
        (137.0,  38.0, "Mar do Japão\n(Mar do Leste)"),
        (151.0,  46.0, "Oceano Pacífico"),
    ],
    "asia-s2": [
        ( 73.0,  -6.0, "Oceano Índico"),
        ( 88.0,  13.0, "Baía de Bengala"),
        (114.0,  12.0, "Mar do Sul da China"),
        (121.0,  32.5, "Mar Amarelo"),
        (137.0,  38.0, "Mar do Japão\n(Mar do Leste)"),
        (148.0,  48.0, "Oceano Pacífico"),
    ],
    "america-do-sul": [
        (-43.0, -16.0, "Oceano Atlântico"),
        (-82.0, -16.0, "Oceano Pacífico"),
    ],
}

# Rótulos geográficos não-aquáticos (penínsulas, etc.) – exibidos como texto itálico escuro
GEO_LABELS = {
    "asia": [
        (127.8, 38.8, "Pen. Coreana"),
    ],
    "asia-s2": [
        (127.8, 38.8, "Pen. Coreana"),
        ( 79.0, 13.5, "Subcontinente\nIndiano"),
    ],
}

# ── Cores ─────────────────────────────────────────────────────────────────────
OCEAN_BG    = "#B8CEDE"
LAND_FILL   = "#E4E0D4"
FOCUS_FILL  = "#C8DEC8"
BORDER      = "#B0A898"
LABEL_COL   = "#2A2228"
WATER_COL   = "#4A6880"
GEO_COL     = "#3A4A30"
ATTRIBUTION = "#909098"

# Semana 1 — casos de estudo
FOCUS_S1 = {"Brasil", "Noruega", "Coreia do Sul", "Nigéria"}

# Semana 2 — países-chave do mapa mundial
FOCUS_S2_WORLD = {
    "Brasil", "Estados Unidos", "China", "Rússia", "Índia",
    "Reino Unido", "França", "Alemanha", "Japão", "Austrália",
    "Egito", "África do Sul",
}

# Semana 2 — foco da Ásia ampliada
FOCUS_S2_ASIA = {"China", "Índia", "Japão", "Coreia do Sul", "Indonésia"}

FOCUS_NAMES = FOCUS_S1  # mantém compatibilidade com chamadas sem parâmetro

# ── Utilitários ───────────────────────────────────────────────────────────────
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def download_ne(url, cache_path):
    if os.path.exists(cache_path):
        print(f"  cache: {os.path.basename(cache_path)}")
    else:
        print(f"  baixando Natural Earth 110m...")
        try:
            urllib.request.urlretrieve(url, cache_path)
            print(f"  salvo em: {cache_path}")
        except urllib.error.URLError as e:
            print(f"ERRO: {e}", file=sys.stderr)
            sys.exit(1)
    with open(cache_path, encoding="utf-8") as f:
        return json.load(f)


# ── Projeção equiretangular ───────────────────────────────────────────────────
def make_proj(bbox, w, h, pad=24):
    min_lon, min_lat, max_lon, max_lat = bbox
    uw, uh = w - 2 * pad, h - 2 * pad

    def proj(lon, lat):
        x = pad + (lon - min_lon) / (max_lon - min_lon) * uw
        y = pad + (max_lat - lat) / (max_lat - min_lat) * uh
        return round(x, 1), round(y, 1)
    return proj


# ── Geometria ─────────────────────────────────────────────────────────────────
def split_antimeridian(ring):
    """Divide o anel onde há salto > 180° de longitude (antimeridiano)."""
    if not ring:
        return [ring]
    segs, cur = [], [ring[0]]
    for i in range(1, len(ring)):
        if abs(ring[i][0] - ring[i-1][0]) > 180:
            segs.append(cur)
            cur = []
        cur.append(ring[i])
    segs.append(cur)
    return [s for s in segs if len(s) >= 2]


def ring_to_d(ring, proj):
    parts = []
    for seg in split_antimeridian(ring):
        pts = [proj(p[0], p[1]) for p in seg]
        if pts:
            parts.append("M " + " L ".join(f"{x},{y}" for x, y in pts) + " Z")
    return " ".join(parts)


def geom_to_d(geom, proj):
    if not geom:
        return ""
    rings = []
    if geom["type"] == "Polygon":
        rings = geom["coordinates"]
    elif geom["type"] == "MultiPolygon":
        rings = [r for poly in geom["coordinates"] for r in poly]
    parts = [ring_to_d(r, proj) for r in rings]
    return " ".join(p for p in parts if p)


def largest_ring(geom):
    rings = []
    if geom["type"] == "Polygon":
        rings = geom["coordinates"]
    elif geom["type"] == "MultiPolygon":
        rings = [r for poly in geom["coordinates"] for r in poly]
    if not rings:
        return None

    def area(r):
        lons = [p[0] for p in r]; lats = [p[1] for p in r]
        return (max(lons) - min(lons)) * (max(lats) - min(lats))
    return max(rings, key=area)


def bbox_center(ring):
    lons = [p[0] for p in ring]; lats = [p[1] for p in ring]
    return (min(lons) + max(lons)) / 2, (min(lats) + max(lats)) / 2


def in_bbox(lon, lat, bbox, margin=3):
    return (bbox[0] - margin <= lon <= bbox[2] + margin and
            bbox[1] - margin <= lat <= bbox[3] + margin)


def feature_intersects(feat, bbox, margin=2):
    geom = feat.get("geometry")
    if not geom:
        return False
    rings = []
    if geom["type"] == "Polygon":
        rings = geom["coordinates"]
    elif geom["type"] == "MultiPolygon":
        rings = [r for poly in geom["coordinates"] for r in poly]
    for ring in rings:
        for lon, lat in ring:
            # Normaliza para o intervalo do bbox
            nlon = lon
            while nlon < bbox[0] - margin: nlon += 360
            while nlon > bbox[2] + margin: nlon -= 360
            if in_bbox(nlon, lat, bbox, margin):
                return True
    return False


# ── Texto SVG com sombra branca ───────────────────────────────────────────────
def text_shadow(x, y, label, size, weight, fill, anchor="middle", baseline="middle"):
    lines = label.split("\n")
    out = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else size * 1.2
        dy_attr = f' dy="{dy:.1f}"' if dy else ""
        x_attr = f' x="{x}"' if dy else ""
        anchor_attr = f'text-anchor="{anchor}"'
        baseline_attr = f'dominant-baseline="{baseline}"'
        common = (
            f'font-family="Helvetica,Arial,sans-serif" font-size="{size}" '
            f'font-weight="{weight}" {anchor_attr} {baseline_attr}'
        )
        if i == 0:
            out.append(
                f'<text x="{x}" y="{y}" {common} '
                f'fill="white" stroke="white" stroke-width="3" '
                f'stroke-linejoin="round" opacity="0.75">'
                f'{esc(line)}</text>'
            )
            out.append(
                f'<text x="{x}" y="{y}" {common} fill="{fill}">'
                f'{esc(line)}</text>'
            )
        else:
            out.append(
                f'<text x="{x}" y="{y + dy:.1f}" {common} '
                f'fill="white" stroke="white" stroke-width="3" '
                f'stroke-linejoin="round" opacity="0.75">'
                f'{esc(line)}</text>'
            )
            out.append(
                f'<text x="{x}" y="{y + dy:.1f}" {common} fill="{fill}">'
                f'{esc(line)}</text>'
            )
    return "\n".join(out)


# ── Geração do SVG ─────────────────────────────────────────────────────────────
def make_svg(features, bbox, w, h, show_labels=True,
             water_key=None, geo_key=None, show_salvador=False, pad=24,
             focus_names=None):

    if focus_names is None:
        focus_names = FOCUS_S1

    proj = make_proj(bbox, w, h, pad)
    min_lon, min_lat, max_lon, max_lat = bbox

    visible = [f for f in features if feature_intersects(f, bbox)]

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">',
        '<defs>',
        f'  <clipPath id="c">',
        f'    <rect x="{pad}" y="{pad}" width="{w-2*pad}" height="{h-2*pad}"/>',
        f'  </clipPath>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="{OCEAN_BG}"/>',
        f'<g clip-path="url(#c)">',
    ]

    # ── Polígonos dos países ──
    for feat in visible:
        props = feat.get("properties", {})
        geom  = feat.get("geometry")
        if not geom:
            continue
        name_en = (props.get("NAME") or props.get("ADMIN") or
                   props.get("NAME_EN") or "")
        name_pt = PT.get(name_en, name_en)
        fill = FOCUS_FILL if name_pt in focus_names else LAND_FILL
        d = geom_to_d(geom, proj)
        if d:
            out.append(
                f'<path d="{d}" fill="{fill}" stroke="{BORDER}" '
                f'stroke-width="0.5" stroke-linejoin="round"/>'
            )

    # ── Rótulos de água ──
    if show_labels and water_key:
        for lon, lat, text in WATER_LABELS.get(water_key, []):
            if not in_bbox(lon, lat, bbox, margin=5):
                continue
            x, y = proj(lon, lat)
            if x < pad - 20 or x > w - pad + 20: continue
            if y < pad - 20 or y > h - pad + 20: continue
            lines = text.split("\n")
            first_x, first_y = x, y
            for i, line in enumerate(lines):
                ey = first_y + i * 11
                out.append(
                    f'<text x="{first_x}" y="{ey}" text-anchor="middle" '
                    f'dominant-baseline="middle" '
                    f'font-family="Helvetica,Arial,sans-serif" font-size="9" '
                    f'fill="{WATER_COL}" font-style="italic" opacity="0.85">'
                    f'{esc(line)}</text>'
                )

    # ── Rótulos geográficos (não-aquáticos) ──
    if show_labels and geo_key:
        for lon, lat, text in GEO_LABELS.get(geo_key, []):
            if not in_bbox(lon, lat, bbox, margin=2):
                continue
            x, y = proj(lon, lat)
            out.append(text_shadow(x, y, text, 8, "normal", GEO_COL))

    # ── Rótulos dos países ──
    if show_labels:
        for feat in visible:
            props = feat.get("properties", {})
            geom  = feat.get("geometry")
            if not geom:
                continue
            name_en = (props.get("NAME") or props.get("ADMIN") or
                       props.get("NAME_EN") or "")
            name_pt = PT.get(name_en, name_en)
            if not name_pt:
                continue

            # Filtra países muito pequenos no mapa-múndi
            if water_key == "world":
                ring = largest_ring(geom)
                if ring:
                    lons = [p[0] for p in ring]
                    lats = [p[1] for p in ring]
                    a = (max(lons) - min(lons)) * (max(lats) - min(lats))
                    if a < 80 and name_pt not in focus_names:
                        continue

            # Posição do rótulo
            if name_pt in LABEL_OVERRIDE:
                llon, llat = LABEL_OVERRIDE[name_pt]
            else:
                ring = largest_ring(geom)
                if not ring:
                    continue
                llon, llat = bbox_center(ring)

            if not in_bbox(llon, llat, bbox, margin=1):
                continue

            x, y = proj(llon, llat)
            if x < pad - 5 or x > w - pad + 5: continue
            if y < pad - 5 or y > h - pad + 5: continue

            is_focus = name_pt in focus_names
            size   = 11 if is_focus else 9
            weight = "bold" if is_focus else "normal"
            out.append(text_shadow(x, y, name_pt, size, weight, LABEL_COL))

    # ── Marcador de Salvador (BA) ──
    if show_salvador:
        slon, slat = -38.5, -12.97
        if in_bbox(slon, slat, bbox):
            sx, sy = proj(slon, slat)
            out.append(
                f'<circle cx="{sx}" cy="{sy}" r="4.5" '
                f'fill="#E8604B" stroke="white" stroke-width="1.5"/>'
            )
            out.append(
                f'<text x="{sx+7}" y="{sy}" text-anchor="start" '
                f'dominant-baseline="middle" '
                f'font-family="Helvetica,Arial,sans-serif" font-size="9" '
                f'fill="{LABEL_COL}" font-weight="bold">'
                f'Salvador (BA)</text>'
            )

    out.append('</g>')

    # Borda do mapa
    out.append(
        f'<rect x="{pad}" y="{pad}" width="{w-2*pad}" height="{h-2*pad}" '
        f'fill="none" stroke="#90A4B8" stroke-width="1"/>'
    )

    # Atribuição
    out.append(
        f'<text x="{w - pad - 2}" y="{h - 5}" text-anchor="end" '
        f'font-family="Helvetica,Arial,sans-serif" font-size="7" '
        f'fill="{ATTRIBUTION}" opacity="0.85">'
        f'Natural Earth · domínio público</text>'
    )

    out.append('</svg>')
    return '\n'.join(out)


# ── Definição dos 6 mapas ────────────────────────────────────────────────────
MAPS = [
    # ── Base — mapas reutilizáveis em todas as semanas ───────────────────────
    dict(id="mapa-mundi-nomes",       subdir="base",
         bbox=(-180,-90,180,90),  w=960,h=500,
         show_labels=True,  water_key="world",
         focus_names=FOCUS_S1),
    dict(id="mapa-mundi-mudo",        subdir="base",
         bbox=(-180,-90,180,90),  w=960,h=500,
         show_labels=False, water_key=None,
         focus_names=FOCUS_S1),
    # ── Semana 1 — gravados em assets/atlas/semana-01/ ───────────────────────
    dict(id="europa-nomes",           subdir="semana-01",
         bbox=(-30,34,55,73),      w=800,h=580,
         show_labels=True,  water_key="europa",
         focus_names=FOCUS_S1),
    dict(id="africa-nomes",           subdir="semana-01",
         bbox=(-20,-37,55,38),     w=740,h=700,
         show_labels=True,  water_key="africa",
         focus_names=FOCUS_S1),
    dict(id="asia-nomes",             subdir="semana-01",
         bbox=(95,28,155,55),      w=800,h=560,
         show_labels=True,  water_key="asia",  geo_key="asia",
         focus_names=FOCUS_S1),
    dict(id="america-do-sul-nomes",   subdir="semana-01",
         bbox=(-85,-57,-30,14),    w=700,h=800,
         show_labels=True,  water_key="america-do-sul", show_salvador=True,
         focus_names=FOCUS_S1),
    # ── Semana 2 — gravados em assets/atlas/semana-02/ ───────────────────────
    dict(id="mapa-mundi-destaques", subdir="semana-02",
         bbox=(-180,-90,180,90), w=960,h=500,
         show_labels=True, water_key="world",
         focus_names=FOCUS_S2_WORLD),
    dict(id="mapa-asia-destaques", subdir="semana-02",
         bbox=(60,-13,155,58),   w=960,h=600,
         show_labels=True, water_key="asia-s2", geo_key="asia-s2",
         focus_names=FOCUS_S2_ASIA),
]


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("=== Atlas v1 — gerador de mapas ===")
    print(f"Saída: {OUT_DIR}\n")

    data     = download_ne(NE_URL, CACHE_FILE)
    features = data["features"]
    print(f"  {len(features)} features carregadas\n")

    for cfg in MAPS:
        mid    = cfg["id"]
        subdir = cfg.get("subdir", "")
        out_dir = os.path.join(OUT_DIR, subdir) if subdir else OUT_DIR
        os.makedirs(out_dir, exist_ok=True)
        svg = make_svg(
            features     = features,
            bbox         = cfg["bbox"],
            w            = cfg["w"],
            h            = cfg["h"],
            show_labels  = cfg.get("show_labels", True),
            water_key    = cfg.get("water_key"),
            geo_key      = cfg.get("geo_key"),
            show_salvador= cfg.get("show_salvador", False),
            focus_names  = cfg.get("focus_names"),
        )
        path = os.path.join(out_dir, f"{mid}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        rel  = (subdir + "/" if subdir else "") + f"{mid}.svg"
        size_kb = os.path.getsize(path) // 1024
        print(f"  OK {rel}  ({size_kb} KB)")

    print(f"\nConcluído. {len(MAPS)} SVGs em assets/atlas/  (2 base/ + 4 semana-01/ + 2 semana-02/)")
    print("Atribuição: Natural Earth, domínio público — https://www.naturalearthdata.com")


if __name__ == "__main__":
    main()
