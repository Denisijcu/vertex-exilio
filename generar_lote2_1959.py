"""
generar_lote2_1959.py — Segundo lote de ejemplos de las etapas 1959-1962 y Pedro Pan.

Uso (desde E:\\vertex-exilio):
    python generar_lote2_1959.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_1959_1962.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_1959_lote2.jsonl con todos los ejemplos en estado 'pendiente'.

Usa sobre todo los fragmentos nuevos (FR-S012 a FR-S029 y FR-PP020 a FR-PP050): cómo funcionaba el
programa de refugiados, el papel de la Iglesia, Bahía de Cochinos, el corte de los vuelos, cómo se
organizó Pedro Pan, quién cuidó a los niños, las cifras que no coinciden entre fuentes y lo que dice
cada parte (EcuRed, Walsh, Carlos Eire, Cauce).
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_1959_1962.jsonl")
DESTINO = Path("datos/borrador_1959_lote2.jsonl")
PREFIJO = "exi-s"
PRIMER_ID = 13

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

S, P = "salida_1959_1962", "pedro_pan"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
# ------------------------------------------------------------------ salida 1959-1962
(S, "hecho", [("¿Cómo funcionaba el centro de refugiados cubanos de Miami a principios de los sesenta?", """El centro de refugiados de Miami era la puerta de entrada al programa federal para los cubanos que llegaban: allí se registraban para recibir ayuda.

El volumen fue grande desde el principio. Según el boletín de la Seguridad Social de 1962, de febrero a diciembre de 1961 se registraron unas 87.000 personas, y a finales de ese año seguían registrándose unas 2.000 por semana.

La mayoría necesitaba ayuda. De cada 20 refugiados registrados, 17 pedían ayuda en efectivo y 16 la recibían. Esa ayuda tenía un tope: 100 dólares al mes para una familia y 60 dólares para una persona sola.

Que tantos la pidieran tiene que ver con cómo salían de Cuba. Según el mismo boletín, desde diciembre de 1960 quienes salían solo podían llevar su ropa, sin muebles, y 5 pesos que valían unos 50 centavos. Del 27 de febrero a finales de 1961 el programa pagó 8.451.308 dólares en ayuda, y a fin de año la recibían 21.294 casos.

En 1962 el centro cambió de escala. Según la ficha del Servicio de Parques Nacionales, el 1 de julio de 1962 el gobierno federal alquiló los cuatro primeros pisos del antiguo edificio del Miami News para el centro de asistencia, y el personal pasó de 14 a más de 300 personas en un año. Ese edificio es la Torre de la Libertad, a la que los refugiados llamaban 'El Refugio', y funcionó como centro federal de asistencia hasta 1974.""")],
 ["FR-S014", "FR-S007", "FR-S019", "FR-S020", "FR-S025", "FR-S009"]),

(S, "contexto", [("¿Cómo era la gente que llegó de Cuba en 1961?", """Las fuentes de la época describen una primera ola con un perfil bastante marcado, aunque conviene recordar que son datos de quienes se registraron en el centro de refugiados de Miami, no de todos los que salieron.

Según el boletín de la Seguridad Social de 1962, tres cuartas partes de los refugiados registrados tenían entre 20 y 50 años y cerca del 60 % eran hombres. Solo un 25 % hablaba inglés lo bastante bien para trabajar. El mismo boletín dice que a principios de 1961 más de la mitad del profesorado de la Universidad de La Habana vivía en Miami o cerca.

Por ocupación, más de un tercio de los cabezas de familia había trabajado en ocupaciones profesionales, semiprofesionales o directivas; casi un tercio, en trabajos de oficina, ventas o especializados; y menos de una cuarta parte no tenía una calificación especial.

Llegaban con muy poco. Según el boletín, desde diciembre de 1960 solo podían sacar de Cuba su ropa y 5 pesos que valían unos 50 centavos.

