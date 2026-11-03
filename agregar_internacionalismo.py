"""
agregar_internacionalismo.py — Etapa internacionalismo_militar (módulo "Cuba: contexto").

Registra las fuentes F099-F108 y crea fuentes/fragmentos_internacionalismo.jsonl (FR-I001 en adelante):
Angola (1975-1991), Etiopía (1977-1978) y el apoyo cubano a guerrillas de Centroamérica y Colombia.

Uso (desde E:\\vertex-exilio):
    python agregar_internacionalismo.py

Criterios:
  - Gleijeses (vía National Security Archive y Wilson Quarterly) es la base académica sobre África; sus
    conclusiones van como postura con actor, porque otros autores discuten su visión.
  - Fidel Castro (2005) es postura del gobierno cubano, cifras incluidas.
  - El Departamento de Estado (informe 90 de 1981 y Libro Blanco de 1981) es postura del gobierno de EE. UU.:
    sus acusaciones van como postura; las críticas que recibió el Libro Blanco van con fuente periodística.
  - El artículo del Mail & Guardian es opinión: sus juicios van como postura; los datos que cita, atribuidos.
  - Cifras que no cuadran entre fuentes: cifra_disputada.
  - No entran: la fecha "1998" de IPS para los acuerdos de Nueva York (es una errata: fueron en diciembre de
    1988), "glorioso", "heroico", "racistas", "títere" y demás lenguaje de las fuentes.

Qué hace:
  1. Comprueba que validar.py tiene la etapa internacionalismo_militar.
  2. Copia de seguridad del registro (y del archivo de fragmentos si ya existiera).
  3. Añade F099-F108 al registro (si alguna ya existe, no toca nada).
  4. Crea el archivo de fragmentos en estado 'pendiente'.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_internacionalismo.jsonl")
HOY = "2026-11-03"
T = "internacionalismo_militar"

NSA = "Según el National Security Archive (2002), que resume el libro del historiador Piero Gleijeses basado en archivos cubanos"
WQ = "Según un resumen en The Wilson Quarterly del estudio del historiador Piero Gleijeses «Moscow's Proxy? Cuba and Africa 1975-1988» (2006)"
IPS = "Según Inter Press Service (La Habana, noviembre de 2005)"
FC = "Según Fidel Castro, en su discurso del 2 de diciembre de 2005 por el 30 aniversario de la misión militar en Angola"
LOC = "Según el estudio de país sobre Etiopía de la Biblioteca del Congreso de EE. UU."
DE = "Según el Departamento de Estado de EE. UU., en su Informe Especial n.º 90 (diciembre de 1981)"
LB = "Según el Libro Blanco del Departamento de Estado de EE. UU. sobre El Salvador (febrero de 1981)"
CSM = "Según The Christian Science Monitor (junio de 1981)"
LG = "Según el politólogo William LeoGrande (American University), en una reseña de 2011 del estudio de Andrea Oñate basado en entrevistas con comandantes del FMLN"
MG = "Según Drew Forrest, exeditor político del diario sudafricano Mail & Guardian (2022)"

FUENTES = [
    ("F099", "Secret Cuban Documents on History of Africa Involvement (Electronic Briefing Book n.º 67, 1 de abril de 2002)",
     "National Security Archive (George Washington University), sobre el libro de Piero Gleijeses 'Conflicting Missions'",
     "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB67/", "archivo", "revisar", "academica", "ambos",
     "Archivo fuentes/docs/NSA_2002_angola.html. Resume las conclusiones de Gleijeses y publica documentos cubanos. "
     "Las conclusiones del autor: hecho atribuido o postura según el caso."),
    ("F100", "Fidel's African Adventures (resumen de Piero Gleijeses, 'Moscow's Proxy? Cuba and Africa 1975-1988', "
             "Journal of Cold War Studies, 2006)", "The Wilson Quarterly",
     "https://www.wilsonquarterly.com/quarterly/_/fidels-african-adventures/", "academica", "revisar", "academica",
     "ambos",
     "Archivo fuentes/docs/WQ_gleijeses_2006.html. Resumen periodístico de un artículo académico: lo que dice Gleijeses, "
     "atribuido a él; sus juicios, como postura."),
    ("F101", "Cuba: Angolan war memories live on (30 de noviembre de 2005)", "Dalia Acosta, Inter Press Service",
     "https://www.ipsnews.net/2005/11/cuba-angolan-war-memories-live-on/", "periodistica", "revisar", "ninguna",
     "ambos",
     "Archivo fuentes/docs/IPS_2005_angola.html. Fecha el acuerdo de Nueva York el '22 de diciembre de 1998': es una "
     "errata (fue en 1988) y no entra. 'Heroic battles' es lenguaje de la nota."),
    ("F102", "La batalla de Cuito Cuanavale. Misión militar cubana en Angola (discurso del 2 de diciembre de 2005; "
             "revista Tareas, n.º 161, 2019, pp. 119-132)", "Fidel Castro Ruz",
     "https://www.redalyc.org/articulo.oa?id=535058540010", "primaria", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/FIDEL_2005_cuito.pdf. Versión oficial cubana: todo como postura, cifras incluidas. Su "
     "lenguaje ('racistas', 'títere', 'glorioso') no entra."),
    ("F103", "Ethiopia: War in the Ogaden and the Turn to the Soviet Union (Ethiopia: A Country Study)",
     "Biblioteca del Congreso de EE. UU., Federal Research Division", "https://countrystudies.us/ethiopia/32.htm",
     "secundaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/LOC_etiopia_ogaden.html (copia en countrystudies.us). 'Revolutionary regime' y "
     "'Mengistu regime' son lenguaje de la fuente."),
    ("F104", "Cuba's Renewed Support for Violence in Latin America (Special Report n.º 90, 14 de diciembre de 1981)",
     "Departamento de Estado de EE. UU., Bureau of Public Affairs", "https://latinamericanstudies.org/guerrilla/report-90.htm",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/STATE_1981_informe90.html (copia en latinamericanstudies.org). Acusaciones de una parte "
     "del conflicto: postura del gobierno de EE. UU. El propio informe dice que algunos detalles no pueden "
     "verificarse en público."),
    ("F105", "Communist interference in El Salvador (Libro Blanco del Departamento de Estado, texto publicado el 26 de "
             "febrero de 1981)", "Departamento de Estado de EE. UU. (publicado por The Christian Science Monitor)",
     "https://www.csmonitor.com/1981/0226/022661.html", "primaria", "dominio_publico (obra del gobierno de EE. UU.)",
     "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/CSM_1981_libro_blanco.html. Postura del gobierno de EE. UU.; criticado después (ver F106)."),
    ("F106", "U.S. defends report on communist arms in El Salvador (25 de junio de 1981)",
     "James Nelson Goodsell, The Christian Science Monitor", "https://www.csmonitor.com/1981/0625/062554.html",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/CSM_1981_criticas.html. Recoge las críticas al Libro Blanco y la defensa del Departamento "
     "de Estado."),
    ("F107", "H-Diplo Article Review n.º 332 (11 de noviembre de 2011), sobre Andrea Oñate, 'The Red Affairs: "
             "FMLN-Cuban relations during the Salvadoran Civil War, 1981-1992' (Cold War History, 2011)",
     "William M. LeoGrande, American University", "https://issforum.org/reviews/PDF/AR332.pdf", "academica",
     "revisar", "academica", "ambos",
     "Archivo fuentes/docs/HDIPLO_2011_leogrande.pdf. Lo que cuenta Oñate (por entrevistas) y lo que discute "
     "LeoGrande: atribuido a cada uno."),
    ("F108", "The battle over Cuito Cuanavale still rages (25 de febrero de 2022)", "Drew Forrest, Mail & Guardian",
     "https://mg.co.za/2022-02-25-the-battle-over-cuito-cuanavale-still-rages/", "opinion", "revisar", "ninguna",
     "ambos",
     "Archivo fuentes/docs/MG_2022_cuito.html. Columna de opinión: sus juicios son postura del autor; las cifras que "
     "cita (de la SADF y otras) van atribuidas. Su lenguaje ('power-intoxicated tribalist', etc.) no entra."),
]

NUEVOS = [
    # ================= Angola: origen de la intervención
    dict(id="FR-I001", tipo="hecho_atribuido", id_fuente="F099", ubicacion="Párrafos 4-6",
         texto=f"{NSA}, Gleijeses fue el primer investigador con acceso a archivos cubanos cerrados, entre ellos los del "
               "Comité Central del Partido, las fuerzas armadas y la cancillería, tras más de seis años de viajes de "
               "investigación; también trabajó en archivos de Estados Unidos, Bélgica, Gran Bretaña y las dos Alemanias "
               "y entrevistó a más de ciento cincuenta protagonistas."),
    dict(id="FR-I002", tipo="hecho_atribuido", id_fuente="F099", ubicacion="Párrafo 3",
         texto=f"{NSA}, Fidel Castro decidió enviar tropas a Angola el 4 de noviembre de 1975 como respuesta a la invasión "
               "sudafricana del país, y no al revés, como sostuvo el gobierno de Ford; Cuba tomó la decisión sin informar "
               "a la Unión Soviética y desplegó sus tropas sin ninguna ayuda soviética durante los dos primeros meses."),
    dict(id="FR-I003", tipo="hecho_atribuido", id_fuente="F099", ubicacion="Párrafos 3 y 8",
         texto=f"{NSA}, Estados Unidos conocía los planes de la invasión encubierta de Sudáfrica y colaboró militarmente con "
               "sus tropas, en contra de lo que el secretario de Estado Henry Kissinger declaró ante el Congreso en 1976; "
               "un colaborador de Kissinger, Joseph Sisco, admitió que el gobierno de Ford no desalentó la intervención "
               "sudafricana, y hay pruebas de que la CIA ayudó a los sudafricanos a llevar armas al frente."),
    dict(id="FR-I004", tipo="hecho_atribuido", id_fuente="F099", ubicacion="Párrafo 7",
         texto=f"{NSA}, la política africana de Cuba venía de antes de Angola: ayuda a los rebeldes argelinos que luchaban "
               "contra Francia en 1961, una guerra secreta entre La Habana y Washington en Zaire en 1964-1965 y una "
               "contribución decisiva a la guerra de independencia de Guinea-Bisáu entre 1966 y 1974."),
    dict(id="FR-I005", tipo="cifra_disputada", id_fuente="F099", ubicacion="Párrafo 7 (F099); párrafo 1 (F100)",
         corroborado_por=["F100"],
         texto="El número de soldados cubanos enviados a Angola en 1975-1976 se da de forma distinta: el National Security "
               "Archive, resumiendo el libro de Gleijeses de 2002, habla de 30.000 cubanos, mientras que el resumen de su "
               "estudio de 2006 en The Wilson Quarterly habla de 36.000 soldados."),
    # ================= Angola: Gleijeses (2006)
    dict(id="FR-I006", tipo="hecho_atribuido", id_fuente="F100", ubicacion="Párrafos 1, 3 y 5",
         texto=f"{WQ}, tras los 36.000 soldados enviados a Angola desde noviembre de 1975, Cuba mandó otros 16.000 a Etiopía a "
               "finales de 1977; los cooperantes y técnicos cubanos en Angola llegaron a ser 5.000; Cuba envió ayuda a "
               "otros 11 países africanos y misiones militares a otros cinco, y perdió más de 2.000 soldados en África."),
    dict(id="FR-I007", tipo="hecho_atribuido", id_fuente="F100", ubicacion="Párrafos 2, 4 y 5",
         texto=f"{WQ}, el líder soviético Leonid Brezhnev se opuso al envío de tropas cubanas a Angola, y Cuba y la URSS "
               "chocaron repetidamente sobre la estrategia en el sur de África, aunque Moscú elogió la intervención en "
               "Etiopía y suministró las armas cubanas; un estudio interagencias de Estados Unidos de 1978 concluyó que "
               "Cuba no actuaba en África «solo ni principalmente» por los soviéticos, y la intervención acabó con la "
               "idea de Carter de normalizar relaciones con La Habana."),
    dict(id="FR-I008", tipo="postura", id_fuente="F100", ubicacion="Párrafos 2, 3 y 6", actor="Piero Gleijeses (historiador)",
         texto=f"{WQ}, Gleijeses concluye que Cuba no fue un peón del Kremlin, al menos en Angola, y que Castro intervino "
               "porque la derrota del MPLA habría sido la victoria del apartheid; sostiene que Cuba salvó a Angola de la "
               "intervención sudafricana y aseguró que Pretoria aceptara después la independencia de Namibia, aunque el "
               "MPLA se volvió represivo y corrupto; sobre Etiopía, dice que Cuba defendió las fronteras pero sostuvo a un "
               "gobierno brutal, que con ese apoyo desató una guerra de terror contra los rebeldes de Eritrea, y que no "
               "puede condenar ni aplaudir ese papel."),
    # ================= Angola: IPS 2005
    dict(id="FR-I009", tipo="hecho_atribuido", id_fuente="F101", ubicacion="Párrafos 2 y 8-9",
         texto=f"{IPS}, unos 350.000 cubanos participaron en la guerra de Angola entre 1975 y 1988; el primer contingente "
               "militar llegó en octubre de 1975 a petición de Agostinho Neto, líder del MPLA, que fue presidente al "
               "declararse la independencia el 11 de noviembre, y la llegada de las tropas cubanas se consideró decisiva para que Luanda no cayera en manos "
               "de la UNITA, apoyada por Zaire, Estados Unidos y Sudáfrica."),
    dict(id="FR-I010", tipo="hecho_atribuido", id_fuente="F101", ubicacion="Párrafos 16-17",
         texto=f"{IPS}, según cifras del gobierno cubano, en todas las misiones «internacionalistas» en África, desde "
               "principios de los años sesenta hasta la salida del último soldado de Angola el 25 de mayo de 1991, murieron "
               "2.077 cubanos; los restos que pudieron recuperarse se repatriaron en diciembre de 1989, en la llamada "
               "Operación Tributo."),
    dict(id="FR-I011", tipo="hecho_atribuido", id_fuente="F101", ubicacion="Párrafo 18",
         texto=f"{IPS}, no hay estadísticas oficiales sobre los heridos, discapacitados o enfermos de la guerra, y los primeros "
               "casos de VIH/sida detectados en Cuba fueron de soldados que volvían de África a mediados de los años "
               "ochenta."),
    dict(id="FR-I012", tipo="hecho_atribuido", id_fuente="F101", ubicacion="Párrafos 3-6 y 11",
         texto=f"{IPS}, alistarse para Angola era oficialmente voluntario, pero negarse costaba la expulsión del Partido "
               "Comunista o de la Unión de Jóvenes Comunistas, y en una sociedad «machista» el que no iba se arriesgaba a "
               "que lo llamaran cobarde; un oficial retirado contó que fue porque quería, mientras otro cubano dijo de su "
               "hermanastro que «nunca menciona la guerra»."),
    dict(id="FR-I013", tipo="hecho_atribuido", id_fuente="F101", ubicacion="Párrafos 20, 24 y 26",
         texto=f"{IPS}, más de 50.000 civiles cubanos participaron en la ayuda no militar a Angola, en salud, educación y "
               "construcción; en la etapa final había unos 53.000 soldados cubanos en el país, y en julio de 1991 Nelson "
               "Mandela viajó a La Habana para agradecer a Fidel Castro el papel de Cuba en la lucha contra el apartheid."),
    # ================= Angola: la versión oficial (Fidel Castro, 2005)
    dict(id="FR-I014", tipo="postura", id_fuente="F102", ubicacion="Páginas 120-122", actor="gobierno_cubano",
         texto=f"{FC}, cuando las columnas sudafricanas avanzaban hacia Luanda solo había en Angola 480 instructores "
               "militares cubanos, llegados a petición de Neto para entrenar al nuevo ejército; ocho murieron en un ataque "
               "sudafricano a principios de noviembre de 1975, y entonces Cuba, en coordinación con Neto, decidió enviar "
               "tropas: así empezó la Operación Carlota, con 36.000 soldados cubanos."),
    dict(id="FR-I015", tipo="postura", id_fuente="F102", ubicacion="Página 123", actor="gobierno_cubano",
         texto=f"{FC}, los soviéticos «no fueron consultados» sobre la decisión cubana de enviar tropas, y después el "
               "gobierno soviético presionó «fuertemente» para una retirada rápida, preocupado por la reacción de Estados "
               "Unidos; Cuba aceptó, solo en parte, un plan de retirada gradual en tres años."),
    dict(id="FR-I016", tipo="postura", id_fuente="F102", ubicacion="Páginas 125-126", actor="gobierno_cubano",
         texto=f"{FC}, en 1987-1988 Cuba reunió 55.000 soldados en Angola; mientras en Cuito Cuanavale se detenía a las "
               "tropas sudafricanas, 40.000 soldados cubanos y 30.000 angolanos, con unos 600 tanques, avanzaban hacia la "
               "frontera de Namibia; Castro habla de «contundentes victorias» que obligaron a Sudáfrica a negociar los "
               "acuerdos firmados en la ONU en diciembre de 1988."),
    dict(id="FR-I017", tipo="postura", id_fuente="F102", ubicacion="Páginas 128-129", actor="gobierno_cubano",
         texto=f"{FC}, más de 300.000 combatientes y cerca de 50.000 colaboradores civiles cumplieron misión en Angola «de "
               "forma absolutamente voluntaria», 2.077 cubanos murieron en África, y Cuba fue «el único país no africano que "
               "combatió y derramó su sangre por África»; acusó a Estados Unidos de querer borrar el papel de Cuba y dijo "
               "que Cuba abriría progresivamente sus archivos a investigadores serios."),
    dict(id="FR-I018", tipo="cifra_disputada", id_fuente="F101", ubicacion="Párrafos 2 y 24 (F101); páginas 125 y 128 (F102)",
         corroborado_por=["F102"],
         texto="Las cifras de cubanos en Angola no coinciden: según Inter Press Service participaron unos 350.000 entre 1975 "
               "y 1988 y en la etapa final había unos 53.000 soldados, mientras que Fidel Castro habló en 2005 de más de "
               "300.000 combatientes y de 55.000 soldados reunidos en 1987-1988."),
    dict(id="FR-I019", tipo="cifra_disputada", id_fuente="F101", ubicacion="Párrafo 16 (F101); párrafo 37 (F108)",
         corroborado_por=["F108"],
         texto="La salida del último soldado cubano de Angola se fecha de forma distinta: según cifras del gobierno cubano "
               "citadas por Inter Press Service fue el 25 de mayo de 1991, mientras que el periodista Drew Forrest escribe "
               "que las últimas tropas cubanas se fueron en julio de 1991."),
    # ================= Cuito Cuanavale
    dict(id="FR-I020", tipo="hecho_atribuido", id_fuente="F108", ubicacion="Párrafos 15-22",
         texto=f"{MG}, Castro decidió hacer una defensa simbólica de Cuito Cuanavale y, sin informar a los soviéticos, envió "
               "15.000 de sus mejores soldados; entre enero y marzo de 1988 las tropas sudafricanas y de la UNITA lanzaron "
               "varios asaltos contra las defensas angolanas y cubanas sin lograr romperlas, y el último fue el 23 de "
               "marzo."),
    dict(id="FR-I021", tipo="hecho_atribuido", id_fuente="F108", ubicacion="Párrafos 26-27",
         texto=f"{MG}, la fuerza de defensa sudafricana (SADF) estima sus propias bajas en 31 muertos frente a 4.785 muertos "
               "de las fuerzas angolanas (FAPLA); el autor sostiene que esa comparación es engañosa porque la SADF usó poco "
               "su infantería y omite los 3.000 o más muertos de la UNITA."),
    dict(id="FR-I022", tipo="postura", id_fuente="F108", ubicacion="Párrafos 1-3 y 44-45", actor="Drew Forrest (periodista)",
         texto=f"{MG}, ningún relato creíble sostiene que la SADF sufriera en Cuito Cuanavale una «derrota aplastante», como "
               "dicen funcionarios cubanos, pero tampoco fue una victoria sudafricana, como sostienen veteranos de la SADF; "
               "el autor la describe como una victoria defensiva angolana y cubana y un serio revés para Sudáfrica, que "
               "minó su confianza militar."),
    dict(id="FR-I023", tipo="hecho_atribuido", id_fuente="F108", ubicacion="Párrafos 33-41",
         texto=f"{MG}, la salida de los cubanos de Angola se acordó en diciembre de 1988 entre Estados Unidos, Cuba, Angola y "
               "Sudáfrica; la SADF salió de Angola en agosto de 1988, Sudáfrica aceptó la independencia de Namibia bajo la "
               "Resolución 435 de la ONU, y en marzo de 1988 Castro abrió un nuevo frente en el suroeste con 40.000 "
               "soldados y 600 tanques que avanzaron hacia la frontera namibia."),
    # ================= Etiopía
    dict(id="FR-I024", tipo="hecho_atribuido", id_fuente="F103", ubicacion="Párrafos 1-3",
         texto=f"{LOC}, en 1977 la guerrilla somalí del Frente de Liberación de Somalia Occidental, apoyada por Somalia, tomó "
               "gran parte del Ogadén etíope; cuando la URSS siguió ayudando a Etiopía, Somalia expulsó a los asesores "
               "soviéticos, desde finales de noviembre llegó a Etiopía una ayuda militar soviética masiva y tropas cubanas "
               "trasladadas desde Angola; para fin de año habían llegado 17.000 cubanos que, junto al ejército etíope, "
               "frenaron la ofensiva."),
    dict(id="FR-I025", tipo="hecho_atribuido", id_fuente="F103", ubicacion="Párrafo 3",
         texto=f"{LOC}, el 13 de febrero de 1978 Somalia envió su ejército regular al Ogadén, pero fue rechazado hacia la "
               "frontera; tras la recuperación de Jijiga por el ejército etíope a principios de marzo, Somalia retiró sus "
               "fuerzas, y Etiopía quedó convertida en cliente militar de Moscú."),
    dict(id="FR-I026", tipo="cifra_disputada", id_fuente="F100", ubicacion="Párrafo 1 (F100); párrafo 3 (F103); 'Background' (F104)",
         corroborado_por=["F103", "F104"],
         texto="El número de soldados cubanos en Etiopía se da de forma distinta: 16.000 según el resumen del estudio de "
               "Gleijeses, 17.000 a finales de 1977 según la Biblioteca del Congreso de EE. UU. y entre 13.000 y 15.000 "
               "según el Departamento de Estado en 1981."),
    dict(id="FR-I027", tipo="postura", id_fuente="F104", ubicacion="Apartado 'Background'", actor="gobierno_eeuu",
         texto=f"{DE}, en Etiopía los soviéticos dieron el mando y control general, el material y el transporte a los "
               "13.000 a 15.000 soldados cubanos que combatían allí, y las costosas actividades de Cuba en el exterior "
               "habrían sido imposibles sin la ayuda soviética."),
    # ================= Centroamérica y Colombia
    dict(id="FR-I028", tipo="postura", id_fuente="F104", ubicacion="Apartado 'Nicaragua'", actor="gobierno_eeuu",
         texto=f"{DE}, Cuba ayudó a unificar las tres facciones del Frente Sandinista en 1977-1978, montó una red de "
               "suministro de armas a través de Panamá y Costa Rica, organizó una «brigada internacionalista» que combatió "
               "con los sandinistas en 1979 y puso asesores militares con sus columnas; después del triunfo había en "
               "Nicaragua unos 5.000 cubanos, entre asesores, maestros y médicos, de ellos más de 1.500 asesores militares "
               "y de seguridad."),
    dict(id="FR-I029", tipo="postura", id_fuente="F104", ubicacion="Apartados 'El Salvador' y 'Guatemala'", actor="gobierno_eeuu",
         texto=f"{DE}, Cuba coordinó envíos de armas de Vietnam, Etiopía y Europa del Este a la guerrilla salvadoreña a "
               "través de Nicaragua y entrenó a sus combatientes, y muchos de los 2.000 o más guerrilleros activos en "
               "Guatemala se entrenaron en Cuba; todo lo coordinaba el Departamento América del Partido Comunista de Cuba, "
               "creado en 1974 y dirigido por Manuel Piñeiro Losada."),
    dict(id="FR-I030", tipo="hecho_atribuido", id_fuente="F104", ubicacion="Apartados 'El Salvador' y 'Colombia'",
         texto=f"{DE}, en abril de 1981 Fidel Castro admitió ante el enviado de la Internacional Socialista "
               "Wischnewski que Cuba había enviado armas a la guerrilla salvadoreña, y el vicepresidente Carlos Rafael "
               "Rodríguez explicó en septiembre de 1981 que Cuba no negaba haber entrenado a guerrilleros del M-19 "
               "colombiano porque no podía negarse a enseñar técnicas de resistencia a revolucionarios latinoamericanos."),
    dict(id="FR-I031", tipo="postura", id_fuente="F105", ubicacion="Resumen inicial y párrafo 3", actor="gobierno_eeuu",
         texto=f"{LB}, varios países comunistas se comprometieron a dar a la guerrilla salvadoreña cerca de 800 toneladas de "
               "armas, y cerca de 200 toneladas llegaron en secreto, sobre todo a través de Cuba y Nicaragua, antes de la "
               "ofensiva de enero de 1981; el documento califica sus pruebas de «incontrovertibles»."),
    dict(id="FR-I032", tipo="hecho_atribuido", id_fuente="F106", ubicacion="Párrafos 2-9",
         texto=f"{CSM}, el Wall Street Journal y el Washington Post concluyeron que el Libro Blanco sobre El Salvador era, en el "
               "mejor de los casos, defectuoso; su responsable, Jon Glassman, admitió que partes podían ser «engañosas» y "
               "estar «adornadas», y los críticos dijeron que no había apoyo concreto para la cifra de 200 toneladas; el "
               "Departamento de Estado respondió con un documento guerrillero que hablaba de 109 toneladas de armas en "
               "Nicaragua el 1 de noviembre de 1980 y mantuvo sus conclusiones."),
    dict(id="FR-I033", tipo="hecho_atribuido", id_fuente="F107", ubicacion="Páginas 2-4",
         texto=f"{LG}, Cuba limitó su ayuda directa a la revolución nicaragüense hasta los últimos seis meses para no provocar "
               "una intervención de Estados Unidos; ayudó a preparar la «ofensiva final» del FMLN de enero de 1981, pero "
               "a las pocas semanas suspendió la ayuda militar y presionó por negociar, y la reanudó cuando Washington "
               "rechazó esos acercamientos; también usó la promesa de ayuda para empujar a los cinco grupos del FMLN a "
               "unificarse."),
    dict(id="FR-I034", tipo="postura", id_fuente="F107", ubicacion="Páginas 3-5", actor="William LeoGrande (politólogo)",
         texto=f"{LG}, el debate real no era si Cuba ayudaba a la guerrilla salvadoreña, sino si la guerra nacía de las "
               "condiciones internas o de La Habana y Moscú; LeoGrande sostiene que La Habana sabía que la guerra aumentaba "
               "el riesgo para la propia Cuba y que, al final de la Guerra Fría, se opuso a abandonar a los salvadoreños, lo "
               "que agrandó su ruptura con Moscú."),
    dict(id="FR-I035", tipo="hecho_atribuido", id_fuente="F107", ubicacion="Página 2 y nota 1",
         texto=f"{LG}, la participación cubana en El Salvador no era un secreto: Fidel Castro la reconoció ante "
               "representantes de la Unión Interparlamentaria en La Habana, y el vicepresidente Carlos Rafael Rodríguez la "
               "confirmó en 1982 a una delegación de especialistas estadounidenses en política exterior de la que formaba "
               "parte el propio LeoGrande."),
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
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]}.")
print(f"Añadidos {len(NUEVOS)} fragmentos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
