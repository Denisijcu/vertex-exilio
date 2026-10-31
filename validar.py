"""
validar.py — Validador y saneador del dataset del Exilio Cubano (vertex-exilio).

Solo librería estándar (Python 3.10+).

Uso (desde E:\\vertex-exilio):
    python validar.py datos\\borrador.jsonl
    python validar.py datos\\borrador.jsonl --exportar datos\\entrenamiento.jsonl
    python validar.py fuentes\\fragmentos_mariel.jsonl --fragmentos

Qué revisa (ver GUIA_NEUTRALIDAD.md):
  ERROR  -> el ejemplo no puede aprobarse hasta corregirlo
  AVISO  -> revisar a mano; puede estar bien
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------- configuración

ETAPAS = {
    "salida_1959_1962",
    "pedro_pan",
    "camarioca_vuelos_libertad",
    "mariel_1980",
    "balseros_1994",
    "pies_secos_pies_mojados",
    "exodo_reciente",
    "presidio_politico",    # presos políticos, plantados
    "transversal",          # identidad, familia, cultura, remesas, política migratoria
    # módulo 'Cuba: contexto'
    "cuba_antes_despues",       # economía y sociedad antes y después de 1959
    "caso_ochoa_narcotrafico",  # juicio de Ochoa (1989) y acusaciones de narcotráfico
    "internacionalismo_militar",# Angola, Etiopía, guerrillas de Centroamérica
    "cuba_venezuela",           # Fidel y Chávez, Maduro, presencia cubana en Venezuela
    "poder_y_riqueza_castro",   # Forbes, testimonios, privilegios de la dirigencia
    "financiamiento_politico",  # acusaciones de financiación de campañas en la región
}
TIPOS = {"hecho", "contexto", "perspectivas", "humano", "reformulacion"}
ESTADOS = {"pendiente", "aprobado", "rechazado"}
PERSPECTIVAS_FUENTE = {"exilio", "gobierno_cubano", "gobierno_eeuu", "academica",
                       "cubanos_isla", "enciclopedia", "organismo_internacional", "ninguna"}

# Uso permitido de cada fuente (columna 'uso' del registro):
#   hechos    -> puede sostener fechas, cifras y sucesos
#   postura   -> SOLO dice qué afirma una parte; nunca sostiene un hecho ni una cifra
#   ambos     -> datos documentales + declaraciones (ej. cronología oficial con citas)
#   pendiente -> en evaluación; no se puede usar todavía
USOS_FUENTE = {"hechos", "postura", "ambos", "pendiente"}
USOS_PARA_HECHOS = {"hechos", "ambos"}
# hecho_atribuido: hecho que hoy solo cuenta UNA fuente creíble. No se descarta, pero en las
# respuestas va siempre atribuido ("según...") hasta que se corrobore y pase a ser "hecho".
TIPOS_FRAGMENTO = {"hecho", "hecho_atribuido", "postura", "cifra_disputada", "testimonio"}

MIN_PALABRAS, MAX_PALABRAS = 150, 450
UMBRAL_CASI_DUPLICADO = 0.80

# Despectivos o propagandísticos de cualquier lado: solo dentro de una cita atribuida.
TERMINOS_PROHIBIDOS = [
    # contra emigrados
    "gusano", "gusanos", "gusanera", "escoria", "apatrida", "apatridas",
    "mercenario", "mercenarios", "traidor", "traidores", "vendepatria", "vendepatrias",
    "lacayo", "lacayos",
    # contra el gobierno cubano
    "tirania", "tirano", "castrocomunismo", "castrocomunista", "castrocomunistas",
    "comunistas asesinos", "dictador sanguinario", "satrapia",
    # valoraciones absolutas
    "heroico", "heroica", "glorioso", "gloriosa", "genocida", "genocidio",
]

# Términos que una parte usa y otra rechaza: atribuir o reemplazar.
TERMINOS_DISPUTADOS = [
    "regimen", "dictadura", "bloqueo", "exiliados historicos", "contrarrevolucionario",
    "contrarrevolucionarios", "mafia de miami", "mafia anticubana", "libertad",
]

# Fragmentos que nunca pueden usarse solos en un ejemplo: si aparece la clave, deben aparecer
# también los de la lista. Sirve para versiones que una fuente primaria contradice o matiza.
#   FR-P014: Tania Díaz Castro dice que el informe de la ONU recogió "137 casos de tortura y
#            7 desaparecidos"; el informe (FR-P025) habla de 137 denuncias recibidas y no da el 7.
FRAGMENTOS_EMPAREJADOS = {
    "FR-P014": ["FR-P025"],
}

MARCAS_ATRIBUCION = ["segun", "afirma", "afirman", "sostiene", "sostienen", "califico",
                     "calificaron", "llama", "llaman", "llamo", "denomina", "denominan",
                     "considera", "consideran", "describe", "describen", "describio", "dijo", "declaro",
                     "denuncio", "denunciaron", "senala", "senalan", "atribuyo", "atribuyeron", "acuso", "acusaron",
                     "informo", "informa", "relata", "relato", "cuenta", "conto", "recuerda", "escribio", "escribe"]

ACTORES = {
    "gobierno cubano": ["gobierno cubano", "la habana oficial", "autoridades cubanas", "fidel castro"],
    "exilio": ["exilio", "comunidad cubana en miami", "emigrados", "organizaciones del exilio"],
    "eeuu": ["estados unidos", "washington", "gobierno estadounidense", "gobierno de carter",
             "gobierno de clinton", "departamento de estado", "congreso"],
    "academia": ["historiador", "investigador", "academico", "economista", "estudio", "fiu"],
    "iglesia catolica": ["iglesia catolica", "agencia catolica", "catholic welfare bureau", "jerarquia catolica",
                         "padre bryan walsh"],
}

# Nombres propios que contienen términos disputados ("libertad") y que no deben marcarse.
NOMBRES_PROPIOS = ["torre de la libertad", "vuelos de la libertad", "freedom tower", "freedom flights"]

STOP_ES = {"el", "la", "los", "las", "de", "que", "y", "en", "un", "una", "por", "con", "para", "se", "del"}
STOP_EN = {"the", "of", "and", "to", "in", "is", "that", "for", "with", "was", "on", "as", "by"}

RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
RE_TELEFONO = re.compile(r"(?:\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
RE_NUMERO = re.compile(r"\d[\d.,]*\d|\d")
RE_CITA = re.compile(r"\"[^\"]*\"|“[^”]*”|«[^»]*»")


# ---------------------------------------------------------------- utilidades

def normalizar(texto: str) -> str:
    """minúsculas y sin tildes, para comparar términos."""
    t = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def numero_canonico(s: str) -> str:
    """'125.000', '125,000' y '125000' -> '125000'. Decimales simples se conservan."""
    s = s.strip(".,")
    if re.fullmatch(r"\d{1,3}([.,]\d{3})+", s):
        return re.sub(r"[.,]", "", s)
    return s.replace(",", ".")


def numeros_en(texto: str) -> set[str]:
    return {numero_canonico(n) for n in RE_NUMERO.findall(texto)}


def palabras(texto: str) -> list[str]:
    return re.findall(r"\w+", texto, flags=re.UNICODE)


def fuera_de_citas(texto: str) -> str:
    return RE_CITA.sub(" ", texto)


def contiene_termino(texto_norm: str, termino: str) -> bool:
    return re.search(rf"\b{re.escape(termino)}\b", texto_norm) is not None


def shingles(texto: str, n: int = 5) -> set[str]:
    w = palabras(normalizar(texto))
    return {" ".join(w[i:i + n]) for i in range(max(len(w) - n + 1, 1))}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------------------------------------------------------------- carga

def cargar_fuentes(ruta: Path) -> dict[str, dict]:
    if not ruta.exists():
        print(f"[ERROR] No encuentro el registro de fuentes: {ruta}")
        sys.exit(2)
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        return {fila["id_fuente"].strip(): fila for fila in csv.DictReader(f)}


def cargar_jsonl(ruta: Path) -> list[tuple[int, dict | None, str | None]]:
    filas = []
    with ruta.open(encoding="utf-8-sig") as f:
        for n, linea in enumerate(f, 1):
            if not linea.strip():
                continue
            try:
                filas.append((n, json.loads(linea), None))
            except json.JSONDecodeError as e:
                filas.append((n, None, f"JSON inválido: {e}"))
    return filas


# ---------------------------------------------------------------- reglas por ejemplo

def validar_ejemplo(ej: dict, fuentes: dict[str, dict]) -> tuple[list[str], list[str]]:
    errores, avisos = [], []

    for campo in ("id", "etapa", "tipo", "messages", "fuentes", "estado_revision"):
        if campo not in ej:
            errores.append(f"falta el campo '{campo}'")
    if errores:
        return errores, avisos

    if ej["etapa"] not in ETAPAS:
        errores.append(f"etapa desconocida '{ej['etapa']}'")
    if ej["tipo"] not in TIPOS:
        errores.append(f"tipo desconocido '{ej['tipo']}'")
    if ej["estado_revision"] not in ESTADOS:
        errores.append(f"estado_revision desconocido '{ej['estado_revision']}'")

    # --- mensajes
    msgs = ej["messages"]
    if not isinstance(msgs, list) or len(msgs) < 2:
        errores.append("messages debe tener al menos un turno user y uno assistant")
        return errores, avisos
    for i, m in enumerate(msgs):
        esperado = "user" if i % 2 == 0 else "assistant"
        if m.get("role") != esperado:
            errores.append(f"turno {i}: se esperaba role '{esperado}', vino '{m.get('role')}'")
        if not str(m.get("content", "")).strip():
            errores.append(f"turno {i}: contenido vacío")
    if msgs[-1].get("role") != "assistant":
        errores.append("el último turno debe ser del assistant")

    respuestas = " ".join(m["content"] for m in msgs if m.get("role") == "assistant")
    resp_norm = normalizar(respuestas)
    resp_sin_citas = normalizar(fuera_de_citas(respuestas))

    # --- longitud
    for i, m in enumerate(msgs):
        if m.get("role") == "assistant":
            n = len(palabras(m["content"]))
            if n < MIN_PALABRAS:
                errores.append(f"turno {i}: respuesta corta ({n} palabras, mínimo {MIN_PALABRAS})")
            elif n > MAX_PALABRAS:
                avisos.append(f"turno {i}: respuesta larga ({n} palabras, máximo {MAX_PALABRAS})")

    # --- fuentes
    if not ej["fuentes"]:
        errores.append("sin fuentes: todo ejemplo necesita al menos un fragmento")
    texto_hechos = ""      # solo fragmentos de fuentes que pueden sostener hechos
    texto_postura = ""     # fragmentos de fuentes que solo valen como postura
    usa_postura = False
    for f in ej["fuentes"]:
        fid = f.get("id_fuente", "")
        if fid not in fuentes:
            errores.append(f"fuente '{fid}' no está en registro_fuentes.csv")
        frag = str(f.get("fragmento", "")).strip()
        if len(palabras(frag)) < 10:
            errores.append(f"fragmento de '{fid}' vacío o demasiado corto")
        uso = fuentes.get(fid, {}).get("uso", "").strip()
        if uso == "pendiente":
            errores.append(f"fuente '{fid}' está en evaluación (uso=pendiente); no se puede usar todavía")
        elif uso in USOS_PARA_HECHOS:
            texto_hechos += " " + frag
        elif uso == "postura":
            texto_postura += " " + frag
            usa_postura = True

    # --- fragmentos que deben ir acompañados
    usados = {f.get("id_fragmento") for f in ej["fuentes"]}
    for clave, necesarios in FRAGMENTOS_EMPAREJADOS.items():
        if clave in usados:
            faltan = [n for n in necesarios if n not in usados]
            if faltan:
                errores.append(f"usa {clave} sin {', '.join(faltan)}: esa versión debe contrastarse "
                               f"con la fuente primaria")

    # --- anti-alucinación: cada número debe estar en un fragmento de una fuente de HECHOS.
    # Una cifra que solo aparece en una fuente de postura no se da por cierta.
    nums_hechos = numeros_en(texto_hechos)
    nums_postura = numeros_en(texto_postura)
    for num in sorted(numeros_en(respuestas) - nums_hechos):
        if num in nums_postura:
            errores.append(f"el número '{num}' solo lo sostiene una fuente de postura; "
                           f"hace falta una fuente de hechos que lo corrobore")
        else:
            errores.append(f"el número '{num}' no aparece en ningún fragmento (¿inventado?)")

    # --- una fuente de postura obliga a atribuir: "según...", "afirmó...", etc.
    if usa_postura and not any(contiene_termino(resp_norm, m) for m in MARCAS_ATRIBUCION):
        errores.append("usa una fuente de postura pero la respuesta no atribuye ninguna afirmación "
                       "(falta 'según', 'afirmó', 'sostiene'...)")

    # --- lenguaje cargado
    for t in TERMINOS_PROHIBIDOS:
        if contiene_termino(resp_sin_citas, t):
            errores.append(f"término cargado fuera de cita: '{t}' (atribúyelo entre comillas o quítalo)")
        elif contiene_termino(resp_norm, t):
            avisos.append(f"término cargado dentro de cita: '{t}' — confirma que está atribuido")
    for oracion in re.split(r"(?<=[.!?])\s+", fuera_de_citas(respuestas)):
        on = normalizar(oracion)
        for nombre in NOMBRES_PROPIOS:
            on = on.replace(nombre, " ")
        for t in TERMINOS_DISPUTADOS:
            if contiene_termino(on, t) and not any(contiene_termino(on, m) for m in MARCAS_ATRIBUCION):
                avisos.append(f"término disputado sin atribución: '{t}' en «{oracion.strip()[:80]}…»")

    # --- simetría en ejemplos de perspectivas
    if ej["tipo"] == "perspectivas":
        presentes = [a for a, claves in ACTORES.items() if any(c in resp_norm for c in claves)]
        if len(presentes) < 2:
            errores.append(f"tipo 'perspectivas' con menos de 2 actores (encontrados: {presentes or 'ninguno'})")

    # --- datos personales
    if RE_EMAIL.search(respuestas):
        errores.append("posible correo electrónico en la respuesta")
    if RE_TELEFONO.search(respuestas):
        avisos.append("posible número de teléfono en la respuesta")

    # --- idioma
    w = [x.lower() for x in palabras(respuestas)]
    es, en = sum(x in STOP_ES for x in w), sum(x in STOP_EN for x in w)
    if en > es:
        errores.append("la respuesta parece estar en inglés")

    # --- aprobado con notas de rechazo, o sin revisor
    if ej["estado_revision"] == "aprobado" and not str(ej.get("revisor", "")).strip():
        avisos.append("aprobado sin nombre de revisor")

    return errores, avisos


# ---------------------------------------------------------------- reglas de conjunto

def revisar_duplicados(ejemplos: list[dict]) -> dict[str, list[str]]:
    hallazgos: dict[str, list[str]] = defaultdict(list)

    ids = Counter(e["id"] for e in ejemplos)
    for i, c in ids.items():
        if c > 1:
            hallazgos[i].append(f"ERROR id repetido {c} veces")

    hashes: dict[str, str] = {}
    preguntas: dict[str, str] = {}
    sh: list[tuple[str, set[str]]] = []
    for e in ejemplos:
        resp = " ".join(m["content"] for m in e["messages"] if m.get("role") == "assistant")
        preg = normalizar(e["messages"][0]["content"]).strip()
        h = hashlib.sha256(normalizar(resp).encode()).hexdigest()
        if h in hashes:
            hallazgos[e["id"]].append(f"ERROR respuesta idéntica a {hashes[h]}")
        else:
            hashes[h] = e["id"]
        if preg in preguntas:
            hallazgos[e["id"]].append(f"AVISO pregunta idéntica a {preguntas[preg]}")
        else:
            preguntas[preg] = e["id"]
        sh.append((e["id"], shingles(resp)))

    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            a, b = sh[i][1], sh[j][1]
            if min(len(a), len(b)) / max(len(a), len(b), 1) < UMBRAL_CASI_DUPLICADO:
                continue  # tamaños muy distintos: no pueden superar el umbral
            s = jaccard(a, b)
            if s >= UMBRAL_CASI_DUPLICADO:
                hallazgos[sh[j][0]].append(f"AVISO casi duplicado de {sh[i][0]} (similitud {s:.2f})")
    return hallazgos


def balance(ejemplos: list[dict], fuentes: dict[str, dict]) -> dict:
    por_etapa = Counter(e["etapa"] for e in ejemplos)
    por_tipo = Counter(e["tipo"] for e in ejemplos)
    persp = defaultdict(Counter)
    for e in ejemplos:
        for f in e["fuentes"]:
            src = fuentes.get(f.get("id_fuente", ""))
            if src:
                persp[e["etapa"]][src.get("perspectiva", "?")] += 1
    return {"por_etapa": dict(por_etapa), "por_tipo": dict(por_tipo),
            "perspectiva_fuentes_por_etapa": {k: dict(v) for k, v in persp.items()}}


def revisar_registro(fuentes: dict[str, dict]) -> list[str]:
    problemas = []
    for fid, fila in fuentes.items():
        if fila.get("perspectiva", "").strip() not in PERSPECTIVAS_FUENTE:
            problemas.append(f"{fid}: perspectiva '{fila.get('perspectiva')}' no válida "
                             f"(usa: {', '.join(sorted(PERSPECTIVAS_FUENTE))})")
        if fila.get("uso", "").strip() not in USOS_FUENTE:
            problemas.append(f"{fid}: uso '{fila.get('uso')}' no válido (usa: {', '.join(sorted(USOS_FUENTE))})")
        if (fila.get("perspectiva", "").strip() == "gobierno_cubano"
                and fila.get("uso", "").strip() != "postura"):
            problemas.append(f"{fid}: una fuente oficial cubana solo puede tener uso=postura")
        if not fila.get("licencia", "").strip():
            problemas.append(f"{fid}: falta la licencia")
        if not fila.get("url", "").strip():
            problemas.append(f"{fid}: falta la url o referencia")
    return problemas


# ---------------------------------------------------------------- fragmentos

def validar_fragmentos(ruta: Path, fuentes: dict[str, dict]) -> int:
    """Valida fuentes/fragmentos_*.jsonl: cada fragmento es UN hecho o UNA postura, redactado
    con palabras propias, con la fuente principal y las que lo corroboran."""
    filas = cargar_jsonl(ruta)
    print(f"\n=== Validando fragmentos {ruta} ({len(filas)} líneas) ===\n")
    for p in revisar_registro(fuentes):
        print(f"[REGISTRO] {p}")

    total_err = total_av = 0
    ids = Counter()
    por_tipo, por_persp = Counter(), Counter()
    estados = Counter()
    for n, fr, err in filas:
        errores, avisos = [], []
        if err:
            errores.append(err)
            fr = {}
        fid_frag = fr.get("id", f"linea_{n}")
        ids[fid_frag] += 1
        if fr.get("estado") == "rechazado":
            estados["rechazado"] += 1
            continue  # se conserva por trazabilidad, pero no se valida ni se usa
        estados["aprobado" if fr.get("estado") == "aprobado" else "pendiente"] += 1
        for campo in ("id", "etapa", "tipo", "id_fuente", "ubicacion", "texto", "corroborado_por", "revisado"):
            if campo not in fr and not err:
                errores.append(f"falta el campo '{campo}'")
        tipo = fr.get("tipo")
        if tipo and tipo not in TIPOS_FRAGMENTO:
            errores.append(f"tipo '{tipo}' no válido (usa: {', '.join(sorted(TIPOS_FRAGMENTO))})")
        if fr.get("etapa") and fr["etapa"] not in ETAPAS:
            errores.append(f"etapa desconocida '{fr['etapa']}'")

        principal = fr.get("id_fuente", "")
        todas = [principal] + list(fr.get("corroborado_por", []))
        for f in todas:
            if f and f not in fuentes:
                errores.append(f"fuente '{f}' no está en el registro")
        usos = {f: fuentes.get(f, {}).get("uso", "") for f in todas if f in fuentes}
        de_hechos = [f for f, u in usos.items() if u in USOS_PARA_HECHOS]
        if any(u == "pendiente" for u in usos.values()):
            errores.append("cita una fuente en evaluación (uso=pendiente)")

        if tipo == "hecho" and not de_hechos:
            errores.append("un 'hecho' necesita al menos una fuente de hechos (no de postura)")
        if tipo == "hecho" and len(de_hechos) < 2:
            avisos.append("hecho con una sola fuente de hechos: buscar corroboración")
        if tipo == "postura":
            if usos.get(principal) in USOS_PARA_HECHOS and not fr.get("actor"):
                avisos.append("postura sin campo 'actor' (¿de quién es esta postura?)")
            if not any(contiene_termino(normalizar(fr.get("texto", "")), m) for m in MARCAS_ATRIBUCION):
                errores.append("una postura debe ir atribuida en el texto ('según...', 'afirmó...')")
        if tipo == "hecho_atribuido":
            if usos.get(principal) not in USOS_PARA_HECHOS:
                errores.append("un 'hecho_atribuido' necesita una fuente de uso hechos/ambos; "
                               "lo que dice una fuente de postura es una 'postura'")
            if not any(contiene_termino(normalizar(fr.get("texto", "")), m) for m in MARCAS_ATRIBUCION):
                errores.append("un 'hecho_atribuido' debe ir atribuido en el texto ('según...', 'relata...')")
            if len(de_hechos) >= 2:
                avisos.append("ya tiene dos fuentes de hechos: puede pasar a tipo 'hecho'")
        if tipo == "testimonio":
            # Experiencia personal real: siempre atribuida a quien la vivió y con fuente publicada.
            if not fr.get("testigo"):
                errores.append("un testimonio necesita el campo 'testigo' (quién lo contó, o 'anónimo')")
            if not any(contiene_termino(normalizar(fr.get("texto", "")), m) for m in MARCAS_ATRIBUCION ):
                errores.append("un testimonio debe ir atribuido en el texto ('según contó...', 'recuerda...')")
        if tipo == "cifra_disputada" and len(todas) < 2:
            errores.append("una cifra disputada debe citar al menos dos fuentes con valores distintos")

        if len(palabras(fr.get("texto", ""))) < 8:
            errores.append("texto vacío o demasiado corto")
        if not fr.get("revisado"):
            avisos.append("sin revisar por Denis")

        por_tipo[tipo] += 1
        por_persp[fuentes.get(principal, {}).get("perspectiva", "?")] += 1
        if errores or avisos:
            print(f"--- {fid_frag}")
            for e in errores:
                print(f"   ERROR  {e}")
            for a in avisos:
                print(f"   AVISO  {a}")
        total_err += len(errores)
        total_av += len(avisos)

    for i, c in ids.items():
        if c > 1:
            print(f"--- {i}\n   ERROR  id repetido {c} veces")
            total_err += 1

    print("\n=== Balance de fragmentos ===")
    print("Por tipo:       ", dict(por_tipo))
    print("Por perspectiva:", dict(por_persp))
    print(f"Revisión: {estados['aprobado']} aprobados | {estados['rechazado']} rechazados | "
          f"{estados['pendiente']} pendientes")
    print(f"Errores: {total_err} | Avisos: {total_av}")
    return 1 if total_err else 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description="Valida el dataset del exilio cubano")
    ap.add_argument("archivo", type=Path, help="JSONL a validar")
    ap.add_argument("--fuentes", type=Path, default=Path("fuentes/registro_fuentes.csv"))
    ap.add_argument("--exportar", type=Path, help="escribe solo los aprobados sin errores, listos para SFT")
    ap.add_argument("--reporte", type=Path, default=Path("reportes/reporte_validacion.json"))
    ap.add_argument("--fragmentos", action="store_true",
                    help="el archivo es un fuentes/fragmentos_*.jsonl, no ejemplos de entrenamiento")
    args = ap.parse_args()

    fuentes = cargar_fuentes(args.fuentes)
    filas = cargar_jsonl(args.archivo)
    if not args.fragmentos:
        # Detección automática: un fragmento tiene 'id_fuente' y 'texto', y no tiene 'messages'.
        primera = next((d for _, d, e in filas if d), None)
        if primera and "messages" not in primera and "id_fuente" in primera:
            print("(Detectado archivo de fragmentos: se valida como --fragmentos)")
            args.fragmentos = True
    if args.fragmentos:
        return validar_fragmentos(args.archivo, fuentes)

    print(f"\n=== Validando {args.archivo} ({len(filas)} líneas) ===\n")
    for p in revisar_registro(fuentes):
        print(f"[REGISTRO] {p}")

    resultados: dict[str, dict] = {}
    ejemplos: list[dict] = []
    for n, ej, err in filas:
        if err:
            resultados[f"linea_{n}"] = {"errores": [err], "avisos": []}
            continue
        errores, avisos = validar_ejemplo(ej, fuentes)
        resultados[ej.get("id", f"linea_{n}")] = {"errores": errores, "avisos": avisos}
        if "messages" in ej and "id" in ej and isinstance(ej["messages"], list) and ej["messages"]:
            ejemplos.append(ej)

    for eid, lista in revisar_duplicados(ejemplos).items():
        for h in lista:
            nivel, msg = h.split(" ", 1)
            resultados.setdefault(eid, {"errores": [], "avisos": []})
            resultados[eid]["errores" if nivel == "ERROR" else "avisos"].append(msg)

    total_err = total_av = 0
    for eid, r in resultados.items():
        if not r["errores"] and not r["avisos"]:
            continue
        print(f"--- {eid}")
        for e in r["errores"]:
            print(f"   ERROR  {e}")
        for a in r["avisos"]:
            print(f"   AVISO  {a}")
        total_err += len(r["errores"])
        total_av += len(r["avisos"])

    bal = balance(ejemplos, fuentes)
    print("\n=== Balance ===")
    print("Por etapa:", bal["por_etapa"])
    print("Por tipo: ", bal["por_tipo"])
    for etapa, c in bal["perspectiva_fuentes_por_etapa"].items():
        print(f"Fuentes en {etapa}: {c}")
        if len(c) == 1:
            print(f"   AVISO  {etapa} se apoya en una sola perspectiva de fuente")

    limpios = [e for e in ejemplos if not resultados[e["id"]]["errores"]]
    aprobados = [e for e in limpios if e.get("estado_revision") == "aprobado"]
    print(f"\nEjemplos: {len(ejemplos)} | sin errores: {len(limpios)} | aprobados listos: {len(aprobados)}")
    print(f"Errores: {total_err} | Avisos: {total_av}")

    args.reporte.parent.mkdir(parents=True, exist_ok=True)
    args.reporte.write_text(json.dumps({"resultados": resultados, "balance": bal}, ensure_ascii=False, indent=2),
                            encoding="utf-8")
    print(f"Reporte completo: {args.reporte}")

    if args.exportar:
        args.exportar.parent.mkdir(parents=True, exist_ok=True)
        with args.exportar.open("w", encoding="utf-8") as f:
            for e in aprobados:
                f.write(json.dumps({"messages": e["messages"]}, ensure_ascii=False) + "\n")
        print(f"Exportados {len(aprobados)} ejemplos a {args.exportar}")

    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
