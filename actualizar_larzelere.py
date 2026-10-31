"""
actualizar_larzelere.py — Añade fragmentos verificados en el PDF de Larzelere (F007) y corrige
las páginas de la cronología en fragmentos ya aprobados.

Uso (desde E:\\vertex-exilio):
    python actualizar_larzelere.py

Fuente leída: fuentes/docs/LARZELERE_MARIEL_BOATLIFT.pdf (564 págs.) y, para "escoria", el
discurso del 1 de mayo de 1980 (F002, traducción FBIS).

Qué hace:
  1. Copia de seguridad de fuentes/fragmentos_mariel.jsonl y del registro.
  2. Corrige SOLO el campo 'ubicacion' de 8 fragmentos aprobados: la página de la cronología
     estaba desviada en una. El texto no cambia, así que siguen aprobados.
  3. Añade FR-M043 a FR-M051 en 'pendiente'.
  4. Actualiza la nota de F007 en el registro.
Si los fragmentos nuevos ya existen, no hace nada.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

FRAG = Path("fuentes/fragmentos_mariel.jsonl")
REG = Path("fuentes/registro_fuentes.csv")

# id: (ubicación que debería tener ahora, ubicación corregida)
UBICACIONES = {
    "FR-M005": ("pp. 33-35; cronología p. xxix", "pp. 33-35; cronología p. xxviii"),
    "FR-M007": ("Cronología p. xxx", "Cronología p. xxix; pp. 123-124"),
    "FR-M008": ("Cronología p. xxx", "Cronología p. xxix"),
    "FR-M014": ("Cronología p. xxxi", "Cronología p. xxx"),
    "FR-M015": ("Cronología p. xxxii", "Cronología p. xxxi"),
    "FR-M017": ("Cronología p. xxxiii", "Cronología p. xxxii"),
    "FR-M018": ("Cronología p. xxxiii", "Cronología p. xxxii"),
    "FR-M019": ("Cronología p. xxxiii", "Cronología p. xxxii"),
}

# (id, tipo, fuente, ubicación, actor, texto)
NUEVOS = [
    ("FR-M043", "hecho", "F007", "Cronología p. xxix", None,
     "El 27 de abril de 1980 se designó a la Agencia Federal para el Manejo de Emergencias (FEMA) "
     "para coordinar la respuesta federal sobre el terreno a la emergencia de los refugiados cubanos."),
    ("FR-M044", "hecho", "F007", "Cronología p. xxx", None,
     "El 28 de abril de 1980 el Servicio de Aduanas de Estados Unidos empezó a incautar los barcos que "
     "volvían de Mariel por traer extranjeros ilegales; la FEMA suspendió las incautaciones a los dos "
     "días, cuando el ambiente en los muelles de Cayo Hueso se volvió tenso."),
    ("FR-M045", "hecho", "F007", "Cronología p. xxxi", None,
     "El 20 de mayo de 1980 la Casa Blanca anunció que los cubanos que llegaban no serían tratados como "
     "refugiados bajo la Ley de Refugiados de 1980, sino como solicitantes de asilo."),
    ("FR-M046", "hecho_atribuido", "F007", "Cronología p. xxx", None,
     "Según la cronología de Larzelere, el 2 de mayo de 1980 un grupo de unos 300 hombres armados con "
     "palos, llevados en autobuses del gobierno, atacó en La Habana a ex presos políticos y a sus "
     "familiares reunidos frente a la Sección de Intereses de Estados Unidos."),
    ("FR-M047", "hecho_atribuido", "F007", "p. 35", None,
     "Según Larzelere, en los dos primeros días del puente aéreo a San José se evacuó a 678 refugiados; "
     "al tercer día el gobierno de Costa Rica anunció que suspendía los vuelos a petición de Cuba. "
     "Larzelere lo atribuye a que la publicidad internacional negativa de los vuelos había molestado "
     "al gobierno de Castro."),
    ("FR-M048", "hecho", "F007", "p. 331", None,
     "El 26 de abril de 1980 el gobernador de la Florida, Bob Graham, declaró zonas de desastre los "
     "condados de Monroe y Dade por la llegada de refugiados cubanos y activó la Guardia Nacional de "
     "la Florida."),
    ("FR-M049", "hecho", "F007", "pp. 5-6", None,
     "A principios de 1980, cuando 12 personas entraron por la fuerza en la embajada del Perú en La "
     "Habana, el embajador Edgardo de Habich les negó el asilo y las devolvió a sus casas. El "
     "Ministerio de Relaciones Exteriores del Perú desautorizó su decisión y le ordenó llevarlas de "
     "vuelta a la embajada; él lo hizo y anunció que dejaba el cargo."),
    ("FR-M050", "postura", "F007", "pp. 4-5", "gobierno_cubano",
     "Según Larzelere, tras el incidente del 1 de abril de 1980 el gobierno cubano declaró en la "
     "primera página de Granma que no daría salvoconducto para salir del país a nadie que entrara por "
     "la fuerza en una embajada extranjera."),
    ("FR-M051", "postura", "F002", "discurso del 1 de mayo de 1980, traducción FBIS", "gobierno_cubano",
     "En el discurso del 1 de mayo de 1980, según la traducción al inglés del FBIS, Castro llamó "
     "'scum' (escoria) a quienes habían entrado en la embajada del Perú."),
]

NOTA_F007 = ("PDF en fuentes/docs (564 págs.). Páginas verificadas en el PDF. Datos operativos = hechos; "
             "declaraciones de la Casa Blanca o del gobierno cubano = postura. No menciona la fecha del "
             "fin por acuerdo (octubre) ni el día de más llegadas.")

for p in (FRAG, REG):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

with FRAG.open(encoding="utf-8-sig") as f:
    frags = [json.loads(l) for l in f if l.strip()]
por_id = {d["id"]: d for d in frags}
if any(n[0] in por_id for n in NUEVOS):
    print("Los fragmentos FR-M043 en adelante ya existen. No toco nada.")
    sys.exit(0)

for fid, (antes, despues) in UBICACIONES.items():
    d = por_id.get(fid)
    if d is None:
        print(f"No encuentro {fid}. No toco nada.")
        sys.exit(1)
    if d["ubicacion"] not in (antes, despues):
        print(f"{fid} tiene ubicacion '{d['ubicacion']}', esperaba '{antes}'. No toco nada.")
        sys.exit(1)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
for p in (FRAG, REG):
    shutil.copy2(p, p.with_name(f"{p.name}.{marca}.bak"))

for fid, (antes, despues) in UBICACIONES.items():
    por_id[fid]["ubicacion"] = despues

for fid, tipo, fuente, ubic, actor, texto in NUEVOS:
    d = {"id": fid, "etapa": "mariel_1980", "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
         "corroborado_por": [], "texto": texto, "notas": "", "revisado": False, "estado": "pendiente"}
    if actor:
        d["actor"] = actor
    frags.append(d)

tmp = FRAG.with_suffix(".jsonl.tmp")
with tmp.open("w", encoding="utf-8", newline="\n") as f:
    for d in frags:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
tmp.replace(FRAG)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
for r in filas:
    if r["id_fuente"] == "F007":
        r["notas"] = NOTA_F007
tmp = REG.with_suffix(".csv.tmp")
with tmp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)
tmp.replace(REG)

print(f"Páginas corregidas en {len(UBICACIONES)} fragmentos (siguen aprobados).")
print(f"Añadidos {len(NUEVOS)} fragmentos (FR-M043 a FR-M051) en 'pendiente'.")
print("Nota de F007 actualizada en el registro.")
print("Ahora: python revisar.py fuentes\\fragmentos_mariel.jsonl")
