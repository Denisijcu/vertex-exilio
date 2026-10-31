"""
generar_lote2_presidio.py — Segundo lote de ejemplos del presidio político (y alguno transversal).

Uso (desde E:\\vertex-exilio):
    python generar_lote2_presidio.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_presidio.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_presidio_lote2.jsonl con todos los ejemplos en estado 'pendiente'.

Usa los fragmentos nuevos FR-P033 a FR-P068: Human Rights Watch (1999), EcuRed (Húber Matos y Lucha
contra Bandidos) y Wikipedia (Huber Matos y la rebelión del Escambray). En Matos y en el Escambray cada
ejemplo lleva las dos versiones; las cifras de EcuRed solo aparecen cuando también las recoge Wikipedia.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_presidio.jsonl")
DESTINO = Path("datos/borrador_presidio_lote2.jsonl")
PREFIJO = "exi-p"
PRIMER_ID = 14

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

P, T = "presidio_politico", "transversal"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(P, "contexto", [("¿Había presos políticos en Cuba a finales de los años noventa?", """Depende de a quién se le pregunte, y las dos posiciones están documentadas.

El gobierno cubano sostenía que no. Según Human Rights Watch, en junio de 1998 el ministro de Justicia, Roberto Díaz Sotolongo, afirmó que Cuba no tenía presos políticos porque su Código Penal solo sanciona la conducta y no el pensamiento. En julio de 1998 el portavoz del Ministerio de Relaciones Exteriores, Alejandro González, dijo que el gobierno prefería la expresión 'presos contrarrevolucionarios'.

Human Rights Watch, una organización de derechos humanos, llegó a otra conclusión. Según su informe, el gobierno no revelaba el tamaño de su población carcelaria ni permitía la observación de los derechos humanos, pero HRW concluyó que había varios centenares de presos políticos, y a mediados de 1998 una organización no gubernamental cubana elaboró una lista de casi 400.

Según el mismo informe, el número había bajado en los años noventa por una tendencia a condenas más cortas, con frecuencia de 18 meses a cuatro años, frente a los diez a 20 años del pasado, aunque seguía habiendo disidentes cumpliendo condenas largas.

La diferencia no es solo de cifras, también de palabras: lo que para HRW eran presos políticos, el gobierno prefería llamarlos «presos contrarrevolucionarios». Como el gobierno no publicaba datos, no hay una cifra oficial con la que comparar.""")],
 ["FR-P034", "FR-P035", "FR-P036"]),

(P, "hecho", [("¿Cómo eran las condiciones de los presos políticos en Cuba en los años noventa?", """La fuente más detallada que tenemos para esa época es el informe de Human Rights Watch de 1999, y lo que describe va siempre atribuido a esa organización.

Según HRW, para su informe entrevistó a docenas de ex presos y familiares y reunió información sobre 24 prisiones de máxima seguridad. Describe malnutrición, hacinamiento, atención médica insuficiente, sesiones obligatorias de reeducación política y abusos cometidos por presos de los consejos de reclusos con la aquiescencia de los guardias.

Los presos políticos tenían además problemas propios. Según HRW, las autoridades penitenciarias se negaban a reconocer su condición distinta y los sancionaban por negarse a participar en la reeducación política, por no llevar el uniforme carcelario o por denunciar violaciones de derechos humanos en las prisiones.

Las celdas de aislamiento eran uno de los castigos. Según HRW, en ellas se aplicaban privaciones como tapar la luz y la ventilación, retirar camas o colchones, dejar la luz encendida las 24 horas o poner música a gran volumen, y señala que expertos en el tratamiento de sobrevivientes de la tortura consideran esas medidas métodos de tortura física o psicológica.

El gobierno cubano no permitía la observación independiente de las cárceles, así que no tenemos una versión oficial que responda punto por punto a estas descripciones. Lo que sí está documentado es que sus funcionarios negaban que hubiera presos políticos.""")],
 ["FR-P037", "FR-P033", "FR-P038", "FR-P035", "FR-P034"]),

(P, "reformulacion", [("Leí que los plantados se acabaron en 1991 con la salida de Mario Chanes. ¿Ya no hubo más presos que se negaran a la reeducación?", """Es cierto que Mario Chanes de Armas fue el último de los plantados históricos en salir de la cárcel, pero eso no quiere decir que se acabaran los presos que se negaban a cooperar.

