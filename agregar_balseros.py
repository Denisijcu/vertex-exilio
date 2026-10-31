"""
agregar_balseros.py — Abre la etapa de la crisis de los balseros (1994-1995):
registra las fuentes F040-F045 y crea fuentes/fragmentos_balseros_1994.jsonl.

Uso (desde E:\\vertex-exilio):
    python agregar_balseros.py

Documentos leídos (en fuentes/docs): GAO_1995_crisis_migratoria.htm, CRS_RS20468_2006.pdf,
FIU_crisis_balseros.pdf, WIKI_rafter_crisis_1994.html, WIKI_maleconazo.html,
"Crisis de los balseros.md" (copia de EcuRed traducida al inglés). La página o sección va en 'ubicacion'.
El informe GAO es texto plano sin páginas: la ubicación es la sección ("Letter :2", etc.).

Qué hace:
  1. Copia de seguridad del registro.
  2. Añade F040-F045 al registro (si ya existen, no hace nada).
  3. Crea fuentes/fragmentos_balseros_1994.jsonl con todos los fragmentos en 'pendiente'
     (si el archivo ya existe, no lo toca).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_balseros_1994.jsonl")
HOY = "2026-10-30"
ETAPA = "balseros_1994"

FUENTES = [
    ("F040", "Cuba: U.S. Response to the 1994 Cuban Migration Crisis (GAO/NSIAD-95-211, 18 de septiembre de 1995)",
     "US General Accounting Office (GAO)", "https://www.gao.gov/products/nsiad-95-211", "primaria",
     "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/GAO_1995_crisis_migratoria.htm (texto plano, sin páginas: ubicación = sección). "
     "Datos = hechos; su juicio sobre las condiciones de los campamentos ('adequate') = postura de EE. UU. "
     "OJO: el resumen inicial da un costo de 533 millones y la tabla 2 da 497,2; se usa la tabla."),
    ("F041", "Cuban Migration Policy and Issues (CRS RS20468, actualizado el 19 de enero de 2006)",
     "Ruth Ellen Wasem, Congressional Research Service", "https://crsreports.congress.gov/product/pdf/RS/RS20468",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "hechos",
     "Archivo fuentes/docs/CRS_RS20468_2006.pdf (6 págs.). OJO: el enlace de CRS puede servir una versión más "
     "nueva; la que leímos es la de 2006. En la p. 5 trae erratas: '433,00' y '541,00' (se entiende 433.000 y 541.000)."),
    ("F042", "Una visión de la crisis de los balseros en el XX aniversario",
     "Siro del Castillo - ponencia en el simposio del Instituto de Investigaciones Cubanas de FIU, 4 de septiembre de 2014",
     "https://cri.fiu.edu/", "academica", "revisar", "academica", "ambos",
     "Archivo fuentes/docs/FIU_crisis_balseros.pdf (11 págs.). Describe los campamentos de Guantánamo. Sus juicios "
     "('inhumanas', 'página gris', 'trato discriminatorio') = postura del autor. Dice que 'pies secos, pies mojados' "
     "se practica desde abril de 1999, distinto de CRS: va como cifra disputada. URL exacta del PDF: a completar."),
    ("F043", "1994 Cuban rafter crisis", "Wikipedia", "https://en.wikipedia.org/wiki/1994_Cuban_rafter_crisis",
     "enciclopedia", "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_rafter_crisis_1994.html (descargado el 2026-10-30). Artículo corto; dice 'unos "
     "20.000' detenidos en la base, muy por debajo de GAO y FIU: va como cifra disputada."),
    ("F044", "Maleconazo", "Wikipedia", "https://en.wikipedia.org/wiki/Maleconazo", "enciclopedia", "CC-BY-SA-4.0",
     "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_maleconazo.html (descargado el 2026-10-30). Los 'objetivos' de la ficha (renuncia de "
     "Castro, elecciones, etc.) no tienen fuente clara y no entran. Datos solo con atribución."),
    ("F045", "Crisis de los Balseros", "EcuRed (copia traducida al inglés guardada por Denis)",
     "https://www.ecured.cu/Crisis_de_los_Balseros", "enciclopedia", "revisar", "gobierno_cubano", "postura",
     "Archivo 'fuentes/docs/Crisis de los balseros.md'. Enciclopedia oficial cubana; cita gacetadejagua.cu y "
     "revistacaliban.cu. SOLO para documentar la versión oficial cubana. Nunca sostiene un hecho ni una cifra."),
]

# (id, tipo, fuente, ubicación, corroborado_por, actor, texto)
FRAGMENTOS = [
    # ---------------- antecedentes
    ("FR-B001", "hecho", "F041", "p. 1", ["F043"], None,
     "Las salidas de balseros cubanos subieron de unos pocos cientos en 1989 a unos pocos miles en 1993; Wikipedia "
     "cifra en 3.676 los cubanos interceptados por la Guardia Costera de Estados Unidos en 1993."),
    ("FR-B002", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, en los primeros seis meses de 1993 la Guardia Costera de Estados Unidos recogió a unos 1.300 "
     "balseros cubanos y los llevó a Estados Unidos; en el mismo período de 1994 fueron unos 4.700."),
    ("FR-B003", "hecho", "F042", "p. 1", ["F044"], None,
     "El aumento de las salidas ilegales a principios de los años noventa coincidió con una crisis económica grave en "
     "Cuba tras la desaparición del bloque comunista de Europa del Este y de la Unión Soviética, la etapa que el "
     "gobierno cubano llamó 'Período Especial'."),
    ("FR-B004", "hecho_atribuido", "F044", "Background", [], None,
     "Según Wikipedia, tras la caída de la Unión Soviética Cuba perdió cerca del 80 % de su comercio y su principal "
     "proveedor de alimentos y combustible, y hubo apagones de hasta veinte horas."),
    ("FR-B005", "hecho_atribuido", "F042", "p. 1", [], None,
     "Según Siro del Castillo, otra causa del aumento de las salidas fue que Estados Unidos no cumplió el acuerdo "
     "migratorio de 1987, que permitía hasta 20.000 visas al año: entre 1987 y 1994 solo se otorgaron 11.222 visas."),
    ("FR-B006", "postura", "F045", "Background", [], "gobierno_cubano",
     "Según EcuRed, entre 1991 y 1994 Estados Unidos recibió 12.808 inmigrantes cubanos indocumentados y aceptó solo "
     "3.794 solicitudes de entrada legal, y la crisis de 1994 se debió a la política estadounidense de acoger a todo "
     "cubano que llegara a sus costas."),
    # ---------------- escalada del verano de 1994
    ("FR-B007", "hecho", "F042", "p. 1", ["F040"], None,
     "En el verano de 1994 hubo varios intentos de llevarse por la fuerza remolcadores y otras embarcaciones de la "
     "bahía de La Habana para llegar a Estados Unidos."),
    ("FR-B008", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, en junio de 1994 las autoridades cubanas mataron a tiros a un cubano que intentaba escapar de la "
     "isla, y entre el 13 de julio y el 8 de agosto de 1994 murieron al menos 37 personas que intentaban salir y 2 "
     "funcionarios cubanos en una serie de secuestros de embarcaciones."),
    ("FR-B009", "hecho_atribuido", "F044", "Background", [], None,
     "Según Wikipedia, el 13 de julio de 1994 un grupo de cubanos se llevó el remolcador '13 de Marzo' para intentar "
     "llegar a Estados Unidos, y la embarcación se hundió poco después de salir de la costa con muchos muertos."),
    ("FR-B010", "postura", "F044", "Background", [], "sobrevivientes",
     "Según Wikipedia, los sobrevivientes del remolcador '13 de Marzo' afirmaron que la embarcación fue hundida a "
     "propósito por los guardafronteras cubanos."),
    ("FR-B011", "postura", "F044", "Background", [], "gobierno_cubano",
     "Según Wikipedia, el gobierno cubano negó con firmeza que el remolcador '13 de Marzo' hubiera sido hundido a "
     "propósito."),
    # ---------------- el Maleconazo (5 de agosto de 1994)
    ("FR-B012", "hecho", "F040", "Letter :2", ["F044"], None,
     "El 5 de agosto de 1994 estallaron disturbios en La Habana, en la zona del Malecón, el episodio conocido como "
     "el Maleconazo."),
    ("FR-B013", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, el disturbio del 5 de agosto de 1994 empezó cuando la policía intentó dispersar a una multitud que "
     "se había reunido por un rumor falso de que una flotilla de barcos venía a recoger a quienes quisieran irse."),
    ("FR-B014", "hecho_atribuido", "F044", "Protests", [], None,
     "Según Wikipedia, el 5 de agosto de 1994 las autoridades descubrieron una vía de salida ilegal que usaban muchos "
     "cubanos, cerraron el paso por el Malecón para impedir las salidas y la gente salió a la calle a protestar."),
    ("FR-B015", "postura", "F045", "Events", [], "gobierno_cubano",
     "Según EcuRed, el disturbio del 5 de agosto de 1994 se produjo después de que Radio Martí anunciara que venían "
     "barcos a La Habana a recoger a quienes se reunieran en el Malecón; al no llegar ningún barco, la gente apedreó "
     "comercios y agredió a personas, entre ellas policías."),
    ("FR-B016", "hecho_atribuido", "F044", "Protests", [], None,
     "Según Wikipedia, durante el Maleconazo se rompieron vidrieras y se saquearon tiendas, los manifestantes gritaron "
     "\"¡Libertad!\" y \"¡Abajo los Castro!\", y fue el mayor desafío público al gobierno desde 1959."),
    ("FR-B017", "hecho_atribuido", "F044", "Police response", [], None,
     "Según Wikipedia, a los manifestantes los enfrentaron policías armados, agentes de la Seguridad del Estado y "
     "paramilitares, y varios videos y testimonios muestran a esas fuerzas disparando y golpeando a manifestantes."),
    ("FR-B018", "hecho_atribuido", "F044", "Police response", [], None,
     "Según Wikipedia, el Maleconazo dejó unos 370 arrestos registrados y 30 heridos, 11 de ellos policías, y los "
     "disturbios se calmaron por la tarde, cuando Fidel Castro llegó a la zona."),
    ("FR-B019", "postura", "F044", "Aftermath", [], "gobierno_cubano",
     "Según Wikipedia, Fidel Castro culpó de los problemas de Cuba a Estados Unidos, citando el embargo y lo que llamó "
     "intentos de provocar desórdenes y salidas ilegales."),
    # ---------------- apertura de las costas
    ("FR-B020", "postura", "F040", "Letter :2", [], "gobierno_cubano",
     "Según la GAO, en un discurso televisado el 13 de agosto de 1994 Fidel Castro culpó a Estados Unidos de los "
     "disturbios y la violencia y amenazó con levantar las restricciones de salida si Estados Unidos no tomaba medidas "
     "para frenar las salidas en bote y no devolvía a los secuestradores que habían llegado allí."),
    ("FR-B021", "hecho_atribuido", "F042", "p. 1", [], None,
     "Según Siro del Castillo, el 13 de agosto de 1994 Fidel Castro anunció que se retirarían los guardafronteras de "
     "las costas y que podría irse del país cualquier persona que quisiera."),
    ("FR-B022", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, al no recibir de Estados Unidos la respuesta que esperaba, Castro indicó que no impediría las "
     "salidas, y durante la semana siguiente muchos cubanos fueron a las playas, construyeron embarcaciones "
     "improvisadas y se hicieron a la mar."),
    ("FR-B023", "postura", "F045", "Events", [], "gobierno_cubano",
     "Según EcuRed, la presión de la emigración ilegal, los secuestros de embarcaciones y los disturbios llevaron al "
     "gobierno cubano a decidir el 12 de agosto de 1994 eliminar las restricciones a las salidas, y Castro retó a "
     "Clinton a aceptar a todos los cubanos que quisieran ir."),
    # ---------------- respuesta de EE. UU. y Guantánamo
    ("FR-B024", "hecho", "F040", "Letter :1, Letter :2", ["F042"], None,
     "El 19 de agosto de 1994 el presidente Clinton anunció que la Guardia Costera ya no llevaría a Estados Unidos a "
     "los balseros cubanos interceptados en el mar, sino a la base naval de Guantánamo, lo que invirtió una política "
     "de unas tres décadas de acoger a los cubanos que huían."),
    ("FR-B025", "postura", "F042", "p. 2", [], "gobierno_eeuu",
     "Según Siro del Castillo, Clinton afirmó entonces que no permitiría que el gobierno de Cuba aprovechara la "
     "tradicional política de 'puertas abiertas' para exportar a la oposición y usar las salidas como válvula de escape "
     "en plena crisis económica."),
    ("FR-B026", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, el presidente y la fiscal general dijeron al principio que los cubanos llevados a Guantánamo no "
     "tendrían oportunidad de entrar después en Estados Unidos, pero muchos cubanos no creyeron que la nueva política "
     "se aplicaría y siguieron saliendo."),
    ("FR-B027", "cifra_disputada", "F042", "p. 3", ["F040", "F043"], None,
     "El número de balseros llevados a Guantánamo varía según la fuente: Siro del Castillo da 32.362 cubanos "
     "interceptados entre agosto y septiembre de 1994 en la operación 'Able Vigil'; la GAO habla de unos 33.000 "
     "recogidos en el mar y llevados a la base; Wikipedia dice que unos 20.000 quedaron detenidos en ella."),
    ("FR-B028", "hecho_atribuido", "F041", "p. 1", [], None,
     "Según el Servicio de Investigación del Congreso (CRS), el número de cubanos interceptados por la Guardia Costera "
     "o la Patrulla Fronteriza de Estados Unidos llegó a casi 40.000 en 1994, la cifra más alta desde el Mariel."),
    ("FR-B029", "hecho_atribuido", "F040", "Letter :2, Letter :4", [], None,
     "Según la GAO, 8.763 cubanos fueron trasladados de Guantánamo a un refugio en Panamá entre septiembre de 1994 y "
     "febrero de 1995, y 7.291 fueron devueltos a Guantánamo en febrero de 1995."),
    ("FR-B030", "cifra_disputada", "F040", "Letter :7", ["F042"], None,
     "La población total de los campamentos de Guantánamo en septiembre de 1994, contando a los haitianos que ya "
     "estaban allí, varía según la fuente: la GAO habla de unas 45.000 personas, con unos 12.000 haitianos; Siro del "
     "Castillo dice que llegó a cerca de 50.000."),
    ("FR-B031", "hecho_atribuido", "F042", "p. 4", [], None,
     "Según Siro del Castillo, cuando llegaron los haitianos y los cubanos la infraestructura de la base de Guantánamo "
     "estaba preparada para unas 5.000 personas, y todo había que traerlo de fuera."),
    ("FR-B032", "hecho_atribuido", "F042", "pp. 3-5", [], None,
     "Según Siro del Castillo, en los primeros meses los refugiados vivían en tiendas de lona sobre la tierra, dormían "
     "en catres del ejército dentro de campamentos rodeados de alambre de púas, pocos tenían agua corriente, usaban "
     "letrinas portátiles y comían sobre todo raciones militares."),
    ("FR-B033", "postura", "F042", "pp. 5-6", [], "Siro del Castillo",
     "Según Siro del Castillo, las condiciones de los campamentos en los primeros meses fueron pésimas y en algunos "
     "casos inhumanas, y algunos militares de la fuerza de tarea dieron a los refugiados un trato arbitrario y a veces "
     "abusivo."),
    ("FR-B034", "hecho_atribuido", "F042", "p. 5", [], None,
     "Según Siro del Castillo, en octubre de 1994 el Departamento de Estado anunció mejoras en Guantánamo: agua "
     "corriente en todos los campamentos haitianos y en el 75 % de los cubanos, pisos de madera para las tiendas y "
     "limpieza diaria de las letrinas, que eran una por cada 30 refugiados."),
    ("FR-B035", "postura", "F040", "Letter :1, Letter :7", [], "gobierno_eeuu",
     "Según la GAO, que visitó Guantánamo en junio de 1995, las condiciones de los campamentos eran difíciles pero "
     "adecuadas y en general superaban las pautas mínimas de inspección del ACNUR, como 3,5 metros cuadrados de "
     "espacio por persona."),
    ("FR-B036", "hecho_atribuido", "F040", "Letter :7", [], None,
     "Según la GAO, en septiembre de 1994, cuando llegaban miles de personas por día, los propios mandos militares "
     "describían las condiciones como marginales, porque se levantaban tiendas e instalaban baños portátiles a medida "
     "que llegaba la gente; después el Departamento de Defensa gastó unos 25,3 millones de dólares en mejoras."),
    ("FR-B037", "hecho_atribuido", "F042", "p. 6", [], None,
     "Según Siro del Castillo, la incertidumbre y las condiciones causaron ansiedad y depresión en adultos y menores, "
     "muchos balseros se lanzaron a los campos minados o al mar para volver a territorio cubano y otros pidieron ser "
     "repatriados."),
    ("FR-B038", "hecho_atribuido", "F040", "Letter :6", [], None,
     "Según la GAO, hasta el 27 de junio de 1995 unos 622 cubanos habían vuelto de Guantánamo a Cuba por vía "
     "diplomática, 1.000 habían regresado por su cuenta, por tierra o por mar, y 139 se habían reasentado en terceros "
     "países."),
    ("FR-B039", "hecho", "F040", "Letter :2", ["F042"], None,
     "El 14 de octubre de 1994 Clinton anunció que recibirían permiso de entrada (parole) los mayores de 70 años, los "
     "menores no acompañados y las personas con enfermedades graves y sus cuidadores; el 2 de diciembre se añadieron, "
     "caso por caso, los niños y sus familias. Se les llamó los 'cuatro protocolos'."),
    ("FR-B040", "hecho_atribuido", "F043", "Exodus and detention", [], None,
     "Según Wikipedia, mientras esperaban, algunos detenidos de Guantánamo montaron gimnasios improvisados, galerías "
     "de arte, periódicos y una emisora de radio, y organizaron lecturas de poesía."),
    # ---------------- acuerdos migratorios
    ("FR-B041", "hecho", "F041", "pp. 2-3", ["F040"], None,
     "El 9 de septiembre de 1994 Estados Unidos y Cuba firmaron un acuerdo migratorio: Estados Unidos admitiría al "
     "menos 20.000 inmigrantes cubanos al año, sin contar a los familiares directos de ciudadanos estadounidenses, y "
     "Cuba se comprometió a impedir las salidas inseguras 'usando principalmente métodos persuasivos'."),
    ("FR-B042", "hecho_atribuido", "F041", "p. 3", [], None,
     "Según el CRS, el acuerdo de septiembre de 1994 también incluyó cooperar contra el tráfico ilegal de personas y "
     "en el regreso voluntario de cubanos, y seguir negociando sobre los cubanos no admisibles bajo la ley migratoria "
     "estadounidense, punto en el que no hubo acuerdo."),
    ("FR-B043", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, a los pocos días del acuerdo la policía cubana volvió a patrullar los caminos hacia las playas con "
     "órdenes de arrestar a quienes llevaran balsas o materiales para hacerlas, y cesaron las salidas en balsa."),
    ("FR-B044", "hecho_atribuido", "F040", "Letter :2", [], None,
     "Según la GAO, la Sección de Intereses de Estados Unidos en La Habana calculó que las 20.000 entradas anuales se "
     "repartirían en unos 7.000 refugiados y familiares, 8.000 visas de inmigrante con sus familias y 5.000 personas "
     "elegidas por un sorteo especial."),
    ("FR-B045", "hecho_atribuido", "F041", "pp. 3, 5", [], None,
     "Según el CRS, como el sistema normal de visas no alcanzaba las 20.000 entradas, Estados Unidos creó un sorteo "
     "especial de visas; en sus tres convocatorias se inscribieron unas 189.000 personas en 1994, 433.000 en 1996 "
     "y 541.000 en 1998."),
    ("FR-B046", "hecho_atribuido", "F041", "p. 5", [], None,
     "Según el CRS, para el sorteo había que tener entre 18 y 55 años y cumplir dos de tres requisitos: haber terminado "
     "la enseñanza secundaria, tener al menos tres años de experiencia laboral o tener familiares en Estados Unidos."),
    ("FR-B047", "hecho", "F041", "p. 3", ["F040"], None,
     "El 2 de mayo de 1995 el gobierno de Clinton anunció un nuevo acuerdo con Cuba: la mayoría de los cubanos de "
     "Guantánamo entrarían en Estados Unidos con permiso humanitario, descontando 5.000 al año durante tres años de "
     "las 20.000 entradas anuales, y los cubanos interceptados en el mar serían devueltos a Cuba en vez de ir a "
     "Guantánamo."),
    ("FR-B048", "hecho_atribuido", "F041", "p. 3", [], None,
     "Según el CRS, en el acuerdo de mayo de 1995 ambos gobiernos se comprometieron a que no se tomaran represalias "
     "contra los repatriados, a quienes funcionarios estadounidenses informarían cómo emigrar legalmente; los acusados "
     "de tráfico de personas sí se exponían a prisión en Cuba."),
    ("FR-B049", "hecho_atribuido", "F040", "Letter :2, Letter :8", [], None,
     "Según la GAO, al 7 de junio de 1995 quedaban unos 18.500 cubanos en Guantánamo, y salían de la base de 500 a 550 "
     "por semana en tres vuelos chárter, porque las autoridades de Florida sostenían que el estado no podía recibir "
     "más de 550 por semana."),
    ("FR-B050", "hecho_atribuido", "F042", "p. 7", [], None,
     "Según Siro del Castillo, tras el acuerdo de mayo de 1995 la fiscal general Janet Reno anunció que todos los "
     "cubanos de la base, salvo los que tuvieran antecedentes penales, podrían viajar a Estados Unidos, y a finales de "
     "enero de 1996 el último salió de Guantánamo."),
    ("FR-B051", "hecho_atribuido", "F040", "Letter :4", [], None,
     "Según la GAO, el costo adicional de la respuesta estadounidense a la crisis entre agosto de 1994 y septiembre de "
     "1995 superaría los 497 millones de dólares, de los cuales unos 434 millones correspondían al Departamento de "
     "Defensa."),
    ("FR-B052", "hecho_atribuido", "F040", "Letter :8", [], None,
     "Según la GAO, en febrero de 1995 el gobierno cubano subió el pasaje de ida La Habana-Miami de 150 a 990 dólares, "
     "y en junio de 1995 impuso cobros de 400 dólares por el examen médico (250 para niños), 250 por el permiso de "
     "salida y documentos y 50 por el pasaporte."),
    ("FR-B053", "postura", "F040", "Letter :8", [], "gobierno_eeuu",
     "Según la GAO, funcionarios estadounidenses consideraron que algunos cobros por servicios antes gratuitos podían "
     "ser razonables, pero que los impuestos por Cuba serían un obstáculo serio para quienes querían emigrar."),
    # ---------------- consecuencia: pies secos, pies mojados
    ("FR-B054", "hecho", "F041", "p. 4", ["F043"], None,
     "De los acuerdos de 1994 y 1995 surgió la práctica conocida como 'pies secos, pies mojados': los cubanos "
     "interceptados en el mar eran devueltos a Cuba salvo que expresaran temor a ser perseguidos, y los que llegaban a "
     "tierra en general podían quedarse y pedir la residencia al año siguiente por la Ley de Ajuste Cubano."),
    ("FR-B055", "cifra_disputada", "F042", "p. 8", ["F041", "F043"], None,
     "El origen de 'pies secos, pies mojados' se fecha de forma distinta: Siro del Castillo dice que el gobierno "
     "estadounidense la practica desde abril de 1999; el CRS la describe como una práctica que fue surgiendo de los "
     "acuerdos de 1994 y 1995; Wikipedia la atribuye a Clinton como respuesta a la crisis de 1994."),
    # ---------------- contexto caribeño
    ("FR-B056", "hecho_atribuido", "F042", "pp. 2-3", [], None,
     "Según Siro del Castillo, antes de los balseros cubanos Estados Unidos ya interceptaba a haitianos en alta mar: "
     "entre octubre de 1991 y junio de 1992 interceptó a 36.596, y entre junio de 1993 y noviembre de 1994 llevó a "
     "21.638 a los campamentos de Guantánamo."),
    ("FR-B057", "postura", "F042", "p. 8", [], "Siro del Castillo",
     "Según Siro del Castillo, el trato especial que reciben los cubanos que llegan a Estados Unidos contrasta con el "
     "trato que considera discriminatorio hacia dominicanos y haitianos, a quienes se deporta sin la misma oportunidad "
     "de pedir asilo."),
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
    print("Las fuentes F040 en adelante ya están en el registro. No toco nada.")
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

print(f"Registradas {len(FUENTES)} fuentes (F040 a F045).")
print(f"Creado {FRAG} con {len(FRAGMENTOS)} fragmentos en 'pendiente'.")
print(f"Ahora: python revisar.py {FRAG}")
