"""
agregar_presidio_lote2b.py — Complemento de agregar_presidio_lote2.py: registra F070-F071 (Wikipedia) y añade
FR-P057 a FR-P068 a fuentes/fragmentos_presidio.jsonl.

Hace falta porque agregar_presidio_lote2.py se corrió en su primera versión (F067-F069 y FR-P033 a FR-P056),
antes de que se le añadieran las dos páginas de Wikipedia.

Uso (desde E:\\vertex-exilio):
    python agregar_presidio_lote2b.py

Fuentes nuevas (en fuentes/docs, guardadas desde Chrome el 2026-10-30):
  F070  Wikipedia, 'Huber Matos'.
  F071  Wikipedia, 'Escambray rebellion'. Sus cifras de bajas, solo como disputadas.

Qué hace:
  1. Copia de seguridad del registro y del archivo de fragmentos.
  2. Añade F070-F071 al registro (si alguna ya existe, no toca nada).
  3. Añade FR-P057 a FR-P068 en 'pendiente' (si alguno de los IDs ya existe, no toca nada).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_presidio.jsonl")
HOY = "2026-10-30"
P, T = "presidio_politico", "transversal"

FUENTES = [
    ("F070", "Huber Matos", "Wikipedia", "https://en.wikipedia.org/wiki/Huber_Matos", "enciclopedia", "CC-BY-SA-4.0",
     "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_huber_matos.html (guardado desde Chrome el 2026-10-30). Se apoya en The New York Times "
     "de 1959 y 1979, PBS y Bonsal. 'Regime' no entra. Da dos fechas de fundación de CID (1981 y octubre de 1980). "
     "No se usa lo del proceso judicial de su hijo (no es del tema). Algunas frases llevan 'citation needed' y no se usan."),
    ("F071", "Escambray rebellion", "Wikipedia", "https://en.wikipedia.org/wiki/Escambray_rebellion", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_escambray.html (guardado desde Chrome el 2026-10-30). Cifras de bajas muy dispares y "
     "poco consistentes dentro del propio artículo: solo como cifra disputada. Fuentes de ambos lados (Encinosa, Dreke)."),
]

NUEVOS = [
    # ---------------- Wikipedia, Huber Matos
    dict(id="FR-P057", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Early life' y 'Revolutionary activity'",
         texto="Según Wikipedia, Huber Matos (1918-2014), maestro en Manzanillo, se opuso a Batista desde el golpe de 1952 y "
               "desde Costa Rica ayudó a los rebeldes de la Sierra Maestra; el 31 de marzo de 1958 llevó en avión un "
               "cargamento de armas y municiones, Castro le dio el mando de la columna 9 y el 11 de enero de 1959 fue "
               "nombrado jefe del ejército en la provincia de Camagüey."),
    dict(id="FR-P058", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Split with Castro'",
         texto="Según Wikipedia, en julio de 1959 Matos dio discursos anticomunistas en Camagüey, y el 19 de octubre envió a "
               "Castro una segunda carta de renuncia, después de haber escrito que la influencia comunista en el gobierno "
               "seguía creciendo; dos días después Camilo Cienfuegos lo arrestó junto con sus ayudantes militares."),
    dict(id="FR-P059", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Sentencing and imprisonment'",
         texto="Según Wikipedia, el mismo día del arresto Pedro Luis Díaz Lanz lanzó octavillas sobre La Habana; Castro "
               "convocó un mitin para pedir tribunales revolucionarios contra Matos y Díaz Lanz y, según The New York "
               "Times, cuando preguntó si Matos debía ser fusilado casi todos levantaron la mano y la multitud pidió el "
               "fusilamiento."),
    dict(id="FR-P060", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Sentencing and imprisonment'",
         texto="Según Wikipedia, en el juicio de diciembre de 1959, junto a cinco capitanes y once tenientes, Matos declaró "
               "que había hablado con oficiales anticomunistas sobre el nombramiento de comunistas pero que no había "
               "conspirado; Raúl Castro dijo que agitaba 'el fantasma del comunismo' y Fidel Castro, en un discurso de siete "
               "horas, lo acusó de favorecer indirectamente a Estados Unidos, a los latifundistas y a los partidarios de "
               "Batista; la fiscalía pidió la pena de muerte y el 15 de diciembre fue condenado a veinte años por actividad "
               "contrarrevolucionaria."),
    dict(id="FR-P061", etapa=P, tipo="testimonio", id_fuente="F070", ubicacion="'Sentencing and imprisonment'",
         testigo="Huber Matos",
         texto="Según contó Huber Matos, citado por Wikipedia, salió vivo de la cárcel por la voluntad de Dios: hizo huelgas "
               "de hambre, pasó en total dieciséis años en régimen de aislamiento, le repetían que moriría preso y fue "
               "torturado en varias ocasiones."),
    dict(id="FR-P062", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Sentencing and imprisonment' y 'Life after prison'",
         texto="Según Wikipedia, Matos cumplió los primeros seis años y medio de su condena en la prisión de Isla de Pinos y el "
               "resto en La Cabaña; salió en 1979, a los sesenta años, se reunió en Costa Rica con su esposa y sus hijos, "
               "que habían salido de Cuba en los años sesenta, y después se instaló en Miami, donde murió en febrero de 2014."),
    dict(id="FR-P063", etapa=T, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Life after prison'",
         texto="Según Wikipedia, Matos fundó en el exilio Cuba Independiente y Democrática (CID), que operaba emisoras de radio "
               "con noticias sin censura dirigidas a Cuba, convencido de que el cambio vendría desde dentro de la isla; el "
               "artículo da dos fechas de fundación, 1981 y octubre de 1980 en Venezuela. Escribió sus memorias, 'Cómo llegó "
               "la noche'."),
    dict(id="FR-P064", etapa=P, tipo="postura", id_fuente="F070", ubicacion="'Sentencing and imprisonment'", actor="Philip Bonsal",
         texto="Según Wikipedia, el embajador de Estados Unidos en Cuba, Philip Bonsal, consideró que Castro usó el vuelo de "
               "Díaz Lanz para provocar una reacción de masas y dejar de lado las cuestiones que planteaba la renuncia de Matos."),
    # ---------------- Wikipedia, rebelión del Escambray
    dict(id="FR-P065", etapa=P, tipo="hecho_atribuido", id_fuente="F071", ubicacion="introducción",
         texto="Según Wikipedia, la rebelión del Escambray (1959-1965) fue un conflicto armado en el que varios grupos "
               "insurgentes lucharon contra el gobierno de Fidel Castro, que llamó a su operación Lucha contra Bandidos; los "
               "rebeldes eran una mezcla de antiguos soldados de Batista, campesinos de la zona y antiguos guerrilleros que "
               "habían luchado junto a Castro, y en 1965 todos habían sido eliminados."),
    dict(id="FR-P066", etapa=P, tipo="hecho_atribuido", id_fuente="F071", ubicacion="'Beginning' e 'Insurgency'",
         texto="Según Wikipedia, entre los jefes de la rebelión estaban Osvaldo Ramírez y el estadounidense William Alexander "
               "Morgan, que habían combatido a Batista en esa misma zona; pequeños campesinos contrarios a la colectivización "
               "tuvieron un papel central, y la CIA y el gobierno de Eisenhower apoyaron la rebelión en secreto, aunque la CIA "
               "retiró su apoyo tras Bahía de Cochinos. Morgan fue detenido y fusilado en 1961 tras un juicio militar."),
    dict(id="FR-P067", etapa=P, tipo="cifra_disputada", id_fuente="F071", ubicacion="ficha y 'Legacy'", corroborado_por=["F069"],
         texto="Las cifras del Escambray varían mucho según la fuente: Wikipedia da entre 2.000 y 3.995 insurgentes y más de "
               "6.000 colaboradores, de 2.000 a 3.000 rebeldes muertos y 5.000 capturados, y del lado del gobierno 500 "
               "militares y 3.500 milicianos muertos; recoge que Raúl Castro habló en 1970 de 500 militares muertos y que "
               "las estimaciones del total de muertos van de 1.000 a 7.000. EcuRed habla de unos 4.190 alzados, 9.250 "
               "colaboradores y unas 590 bajas del gobierno."),
    dict(id="FR-P068", etapa=P, tipo="hecho_atribuido", id_fuente="F071", ubicacion="'Insurgency', 'Defeat' y 'Legacy'",
         texto="Según Wikipedia, el gobierno desplegó miles de soldados, a veces hasta 250.000 hombres, casi todos milicianos, "
               "en cercos cada vez más estrechos; algunos insurgentes que se rindieron fueron fusilados de inmediato y solo "
               "unos pocos lograron escapar; la Lucha contra Bandidos duró más y movilizó más soldados que la guerra contra "
               "Batista."),
]

for p in (REG, FRAG):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
if any(fu[0] in {r["id_fuente"] for r in filas} for fu in FUENTES):
    print("Alguna de las fuentes F070-F071 ya está en el registro. No toco nada.")
    sys.exit(0)

with FRAG.open(encoding="utf-8-sig") as f:
    lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n["id"] for n in NUEVOS if n["id"] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(REG, REG.with_name(f"{REG.name}.{marca}.bak"))
shutil.copy2(FRAG, FRAG.with_name(f"{FRAG.name}.{marca}.bak"))

for fid, titulo, autor, url, tipo, lic, persp, uso, notas in FUENTES:
    filas.append({"id_fuente": fid, "titulo": titulo, "autor_institucion": autor, "url": url, "tipo": tipo,
                  "licencia": lic, "perspectiva": persp, "uso": uso, "fecha_consulta": HOY, "notas": notas})
tmp = REG.with_suffix(".csv.tmp")
with tmp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)
tmp.replace(REG)

with FRAG.open("a", encoding="utf-8", newline="\n") as f:
    if lineas and not lineas[-1].endswith("\n"):
        f.write("\n")
    for n in NUEVOS:
        d = {"id": n["id"], "etapa": n["etapa"], "tipo": n["tipo"], "id_fuente": n["id_fuente"],
             "ubicacion": n["ubicacion"], "corroborado_por": n.get("corroborado_por", []), "texto": n["texto"],
             "notas": "", "revisado": False, "estado": "pendiente"}
        if n.get("actor"):
            d["actor"] = n["actor"]
        if n.get("testigo"):
            d["testigo"] = n["testigo"]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas {len(FUENTES)} fuentes (F070 y F071).")
print(f"Añadidos {len(NUEVOS)} fragmentos nuevos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
