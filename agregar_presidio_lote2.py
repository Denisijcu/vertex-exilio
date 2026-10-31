"""
agregar_presidio_lote2.py — Registra cinco fuentes nuevas (F067-F071) y añade fragmentos nuevos a
fuentes/fragmentos_presidio.jsonl (FR-P033 en adelante).

Uso (desde E:\\vertex-exilio):
    python agregar_presidio_lote2.py

Fuentes nuevas (en fuentes/docs, descargadas el 2026-10-30):
  F067  Human Rights Watch, 'La maquinaria represiva de Cuba' (1999), en español: resumen (cap. I),
        procesamientos políticos (cap. IV), trato a los presos políticos (cap. VI y su continuación) y
        pena de muerte (cap. VII). ONG de derechos humanos: sus datos van atribuidos ('según HRW') y sus
        valoraciones ('maquinaria represiva', 'escandaloso'...) solo como postura de HRW. Recoge también
        declaraciones de funcionarios cubanos, que van como postura del gobierno cubano.
  F068  EcuRed, 'Húber Matos': versión oficial cubana. SOLO postura.
  F069  EcuRed, 'Lucha contra Bandidos (1959-1965)': versión oficial cubana sobre los alzados del
        Escambray. SOLO postura; sus cifras (de un libro editado en Cuba) no se dan por hechos.
  F070  Wikipedia, 'Huber Matos' (guardado desde Chrome).
  F071  Wikipedia, 'Escambray rebellion' (guardado desde Chrome). Sus cifras de bajas, solo como disputadas.

Qué hace:
  1. Copia de seguridad del registro y del archivo de fragmentos.
  2. Añade F067-F071 al registro (si alguna ya existe, no toca nada).
  3. Añade los fragmentos nuevos en 'pendiente' (si alguno de los IDs ya existe, no toca nada).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_presidio.jsonl")
HOY = "2026-10-30"
P, T = "presidio_politico", "transversal"

FUENTES = [
    ("F067", "La maquinaria represiva de Cuba: los derechos humanos cuarenta años después de la revolución (1999)",
     "Human Rights Watch", "https://www.hrw.org/legacy/spanish/informes/1999/cuba.html", "ong", "revisar",
     "organismo_internacional", "ambos",
     "Archivos fuentes/docs/HRW_1999_resumen.html (cap. I), HRW_1999_procesamientos.html (cap. IV), "
     "HRW_1999_presos.html (cap. VI) y HRW_1999_pena_muerte.html (continuación del cap. VI y cap. VII). "
     "ONG de derechos humanos (se clasifica como organismo_internacional, igual que Amnistía en F022). Datos "
     "atribuidos; valoraciones ('maquinaria represiva', 'escandaloso') solo como postura de HRW. Las declaraciones "
     "de funcionarios cubanos que recoge van como postura del gobierno cubano. No se descargó cuba2.html (error 403)."),
    ("F068", "Húber Matos", "EcuRed (enciclopedia del gobierno cubano)", "https://www.ecured.cu/H%C3%BAber_Matos",
     "enciclopedia", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/ECURED_huber_matos.html. Versión oficial cubana: SOLO para documentar lo que afirma el "
     "gobierno. Lenguaje cargado ('contrarrevolucionario', 'mafia', 'terroristas') solo entre comillas y atribuido. "
     "Contradicción interna: fecha la sedición en 'octubre de 1958' en un párrafo y el 20 de octubre de 1959 en otro."),
    ("F069", "Lucha contra Bandidos (1959-1965)", "EcuRed (enciclopedia del gobierno cubano)",
     "https://www.ecured.cu/Lucha_contra_Bandidos_(1959-1965)", "enciclopedia", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/ECURED_lucha_bandidos.html. Versión oficial cubana sobre los alzados del Escambray: SOLO "
     "postura. Sus cifras vienen del libro 'Bandidismo: Derrota de la CIA en Cuba' (Etcheverry y Gutiérrez) y no "
     "se dan por hechos. 'Bandidos' es el término oficial: solo entre comillas y atribuido."),
    ("F070", "Huber Matos", "Wikipedia", "https://en.wikipedia.org/wiki/Huber_Matos", "enciclopedia", "CC-BY-SA-4.0",
     "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_huber_matos.html (guardado desde Chrome el 2026-10-30). Se apoya en The New York Times "
     "de 1959 y 1979, PBS y Bonsal. 'Regime' no entra. Da dos fechas de fundación de CID (1981 y octubre de 1980). "
     "No se usa lo del proceso judicial de su hijo (no es del tema). Algunas frases llevan 'citation needed' y no se usan."),
    ("F071", "Escambray rebellion", "Wikipedia", "https://en.wikipedia.org/wiki/Escambray_rebellion", "enciclopedia",
     "CC-BY-SA-4.0", "enciclopedia", "hechos",
     "Archivo fuentes/docs/WIKI_escambray.html (guardado desde Chrome el 2026-10-30). Cifras de bajas muy dispares y "
     "poco consistentes dentro del propio artículo: solo como cifra disputada. Fuentes de ambos lados (Encinosa, Dreke)."),
]

NUEVOS = [
    # ---------------- Human Rights Watch, 1999
    dict(id="FR-P033", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. I (resumen)",
         texto="Según Human Rights Watch, a finales de los años noventa las autoridades penitenciarias cubanas se negaban "
               "a reconocer la condición distinta de los presos políticos y los sancionaban por negarse a participar en la "
               "reeducación política, por no llevar el uniforme carcelario o por denunciar violaciones de derechos humanos "
               "en las prisiones."),
    dict(id="FR-P034", etapa=P, tipo="postura", id_fuente="F067", ubicacion="cap. VI", actor="gobierno_cubano",
         texto="Según Human Rights Watch, en junio de 1998 el ministro de Justicia de Cuba, Roberto Díaz Sotolongo, afirmó "
               "que Cuba no tenía presos políticos porque su Código Penal solo sanciona la conducta y no el pensamiento, y "
               "en julio de 1998 el portavoz del Ministerio de Relaciones Exteriores, Alejandro González, dijo que el "
               "gobierno prefería la expresión 'presos contrarrevolucionarios'."),
    dict(id="FR-P035", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. VI",
         texto="Según Human Rights Watch, el gobierno cubano no revelaba el tamaño de su población carcelaria ni permitía "
               "la observación nacional o internacional de los derechos humanos; HRW concluyó que había varios centenares "
               "de presos políticos, y a mediados de 1998 una organización no gubernamental cubana elaboró una lista de "
               "casi 400."),
    dict(id="FR-P036", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. VI",
         texto="Según Human Rights Watch, el número de presos políticos había bajado en los años noventa por una tendencia "
               "a imponer condenas más cortas, con frecuencia de 18 meses a cuatro años, frente a los diez a 20 años del "
               "pasado, aunque seguía habiendo disidentes cumpliendo condenas de diez a 20 años."),
    dict(id="FR-P037", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. I (resumen)",
         texto="Según Human Rights Watch, para su informe de 1999 entrevistó a docenas de ex presos y familiares y reunió "
               "información sobre 24 prisiones de máxima seguridad; describe malnutrición, hacinamiento, atención médica "
               "insuficiente, sesiones obligatorias de reeducación política y abusos cometidos por presos de los consejos "
               "de reclusos con la aquiescencia de los guardias."),
    dict(id="FR-P038", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. VI",
         texto="Según Human Rights Watch, en las celdas de aislamiento se aplicaban privaciones como tapar la luz y la "
               "ventilación, retirar camas o colchones, dejar la luz encendida las 24 horas o poner música a gran volumen; "
               "HRW señala que expertos en el tratamiento de sobrevivientes de la tortura consideran esas medidas métodos "
               "de tortura física o psicológica."),
    dict(id="FR-P039", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="caps. I y VI",
         texto="Según Human Rights Watch, los cuatro dirigentes del Grupo de Trabajo de la Disidencia Interna, Vladimiro "
               "Roca Antúnez, Martha Beatriz Roque Cabello, Félix Bonne Carcassés y René Gómez Manzano, fueron detenidos "
               "en julio de 1997, pasaron más de 19 meses en detención preventiva, recibieron cargos a los 15 meses y en "
               "marzo de 1999 fueron condenados por incitación a la sedición a penas de entre tres años y medio y cinco años."),
    dict(id="FR-P040", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. VI (continuación)",
         texto="Según Human Rights Watch, el gobierno cubano liberó a un centenar de presos políticos a principios de 1998, "
               "tras las peticiones del papa Juan Pablo II durante su visita de enero; la mayoría había cumplido casi toda "
               "su condena, y 17 fueron liberados a condición de exiliarse en Canadá."),
    dict(id="FR-P041", etapa=T, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. VI (continuación), 'Exilio forzado'",
         texto="Según Human Rights Watch, el gobierno cubano imponía habitualmente el exilio como condición para liberar a "
               "presos políticos; por ejemplo, en noviembre de 1998 liberó a Dessy Mendoza Rivero y a Jesús Chamber a "
               "condición de que se exiliaran en España, después de que lo pidiera el ministro español de Asuntos "
               "Exteriores, Abel Matutes."),
    dict(id="FR-P042", etapa=T, tipo="testimonio", id_fuente="F067", ubicacion="cap. VI (continuación), 'Exilio forzado'",
         testigo="Armando Alonso Romero",
         texto="Según contó a Human Rights Watch el ex preso político Armando Alonso Romero, agentes de la Seguridad del "
               "Estado en Villa Marista le obligaron a firmar documentos que decían que, si no salía de Cuba, tendría que "
               "cumplir el resto de su condena, y resumió: 'esto no es libertad, es destierro'."),
    dict(id="FR-P043", etapa=P, tipo="postura", id_fuente="F067", ubicacion="cap. VI (continuación)", actor="gobierno_cubano",
         texto="Según Human Rights Watch, en una entrevista de octubre de 1998 Fidel Castro dijo que Cuba estaba dispuesta "
               "a aceptar sugerencias y solicitudes de clemencia 'hechas con otro espíritu', pero no a colaborar con "
               "campañas organizadas, y que por la visita del Papa liberaron a presos por delitos 'de carácter "
               "contrarrevolucionario, como les llamamos nosotros' y a presos comunes, como gesto humanitario."),
    dict(id="FR-P044", etapa=P, tipo="postura", id_fuente="F067", ubicacion="cap. VI (continuación)", actor="Human Rights Watch",
         texto="Según Human Rights Watch, que Castro pusiera el acento en el 'espíritu' de las peticiones de liberación, y "
               "no en si los procesos habían sido justos, revela que la respuesta del gobierno a esas peticiones era "
               "políticamente calculada."),
    dict(id="FR-P045", etapa=P, tipo="postura", id_fuente="F067", ubicacion="cap. I (resumen)", actor="gobierno_cubano",
         texto="Según Human Rights Watch, en junio de 1998 el ministro de Justicia, Roberto Díaz Sotolongo, justificó las "
               "restricciones a la disidencia diciendo que, igual que España protege de las críticas a su rey, Cuba tenía "
               "motivos para proteger de las críticas a Fidel Castro, que cumplía una función parecida."),
    dict(id="FR-P046", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. VII",
         texto="Según Human Rights Watch, en mayo de 1995 Fidel Castro dijo a una delegación encabezada por France-Libertés "
               "que pensaba presentar un proyecto para abolir la pena de muerte; el 30 de septiembre de 1997 la delegación "
               "cubana ante la ONU informó de que, dadas las circunstancias del país, no era posible abolirla totalmente, "
               "y en marzo de 1999 Cuba la extendió a dos delitos más, el narcotráfico internacional y la corrupción de "
               "menores."),
    dict(id="FR-P047", etapa=P, tipo="hecho_atribuido", id_fuente="F067", ubicacion="cap. I (resumen)",
         texto="Según Human Rights Watch, la Ley de Protección de la Independencia Nacional y la Economía de Cuba, aprobada "
               "en febrero de 1999 y en vigor desde marzo de ese año, establecía penas de hasta 20 años de prisión por "
               "hechos que pudieran interpretarse como apoyo al embargo estadounidense, y desarrollaba una ley de diciembre "
               "de 1996 que el gobierno cubano presentó como 'una respuesta a la Ley Helms-Burton'."),
    # ---------------- EcuRed, Húber Matos (solo postura)
    dict(id="FR-P048", etapa=P, tipo="postura", id_fuente="F068", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, Huber Matos, comandante del Ejército Rebelde y jefe militar de Camagüey, se mostró inconforme "
               "con la radicalización de la revolución y empezó a acusarla de 'deslizarse' hacia el comunismo; EcuRed "
               "afirma que eso hizo que la CIA se fijara en él y que intentó frenar la reforma agraria en el territorio "
               "bajo su mando."),
    dict(id="FR-P049", etapa=P, tipo="postura", id_fuente="F068", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, en octubre de 1959 Matos escribió una carta de renuncia dirigida a Fidel Castro que se difundió "
               "entre oficiales y periodistas, y que EcuRed presenta como estímulo de una 'sedición contrarrevolucionaria'; "
               "Camilo Cienfuegos lo detuvo acusado de traición, Matos no ofreció resistencia, y fue juzgado por sedición "
               "y condenado a veinte años de prisión."),
    dict(id="FR-P050", etapa=P, tipo="postura", id_fuente="F068", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, Matos cumplió íntegra su condena, salió de prisión el 21 de octubre de 1979, pasó a Costa Rica "
               "y luego a Miami, donde fundó la organización Cuba Independiente y Democrática, a la que EcuRed atribuye "
               "'acciones terroristas' contra Cuba; murió en Miami el 27 de febrero de 2014."),
    dict(id="FR-P051", etapa=P, tipo="postura", id_fuente="F068", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, Matos fue un 'contrarrevolucionario' y uno de los más 'extremistas' del exilio, que apoyó la "
               "Ley Helms-Burton y el embargo de Estados Unidos y defendió una confrontación directa para acabar con la "
               "revolución."),
    # ---------------- EcuRed, Lucha contra Bandidos (solo postura)
    dict(id="FR-P052", etapa=P, tipo="postura", id_fuente="F069", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, la llamada Lucha contra Bandidos (1959-1965) fue la respuesta de las Fuerzas Armadas "
               "Revolucionarias, el Ministerio del Interior y las milicias a 'bandas armadas por la CIA', y tuvo su mayor "
               "fuerza en la región del Escambray."),
    dict(id="FR-P053", etapa=P, tipo="postura", id_fuente="F069", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, los primeros grupos alzados, en 1959, estaban formados sobre todo por antiguos miembros de los "
               "cuerpos represivos de Batista que huían de los tribunales, y en una segunda etapa, de abril de 1961 a julio "
               "de 1965, sus jefes eran sobre todo antiguos miembros del Ejército Rebelde descontentos."),
    dict(id="FR-P054", etapa=P, tipo="postura", id_fuente="F069", ubicacion="texto, 'El balance final'", actor="gobierno_cubano",
         texto="Según EcuRed, que cita el libro 'Bandidismo: Derrota de la CIA en Cuba', de Etcheverry y Gutiérrez, hubo "
               "cerca de 290 grupos alzados con unos 4.190 integrantes y 9.250 colaboradores; las fuerzas del gobierno "
               "tuvieron unas 590 bajas y en la lucha participaron más de 100.000 milicianos y militares."),
    dict(id="FR-P055", etapa=P, tipo="postura", id_fuente="F069", ubicacion="texto, 'Crímenes cometidos por las bandas'",
         actor="gobierno_cubano",
         texto="Según EcuRed, citando el mismo libro, los alzados mataron a 214 personas, entre ellas 63 campesinos y "
               "trabajadores agrícolas, 13 niños y 9 maestros voluntarios y brigadistas de la campaña de alfabetización, "
               "como el brigadista Manuel Ascunce Domenech y el campesino Pedro Lantigua en noviembre de 1961, después de "
               "lo cual el gobierno dictó la Ley 988."),
    dict(id="FR-P056", etapa=P, tipo="postura", id_fuente="F069", ubicacion="texto", actor="gobierno_cubano",
         texto="Según EcuRed, el último alzado, José 'Pepe' Rebozo, fue capturado el 1 de octubre de 1966; Fidel Castro "
               "decidió no fusilarlo sino condenarlo a 30 años, y fue liberado y enviado a Estados Unidos a mediados de los "
               "años setenta."),
    # ---------------- Wikipedia, Huber Matos
    dict(id="FR-P057", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Early life' y 'Revolutionary activity'",
         texto="Según Wikipedia, Huber Matos (1918-2014), maestro en Manzanillo, se opuso a Batista desde el golpe de 1952 y "
               "desde Costa Rica ayudó a los rebeldes de la Sierra Maestra; el 31 de marzo de 1958 llevó en avión un "
               "cargamento de armas y municiones, Castro le dio el mando de la columna 9 y el 11 de enero de 1959 fue "
               "nombrado jefe del ejército en la provincia de Camagüey."),
    dict(id="FR-P058", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Split with Castro'",
         texto="Según Wikipedia, en julio de 1959 Matos dio discursos anticomunistas en Camagüey, y el 19 de octubre envió a "
               "Castro una segunda carta de renuncia, después de haber escrito que la influencia comunista en el gobierno "
               "seguía creciendo; dos días después Camilo Cienfuegos lo arrestó junto con sus ayudantes militares."),
    dict(id="FR-P059", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Sentencing and imprisonment'",
         texto="Según Wikipedia, el mismo día del arresto Pedro Luis Díaz Lanz lanzó octavillas sobre La Habana; Castro "
               "convocó un mitin para pedir tribunales revolucionarios contra Matos y Díaz Lanz y, según The New York "
               "Times, cuando preguntó si Matos debía ser fusilado casi todos levantaron la mano y la multitud pidió el "
               "fusilamiento."),
    dict(id="FR-P060", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Sentencing and imprisonment'",
         texto="Según Wikipedia, en el juicio de diciembre de 1959, junto a cinco capitanes y once tenientes, Matos declaró "
               "que había hablado con oficiales anticomunistas sobre el nombramiento de comunistas pero que no había "
               "conspirado; Raúl Castro dijo que agitaba 'el fantasma del comunismo' y Fidel Castro, en un discurso de siete "
               "horas, lo acusó de favorecer indirectamente a Estados Unidos, a los latifundistas y a los partidarios de "
               "Batista; la fiscalía pidió la pena de muerte y el 15 de diciembre fue condenado a veinte años por actividad "
               "contrarrevolucionaria."),
    dict(id="FR-P061", etapa=P, tipo="testimonio", id_fuente="F070", ubicacion="'Sentencing and imprisonment'",
         testigo="Huber Matos",
         texto="Según contó Huber Matos, citado por Wikipedia, salió vivo de la cárcel por la voluntad de Dios: hizo huelgas "
               "de hambre, pasó en total dieciséis años en régimen de aislamiento, le repetían que moriría preso y fue "
               "torturado en varias ocasiones."),
    dict(id="FR-P062", etapa=P, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Sentencing and imprisonment' y 'Life after prison'",
         texto="Según Wikipedia, Matos cumplió los primeros seis años y medio de su condena en la prisión de Isla de Pinos y el "
               "resto en La Cabaña; salió en 1979, a los sesenta años, se reunió en Costa Rica con su esposa y sus hijos, "
               "que habían salido de Cuba en los años sesenta, y después se instaló en Miami, donde murió en febrero de 2014."),
    dict(id="FR-P063", etapa=T, tipo="hecho_atribuido", id_fuente="F070", ubicacion="'Life after prison'",
         texto="Según Wikipedia, Matos fundó en el exilio Cuba Independiente y Democrática (CID), que operaba emisoras de radio "
               "con noticias sin censura dirigidas a Cuba, convencido de que el cambio vendría desde dentro de la isla; el "
               "artículo da dos fechas de fundación, 1981 y octubre de 1980 en Venezuela. Escribió sus memorias, 'Cómo llegó "
               "la noche'."),
    dict(id="FR-P064", etapa=P, tipo="postura", id_fuente="F070", ubicacion="'Sentencing and imprisonment'", actor="Philip Bonsal",
         texto="Según Wikipedia, el embajador de Estados Unidos en Cuba, Philip Bonsal, consideró que Castro usó el vuelo de "
               "Díaz Lanz para provocar una reacción de masas y dejar de lado las cuestiones que planteaba la renuncia de Matos."),
    # ---------------- Wikipedia, rebelión del Escambray
    dict(id="FR-P065", etapa=P, tipo="hecho_atribuido", id_fuente="F071", ubicacion="introducción",
         texto="Según Wikipedia, la rebelión del Escambray (1959-1965) fue un conflicto armado en el que varios grupos "
               "insurgentes lucharon contra el gobierno de Fidel Castro, que llamó a su operación Lucha contra Bandidos; los "
               "rebeldes eran una mezcla de antiguos soldados de Batista, campesinos de la zona y antiguos guerrilleros que "
               "habían luchado junto a Castro, y en 1965 todos habían sido eliminados."),
    dict(id="FR-P066", etapa=P, tipo="hecho_atribuido", id_fuente="F071", ubicacion="'Beginning' e 'Insurgency'",
         texto="Según Wikipedia, entre los jefes de la rebelión estaban Osvaldo Ramírez y el estadounidense William Alexander "
               "Morgan, que habían combatido a Batista en esa misma zona; pequeños campesinos contrarios a la colectivización "
               "tuvieron un papel central, y la CIA y el gobierno de Eisenhower apoyaron la rebelión en secreto, aunque la CIA "
               "retiró su apoyo tras Bahía de Cochinos. Morgan fue detenido y fusilado en 1961 tras un juicio militar."),
    dict(id="FR-P067", etapa=P, tipo="cifra_disputada", id_fuente="F071", ubicacion="ficha y 'Legacy'", corroborado_por=["F069"],
         texto="Las cifras del Escambray varían mucho según la fuente: Wikipedia da entre 2.000 y 3.995 insurgentes y más de "
               "6.000 colaboradores, de 2.000 a 3.000 rebeldes muertos y 5.000 capturados, y del lado del gobierno 500 "
               "militares y 3.500 milicianos muertos; recoge que Raúl Castro habló en 1970 de 500 militares muertos y que "
               "las estimaciones del total de muertos van de 1.000 a 7.000. EcuRed habla de unos 4.190 alzados, 9.250 "
               "colaboradores y unas 590 bajas del gobierno."),
    dict(id="FR-P068", etapa=P, tipo="hecho_atribuido", id_fuente="F071", ubicacion="'Insurgency', 'Defeat' y 'Legacy'",
         texto="Según Wikipedia, el gobierno desplegó miles de soldados, a veces hasta 250.000 hombres, casi todos milicianos, "
               "en cercos cada vez más estrechos; algunos insurgentes que se rindieron fueron fusilados de inmediato y solo "
               "unos pocos lograron escapar; la Lucha contra Bandidos duró más y movilizó más soldados que la guerra contra "
               "Batista."),
]

for p in (REG, FRAG):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
if any(fu[0] in {r["id_fuente"] for r in filas} for fu in FUENTES):
    print("Alguna de las fuentes F067-F071 ya está en el registro. No toco nada.")
    sys.exit(0)

with FRAG.open(encoding="utf-8-sig") as f:
    lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n["id"] for n in NUEVOS if n["id"] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(REG, REG.with_name(f"{REG.name}.{marca}.bak"))
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
        d = {"id": n["id"], "etapa": n["etapa"], "tipo": n["tipo"], "id_fuente": n["id_fuente"],
             "ubicacion": n["ubicacion"], "corroborado_por": n.get("corroborado_por", []), "texto": n["texto"],
             "notas": "", "revisado": False, "estado": "pendiente"}
        if n.get("actor"):
            d["actor"] = n["actor"]
        if n.get("testigo"):
            d["testigo"] = n["testigo"]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas {len(FUENTES)} fuentes (F067 a F071).")
print(f"Añadidos {len(NUEVOS)} fragmentos nuevos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