El boletín recoge además un detalle poco conocido: algunos refugiados devolvieron por su cuenta parte de la ayuda que habían recibido. De mayo a diciembre de 1961 esas devoluciones voluntarias sumaron 119.930 dólares, y solo en diciembre 874 refugiados devolvieron 48.873,97 dólares.

Es el retrato que dan esas fuentes: mucha gente con oficio o profesión, que llegaba casi sin nada y, en su mayoría, sin el inglés necesario para trabajar.""")],
 ["FR-S015", "FR-S008", "FR-S020", "FR-S016"]),

(S, "hecho", [("¿Por qué no pusieron a los cubanos en campamentos de refugiados?", """Hubo quien lo propuso, pero el programa federal tomó otro camino.

Según la ficha del Servicio de Parques Nacionales, el padre Bryan Walsh recordaba que algunos políticos querían alojar a todos los refugiados en un campamento en Opa-locka y que la diócesis de Miami se opuso. En su lugar se dieron subsidios de alquiler de 80 a 100 dólares al mes, y según la misma ficha eso facilitó que surgiera la Pequeña Habana.

El gobierno federal también explicó su decisión. Según el boletín de la Seguridad Social de 1962, prefería no crear campamentos para no fomentar la dependencia, y el programa puso el acento en reasentar a los cubanos fuera de Miami.

Ese reasentamiento avanzó, pero con resistencia. A finales de 1961 se habían reasentado 16.532 refugiados, con un costo medio de unos 130 dólares cada uno, en todos los estados menos Alaska, en Puerto Rico y en 16 países. Los destinos principales fueron Nueva York, la Florida fuera de Miami, Nueva Jersey, California y Texas.

Aun así, según el mismo boletín, muchos refugiados no querían irse de Miami por sus lazos personales, el clima, el miedo a quedar aislados y el deseo de estar cerca de su país.

El resultado fue doble: una parte de los cubanos se repartió por todo Estados Unidos, y otra se quedó en Miami, donde los subsidios de alquiler, en lugar de los campamentos, facilitaron que surgiera la Pequeña Habana.""")],
 ["FR-S024", "FR-S021", "FR-S006", "FR-S017", "FR-S018"]),

(S, "contexto", [("¿Qué papel tuvo la Iglesia católica con los primeros exiliados en Miami?", """Según las fuentes que tenemos, la Iglesia católica de Miami ayudó a los cubanos antes de que llegara la ayuda federal, y también influyó en cómo se organizó la acogida.

Según la ficha del Servicio de Parques Nacionales, en 1959 el obispo Coleman Carroll creó el Centro Hispano Católico, y para diciembre de 1961 la diócesis de Miami había gastado unos 1,5 millones de dólares en ayuda a refugiados.

Según la misma ficha, el padre Bryan Walsh recordaba que algunos políticos querían alojar a todos los refugiados en un campamento en Opa-locka y que la diócesis se opuso; en su lugar se dieron subsidios de alquiler de 80 a 100 dólares al mes.

Con los niños que llegaban solos, la Iglesia también tuvo un papel. Según Rita Cauce, de la FIU, Walsh insistió en que los menores fueran atendidos por agencias de bienestar infantil con licencia y en que se respetara su religión. Quería evitar lo ocurrido con niños de la revolución húngara de 1956, colocados en casas con una simple llamada telefónica.

Según Cauce, la ayuda para los niños la supervisaba el Departamento de Bienestar Público de la Florida en nombre del gobierno federal, y cuatro agencias se encargaban del cuidado según la religión del niño, entre ellas el Catholic Welfare Bureau para los católicos.""")],
 ["FR-S023", "FR-S024", "FR-PP022", "FR-PP021"]),

(S, "contexto", [("¿Los primeros cubanos que llegaron eran exiliados o inmigrantes?", """Según las fuentes que tenemos, en aquellos primeros años tanto los propios cubanos como el gobierno de Estados Unidos los veían como exiliados.

