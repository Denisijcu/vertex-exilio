"""
agregar_guerra.py — Añade fragmentos y testimonios verificados en el artículo de Lillian Guerra
(F006) y corrige los ejemplos exi-m037 y exi-m035.

Uso (desde E:\\vertex-exilio):
    python agregar_guerra.py

Fuente leída: fuentes/docs/GUERRA_2024_LARR.pdf (Latin American Research Review 59, 2024,
pp. 872-894, CC-BY 4.0). La página va en 'ubicacion'.

Por qué se corrigen los ejemplos:
  - exi-m037 decía que "en las fuentes que hemos revisado no hay documentación" de que se obligara a
    gente a salir. Guerra (p. 876), citando a Clark, Lasaga y Reque (1981), dice que menos del 40 %
    fue recogido por familiares y que el resto fue obligado a salir por el gobierno o salió por su
    cuenta. La respuesta era falsa: se reescribe.
  - exi-m035 decía que no había datos sobre enfermos mentales. Guerra dice que los hubo, sin cifra.
    Se ajusta esa frase.

Qué hace:
  1. Copia de seguridad (.bak con fecha) de cada archivo que toca.
  2. Añade FR-M052 a FR-M062 en 'pendiente'.
  3. Reescribe las respuestas de exi-m037 y exi-m035, añade sus nuevos fragmentos y los deja en
     'pendiente'.
  4. Aplica el mismo cambio en generar_lote3_mariel.py para que no vuelva el texto viejo.
Es todo o nada: si algo no encaja, no escribe nada.
"""
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

FRAG = Path("fuentes/fragmentos_mariel.jsonl")
DATOS = Path("datos/borrador_mariel_lote3.jsonl")
GEN = Path("generar_lote3_mariel.py")

# (id, tipo, ubicación, testigo, texto) — todos de F006
NUEVOS = [
    ("FR-M052", "hecho_atribuido", "p. 875", None,
     "Según la historiadora Lillian Guerra, el embajador del Perú, Ernesto Pinto Bazurco Rittler, se negó "
     "a entregar a quienes entraron en la embajada el 1 de abril de 1980 pese a las exigencias de las "
     "autoridades cubanas, y Guerra sostiene que Fidel Castro retiró la guardia el 4 de abril como "
     "represalia."),
    ("FR-M053", "testimonio", "p. 875", "Ernesto Pinto Bazurco Rittler, embajador del Perú",
     "Según el embajador peruano Ernesto Pinto Bazurco Rittler, citado por Guerra, el primer cubano que "
     "entró a pedir asilo cuando se retiró la guardia fue un hombre negro, que le dijo que esperaba que "
     "muchos siguieran su ejemplo; el embajador cuenta que entre los policías, militares e informantes "
     "reunidos alrededor de la embajada no distinguió a ningún afrocubano."),
    ("FR-M054", "hecho_atribuido", "p. 876", None,
     "Según Guerra, que cita un estudio de Clark, Lasaga y Reque de 1981, menos del 40 por ciento de los "
     "refugiados del Mariel fueron recogidos por sus familiares; el resto fueron obligados a salir por el "
     "gobierno o salieron por iniciativa propia tras 'demostrar' ante la policía que estaban contra el "
     "gobierno, muchas veces con confesiones falsas o exageradas de conductas que la ley consideraba "
     "antisociales."),
    ("FR-M055", "hecho_atribuido", "p. 876", None,
     "Según Guerra, entre quienes salieron por Mariel había enfermos mentales y ancianos dependientes, y al "
     "menos 20.000 personas que habían pasado algún tiempo en prisiones cubanas; la mayoría de estas no "
     "eran autores de delitos violentos, sino personas que se resistían al adoctrinamiento político o "
     "que habían participado en el mercado negro."),
    ("FR-M056", "testimonio", "p. 888", "estudiante de 19 años (anónimo), entrevistado por Cros Sandoval",
     "Un estudiante de 19 años entrevistado por Mercedes Cros Sandoval contó que, criado como católico a "
     "escondidas, cuestionó en clase que hubiera que hacer trabajo voluntario en memoria de Marx y Lenin; "
     "el maestro lo llevó aparte, le advirtió que era demasiado joven para acabar preso, y él lloró."),
    ("FR-M057", "testimonio", "p. 888", "María (marielita), entrevistada por Cros Sandoval",
     "Una marielita llamada María contó a Cros Sandoval que a los 14 años preguntó en clase por qué en Cuba "
     "no había mariscos para el consumo si abundaban en sus aguas; la maestra dio una explicación oficial y "
     "después la llevó aparte para advertirle que no hiciera preguntas que pudieran avergonzar al gobierno."),
    ("FR-M058", "testimonio", "p. 889", "mujer anónima, entrevistada por Cros Sandoval",
     "Una mujer contó a Cros Sandoval que su esposo, militante comunista, se había inventado un origen "
     "humilde que su hijo mayor desmintió cuando los visitó la familia exiliada; dos años después ese hijo "
     "entró con su esposa en la embajada del Perú, y ella y su hijo menor lo siguieron."),
    ("FR-M059", "hecho_atribuido", "p. 889", None,
     "Según Guerra, los mítines de repudio los dirigían activistas de los CDR, en su mayoría amas de casa y "
     "jubilados, y maestros que llevaban aulas enteras, por lo que predominaban mujeres y niños; de noche se "
     "pintaban en las fachadas frases como 'Aquí vive un traidor'."),
    ("FR-M060", "hecho_atribuido", "p. 890", None,
     "Según Guerra, que cita a Clark, de Fana y Sánchez (1991), el CDR colgó en la puerta de Olga Alujas, "
     "que había sido militante de la Juventud Comunista, un cartel que la llamaba traidora a la UJC y al "
     "pueblo por haber entrado en la embajada del Perú."),
    ("FR-M061", "hecho_atribuido", "p. 890", None,
     "Según Guerra, el profesor de filosofía marxista Ariel Hidalgo fue internado en un hospital "
     "psiquiátrico después de defender a un alumno atacado en un mitin de repudio; más tarde fue detenido "
     "por un manuscrito crítico y empezó a cumplir una condena de ocho años el 19 de abril de 1981, los "
     "primeros catorce meses en régimen de aislamiento."),
    ("FR-M062", "hecho_atribuido", "p. 877", None,
     "Según Guerra, que cita a Clark, Lasaga y Reque (1981) y a María Cristina García (1996), los "
     "marielitos eran un 70 por ciento hombres, un 92 por ciento de clase trabajadora y hasta un 40 por "
     "ciento mestizos o negros, con una edad media de unos 30 años: a diferencia de las olas anteriores, "
     "habían crecido bajo la revolución."),
]

