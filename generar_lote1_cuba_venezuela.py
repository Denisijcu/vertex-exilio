"""
generar_lote1_cuba_venezuela.py — Primer lote de ejemplos de la etapa cuba_venezuela (módulo "Cuba: contexto"):
Fidel y Chávez, petróleo por profesionales, los médicos de Barrio Adentro, los acuerdos militares y la DGCIM, las
negativas oficiales, los 32 muertos de enero de 2026 y el fin del petróleo venezolano.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_cuba_venezuela.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_cuba_venezuela.jsonl y se niega a usar fragmentos que
no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_cuba_venezuela_lote1.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_cuba_venezuela.jsonl")
DESTINO = Path("datos/borrador_cuba_venezuela_lote1.jsonl")
PREFIJO = "exi-cv"
PRIMER_ID = 1
NOTA = "cuba_venezuela lote 1"

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "cuba_venezuela"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "hecho", [("¿Cómo empezó la relación entre Fidel Castro y Hugo Chávez?", """Empezó en 1994, antes de que Chávez fuera presidente, y se convirtió en una de las alianzas políticas más estrechas de América Latina.

Según una investigación de Reuters de 2019, en 1994, meses después de salir de prisión por un indulto presidencial, Hugo Chávez viajó a La Habana, donde Fidel Castro lo recibió en el aeropuerto en su primer encuentro en persona. En un discurso en la Universidad de La Habana, Chávez llamó a Cuba «un bastión de la dignidad latinoamericana».

La versión oficial lo cuenta con más emoción. Según la emisora estatal cubana Radio Rebelde, Nicolás Maduro recordó treinta años después que Chávez fue recibido por Fidel Castro «con honores de jefe de Estado» y habló del inicio de una historia de «unidad, solidaridad y liberación».

Según Reuters, Castro fue mentor de Chávez antes de que llegara a la presidencia y vio en el petróleo venezolano un posible alimento para una economía cubana golpeada por el fin de la URSS. Tras la elección de Chávez en 1998, los vínculos con Cuba se estrecharon.

La relación personal era muy cercana. Según la periodista Alma Guillermoprieto, Chávez le escribió a Fidel Castro que no sabía si llamarlo «hermano o padre», y los dos hablaban constantemente por teléfono. Según Reuters, Chávez se operó cuatro veces en Cuba antes de morir en 2013, y Fidel Castro lo llamó «el mejor amigo que tuvo el pueblo cubano en su historia».

Es decir, la alianza fue a la vez personal, política y económica, y siguió con Maduro después de la muerte de Chávez.""")],
 ["FR-VZ001", "FR-VZ002", "FR-VZ003", "FR-VZ004", "FR-VZ016"]),

(T, "hecho", [("¿Qué era el acuerdo de petróleo por médicos entre Cuba y Venezuela?", """Era el centro económico de la alianza: Venezuela mandaba petróleo y Cuba mandaba profesionales, sobre todo personal de salud.

Según el Servicio de Investigación del Congreso de EE. UU., en 2000 los dos países firmaron un acuerdo petrolero preferencial, en esencia un trueque de petróleo por personal médico, que dio a Cuba entre 90.000 y 100.000 barriles diarios, cerca de dos tercios de su consumo.

La periodista Alma Guillermoprieto lo describía así en 2005: desde octubre de 2000 Cuba recibía petróleo venezolano a precio de mercado pero con un crédito muy fácil, 90.000 barriles diarios en 2005, y desde 2001 Venezuela pagaba además en efectivo bienes y servicios cubanos, desde casas prefabricadas hasta entrenadores deportivos.

El intercambio creció en 2003. Según Guillermoprieto, cuando Chávez estaba en serios problemas políticos, Fidel Castro aceptó enviarle cerca de 30.000 internacionalistas, entre médicos, enfermeros, entrenadores, maestros y alfabetizadores. La Misión Barrio Adentro llevó atención médica a casi todos los barrios pobres del país.