Según la ficha del Servicio de Parques Nacionales, que cita a la historiadora María Cristina García, los cubanos de esa primera ola se veían a sí mismos como exiliados y no como inmigrantes, igual que el gobierno de Estados Unidos, y esa idea influyó en las políticas de reasentamiento.

El lenguaje oficial de la época lo refleja. Según el boletín de la Seguridad Social de 1962, el gobierno de Estados Unidos sostenía que a los refugiados se les consideraba 'no como intrusos sino como amigos' y los describía como 'exiliados por razones de conciencia'. Según el mismo boletín, Kennedy presentó la ayuda como temporal: pidió asegurar a los refugiados que se buscaría facilitar su regreso voluntario a Cuba en cuanto las condiciones lo permitieran.

La situación legal iba en la misma línea. A los cubanos se les autorizó una 'salida voluntaria indefinida', sin límite de tiempo, de modo que no se les abría proceso de deportación.

Era además una situación nueva para Estados Unidos. Con la llegada de los cubanos, el país fue por primera vez en su historia país de primer asilo para un gran número de refugiados, y por primera vez creó un programa para ayudar a refugiados de otro país del mismo hemisferio.""")],
 ["FR-S026", "FR-S021", "FR-S004", "FR-S005", "FR-S012"]),

(S, "hecho", [("¿Qué pasó en Bahía de Cochinos y qué relación tuvo con el exilio?", """Bahía de Cochinos fue un desembarco de exiliados cubanos en abril de 1961, y su fracaso coincidió con un aumento de las salidas de niños en Pedro Pan.

Según la ficha del Servicio de Parques Nacionales, la Brigada 2506, formada por unos 1.300 exiliados, desembarcó en Bahía de Cochinos el 17 de abril de 1961 y fue derrotada en tres días, con 117 muertos. Más de mil cayeron prisioneros y fueron liberados en diciembre de 1962 a cambio de más de 53 millones de dólares en alimentos y medicinas.

El fracaso tuvo efectos en la emigración. Según Rita Cauce, de la FIU, en la primera semana de Pedro Pan llegaban tres o cuatro niños al día, y las llegadas se multiplicaron después del fracaso de Bahía de Cochinos, en abril de 1961.

Ese mismo mes, según Cauce, se cerraron en Cuba las escuelas de sexto a duodécimo grado durante ocho meses y medio, y unos 100.000 jóvenes fueron enviados al campo a enseñar a leer y escribir a los campesinos en la campaña de alfabetización. Cauce cita esa campaña entre los hechos que pesaron en la decisión de muchos padres de enviar a sus hijos fuera.

Las fuentes que tenemos aquí no detallan la organización ni la planificación de la invasión; para eso harían falta otras fuentes.""")],
 ["FR-S027", "FR-PP027", "FR-PP049", "FR-PP009"]),

(S, "hecho", [("¿Por qué se cortaron los vuelos entre Cuba y Estados Unidos en 1962 y cómo salía la gente después?", """Los vuelos se cortaron con la Crisis de Octubre, en octubre de 1962, y no se reanudaron hasta diciembre de 1965.

Entre esas dos fechas, quienes querían llegar a Estados Unidos tenían que pasar por otros países, como España o México.

El corte dejó a mucha gente a medio camino. Según Rita Cauce, de la FIU, cuando se cerraron los vuelos en octubre de 1962 miles de niños se quedaron en Cuba con sus exenciones de visa de Pedro Pan en la mano. A ellos se les llama 'Pedro sin Pan'.

La salida directa volvió en 1965. Según la ficha del Servicio de Parques Nacionales, que toma las cifras de María Cristina García, los vuelos desde Cuba se reanudaron ese año y siguieron, con una breve pausa, hasta el 6 de abril de 1973; en más de 3.000 'Vuelos de la Libertad' llegaron otros 175.000 cubanos.