M037_VIEJO = """Hay quien lo afirma, pero en las fuentes que hemos revisado no hay documentación que lo pruebe, así que no se puede dar como hecho.

Lo que sí está documentado es una acusación. Según la cronología del historiador Alex Larzelere, el 7 de junio de 1980 la Casa Blanca denunció que el gobierno cubano estaba enviando "criminales endurecidos" sacados de sus cárceles. Esa fue la postura del gobierno de Estados Unidos; una denuncia política no es lo mismo que una prueba de que se obligara a nadie a embarcar.

Lo documentado sobre cómo se organizó la salida es otra cosa: el 20 de abril de 1980 el gobierno cubano anunció que el puerto de Mariel quedaba abierto para quien tuviera a alguien que fuera a recogerlo en barco, y alrededor de 1.700 embarcaciones, en su mayoría organizadas por cubanos de la Florida, fueron a buscar a quienes querían salir.

En cuanto a los antecedentes penales, las cifras disponibles hablan de una proporción pequeña: alrededor del 2,2 por ciento fue clasificado como delincuente grave bajo la ley estadounidense.

Si encuentras una fuente seria que documente casos concretos de personas embarcadas a la fuerza, vale la pena revisarla con cuidado. Hasta entonces, lo correcto es decir que se ha afirmado, pero que no está demostrado en lo que hemos revisado."""

M037_NUEVO = """Sí, hay fuentes que lo sostienen, aunque conviene distinguir bien qué dice cada una.

La historiadora Lillian Guerra, que cita un estudio de Clark, Lasaga y Reque de 1981, afirma que menos del 40 por ciento de los refugiados del Mariel fueron recogidos por sus familiares. Según ella, el resto fueron obligados a salir por el gobierno o salieron por iniciativa propia, después de "demostrar" ante la policía que estaban contra el gobierno, muchas veces con confesiones falsas o exageradas de conductas que la ley consideraba antisociales.

A eso se suma una acusación política. Según la cronología del historiador Alex Larzelere, el 7 de junio de 1980 la Casa Blanca denunció que el gobierno cubano estaba enviando "criminales endurecidos" sacados de sus cárceles. Esa fue la postura del gobierno de Estados Unidos.

El marco oficial de la salida era otro: el 20 de abril de 1980 el gobierno cubano anunció que el puerto de Mariel quedaba abierto para quien tuviera a alguien que fuera a recogerlo en barco, y alrededor de 1.700 embarcaciones, en su mayoría organizadas por cubanos de la Florida, fueron a buscar gente.

Lo que las fuentes no permiten es decir cuántas personas exactamente salieron obligadas. Y en cuanto a antecedentes penales graves, las cifras disponibles hablan de alrededor del 2,2 por ciento."""

