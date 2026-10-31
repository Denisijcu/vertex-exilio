"""
agregar_fragmentos_onu.py — Añade los fragmentos sacados del informe de la ONU de 1988 (F019).

Uso (desde E:\\vertex-exilio):
    python agregar_fragmentos_onu.py

Fuente: E/CN.4/1989/46, versión en español (fuentes/docs/E_CN.4_1989_46-ES.pdf).
Cada fragmento indica el párrafo del informe en 'ubicacion' para que puedas comprobarlo.

Qué hace:
  1. Copia de seguridad de fuentes/fragmentos_presidio.jsonl y del registro.
  2. Añade FR-P021 a FR-P032, todos en 'pendiente' para que los revises.
  3. Devuelve FR-P014 a 'pendiente' con una nota: el informe no dice "137 casos de tortura y 7
     desaparecidos", sino "137 denuncias recibidas", y no da la cifra de 7. Tú decides si lo rechazas.
  4. Actualiza la nota de F019 en el registro de fuentes.
Si los fragmentos ya existen, no hace nada.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

FRAG = Path("fuentes/fragmentos_presidio.jsonl")
REG = Path("fuentes/registro_fuentes.csv")

NUEVOS = [
    ("FR-P021", "presidio_politico", "hecho", "párr. 3", None,
     "La misión de la Comisión de Derechos Humanos de la ONU que visitó Cuba en 1988 estuvo presidida "
     "por el embajador Alioune Sene, de Senegal, e integrada por representantes de Nigeria, Bulgaria, "
     "Filipinas, Irlanda y Colombia, uno por cada grupo regional."),
    ("FR-P022", "presidio_politico", "hecho", "párr. 12 y 21", None,
     "La misión estuvo en Cuba del 16 al 25 de septiembre de 1988. El día de su partida fue recibida "
     "por Fidel Castro y por Carlos Rafael Rodríguez, presidente y vicepresidente del Consejo de Estado."),
    ("FR-P023", "presidio_politico", "hecho", "párr. 19 y 20", None,
     "Según el informe, la misión escuchó directamente a 87 personas, más de 30 de ellas en "
     "representación de organizaciones no gubernamentales, y recogió el testimonio escrito de "
     "aproximadamente 1.600 personas."),
    ("FR-P024", "presidio_politico", "hecho", "párr. 16, 18 y 69", None,
     "La misión visitó el centro de detención de Villa Marista, sede del Departamento de Seguridad del "
     "Estado; la prisión Combinado del Este, donde entrevistó a nueve presos elegidos por ella; y la "
     "prisión provincial de Pinar del Río conocida como Cinco y Medio. Pidió visitar también El Morro, "
     "La Cabaña y Quivicán, y el ministro de Relaciones Exteriores le informó que estaban cerradas."),
    ("FR-P025", "presidio_politico", "hecho", "párr. 69", None,
     "Durante la visita, la Secretaría de la ONU recibió en nombre de la misión 137 denuncias de "
     "torturas, penas o tratos crueles, inhumanos o degradantes. El informe habla de denuncias "
     "recibidas."),
    ("FR-P026", "presidio_politico", "postura", "párr. 70", "gobierno_cubano",
     "Según el informe, el ministro del Interior de Cuba admitió ante la misión que en el pasado algunos "
     "detenidos y presos fueron golpeados y que los responsables fueron sancionados, pero afirmó que en "
     "Cuba no existen casos de tortura."),
    ("FR-P027", "presidio_politico", "postura", "párr. 67", "gobierno_cubano",
     "Según el informe, el ministro del Interior dijo a la misión que no tenía conocimiento de casos de "
     "desaparición forzada y que desde 1982 solo una persona había sido fusilada por delitos contra la "
     "seguridad del Estado; el ministro de Relaciones Exteriores afirmó que en Cuba no se producen "
     "desapariciones forzadas."),
    ("FR-P028", "presidio_politico", "hecho_atribuido", "párr. 68", None,
     "El informe recoge, según una carta de presos del Combinado del Este, que 13 presos políticos "
     "fueron fusilados en La Cabaña entre 1980 y 1987, y testimonios escritos que denuncian la "
     "desaparición de tres personas entre 1964 y 1974."),
    ("FR-P029", "presidio_politico", "hecho_atribuido", "párr. 74", None,
     "Según documentos que el Comité Cubano Pro Derechos Humanos y dos presos políticos entregaron a la "
     "misión, el 28 de mayo de 1988 presos políticos encontraron 15 micrófonos en sus celdas y se "
     "deshicieron de ellos; el incidente fue seguido de dos huelgas de hambre."),
    ("FR-P030", "transversal", "hecho", "párr. 85", None,
     "De las más de 1.600 personas que presentaron denuncias ante la misión de la ONU en 1988, 1.183 "
     "afirmaron tener dificultades para salir de Cuba, temporal o definitivamente, o tener familiares "
     "que querían visitar Cuba y no podían."),
    ("FR-P031", "transversal", "postura", "párr. 86", "gobierno_cubano",
     "Según el informe, Fidel Castro dijo a la misión que su gobierno autoriza por lo general la salida "
     "de quienes quieren irse, con excepciones como profesionales y científicos, ex oficiales de las "
     "Fuerzas Armadas, personas con secretos militares, desertores o sus familiares y jóvenes en edad "
     "de servicio militar, y responsabilizó a Estados Unidos de no conceder visas."),
    ("FR-P032", "transversal", "postura", "párr. 87", "gobierno_cubano",
     "Según el informe, Carlos Rafael Rodríguez afirmó que 35.000 cubanos salieron del país entre 1983 "
     "y 1988 y 5.932 entre enero y septiembre de 1988, y atribuyó a Estados Unidos que no se llegara a "
     "las 20.000 salidas anuales previstas en el acuerdo entre ambos países."),
]

NOTA_P014 = ("Revisar: el informe E/CN.4/1989/46 (párr. 69) habla de '137 denuncias recibidas', no de "
             "'137 casos'; y no da la cifra de 7 desaparecidos (el párr. 68 recoge denuncias sobre 3). "
             "Lo sustituye FR-P025. Propuesta: rechazar.")
NOTA_F019 = ("Leído (versión ES, 385 págs. escaneadas con OCR). Fragmentos FR-P021 a FR-P032. Las "
             "declaraciones de las autoridades cubanas recogidas en el informe van como postura.")

for p in (FRAG, REG):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

with FRAG.open(encoding="utf-8-sig") as f:
    frags = [json.loads(l) for l in f if l.strip()]
existentes = {d["id"] for d in frags}
if any(n[0] in existentes for n in NUEVOS):
    print("Los fragmentos FR-P021 en adelante ya existen. No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
for p in (FRAG, REG):
    shutil.copy2(p, p.with_name(f"{p.name}.{marca}.bak"))

for d in frags:
    if d["id"] == "FR-P014":
        d["estado"] = "pendiente"
        d["revisado"] = False
        d["notas"] = (d.get("notas", "") + " | " + NOTA_P014).strip(" |")

for fid, etapa, tipo, ubic, actor, texto in NUEVOS:
    d = {"id": fid, "etapa": etapa, "tipo": tipo, "id_fuente": "F019", "ubicacion": ubic,
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
    if r["id_fuente"] == "F019":
        r["notas"] = NOTA_F019
tmp = REG.with_suffix(".csv.tmp")
with tmp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)
tmp.replace(REG)

print(f"Añadidos {len(NUEVOS)} fragmentos (FR-P021 a FR-P032) en 'pendiente'.")
print("FR-P014 vuelve a 'pendiente' con la nota del informe: decide si lo rechazas.")
print("Nota de F019 actualizada en el registro.")
print("Ahora: python revisar.py fuentes\\fragmentos_presidio.jsonl")