Según Cauce, esos vuelos daban prioridad a los padres y familiares directos de los niños cubanos menores de 21 años que ya estaban en Estados Unidos, y Walsh contó que el número de niños a cargo del programa bajó de unos 5.000 a 500 en seis meses.

Así que, entre 1962 y 1965, salir de Cuba hacia Estados Unidos obligaba a dar un rodeo por terceros países, y miles de niños con papeles para Pedro Pan se quedaron sin poder usarlos.""")],
 ["FR-S028", "FR-PP036", "FR-S011", "FR-PP034"]),

(S, "reformulacion", [("Leí que en 1960 llegaron 62.000 cubanos a Estados Unidos y en otro sitio que fueron 40.000. ¿Cuál es la buena?", """Las dos cifras aparecen en una fuente seria y, con lo que tenemos, no se puede decir cuál es la buena.

De hecho, las dos están en el mismo documento. La ficha del Servicio de Parques Nacionales sobre la Torre de la Libertad, citando a Levine y Asis, da 62.000 emigrados a Estados Unidos en 1960, 67.000 en 1961 y 66.000 en 1962. En otra página, la misma ficha dice que a finales de 1960 habían entrado unos 40.000, y no explica por qué las dos cifras no coinciden.

Otras fuentes cuentan de forma acumulada. El sociólogo Juan Clark, citado por Rita Cauce, de la FIU, da 64.000 salidas a finales de 1959 y 248.070 a finales de 1962.

Y hay una tercera forma de medir: quiénes se registraron en el centro de refugiados de Miami. Según el boletín de la Seguridad Social de 1962, de febrero a diciembre de 1961 se registraron unas 87.000 personas.

Fíjate que no todas miden lo mismo: unas son por año, otras acumuladas desde 1959, unas hablan de llegadas a Estados Unidos y otras de salidas de Cuba, y otra cuenta solo a quienes se registraron en Miami. Por eso conviene no comparar una con otra sin mirar qué está contando cada una.

Lo más honesto es dar la cifra con su fuente y aceptar que, para esos años, solo hay estimaciones que no coinciden del todo.""")],
 ["FR-S022", "FR-S001", "FR-S014"]),

(S, "hecho", [("¿Cuánto dinero puso Estados Unidos al principio para los refugiados cubanos?", """Las cifras del arranque del programa no coinciden del todo entre fuentes, pero dan una idea del tamaño.

La primera asignación del programa de Kennedy varía según la fuente: el boletín de la Seguridad Social de 1962 habla de 2 millones de dólares del fondo de contingencia del presidente para el año fiscal 1960-61, y Rita Cauce, de la FIU, citando un informe de 1963, habla de 4 millones adicionales hasta junio de 1961.

Antes ya había un centro en marcha. En noviembre de 1960 el presidente Eisenhower encargó a Tracy S. Voorhees estudiar la situación, y bajo su dirección se creó en Miami un Centro de Emergencia para Refugiados Cubanos, financiado en parte con el fondo de contingencia del presidente.

El dinero se repartía en varios frentes. Según el boletín, el gobierno federal pagaba la mitad del costo por alumno de los niños refugiados en las escuelas de Dade, financiaba clases de inglés para más de 6.000 adultos y daba préstamos a estudiantes universitarios cubanos. Reasentar a una persona fuera de Miami costaba de media unos 130 dólares.

No todo era dinero público. Según la ficha del Servicio de Parques Nacionales, para diciembre de 1961 la diócesis de Miami había gastado unos 1,5 millones de dólares en ayuda a refugiados.

En 1962 la administración Kennedy impulsó además la Ley de Asistencia a la Migración y a los Refugiados para dar ayuda a los cubanos que llegaban a Miami.""")],
 ["FR-S013", "FR-S002", "FR-S029", "FR-S017", "FR-S023", "FR-S010"]),

(S, "humano", [("Mi abuelo era profesor en La Habana y cuando llegó a Miami en 1961 tuvo que trabajar en lo que apareció. ¿Le pasó a mucha gente?", """Las fuentes de la época no dan una cifra de cuántos tuvieron que cambiar de oficio, pero sí describen la situación en la que llegaba la gente como tu abuelo.

