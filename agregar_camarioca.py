"""
agregar_camarioca.py — Abre la etapa de Camarioca y los Vuelos de la Libertad (1965-1973):
registra las fuentes F034-F039 y crea fuentes/fragmentos_camarioca_vuelos.jsonl.

Uso (desde E:\\vertex-exilio):
    python agregar_camarioca.py

Documentos leídos (en fuentes/docs): FRUS_1964-68_v32_d308.html, CAMARIOCA1965.pdf,
LARZELERE_MARIEL_BOATLIFT.pdf (F007), b-164031(3)-095487.pdf (GAO, F030),
"Camarioca crisis in 1965.html" (Suiza), WIKI_freedom_flights.html, CAMARIOCA-cubaNet.md,
CASTRO_discurso_3oct1965.html. La página o sección va en 'ubicacion'.

Qué hace:
  1. Copia de seguridad del registro.
  2. Añade F034-F039 al registro (si ya existen, no hace nada).
  3. Crea fuentes/fragmentos_camarioca_vuelos.jsonl con todos los fragmentos en 'pendiente'
     (si el archivo ya existe, no lo toca).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_camarioca_vuelos.jsonl")
HOY = "2026-10-30"
ETAPA = "camarioca_vuelos_libertad"

FUENTES = [
    ("F034", "The 'Other' Boatlift: Camarioca, Cuba, 1965", "US Coast Guard Historian's Office (copia en media.defense.gov)",
     "https://media.defense.gov/2020/Jul/02/2002356759/0/0/0/CAMARIOCA1965.PDF", "primaria",
     "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/CAMARIOCA1965.pdf (18 págs., casi todo fotos). Datos = hechos; 'journey to freedom' "
     "y expresiones parecidas no entran."),
    ("F035", "Foreign Relations of the United States, 1964-1968, vol. XXXII, doc. 308 (Editorial Note)",
     "Office of the Historian, US Department of State", "https://history.state.gov/historicaldocuments/frus1964-68v32/d308",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/FRUS_1964-68_v32_d308.html (pp. 730-732). Cita memorandos internos y el Research "
     "Memorandum 1230 (1980). Datos = hechos; declaraciones de Johnson = postura de EE. UU."),
    ("F036", "Camarioca crisis in 1965", "Departamento Federal de Asuntos Exteriores de Suiza (FDFA), 3 de mayo de 2023",
     "https://www.eda.admin.ch/en/camarioca-crisis-in-1965", "primaria", "revisar", "ninguna", "hechos",
     "Archivo 'fuentes/docs/Camarioca crisis in 1965.html'. Suiza representaba a EE. UU. en Cuba y negoció el "
     "puente aéreo: tercero con papel directo. Su expresión 'opponents of the regime' no entra."),
    ("F037", "Freedom Flights", "Wikipedia", "https://en.wikipedia.org/wiki/Freedom_Flights", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_freedom_flights.html (descargado el 2026-10-30). Tiene lenguaje valorativo "
     "('oppressive government', 'climate of fear') que no entra; los datos van atribuidos."),
    ("F038", "Boca de Camarioca, el primer éxodo masivo de cubanos", "CubaNet (copia traducida al inglés guardada por Denis; sin autor ni fecha visibles)",
     "https://www.cubanet.org/boca-de-camarioca-el-primer-exodo-masivo-de-cubanos/", "periodistica",
     "CubaNet autoriza reproducir citando la fuente", "cubanos_isla", "ambos",
     "Archivo fuentes/docs/CAMARIOCA-cubaNet.md. Lenguaje valorativo ('dictador', 'régimen comunista') que no "
     "entra. Fecha de apertura (3 de octubre) distinta de FRUS y Larzelere (10 de octubre)."),
    ("F039", "Discurso en la presentación del Comité Central del Partido Comunista de Cuba, teatro Chaplin, 3 de octubre de 1965",
     "Fidel Castro - versión taquigráfica del Consejo de Estado (fidelcastro.cu), copia en Marxists Internet Archive",
     "https://www.marxists.org/history/cuba/archive/castro/1965/10/03-oct-1965.htm", "primaria", "revisar",
     "gobierno_cubano", "postura",
     "Archivo fuentes/docs/CASTRO_discurso_3oct1965.html (traducción al inglés). SOLO para documentar lo que "
     "afirmó el gobierno cubano. Nunca sostiene un hecho ni una cifra."),
]

# (id, tipo, fuente, ubicación, corroborado_por, actor, texto)
FRAGMENTOS = [
    ("FR-V001", "hecho", "F035", "p. 730", ["F007", "F034"], None,
     "El 28 de septiembre de 1965 Fidel Castro anunció que los cubanos que quisieran irse a Estados Unidos podrían "
     "hacerlo y que los exiliados podrían recoger a sus familiares en el puerto de Camarioca a partir del 10 de "
     "octubre."),
    ("FR-V002", "cifra_disputada", "F038", "texto", ["F035", "F007"], None,
     "La fecha de apertura del puerto de Camarioca varía según la fuente: CubaNet dice que el puente marítimo se "
     "abrió oficialmente el 3 de octubre de 1965, mientras que el Departamento de Estado y el historiador Alex "
     "Larzelere hablan del 10 de octubre."),
    ("FR-V003", "postura", "F035", "p. 730", [], "gobierno_eeuu",
     "Según el Departamento de Estado, el 3 de octubre de 1965, en la firma de una ley de inmigración en la isla de "
     "la Libertad, en Nueva York, el presidente Johnson declaró al pueblo de Cuba que quienes buscaran refugio en "
     "Estados Unidos lo encontrarían, y ordenó preparar una entrada ordenada, con prioridad para los familiares "
     "directos."),
    ("FR-V004", "postura", "F039", "discurso del 3 de octubre de 1965", [], "gobierno_cubano",
     "Según su discurso del 3 de octubre de 1965, Fidel Castro sostuvo que la política de su gobierno sobre la salida "
     "del país no había cambiado, que después de la Crisis de Octubre seguían saliendo unas 300 personas al mes por "
     "España y México, y que Estados Unidos era el único responsable de que las vías normales estuvieran cerradas, "
     "para fomentar salidas clandestinas y peligrosas con fines de propaganda."),
    ("FR-V005", "postura", "F039", "discurso del 3 de octubre de 1965", [], "gobierno_cubano",
     "Según ese mismo discurso, Castro sostuvo que la salida de las clases privilegiadas era un hecho histórico en todas "
     "las revoluciones y pidió a Johnson que permitiera a los cubanos que vivían en Estados Unidos viajar a Cuba para "
     "visitar a sus familiares."),
    ("FR-V006", "hecho", "F035", "p. 730", [], None,
     "Las primeras personas con familiares en Estados Unidos empezaron a llegar a la Florida en pequeñas "
     "embarcaciones en octubre de 1965; para el 18 de octubre ya eran más de 700."),
    ("FR-V007", "hecho", "F035", "pp. 730-731", [], None,
     "Según un memorando del asesor de seguridad nacional, McGeorge Bundy, al presidente Johnson del 14 de octubre de "
     "1965, Estados Unidos quería limitar la salida "
     "a unas 3.000 personas al mes, mientras que Cuba prefería unas 12.000; Cuba anunció que no dejaría salir a los "
     "hombres en edad militar, de 15 a 26 años, y no quería que participara la Cruz Roja, sino Suiza."),
    ("FR-V008", "hecho", "F035", "p. 731", ["F036"], None,
     "Tras negociar a través de la Embajada de Suiza en La Habana, Estados Unidos y Cuba intercambiaron notas el 6 de "
     "noviembre de 1965 y formalizaron un memorando de entendimiento: entre 3.000 y 4.000 cubanos saldrían cada mes "
     "en un puente aéreo pagado por Estados Unidos desde el aeropuerto de Varadero, sin límite de tiempo."),
    ("FR-V009", "hecho", "F035", "p. 731", [], None,
     "Cuba quería incluir en el memorando de 1965 la exclusión de los hombres en edad militar y de técnicos y "
     "profesionales; Estados Unidos se negó, y Cuba recogió en notas aparte su prohibición de que salieran los "
     "hombres en edad militar, ciertos técnicos y los presos políticos."),
    ("FR-V010", "hecho", "F036", "texto", [], None,
     "El embajador suizo en Cuba, Emil A. Stadelhofer, negoció en nombre de Estados Unidos el puente aéreo con Cuba en "
     "1965, y Suiza registró a cada persona que salió del país por esa vía."),
    ("FR-V011", "hecho", "F035", "pp. 731-732", ["F007", "F034"], None,
     "Cuba dejó de admitir barcos en Camarioca a partir del 28 de octubre de 1965 y prohibió nuevas salidas desde allí "
     "el 4 de noviembre. Entre el 13 y el 24 de noviembre Estados Unidos evacuó en barcos fletados a unas 2.000 "
     "personas que se habían quedado varadas en el puerto."),
    ("FR-V012", "hecho", "F007", "p. 117 (nota)", ["F034", "F038"], None,
     "Por Camarioca salieron 2.979 cubanos antes de que el puerto se cerrara el 15 de noviembre de 1965."),
    ("FR-V013", "hecho_atribuido", "F007", "p. 117 (nota)", ["F034"], None,
     "Según el historiador Alex Larzelere y la Guardia Costera de Estados Unidos, quienes salían por Camarioca tenían "
     "que dejar sus casas y propiedades al gobierno cubano."),
    ("FR-V014", "hecho", "F035", "p. 732", ["F007", "F037"], None,
     "Los Vuelos de la Libertad empezaron el 1 de diciembre de 1965, con dos vuelos al día, cinco días a la semana, "
     "desde Varadero hasta Miami."),
    ("FR-V015", "hecho", "F035", "p. 732", [], None,
     "En 1965 llegaron 9.268 refugiados desde Cuba, 3.349 de ellos en diciembre por el puente aéreo; para el 1 de "
     "diciembre de 1968 el puente aéreo había traído a 131.372 cubanos."),
    ("FR-V016", "cifra_disputada", "F035", "p. 732", ["F007", "F036", "F037", "F027"], None,
     "El total de los Vuelos de la Libertad varía según la fuente: el Departamento de Estado da 260.737 refugiados "
     "hasta abril de 1973; Larzelere, 260.561 en 3.049 vuelos; Suiza, unos 260.000; Wikipedia, 297.318 en 3.048 "
     "vuelos; y la ficha del Servicio de Parques Nacionales, unos 175.000."),
    ("FR-V017", "hecho", "F030", "Resumen, p. 1", [], None,
     "Según un informe del Contralor General de Estados Unidos de 1971, unos 600.000 refugiados cubanos habían "
     "llegado a Estados Unidos desde 1959, unos 243.000 de ellos por el puente aéreo, y el programa de refugiados "
     "había costado unos 730 millones de dólares, incluidas las estimaciones para los años fiscales 1971 y 1972."),
    ("FR-V018", "hecho", "F030", "Resumen, pp. 2-3", [], None,
     "El Departamento de Estado anunció el 31 de agosto de 1971 que el puente aéreo se interrumpiría durante varias "
     "semanas a partir del 1 de septiembre; el número de vuelos restantes dependía de cuántos cubanos dejara salir su "
     "gobierno."),
    ("FR-V019", "hecho", "F035", "p. 732", [], None,
     "Cuando empezó el puente aéreo, según un documento interno del Departamento de Estado de 1968, varios cientos de "
     "miles de cubanos se inscribieron para salir. El gobierno cubano dejó de aceptar nuevas inscripciones en mayo de "
     "1966, y en diciembre de 1968 todavía había miles en la lista de espera."),
    ("FR-V020", "hecho_atribuido", "F037", "sección 'Persecution in Cuba'", [], None,
     "Según Wikipedia, quienes se inscribían para salir eran despedidos de sus trabajos, considerados enemigos del "
     "Estado y hostigados por los Comités de Defensa de la Revolución; algunos fueron internados en campamentos lejos "
     "de sus familias, y sus propiedades se confiscaban al salir."),
    ("FR-V021", "hecho_atribuido", "F037", "sección 'Persecution in Cuba'", [], None,
     "Según Wikipedia, Castro llamaba 'gusanos' a quienes se iban y decía que Cuba estaba mejor sin ellos."),
    ("FR-V022", "hecho_atribuido", "F037", "sección 'Race, gender, and socioeconomic status'", [], None,
     "Según Wikipedia, por las restricciones de salida, entre los refugiados de los Vuelos de la Libertad había más "
     "mujeres y personas mayores que hombres en edad de trabajar; alrededor del 57 por ciento era de clase "
     "trabajadora, y los cubanos negros eran menos del 3 por ciento de los migrantes cubanos en Estados Unidos en "
     "1970."),
    ("FR-V023", "hecho", "F030", "Resumen, p. 3", [], None,
     "Según el informe del Contralor General de 1971, el nivel educativo y el dominio del inglés de los refugiados "
     "llegados desde que empezó el puente aéreo, en diciembre de 1965, eran menores que los de los anteriores, lo que "
     "reducía sus posibilidades de mantenerse por sí mismos."),
    ("FR-V024", "hecho_atribuido", "F037", "sección 'Cuban Adjustment Act'", [], None,
     "Según Wikipedia, la Ley de Ajuste Cubano de 1966 cambió la situación de los cubanos, que habían entrado como "
     "'parolees' con un permiso temporal porque se suponía que volverían pronto a la isla, y les abrió una vía "
     "propia para obtener la residencia permanente."),
    ("FR-V025", "hecho", "F034", "p. 1", [], None,
     "Antes de Camarioca, entre 1959 y el 1 de junio de 1965, la Guardia Costera de Estados Unidos había rescatado o "
     "ayudado a 6.862 cubanos que intentaban cruzar por mar; el primer rescate fue el 22 de julio de 1959, cerca de "
     "las Dry Tortugas."),
    ("FR-V026", "hecho", "F034", "p. 1", [], None,
     "Según la Guardia Costera de Estados Unidos, para salir por Camarioca había que presentar una solicitud al "
     "Ministerio del Interior de Cuba."),
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
    print("Las fuentes F034 en adelante ya están en el registro. No toco nada.")
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

print(f"Registradas {len(FUENTES)} fuentes (F034 a F039).")
print(f"Creado {FRAG} con {len(FRAGMENTOS)} fragmentos en 'pendiente'.")
print(f"Ahora: python revisar.py {FRAG}")