Mario Chanes de Armas cumplió 30 años de prisión y fue el último plantado en salir, en 1991. Se llamó plantados a los presos políticos cubanos que se negaron a cooperar con el sistema penitenciario: rechazaban el trabajo forzado, los programas de reeducación política y el uniforme de preso común.

Pero esa forma de resistencia siguió existiendo después. Según Human Rights Watch, a finales de los años noventa las autoridades penitenciarias cubanas se negaban a reconocer la condición distinta de los presos políticos y los sancionaban por negarse a participar en la reeducación política, por no llevar el uniforme carcelario o por denunciar violaciones de derechos humanos en las prisiones.

Es decir, las mismas negativas que definían a los plantados de los años sesenta y setenta seguían costando castigos a otros presos políticos treinta años después.

La diferencia es de escala y de nombre. Los plantados históricos fueron un grupo que se conoce con ese nombre; los presos de los años noventa que describe HRW no aparecen en nuestras fuentes agrupados así, aunque hicieran cosas parecidas.""")],
 ["FR-P004", "FR-P001", "FR-P033"]),

(P, "hecho", [("¿Qué pasó con los líderes del Grupo de Trabajo de la Disidencia Interna?", """Es uno de los casos que documenta el informe de Human Rights Watch de 1999 sobre Cuba.

Según HRW, los cuatro dirigentes del Grupo de Trabajo de la Disidencia Interna, Vladimiro Roca Antúnez, Martha Beatriz Roque Cabello, Félix Bonne Carcassés y René Gómez Manzano, fueron detenidos en julio de 1997. Pasaron más de 19 meses en detención preventiva, recibieron cargos a los 15 meses, y en marzo de 1999 fueron condenados por incitación a la sedición a penas de entre tres años y medio y cinco años.

El caso coincidió con la visita del papa Juan Pablo II a Cuba en enero de 1998. Según HRW, el gobierno liberó a un centenar de presos políticos a principios de ese año tras las peticiones del Papa; la mayoría había cumplido casi toda su condena, y 17 fueron liberados a condición de exiliarse en Canadá. Los cuatro dirigentes siguieron presos y fueron juzgados un año después.

La posición del gobierno cubano en esos años era que no había presos políticos. Según HRW, en junio de 1998 el ministro de Justicia, Roberto Díaz Sotolongo, afirmó que Cuba no tenía presos políticos porque su Código Penal solo sanciona la conducta y no el pensamiento.

Nuestras fuentes no incluyen la sentencia ni una explicación oficial del caso concreto; para eso harían falta documentos del propio proceso.""")],
 ["FR-P039", "FR-P040", "FR-P034"]),

(T, "contexto", [("¿Es verdad que a algunos presos políticos cubanos los soltaban con la condición de irse del país?", """Sí, está documentado, y es una de las formas en que presidio político y exilio se cruzan.

Según Human Rights Watch, el gobierno cubano imponía habitualmente el exilio como condición para liberar a presos políticos. Por ejemplo, en noviembre de 1998 liberó a Dessy Mendoza Rivero y a Jesús Chamber a condición de que se exiliaran en España, después de que lo pidiera el ministro español de Asuntos Exteriores, Abel Matutes. Ese mismo año, según HRW, de los presos liberados tras las peticiones del papa Juan Pablo II, 17 salieron a condición de exiliarse en Canadá.

Algunos lo vivieron como un destierro. Según contó a HRW el ex preso político Armando Alonso Romero, agentes de la Seguridad del Estado le obligaron a firmar documentos que decían que, si no salía de Cuba, tendría que cumplir el resto de su condena, y resumió: 'esto no es libertad, es destierro'.

El gobierno cubano lo explicaba de otra manera. Según HRW, en una entrevista de octubre de 1998 Fidel Castro dijo que Cuba estaba dispuesta a aceptar solicitudes de clemencia 'hechas con otro espíritu', pero no a colaborar con campañas organizadas, y presentó las liberaciones por la visita del Papa como un gesto humanitario.