Según el boletín de la Seguridad Social de 1962, a principios de 1961 más de la mitad del profesorado de la Universidad de La Habana vivía en Miami o cerca. Más de un tercio de los cabezas de familia refugiados había trabajado en ocupaciones profesionales, semiprofesionales o directivas.

El primer obstáculo solía ser el idioma: según el mismo boletín, solo un 25 % de los refugiados registrados hablaba inglés lo bastante bien para trabajar. Y llegaban sin recursos: desde diciembre de 1960 solo se podía sacar de Cuba la ropa y 5 pesos que valían unos 50 centavos.

El programa federal intentó ayudar con eso. Financiaba clases de inglés para más de 6.000 adultos y daba préstamos a estudiantes universitarios cubanos. También puso el acento en reasentar a los cubanos fuera de Miami, pero según el mismo boletín muchos refugiados no querían irse de allí por sus lazos personales, el clima, el miedo a quedar aislados y el deseo de estar cerca de su país.

Lo que esas fuentes no dicen es cuántos profesionales tuvieron que trabajar en otra cosa ni cuánto tardaron en volver a lo suyo.

Si tu abuelo vive, o alguien de la familia lo recuerda, vale la pena preguntarle cuál fue su primer trabajo en Miami y si volvió a dar clases. Esas historias son las que mejor explican cómo fue esa etapa.""")],
 ["FR-S015", "FR-S008", "FR-S020", "FR-S029", "FR-S006", "FR-S018"]),

# ------------------------------------------------------------------ Pedro Pan
(P, "hecho", [("¿Cómo se organizó Pedro Pan al principio?", """Pedro Pan empezó como un plan pequeño y fue creciendo.

Según Rita Cauce, de la FIU, el plan original era sacar a unos 200 niños con visas de estudiante. El padre Bryan Walsh consiguió formularios de matrícula de la escuela secundaria de Coral Gables y firmó cartas asumiendo la responsabilidad de los menores.

Cuando Estados Unidos rompió relaciones con Cuba, el 3 de enero de 1961, el Departamento de Estado autorizó el 9 de enero a la agencia de Walsh, el Catholic Welfare Bureau, a emitir exenciones de visa: cartas firmadas por él que las aerolíneas aceptaban.

Hacer llegar esos papeles a Cuba fue otra parte del trabajo. Según Cauce, los documentos se movían entre Miami y La Habana en valijas diplomáticas, llevadas por simpatizantes como el agregado británico y esposas de embajadores, y miles de cartas de exención firmadas por Walsh fueron copiadas y repartidas por una red clandestina. Según Wikipedia, entre las personas clave en Cuba estaban Polita Grau y su hermano Ramón Grau Alsina.

Quedaba el problema del dinero. Según Wikipedia, empresarios estadounidenses de la antigua Cámara de Comercio de La Habana ayudaron a pagar los pasajes: enviaban cheques a personas en Miami, que a su vez pagaban a la agencia de viajes W. Henry Smith de La Habana, porque los pasajes no se podían comprar con pesos cubanos.

En la primera semana llegaban tres o cuatro niños al día, según Cauce, y las llegadas se multiplicaron después de Bahía de Cochinos.""")],
 ["FR-PP023", "FR-PP004", "FR-PP025", "FR-PP026", "FR-PP043", "FR-PP027"]),

(P, "contexto", [("¿Quién cuidaba a los niños de Pedro Pan que no tenían familia en Estados Unidos?", """Aproximadamente la mitad de los niños de Pedro Pan tenía familiares o amigos en Estados Unidos que los acogieron. El resto quedaba a cargo de agencias según su religión, y el Catholic Welfare Bureau atendió a algo más de 7.000.