M035_VIEJO = ("Sobre los enfermos mentales: en las fuentes que hemos revisado no hay cifras verificadas, así "
              "que lo honesto es no dar ningún número.")
M035_NUEVO = ("Sobre los enfermos mentales: la historiadora Lillian Guerra señala que entre quienes salieron "
              "había enfermos mentales y ancianos dependientes, pero no da ninguna cifra, así que lo honesto "
              "es no inventar un número.")

# id del ejemplo: (sustituciones en la respuesta, fragmentos a añadir)
CAMBIOS = {
    "exi-m037": ([(M037_VIEJO, M037_NUEVO)], ["FR-M054"]),
    "exi-m035": ([(M035_VIEJO, M035_NUEVO)], ["FR-M055"]),
}
LISTAS_GEN = [
    ('["FR-M017", "FR-M006", "FR-M009", "FR-M020"]),',
     '["FR-M017", "FR-M006", "FR-M009", "FR-M020", "FR-M054"]),'),
    ('["FR-M020", "FR-M028", "FR-M017", "FR-M041", "FR-M027", "FR-M026", "FR-M038"]),',
     '["FR-M020", "FR-M028", "FR-M017", "FR-M041", "FR-M027", "FR-M026", "FR-M038", "FR-M055"]),'),
]
NOTA = "Corregido con Guerra (F006, p. 876): ver agregar_guerra.py."


def leer(p):
    with p.open(encoding="utf-8-sig") as f:
        return [json.loads(l) for l in f if l.strip()]


def escribir(p, filas):
    tmp = p.with_suffix(p.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as f:
        for d in filas:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    tmp.replace(p)


for p in (FRAG, DATOS, GEN):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

frags = leer(FRAG)
if any(d["id"] == NUEVOS[0][0] for d in frags):
    print("Los fragmentos FR-M052 en adelante ya existen. No toco nada.")
    sys.exit(0)
nuevos_frag = []
for fid, tipo, ubic, testigo, texto in NUEVOS:
    d = {"id": fid, "etapa": "mariel_1980", "tipo": tipo, "id_fuente": "F006", "ubicacion": ubic,
         "corroborado_por": [], "texto": texto, "notas": "", "revisado": False, "estado": "pendiente"}
    if testigo:
        d["testigo"] = testigo
    nuevos_frag.append(d)
texto_de = {d["id"]: d["texto"] for d in nuevos_frag}

ejemplos = leer(DATOS)
hechos = set()
for ej in ejemplos:
    if ej["id"] not in CAMBIOS:
        continue
    sust, extra = CAMBIOS[ej["id"]]
    for viejo, nuevo in sust:
        cuantos = sum(m["content"].count(viejo) for m in ej["messages"] if m["role"] == "assistant")
        if cuantos != 1:
            print(f"{ej['id']}: no encuentro el texto a corregir (¿ya se corrigió?). No toco nada.")
            sys.exit(1)
        for m in ej["messages"]:
            if m["role"] == "assistant":
                m["content"] = m["content"].replace(viejo, nuevo)
    for fid in extra:
        ej["fuentes"].append({"id_fragmento": fid, "id_fuente": "F006", "fragmento": texto_de[fid]})
    ej["estado_revision"] = "pendiente"
    ej["notas"] = (ej.get("notas", "") + " | " + NOTA).strip(" |")
    hechos.add(ej["id"])
if hechos != set(CAMBIOS):
    print(f"No encuentro los ejemplos {sorted(set(CAMBIOS) - hechos)}. No toco nada.")
    sys.exit(1)

gen = GEN.read_text(encoding="utf-8")
for viejo, nuevo in [(M037_VIEJO, M037_NUEVO), (M035_VIEJO, M035_NUEVO)] + LISTAS_GEN:
    if gen.count(viejo) != 1:
        print(f"{GEN.name}: no encuentro un texto a corregir. No toco nada.")
        sys.exit(1)
    gen = gen.replace(viejo, nuevo)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
for p in (FRAG, DATOS, GEN):
    shutil.copy2(p, p.with_name(f"{p.name}.{marca}.bak"))
escribir(FRAG, frags + nuevos_frag)
escribir(DATOS, ejemplos)
GEN.write_text(gen, encoding="utf-8", newline="\n")

print(f"Añadidos {len(NUEVOS)} fragmentos de Guerra (FR-M052 a FR-M062) en 'pendiente'.")
print("Corregidos exi-m037 y exi-m035; vuelven a 'pendiente'.")
print("Ahora revisa primero los fragmentos y después los ejemplos.")