En dinero, la escala era enorme. Según el economista Carmelo Mesa-Lago, la ayuda de Venezuela a Cuba se estimó en 9.405 millones de dólares en 2008, más que en cualquier año de la relación con la URSS: 5.650 millones por los servicios de 40.000 profesionales cubanos, 97.000 barriles diarios de crudo y derivados con un subsidio de precios de 2.400 millones, e inversiones en 76 proyectos.

En resumen, fue un trueque que le daba a Cuba la mayor parte de su petróleo y a Chávez miles de profesionales para sus programas sociales.""")],
 ["FR-VZ006", "FR-VZ005", "FR-VZ007", "FR-VZ011"]),

(T, "humano", [("Mi prima fue médica en Barrio Adentro en Venezuela. Ella dice que la gente allá los quería mucho, pero que la pasó mal lejos de su familia. ¿Era así para todos?", """Lo que cuenta tu prima coincide con lo que se ha publicado sobre esas misiones, aunque cada experiencia fue distinta.

Sobre el cariño de la gente: según la periodista Alma Guillermoprieto, que escribió sobre Venezuela en 2005, en los barrios había consenso en que los médicos cubanos eran trabajadores y competentes, y eran «muy queridos». La Misión Barrio Adentro llevó atención médica a casi todos los barrios pobres del país.

Sobre la distancia y las condiciones: Guillermoprieto recoge el relato de una cubana que vivía en Venezuela y tenía dos primos médicos. Según ella, los médicos dejaban a su familia en Cuba y no podían visitarla en los dos o tres años de contrato, y recibían 200 dólares al mes del gobierno venezolano más 100 dólares depositados en una cuenta en Cuba, cuando en Cuba un médico ganaba unos 15 dólares al mes. Es el testimonio de una persona, de 2005, y las condiciones pudieron cambiar después.

La escala fue grande: según la misma periodista, en 2003 Fidel Castro aceptó enviar a Venezuela cerca de 30.000 internacionalistas, entre médicos, enfermeros, maestros y otros profesionales.

Así que tu prima no está sola: muchos médicos vivieron a la vez el agradecimiento de los pacientes y el costo de estar lejos de los suyos. Su testimonio es valioso: según Guillermoprieto, los médicos evitaban hablar con la prensa.""")],
 ["FR-VZ009", "FR-VZ008", "FR-VZ007"]),

(T, "perspectivas", [("¿Quién salía ganando con la alianza entre Cuba y Venezuela?", """Las dos partes sacaban algo, y lo que se discute es quién dependía más de quién.

Lo que recibía Cuba: según el economista Carmelo Mesa-Lago, la ayuda de Venezuela se estimó en 9.405 millones de dólares en 2008, más que en cualquier año de la relación con la URSS, incluidos 5.650 millones por los servicios de 40.000 profesionales cubanos y 97.000 barriles diarios de crudo y derivados, el 65 % de la demanda cubana. Mesa-Lago advertía que la dependencia era muy fuerte y que, si la ayuda terminaba o se reducía mucho, Cuba podría enfrentar un segundo «Período Especial».

Lo que recibía el chavismo, según algunos analistas: el historiador Alejandro Velasco, de la Universidad de Nueva York, considera que la influencia cubana fue «absolutamente esencial» para la supervivencia del gobierno chavista. La periodista Alma Guillermoprieto escribía en 2005 que el petróleo venezolano ayudaba a Fidel Castro a mantenerse en el poder, y que los cubanos le ahorraban a Chávez trabajar con instituciones que no fueran las suyas.

La posición de Estados Unidos y la de La Habana chocan. Según Reuters, en enero de 2026 Trump escribió que Cuba vivió durante años de grandes cantidades de petróleo y dinero de Venezuela; el canciller del gobierno cubano, Bruno Rodríguez, negó que Cuba hubiera recibido compensación por servicios de seguridad prestados a cualquier país.

