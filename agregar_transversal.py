"""
agregar_transversal.py — Abre la etapa transversal (identidad, cultura, generaciones, remesas y relación
del gobierno cubano con sus emigrados): registra las fuentes F061-F066 y crea
fuentes/fragmentos_transversal.jsonl.

Uso (desde E:\\vertex-exilio):
    python agregar_transversal.py

Documentos leídos (en fuentes/docs): PEW_2026.html, WIKI_cubanoamericanos.html, WIKI_pequena_habana.html,
WIKI_remesas_cuba.html (Economy of Cuba), ONCUBA_remesas.html, ONCUBA_nacion_emigracion.html.
La sección va en 'ubicacion'.

Qué hace:
  1. Copia de seguridad del registro.
  2. Añade F061-F066 al registro (si ya existen, no hace nada).
  3. Crea fuentes/fragmentos_transversal.jsonl con todos los fragmentos en 'pendiente'
     (si el archivo ya existe, no lo toca).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_transversal.jsonl")
HOY = "2026-10-30"
ETAPA = "transversal"

FUENTES = [
    ("F061", "10 facts about Cubans in the U.S. (7 de mayo de 2026)", "Pew Research Center",
     "https://www.pewresearch.org/short-reads/2026/05/07/10-facts-about-cubans-in-the-u-s/", "academica", "revisar",
     "academica", "hechos",
     "Archivo fuentes/docs/PEW_2026.html (guardado desde Chrome). Datos del censo (ACS 2024) y encuestas de Pew de "
     "2020 y 2025. La copia guardada llega hasta el dato 8 de los 10. Su edad mediana (38,2) es de toda la población "
     "de origen cubano; la del MPI (55) es solo de los nacidos en Cuba: no se contradicen."),
    ("F062", "Cuban Americans", "Wikipedia", "https://en.wikipedia.org/wiki/Cuban_Americans", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_cubanoamericanos.html (guardado desde Chrome el 2026-10-30). Las cifras de censo de "
     "la sección Demographics están mezcladas y no se usan. La afirmación de Foreign Policy sobre el 6 de enero no "
     "se usa. Expresiones como 'Castro regime' no entran. Da 75 % para Bush en 2000; el artículo de Elián (F053) "
     "da 80 %: cifra disputada."),
    ("F063", "Little Havana", "Wikipedia", "https://en.wikipedia.org/wiki/Little_Havana", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_pequena_habana.html (guardado desde Chrome el 2026-10-30). 'Castro regime' y "
     "'counter-revolutionary' no entran sin atribución."),
    ("F064", "Economy of Cuba", "Wikipedia", "https://en.wikipedia.org/wiki/Economy_of_Cuba", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_remesas_cuba.html (guardado desde Chrome el 2026-10-30). Casi no trata las remesas; "
     "solo se usan datos generales. Una afirmación sobre '20.000 mercenarios' no tiene apoyo y no se usa."),
    ("F065", "Foreign Ministry regrets suspension of remittances to Cuba through Western Union (11 de febrero de 2025)",
     "OnCuba News (con despacho de EFE)",
     "https://oncubanews.com/en/cuba-usa/foreign-ministry-regrets-suspension-of-remittances-to-cuba-through-western-union-it-was-coming",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/ONCUBA_remesas.html. Medio con redacción en La Habana y Miami. Los hechos van atribuidos; "
     "las declaraciones de la cancillería cubana y de Rubio = postura de cada gobierno. El comentario de un lector "
     "al pie de la página no se usa."),
    ("F066", "Cuban Government announces 4th The Nation and Emigration Conference (12 de diciembre de 2019)",
     "OnCuba News", "https://oncubanews.com/en/cuba/cuban-government-announces-4th-the-nation-and-emigration-conference",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/ONCUBA_nacion_emigracion.html. Recoge la convocatoria oficial (postura del gobierno "
     "cubano) y los puntos de controversia con la emigración. La nota anuncia la conferencia para abril de 2020; "
     "no confirma si se hizo en esa fecha."),
]

# (id, tipo, fuente, ubicación, corroborado_por, actor, texto)
FRAGMENTOS = [
    # ---------------- antes de 1959
    ("FR-T001", "hecho_atribuido", "F062", "Early migrations", [], None,
     "Según Wikipedia, la presencia cubana en lo que hoy es Estados Unidos viene de la época colonial: la Florida "
     "española dependía de la Capitanía General de Cuba, y en 1565 cientos de soldados españoles y sus familias "
     "salieron de Cuba para fundar San Agustín."),
    ("FR-T002", "hecho_atribuido", "F062", "Early migrations", [], None,
     "Según Wikipedia, en 1870 había casi 12.000 inmigrantes cubanos en Estados Unidos, unos 4.500 en Nueva York, "
     "3.000 en Nueva Orleans y 2.000 en Cayo Hueso, y la emigración de esa época tenía causas económicas y políticas."),
    ("FR-T003", "hecho_atribuido", "F062", "Key West and Tampa, Florida", [], None,
     "Según Wikipedia, en el siglo XIX muchos tabaqueros cubanos se instalaron en Cayo Hueso, y en 1885 Vicente "
     "Martínez Ybor trasladó su fábrica de tabacos a Tampa, donde fundó Ybor City; Tampa pasó de unos 1.000 "
     "habitantes en 1885 a más de 16.000 en 1900."),
    ("FR-T004", "hecho_atribuido", "F062", "Key West and Tampa, Florida", [], None,
     "Según Wikipedia, los cubanos de Ybor City y West Tampa apoyaron con dinero, equipos y a veces con su vida la "
     "independencia de Cuba, inspirados por José Martí, que visitó la Florida varias veces."),
    ("FR-T005", "hecho_atribuido", "F062", "Other early waves (1900–1959)", [], None,
     "Según Wikipedia, entre 1900 y 1959 llegaron a Estados Unidos unos 100.000 cubanos, sobre todo por razones "
     "económicas, aunque también había opositores a Batista; en 1958 había registrados unos 125.000 cubanos y "
     "descendientes, y más de 50.000 se quedaron después de 1959."),
    ("FR-T006", "hecho_atribuido", "F062", "Food and drink", [], None,
     "Según Wikipedia, el sándwich cubano se creó y se estandarizó entre los tabaqueros que iban y venían entre Cuba "
     "y la Florida, sobre todo en Ybor City, alrededor del cambio del siglo XIX al XX."),
    # ---------------- después de 1959 y generaciones
    ("FR-T007", "hecho_atribuido", "F062", "Post-1959 revolution", [], None,
     "Según Wikipedia, entre 1960 y 1980 emigró alrededor de un millón de cubanos, cerca del 10 % de la población de "
     "la isla, y el 85 % fue a Estados Unidos."),
    ("FR-T008", "hecho_atribuido", "F061", "dato 3", [], None,
     "Según Pew Research, unos 250.000 cubanos llegaron a Estados Unidos en los años sesenta, tras la Revolución, y "
     "otros 250.000 en los setenta; en los ochenta llegaron, entre otros, los 125.000 del Mariel."),
    ("FR-T009", "hecho_atribuido", "F062", "Post-1959 revolution", [], None,
     "Según Wikipedia, el Programa de Refugiados Cubanos dio más de 1.300 millones de dólares en ayuda directa, y "
     "los recién llegados también podían recibir asistencia pública, clases de inglés gratis, becas y préstamos "
     "universitarios con intereses bajos."),
    ("FR-T010", "hecho_atribuido", "F062", "Post-1959 revolution", [], None,
     "Según Wikipedia, algunos bancos dieron préstamos a exiliados que no tenían garantías ni historial de crédito, "
     "lo que permitió abrir negocios; Miami y Union City, en Nueva Jersey, apodada 'La Habana del Hudson', se "
     "convirtieron en los principales centros de la cultura cubanoamericana."),
    ("FR-T011", "hecho_atribuido", "F063", "History", [], None,
     "Según Wikipedia, la Pequeña Habana surgió en los años sesenta en un barrio de Miami que en los años treinta "
     "había sido de clase media baja y con mucha población judía; los cubanos que llegaban pensaban que su estancia "
     "sería temporal, y para 1970 el barrio era cubano en más de un 85 %."),
    ("FR-T012", "hecho_atribuido", "F063", "Cuban solidification, Contemporary population", [], None,
     "Según Wikipedia, cuando quedó claro que no volverían pronto, los cubanos se asentaron en otros barrios de "
     "Miami, y la proporción de cubanos entre los hispanos de la Pequeña Habana bajó del 84 % en 1979 al 58 % en "
     "1989, con la llegada de nicaragüenses, hondureños y otros centroamericanos, aunque la mayoría de los negocios "
     "seguía en manos cubanas."),
    ("FR-T013", "hecho_atribuido", "F062", "Immigration policy", [], None,
     "Según Wikipedia, los cubanoamericanos de segunda generación se fueron mudando de barrios como la Pequeña "
     "Habana a zonas residenciales como Westchester, y esos barrios pasaron a ser habitados por inmigrantes de "
     "otros países latinoamericanos."),
    ("FR-T014", "hecho_atribuido", "F063", "introducción, Viernes Culturales", [], None,
     "Según Wikipedia, la Pequeña Habana es conocida por la Calle Ocho, el Parque del Dominó (Parque Máximo Gómez), "
     "el Festival de la Calle Ocho, los Viernes Culturales y un paseo de la fama con artistas como Celia Cruz, "
     "Gloria Estefan y Willy Chirino; en 2017 el National Trust for Historic Preservation la declaró tesoro nacional."),
    ("FR-T015", "hecho_atribuido", "F062", "Mid-1990s to 2000s", [], None,
     "Según Wikipedia, en 2008 Jorge Ferragut, fundador de Casa Cuba, una agencia que ayudaba a inmigrantes cubanos "
     "en Texas, dijo que muchos cubanos que llegaron en la primera década del siglo XXI se habían ido por razones "
     "económicas más que políticas."),
    # ---------------- identidad, idioma, religión, cultura
    ("FR-T016", "hecho_atribuido", "F062", "Language", [], None,
     "Según Wikipedia, el 89 % de los cubanoamericanos mayores de 18 años habla en casa un idioma distinto del "
     "inglés, cerca del 60 % domina el inglés y el 36 % se considera bilingüe; usar el español en casa se relaciona "
     "con el deseo de conservar la herencia cultural."),
    ("FR-T017", "hecho_atribuido", "F062", "infobox, Religion", [], None,
     "Según Wikipedia, cerca del 49 % de los cubanoamericanos es católico, un 16 % protestante y un 26 % no tiene "
     "religión, y algunos practican religiones sincréticas de origen africano como la santería o Ifá."),
    ("FR-T018", "hecho_atribuido", "F062", "Beverages", [], None,
     "Según Wikipedia, el café cubano es central en la comunidad: el cafecito o colada, el cortadito (mitad leche, "
     "mitad café) y el café con leche, y refrescos de origen cubano como Materva o Jupiña se siguen produciendo en Miami."),
    ("FR-T019", "hecho_atribuido", "F062", "Assimilation", [], None,
     "Según Wikipedia, en los últimos años creció mucho el interés de los cubanoamericanos por la genealogía, como "
     "forma de conservar sus raíces cubanas mientras adoptan la cultura estadounidense."),
    # ---------------- cifras de hoy (Pew 2026)
    ("FR-T020", "hecho", "F061", "dato 1", ["F062"], None,
     "Los cubanos son el tercer grupo hispano más grande de Estados Unidos, después de los mexicanos y los "
     "puertorriqueños; según Pew Research, en 2024 había 2,9 millones de personas de origen cubano, un 23 % más que en 2019."),
    ("FR-T021", "hecho_atribuido", "F061", "dato 2", [], None,
     "Según Pew Research, en 2024 el 57 % de las personas de origen cubano en Estados Unidos (1,7 millones) había "
     "nacido fuera del país."),
    ("FR-T022", "hecho_atribuido", "F061", "dato 4", [], None,
     "Según Pew Research, antes de 2017 casi no había inmigrantes cubanos indocumentados en Estados Unidos, pero en "
     "julio de 2023 se calculaban 475.000, y al menos 250.000 más entraron hasta finales de 2024."),
    ("FR-T023", "hecho_atribuido", "F061", "dato 6", [], None,
     "Según Pew Research, el 61 % de los cubanos de Estados Unidos (1,8 millones) vive en la Florida y el 8 % en Texas; "
     "el área de Miami concentra el 42 % (1,2 millones), y le siguen Tampa (177.000), Nueva York (153.000) y "
     "Houston (107.000)."),
    ("FR-T024", "hecho_atribuido", "F061", "dato 7", [], None,
     "Según Pew Research, los cubanos son el grupo hispano de mayor edad en Estados Unidos, con una edad mediana de "
     "38,2 años frente a 30,2 del conjunto de hispanos, por la llegada de inmigrantes mayores y una fecundidad baja."),
    ("FR-T025", "hecho_atribuido", "F061", "dato 8", [], None,
     "Según Pew Research, los cubanos nacidos en Cuba tienen menos probabilidades que el conjunto de los "
     "estadounidenses de tener un título universitario, mientras que los cubanos nacidos en Estados Unidos tienen "
     "más probabilidades."),
    ("FR-T026", "cifra_disputada", "F061", "dato 1", ["F062"], None,
     "El total de personas de origen cubano en Estados Unidos varía según la fuente y el año: Pew Research da 2,9 "
     "millones en 2024 y Wikipedia da 3.082.802 en 2025."),
    # ---------------- política (solo datos atribuidos)
    ("FR-T027", "hecho_atribuido", "F061", "dato 5", [], None,
     "Según Pew Research, históricamente los cubanoamericanos se han identificado como republicanos más que el "
     "conjunto de los hispanos, aunque ese apoyo se ha suavizado en algunos momentos."),
    ("FR-T028", "hecho_atribuido", "F061", "dato 5", [], None,
     "Según una encuesta de Pew Research de octubre de 2025, el 40 % de los cubanoamericanos aprobaba la política "
     "migratoria del gobierno de Trump, frente al 21 % del conjunto de hispanos, y el 47 % temía que ellos o alguien "
     "cercano fuera deportado, frente al 52 % de los hispanos."),
    ("FR-T029", "hecho_atribuido", "F062", "Politics", [], None,
     "Según Wikipedia, el fracaso de Bahía de Cochinos en 1961 hizo que muchos exiliados desconfiaran del Partido "
     "Demócrata y se acercaran al Partido Republicano en la Florida, aunque en Nueva Jersey los congresistas "
     "cubanoamericanos han sido sobre todo demócratas, como Albio Sires y Bob Menéndez."),
    ("FR-T030", "hecho_atribuido", "F062", "Politics", [], None,
     "Según Wikipedia, en 2008 Barack Obama obtuvo el 47 % del voto cubanoamericano en la Florida, y según encuestas "
     "a pie de urna de Bendixen el 84 % de los votantes cubanoamericanos de Miami-Dade de 65 años o más apoyó a John "
     "McCain, mientras que el 55 % de los menores de 30 apoyó a Obama."),
    ("FR-T031", "hecho_atribuido", "F062", "Politics", [], None,
     "Según Wikipedia, en la encuesta Cuba Poll de FIU de 2024 el 68 % de los probables votantes cubanoamericanos de "
     "Miami-Dade apoyaba a Donald Trump y el 55 % estaba a favor de mantener el embargo, mientras que los más "
     "jóvenes y nacidos en Estados Unidos estaban más divididos."),
    ("FR-T032", "cifra_disputada", "F062", "Politics", ["F053"], None,
     "El porcentaje del voto cubanoamericano de la Florida que obtuvo George W. Bush en 2000 varía según la fuente: "
     "el artículo de Wikipedia sobre los cubanoamericanos da el 75 % y el artículo sobre Elián González, citando "
     "encuestas de 2001, da el 80 %."),
    # ---------------- remesas
    ("FR-T033", "hecho_atribuido", "F065", "texto", [], None,
     "Según OnCuba, en febrero de 2025 Western Union suspendió indefinidamente el envío de remesas a Cuba por un "
     "cambio en las regulaciones de sanciones de Estados Unidos, después de que la empresa Orbit, que procesaba las "
     "remesas en la isla, fuera incluida en la lista de entidades restringidas."),
    ("FR-T034", "hecho_atribuido", "F065", "texto", [], None,
     "Según OnCuba, con información de EFE, Western Union había reanudado el servicio a Cuba en mayo de 2024, después "
     "de suspenderlo en 2020, cuando Estados Unidos restringió a Fincimex, la entidad anterior, por pertenecer al "
     "conglomerado GAESA, controlado por las Fuerzas Armadas cubanas."),
    ("FR-T035", "postura", "F065", "texto", [], "gobierno_eeuu",
     "Según OnCuba, el secretario de Estado Marco Rubio afirmó que Orbit actúa para las fuerzas militares cubanas o en "
     "su nombre; la declaración oficial cubana no lo confirmó ni lo negó."),
    ("FR-T036", "postura", "F065", "texto", [], "gobierno_cubano",
     "Según OnCuba, la cancillería cubana lamentó la suspensión, dijo que afectaría a 'incontables familias' y la "
     "atribuyó a lo que llamó una política de línea dura irracional del gobierno de Estados Unidos, y aseguró que "
     "la decisión 'se veía venir'."),
    ("FR-T037", "hecho_atribuido", "F065", "texto", [], None,
     "Según OnCuba, las remesas son un aporte fundamental para una parte de la población cubana en medio de la "
     "crisis económica y energética, aunque desde hace años una gran parte de ese dinero se mueve por canales "
     "informales."),
    ("FR-T038", "hecho_atribuido", "F064", "Modern Cuban economy (2021–present)", [], None,
     "Según Wikipedia, la pandemia de 2020-2022 provocó caídas bruscas de las remesas y del turismo en Cuba, y el "
     "PIB cubano cayó más de un 10 % entre 2018 y 2024."),
    # ---------------- el gobierno cubano y la emigración
    ("FR-T039", "hecho_atribuido", "F066", "texto", [], None,
     "Según OnCuba, en diciembre de 2019 el presidente Miguel Díaz-Canel convocó la IV Conferencia 'La Nación y la "
     "Emigración' para el 8 al 10 de abril de 2020 en La Habana, en continuidad con los primeros diálogos entre el "
     "gobierno y emigrados de 1978."),
    ("FR-T040", "postura", "F066", "texto", [], "gobierno_cubano",
     "Según la convocatoria oficial recogida por OnCuba, el gobierno cubano dijo que la conferencia tendría un "
     "significado especial para los jóvenes nacidos fuera de Cuba que se identifican con el país de sus padres y "
     "abuelos, y presentó el acercamiento a los emigrados como algo natural e inevitable."),
    ("FR-T041", "hecho_atribuido", "F066", "texto", [], None,
     "Según OnCuba, en los años anteriores el gobierno cubano eliminó la 'habilitación' del pasaporte para los "
     "emigrados que viajaban a la isla, permitió entrar a quienes habían salido ilegalmente, salvo los que salieron "
     "por la base de Guantánamo, y dejó de exigir aprobación para que los hijos de cubanos nacidos fuera obtuvieran "
     "la ciudadanía."),
    ("FR-T042", "hecho_atribuido", "F066", "texto", [], None,
     "Según OnCuba, seguían abiertos varios puntos de controversia con la emigración: su reclamo de tener más "
     "presencia en la economía, la inversión y la vida política, el costo y los trámites del pasaporte, y la pérdida "
     "de la residencia y la ciudadanía cubanas; además, el gobierno se reunía sobre todo con emigrados que no tenían "
     "una posición abiertamente contraria a él."),
    ("FR-T043", "postura", "F066", "texto", [], "gobierno_cubano",
     "Según OnCuba, las autoridades cubanas reconocen unas 166 organizaciones de cubanos residentes en 79 países que "
     "defienden la soberanía de Cuba y se pronuncian contra el embargo de Estados Unidos, que el gobierno cubano "
     "llama bloqueo."),
]

if not REG.exists():
    print(f"No encuentro {REG}. ¿Estás en E:\\vertex-exilio? No toco nada.")
    sys.exit(1)
if FRAG.exists():
    print(f"{FRAG} ya existe. No toco nada.")
    sys.exit(0)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
ids = {r["id_fuente"] for r in filas}
if any(fu[0] in ids for fu in FUENTES):
    print("Las fuentes F061 en adelante ya están en el registro. No toco nada.")
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
    for fid, tipo, fuente, ubic, corr, actor, texto in FRAGMENTOS:
        d = {"id": fid, "etapa": ETAPA, "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
             "corroborado_por": corr, "texto": texto, "notas": "", "revisado": False, "estado": "pendiente"}
        if actor:
            d["actor"] = actor
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas {len(FUENTES)} fuentes (F061 a F066).")
print(f"Creado {FRAG} con {len(FRAGMENTOS)} fragmentos en 'pendiente'.")
print(f"Ahora: python revisar.py {FRAG}")
