"""
agregar_pies_secos.py — Abre la etapa de "pies secos, pies mojados" (1995-2017):
registra las fuentes F046-F053 y crea fuentes/fragmentos_pies_secos.jsonl.

Uso (desde E:\\vertex-exilio):
    python agregar_pies_secos.py

Documentos leídos (en fuentes/docs): CRS_R44714_2016.html, CRS_R40566_2009.pdf, OBAMA_12ene2017.html,
DHS_12ene2017.html, MINREX_declaracion_2017.html, PEW_2017.html, WIKI_pies_secos.html, WIKI_elian.html.
La página o sección va en 'ubicacion'. En CRS 2009 las páginas son las impresas en el informe
(la página del PDF es la impresa + 3). CRS 2016 está en HTML: la ubicación es la sección.

Qué hace:
  1. Copia de seguridad del registro.
  2. Añade F046-F053 al registro (si ya existen, no hace nada).
  3. Crea fuentes/fragmentos_pies_secos.jsonl con todos los fragmentos en 'pendiente'
     (si el archivo ya existe, no lo toca).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_pies_secos.jsonl")
HOY = "2026-10-30"
ETAPA = "pies_secos_pies_mojados"

FUENTES = [
    ("F046", "U.S. Policy on Cuban Migrants: In Brief (CRS R44714, 16 de diciembre de 2016)",
     "Congressional Research Service (copia de EveryCRSReport)",
     "https://www.everycrsreport.com/files/20161216_R44714_0508b6159e966862f2f9338012a6ccd90216f745.html",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "hechos",
     "Archivo fuentes/docs/CRS_R44714_2016.html (HTML, sin páginas: ubicación = sección). Escrito un mes antes "
     "del fin de la política. Cifra de entradas por puertos en FY2016 solo hasta el 31 de julio de 2016."),
    ("F047", "Cuban Migration to the United States: Policy and Trends (CRS R40566, 2 de junio de 2009)",
     "Congressional Research Service (copia de EveryCRSReport)",
     "https://www.everycrsreport.com/files/20090602_R40566_5c818df5cf6f61aac828f7e487dfe38f29f6dce4.pdf",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "hechos",
     "Archivo fuentes/docs/CRS_R40566_2009.pdf (24 págs.). Páginas = numeración impresa (PDF = impresa + 3). "
     "Recoge argumentos de partidarios y críticos: van como postura con actor. Usa 'dictator' para Batista y "
     "'former dictator' para Fidel Castro: no entra. En la p. 14 dice 6.260 refugiados en FY2005 y su gráfico "
     "dice 6.360: no se usa esa cifra."),
    ("F048", "Statement on the United States Cuban Immigration Policy (12 de enero de 2017)",
     "Barack Obama - The American Presidency Project (UCSB)",
     "https://www.presidency.ucsb.edu/documents/statement-the-united-states-cuban-immigration-policy",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/OBAMA_12ene2017.html. Lo anunciado = hecho; las razones del presidente = postura."),
    ("F049", "Statement by Secretary Johnson on the Continued Normalization of our Migration Relationship with Cuba (12 de enero de 2017)",
     "Jeh Johnson - Department of Homeland Security",
     "https://www.dhs.gov/news/2017/01/12/statement-secretary-johnson-continued-normalization-our-migration-relationship-cuba",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/DHS_12ene2017.html (trae versión en inglés y en español). Lo anunciado = hecho; "
     "valoraciones = postura de EE. UU."),
    ("F050", "Declaración del Gobierno Revolucionario (12 de enero de 2017)",
     "Ministerio de Relaciones Exteriores de Cuba (CubaMinrex, versión en inglés)",
     "https://misiones.cubaminrex.cu/en/articulo/declaration-revolutionary-government-1",
     "primaria", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/MINREX_declaracion_2017.html. SOLO para documentar la versión oficial cubana. "
     "Nunca sostiene un hecho ni una cifra. Expresiones como 'robo de cerebros' van siempre atribuidas."),
    ("F051", "Surge in Cuban immigration to U.S. continued through 2016 (13 de enero de 2017)",
     "Jens Manuel Krogstad - Pew Research Center",
     "https://www.pewresearch.org/short-reads/2017/01/13/cuban-immigration-to-u-s-surges-as-relations-warm/",
     "academica", "revisar", "academica", "hechos",
     "Archivo fuentes/docs/PEW_2017.html. Datos de CBP y Guardia Costera. Dice 'fear of prosecution' donde debe "
     "ser 'persecution' (errata). Guardia Costera FY2016: 5.263, distinto de CRS (5.213): va como cifra disputada."),
    ("F052", "Wet feet, dry feet policy", "Wikipedia", "https://en.wikipedia.org/wiki/Wet_feet,_dry_feet_policy",
     "enciclopedia", "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_pies_secos.html (guardado desde Chrome el 2026-10-30). Varias secciones copian "
     "el CRS casi palabra por palabra: en esos casos no cuenta como corroboración independiente. Da el 1 de mayo "
     "de 1995 para el acuerdo (CRS y GAO: 2 de mayo) y el 7 de enero de 2006 para el caso del puente (CRS: 5 de enero)."),
    ("F053", "Elián González", "Wikipedia", "https://en.wikipedia.org/wiki/Eli%C3%A1n_Gonz%C3%A1lez",
     "enciclopedia", "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_elian.html (el enlace 'Elián González affair' redirige a esta página; guardado "
     "desde Chrome el 2026-10-30). Datos solo con atribución."),
]

# (id, tipo, fuente, ubicación, corroborado_por, actor, texto)
FRAGMENTOS = [
    # ---------------- qué era la política
    ("FR-W001", "hecho", "F046", "Wet Foot/Dry Foot Policy", ["F047"], None,
     "Bajo la política de 'pies secos, pies mojados', los cubanos interceptados en el mar eran devueltos a Cuba "
     "salvo que alegaran un temor fundado de persecución, y en ese caso se les consideraba para reasentarlos en "
     "terceros países; los que llegaban a tierra eran inspeccionados y en general podían quedarse en Estados Unidos."),
    ("FR-W002", "hecho_atribuido", "F046", "Wet Foot/Dry Foot Policy", [], None,
     "Según el Servicio de Investigación del Congreso (CRS), los cubanos que se quedaban por 'pies secos' no "
     "recibían una admisión formal: normalmente se les daba un permiso de entrada temporal (parole) y, como "
     "beneficiarios de ese permiso, podían pedir la residencia permanente al cabo de un año por la Ley de Ajuste Cubano."),
    ("FR-W003", "hecho", "F046", "Cuban Adjustment Act of 1966", ["F047"], None,
     "La Ley de Ajuste Cubano de 1966 permite a los cubanos que llevan al menos un año en Estados Unidos pedir la "
     "residencia permanente sin que los patrocine un familiar o un empleador, una vía que no tiene ninguna otra "
     "nacionalidad."),
    ("FR-W004", "hecho_atribuido", "F046", "Cuban Adjustment Act of 1966", [], None,
     "Según el CRS, en el año fiscal 2014 unos 40.000 cubanos y sus dependientes obtuvieron la residencia "
     "permanente por la Ley de Ajuste Cubano."),
    ("FR-W005", "hecho", "F046", "Cuban Adjustment Act of 1966", ["F047"], None,
     "Una ley de 1996 dispuso que la Ley de Ajuste Cubano quedaría derogada solo cuando el presidente de Estados "
     "Unidos determine que en Cuba gobierna un gobierno elegido democráticamente."),
    ("FR-W006", "hecho_atribuido", "F047", "p. 4", [], None,
     "Según el CRS, de mayo de 1995 a julio de 2003 unos 170 refugiados cubanos interceptados en el mar fueron "
     "reasentados en 11 países, entre ellos España, Venezuela, Australia y Nicaragua."),
    ("FR-W007", "hecho", "F046", "Eligibility for Federal Assistance", ["F047"], None,
     "Leyes de 1980 y de 1996 hicieron que los 'entrantes cubanos y haitianos' tuvieran derecho a la "
     "misma ayuda de reasentamiento y a ciertos beneficios federales en las mismas condiciones que los refugiados."),
    # ---------------- cifras de salidas
    ("FR-W008", "hecho_atribuido", "F047", "p. 9", [], None,
     "Según el CRS, después del acuerdo de mayo de 1995 la Guardia Costera interceptó a 411 cubanos en el año "
     "fiscal 1996 y 421 en 1997; la cifra subió a 903 en 1998 y 1.619 en 1999, bajó de 1.000 en 2000 a 666 en 2002, "
     "llegó a 2.868 en 2007, la más alta en doce años, y fue de 2.199 en 2008."),
    ("FR-W009", "hecho_atribuido", "F046", "Unauthorized Migration Statistics", [], None,
     "Según el CRS, las intercepciones de cubanos en el mar casi se cuadruplicaron entre el año fiscal 2013 y el "
     "2016, de 1.357 a 5.213, la cifra más alta de todo el período 1995-2016."),
    ("FR-W010", "cifra_disputada", "F046", "Unauthorized Migration Statistics", ["F051"], None,
     "El número de cubanos interceptados en el mar por la Guardia Costera en el año fiscal 2016 varía según la "
     "fuente: el CRS da 5.213 y Pew Research da 5.263."),
    ("FR-W011", "hecho_atribuido", "F047", "pp. 11-13", [], None,
     "Según el CRS, muchos cubanos buscaron una ruta distinta al estrecho de la Florida: navegaban hasta la península "
     "de Yucatán, en México, y seguían por tierra hasta la frontera de Estados Unidos, donde los inspeccionaban aunque "
     "no tuvieran documentos y en general los dejaban entrar; según un diario mexicano citado por el CRS, en 2007 "
     "México ya era la ruta principal."),
    ("FR-W012", "hecho_atribuido", "F052", "Changes in immigration patterns", [], None,
     "Según Wikipedia, a los cubanos que llegaban a Estados Unidos a través de México se les llamaba 'pies "
     "polvorientos' (dusty foot), y otros cruzaban el canal de la Mona desde República Dominicana hasta la isla de "
     "Mona, que pertenece a Puerto Rico."),
    ("FR-W013", "hecho_atribuido", "F046", "Unauthorized Migration Statistics", [], None,
     "Según el CRS, los cubanos sin documentos que se presentaban en puertos de entrada de Estados Unidos pasaron de "
     "24.277 en el año fiscal 2014 a 46.590 en el 2016 (este último dato, hasta el 31 de julio de 2016), y la "
     "mayoría llegaba por la frontera terrestre del suroeste."),
    ("FR-W014", "hecho_atribuido", "F051", "texto", [], None,
     "Según Pew Research, 56.406 cubanos entraron en Estados Unidos por puertos de entrada en el año fiscal 2016, un "
     "31 % más que los 43.159 del 2015, que a su vez habían subido un 78 % frente a los 24.278 del 2014."),
    ("FR-W015", "hecho_atribuido", "F051", "texto", [], None,
     "Según Pew Research, miles de cubanos llegaban por tierra: muchos volaban a Ecuador, por su política "
     "migratoria abierta, y seguían hacia el norte por Centroamérica y México; cuando algunos países "
     "centroamericanos cerraron sus fronteras, muchos quedaron varados en el camino."),
    ("FR-W016", "hecho_atribuido", "F051", "texto", [], None,
     "Según Pew Research, la mayoría de los cubanos que entraban por tierra lo hacían por el sector de Laredo, en "
     "Texas: dos tercios (28.371) en el año fiscal 2015 y el 64 % en el 2016."),
    ("FR-W017", "hecho", "F046", "Unauthorized Migration Statistics", ["F052"], None,
     "El aumento de las llegadas de cubanos a partir de 2014 se atribuye sobre todo al temor de que Estados Unidos "
     "terminara pronto con la política que permitía quedarse a quienes llegaban a su territorio."),
    ("FR-W018", "hecho", "F046", "Introduction", ["F051"], None,
     "En diciembre de 2014 el presidente Obama anunció un cambio de política para restablecer las relaciones con Cuba."),
    ("FR-W019", "hecho_atribuido", "F051", "texto", [], None,
     "Según Pew Research, en 2015 vivían en Estados Unidos unos 2 millones de hispanos de origen cubano, y la "
     "proporción de nacidos fuera del país bajó del 68 % en 2000 al 57 % en 2015, porque el crecimiento venía ya "
     "sobre todo de cubanoamericanos nacidos en Estados Unidos."),
    # ---------------- vías legales
    ("FR-W020", "hecho", "F047", "p. 13", ["F046"], None,
     "Desde las conversaciones migratorias de 1994-1995, Estados Unidos tramita solicitudes de refugio dentro de "
     "Cuba para categorías como antiguos presos políticos, miembros de minorías religiosas perseguidas y activistas "
     "de derechos humanos."),
    ("FR-W021", "hecho_atribuido", "F047", "pp. 13-14", [], None,
     "Según el CRS, tras los atentados del 11 de septiembre de 2001 el procesamiento de refugiados se frenó: en el "
     "año fiscal 2003 solo llegaron 305 refugiados cubanos, y en 2004 se aprobaron 5.670 de 8.658 solicitudes, pero "
     "solo llegaron 2.980; en esos años también se reportaron problemas para obtener el permiso de salida del "
     "gobierno cubano."),
    ("FR-W022", "hecho_atribuido", "F046", "Statistics on Refugee Status and Asylum", [], None,
     "Según el CRS, el asilo concedido a cubanos fue muy bajo: el máximo fue de 886 en el año fiscal 1996, y entre "
     "2002 y 2014 cada año lo recibieron menos de 100."),
    ("FR-W023", "hecho_atribuido", "F047", "p. 15", [], None,
     "Según el CRS, 49.500 cubanos obtuvieron la residencia permanente en el año fiscal 2008, y Cuba fue ese año el "
     "quinto país de origen de nuevos residentes, después de México, China, India y Filipinas."),
    # ---------------- incidentes 1999-2006
    ("FR-W024", "hecho", "F047", "p. 16", ["F052"], None,
     "En junio de 1999 la Guardia Costera usó gas pimienta y un cañón de agua para impedir que seis cubanos llegaran "
     "a la playa de Surfside, en la Florida, y pocas semanas después una mujer se ahogó al volcarse una embarcación "
     "durante una intercepción."),
    ("FR-W025", "hecho", "F047", "p. 16", ["F053"], None,
     "A finales de noviembre de 1999 la Guardia Costera llevó a Estados Unidos, en vez de a Cuba, al niño Elián "
     "González, de seis años, y a otros dos sobrevivientes de un naufragio; Elián quedó al cuidado de su tío abuelo "
     "Lázaro González en Miami."),
    ("FR-W026", "hecho_atribuido", "F053", "Journey to Florida", [], None,
     "Según Wikipedia, el 21 de noviembre de 1999 Elián salió de Cárdenas con su madre y otras doce personas en un "
     "bote pequeño de aluminio con el motor defectuoso; su madre y otras diez personas murieron, y a él lo "
     "rescataron dos pescadores cuando flotaba en una cámara de neumático."),
    ("FR-W027", "postura", "F053", "Custody dispute in the United States", [], "exilio",
     "Según Wikipedia, Lázaro González, con el respaldo de cubanoamericanos de Miami, sostuvo que el niño debía "
     "quedarse en Estados Unidos y no ser devuelto a su padre."),
    ("FR-W028", "postura", "F053", "Custody dispute in the United States", [], "gobierno_cubano",
     "Según Wikipedia, el padre de Elián, Juan Miguel González, con el apoyo de las autoridades cubanas, exigió que "
     "su hijo fuera devuelto a Cuba."),
    ("FR-W029", "hecho", "F047", "p. 16", ["F053"], None,
     "Cuando el padre de Elián llegó a Estados Unidos en abril de 2000 para recuperar la custodia, Lázaro González "
     "desobedeció la orden del gobierno de entregar al niño, y la fiscal general Janet Reno ordenó sacarlo de la casa "
     "de Miami en la madrugada del 22 de abril de 2000."),
    ("FR-W030", "hecho", "F047", "p. 16, nota 59", ["F053"], None,
     "El 1 de junio de 2000 un tribunal federal de apelaciones rechazó la apelación de los familiares de Miami, el 28 "
     "de junio la Corte Suprema dejó en pie esa decisión, y ese mismo día Elián volvió a Cuba con su padre."),
    ("FR-W031", "hecho_atribuido", "F053", "Custody dispute in the United States", [], None,
     "Según Wikipedia, durante la disputa las encuestas mostraron que la mayoría de los estadounidenses creía que "
     "Elián debía volver con su padre en Cuba."),
    ("FR-W032", "hecho_atribuido", "F053", "Seizure and reactions", [], None,
     "Según Wikipedia, en el operativo del 22 de abril de 2000 participaron más de 130 agentes del Servicio de "
     "Inmigración, se usó gas pimienta contra personas que intentaron impedirlo fuera de la casa, y una foto del "
     "operativo tomada por Alan Diaz, de Associated Press, ganó el premio Pulitzer en 2001."),
    ("FR-W033", "hecho_atribuido", "F053", "Political ramifications", [], None,
     "Según Wikipedia, comentaristas han señalado que el caso Elián pudo influir en las elecciones presidenciales de "
     "2000 en la Florida, y encuestas de 2001 indicaron que George W. Bush obtuvo el 80 % del voto cubanoamericano de "
     "ese estado, frente al 65 % de Bob Dole en 1996."),
    ("FR-W034", "hecho_atribuido", "F053", "Political ramifications", [], None,
     "Según Wikipedia, en Cuba el caso generó una movilización popular por el regreso del niño, y Fidel Castro lanzó "
     "a partir de ella una campaña llamada la Batalla de Ideas."),
    ("FR-W035", "postura", "F053", "Life in Cuba", [], "Elián González",
     "Según Wikipedia, ya adulto Elián González ha dicho que no se arrepiente de haber vuelto a Cuba, y en 2013 "
     "describió su tiempo en Estados Unidos como una etapa muy triste y culpó a la Ley de Ajuste Cubano de haberle "
     "negado el derecho a estar con su padre."),
    ("FR-W036", "postura", "F053", "Life in Cuba", [], "familia de Miami",
     "Según Wikipedia, su tía Angela González dudó de que una entrevista que Elián dio en 2005 reflejara lo que "
     "realmente pensaba, por los controles que el gobierno cubano impone sobre la información."),
    ("FR-W037", "hecho", "F047", "p. 16", ["F041"], None,
     "El 11 de abril de 2003 el gobierno cubano fusiló a tres hombres que el 2 de abril habían secuestrado una "
     "lancha en La Habana para intentar llegar a Estados Unidos, tras juicios sumarios a puerta cerrada; Amnistía "
     "Internacional, Human Rights Watch, México, la Unión Europea y la Comunidad del Caribe condenaron las ejecuciones."),
    ("FR-W038", "hecho", "F047", "p. 16", ["F041"], None,
     "En julio de 2003 doce personas se llevaron una embarcación de una marina cubana y secuestraron a los tres "
     "vigilantes; tras interceptarlos, Estados Unidos los devolvió cuando el gobierno cubano ofreció condenarlos a "
     "10 años de prisión."),
    ("FR-W039", "cifra_disputada", "F047", "pp. 16-17", ["F052", "F041"], None,
     "En enero de 2006 la Guardia Costera encontró a 15 cubanos en un puente viejo de los Cayos de la Florida que ya "
     "no estaba unido a tierra, los consideró 'pies mojados' y los devolvió a Cuba; el CRS fecha el hallazgo el 5 de "
     "enero de 2006 y Wikipedia, el 7 de enero."),
    ("FR-W040", "hecho_atribuido", "F052", "Recurring issues and criticism", [], None,
     "Según Wikipedia, en protesta por la devolución de los cubanos del puente, el activista Ramón Saúl Sánchez hizo "
     "una huelga de hambre de once días."),
    ("FR-W041", "postura", "F047", "p. 17", [], "partidarios de la repatriación",
     "Según el CRS, quienes defendían las devoluciones sostenían que eran clave para disuadir la migración ilegal y "
     "peligrosa en embarcaciones precarias o sobrecargadas."),
    ("FR-W042", "postura", "F047", "p. 17", [], "críticos de la repatriación",
     "Según el CRS, los críticos de esas devoluciones afirmaban que Estados Unidos y Cuba negaban a esas personas "
     "su derecho a un proceso justo y a una audiencia, y algunos pedían terminar con la política de intercepción y "
     "repatriación."),
    # ---------------- debate sobre la Ley de Ajuste y las conversaciones
    ("FR-W043", "postura", "F047", "p. 17", [], "críticos de la Ley de Ajuste",
     "Según el CRS, algunos críticos sostenían que la Ley de Ajuste Cubano estaba obsoleta y anclada en la Guerra "
     "Fría, que era discriminatoria porque daba a los cubanos una ventaja que no tenía ninguna otra nacionalidad, y "
     "que funcionaba como un imán para cubanos que de otro modo no podrían entrar."),
    ("FR-W044", "postura", "F047", "pp. 17-18", [], "defensores de la Ley de Ajuste",
     "Según el CRS, los defensores de la Ley de Ajuste Cubano sostenían que derogarla mandaría un mensaje "
     "equivocado a los cubanos y que el compromiso de admitir al menos 20.000 cubanos al año dependía de poder "
     "ajustar a los beneficiarios del permiso de entrada por esa ley."),
    ("FR-W045", "hecho_atribuido", "F047", "pp. 4, 18", [], None,
     "Según el CRS, las conversaciones migratorias entre los dos gobiernos se hicieron dos veces al año durante una "
     "década, hasta que el Departamento de Estado canceló la ronda de enero de 2004 alegando que Cuba se negaba a "
     "discutir cinco temas, entre ellos los permisos de salida y la aceptación de cubanos expulsables."),
    ("FR-W046", "postura", "F047", "p. 18", [], "gobierno_cubano",
     "Según el CRS, funcionarios cubanos calificaron de irresponsable la cancelación de las conversaciones de 2004 y "
     "afirmaron que Cuba estaba dispuesta a discutir todos los temas planteados por Estados Unidos."),
    ("FR-W047", "hecho_atribuido", "F047", "p. 18", [], None,
     "Según el CRS, había acusaciones de que algunos cubanos usaban la ayuda federal en efectivo para pagar a "
     "traficantes, que según la prensa cobraban hasta 15.000 dólares por persona; el CRS aclara que esa ayuda se "
     "pagaba por meses, durante un máximo de ocho, y en la Florida era de 95 a 180 dólares al mes para una persona sola."),
    ("FR-W048", "hecho_atribuido", "F046", "Policy Proposals", [], None,
     "Según el CRS, en el Congreso de 2015-2016 se presentaron proyectos de ley para derogar la Ley de Ajuste Cubano "
     "y para eliminar el trato especial de los cubanos en la ayuda federal, pero a diciembre de 2016 ninguno se "
     "había aprobado."),
    # ---------------- el fin de la política (12 de enero de 2017)
    ("FR-W049", "hecho", "F048", "texto", ["F049", "F052"], None,
     "El 12 de enero de 2017 el gobierno de Obama puso fin a la política de 'pies secos, pies mojados': desde ese "
     "día, los cubanos que intentaran entrar ilegalmente en Estados Unidos y no calificaran para protección "
     "humanitaria quedaban sujetos a deportación, y el gobierno cubano aceptó recibir a los que tuvieran orden de "
     "expulsión."),
    ("FR-W050", "hecho", "F049", "texto", ["F048"], None,
     "Ese mismo 12 de enero de 2017 Estados Unidos terminó también el programa de permiso de entrada para "
     "profesionales cubanos de la salud (Cuban Medical Professional Parole)."),
    ("FR-W051", "postura", "F048", "texto", [], "gobierno_eeuu",
     "Según su declaración del 12 de enero de 2017, Obama sostuvo que la política de 'pies secos, pies mojados' "
     "había sido diseñada para otra época y que con el cambio se trataba a los migrantes cubanos igual que a los de "
     "otros países; del programa para médicos dijo que contradecía la cooperación sanitaria entre los dos países y "
     "que corría el riesgo de perjudicar al pueblo cubano."),
    ("FR-W052", "hecho_atribuido", "F049", "texto", [], None,
     "Según el Departamento de Seguridad Nacional, aunque terminaba 'pies secos, pies mojados', la Ley de Ajuste "
     "Cubano y ciertas leyes cubanas seguían vigentes."),
    ("FR-W053", "postura", "F050", "texto", [], "gobierno_cubano",
     "Según la declaración del gobierno cubano del 12 de enero de 2017, 'pies secos, pies mojados' violaba los "
     "acuerdos migratorios de 1994 y 1995, estimulaba la migración irregular y el tráfico de personas, y daba a los "
     "cubanos un trato preferente que no recibían los ciudadanos de otros países."),
    ("FR-W054", "postura", "F050", "texto", [], "gobierno_cubano",
     "Según esa declaración, el gobierno cubano calificó el programa de permiso de entrada para médicos como un "
     "intento de quitarle a Cuba sus profesionales de la salud y un ataque a sus misiones médicas en otros países."),
    ("FR-W055", "postura", "F050", "texto", [], "gobierno_cubano",
     "Según la misma declaración, el gobierno cubano sostuvo que para normalizar las relaciones migratorias el "
     "Congreso de Estados Unidos también debía derogar la Ley de Ajuste Cubano de 1966."),
    ("FR-W056", "postura", "F050", "texto", [], "gobierno_cubano",
     "Según la declaración del gobierno cubano, Cuba había propuesto un nuevo acuerdo migratorio en 2002, rechazado "
     "por el presidente George W. Bush, y lo volvió a presentar en 2009, 2010 y el 30 de noviembre de 2015, y el "
     "acuerdo se alcanzó tras casi un año de negociaciones después del restablecimiento de relaciones diplomáticas "
     "el 20 de julio de 2015."),
    ("FR-W057", "postura", "F050", "texto", [], "gobierno_cubano",
     "Según la declaración del gobierno cubano, los acuerdos migratorios anteriores de 1984, 1994 y 1995 seguían "
     "vigentes, incluido el compromiso de Estados Unidos de garantizar una migración regular de al menos 20.000 "
     "personas al año."),
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
    print("Las fuentes F046 en adelante ya están en el registro. No toco nada.")
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

print(f"Registradas {len(FUENTES)} fuentes (F046 a F053).")
print(f"Creado {FRAG} con {len(FRAGMENTOS)} fragmentos en 'pendiente'.")
print(f"Ahora: python revisar.py {FRAG}")