En resumen, Cuba ganaba petróleo y divisas, y el gobierno venezolano ganaba profesionales y, según varios analistas, seguridad.""")],
 ["FR-VZ011", "FR-VZ012", "FR-VZ027", "FR-VZ010", "FR-VZ022"]),

(T, "hecho", [("¿Qué hacían los militares cubanos en Venezuela?", """Según una investigación de Reuters, una parte clave de su papel fue en la inteligencia militar, para vigilar a las propias fuerzas armadas venezolanas. El gobierno cubano lo negó durante años.

Según esa investigación de 2019, basada en documentos y en exfuncionarios, tras perder un referendo en diciembre de 2007 Chávez pidió consejo a Fidel Castro. El 26 de mayo de 2008 el ministro de Defensa venezolano, Gustavo Rangel, y el viceministro de Defensa cubano, general Álvaro López, firmaron dos acuerdos. Por el primero, Cuba supervisaría la reestructuración de la inteligencia militar venezolana (DIM), y grupos de hasta 40 oficiales se entrenarían en La Habana hasta tres meses. Por el segundo, un grupo de ocho «expertos militares» cubanos inspeccionaría unidades y entrenaría soldados.

Según Reuters, cinco personas que conocían los cursos dijeron que los instructores cubanos explicaron a los agentes venezolanos que su misión sería infiltrar y controlar a las fuerzas armadas. En 2011 la DIM pasó a llamarse DGCIM, de contrainteligencia, y según exfuncionarios creció de unos cientos de agentes a por lo menos 1.500.

La respuesta del gobierno cubano: según Reuters, en marzo de 2019 el canciller Bruno Rodríguez rechazó «firmemente» las «reiteradas y falsas acusaciones» de que militares cubanos entrenaran, controlaran o intimidaran en Venezuela.

Después de la caída de Maduro, según Reuters en febrero de 2026, algunos asesores cubanos fueron apartados de sus puestos en la DGCIM, aunque otros seguían en Venezuela.""")],
 ["FR-VZ013", "FR-VZ014", "FR-VZ015", "FR-VZ025"]),

(T, "reformulacion", [("Cuba siempre dijo que no tenía militares en Venezuela, y era verdad, eran médicos.", """Eso fue lo que dijo el gobierno cubano durante años, pero en enero de 2026 él mismo reconoció que tenía militares allí.

Lo que decía La Habana: según Factchequeado, en abril de 2019 el presidente Miguel Díaz-Canel escribió que «no hay operaciones militares, ni tropas cubanas en Venezuela». El 19 de diciembre de 2024 el viceministro de Exteriores Carlos Fernández de Cossío dijo: «No hay tropas. Cuba no participa en operaciones militares ni en operaciones de seguridad en Venezuela».

Lo que pasó después: el 3 de enero de 2026 una operación militar de Estados Unidos en Caracas capturó a Nicolás Maduro, y el gobierno cubano informó que 32 miembros de sus Fuerzas Armadas Revolucionarias y del Ministerio del Interior murieron en esa operación. Según el comunicado de la Presidencia de Cuba recogido por Infobae, cumplían misiones «a solicitud de órganos homólogos» de Venezuela y «cayeron, tras férrea resistencia, en combate directo contra los atacantes».

Muchos de los cubanos en Venezuela sí eran civiles. Según el Servicio de Investigación del Congreso de EE. UU., los funcionarios cubanos sostenían que la gran mayoría del personal cubano allí era sanitario, y expertos regionales consideraban exagerada la cifra de 20.000 a 25.000 efectivos de seguridad que dio John Bolton en 2019.

Así que lo más exacto sería decir que muchos eran civiles, pero que también había militares y agentes de seguridad cubanos, algo que el gobierno cubano negó hasta enero de 2026.""")],
 ["FR-VZ018", "FR-VZ020", "FR-VZ021", "FR-VZ017"]),

(T, "hecho", [("¿Cuántos cubanos había en Venezuela?", """Nunca se ha conocido una cifra exacta, y las estimaciones varían mucho según quién las dé y qué cuente.

Según el Servicio de Investigación del Congreso de EE. UU., un estudio de 2014 estimó que había unos 40.000 profesionales cubanos en Venezuela, el 75 % de ellos en salud. El economista Carmelo Mesa-Lago menciona 40.000 médicos, maestros y otros profesionales en 2008, y la periodista Alma Guillermoprieto escribió que en 2003 Fidel Castro aceptó enviar cerca de 30.000 internacionalistas.

