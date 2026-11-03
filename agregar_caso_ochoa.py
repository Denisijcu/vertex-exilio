"""
agregar_caso_ochoa.py — Etapa caso_ochoa_narcotrafico (módulo "Cuba: contexto").

Registra las fuentes F090-F098 y crea fuentes/fragmentos_caso_ochoa.jsonl (FR-O001 en adelante):
la Causa 1/89 (juicio y fusilamiento de Ochoa, De la Guardia, Martínez y Padrón), el viaje a Medellín para ver a
Pablo Escobar, la versión oficial de Fidel Castro, las acusaciones de EE. UU. contra Raúl Castro y otros
funcionarios (que nunca llegaron a juicio) y lo que dice Carlos Lehder.

Uso (desde E:\\vertex-exilio):
    python agregar_caso_ochoa.py

Criterios:
  - Lo probado en el juicio de 1989 (y aceptado por el propio gobierno cubano) se separa de las acusaciones
    posteriores, que nunca se juzgaron: el borrador de acusación de Miami de 1993 y los relatos de Lehder.
  - El discurso de Fidel Castro del 9 de julio de 1989 es postura del gobierno cubano, también sus cifras.
  - Las valoraciones de Julia Preston (p. ej. "la traición no quedó demostrada") van como postura con actor.
  - Contradicciones entre fuentes (fechas, papel de Ochoa) van como cifra_disputada.
  - No entran: la edad de Ochoa (Deseret y Preston no coinciden), el "siete fusilados" de Cunningham (error) ni
    las palabras "show trials", "régimen" o "dictadura" de las fuentes.

Qué hace:
  1. Comprueba que validar.py ya tiene la etapa caso_ochoa_narcotrafico.
  2. Copia de seguridad del registro (y del archivo de fragmentos si ya existiera).
  3. Añade F090-F098 al registro (si alguna ya existe, no toca nada).
  4. Crea el archivo de fragmentos en estado 'pendiente'.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_caso_ochoa.jsonl")
HOY = "2026-11-03"
T = "caso_ochoa_narcotrafico"

JP = "Según la periodista Julia Preston (The New York Review of Books, diciembre de 1989)"
FC = "Según Fidel Castro, en su discurso ante el Consejo de Estado del 9 de julio de 1989"
KR = "Según un reportaje de Jeff Leen (Knight-Ridder, abril de 1993) sobre un borrador de acusación de la fiscalía federal de Miami"
AI = "Según Amnistía Internacional (7 de julio de 1989)"

FUENTES = [
    ("F090", "The Trial that Shook Cuba (The New York Review of Books, 7 de diciembre de 1989)", "Julia Preston",
     "https://www.nybooks.com/articles/1989/12/07/the-trial-that-shook-cuba/", "periodistica", "revisar",
     "ninguna", "ambos",
     "Archivo fuentes/docs/NYRB_1989_preston.html. Crónica larga del juicio, con testimonios y cifras de la acusación "
     "cubana. Las valoraciones de la autora van como postura. Su lenguaje ('show trials', 'regime') no entra."),
    ("F091", "Más información sobre AU 216/89 - Pena de muerte, Cuba (AMR 25/09/89/s, 7 de julio de 1989)",
     "Amnistía Internacional", "https://www.amnesty.org/ar/wp-content/uploads/sites/4/2021/06/amr250091989es.pdf",
     "ong", "revisar", "organismo_internacional", "ambos",
     "Archivo fuentes/docs/AMNISTIA_1989.pdf. Escrito antes de las ejecuciones. Sus preocupaciones: postura."),
    ("F092", "Cuban hero, 3 others executed for drug crimes (13 de julio de 1989)", "Deseret News",
     "https://www.deseret.com/1989/7/13/18815336/cuban-hero-3-others-executed-for-drug-crimes/", "periodistica",
     "revisar", "ninguna", "hechos",
     "Archivo fuentes/docs/DESERET_1989_ejecuciones.html. Da 57 años a Ochoa y Preston dice que tenía poco más de "
     "cuarenta: la edad no entra. Escribe 'Armado Padron' por Amado Padrón."),
    ("F093", "Texto íntegro de la intervención de Fidel Castro en la reunión del Consejo de Estado sobre la Causa No. 1 "
             "de 1989 (9 de julio de 1989)", "Fidel Castro Ruz; servicio especial de Prensa Latina",
     "https://sitiosdememoria.uy/sites/default/files/2026-08/19/texto-integro_f16-7-1989.pdf", "primaria",
     "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/FIDEL_1989_consejo_estado.pdf (escaneo con OCR, copia del sitio uruguayo Sitios de "
     "Memoria). Versión oficial del gobierno cubano: todo como postura, cifras incluidas."),
    ("F094", "The U.S. drug case against Cuba: smuggling probe names Raúl Castro, other officials (8 de abril de 1993)",
     "Jeff Leen, Knight-Ridder Newspapers (publicado en The Seattle Times)",
     "https://archive.seattletimes.com/archive/19930408/1694969/the-us-drug-case-against-cuba----smuggling-probe-names-raul-castro-other-officials",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/SEATTLE_1993_acusacion.html. Describe un BORRADOR de acusación que leyó un reportero del "
     "Miami Herald: son acusaciones de la fiscalía, nunca presentadas ni juzgadas (ver F098)."),
    ("F095", "Witness links Cubans with Medellín cartel (27 de noviembre de 1991)", "Deseret News",
     "https://www.deseret.com/1991/11/27/18953940/witness-links-cubans-with-medellin-cartel/", "periodistica",
     "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/DESERET_1991_lehder.html. Testimonio de Carlos Lehder en el juicio de Noriega: lo que dice "
     "Lehder es testimonio de un narcotraficante condenado que coopera con la fiscalía."),
    ("F096", "Exaliado de Pablo Escobar narra supuestos negocios con Cuba y los sandinistas (15 de enero de 2024)",
     "AFP, publicado por TVN Panamá",
     "https://www.tvn-2.com/mundo/exaliado-pablo-escobar-narra-supuestos-negocios-cuba-sandinistas_1_2102184.html",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/AFP_2024_lehder.html. Lo que cuenta Lehder en su libro: postura (no probado en juicio, "
     "como aclara AFP). 'Régimen' es lenguaje de la nota: no entra."),
    ("F097", "Cuba-Drugs: Release of former general raises spectre of scandal (19 de marzo de 1997)",
     "Dalia Acosta, Inter Press Service (La Habana)", "https://www.ipsnews.net/?p=60027", "periodistica", "revisar",
     "ninguna", "ambos",
     "Archivo fuentes/docs/IPS_1997_patricio.html. Atribuye a 'fuentes oficiales' que Ochoa y De la Guardia "
     "organizaron dos redes; Preston (F090) dice que los Castro nunca acusaron a Ochoa de participar en los envíos "
     "de De la Guardia: va como dato disputado."),
    ("F098", "Trump administration prepares to seek Raúl Castro indictment as it pressures Cuba (15 de mayo de 2026)",
     "Joshua Goodman, Alanna Durkin Richer y Eric Tucker, Associated Press (publicado por PBS NewsHour)",
     "https://www.pbs.org/newshour/world/trump-administration-prepares-to-seek-raul-castro-indictment-as-it-pressures-cuba-ap-sources-say",
     "periodistica", "revisar", "ninguna", "hechos",
     "Archivo fuentes/docs/AP_2026_acusacion_raul.html. Solo se usa lo que dice de 1993 (la acusación por drogas "
     "que nunca se presentó). La acusación de 2026 por el derribo de las avionetas de 1996 es otro tema."),
]

NUEVOS = [
    # ================= el juicio: hechos básicos
    dict(id="FR-O001", tipo="hecho", id_fuente="F091", ubicacion="Primer párrafo (F091); sección 1 (F090); párrafo 6 (F092)",
         corroborado_por=["F090", "F092"],
         texto="En la Causa 1 de 1989 un tribunal militar especial juzgó a 14 oficiales del ejército y del Ministerio del "
               "Interior de Cuba; cuatro fueron condenados a muerte, el general Arnaldo Ochoa Sánchez, el capitán Jorge "
               "Martínez Valdés, el coronel Antonio de la Guardia Font y el mayor Amado Padrón Trujillo, y los otros 10 a "
               "penas de entre 10 y 30 años de prisión."),
    dict(id="FR-O002", tipo="hecho", id_fuente="F090", ubicacion="Sección 1 (F090); párrafos 1-2 (F092)",
         corroborado_por=["F092"],
         texto="Ochoa, De la Guardia, Martínez y Padrón fueron fusilados al amanecer del 13 de julio de 1989, después de "
               "que el Consejo de Estado ratificara las condenas a muerte."),
    dict(id="FR-O003", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 1",
         texto=f"{JP}, Ochoa fue arrestado en La Habana el 12 de junio de 1989; trece días después compareció ante un "
               "tribunal de honor de cuarenta y siete generales y almirantes y confesó todos los cargos; el consejo de "
               "guerra empezó el 30 de junio, duró ocho días, y el 7 de julio diez acusados fueron condenados a prisión."),
    dict(id="FR-O004", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 1",
         texto=f"{JP}, el juicio se grabó en video y se transmitió por televisión en Cuba con dos días de retraso para "
               "editarlo, en total más de veintitrés horas; Fidel Castro admitió que se cortaron partes, y los acusados "
               "omitieron los nombres de varios extranjeros a los que se atribuía un papel importante en el narcotráfico."),
    dict(id="FR-O005", tipo="hecho_atribuido", id_fuente="F091", ubicacion="Primer párrafo",
         texto=f"{AI}, el juicio duró 4 días ante un tribunal militar especial; la fiscalía, dirigida por el ministro de "
               "Justicia, general Juan Escalona Reguera, pidió la pena de muerte para siete de los catorce acusados, y los "
               "cargos incluían alta traición y «actos hostiles contra un Estado extranjero», en referencia a Estados "
               "Unidos, por su presunta relación con narcotraficantes colombianos que querían usar Cuba como escala para "
               "llevar cocaína a Estados Unidos."),
    dict(id="FR-O006", tipo="postura", id_fuente="F091", ubicacion="Párrafo 3", actor="Amnistía Internacional",
         texto=f"{AI}, la organización se opone a la pena de muerte en todos los casos, le preocupaba que «consideraciones "
               "políticas» hubieran influido indebidamente en la dirección y el resultado del juicio, y temía que no se "
               "hubieran respetado las normas internacionales de un juicio con las debidas garantías; pidió conmutar las "
               "cuatro condenas a muerte."),
    dict(id="FR-O007", tipo="hecho_atribuido", id_fuente="F092", ubicacion="Párrafos 4-5",
         texto="Según el Deseret News (13 de julio de 1989), los 29 miembros del Consejo de Estado votaron por unanimidad "
               "ratificar las condenas a muerte, y Fidel Castro, en una intervención de cinco horas, sostuvo que los "
               "cuatro debían ser fusilados para restaurar la fe en la Revolución, asegurar la disciplina en las fuerzas "
               "armadas y dar un ejemplo."),
    # ================= la versión oficial (Fidel Castro, 9 de julio de 1989)
    dict(id="FR-O008", tipo="postura", id_fuente="F093", ubicacion="Apartado inicial", actor="gobierno_cubano",
         texto=f"{FC}, el proceso se caracterizó por su «excepcional limpieza» y «nunca hubo un proceso judicial con tanta "
               "participación, con tanta información, con tanta claridad y con tanta equidad»; afirmó que no se ejerció "
               "«la más mínima influencia» sobre el tribunal, que los jueces decidieron «con absoluta libertad» y que "
               "fueron ellos quienes redujeron el número de condenas a muerte que pedía el fiscal."),
    dict(id="FR-O009", tipo="postura", id_fuente="F093", ubicacion="Apartado 'Socios con la mafia de la droga'",
         actor="gobierno_cubano",
         texto=f"{FC}, enviar a Martínez a Colombia «con pasaporte falso, a ponerlo en manos del enemigo», cuando en Angola "
               "se libraban batallas decisivas, fue «un hecho de gravedad extrema»; dijo que Ochoa conspiró para "
               "transportar grandes cantidades de droga a través de Cuba pero no logró realizar ninguna de esas "
               "operaciones, y que lo grave fue que, sabiendo que en el departamento MC del Ministerio del Interior se había "
               "creado una «mafia» que traficaba drogas, se asoció a ella en vez de denunciarla."),
    dict(id="FR-O010", tipo="postura", id_fuente="F093", ubicacion="Páginas 24-26", actor="gobierno_cubano",
         texto=f"{FC}, «la traición es vender al país y vendieron al país»; sostuvo que sin un «castigo ejemplar» el "
               "precedente sería «funesto y desmoralizador» para la disciplina de las fuerzas armadas y del Ministerio "
               "del Interior, y que «hoy la revolución no puede ser generosa sin hacerse un profundo daño a sí misma»."),
    dict(id="FR-O011", tipo="postura", id_fuente="F093", ubicacion="Apartado 'La consulta a organismos e instituciones'",
         actor="gobierno_cubano",
         texto=f"{FC}, antes de decidir se consultó al Buró Político, que pidió por unanimidad la pena más severa, al "
               "Comité Central, de cuyos 162 miembros presentes 10 se opusieron, y a los diputados de la Asamblea "
               "Nacional, de los que solo uno de 402 se pronunció por conmutar la pena; dijo que el tribunal fue "
               "«generoso» y que casi todos los acusados podían haber sido condenados a muerte."),
    dict(id="FR-O012", tipo="postura", id_fuente="F093", ubicacion="Página 24", actor="gobierno_cubano",
         texto=f"{FC}, la investigación sobre drogas empezó a partir de lo que se encontró en casa de Martínez: una carta, un "
               "libro sobre la mafia y una pequeña tarjeta de un hotel de Medellín; Patricio y Antonio de la Guardia "
               "habían sido detenidos por las operaciones de Angola, el tráfico de marfil y diamantes y otras "
               "irregularidades."),
    dict(id="FR-O013", tipo="postura", id_fuente="F093", ubicacion="Páginas 18-19", actor="gobierno_cubano",
         texto=f"{FC}, Estados Unidos empezó «de mala fe» a involucrar el nombre de Raúl Castro porque los aviones del grupo "
               "de De la Guardia aterrizaban en áreas militares; calificó de «cuatro miserables dólares» lo que recaudó ese "
               "grupo y afirmó que «es inviable una revolución que tenga que depender del narcotráfico»; reprochó además a "
               "Estados Unidos no haber avisado a Cuba de los nombres que ya conocía."),
    dict(id="FR-O014", tipo="postura", id_fuente="F090", ubicacion="Sección 3", actor="gobierno_cubano",
         texto=f"{JP}, Raúl Castro, ministro de las Fuerzas Armadas, pidió ante el tribunal de honor un «castigo ejemplar» "
               "para Ochoa, dijo que lo había dominado la «fiebre del oro» y afirmó que «su máxima aspiración era "
               "convertirse en un típico empresario capitalista»."),
    # ================= qué se probó: el grupo de Tony de la Guardia
    dict(id="FR-O015", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 2",
         texto=f"{JP}, Antonio «Tony» de la Guardia dirigía el departamento MC del Ministerio del Interior, creado a "
               "principios de los años ochenta para burlar el embargo estadounidense llevando de contrabando tecnología "
               "médica e informática desde la Florida; el gobierno cubano acusó a su grupo de hacer pasar por Cuba seis "
               "toneladas de cocaína colombiana hacia Estados Unidos en los dos años posteriores a abril de 1987, a cambio "
               "de 3,4 millones de dólares."),
    dict(id="FR-O016", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 4",
         texto=f"{JP}, el primer cargamento llegó el 10 de abril de 1987: 240 kilos de cocaína aterrizaron con escolta de la "
               "fuerza aérea cubana en la base militar de Varadero y pasaron a lanchas rápidas guiadas por los "
               "guardacostas cubanos hacia la Florida; hubo quince envíos exitosos, más de una tonelada se perdió en "
               "decomisos, y tras los arrestos los investigadores recuperaron 156 kilos de cocaína y 1,1 millones de "
               "dólares en efectivo."),
    dict(id="FR-O017", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Secciones 2 y 4",
         texto=f"{JP}, en febrero de 1988 los cubanoamericanos Reinaldo y Rubén Ruiz fueron arrestados en Miami por "
               "introducir en Estados Unidos, a través de Cuba, drogas del cártel de Medellín, y se declararon culpables "
               "en marzo de 1989; un piloto informante de la DEA voló para ellos a Varadero, y los Ruiz quedaron grabados en "
               "video presumiendo de sus operaciones en Cuba."),
    # ================= qué se probó: Ochoa y Escobar
    dict(id="FR-O018", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 2 y sección 4",
         texto=f"{JP}, los Castro nunca sostuvieron que Ochoa participara en los envíos de cocaína de De la Guardia; a Ochoa "
               "se le acusó de enriquecerse en el mercado negro de Angola con recursos del ejército, de quedarse con "
               "161.000 dólares del ejército sandinista por una compra fallida de armas, de los que Martínez depositó "
               "115.000 en una cuenta en Panamá, y de planear grandes envíos de cocaína."),
    dict(id="FR-O019", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 4",
         texto=f"{JP}, en mayo de 1988 Martínez se reunió en Medellín con Pablo Escobar por orden de Ochoa; según Martínez, "
               "Escobar quería misiles tierra-aire para derribar helicópteros antidrogas colombianos y refugio en Cuba, y "
               "la idea de un laboratorio de cocaína en Cuba o Angola fue rechazada; no salió en el juicio ninguna prueba "
               "de que Ochoa llegara a hacer algo por Escobar, aunque él dijo que esperaba hacer «grandes negocios» con el "
               "cártel por Panamá y México, sin pasar droga por Cuba."),
    dict(id="FR-O020", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 1",
         texto=f"{JP}, Ochoa declaró ante el tribunal de honor que ni Fidel ni Raúl Castro ni nadie del partido o del "
               "gobierno «tuvo nunca nada que ver», dijo que «la traición se paga con la vida» y cerró afirmando que, si "
               "lo fusilaban, su último pensamiento sería para Fidel."),
    dict(id="FR-O021", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 5",
         texto=f"{JP}, Fidel Castro afirmó que él y Raúl no supieron de la relación de Ochoa ni de De la Guardia con las "
               "drogas hasta después de los arrestos del 12 de junio; en cambio, Reinaldo Ruiz dijo a investigadores "
               "estadounidenses que Raúl Castro estaba en la base de Varadero cuando llegó el primer cargamento, aunque no "
               "trataron directamente con él."),
    dict(id="FR-O022", tipo="cifra_disputada", id_fuente="F097", ubicacion="Párrafos 7-8 (F097); sección 2 (F090)",
         corroborado_por=["F090"],
         texto="El papel de Ochoa en el narcotráfico se cuenta de forma distinta: según Inter Press Service, que cita "
               "fuentes oficiales cubanas, Antonio de la Guardia y Ochoa organizaron dos redes que dejaron pasar seis "
               "toneladas de cocaína por Cuba; según la periodista Julia Preston, los Castro nunca sostuvieron que Ochoa "
               "participara en esos envíos ni que llegara a realizar una operación de narcotráfico."),
    dict(id="FR-O023", tipo="cifra_disputada", id_fuente="F094", ubicacion="Apartado 'Early marijuana case' (F094); sección 2 (F090)",
         corroborado_por=["F090"],
         texto="El período del narcotráfico del grupo de De la Guardia se da de forma distinta: según el reportaje de "
               "Knight-Ridder de 1993, los fiscales cubanos los acusaron de pasar 6 toneladas de cocaína entre 1986 y "
               "1989, mientras que según Julia Preston la acusación hablaba de seis toneladas en los dos años posteriores "
               "a abril de 1987."),
    # ================= críticas y consecuencias
    dict(id="FR-O024", tipo="postura", id_fuente="F090", ubicacion="Secciones 1, 2 y 4", actor="Julia Preston (periodista)",
         texto=f"{JP}, los acusados nunca pudieron dar su propia versión, sus abogados militares apenas intervinieron y no "
               "había forma de saber qué presiones produjeron las confesiones; la autora sostiene que la traición se "
               "afirmó en la retórica de los Castro y en la confesión de Ochoa, pero «no quedó demostrada por los "
               "hechos», y que Ochoa fue ejecutado por su impaciencia con una realidad en la que los Castro no permiten que "
               "nadie fuera de su control cuestione sus políticas, no por actos concretos."),
    dict(id="FR-O025", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 2",
         texto=f"{JP}, el 29 de junio de 1989 Fidel Castro destituyó al ministro del Interior, José Abrantes, y lo sustituyó "
               "por Abelardo Colomé Ibarra; Abrantes fue arrestado el 31 de julio y el 1 de septiembre condenado a veinte "
               "años por negligencia y corrupción, aunque no se presentó prueba de que estuviera vinculado directamente "
               "con Ochoa ni con el narcotráfico."),
    dict(id="FR-O026", tipo="hecho_atribuido", id_fuente="F094", ubicacion="Apartado 'Inside Interior Ministry'",
         texto=f"{KR}, el exministro del Interior José Abrantes, condenado por no impedir el narcotráfico en su ministerio, "
               "murió dos años después de un ataque al corazón en su celda."),
    dict(id="FR-O027", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 2",
         texto=f"{JP}, después del juicio fue arrestado Elizardo Sánchez Santa Cruz, principal figura del movimiento de "
               "derechos humanos en Cuba, junto con otros dos disidentes, acusados de «difundir noticias falsas» por "
               "criticar en entrevistas con periodistas estadounidenses la falta de defensa de los acusados; Sánchez había "
               "dicho que el juicio fue «un asesinato público vestido de ropa judicial»."),
    dict(id="FR-O028", tipo="hecho_atribuido", id_fuente="F097", ubicacion="Párrafos 1-6",
         texto="Según Inter Press Service (marzo de 1997), Patricio de la Guardia, hermano gemelo de Antonio, condenado a 30 "
               "años por saber de las actividades de su hermano y de Ochoa y no denunciarlas, salió de prisión casi ocho "
               "años después; un profesor universitario dijo a IPS que «el caso Ochoa no es un caso cerrado», y el fiscal "
               "del caso, Juan Escalona, lo describió como «traumático» y «un deber amargo»."),
    dict(id="FR-O029", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 3",
         texto=f"{JP}, Ochoa combatió desde joven en la Sierra Maestra, fue nombrado Héroe de la República en 1984, dirigió "
               "las tropas cubanas en el Ogadén etíope en 1977, encabezó a los asesores militares cubanos en Nicaragua y "
               "luego la misión militar en Angola; iba a asumir el mando del Ejército Occidental el 14 de junio de 1989, "
               "dos días después de su arresto."),
    # ================= acusaciones anteriores y posteriores (no juzgadas en Cuba)
    dict(id="FR-O030", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 5",
         texto=f"{JP}, en 1982 Estados Unidos desarticuló una red del financiero colombiano Jaime Guillot Lara que llevaba "
               "marihuana a Estados Unidos y fusiles a la guerrilla colombiana M-19; un acusado, Johnny Crump, testificó "
               "en la Florida que era el enlace con el embajador cubano en Colombia, Fernando Ravelo Renedo, que fue "
               "acusado en Estados Unidos pero en 1989 era embajador de Cuba en Nicaragua; Cuba dio refugio a Guillot."),
    dict(id="FR-O031", tipo="hecho_atribuido", id_fuente="F094", ubicacion="Apartado 'Early marijuana case'",
         texto=f"{KR}, en 1982 cuatro funcionarios cubanos, entre ellos un vicealmirante de la marina, fueron acusados en "
               "Estados Unidos de introducir marihuana en la Florida, pero nunca fueron arrestados ni juzgados."),
    dict(id="FR-O032", tipo="hecho_atribuido", id_fuente="F090", ubicacion="Sección 5",
         texto=f"{JP}, el panameño José Blandón declaró ante el Senado de Estados Unidos que en junio de 1984 Fidel Castro "
               "medió en La Habana en una disputa entre Manuel Noriega y el cártel de Medellín, algo que Castro negó "
               "rotundamente; y una acusación federal de abril de 1989 en Jacksonville sostuvo que Carlos Lehder pasó una "
               "tonelada y media de cocaína por Cuba en 1984 con ayuda de Robert Vesco."),
    dict(id="FR-O033", tipo="hecho_atribuido", id_fuente="F094", ubicacion="Párrafos 1-8 y apartado 'Pressure on Cuba'",
         texto=f"{KR}, el borrador, de 17 páginas, acusaba al gobierno cubano de ser una organización criminal y a Raúl "
               "Castro de dirigir durante diez años una conspiración con el cártel de Medellín para pasar al menos 7,5 "
               "toneladas de cocaína por Cuba entre 1980 y 1990, con 15 funcionarios como coconspiradores, entre ellos "
               "Manuel Piñeiro, Abelardo Colomé y José Abrantes; no nombraba a Fidel Castro, que había negado durante años "
               "que su gobierno permitiera el narcotráfico."),
    dict(id="FR-O034", tipo="hecho_atribuido", id_fuente="F094", ubicacion="Apartado 'High-level approval'",
         texto=f"{KR}, el borrador acusaba a los cubanos de dar a los narcotraficantes frecuencias de radio especiales para "
               "cruzar el espacio aéreo, avisarles por radar de los guardacostas estadounidenses y dejar vivir en Cuba a "
               "jefes del cártel; se basaba en viejos casos de Miami, en desertores cubanos y en el testimonio de Carlos "
               "Lehder, y no mencionaba a Ochoa."),
    dict(id="FR-O035", tipo="hecho_atribuido", id_fuente="F098", ubicacion="Párrafo sobre 1993",
         texto="Según Associated Press (mayo de 2026), en 1993 los fiscales federales de Miami estudiaron acusar a Raúl "
               "Castro y a otros altos mandos militares cubanos de narcotráfico, a partir de testimonios de narcotraficantes "
               "colombianos surgidos en el juicio de Noriega, pero la acusación nunca se presentó, por dudas sobre la "
               "credibilidad del testigo y por el temor a poner en riesgo operaciones de inteligencia y el acercamiento "
               "del gobierno de Clinton."),
    dict(id="FR-O036", tipo="hecho_atribuido", id_fuente="F095", ubicacion="Párrafos 1-8",
         texto="Según el Deseret News (noviembre de 1991), Carlos Lehder, exjefe del cártel de Medellín, declaró en el juicio "
               "de Manuel Noriega que era el enlace del cártel con Raúl Castro y con Manuel Piñeiro, que viajó a Cuba por "
               "primera vez en 1981, le regaló un avión a Raúl Castro, cerró un acuerdo en 1982 y pasó varios cargamentos "
               "por Cuba en 1983 y 1984; reconoció que colaboraba con agentes federales, y un portavoz del gobierno cubano "
               "había negado con fuerza sus acusaciones la semana anterior."),
    dict(id="FR-O037", tipo="cifra_disputada", id_fuente="F094", ubicacion="Apartado 'High-level approval' (F094); párrafo 6 (F095)",
         corroborado_por=["F095"],
         texto="La fecha del primer viaje de Carlos Lehder a Cuba se da de forma distinta: según el borrador de acusación "
               "de Miami descrito por Knight-Ridder en 1993, viajó en 1979, mientras que según su propio testimonio en el "
               "juicio de Noriega, recogido por el Deseret News en 1991, fue en 1981."),
    dict(id="FR-O038", tipo="postura", id_fuente="F096", ubicacion="Párrafos 1-10",
         actor="Carlos Lehder (narcotraficante condenado)",
         texto="Según AFP (enero de 2024), Carlos Lehder afirma en su libro «Vida y muerte del Cartel de Medellín» que "
               "contrató con el gobierno cubano, con autorización de Pablo Escobar y Gustavo Gaviria, una ruta para llevar "
               "cocaína a las Bahamas, que acordó con Antonio de la Guardia el uso de pistas de aterrizaje con permiso de "
               "«sus superiores» y que no habría podido entrar a Cuba en su avión «sin la venia de Fidel Castro»; AFP "
               "aclara que esos hechos no han sido juzgados."),
    dict(id="FR-O039", tipo="cifra_disputada", id_fuente="F091", ubicacion="Primer párrafo (F091); sección 1 (F090)",
         corroborado_por=["F090"],
         texto="La duración del juicio se da de forma distinta: según Amnistía Internacional fue un juicio de 4 días ante un "
               "tribunal militar especial, mientras que según Julia Preston el consejo de guerra empezó el 30 de junio de "
               "1989 y duró ocho días."),
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