HRW lo interpreta de forma crítica: según la organización, que Castro pusiera el acento en el 'espíritu' de las peticiones, y no en si los procesos habían sido justos, revela que la respuesta del gobierno era políticamente calculada.""")],
 ["FR-P041", "FR-P040", "FR-P042", "FR-P043", "FR-P044"]),

(P, "perspectivas", [("¿Quién fue Huber Matos?", """Huber Matos es una figura que se cuenta de forma muy distinta en La Habana y en el exilio.

Según Wikipedia, Huber Matos (1918-2014) fue maestro en Manzanillo, se opuso a Batista desde el golpe de 1952 y desde Costa Rica ayudó a los rebeldes de la Sierra Maestra. El 31 de marzo de 1958 llevó en avión un cargamento de armas y municiones, Castro le dio el mando de la columna 9, y el 11 de enero de 1959 fue nombrado jefe del ejército en la provincia de Camagüey.

Pocos meses después rompió con Castro. Según Wikipedia, en julio de 1959 dio discursos anticomunistas en Camagüey, y el 19 de octubre envió a Castro una segunda carta de renuncia; dos días después Camilo Cienfuegos lo arrestó. En diciembre fue condenado a veinte años por actividad contrarrevolucionaria. Salió de la cárcel en 1979 y se instaló en Miami, donde murió en 2014.

La versión del gobierno cubano es muy distinta. Según EcuRed, su enciclopedia oficial, Matos se mostró inconforme con la radicalización de la revolución, empezó a acusarla de 'deslizarse' hacia el comunismo, la CIA se fijó en él e intentó frenar la reforma agraria. EcuRed lo llama 'contrarrevolucionario' y uno de los más 'extremistas' del exilio, que apoyó la Ley Helms-Burton y el embargo de Estados Unidos.

Los hechos básicos coinciden: fue comandante rebelde, rompió con Castro en 1959 y pasó veinte años preso. Lo que cambia es la lectura: para unos, un revolucionario que denunció el giro al comunismo; para el gobierno cubano, alguien que buscó una «sedición contrarrevolucionaria».""")],
 ["FR-P057", "FR-P058", "FR-P060", "FR-P062", "FR-P048", "FR-P051", "FR-P049"]),

(P, "perspectivas", [("¿Por qué condenaron a Huber Matos en 1959?", """El caso de Huber Matos tiene dos versiones enfrentadas, y además una tercera mirada desde la embajada de Estados Unidos.

Según Wikipedia, en julio de 1959 Matos dio discursos anticomunistas en Camagüey, y el 19 de octubre envió a Castro una segunda carta de renuncia, después de haber escrito que la influencia comunista en el gobierno seguía creciendo. Dos días después Camilo Cienfuegos lo arrestó junto con sus ayudantes militares.

En el juicio de diciembre de 1959, junto a cinco capitanes y once tenientes, Matos declaró que había hablado con oficiales anticomunistas sobre el nombramiento de comunistas pero que no había conspirado. Raúl Castro dijo que agitaba 'el fantasma del comunismo' y Fidel Castro, en un discurso de siete horas, lo acusó de favorecer indirectamente a Estados Unidos, a los latifundistas y a los partidarios de Batista. La fiscalía pidió la pena de muerte y el 15 de diciembre fue condenado a veinte años por actividad contrarrevolucionaria.

La versión del gobierno cubano, según EcuRed, es que su carta de renuncia se difundió entre oficiales y periodistas para estimular una 'sedición contrarrevolucionaria', y que fue juzgado por sedición.

Hubo además un contexto que pesó. Según Wikipedia, el mismo día del arresto Pedro Luis Díaz Lanz lanzó octavillas sobre La Habana, y en un mitin posterior la multitud pidió el fusilamiento de Matos. El embajador de Estados Unidos en Cuba, Philip Bonsal, consideró que Castro usó ese vuelo para provocar una reacción de masas y dejar de lado las cuestiones que planteaba la renuncia de Matos.""")],
 ["FR-P058", "FR-P060", "FR-P049", "FR-P059", "FR-P064"]),

(P, "humano", [("Mi abuelo estuvo preso en La Cabaña y siempre hablaba de Huber Matos. ¿Cómo fue su tiempo en la cárcel?", """Puede que tu abuelo coincidiera con él, porque Matos pasó buena parte de su condena precisamente en La Cabaña.