Según Rita Cauce, de la FIU, la ayuda la supervisaba el Departamento de Bienestar Público de la Florida en nombre del gobierno federal, y cuatro agencias se encargaban del cuidado: el Catholic Welfare Bureau de los niños católicos, el Children's Service Bureau de Dade de los protestantes, y el Jewish Family and Children's Service y la HIAS de los judíos.

Según Cauce, el padre Bryan Walsh insistió en que los menores fueran atendidos por agencias de bienestar infantil con licencia y en que se respetara su religión, para no repetir lo ocurrido con niños de la revolución húngara de 1956.

Las otras agencias atendieron a muchos menos niños que la católica. Según Cauce, el Children's Service Bureau atendió a varios cientos de niños protestantes y de otras confesiones, y sobre los niños judíos hay dos cifras: 396 según los archivos de la HIAS y 145 según la Oficina Federal de la Infancia en abril de 1967.

En Miami, el albergue más grande fue el campamento de Florida City, un bloque de edificios de apartamentos para niñas de hasta 18 años y niños menores de 12. La familia Ferré prestó una casa en Miami para alojar a adolescentes varones.

Según el boletín de la Seguridad Social de 1962, al 31 de diciembre de 1961 había 2.309 niños refugiados en hogares de acogida o en instituciones, un tercio en el área de Miami; el programa había atendido a unos 3.000, y cerca de 1.000 ya se habían reunido con sus familias.""")],
 ["FR-PP006", "FR-PP021", "FR-PP022", "FR-PP031", "FR-PP032", "FR-PP030"]),

(P, "reformulacion", [("Siempre oigo que los de Pedro Pan eran niños chiquitos. ¿Es así?", """No del todo. Había niños pequeños, pero también muchos adolescentes, y las fuentes no describen las edades de la misma manera.

El boletín de la Seguridad Social de 1962 dice que la mayoría tenía entre 5 y 16 años. El padre Bryan Walsh, cuya agencia atendió a unos 7.000 de los niños, dice que el 85 % de ellos tenía entre 12 y 18 años al llegar y que el 70 % eran varones mayores de 12. Wikipedia dice que la mayoría eran adolescentes varones.

Las fuentes no explican de dónde viene la diferencia, pero hay que tener en cuenta que Walsh habla solo de los niños que pasaron por su agencia, no de todos los que salieron.

La edad también importaba para los papeles. La autorización del Departamento de Estado para las exenciones de visa era general para niños de 6 a 16 años; para los de 16 a 18 había que pedir antes una revisión de seguridad.

Y la edad marcaba dónde vivían. En el campamento de Florida City había niñas de hasta 18 años y niños menores de 12, y para adolescentes varones la familia Ferré prestó una casa en Miami.

Así que la imagen de niños muy pequeños no es falsa, pero se queda corta: según Walsh y Wikipedia, buena parte eran adolescentes, sobre todo varones.""")],
 ["FR-PP029", "FR-PP007", "FR-PP004", "FR-PP032"]),

(P, "perspectivas", [("¿Cómo se ve Pedro Pan desde el gobierno cubano y desde los que salieron?", """Pedro Pan se cuenta de formas casi opuestas según quién hable, y vale la pena conocer cada versión con su fuente.

La versión del gobierno cubano está en EcuRed, su enciclopedia oficial. Según EcuRed, la jerarquía de la Iglesia en Cuba, la mayor parte del clero y sus organizaciones laicas se aliaron con la Iglesia y el gobierno de Estados Unidos y alentaron la emigración. EcuRed compara Pedro Pan con la salida de niños vascos y de niños judíos de Alemania a finales de los años treinta, y afirma que, a diferencia de ellas, esta se hizo sin ninguna justificación política, ética ni moral. También cita a la escritora estadounidense Joan Didion, según la cual dar al padre Walsh plena autoridad para emitir exenciones de visa fue un acto sin precedentes y contrario a la ley de Estados Unidos.

