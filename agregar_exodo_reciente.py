"""
agregar_exodo_reciente.py — Abre la etapa del éxodo reciente (2017 en adelante):
registra las fuentes F054-F060 y crea fuentes/fragmentos_exodo_reciente.jsonl.

Uso (desde E:\\vertex-exilio):
    python agregar_exodo_reciente.py

Documentos leídos (en fuentes/docs): MPI_cubanos.html, WOLA_2023.html, FR_2025_CHNV.htm,
MINREX_conversaciones.html, STATE_2022_conversaciones.htm, WIKI_crisis_2021_2023.html, WIKI_11J.html.
La página o sección va en 'ubicacion'. El Registro Federal lleva la página impresa (90 FR 13611-13622).

Qué hace:
  1. Copia de seguridad del registro.
  2. Añade F054-F060 al registro (si ya existen, no hace nada).
  3. Crea fuentes/fragmentos_exodo_reciente.jsonl con todos los fragmentos en 'pendiente'
     (si el archivo ya existe, no lo toca).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_exodo_reciente.jsonl")
HOY = "2026-10-30"
ETAPA = "exodo_reciente"

FUENTES = [
    ("F054", "Cuban Immigrants in the United States (7 de septiembre de 2023)",
     "Jiaxin Wei y Jeanne Batalova - Migration Policy Institute",
     "https://www.migrationpolicy.org/article/cuban-immigrants-united-states", "academica", "revisar",
     "academica", "hechos",
     "Archivo fuentes/docs/MPI_cubanos.html (guardado desde Chrome). Datos del censo (ACS 2021), DHS y ONU. "
     "Cifras demográficas de 2021: no son 'de hoy'."),
    ("F055", "Five Key Trends in Cuban Migration in 2023 (20 de diciembre de 2023)",
     "WOLA (Washington Office on Latin America)",
     "https://www.wola.org/analysis/developments-cuban-migration-2023/", "academica", "revisar", "academica", "ambos",
     "Archivo fuentes/docs/WOLA_2023.html. ONG de derechos humanos con sede en Washington; tiene posición propia "
     "(crítica del embargo y del sistema político cubano). Datos de CBP y de otras organizaciones = hechos "
     "atribuidos; sus valoraciones ('unbearable', 'abject suffering') = postura de WOLA. Fecha las conversaciones "
     "migratorias de 2022 el 14 de abril; la declaración de EE. UU. (F058) dice 21 de abril: cifra disputada."),
    ("F056", "Termination of Parole Processes for Cubans, Haitians, Nicaraguans, and Venezuelans (90 FR 13611, 25 de marzo de 2025)",
     "Department of Homeland Security - Federal Register (govinfo.gov)",
     "https://www.govinfo.gov/content/pkg/FR-2025-03-25/html/2025-05128.htm", "primaria",
     "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/FR_2025_CHNV.htm. Ubicación = página impresa (13611-13622). Fechas y cifras = hechos; "
     "los argumentos para cerrar el programa = postura del gobierno de EE. UU. (administración Trump). La cifra "
     "de 532.000 es de las cuatro nacionalidades juntas, no solo de cubanos."),
    ("F057", "Cuba and the United States hold immigration talks in Washington DC (16 de abril de 2024)",
     "Ministerio de Relaciones Exteriores de Cuba (cubaminrex.cu, versión en inglés)",
     "https://cubaminrex.cu/en/cuba-and-united-states-hold-immigration-talks-washington-dc", "primaria", "revisar",
     "gobierno_cubano", "postura",
     "Archivo fuentes/docs/MINREX_conversaciones.html. SOLO para documentar la versión oficial cubana. Nunca "
     "sostiene un hecho ni una cifra. Usa 'bloqueo' (término disputado): siempre atribuido."),
    ("F058", "Migration Talks with the Government of Cuba (21 de abril de 2022)",
     "Department of State (copia en GlobalSecurity.org)",
     "https://www.globalsecurity.org/wmd/library/news/cuba/cuba-220421-state01.htm", "primaria",
     "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/STATE_2022_conversaciones.htm. Copia del comunicado del Departamento de Estado. "
     "Datos de la reunión = hechos; valoraciones = postura de EE. UU."),
    ("F059", "2021–2023 Cuban migration crisis", "Wikipedia",
     "https://en.wikipedia.org/wiki/2021%E2%80%932023_Cuban_migration_crisis", "enciclopedia", "CC-BY-SA-4.0",
     "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_crisis_2021_2023.html (guardado desde Chrome el 2026-10-30). Tiene "
     "incoherencias internas: dice que Cuba perdió casi el 8 % de su población y más abajo el 3,5 %; da 313.488 "
     "llegadas en 2022 en el texto y 313.499 en la tabla; la cifra de 850.000 no cuadra con otras fuentes. "
     "Un párrafo sobre 'expedited removal' es confuso y no se usa."),
    ("F060", "2021 Cuban protests", "Wikipedia", "https://en.wikipedia.org/wiki/2021_Cuban_protests",
     "enciclopedia", "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_11J.html (guardado desde Chrome el 2026-10-30). Artículo largo; los 'objetivos' de "
     "la ficha (incluida la intervención militar) no se usan. Expresiones como 'dictatorship' o 'police state' "
     "son citas de terceros: no entran."),
]

# (id, tipo, fuente, ubicación, corroborado_por, actor, texto)
FRAGMENTOS = [
    # ---------------- tamaño del éxodo
    ("FR-R001", "hecho", "F054", "introducción", ["F059"], None,
     "Desde 2020-2021 la salida irregular de cubanos hacia Estados Unidos creció tanto que se considera la mayor "
     "emigración en la historia moderna de Cuba."),
    ("FR-R002", "hecho", "F054", "Highlights", ["F059"], None,
     "En el año fiscal 2022 las autoridades de Estados Unidos registraron casi 225.000 encuentros con cubanos en la "
     "frontera con México y más de 6.000 intercepciones de cubanos en el mar, cifras que juntas superan las del "
     "Mariel en 1980 y la crisis de los balseros de 1994."),
    ("FR-R003", "hecho_atribuido", "F055", "introducción", [], None,
     "Según WOLA, casi 425.000 cubanos llegaron a Estados Unidos en los años fiscales 2022 y 2023, y otros 36.000 "
     "pidieron asilo en México entre enero de 2022 y noviembre de 2023, sin contar a los que se fueron a Brasil, "
     "Rusia, Uruguay y otros países."),
    ("FR-R004", "cifra_disputada", "F055", "introducción", ["F059"], None,
     "El récord mensual de llegadas de cubanos a Estados Unidos fue en diciembre de 2022, pero la cifra varía según "
     "la fuente: WOLA da 44.079 y Wikipedia da 44.064."),
    ("FR-R005", "hecho_atribuido", "F059", "Exodus", [], None,
     "Según Wikipedia, en el año calendario 2022 llegaron a Estados Unidos unos 313.000 cubanos (313.488 según el "
     "texto del artículo y 313.499 según su tabla)."),
    ("FR-R006", "cifra_disputada", "F055", "introducción", ["F059"], None,
     "Las estimaciones de cuánta población perdió Cuba con este éxodo no coinciden: WOLA calcula más del 4 %, "
     "contando a los que llegaron a Estados Unidos en los años fiscales 2022 y 2023 y a los que pidieron asilo en "
     "México; Wikipedia da en un lugar casi el 8 % y en otro el 3,5 %."),
    ("FR-R007", "hecho_atribuido", "F059", "Demographics", [], None,
     "Según Wikipedia, los demógrafos Juan Carlos Albizu-Campos y Sergio Díaz-Briquets calculan que cerca del 80 % "
     "de los que emigraron en 2022 tenía entre 15 y 59 años, y economistas y sociólogos cubanos advierten que se "
     "están yendo sobre todo jóvenes, estudiantes y profesionales."),
    # ---------------- causas
    ("FR-R008", "hecho", "F059", "Background and contributing factors", ["F055", "F060"], None,
     "El éxodo coincidió con una crisis económica grave en Cuba, con escasez de alimentos y medicinas, inflación y "
     "apagones frecuentes, y con las protestas del 11 de julio de 2021."),
    ("FR-R009", "hecho_atribuido", "F060", "Background", [], None,
     "Según Wikipedia, la economía cubana se contrajo un 10,9 % en 2020 y un 2 % en el primer semestre de 2021, por "
     "una combinación de factores: menos ayuda de Venezuela, el embargo y las sanciones de Estados Unidos "
     "(endurecidas en 2019) y la pandemia, que golpeó el turismo y las remesas; la reforma monetaria disparó una "
     "inflación estimada en un 500 %."),
    ("FR-R010", "postura", "F060", "Background", [], "academia",
     "Según Wikipedia, la historiadora Lillian Guerra atribuyó la escasez de alimentos a que el gobierno gastaba en "
     "hoteles e instalaciones turísticas, mientras que el economista Pavel Vidal sostuvo que tanto el embargo como "
     "la falta de reformas en Cuba causan problemas."),
    ("FR-R011", "hecho_atribuido", "F059", "Background and contributing factors", [], None,
     "Según Wikipedia, Jorge Duany, director del Instituto de Investigaciones Cubanas de FIU, considera que la razón "
     "más inmediata del aumento de la emigración fueron las protestas de julio de 2021."),
    ("FR-R012", "hecho", "F059", "Background and contributing factors", ["F055"], None,
     "En 2017 Estados Unidos redujo el personal de su embajada en La Habana tras los problemas de salud que "
     "afectaron a sus diplomáticos, suspendió los servicios consulares, y los cubanos tuvieron que viajar a Guyana "
     "para tramitar visas, un viaje caro."),
    ("FR-R013", "hecho_atribuido", "F059", "Background and contributing factors", [], None,
     "Según Wikipedia, por el recorte de personal en la embajada Estados Unidos no pudo cumplir su compromiso de dar "
     "20.000 visas de inmigrante al año a los cubanos."),
    # ---------------- la ruta por Nicaragua
    ("FR-R014", "hecho", "F055", "Nicaragua", ["F059"], None,
     "En noviembre de 2021 Nicaragua eliminó el visado para los cubanos, lo que abrió una ruta aérea hasta Managua y "
     "de ahí por tierra hacia Estados Unidos, que evitaba el mar y la selva del Darién."),
    ("FR-R015", "hecho_atribuido", "F055", "Nicaragua", [], None,
     "Según WOLA, con datos del Diálogo Interamericano, en 2023 hubo un promedio de 50 vuelos chárter al mes entre "
     "La Habana y Managua, que llevaron a unas 100.000 personas, y casi 77.000 pasaron por Honduras en los primeros "
     "once meses del año."),
    ("FR-R016", "hecho_atribuido", "F059", "Exodus", [], None,
     "Según Wikipedia, el viaje por Centroamérica costaba a cada persona entre 8.000 y 10.000 dólares y causó "
     "varias muertes."),
    ("FR-R017", "postura", "F055", "Nicaragua", [], "WOLA",
     "Según WOLA, en Managua el gobierno de Ortega y Murillo cobraba tarifas de entrada arbitrarias antes de dejar "
     "que redes de tráfico llevaran a los migrantes hasta la frontera con Honduras."),
    ("FR-R018", "postura", "F059", "Visa change of Nicaragua", [], "algunos expertos",
     "Según Wikipedia, algunos expertos especularon que Nicaragua podía estar usando a los migrantes cubanos para "
     "presionar a Estados Unidos a levantar las sanciones contra Daniel Ortega y su entorno."),
    ("FR-R019", "hecho_atribuido", "F055", "Nicaragua", [], None,
     "Según WOLA, el 21 de noviembre de 2023 el Departamento de Estado anunció restricciones de visado contra "
     "aerolíneas que facilitaban vuelos chárter a Managua, y dos compañías dominicanas y Aruba Airlines suspendieron "
     "el servicio."),
    ("FR-R020", "hecho_atribuido", "F055", "rutas", [], None,
     "Según WOLA, varios países empezaron a exigir visado de tránsito a los cubanos: Costa Rica en febrero de 2022, "
     "Panamá y República Dominicana en marzo de 2022, y Jamaica y México en marzo y octubre de 2023; Guyana seguía "
     "sin pedir visado."),
    ("FR-R021", "hecho_atribuido", "F055", "mar", [], None,
     "Según WOLA, las 13.000 intercepciones y encuentros de cubanos en el mar en los años fiscales 2022 y 2023 son la "
     "mayor ola por mar desde la crisis de los balseros de 1994, aunque mucho menor que la llegada por tierra y aire."),
    ("FR-R022", "hecho_atribuido", "F059", "Exodus", [], None,
     "Según Wikipedia, entre octubre de 2021 y diciembre de 2022 llegaron por mar 9.164 migrantes cubanos."),
    # ---------------- vías legales y parole
    ("FR-R023", "hecho", "F054", "introducción", ["F055"], None,
     "En enero de 2023 la embajada de Estados Unidos en La Habana reanudó los servicios regulares de visas y consulares por "
     "primera vez en cinco años, y en mayo de 2022 Estados Unidos había anunciado la reanudación del programa de "
     "reunificación familiar para cubanos, creado en 2007 y suspendido en 2018."),
    ("FR-R024", "hecho", "F056", "p. 13611-13612", ["F054", "F055"], None,
     "En enero de 2023 el Departamento de Seguridad Nacional abrió un programa de permiso humanitario (parole) para "
     "cubanos, haitianos y nicaragüenses, que se sumó al de venezolanos de octubre de 2022; el de cubanos empezó el "
     "6 de enero de 2023."),
    ("FR-R025", "hecho_atribuido", "F054", "introducción", [], None,
     "Según el Migration Policy Institute, ese programa permitía venir en avión a quienes tuvieran un patrocinador en "
     "Estados Unidos y vivir allí dos años; admitía hasta 30.000 personas al mes de las cuatro nacionalidades, y "
     "para finales de agosto de 2023 habían llegado más de 43.000 cubanos."),
    ("FR-R026", "hecho_atribuido", "F055", "políticas", [], None,
     "Según WOLA, para diciembre de 2023 más de 50.000 cubanos habían viajado a Estados Unidos con el programa de "
     "permiso humanitario."),
    ("FR-R027", "hecho_atribuido", "F056", "p. 13612", [], None,
     "Según el Registro Federal de Estados Unidos, entre octubre de 2022 y el 22 de enero de 2025 unas 532.000 "
     "personas de las cuatro nacionalidades (Cuba, Haití, Nicaragua y Venezuela) recibieron autorización para viajar "
     "con ese programa."),
    ("FR-R028", "hecho_atribuido", "F055", "políticas", [], None,
     "Según WOLA, desde enero de 2023 Estados Unidos aplicó con rigor el Título 42 para devolver a México a cubanos "
     "que llegaban a la frontera, y tras el fin de esa norma en mayo de 2023 siguió devolviéndolos gracias a un "
     "acuerdo con México; entre mayo y octubre de 2023 fueron devueltos a México 17.000 ciudadanos de Cuba, Haití, "
     "Nicaragua y Venezuela."),
    ("FR-R029", "hecho_atribuido", "F059", "Exodus", [], None,
     "Según Wikipedia, en 2022 México no permitía que Estados Unidos expulsara cubanos por la frontera terrestre bajo "
     "el Título 42 y Cuba no aceptaba vuelos de expulsión, de modo que cerca del 98 % de los cubanos detenidos en la "
     "frontera fueron procesados en Estados Unidos por la ley migratoria ordinaria."),
    ("FR-R030", "hecho", "F055", "conversaciones", ["F059"], None,
     "En noviembre de 2022 Cuba aceptó recibir vuelos de deportación desde Estados Unidos; según WOLA, los vuelos se "
     "reanudaron el 24 de abril de 2023, siguieron una vez al mes y para diciembre de 2023 habían devuelto a 386 cubanos."),
    ("FR-R031", "hecho_atribuido", "F055", "Ley de Ajuste", [], None,
     "Según WOLA, en septiembre de 2023 la Junta de Apelaciones de Inmigración decidió que el documento I-220A, que "
     "se daba a muchos cubanos al soltarlos en la frontera, no equivale a una admisión legal, por lo que sus "
     "portadores no pueden pedir la residencia por la Ley de Ajuste Cubano, y miles quedaron en un limbo legal."),
    ("FR-R032", "hecho_atribuido", "F055", "Ley de Ajuste", [], None,
     "Según WOLA, desde el inicio del año fiscal 2022 hasta diciembre de 2023 las autoridades fronterizas de "
     "Estados Unidos registraron 442.977 encuentros con cubanos."),
    # ---------------- fin del parole (2025)
    ("FR-R033", "hecho_atribuido", "F056", "p. 13611", [], None,
     "Según el Registro Federal, el Departamento de Seguridad Nacional dio por terminados los programas de permiso "
     "humanitario para cubanos, haitianos, nicaragüenses y venezolanos el 25 de marzo de 2025, y los permisos que no "
     "hubieran vencido terminaban el 24 de abril de 2025, salvo decisión individual en contra."),
    ("FR-R034", "hecho_atribuido", "F056", "p. 13614", [], None,
     "Según el Registro Federal, el 4 de octubre de 2024, todavía bajo el gobierno de Biden, ya se había anunciado "
     "que no habría renovación del permiso al terminar los dos años iniciales."),
    ("FR-R035", "postura", "F056", "pp. 13611-13613", [], "gobierno_eeuu",
     "Según el Registro Federal, el gobierno de Trump sostuvo que esos programas no lograron una mejora suficiente y "
     "duradera de la seguridad fronteriza y que dejaron dentro del país a una población grande sin una vía clara "
     "hacia un estatus estable; la orden ejecutiva 14165, del 20 de enero de 2025, había ordenado terminarlos."),
    ("FR-R036", "hecho_atribuido", "F056", "p. 13614", [], None,
     "Según el Registro Federal, en diciembre de 2022 la Patrulla Fronteriza encontró a unos 84.000 ciudadanos de "
     "Cuba, Haití, Nicaragua y Venezuela en la frontera suroeste; desde enero de 2024 la cifra estuvo por debajo de "
     "12.000 cada mes, y desde junio de 2024 por debajo de 6.000."),
    # ---------------- 11 de julio de 2021
    ("FR-R037", "hecho", "F060", "introducción", ["F055", "F059"], None,
     "El 11 de julio de 2021 empezaron en Cuba protestas contra el gobierno, desencadenadas por la escasez de "
     "alimentos y medicinas y por la situación de la pandemia; fueron las mayores desde el Maleconazo de 1994."),
    ("FR-R038", "hecho_atribuido", "F060", "11 July", [], None,
     "Según Wikipedia, las protestas del 11 de julio empezaron en San Antonio de los Baños y Palma Soriano, se "
     "extendieron a al menos 50 ciudades, y muchos manifestantes cantaban 'Patria y Vida', canción cuyo título "
     "invierte el lema 'Patria o Muerte'."),
    ("FR-R039", "postura", "F060", "11 July", [], "gobierno_cubano",
     "Según Wikipedia, el presidente Miguel Díaz-Canel culpó de la situación al embargo y las sanciones de Estados "
     "Unidos, llamó por televisión a los partidarios del gobierno a salir a la calle a enfrentar las protestas, y el "
     "gobierno calificó las manifestaciones de contrarrevolucionarias."),
    ("FR-R040", "hecho_atribuido", "F060", "13 July", [], None,
     "Según Wikipedia, el Ministerio del Interior reconoció la muerte de un manifestante, Diubis Laurencio Tejeda, de "
     "36 años, mientras que la organización opositora Cuba Decide estimó cinco muertos."),
    ("FR-R041", "cifra_disputada", "F060", "introducción y ficha", ["F059", "F055"], None,
     "El número de detenidos por el 11J varía según la fuente: Human Rights Watch habla de unos 400 y Cubalex de más "
     "de 500, según Wikipedia; otro artículo de Wikipedia dice más de 700, y WOLA habla de cientos de detenidos. "
     "Según Wikipedia, al menos 710 personas fueron acusadas de delitos, entre ellos sedición."),
    ("FR-R042", "hecho_atribuido", "F060", "introducción", [], None,
     "Según Wikipedia, algunos manifestantes recibieron largas penas de prisión en juicios que Amnistía "
     "Internacional, activistas y familiares criticaron como injustos; el gobierno levantó temporalmente límites a "
     "la importación de alimentos y medicinas, y Estados Unidos impuso nuevas sanciones a funcionarios cubanos."),
    ("FR-R043", "postura", "F060", "Background", [], "gobierno_cubano",
     "Según Wikipedia, el gobierno cubano atribuyó la crisis económica al embargo y a su endurecimiento, y a los "
     "efectos de la pandemia."),
    # ---------------- los dos gobiernos
    ("FR-R044", "hecho_atribuido", "F058", "texto", [], None,
     "Según el Departamento de Estado, el 21 de abril de 2022 delegaciones de Estados Unidos y Cuba se reunieron en "
     "Washington para revisar los acuerdos migratorios, en las primeras conversaciones de ese tipo desde 2018, y "
     "Estados Unidos anunció la reanudación limitada de visas de inmigrante en su embajada a partir de mayo."),
    ("FR-R045", "cifra_disputada", "F055", "conversaciones", ["F058"], None,
     "La fecha de las conversaciones migratorias de 2022 varía según la fuente: WOLA dice que fueron el 14 de abril "
     "de 2022 y el comunicado del Departamento de Estado, el 21 de abril."),
    ("FR-R046", "postura", "F058", "texto", [], "gobierno_eeuu",
     "Según el comunicado del Departamento de Estado de abril de 2022, facilitar una migración segura, legal y "
     "ordenada era un interés común de los dos países y respondía al interés de Estados Unidos en la reunificación "
     "familiar y en un mayor respeto de los derechos humanos en Cuba."),
    ("FR-R047", "hecho_atribuido", "F059", "Bilaterial discussion", [], None,
     "Según Wikipedia, en las conversaciones de abril de 2022 el gobierno cubano pidió a Estados Unidos cumplir el "
     "compromiso de dar 20.000 visas de inmigrante al año, y Estados Unidos pidió a La Habana aceptar a los cubanos "
     "deportados por haber llegado ilegalmente."),
    ("FR-R048", "postura", "F059", "Responses", [], "gobierno_eeuu",
     "Según Wikipedia, Estados Unidos culpó del éxodo a la incapacidad del gobierno cubano de garantizar servicios "
     "básicos como la electricidad."),
    ("FR-R049", "postura", "F059", "Responses", [], "gobierno_cubano",
     "Según Wikipedia, el gobierno cubano atribuye las salidas masivas al embargo de Estados Unidos y a su política "
     "de dar beneficios a los migrantes cubanos, incluso a los que llegan ilegalmente."),
    ("FR-R050", "postura", "F057", "texto", [], "gobierno_cubano",
     "Según la cancillería cubana, en las conversaciones migratorias del 16 de abril de 2024 Cuba reafirmó que cumple "
     "los acuerdos y denunció que el embargo de Estados Unidos (que el gobierno cubano llama bloqueo), endurecido "
     "desde 2019, es un incentivo importante para emigrar, junto con la inclusión de Cuba en la lista de países "
     "patrocinadores del terrorismo, el trato preferente a los cubanos que entran ilegalmente y la Ley de Ajuste Cubano."),
    ("FR-R051", "hecho_atribuido", "F055", "causas", [], None,
     "Según WOLA, en enero de 2021 el gobierno de Trump volvió a incluir a Cuba en la lista de países patrocinadores "
     "del terrorismo."),
    ("FR-R052", "postura", "F055", "causas", [], "WOLA",
     "Según WOLA, las restricciones del embargo que impiden a Cuba comprar a crédito agravaron el golpe económico de "
     "la pandemia, y en Estados Unidos hay poca voluntad política de revisar políticas que, a su juicio, empeoran "
     "las dificultades económicas de Cuba."),
    ("FR-R053", "hecho_atribuido", "F055", "causas", [], None,
     "Según WOLA, cifras del gobierno cubano indican que el país perdió el 9 % de sus profesionales de la salud entre "
     "2021 y 2022, las escuelas tenían falta de maestros, y funcionarios cubanos advirtieron de apagones de 8 a 10 "
     "horas diarias."),
    # ---------------- los cubanos en Estados Unidos
    ("FR-R054", "hecho_atribuido", "F054", "Highlights", [], None,
     "Según el Migration Policy Institute, en 2021 vivían en Estados Unidos cerca de 1,3 millones de inmigrantes "
     "cubanos; en 2017-2021 el 76 % vivía en la Florida, el 52 % solo en el condado de Miami-Dade, y una de cada "
     "ocho personas del área de Miami había nacido en Cuba."),
    ("FR-R055", "hecho_atribuido", "F054", "Diaspora", [], None,
     "Según el Migration Policy Institute, en 2021 unos 2,7 millones de residentes en Estados Unidos habían nacido "
     "en Cuba o declaraban ascendencia cubana, y 1,4 millones de ellos (el 52 %) habían nacido en Estados Unidos."),
    ("FR-R056", "hecho_atribuido", "F054", "Age, Education, Income, Naturalization", [], None,
     "Según el Migration Policy Institute, en 2021 la edad mediana de los inmigrantes cubanos era de 55 años, el 66 % "
     "eran ciudadanos estadounidenses, el ingreso mediano de sus hogares era de 52.000 dólares, frente a unos 70.000 "
     "del conjunto de inmigrantes, y el 16 % vivía en la pobreza."),
    ("FR-R057", "hecho_atribuido", "F054", "Immigration Pathways", [], None,
     "Según el Migration Policy Institute, en el año fiscal 2022 obtuvieron la residencia permanente 36.600 cubanos, "
     "y el 40 % lo hizo por una vía humanitaria, frente al 8 % del total de nuevos residentes."),
    ("FR-R058", "hecho_atribuido", "F054", "Top Global Destinations", [], None,
     "Según el Migration Policy Institute, con estimaciones de la ONU de 2020, después de Estados Unidos los "
     "principales destinos de los cubanos en el exterior eran España (162.000), Italia (39.000), Chile (24.000) y "
     "Canadá (19.000)."),
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
    print("Las fuentes F054 en adelante ya están en el registro. No toco nada.")
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

print(f"Registradas {len(FUENTES)} fuentes (F054 a F060).")
print(f"Creado {FRAG} con {len(FRAGMENTOS)} fragmentos en 'pendiente'.")
print(f"Ahora: python revisar.py {FRAG}")