Sobre el personal de seguridad las cifras se disparan. Según el mismo informe del Congreso, en 2019 el asesor de Seguridad Nacional John Bolton dijo que Cuba tenía entre 20.000 y 25.000 efectivos de seguridad en Venezuela, aunque expertos regionales consideraban la cifra mucho menor y sin capacidad de combate. El secretario de Estado Pompeo habló después de 2.300, y los funcionarios cubanos sostenían que la gran mayoría del personal cubano era sanitario.

El dato más firme llegó en 2026: el gobierno cubano informó que 32 miembros de sus Fuerzas Armadas Revolucionarias y del Ministerio del Interior murieron en la operación estadounidense que capturó a Maduro, lo que confirmó que había militares cubanos en Venezuela, aunque no cuántos.

En resumen, había decenas de miles de profesionales civiles, sobre todo de salud, y un número desconocido de personal militar y de seguridad.""")],
 ["FR-VZ019", "FR-VZ006", "FR-VZ017", "FR-VZ020"]),

(T, "hecho", [("¿Qué pasó con los cubanos cuando Estados Unidos capturó a Maduro?", """Murieron 32 militares cubanos, y el gobierno de Cuba tuvo que reconocer públicamente su presencia en Venezuela.

El 3 de enero de 2026 una operación militar de Estados Unidos en Caracas capturó a Nicolás Maduro. El gobierno cubano informó que 32 miembros de sus Fuerzas Armadas Revolucionarias y del Ministerio del Interior murieron en esa operación y decretó duelo nacional.

La versión oficial: según el comunicado de la Presidencia de Cuba recogido por Infobae, los 32 cubanos cumplían misiones «a solicitud de órganos homólogos» de Venezuela y «cayeron, tras férrea resistencia, en combate directo contra los atacantes o como resultado de los bombardeos a las instalaciones».

La reacción de Washington y La Habana: según Reuters, el 11 de enero Trump escribió que «no habrá más petróleo ni dinero para Cuba». Díaz-Canel respondió que «nadie nos dicta lo que hacemos», y el canciller Bruno Rodríguez negó que Cuba hubiera recibido compensación financiera o «material» por servicios de seguridad prestados a cualquier país. Cuba dijo que los 32 muertos se ocupaban de «seguridad y defensa», sin detallar el acuerdo.

Lo que se supo después: según Reuters en febrero de 2026, los 32 formaban parte de un acuerdo de seguridad iniciado a finales de los años 2000, y desde mediados de diciembre de 2025 Estados Unidos bloqueaba los envíos de petróleo venezolano a Cuba. Cuba condenaba que Estados Unidos impidiera esos envíos y se decía abierta al diálogo en pie de igualdad.""")],
 ["FR-VZ020", "FR-VZ021", "FR-VZ022", "FR-VZ026"]),

(T, "contexto", [("¿Por qué se acabó el petróleo venezolano para Cuba?", """No se acabó de golpe: venía cayendo desde hacía años y se cortó del todo con la caída de Maduro.

La caída gradual: según OnCuba, con datos de Reuters, las exportaciones de petróleo de PDVSA a Cuba fueron de unos 56.000 barriles diarios en 2023 y de 24.000 en 2024, bajaron a unos 10.000 en enero de 2025 y a 8.000 en junio, y subieron a 31.000 en julio de 2025. Para comparar, según el economista Carmelo Mesa-Lago, en 2008 Venezuela enviaba 97.000 barriles diarios.

El corte: según Reuters, en 2025 Venezuela seguía siendo el mayor proveedor de petróleo de Cuba, con unos 26.500 barriles diarios, cerca del 50 % del déficit petrolero cubano, pero desde la captura de Maduro en enero de 2026 no había salido ningún cargamento hacia Cuba. Según otra nota de Reuters, desde mediados de diciembre de 2025 Estados Unidos bloqueaba esos envíos. México se volvió un proveedor alternativo, en volúmenes pequeños.