Del otro lado, el padre Bryan Walsh sostiene que su agencia no tenía constancia de ningún niño perdido, que ningún menor fue dado en adopción y que la Iglesia en Cuba como institución no participó.

Entre los que salieron hay también voces propias. Según Rita Cauce, de la FIU, el profesor de Yale Carlos Eire, que salió en Pedro Pan, afirmó que fue el mayor éxodo de niños en la historia de América y que pasó casi inadvertido, y pidió a los Pedro Pan contar sus historias porque cada uno se ha encontrado alguna vez con una narración muy distinta de lo que vivió.

Son versiones que no se pueden reconciliar del todo. Para los hechos concretos, lo más útil es contrastar cada afirmación con documentos.""")],
 ["FR-PP045", "FR-PP046", "FR-PP048", "FR-PP015", "FR-PP037"]),

(P, "contexto", [("¿Qué pasó con los niños de Pedro Pan cuando se hicieron adultos?", """No hay una sola historia, pero las fuentes describen algunos rasgos comunes.

Según Rita Cauce, de la FIU, durante sus primeros 30 años en Estados Unidos la mayoría de los Pedro Pan no conocía la magnitud del éxodo ni sabía que había formado parte de él. Intentaron adaptarse a la cultura estadounidense y solo de adultos empezaron a investigar su historia.

Los caminos fueron muy distintos. Según Wikipedia, en una sección que todavía pide más fuentes, muchos Pedro Pan tuvieron dificultades para adaptarse y se sintieron ajenos tanto a su país como al nuevo; algunos participaron en el movimiento por los derechos civiles o contra la guerra, o rechazaron la ideología de sus padres, y otros tuvieron mucho éxito profesional.

Con el tiempo se organizaron. Según Cauce, en 1991 antiguos niños de Pedro Pan fundaron Operation Pedro Pan Group, que mantiene el contacto con más de 2.000 de ellos, y gracias a su trabajo el sitio del albergue de Florida City fue declarado lugar histórico de la Florida.

La memoria también llegó a otros estados. Según Cauce, Nuevo México fue el segundo estado, después de la Florida, en recibir niños de Pedro Pan, con 374, y la alcaldía de Albuquerque proclamó el 18 de mayo de 2012 'Día de Pedro Pan'.

Parte de esa historia sigue cerrada. Según Cauce, los papeles del padre Bryan Walsh sobre Pedro Pan están en el archivo de Barry University, pero los expedientes personales de los niños están restringidos hasta 2050.""")],
 ["FR-PP038", "FR-PP041", "FR-PP039", "FR-PP040", "FR-PP044"]),

(P, "hecho", [("¿Qué pasó con los niños que tenían la visa de Pedro Pan pero no llegaron a salir?", """Son los llamados 'Pedro sin Pan', y su historia está ligada al corte de los vuelos en 1962.

Según Rita Cauce, de la FIU, cuando se cerraron los vuelos en octubre de 1962, con la Crisis de Octubre, miles de niños se quedaron en Cuba con sus exenciones de visa en la mano. Entre esa fecha y diciembre de 1965 no hubo vuelos entre Cuba y Estados Unidos, y quien quería llegar tenía que pasar por otros países, como España o México.

Para las familias que ya estaban separadas, la situación también se complicó. Una vez en Estados Unidos, los niños de Pedro Pan podían pedir exenciones de visa para sus padres en Cuba; según Wikipedia, el Departamento de Estado lo permitió desde septiembre de 1961. Pero desde octubre de 1962 ya no había vuelos directos para usarlas.

La salida volvió con los Vuelos de la Libertad. Según Cauce, esos vuelos daban prioridad a los padres y familiares directos de los niños cubanos menores de 21 años que estaban en Estados Unidos, y Walsh contó que el número de niños a cargo del programa bajó de unos 5.000 a 500 en seis meses.

