"""
agregar_1959_1962.py — Abre las etapas 1959-1962 y Pedro Pan: registra las fuentes F026-F033 y
crea fuentes/fragmentos_1959_1962.jsonl con los fragmentos verificados en los documentos.

Uso (desde E:\\vertex-exilio):
    python agregar_1959_1962.py

Documentos leídos (en fuentes/docs): FIU_Cauce_Pedro_Pan.pdf, NPS_freedom_tower_NHL.pdf,
Walsh_2001_history_pedro_pan.htm, v25n3p3.pdf (SSA 1962), WIKI_operation_peter_pan.html,
ECURED_operacion_peter_pan.html. La página o sección va en 'ubicacion'.

Criterio: la versión del organizador (Walsh) y la del gobierno cubano (EcuRed) van como postura
o atribuidas; el lenguaje valorativo de cualquiera de las fuentes no entra.

Qué hace:
  1. Copia de seguridad del registro.
  2. Añade F026-F033 al registro (si ya existen, no hace nada).
  3. Crea fuentes/fragmentos_1959_1962.jsonl con todos los fragmentos en 'pendiente'
     (si el archivo ya existe, no lo toca).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_1959_1962.jsonl")
HOY = "2026-10-30"

FUENTES = [
    ("F026", "Operation Pedro Pan: 50 Years Later", "Rita M. Cauce - Florida International University Libraries (c. 2012)",
     "https://digitalcommons.fiu.edu/record/17769/files/Cauce_Operation_Pedro_Pan.pdf", "academica", "revisar",
     "academica", "ambos",
     "Archivo fuentes/docs/FIU_Cauce_Pedro_Pan.pdf (14 págs.). Usa lenguaje valorativo contra el gobierno cubano "
     "('régimen', 'eliminación despiadada'): NO entra al dataset. Sus datos van con página."),
    ("F027", "Freedom Tower - National Historic Landmark Nomination", "US National Park Service (2008)",
     "https://npgallery.nps.gov/pdfhost/docs/NRHP/Text/79000665.pdf", "primaria", "dominio_publico (obra del gobierno de EE. UU.)",
     "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/NPS_freedom_tower_NHL.pdf. Datos = hechos; valoraciones ('magnanimidad', 'tiranía') = "
     "postura de EE. UU., no entran."),
    ("F028", "The History of Operation Pedro Pan", "Mons. Bryan O. Walsh - Operation Pedro Pan Group, 2001 (copia en BishopAccountability.org)",
     "https://www.bishop-accountability.org/news5/2001_03_01_Walsh_TheHistory.htm", "primaria",
     "BishopAccountability: reproducción libre citando la fuente", "exilio", "ambos",
     "Archivo fuentes/docs/Walsh_2001_history_pedro_pan.htm. Texto del organizador de Pedro Pan: los datos de su "
     "agencia van atribuidos; sus desmentidos y valoraciones, como postura."),
    ("F029", "The Cuban Refugee Program", "William L. Mitchell, Comisionado de Seguridad Social - Social Security Bulletin 25(3), marzo de 1962",
     "https://ssa.gov/policy/docs/ssb/v25n3/v25n3p3.pdf", "primaria", "dominio_publico (obra del gobierno de EE. UU.)",
     "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/v25n3p3.pdf (pp. 3-8). Datos del programa = hechos; las declaraciones de Kennedy = "
     "postura de EE. UU."),
    ("F030", "Analysis of Federal Expenditures to Aid Cuban Refugees (B-164031(3))", "Comptroller General of the United States (GAO), 1971",
     "https://www.gao.gov/assets/b-164031%283%29-095487.pdf", "primaria", "dominio_publico (obra del gobierno de EE. UU.)",
     "gobierno_eeuu", "hechos",
     "Archivo fuentes/docs/b-164031(3)-095487.pdf (escaneado con OCR). Para la etapa de los Vuelos de la Libertad; "
     "todavía sin extraer."),
    ("F031", "Operation Peter Pan", "Wikipedia", "https://en.wikipedia.org/wiki/Operation_Peter_Pan", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_operation_peter_pan.html (descargado el 2026-10-30). Resume a Torres, Shnookal y el "
     "fallo judicial de 1999. Para cifras polémicas, ir a las fuentes que cita."),
    ("F032", "Operación Peter Pan", "EcuRed (enciclopedia del gobierno cubano)", "https://www.ecured.cu/Operaci%C3%B3n_Peter_Pan",
     "enciclopedia", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/ECURED_operacion_peter_pan.html. Versión oficial cubana: SOLO para documentar lo que "
     "afirma el gobierno. Nunca sostiene un hecho ni una cifra."),
    ("F033", "Operación Peter Pan: cerrando el círculo en Cuba", "Estela Bravo (doc.), Olga Rosa Gómez Cortés (comp.) - Fondo Editorial Casa de las Américas, La Habana, 2013",
     "https://biblioteca.clacso.edu.ar/Cuba/casa/20200419043104/Operacion-Peter-Pan.pdf", "secundaria", "revisar",
     "gobierno_cubano", "postura",
     "No se pudo descargar (el servidor de CLACSO falla) y todavía no se ha leído. Editorial del Estado cubano: solo postura."),
]

# (id, etapa, tipo, fuente, ubicación, corroborado_por, actor, texto)
FRAGMENTOS = [
    ("FR-S001", "salida_1959_1962", "hecho_atribuido", "F026", "p. 6", [], None,
     "Según el sociólogo Juan Clark, citado por Cauce, unos 64.000 cubanos habían salido de la isla a finales de "
     "1959, y la cifra llegó a 248.070 a finales de 1962."),
    ("FR-S002", "salida_1959_1962", "hecho", "F029", "p. 3", ["F026"], None,
     "En noviembre de 1960 el presidente Eisenhower encargó a Tracy S. Voorhees estudiar la situación de los "
     "refugiados cubanos, y bajo su dirección se creó en Miami un Centro de Emergencia para Refugiados Cubanos, "
     "financiado en parte con el Fondo de Contingencia del presidente."),
    ("FR-S003", "salida_1959_1962", "hecho", "F029", "pp. 3-4", ["F026"], None,
     "El 27 de enero de 1961 el presidente Kennedy encargó al secretario de Salud, Educación y Bienestar, Abraham "
     "Ribicoff, dirigir las actividades federales para los refugiados cubanos, y el 3 de febrero le ordenó poner en "
     "marcha un programa de nueve puntos con ayuda económica, salud, educación, empleo, reasentamiento en otras zonas "
     "y atención a los niños que llegaban sin sus padres."),
    ("FR-S004", "salida_1959_1962", "postura", "F029", "p. 3", [], "gobierno_eeuu",
     "Según el artículo de la Seguridad Social de 1962, Kennedy presentó la ayuda como temporal: pidió asegurar a los "
     "refugiados que se buscaría facilitar su regreso voluntario a Cuba en cuanto las condiciones lo permitieran."),
    ("FR-S005", "salida_1959_1962", "hecho", "F029", "p. 4", [], None,
     "Para el programa de refugiados, a los cubanos se les autorizó una 'salida voluntaria indefinida', sin límite de "
     "tiempo, de modo que no se les abría proceso de deportación."),
    ("FR-S006", "salida_1959_1962", "hecho", "F029", "p. 5", [], None,
     "El programa federal evitó crear campamentos de refugiados y puso el acento en reasentar a los cubanos fuera de "
     "Miami. Según el artículo de marzo de 1962, más de 16.000 personas habían sido reasentadas por el programa y otras "
     "16.000 se habían trasladado por su cuenta, y la población refugiada en el condado de Dade superaba las 55.000 "
     "personas."),
    ("FR-S007", "salida_1959_1962", "hecho", "F029", "p. 5", [], None,
     "De cada 20 refugiados registrados en el centro de Miami, 17 pedían ayuda en efectivo y 16 la recibían, según el "
     "artículo de la Seguridad Social de 1962."),
    ("FR-S008", "salida_1959_1962", "hecho", "F029", "p. 5", [], None,
     "Según el artículo de la Seguridad Social de 1962, más de un tercio de los cabezas de familia refugiados había "
     "trabajado en ocupaciones profesionales, semiprofesionales o directivas; casi un tercio, en trabajos de oficina, "
     "ventas o especializados; y menos de una cuarta parte no tenía una calificación especial."),
    ("FR-S009", "salida_1959_1962", "hecho", "F027", "pp. 4 y 13", [], None,
     "La Torre de la Libertad de Miami, a la que los refugiados llamaban 'El Refugio', funcionó entre 1962 y 1974 "
     "como centro federal de asistencia a los refugiados cubanos."),
    ("FR-S010", "salida_1959_1962", "hecho", "F027", "p. 4", [], None,
     "En 1962 la administración Kennedy impulsó la Ley de Asistencia a la Migración y a los Refugiados (Migration and "
     "Refugee Assistance Act) para dar ayuda a los cubanos que llegaban a Miami."),
    ("FR-S011", "camarioca_vuelos_libertad", "hecho_atribuido", "F027", "p. 12", [], None,
     "Según la ficha del Servicio de Parques Nacionales, que toma las cifras de María Cristina García, los vuelos "
     "desde Cuba se reanudaron en 1965 y siguieron, con una breve pausa, hasta el 6 de abril de 1973; en más de 3.000 "
     "'Vuelos de la Libertad' llegaron otros 175.000 cubanos."),
    ("FR-PP001", "pedro_pan", "hecho", "F026", "p. 9", ["F028", "F031"], None,
     "Entre diciembre de 1960 y octubre de 1962 llegaron a Estados Unidos sin sus padres más de 14.000 niños y "
     "adolescentes cubanos en lo que se llamó Operación Pedro Pan; la estimación más citada es de 14.048."),
    ("FR-PP002", "pedro_pan", "cifra_disputada", "F028", "texto", ["F026", "F027"], None,
     "Las fechas de Pedro Pan varían según la fuente: Walsh sitúa las llegadas entre el 26 de diciembre de 1960 y el "
     "23 de octubre de 1962; Cauce dice que la operación se detuvo el 22 de octubre de 1962, con la Crisis de "
     "Octubre; la ficha del Servicio de Parques Nacionales la data desde el 12 de diciembre de 1960, el día en que se "
     "reunieron Walsh y James Baker."),
    ("FR-PP003", "pedro_pan", "hecho", "F026", "pp. 4, 6-7", ["F028"], None,
     "En noviembre de 1960 llegó a la oficina del padre Bryan Walsh, director del Catholic Welfare Bureau de Miami, "
     "un muchacho cubano de 15 años, Pedro, cuyos familiares en Miami no podían mantenerlo. El 12 de diciembre de "
     "1960 Walsh se reunió con James Baker, director de la Academia Ruston de La Habana, que ayudaba a padres cubanos "
     "a enviar a sus hijos a Estados Unidos."),
    ("FR-PP004", "pedro_pan", "hecho", "F026", "p. 8", [], None,
     "Tras la ruptura de relaciones entre Estados Unidos y Cuba el 3 de enero de 1961, el Departamento de Estado "
     "autorizó el 9 de enero al Catholic Welfare Bureau a emitir exenciones de visa: cartas firmadas por Walsh que las "
     "aerolíneas aceptaban. La autorización era general para niños de 6 a 16 años; para los de 16 a 18 había que "
     "pedir antes una revisión de seguridad."),
    ("FR-PP005", "pedro_pan", "hecho_atribuido", "F026", "p. 8", [], None,
     "Según Cauce, en Cuba los papeles de los niños se movieron por una red clandestina encabezada por la enfermera "
     "británica Penny Powers, que había trabajado en el Kindertransport; muchos de sus miembros fueron detenidos y "
     "cumplieron largas condenas."),
    ("FR-PP006", "pedro_pan", "hecho", "F026", "p. 9", ["F028"], None,
     "Aproximadamente la mitad de los niños de Pedro Pan tenía familiares o amigos en Estados Unidos que los "
     "acogieron; el resto quedó al cuidado de agencias según su religión, y el Catholic Welfare Bureau atendió a algo "
     "más de 7.000."),
    ("FR-PP007", "pedro_pan", "hecho_atribuido", "F028", "texto", [], None,
     "Según Walsh, el 85 por ciento de los 7.000 niños atendidos por su agencia tenía entre 12 y 18 años al llegar, y "
     "el 70 por ciento eran varones mayores de 12."),
    ("FR-PP008", "pedro_pan", "hecho", "F026", "p. 9", ["F028"], None,
     "Los niños de Pedro Pan fueron acogidos en hogares y centros de unas 100 ciudades de 35 estados; en Miami hubo "
     "albergues como el campamento de Matecumbe, con unos 400 varones, y el de Florida City."),
    ("FR-PP009", "pedro_pan", "hecho_atribuido", "F026", "pp. 4-5", ["F028"], None,
     "Según Cauce, los padres querían evitar que sus hijos recibieran adoctrinamiento comunista; entre los hechos que "
     "pesaron cita la campaña de alfabetización y la confiscación de las escuelas privadas y católicas en 1961."),
    ("FR-PP010", "pedro_pan", "hecho", "F031", "introducción", ["F026"], None,
     "El gobierno cubano nunca aprobó una ley para quitar a los padres la patria potestad sobre sus hijos. El rumor de "
     "que lo haría circuló en aquellos años y pesó en la decisión de muchas familias de enviar a sus hijos solos."),
    ("FR-PP011", "pedro_pan", "hecho_atribuido", "F031", "sección sobre el rumor de la patria potestad", [], None,
     "Según la historiadora Deborah Shnookal, citada por Wikipedia, la falsa ley de la patria potestad circuló primero "
     "en Cuba a través de grupos contrarios a Castro y de católicos, y después la amplificó Radio Swan, una emisora "
     "respaldada por la CIA."),
    ("FR-PP012", "pedro_pan", "hecho_atribuido", "F031", "sección sobre la controversia con la CIA", [], None,
     "Según Wikipedia, en 1999 un tribunal federal de Illinois concluyó, tras revisar 733 páginas de documentos de la "
     "CIA, que la evacuación de los niños no fue una operación de la CIA; aun así, varios ex agentes de la CIA "
     "admitieron haber editado, impreso y distribuido copias de la falsa ley."),
    ("FR-PP013", "pedro_pan", "postura", "F032", "introducción", [], "gobierno_cubano",
     "Según EcuRed, la enciclopedia oficial cubana, la Operación Peter Pan fue una operación de subversión organizada "
     "por el Departamento de Estado, la jerarquía católica de Miami, la CIA y organizaciones opuestas al gobierno "
     "revolucionario, que manipuló el tema de la patria potestad; afirma que muchos de los niños nunca volvieron a "
     "encontrarse con sus padres."),
    ("FR-PP014", "pedro_pan", "postura", "F032", "sección 'Contexto histórico'", [], "gobierno_cubano",
     "Según EcuRed, la campaña sobre la patria potestad empezó el 26 de octubre de 1960 en Radio Swan con mensajes "
     "dirigidos a las madres cubanas, y la falsa ley se redactó en Estados Unidos y la introdujo en Cuba José Pujals "
     "Mederos; EcuRed cita a Ángel Fernández Varela, a quien llama agente de la CIA, como uno de sus redactores."),
    ("FR-PP015", "pedro_pan", "postura", "F028", "texto", [], "organizadores_pedro_pan",
     "Según Walsh, su agencia no tenía constancia de ningún niño perdido, ningún menor fue enviado a reformatorios ni "
     "dado en adopción, y la Iglesia en Cuba como institución no participó; considera falsos los informes de que "
     "muchos niños perdieron el contacto con sus familias."),
    ("FR-PP016", "pedro_pan", "hecho_atribuido", "F028", "texto", [], None,
     "Según Walsh, cuando empezaron los Vuelos de la Libertad, el 1 de diciembre de 1965, los padres de los niños de "
     "Pedro Pan tuvieron prioridad, y cerca del 90 por ciento de los que seguían a cargo de su agencia se reunió con "
     "sus padres para junio de 1966."),
    ("FR-PP017", "pedro_pan", "hecho_atribuido", "F028", "texto", [], None,
     "Según Walsh, después de 1965 los retrasos en las reunificaciones se debieron sobre todo a que el gobierno "
     "cubano demoraba la salida de ciertos profesionales y no dejaba salir con sus padres a los varones de 15 a 26 "
     "años por el servicio militar."),
    ("FR-PP018", "pedro_pan", "hecho_atribuido", "F031", "sección sobre la vida en Estados Unidos", [], None,
     "Según Wikipedia, en 1978 el grupo Areíto y Casa de las Américas publicaron 'Contra viento y marea', un libro "
     "de testimonios anónimos de cubanos que salieron de niños, con relatos de soledad, malas condiciones y maltrato "
     "mental, físico y sexual."),
    ("FR-PP019", "pedro_pan", "hecho", "F026", "p. 10", [], None,
     "El programa federal para niños cubanos no acompañados (Cuban Children's Program) siguió atendiendo a niños "
     "llegados de Cuba hasta 1982."),
]

for p in (REG,):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)
if FRAG.exists():
    print(f"{FRAG} ya existe. No toco nada.")
    sys.exit(0)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
ids = {r["id_fuente"] for r in filas}
if any(fu[0] in ids for fu in FUENTES):
    print("Las fuentes F026 en adelante ya están en el registro. No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(REG, REG.with_name(f"{REG.name}.{marca}.bak"))
for fid, titulo, autor, url, tipo, lic, persp, uso, notas in FUENTES:
    filas.append({"id_fuente": fid, "titulo": titulo, "autor_institucion": autor, "url": url, "tipo": tipo,
                  "licencia": lic, "perspectiva": persp, "uso": uso, "fecha_consulta": HOY, "notas": notas})
tmp = REG.with_suffix(".csv.tmp")
with tmp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)
tmp.replace(REG)

with FRAG.open("w", encoding="utf-8", newline="\n") as f:
    for fid, etapa, tipo, fuente, ubic, corr, actor, texto in FRAGMENTOS:
        d = {"id": fid, "etapa": etapa, "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
             "corroborado_por": corr, "texto": texto, "notas": "", "revisado": False, "estado": "pendiente"}
        if actor:
            d["actor"] = actor
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas {len(FUENTES)} fuentes (F026 a F033).")
print(f"Creado {FRAG} con {len(FRAGMENTOS)} fragmentos en 'pendiente'.")
print(f"Ahora: python revisar.py {FRAG}")