Lo que se temía: Mesa-Lago ya advertía en 2009 que la dependencia de Cuba respecto a Venezuela era muy fuerte y que, si la ayuda terminaba o se reducía mucho, Cuba podría enfrentar un segundo «Período Especial».

En resumen, los envíos venían cayendo desde hacía años, y la captura de Maduro y el cierre impuesto por Estados Unidos los cortaron.""")],
 ["FR-VZ024", "FR-VZ023", "FR-VZ026", "FR-VZ011", "FR-VZ012"]),

(T, "perspectivas", [("¿Cuba cobraba por la ayuda que daba a Venezuela?", """Depende de qué ayuda. Por los profesionales civiles hay estimaciones de mucho dinero. Por la seguridad, el gobierno cubano lo niega y no hay cifras públicas.

Los profesionales: según el economista Carmelo Mesa-Lago, en 2008 Venezuela pagó unos 5.650 millones de dólares por los servicios de 40.000 médicos, maestros y otros profesionales cubanos, dentro de una ayuda total estimada en 9.405 millones ese año. Según el Servicio de Investigación del Congreso de EE. UU., el acuerdo de 2000 era en esencia un trueque de petróleo por personal médico.

El petróleo: según la periodista Alma Guillermoprieto, desde octubre de 2000 Cuba recibía petróleo a precio de mercado pero con un crédito muy fácil, y desde 2001 Venezuela pagaba además en efectivo bienes y servicios cubanos. Según una investigación de Reuters, desde la llegada de Chávez Venezuela envió al menos 55.000 barriles diarios, más de 21.000 millones de dólares según cifras oficiales y precios medios.

La seguridad: según Reuters, en enero de 2026 el canciller del gobierno cubano, Bruno Rodríguez, negó que Cuba hubiera recibido compensación financiera o «material» por servicios de seguridad prestados a cualquier país, mientras Trump sostenía que Cuba vivió durante años del petróleo y el dinero de Venezuela.

Las dos afirmaciones no se contradicen necesariamente: una cosa son los pagos por profesionales civiles, que están estimados, y otra los servicios de seguridad, sobre los que las fuentes que tenemos no dan cifras.""")],
 ["FR-VZ011", "FR-VZ006", "FR-VZ005", "FR-VZ003", "FR-VZ022"]),

(T, "hecho", [("¿Qué pasó con los cubanos en Venezuela después de la caída de Maduro?", """Muchos empezaron a irse, sobre todo los de seguridad, aunque la relación oficial entre los dos gobiernos siguió.

Según Reuters, que citó a 11 fuentes en febrero de 2026, asesores de seguridad y médicos cubanos estaban saliendo de Venezuela bajo la presión de Washington sobre el gobierno de la presidenta interina Delcy Rodríguez. Ella confió su protección a escoltas venezolanos, a diferencia de Maduro y de Chávez, que dependían de fuerzas cubanas de élite. Algunos asesores cubanos fueron apartados de sus puestos en la DGCIM, aunque otros seguían en Venezuela.

En público, la relación no se rompió: según la misma nota, Delcy Rodríguez y Díaz-Canel dijeron que los dos países seguían «unidos». Cuba condenaba que Estados Unidos impidiera los envíos de petróleo venezolano, se decía abierta al diálogo en pie de igualdad y prometía resistir.

El petróleo ya no llegaba: según Reuters, desde la captura de Maduro no había salido ningún cargamento de petróleo venezolano hacia Cuba, cuando en 2025 Venezuela había enviado unos 26.500 barriles diarios.

Qué significa, según un experto: el historiador Alejandro Velasco, de la Universidad de Nueva York, considera que la influencia cubana fue «absolutamente esencial» para la supervivencia del gobierno chavista. Si eso es así, su salida es un cambio de fondo para el nuevo gobierno venezolano.""")],
 ["FR-VZ025", "FR-VZ026", "FR-VZ023", "FR-VZ027"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": NOTA}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