Según Wikipedia, Matos cumplió los primeros seis años y medio de su condena de veinte años en la prisión de Isla de Pinos y el resto en La Cabaña. Salió en 1979, a los sesenta años, se reunió en Costa Rica con su esposa y sus hijos, que habían salido de Cuba en los años sesenta, y después se instaló en Miami, donde murió en febrero de 2014.

Él mismo contó cómo fueron esos años. Según contó Huber Matos, citado por Wikipedia, salió vivo de la cárcel por la voluntad de Dios: hizo huelgas de hambre, pasó en total dieciséis años en régimen de aislamiento, le repetían que moriría preso y fue torturado en varias ocasiones. Es su testimonio; el gobierno cubano no ha respondido a esas acusaciones en las fuentes que tenemos.

Después de la cárcel siguió activo. Según Wikipedia, fundó en el exilio Cuba Independiente y Democrática, que operaba emisoras de radio con noticias dirigidas a Cuba, y escribió sus memorias, 'Cómo llegó la noche'. La versión oficial cubana, según EcuRed, atribuye a esa organización 'acciones terroristas' contra Cuba.

Si tu abuelo dejó cartas o recuerdos de esos años, o si alguien de la familia recuerda lo que contaba de La Cabaña, esa memoria tiene mucho valor. Las memorias de Matos pueden ayudar a ponerla en contexto.""")],
 ["FR-P062", "FR-P061", "FR-P063", "FR-P050"]),

(P, "perspectivas", [("¿Qué fue la rebelión del Escambray?", """Fue un conflicto armado en las montañas del Escambray entre 1959 y 1965, y hasta el nombre depende de quién lo cuente.

Según Wikipedia, fue un conflicto en el que varios grupos insurgentes lucharon contra el gobierno de Fidel Castro, que llamó a su operación Lucha contra Bandidos. Los rebeldes eran una mezcla de antiguos soldados de Batista, campesinos de la zona y antiguos guerrilleros que habían luchado junto a Castro, y en 1965 todos habían sido eliminados.

Según la misma fuente, entre sus jefes estaban Osvaldo Ramírez y el estadounidense William Alexander Morgan, que habían combatido a Batista en esa misma zona. Pequeños campesinos contrarios a la colectivización tuvieron un papel central, y la CIA y el gobierno de Estados Unidos, entonces presidido por Eisenhower, apoyaron la rebelión en secreto, aunque la CIA retiró su apoyo tras Bahía de Cochinos.

La versión del gobierno cubano, recogida por EcuRed, su enciclopedia oficial, es que la Lucha contra Bandidos fue la respuesta de las Fuerzas Armadas Revolucionarias, el Ministerio del Interior y las milicias a 'bandas armadas por la CIA'. Según EcuRed, los primeros grupos estaban formados sobre todo por antiguos miembros de los cuerpos represivos de Batista que huían de los tribunales, y en una segunda etapa sus jefes eran sobre todo antiguos miembros del Ejército Rebelde descontentos.

Las dos versiones coinciden en que hubo apoyo de la CIA y en que entre los alzados había ex rebeldes y gente de Batista. Difieren en el peso que dan a los campesinos y en cómo los llaman: insurgentes para unos, 'bandidos' para el gobierno.""")],
 ["FR-P065", "FR-P066", "FR-P052", "FR-P053"]),

(P, "reformulacion", [("¿Cuánta gente murió en la guerra del Escambray? He visto cifras muy distintas.", """Es normal, porque las cifras del Escambray varían mucho y ninguna fuente que tengamos da un recuento que se pueda dar por definitivo.

Wikipedia da entre 2.000 y 3.995 insurgentes y más de 6.000 colaboradores, de 2.000 a 3.000 rebeldes muertos y 5.000 capturados, y del lado del gobierno 500 militares y 3.500 milicianos muertos. Recoge también que Raúl Castro habló en 1970 de 500 militares muertos, y que las estimaciones del total de muertos van de 1.000 a 7.000. Esas cifras no encajan del todo entre sí dentro del propio artículo.

