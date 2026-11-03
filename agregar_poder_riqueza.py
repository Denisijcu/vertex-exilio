"""
agregar_poder_riqueza.py — Etapa poder_y_riqueza_castro (módulo "Cuba: contexto").

Registra las fuentes F115-F121 y crea fuentes/fragmentos_poder_riqueza.jsonl (FR-PR001 en adelante):
la estimación de Forbes (2006) y la respuesta de Fidel Castro, el libro del exescolta Juan Reinaldo Sánchez (2014)
con las voces que lo matizan, y el debate de 2025 sobre el dinero de GAESA.

Uso (desde E:\\vertex-exilio):
    python agregar_poder_riqueza.py

Criterios:
  - Forbes es una ESTIMACIÓN con supuestos que la propia revista declara: hecho atribuido, nunca hecho.
  - Lo que cuenta Sánchez es testimonio (campo 'testigo'): no se da por probado.
  - GAESA: la investigación del Miami Herald y la refutación de la economista Emily Morris, cada una atribuida.
  - No entran: la "herencia multimillonaria" de los hijos (no hay fuente seria), datos de familiares sin cargo
    público, la acusación de narcotráfico del libro (está en caso_ochoa con mejores fuentes), "controversial
    dictator" (Forbes), "communist regime" (Rubio) ni los datos de contacto de la ficha editorial.

Qué hace:
  1. Comprueba que validar.py tiene la etapa poder_y_riqueza_castro.
  2. Copia de seguridad del registro (y del archivo de fragmentos si ya existiera).
  3. Añade F115-F121 al registro (si alguna ya existe, no toca nada).
  4. Crea el archivo de fragmentos en estado 'pendiente'.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_poder_riqueza.jsonl")
HOY = "2026-11-03"
T = "poder_y_riqueza_castro"

FB = "Según la revista Forbes, en su lista de 2006 de fortunas de reyes, reinas y dictadores"
GU = "Según The Guardian (Kim Willsher, mayo de 2014), sobre el libro del exescolta Juan Reinaldo Sánchez"
JS = "Según cuenta el exescolta Juan Reinaldo Sánchez en su libro «La vida oculta de Fidel Castro» (2014), recogido por The Guardian"
MH = "Según una investigación del Miami Herald (Nora Gámez Torres, agosto de 2025) basada en 22 estados financieros internos de GAESA"
EM = "Según la economista Emily Morris (University College London), entrevistada por Belly of the Beast en agosto de 2025"

FUENTES = [
    ("F115", "Fortunes of kings, queens and dictators (2006)", "Forbes (publicado por NBC News)",
     "https://www.nbcnews.com/id/wbna12635548", "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/FORBES_2006_fortunas.html. La cifra es una estimación con supuestos que Forbes declara "
     "('more art than science'): siempre atribuida. 'Controversial dictator' es lenguaje de la fuente: no entra."),
    ("F116", "Castro denies $900m fortune claim (16 de mayo de 2006)", "Al Jazeera y agencias",
     "https://www.aljazeera.com/news/2006/5/16/castro-denies-900m-fortune-claim", "periodistica", "revisar",
     "ninguna", "ambos",
     "Archivo fuentes/docs/ALJAZEERA_2006_castro_forbes.html. Lo que dicen Castro y Soberón: postura del gobierno cubano."),
    ("F117", "Castro dice que renunciará si hallan pruebas de su supuesta fortuna (16 de mayo de 2006)",
     "EFE (publicado por Infobae)",
     "https://www.infobae.com/2006/05/16/255110-castro-dice-que-renunciara-si-hallan-pruebas-su-supuesta-fortuna/",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/EFE_2006_castro_forbes.html. Citas de Castro en español: postura."),
    ("F118", "Fidel Castro 'lived like a king', new book claims (The Guardian, 21 de mayo de 2014)",
     "Kim Willsher, The Guardian (copia en The Cuban Economy)", "https://thecubaneconomy.com/?p=4419",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/GUARDIAN_2014_sanchez.html (copia íntegra del artículo del Guardian; el original no se pudo "
     "descargar). Lo que cuenta Sánchez: testimonio. Recoge también voces que lo matizan (Bardach, Ramonet)."),
    ("F119", "La vida oculta de Fidel Castro (ficha editorial, 21 de octubre de 2014)", "Ediciones Península (Grupo Planeta)",
     "https://proapi.planetadelibros.com/descargas/sala-prensa-libro/sinopsis-y-biografia/167881/la-vida-oculta-de-fidel-castro.pdf",
     "secundaria", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/PENINSULA_2014_sinopsis.pdf. Texto promocional de la editorial: solo se usan los datos "
     "biográficos de los autores. Los datos de contacto de prensa no entran."),
    ("F120", "Where is Cuba's money? Secret records show military conglomerate GAESA is flush with cash (6 de agosto de 2025)",
     "Nora Gámez Torres, Miami Herald (publicado por Yahoo Finance)",
     "https://finance.yahoo.com/news/where-cuba-money-secret-records-093000858.html", "periodistica", "revisar",
     "ninguna", "ambos",
     "Archivo fuentes/docs/HERALD_2025_gaesa.html. Documentos filtrados que el Herald no publicó íntegros; su "
     "interpretación la discute F121. 'Shadow government' y similares: atribuidos."),
    ("F121", "Is Cuba's Military Really Holding Billions Overseas? An interview with economist Emily Morris (27 de agosto de 2025)",
     "Belly of the Beast", "https://www.bellyofthebeastcuba.com/cuba-military-gaesa-billions-claim-debunked",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/BOTB_2025_gaesa.html. Entrevista: lo que dice Morris va como postura de la economista."),
]

NUEVOS = [
    # ================= Forbes 2006
    dict(id="FR-PR001", tipo="hecho_atribuido", id_fuente="F115", ubicacion="Párrafos 1-2 y apartado sobre Castro",
         texto=f"{FB}, la fortuna de Fidel Castro se estimaba en 900 millones de dólares; para calcularla, la revista "
               "asumió que Castro tenía el control económico de una red de empresas estatales, como el Palacio de "
               "Convenciones, la corporación comercial Cimex y Medicuba, valoró esas empresas y supuso que una parte de "
               "sus ganancias iba a Castro; la propia revista advierte que estas estimaciones son «más arte que ciencia»."),
    dict(id="FR-PR002", tipo="hecho_atribuido", id_fuente="F115", ubicacion="Apartado sobre Castro y párrafo final",
         texto=f"{FB}, exfuncionarios cubanos aseguraban que Castro se quedaba desde hacía años con ganancias de esas "
               "empresas y había rumores de cuentas en Suiza, pero la revista no los contó en su cálculo; Forbes explica "
               "que hace una lista aparte para gobernantes por la dificultad de separar su fortuna personal de la riqueza "
               "del Estado, y recoge que Castro insistía en que su patrimonio personal era cero."),
    dict(id="FR-PR003", tipo="hecho_atribuido", id_fuente="F116", ubicacion="Párrafos 2 y 7",
         texto="Según Al Jazeera (mayo de 2006), la estimación de Forbes sobre Castro era casi el doble de la que daba para la "
               "reina Isabel II, 500 millones de dólares; en 2005 Forbes le había atribuido 550 millones, y Castro había "
               "amenazado entonces con demandar a la revista."),
    dict(id="FR-PR004", tipo="postura", id_fuente="F117", ubicacion="Párrafos 1-6", actor="gobierno_cubano",
         texto="Según EFE, Fidel Castro respondió a Forbes el 15 de mayo de 2006 en un programa de televisión de unas cuatro "
               "horas y media: «Si ellos prueban que yo tengo una cuenta en el exterior de 900 millones de dólares o de un "
               "dólar, yo renuncio ahora a todas las funciones que estoy desempeñando»; retó a la revista con «búsquenme un "
               "testaferro, una cuenta, búsquenme un dólar», la llamó «libelo» y dijo que era ridículo atribuirle «una "
               "fortuna sin herederos»."),
    dict(id="FR-PR005", tipo="postura", id_fuente="F116", ubicacion="Párrafos 4-6", actor="gobierno_cubano",
         texto="Según Al Jazeera, Fidel Castro llamó a la información de Forbes una «calumnia repugnante», dijo que su "
               "patrimonio era nulo y que ganaba 900 pesos cubanos al mes, unos 40 dólares."),
    dict(id="FR-PR006", tipo="postura", id_fuente="F117", ubicacion="Párrafo 7", actor="gobierno_cubano",
         texto="Según EFE, el presidente del Banco Central de Cuba, Francisco Soberón, calificó de «burdas y ridículas» las "
               "fórmulas de Forbes y afirmó que en la economía centralizada cubana «es totalmente imposible» que un "
               "dirigente pueda tener cuentas personales en el exterior."),
    dict(id="FR-PR007", tipo="cifra_disputada", id_fuente="F115", ubicacion="Apartado sobre Castro (F115); párrafo 4 (F116)",
         corroborado_por=["F116"],
         texto="La fortuna personal de Fidel Castro se da de forma opuesta: Forbes la estimó en 2006 en 900 millones de "
               "dólares, con supuestos sobre empresas estatales, mientras que Castro afirmó que su patrimonio era nulo y "
               "retó a probar que tuviera un solo dólar en el exterior."),
    # ================= el libro de Juan Reinaldo Sánchez
    dict(id="FR-PR008", tipo="hecho_atribuido", id_fuente="F119", ubicacion="Biografía de los autores",
         texto="Según la editorial Ediciones Península, el teniente coronel Juan Reinaldo Sánchez (La Habana, 1949 - Miami, "
               "2015) fue escolta personal de Fidel Castro entre 1977 y 1994; al anunciar su retiro fue detenido y estuvo "
               "preso hasta 1996, y en 2008, tras diez intentos fallidos, salió de Cuba hacia Miami; escribió el libro con "
               "el periodista francés Axel Gyldén, del semanario L'Express."),
    dict(id="FR-PR009", tipo="testimonio", id_fuente="F118", ubicacion="Párrafos 6-8 y 24", testigo="Juan Reinaldo Sánchez",
         texto=f"{JS}, Fidel Castro «nunca renunció a las comodidades capitalistas ni eligió vivir en la austeridad», y su "
               "estilo de vida era un «privilegio loco» mientras los cubanos pasaban grandes penurias en los años noventa."),
    dict(id="FR-PR010", tipo="testimonio", id_fuente="F118", ubicacion="Párrafos 16-18", testigo="Juan Reinaldo Sánchez",
         texto=f"{JS}, Castro tenía una isla privada, Cayo Piedra, al sur de Bahía de Cochinos, que el exescolta describe como un «jardín "
               "del Edén», donde recibía a invitados como Gabriel García Márquez; viajaba a ella en el yate Aquarama II, con "
               "madera de Angola y cuatro motores enviados por Leonid Brezhnev, y tenía además una gran finca en La Habana y "
               "un bungaló con marina privada en la costa."),
    dict(id="FR-PR011", tipo="testimonio", id_fuente="F118", ubicacion="Párrafos 25-26 y 31", testigo="Juan Reinaldo Sánchez",
         texto=f"{JS}, Castro tuvo al menos nueve hijos, algo que la prensa cubana tenía prohibido mencionar, nunca iba a "
               "ninguna parte sin al menos 10 escoltas, entre ellos dos «donantes de sangre», y guardaba diamantes de Angola "
               "en una caja de tabacos Cohiba."),
    dict(id="FR-PR012", tipo="testimonio", id_fuente="F118", ubicacion="Párrafo 9", testigo="Juan Reinaldo Sánchez",
         texto=f"{JS}, cuando pidió retirarse cayó en desgracia, fue tachado de traidor, encarcelado «como un perro», "
               "torturado y encerrado en una celda llena de cucarachas."),
    dict(id="FR-PR013", tipo="hecho_atribuido", id_fuente="F118", ubicacion="Párrafos 11-12",
         texto=f"{GU}, el coautor del libro, Axel Gyldén, admitió que Sánchez tenía cuentas pendientes con Castro, pero "
               "aseguró que había comprobado su historia, y dijo que era la primera vez que alguien del círculo íntimo de "
               "Castro hablaba."),
    dict(id="FR-PR014", tipo="postura", id_fuente="F118", ubicacion="Párrafos 20-23", actor="Ann Louise Bardach (periodista)",
         texto=f"{GU}, la periodista Ann Louise Bardach, que entrevistó a Castro, sostuvo que tenía la mejor comida y atención "
               "médica pero no un estilo de vida lujoso, que «no lo hizo por dinero» y que su casa cerca de La Habana tenía "
               "cuatro habitaciones, propia de la clase media o media alta en Occidente; para ella, lo importante era otra "
               "cosa: «Es el dueño de la isla de Cuba»."),
    dict(id="FR-PR015", tipo="hecho_atribuido", id_fuente="F118", ubicacion="Párrafo 15",
         texto=f"{GU}, visitantes como el periodista francés Ignacio Ramonet, que entrevistó largamente a Castro, describieron "
               "un estilo de vida austero, de lectura, ejercicio, comidas sencillas y comodidades modestas."),
    # ================= GAESA
    dict(id="FR-PR016", tipo="hecho_atribuido", id_fuente="F120", ubicacion="Párrafos 4, 12-13 y 27",
         texto=f"{MH}, de marzo y agosto de 2024, las empresas del conglomerado militar GAESA, sin contar Cimex, tenían en "
               "marzo de 2024 activos por 18.000 millones de dólares fácilmente convertibles en efectivo, 14.500 millones "
               "de ellos en cuentas bancarias, más que las reservas internacionales de países como Costa Rica, Uruguay o "
               "Panamá; el conglomerado completo declaró 7.200 millones de dólares de beneficio neto en los primeros ocho "
               "meses de 2023."),
    dict(id="FR-PR017", tipo="hecho_atribuido", id_fuente="F120", ubicacion="Párrafos 18-19 y 37",
         texto=f"{MH}, el economista Pavel Vidal estimó que los beneficios brutos de GAESA en 2023 equivalían a cerca del 40 % "
               "del PIB oficial y la describió como «un gobierno paralelo que no rinde cuentas»; la contralora general Gladys "
               "Bejerano, que había dicho a EFE que no podía auditar a GAESA, fue destituida poco después sin explicación."),
    dict(id="FR-PR018", tipo="hecho_atribuido", id_fuente="F120", ubicacion="Párrafos 47-48",
         texto=f"{MH}, GAESA está supervisada por el Departamento V de las fuerzas armadas, y hasta su muerte en 2022 la dirigió "
               "el general Luis Alberto Rodríguez López-Calleja, exyerno de Raúl Castro; desde entonces la dirige la "
               "general de brigada Ania Guillermina Lastres Morera, sin vínculos familiares conocidos con los Castro."),
    dict(id="FR-PR019", tipo="hecho_atribuido", id_fuente="F120", ubicacion="Párrafos 60-62",
         texto=f"{MH}, el valor en dólares de parte de los activos depende del tipo de cambio: 234.000 millones de pesos "
               "equivalían a 9.800 millones de dólares al cambio oficial de 24 pesos por dólar, pero a solo 632 millones al "
               "cambio informal de unos 370 pesos."),
    dict(id="FR-PR020", tipo="postura", id_fuente="F120", ubicacion="Párrafos 26 y 65-66", actor="gobierno_cubano",
         texto=f"{MH}, la Contraloría y la cancillería cubanas no respondieron a sus preguntas, y en marzo de 2025 Díaz-Canel "
               "dijo que los problemas de Cuba «no se deben a mala gestión del gobierno» sino a que «no hemos tenido el "
               "dinero» durante años para mantener las termoeléctricas."),
    dict(id="FR-PR021", tipo="postura", id_fuente="F121", ubicacion="Respuestas 1-3", actor="Emily Morris (economista)",
         texto=f"{EM}, no está nada claro que GAESA tenga 18.000 millones de dólares: el Herald no publicó los documentos, no se "
               "sabe con certeza si son auténticos, y el encabezado del único estado financiero visible indica que todo está "
               "en pesos cubanos; si es así, los activos serían 17.900 millones de pesos, unos 746 millones de dólares, y lo "
               "depositado en bancos, unos 603 millones."),
    dict(id="FR-PR022", tipo="postura", id_fuente="F121", ubicacion="Respuestas 4-6", actor="Emily Morris (economista)",
         texto=f"{EM}, los documentos muestran activos de GAESA pero no que se le quite dinero al Estado ni prueban corrupción, "
               "y si hubiera una fortuna así se vería una clase de funcionarios muy ricos o un ejército muy bien equipado; "
               "Morris admite que la falta de transparencia es un riesgo real de corrupción."),
    dict(id="FR-PR023", tipo="hecho_atribuido", id_fuente="F121", ubicacion="Respuestas 1 y 5",
         texto=f"{EM}, GAESA se creó en los años noventa, durante el Período Especial, para que militares formados en gestión "
               "dirigieran empresas estatales, y las reservas internacionales de Cuba son secreto oficial, por lo que "
               "incluso la Economist Intelligence Unit tenía que estimarlas."),
    dict(id="FR-PR024", tipo="cifra_disputada", id_fuente="F120", ubicacion="Párrafo 13 (F120); respuesta 2 (F121)",
         corroborado_por=["F121"],
         texto="Los activos de GAESA en marzo de 2024 se dan de forma muy distinta: el Miami Herald los calcula en 18.000 "
               "millones de dólares, con 14.500 millones en bancos, y la economista Emily Morris sostiene que esas cifras "
               "son pesos y equivalen a unos 746 millones de dólares, con 603 millones en bancos."),
]

for p in (REG, Path("validar.py")):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)
if f'"{T}"' not in Path("validar.py").read_text(encoding="utf-8"):
    print(f"validar.py no tiene la etapa {T}. Corre primero: python agregar_etapas_contexto.py")
    sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
ya = {r["id_fuente"] for r in filas}
if any(fu[0] in ya for fu in FUENTES):
    print(f"Alguna de las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]} ya está en el registro. No toco nada.")
    sys.exit(0)

lineas = []
if FRAG.exists():
    with FRAG.open(encoding="utf-8-sig") as f:
        lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n["id"] for n in NUEVOS if n["id"] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(REG, REG.with_name(f"{REG.name}.{marca}.bak"))
if FRAG.exists():
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
        d = {"id": n["id"], "etapa": T, "tipo": n["tipo"], "id_fuente": n["id_fuente"],
             "ubicacion": n["ubicacion"], "corroborado_por": n.get("corroborado_por", []), "texto": n["texto"],
             "notas": "", "revisado": False, "estado": "pendiente"}
        if n.get("actor"):
            d["actor"] = n["actor"]
        if n.get("testigo"):
            d["testigo"] = n["testigo"]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]}.")
print(f"Añadidos {len(NUEVOS)} fragmentos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