El programa federal para niños cubanos siguió funcionando muchos años, aunque la fecha de cierre varía según la fuente: Cauce dice que siguió atendiendo a niños llegados de Cuba hasta 1982 y Wikipedia dice que hasta 1981. Wikipedia calcula además que unos 25.000 niños pasaron por el programa en total.""")],
 ["FR-PP036", "FR-S028", "FR-PP033", "FR-PP034", "FR-PP035"]),

(P, "perspectivas", [("¿Por qué tantos padres cubanos mandaron a sus hijos solos a Estados Unidos?", """Es una de las preguntas centrales de Pedro Pan, y la respuesta cambia según la fuente.

Rita Cauce, de la FIU, sostiene que los padres querían evitar que sus hijos recibieran adoctrinamiento comunista. Entre los hechos que pesaron cita la campaña de alfabetización y la confiscación de las escuelas privadas y católicas en 1961. Según Cauce, en abril de ese año se cerraron las escuelas de sexto a duodécimo grado durante ocho meses y medio, y unos 100.000 jóvenes fueron enviados al campo a enseñar a leer y escribir a los campesinos. Cauce afirma además que las organizaciones juveniles del gobierno buscaban adoctrinar a los jóvenes y que se esperaba que vigilaran e informaran sobre sus padres.

Hubo también un rumor que pesó mucho: que el gobierno iba a quitar a los padres la patria potestad sobre sus hijos. Esa ley nunca existió, pero el rumor circuló en aquellos años y empujó a muchas familias a decidir.

El gobierno cubano lo explica de otra manera. Según EcuRed, su enciclopedia oficial, fue una operación de subversión organizada por el Departamento de Estado, la jerarquía católica de Miami, la CIA y organizaciones opuestas al gobierno revolucionario, que manipuló el tema de la patria potestad. EcuRed afirma también que la jerarquía de la Iglesia en Cuba y la mayor parte del clero alentaron la emigración.

Con lo documentado, la ley de la patria potestad nunca existió. El cierre de las escuelas por la campaña de alfabetización lo recoge Cauce como uno de los hechos que pesaron en las familias.""")],
 ["FR-PP009", "FR-PP049", "FR-PP050", "FR-PP010", "FR-PP013", "FR-PP045"]),
]

if DESTINO.exists():
    with DESTINO.open(encoding="utf-8-sig") as f:
        revisados = [json.loads(l)["id"] for l in f if l.strip() and json.loads(l).get("estado_revision") != "pendiente"]
    if revisados:
        print(f"{DESTINO} ya tiene {len(revisados)} ejemplos revisados ({', '.join(revisados[:5])}...). No lo sobrescribo.")
        sys.exit(1)

usados = sorted({x for _, _, _, ids in E for x in ids})
faltan = [x for x in usados if x not in frag]
no_aprobados = [x for x in usados if x in frag and frag[x].get("estado") != "aprobado"]
if faltan or no_aprobados:
    print(f"No genero nada. Fragmentos que no existen: {faltan}. Fragmentos sin aprobar: {no_aprobados}.")
    sys.exit(1)

DESTINO.parent.mkdir(exist_ok=True)
with DESTINO.open("w", encoding="utf-8", newline="\n") as f:
    for i, (etapa, tipo, turnos, ids) in enumerate(E):
        mensajes = []
        for preg, resp in turnos:
            mensajes += [{"role": "user", "content": preg}, {"role": "assistant", "content": resp.strip()}]
        ej = {"id": f"{PREFIJO}{PRIMER_ID + i:03d}", "etapa": etapa, "tipo": tipo, "messages": mensajes,
              "fuentes": [{"id_fragmento": x, "id_fuente": frag[x]["id_fuente"], "fragmento": frag[x]["texto"]} for x in ids],
              "estado_revision": "pendiente", "revisor": "", "notas": "1959-1962 lote 2"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