La versión del gobierno cubano, recogida por EcuRed, habla de unos 4.190 alzados, 9.250 colaboradores y unas 590 bajas del gobierno. EcuRed atribuye además a los alzados la muerte de campesinos, niños y maestros y brigadistas de la campaña de alfabetización, como el brigadista Manuel Ascunce Domenech y el campesino Pedro Lantigua, y da sus propias cifras de víctimas, que no tenemos otra fuente que confirme.

Lo que sí se ve es que la diferencia más grande está en las bajas del gobierno: unas 590 según EcuRed, 500 militares según Raúl Castro, y 500 militares más 3.500 milicianos según Wikipedia. Puede depender de si se cuenta o no a los milicianos, pero las fuentes no lo aclaran.

Así que lo honesto es dar cada cifra con su fuente y decir que el número real de muertos, de ambos lados y de civiles, no se conoce con certeza.""")],
 ["FR-P067", "FR-P054", "FR-P055"]),

(P, "hecho", [("¿Qué pasaba con los alzados del Escambray que capturaban?", """La guerra del Escambray también llenó cárceles, y las fuentes recogen varios destinos posibles para los alzados capturados.

Según Wikipedia, de 2.000 a 3.000 rebeldes murieron y 5.000 fueron capturados. El gobierno desplegó miles de soldados, a veces hasta 250.000 hombres, casi todos milicianos, en cercos cada vez más estrechos; según la misma fuente, algunos insurgentes que se rindieron fueron fusilados de inmediato y solo unos pocos lograron escapar.

Uno de los jefes, el estadounidense William Alexander Morgan, fue detenido y fusilado en 1961 tras un juicio militar.

No todos terminaron así. Según EcuRed, la enciclopedia oficial cubana, el último alzado, José 'Pepe' Rebozo, fue capturado cuando la lucha ya terminaba; Fidel Castro decidió no fusilarlo sino condenarlo a una larga pena de cárcel, y años después fue liberado y enviado a Estados Unidos. Es un caso que une el Escambray con el presidio político y con el exilio.

Las fuentes que tenemos no dicen cuántos de los capturados fueron fusilados, cuántos condenados a prisión ni cuántos años cumplieron. Tampoco permiten saber cuántos de ellos acabaron entre los presos políticos de las décadas siguientes.""")],
 ["FR-P067", "FR-P068", "FR-P066", "FR-P056"]),

(P, "contexto", [("¿Qué leyes usaba Cuba contra los opositores a finales de los noventa?", """Según el informe de Human Rights Watch de 1999, el marco legal era una de las claves de la represión de la disidencia, y el gobierno cubano lo justificaba de otra manera.

Según HRW, la Ley de Protección de la Independencia Nacional y la Economía de Cuba, aprobada en febrero de 1999 y en vigor desde marzo de ese año, establecía penas de hasta 20 años de prisión por hechos que pudieran interpretarse como apoyo al embargo estadounidense. Desarrollaba una ley de diciembre de 1996 que el gobierno cubano presentó como 'una respuesta a la Ley Helms-Burton'.

La pena de muerte también se amplió. Según HRW, en mayo de 1995 Fidel Castro dijo a una delegación encabezada por France-Libertés que pensaba presentar un proyecto para abolirla; el 30 de septiembre de 1997 la delegación cubana ante la ONU informó de que, dadas las circunstancias del país, no era posible abolirla totalmente, y en marzo de 1999 Cuba la extendió a dos delitos más, el narcotráfico internacional y la corrupción de menores.

El gobierno defendía esas restricciones. Según HRW, en junio de 1998 el ministro de Justicia, Roberto Díaz Sotolongo, las justificó diciendo que, igual que España protege de las críticas a su rey, Cuba tenía motivos para proteger de las críticas a Fidel Castro, que cumplía una función parecida. El mismo ministro afirmó que Cuba no tenía presos políticos porque su Código Penal solo sanciona la conducta y no el pensamiento.

El gobierno presentó la ley de 1996 como una respuesta a la Ley Helms-Burton; HRW la incluye en su informe como parte del marco legal usado contra la disidencia.""")],
 ["FR-P047", "FR-P046", "FR-P045", "FR-P034"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "presidio lote 2"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
