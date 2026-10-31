"""
agregar_1959_lote2.py — Añade fragmentos nuevos a fuentes/fragmentos_1959_1962.jsonl (etapas salida_1959_1962
y pedro_pan), sacados de documentos que ya están registrados (F026-F032). No registra fuentes nuevas.

Uso (desde E:\\vertex-exilio):
    python agregar_1959_lote2.py

Documentos releídos (en fuentes/docs): FIU_Cauce_Pedro_Pan.pdf (F026), NPS_freedom_tower_NHL.pdf (F027),
v25n3p3.pdf (F029, boletín de la Seguridad Social, marzo de 1962), WIKI_operation_peter_pan.html (F031),
ECURED_operacion_peter_pan.html (F032). En F029 las páginas son las impresas del boletín (3-8); en F026, las
de Cauce; en F027, las del formulario del NPS.

Qué hace:
  1. Copia de seguridad del archivo de fragmentos.
  2. Añade los fragmentos nuevos en 'pendiente' (FR-S012 en adelante y FR-PP020 en adelante).
     Si alguno de esos IDs ya existe, no toca nada.
"""
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

FRAG = Path("fuentes/fragmentos_1959_1962.jsonl")
S, P = "salida_1959_1962", "pedro_pan"

# (id, etapa, tipo, fuente, ubicación, corroborado_por, actor, texto)
NUEVOS = [
    # ---------------- salida 1959-1962
    ("FR-S012", S, "hecho", "F029", "p. 3", ["F027"], None,
     "Con la llegada de los cubanos, Estados Unidos fue por primera vez en su historia país de primer asilo para un "
     "gran número de refugiados, y por primera vez creó un programa para ayudar a refugiados de otro país del "
     "mismo hemisferio."),
    ("FR-S013", S, "cifra_disputada", "F029", "p. 4", ["F026"], None,
     "La primera asignación del programa de Kennedy para refugiados cubanos varía según la fuente: el boletín de "
     "la Seguridad Social de 1962 habla de 2 millones de dólares del fondo de contingencia del presidente para el "
     "año fiscal 1960-61, y Cauce, citando un informe de 1963, habla de 4 millones adicionales hasta junio de 1961."),
    ("FR-S014", S, "hecho_atribuido", "F029", "pp. 5, 8", [], None,
     "Según el boletín de la Seguridad Social de 1962, de febrero a diciembre de 1961 se registraron unas 87.000 "
     "personas en el centro de refugiados de Miami, y a finales de 1961 seguían registrándose unas 2.000 por semana."),
    ("FR-S015", S, "hecho_atribuido", "F029", "p. 5", [], None,
     "Según el boletín de la Seguridad Social de 1962, tres cuartas partes de los refugiados registrados tenían "
     "entre 20 y 50 años, cerca del 60 % eran hombres, solo un 25 % hablaba inglés lo bastante bien para trabajar, "
     "y a principios de 1961 más de la mitad del profesorado de la Universidad de La Habana vivía en Miami o cerca."),
    ("FR-S016", S, "hecho_atribuido", "F029", "pp. 5-6", [], None,
     "Según el boletín de la Seguridad Social de 1962, algunos refugiados devolvieron por su cuenta parte de la "
     "ayuda recibida: de mayo a diciembre de 1961 las devoluciones voluntarias sumaron 119.930 dólares, y solo en "
     "diciembre 874 refugiados devolvieron 48.873,97 dólares."),
    ("FR-S017", S, "hecho_atribuido", "F029", "p. 6", [], None,
     "Según el boletín de la Seguridad Social de 1962, a finales de 1961 se habían reasentado 16.532 refugiados, con "
     "un costo medio de unos 130 dólares cada uno, en todos los estados menos Alaska, en Puerto Rico y en 16 países; "
     "los destinos principales fueron Nueva York, la Florida fuera de Miami, Nueva Jersey, California y Texas."),
    ("FR-S018", S, "hecho_atribuido", "F029", "p. 6", [], None,
     "Según el boletín de la Seguridad Social de 1962, muchos refugiados no querían irse de Miami por sus lazos "
     "personales, el clima, el miedo a quedar aislados y el deseo de estar cerca de su país."),
    ("FR-S019", S, "hecho", "F029", "p. 7", ["F027"], None,
     "La ayuda en efectivo del programa para refugiados cubanos tenía un máximo de 100 dólares al mes para una "
     "familia y 60 dólares para una persona sola."),
    ("FR-S020", S, "hecho_atribuido", "F029", "p. 7", [], None,
     "Según el boletín de la Seguridad Social de 1962, quienes salían de Cuba desde diciembre de 1960 solo podían "
     "llevar su ropa, sin muebles y con 5 pesos que valían unos 50 centavos; del 27 de febrero a finales de 1961 el "
     "programa pagó 8.451.308 dólares en ayuda, y a fin de año la recibían 21.294 casos."),
    ("FR-S021", S, "postura", "F029", "pp. 4-5, 7", [], "gobierno_eeuu",
     "Según el boletín de la Seguridad Social de 1962, el gobierno de Estados Unidos sostenía que a los refugiados "
     "se les consideraba 'no como intrusos sino como amigos', los describía como 'exiliados por razones de "
     "conciencia' y prefería no crear campamentos de refugiados para no fomentar la dependencia."),
    ("FR-S022", S, "cifra_disputada", "F027", "pp. 18-19", ["F026"], None,
     "Las cifras de salidas en los primeros años varían según la fuente: la ficha del Servicio de Parques "
     "Nacionales, citando a Levine y Asis, da 62.000 emigrados a Estados Unidos en 1960, 67.000 en 1961 y 66.000 en "
     "1962, y en otra página dice que a finales de 1960 habían entrado unos 40.000; el sociólogo Juan Clark, citado "
     "por Cauce, da 64.000 salidas a finales de 1959 y 248.070 a finales de 1962."),
    ("FR-S023", S, "hecho_atribuido", "F027", "p. 19", [], None,
     "Según la ficha del Servicio de Parques Nacionales, antes de que llegara la ayuda federal la Iglesia católica "
     "encabezó la asistencia a los cubanos: en 1959 el obispo Coleman Carroll creó el Centro Hispano Católico, y para "
     "diciembre de 1961 la diócesis de Miami había gastado unos 1,5 millones de dólares en ayuda a refugiados."),
    ("FR-S024", S, "hecho_atribuido", "F027", "p. 20", [], None,
     "Según la ficha del Servicio de Parques Nacionales, el padre Walsh recordaba que algunos políticos querían "
     "alojar a todos los refugiados en un campamento en Opa-locka y que la diócesis se opuso; en su lugar se dieron "
     "subsidios de alquiler de 80 a 100 dólares al mes, que facilitaron que surgiera la Pequeña Habana."),
    ("FR-S025", S, "hecho_atribuido", "F027", "p. 20", [], None,
     "Según la ficha del Servicio de Parques Nacionales, el 1 de julio de 1962 el gobierno federal alquiló los "
     "cuatro primeros pisos del antiguo edificio del Miami News para el centro de asistencia, la futura Torre de la "
     "Libertad, y el personal del centro pasó de 14 a más de 300 personas en un año."),
    ("FR-S026", S, "hecho_atribuido", "F027", "p. 17", [], None,
     "Según la ficha del Servicio de Parques Nacionales, que cita a la historiadora María Cristina García, los cubanos "
     "de esa primera ola se veían a sí mismos como exiliados y no como inmigrantes, igual que el gobierno de Estados "
     "Unidos, y esa idea influyó en las políticas de reasentamiento."),
    ("FR-S027", S, "hecho_atribuido", "F027", "p. 18", [], None,
     "Según la ficha del Servicio de Parques Nacionales, la Brigada 2506, de unos 1.300 exiliados, desembarcó en "
     "Bahía de Cochinos el 17 de abril de 1961 y fue derrotada en tres días, con 117 muertos; más de mil prisioneros "
     "fueron liberados en diciembre de 1962 a cambio de más de 53 millones de dólares en alimentos y medicinas."),
    ("FR-S028", S, "hecho", "F027", "p. 18", ["F031"], None,
     "Entre octubre de 1962, con la Crisis de Octubre, y diciembre de 1965 no hubo vuelos entre Cuba y Estados "
     "Unidos, y quienes querían llegar a Estados Unidos tenían que pasar por otros países, como España o México."),
    ("FR-S029", S, "hecho_atribuido", "F029", "pp. 7-8", [], None,
     "Según el boletín de la Seguridad Social de 1962, el gobierno federal pagaba la mitad del costo por alumno de "
     "los niños refugiados en las escuelas de Dade, financiaba clases de inglés para más de 6.000 adultos y daba "
     "préstamos a estudiantes universitarios cubanos."),
    # ---------------- Pedro Pan
    ("FR-PP020", P, "hecho", "F029", "pp. 3-4", ["F026"], None,
     "El programa de nueve puntos que Kennedy ordenó en febrero de 1961 incluía, en el punto 8, ayuda económica para "
     "el cuidado y la protección de los niños que llegaban sin acompañante, a los que llamó 'el grupo más indefenso' "
     "entre los refugiados."),
    ("FR-PP021", P, "hecho_atribuido", "F026", "pp. 7-8", [], None,
     "Según Cauce, la ayuda para los niños la supervisaba el Departamento de Bienestar Público de la Florida en nombre "
     "del gobierno federal, y cuatro agencias se encargaban del cuidado: el Catholic Welfare Bureau de los niños "
     "católicos, el Children's Service Bureau de Dade de los protestantes, y el Jewish Family and Children's Service "
     "y la HIAS de los judíos."),
    ("FR-PP022", P, "hecho_atribuido", "F026", "p. 6", [], None,
     "Según Cauce, Walsh insistió en que los menores fueran atendidos por agencias de bienestar infantil con licencia "
     "y en que se respetara su religión, para no repetir lo ocurrido con niños de la revolución húngara de 1956, "
     "colocados en casas con una simple llamada telefónica."),
    ("FR-PP023", P, "hecho_atribuido", "F026", "p. 7", [], None,
     "Según Cauce, el plan original era sacar a unos 200 niños con visas de estudiante: Walsh consiguió formularios "
     "de matrícula de la escuela secundaria de Coral Gables y firmó cartas asumiendo la responsabilidad de los menores."),
    ("FR-PP024", P, "postura", "F032", "texto", [], "gobierno_cubano",
     "Según EcuRed, los primeros cinco niños de la operación llegaron a Miami el 26 de diciembre de 1960 en el vuelo "
     "422 de Pan American, y cuando Estados Unidos rompió relaciones quedaron sin tramitar unos 100 pasaportes del "
     "grupo inicial de 200."),
    ("FR-PP025", P, "hecho_atribuido", "F026", "p. 8", [], None,
     "Según Cauce, los documentos de los niños se movían entre Miami y La Habana en valijas diplomáticas, llevadas por "
     "simpatizantes como el agregado británico y esposas de embajadores, y miles de cartas de exención firmadas por "
     "Walsh fueron copiadas y repartidas por una red clandestina."),
    ("FR-PP026", P, "hecho_atribuido", "F031", "Organizing an exodus", [], None,
     "Según Wikipedia, entre las personas clave de la operación en Cuba estaban Polita Grau y su hermano Ramón Grau "
     "Alsina."),
    ("FR-PP027", P, "hecho_atribuido", "F026", "p. 9", [], None,
     "Según Cauce, en la primera semana llegaban tres o cuatro niños al día, y las llegadas se multiplicaron después "
     "del fracaso de Bahía de Cochinos, en abril de 1961."),
    ("FR-PP028", P, "hecho_atribuido", "F031", "End", [], None,
     "Según Wikipedia, el programa se mantuvo en secreto hasta febrero de 1962, cuando lo dio a conocer el diario The "
     "Plain Dealer, y el 9 de marzo de 1962 el periodista Gene Miller, del Miami Herald, acuñó el nombre de Operación "
     "Pedro Pan."),
    ("FR-PP029", P, "cifra_disputada", "F029", "p. 7", ["F028", "F031"], None,
     "La edad de los niños de Pedro Pan se describe de forma distinta: el boletín de la Seguridad Social de 1962 dice "
     "que la mayoría tenía entre 5 y 16 años; Walsh dice que el 85 % de los 7.000 que atendió su agencia tenía entre "
     "12 y 18 años y que el 70 % eran varones mayores de 12; Wikipedia dice que la mayoría eran adolescentes varones."),
    ("FR-PP030", P, "hecho_atribuido", "F029", "p. 7", [], None,
     "Según el boletín de la Seguridad Social de 1962, al 31 de diciembre de 1961 había 2.309 niños refugiados en "
     "hogares de acogida o en instituciones, un tercio en el área de Miami; el programa había atendido a unos 3.000, "
     "y cerca de 1.000 ya se habían reunido con sus familias."),
    ("FR-PP031", P, "hecho_atribuido", "F026", "p. 9, nota 31", [], None,
     "Según Cauce, el Children's Service Bureau atendió a varios cientos de niños protestantes y de otras confesiones, "
     "y sobre los niños judíos hay dos cifras: 396 según los archivos de la HIAS y 145 según la Oficina Federal de la "
     "Infancia en abril de 1967."),
    ("FR-PP032", P, "hecho_atribuido", "F026", "p. 9", [], None,
     "Según Cauce, el albergue más grande fue el campamento de Florida City, un bloque de edificios de apartamentos para "
     "niñas de hasta 18 años y niños menores de 12, y la familia Ferré prestó una casa en Miami para alojar a "
     "adolescentes varones."),
    ("FR-PP033", P, "hecho", "F026", "p. 2", ["F031"], None,
     "Una vez en Estados Unidos, los niños de Pedro Pan podían pedir exenciones de visa para sus padres en Cuba; según "
     "Wikipedia, el Departamento de Estado lo permitió desde septiembre de 1961."),
    ("FR-PP034", P, "hecho_atribuido", "F026", "p. 10", [], None,
     "Según Cauce, los Vuelos de la Libertad daban prioridad a los padres y familiares directos de los niños cubanos "
     "menores de 21 años que estaban en Estados Unidos, y Walsh contó que el número de niños a cargo del programa bajó "
     "de unos 5.000 a 500 en seis meses."),
    ("FR-PP035", P, "cifra_disputada", "F026", "p. 10", ["F031"], None,
     "La fecha de cierre del programa federal para niños cubanos varía según la fuente: Cauce dice que siguió atendiendo "
     "a niños llegados de Cuba hasta 1982 y Wikipedia dice que hasta 1981; Wikipedia calcula además que unos 25.000 "
     "niños pasaron por el programa en total."),
    ("FR-PP036", P, "hecho_atribuido", "F026", "p. 11", [], None,
     "Según Cauce, cuando se cerraron los vuelos en octubre de 1962 miles de niños se quedaron en Cuba con sus "
     "exenciones de visa en la mano; a ellos se les llama 'Pedro sin Pan'."),
    ("FR-PP037", P, "postura", "F026", "pp. 1, 11", [], "Carlos Eire",
     "Según Cauce, el profesor de Yale Carlos Eire, que salió en Pedro Pan, afirmó que fue el mayor éxodo de niños en "
     "la historia de América y que pasó casi inadvertido, y pidió a los Pedro Pan contar sus historias porque cada uno "
     "se ha encontrado alguna vez con una narración muy distinta de lo que vivió."),
    ("FR-PP038", P, "hecho_atribuido", "F026", "p. 1", [], None,
     "Según Cauce, durante sus primeros 30 años en Estados Unidos la mayoría de los Pedro Pan no conocía la magnitud "
     "del éxodo ni sabía que había formado parte de él; intentaron adaptarse a la cultura estadounidense y solo de "
     "adultos empezaron a investigar su historia."),
    ("FR-PP039", P, "hecho_atribuido", "F026", "p. 10", [], None,
     "Según Cauce, en 1991 antiguos niños de Pedro Pan fundaron Operation Pedro Pan Group, que mantiene el contacto con "
     "más de 2.000 de ellos, y gracias a su trabajo el sitio del albergue de Florida City fue declarado lugar histórico "
     "de la Florida."),
    ("FR-PP040", P, "hecho_atribuido", "F026", "p. 10", [], None,
     "Según Cauce, Nuevo México fue el segundo estado, después de la Florida, en recibir niños de Pedro Pan, con 374, y "
     "la alcaldía de Albuquerque proclamó el 18 de mayo de 2012 'Día de Pedro Pan'."),
    ("FR-PP041", P, "hecho_atribuido", "F031", "Pedro Pan children", [], None,
     "Según Wikipedia, en una sección que pide más fuentes, muchos Pedro Pan tuvieron dificultades para adaptarse y se "
     "sintieron ajenos tanto a su país como al nuevo; algunos participaron en el movimiento por los derechos civiles o "
     "contra la guerra, o rechazaron la ideología de sus padres, y otros tuvieron mucho éxito profesional."),
    ("FR-PP042", P, "hecho_atribuido", "F031", "Film", [], None,
     "Según Wikipedia, el fiscal general Robert F. Kennedy aprobó fondos para una película de la Agencia de Información "
     "de Estados Unidos, 'The Lost Apple', sobre niños del campamento de Florida City, para explicarles por qué estaban "
     "allí; Wikipedia la califica de propaganda y señala que no menciona lo que pasaba en Cuba."),
    ("FR-PP043", P, "hecho_atribuido", "F031", "Funding", [], None,
     "Según Wikipedia, empresarios estadounidenses de la antigua Cámara de Comercio de La Habana ayudaron a financiar "
     "los pasajes: el dinero se enviaba con cheques a personas en Miami, que a su vez pagaban a la agencia de viajes W. "
     "Henry Smith de La Habana, porque los pasajes no se podían comprar con pesos cubanos."),
    ("FR-PP044", P, "hecho_atribuido", "F026", "pp. 3-4", [], None,
     "Según Cauce, Bryan O. Walsh nació en Irlanda en 1930 y murió en 2001; sus papeles sobre Pedro Pan están en el "
     "archivo de Barry University, y los expedientes personales de los niños están restringidos hasta 2050."),
    ("FR-PP045", P, "postura", "F032", "texto", [], "gobierno_cubano",
     "Según EcuRed, la jerarquía de la Iglesia en Cuba, la mayor parte del clero y sus organizaciones laicas se aliaron "
     "con la Iglesia y el gobierno de Estados Unidos y alentaron la emigración."),
    ("FR-PP046", P, "postura", "F032", "texto", [], "gobierno_cubano",
     "Según EcuRed, a diferencia de la salida de 20.000 niños vascos en 1937 o de 30.000 niños judíos de Alemania en "
     "1938-1939, la Operación Peter Pan se hizo sin ninguna justificación política, ética ni moral."),
    ("FR-PP047", P, "postura", "F032", "texto", [], "gobierno_cubano",
     "Según EcuRed, el 9 de enero de 1961 el Departamento de Estado aprobó también una ruta La Habana-Kingston-Miami, "
     "con visas británicas de tránsito por Jamaica gestionadas por Penny Powers en la embajada británica."),
    ("FR-PP048", P, "postura", "F032", "texto", [], "gobierno_cubano",
     "Según EcuRed, que cita a la escritora estadounidense Joan Didion, dar a Walsh plena autoridad para emitir "
     "exenciones de visa fue un acto sin precedentes y contrario a la ley de Estados Unidos."),
    ("FR-PP049", P, "hecho_atribuido", "F026", "p. 5", [], None,
     "Según Cauce, en abril de 1961 se cerraron las escuelas de sexto a duodécimo grado durante ocho meses y medio, y "
     "unos 100.000 jóvenes fueron enviados al campo a enseñar a leer y escribir a los campesinos en la campaña de "
     "alfabetización."),
    ("FR-PP050", P, "postura", "F026", "pp. 4-5", [], "Cauce (FIU)",
     "Según Cauce, entre lo que pesó en la decisión de los padres estaban las organizaciones juveniles del gobierno, "
     "como los Pioneros Rebeldes para niños de 6 a 13 años y la Asociación de Jóvenes Rebeldes para los de 14 a 21, que "
     "según ella buscaban adoctrinar a los jóvenes, y afirma que se esperaba que los jóvenes vigilaran e informaran "
     "sobre sus padres."),
]

if not FRAG.exists():
    print(f"No encuentro {FRAG}. ¿Estás en E:\\vertex-exilio? No toco nada.")
    sys.exit(1)

with FRAG.open(encoding="utf-8-sig") as f:
    lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n[0] for n in NUEVOS if n[0] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(FRAG, FRAG.with_name(f"{FRAG.name}.{marca}.bak"))
with FRAG.open("a", encoding="utf-8", newline="\n") as f:
    if lineas and not lineas[-1].endswith("\n"):
        f.write("\n")
    for fid, etapa, tipo, fuente, ubic, corr, actor, texto in NUEVOS:
        d = {"id": fid, "etapa": etapa, "tipo": tipo, "id_fuente": fuente, "ubicacion": ubic,
             "corroborado_por": corr, "texto": texto, "notas": "", "revisado": False, "estado": "pendiente"}
        if actor:
            d["actor"] = actor
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Añadidos {len(NUEVOS)} fragmentos nuevos a {FRAG} (en 'pendiente').")
print(f"Ahora: python revisar.py {FRAG}")
