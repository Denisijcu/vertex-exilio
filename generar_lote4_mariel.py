"""
generar_lote4_mariel.py — Cuarto lote de ejemplos sobre el Mariel (11 ejemplos).

Uso (desde E:\\vertex-exilio):
    python generar_lote4_mariel.py

Este lote trae la voz de quienes salieron (testimonios recogidos por Cros Sandoval y citados por
Guerra), quién organizaba los actos de repudio, el perfil de los marielitos y la respuesta de
Estados Unidos, con los fragmentos verificados en Larzelere (F007) y Guerra (F006).

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_mariel.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_mariel_lote4.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_mariel.jsonl")
DESTINO = Path("datos/borrador_mariel_lote4.jsonl")
PRIMER_ID = 42

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
("humano", [("Mi papá salió por el Mariel con 25 años. ¿Por qué se fue tanta gente joven?", """Tu papá encaja en el perfil de quienes salieron en 1980. Según la historiadora Lillian Guerra, que cita estudios de Clark, Lasaga y Reque y de María Cristina García, los marielitos eran un 70 por ciento hombres, un 92 por ciento de clase trabajadora y hasta un 40 por ciento mestizos o negros, con una edad media de unos 30 años. A diferencia de las olas anteriores, habían crecido bajo la revolución.

Ese perfil no explica por sí solo por qué se fueron, y cada persona tuvo sus razones. Pero los testimonios que recogió la antropóloga Mercedes Cros Sandoval, que entre 1980 y 1982 entrevistó a 439 refugiados del Mariel, dan algunas pistas.

Un estudiante de 19 años contó que, por cuestionar en clase el trabajo voluntario en memoria de Marx y Lenin, el maestro lo llevó aparte y le advirtió que era demasiado joven para acabar preso. Una muchacha llamada María contó que a los 14 años la maestra le pidió en privado que no hiciera preguntas que pudieran avergonzar al gobierno, después de que preguntara en clase por qué no había mariscos para los cubanos.

Son experiencias individuales, no una estadística, pero muestran el tipo de situaciones que algunos de esos jóvenes contaron al explicar su salida.

Si tu papá está dispuesto, su propia historia vale más que cualquier promedio. Pregúntale qué lo llevó a decidir irse.""")],
 ["FR-M062", "FR-M037", "FR-M056", "FR-M057"]),

("humano", [("¿Cómo era para un joven en Cuba antes del Mariel? ¿Se podía decir lo que uno pensaba?", """Lo que se puede contar con base son los testimonios de quienes salieron, y conviene tomarlos como lo que son: experiencias personales de un grupo concreto.

Entre 1980 y 1982 la antropóloga Mercedes Cros Sandoval entrevistó a 439 refugiados del Mariel, y algunos de esos relatos tratan justamente de eso. Un estudiante de 19 años, criado como católico a escondidas, contó que cuestionó en clase que hubiera que hacer trabajo voluntario en memoria de Marx y Lenin; el maestro lo llevó aparte, le advirtió que era demasiado joven para acabar preso, y él lloró.

Una marielita llamada María contó que a los 14 años preguntó en clase por qué en Cuba no había mariscos para el consumo si abundaban en sus aguas. La maestra dio una explicación oficial y después la llevó aparte para advertirle que no hiciera preguntas que pudieran avergonzar al gobierno.

Una mujer contó que su esposo, militante comunista, se había inventado un origen humilde, y que su hijo mayor lo desmintió cuando los visitó la familia exiliada. Dos años después ese hijo entró con su esposa en la embajada del Perú, y ella y su hijo menor lo siguieron.

Estas historias no dicen cómo lo vivían todos los cubanos de la época; quienes se quedaron pueden contarlo de otra manera. Lo que sí muestran son situaciones que algunos de los que se fueron en 1980 recordaban al explicar por qué salieron.""")],
 ["FR-M037", "FR-M056", "FR-M057", "FR-M058"]),

("contexto", [("¿Los actos de repudio eran espontáneos o los organizaba alguien?", """Las fuentes que hemos revisado los describen como actos organizados.

Según la historiadora Lillian Guerra, los actos de repudio de 1980 los organizaban los Comités de Defensa de la Revolución, incluida su dirección nacional, junto con escuelas y organizaciones de masas, y muchos maestros llevaron a sus aulas completas. Guerra añade que los dirigían activistas de los CDR, en su mayoría amas de casa y jubilados, y maestros, por lo que predominaban mujeres y niños.

También describe cómo fueron cambiando. Desde abril y durante todo el verano, los mítines empezaron cerca de la embajada del Perú y pasaron después a las casas de quienes pedían permiso de salida, a menudo repetidos hasta el día en que se iban. De noche se pintaban las fachadas con frases como "Aquí vive un traidor".

La escala la da el propio periódico oficial. Según Granma, citado por Guerra, en la calzada de Carlos III de La Habana se celebró un mitin de repudio de unas 100.000 personas, y Guerra señala que reuniones parecidas se hacían en toda la isla casi cada noche.

Eso no quiere decir que todos los que participaron lo hicieran por la misma razón: las fuentes hablan de cómo se organizaban, no de lo que pensaba cada participante. Pero con lo que tenemos, la respuesta es que había una estructura detrás.""")],
 ["FR-M030", "FR-M059", "FR-M031", "FR-M034"]),

("humano", [("¿Qué le pasaba a alguien que defendía a la víctima de un acto de repudio?", """Lo que tenemos documentado es un caso concreto, y conviene no generalizar a partir de uno solo.

Según la historiadora Lillian Guerra, el profesor de filosofía marxista Ariel Hidalgo defendió a un alumno que estaba siendo atacado en un mitin de repudio. Después de eso fue internado en un hospital psiquiátrico. Más tarde fue detenido por un manuscrito crítico y empezó a cumplir una condena de ocho años el 19 de abril de 1981, y pasó los primeros catorce meses aislado.

Guerra presenta el caso como ejemplo de que oponerse a los actos de repudio también tenía consecuencias. Llama la atención, además, que Hidalgo enseñara precisamente filosofía marxista.

Lo que no podemos decir con las fuentes que tenemos es qué le pasaba a quien simplemente no acudía a un mitin, ni con qué frecuencia se castigaba a quienes intervenían. Para eso harían falta más testimonios o documentos de la época, y prefiero no rellenar ese hueco con suposiciones.

Si en tu familia alguien vivió un acto de repudio, de un lado o del otro, su recuerdo es justamente el tipo de testimonio que falta para entender mejor esos meses.""")],
 ["FR-M061", "FR-M032"]),

("contexto", [("¿Por qué Perú no entregó a los que entraron por la fuerza en su embajada?", """Para entenderlo hay que ir un poco antes del 1 de abril de 1980.

Según el historiador Alex Larzelere, a principios de ese año 12 personas entraron por la fuerza en la embajada del Perú en La Habana. El embajador, Edgardo de Habich, les negó el asilo y las devolvió a sus casas, pero el Ministerio de Relaciones Exteriores del Perú desautorizó su decisión y le ordenó llevarlas de vuelta a la embajada. Él lo hizo y anunció que dejaba el cargo. Perú ya había dejado clara su posición sobre el asilo.

Tras el incidente del 1 de abril, según Larzelere, el gobierno cubano declaró en la primera página de Granma que no daría salvoconducto para salir del país a nadie que entrara por la fuerza en una embajada extranjera. Según la historiadora Lillian Guerra, el embajador peruano, Ernesto Pinto Bazurco Rittler, se negó a entregar a quienes habían entrado pese a las exigencias de las autoridades cubanas.

El 4 de abril el gobierno cubano retiró la custodia de la embajada y dejó el acceso abierto. Guerra sostiene que fue una represalia por la negativa peruana; es su interpretación, y así conviene contarla.

En resumen, Perú defendía su derecho a conceder asilo, y el gobierno cubano sostenía que quien entrara por la fuerza no tenía derecho a salir.""")],
 ["FR-M049", "FR-M050", "FR-M052", "FR-M002"]),

("hecho", [("Leí que el primero en entrar a la embajada del Perú era negro. ¿Es verdad? ¿Había muchos negros entre los marielitos?", """Eso lo cuenta el propio embajador del Perú de entonces, Ernesto Pinto Bazurco Rittler. Según su testimonio, citado por la historiadora Lillian Guerra, el primer cubano que entró a pedir asilo cuando se retiró la guardia fue un hombre negro, que le dijo que esperaba que muchos siguieran su ejemplo. El embajador cuenta también que entre los policías, militares e informantes reunidos alrededor de la embajada no distinguió a ningún afrocubano.

Conviene tomarlo como lo que es: el recuerdo de un testigo directo, no un recuento.

Para la segunda pregunta sí hay cifras. Según Guerra, que cita estudios de Clark, Lasaga y Reque y de María Cristina García, hasta un 40 por ciento de los marielitos eran mestizos o negros. Además eran un 70 por ciento hombres y un 92 por ciento de clase trabajadora, con una edad media de unos 30 años. Guerra subraya que, a diferencia de las olas anteriores, habían crecido bajo la revolución.

Ese perfil es una de las cosas que distinguen al Mariel de las salidas anteriores, aunque para compararlas con precisión harían falta las cifras de esas otras olas, que todavía no tenemos verificadas.""")],
 ["FR-M053", "FR-M062"]),

("hecho", [("¿Qué hizo el gobierno de Estados Unidos en las primeras semanas del Mariel?", """En pocas semanas la respuesta de Estados Unidos fue cambiando. Va en orden.

El 26 de abril de 1980, el gobernador de la Florida, Bob Graham, declaró zonas de desastre los condados de Monroe y Dade por la llegada de refugiados cubanos y activó la Guardia Nacional de la Florida. Al día siguiente, el 27 de abril, se designó a la FEMA para coordinar la respuesta federal sobre el terreno.

El 28 de abril el Servicio de Aduanas empezó a incautar los barcos que volvían de Mariel por traer extranjeros ilegales, pero la FEMA suspendió las incautaciones a los dos días, cuando el ambiente en los muelles de Cayo Hueso se volvió tenso.

El 6 de mayo el gobierno federal declaró la emergencia en la Florida y destinó 10 millones de dólares en fondos para refugiados. En esas semanas Carter pasó de hablar de recibir a los cubanos con los brazos abiertos a anunciar, el 14 de mayo, un programa de cinco puntos para poner fin al éxodo.

El 20 de mayo la Casa Blanca anunció que los cubanos que llegaban no serían tratados como refugiados bajo la Ley de Refugiados de 1980, sino como solicitantes de asilo.

Todas estas fechas vienen de la obra del historiador Alex Larzelere sobre el éxodo.""")],
 ["FR-M048", "FR-M043", "FR-M044", "FR-M014", "FR-M016", "FR-M045"]),

("contexto", [("¿Los marielitos entraron como refugiados?", """No exactamente, y la diferencia tuvo consecuencias.

El 20 de mayo de 1980 la Casa Blanca anunció que los cubanos que llegaban no serían tratados como refugiados bajo la Ley de Refugiados de 1980, sino como solicitantes de asilo. Un mes después, el 20 de junio, Estados Unidos creó para ellos el estatus de "Cuban-Haitian Entrant", distinto del de refugiado.

Esa situación se prolongó durante años. La salida llegó en 1984, cuando una revisión de la Ley de Ajuste Cubano de 1966 permitió a los cubanos del Mariel obtener la residencia permanente. Los haitianos llegados en esas fechas no recibieron ese beneficio.

Así que, en sentido estricto, los marielitos no entraron con el estatus legal de refugiado, aunque en el lenguaje de todos los días se les llame así. Lo que tuvieron fue una vía específica, la revisión de 1984, para quedarse legalmente.

Para una minoría el camino fue más largo: para junio de 2016 todavía quedaban 478 marielitos que no podían ser admitidos bajo la ley migratoria estadounidense.""")],
 ["FR-M045", "FR-M018", "FR-M021", "FR-M024"]),

("hecho", [("Aparte de los actos de repudio, ¿hubo violencia contra los que querían irse?", """Sí, las fuentes registran más de un tipo de violencia, y conviene distinguirlos.

Los actos de repudio, según las fuentes que hemos revisado, incluían turbas que golpeaban a las personas, les colgaban carteles acusatorios y destrozaban sus casas, y se organizaron durante meses. Según la historiadora Lillian Guerra, empezaron cerca de la embajada del Perú y pasaron después a las casas de quienes pedían permiso de salida, a menudo repetidos hasta el día en que se iban.

Hubo además un episodio distinto. Según la cronología del historiador Alex Larzelere, el 2 de mayo de 1980 un grupo de unos 300 hombres armados con palos, llevados en autobuses del gobierno, atacó en La Habana a ex presos políticos y a sus familiares reunidos frente a la Sección de Intereses de Estados Unidos.

Ese último dato viene de una sola fuente, así que lo correcto es contarlo atribuido a Larzelere mientras no aparezca una segunda.

Lo que no tenemos es un recuento de heridos de esos meses, así que no te puedo dar cifras sobre eso.""")],
 ["FR-M025", "FR-M031", "FR-M046"]),

("perspectivas", [("¿Por qué se suspendieron los vuelos de La Habana a Costa Rica en 1980?", """Los vuelos duraron muy poco. El 16 de abril de 1980 empezaron vuelos de evacuación desde La Habana hacia San José, Costa Rica, y a los dos días se suspendieron, cuando se habían evacuado 678 personas.

El historiador Alex Larzelere da más detalle sobre cómo terminó. Según él, al tercer día el gobierno de Costa Rica anunció que suspendía los vuelos a petición de Cuba.

El porqué es otra cuestión. Larzelere lo atribuye a que la publicidad internacional negativa de los vuelos había molestado al gobierno de Castro. Es su interpretación: no tenemos una declaración del gobierno cubano que explique la decisión, así que lo correcto es presentarla como la explicación de Larzelere y no como un hecho comprobado.

Lo que sí está claro es lo que vino después. El 20 de abril el gobierno cubano anunció que el puerto de Mariel quedaba abierto para quien tuviera a alguien que fuera a recogerlo en barco, y la salida pasó del aire al mar.""")],
 ["FR-M005", "FR-M047", "FR-M006"]),

("reformulacion", [("Fidel dijo que los que se iban eran escoria, ¿no? ¿Eso es verdad o es un invento de Miami?", """Lo dijo, sí, aunque conviene precisar cómo.

En su discurso del Primero de Mayo de 1980, según la traducción al inglés del servicio FBIS, Fidel Castro llamó "scum", es decir "escoria", a quienes habían entrado en la embajada del Perú. En ese mismo discurso describió a la mayoría de quienes se iban como "lumpen" y elementos antisociales, y responsabilizó a Estados Unidos y a la CIA de alentar el desorden.

No fue algo aislado. Durante el éxodo, la prensa estatal cubana calificó públicamente a quienes se iban con términos despectivos, y el gobierno difundió el testimonio de un agente infiltrado entre quienes pidieron asilo en la embajada del Perú, que los describía como "escoria", y lo exhibió en fotomurales en la antigua sede de la embajada.

Otra cosa es si la descripción se ajusta a los datos. Según las cifras que recoge Wikipedia, alrededor del 2,2 por ciento de los cerca de 125.000 que llegaron fueron clasificados como delincuentes graves bajo la ley estadounidense. La historiadora Lillian Guerra señala que al menos 20.000 habían pasado algún tiempo en prisiones cubanas, pero que la mayoría de ellos no eran autores de delitos violentos, sino personas que se resistían al adoctrinamiento político o que habían participado en el mercado negro.

Así que la palabra no es un invento: está en el discurso. Lo que los datos no sostienen es que describiera a la mayoría de los que salieron.""")],
 ["FR-M051", "FR-M028", "FR-M027", "FR-M026", "FR-M038", "FR-M020", "FR-M011", "FR-M055"]),
]

if DESTINO.exists():
    with DESTINO.open(encoding="utf-8-sig") as f:
        revisados = [json.loads(l)["id"] for l in f if l.strip() and json.loads(l).get("estado_revision") != "pendiente"]
    if revisados:
        print(f"{DESTINO} ya tiene {len(revisados)} ejemplos revisados ({', '.join(revisados[:5])}...). No lo sobrescribo.")
        sys.exit(1)

usados = sorted({x for _, _, ids in E for x in ids})
faltan = [x for x in usados if x not in frag]
no_aprobados = [x for x in usados if x in frag and frag[x].get("estado") != "aprobado"]
if faltan or no_aprobados:
    print(f"No genero nada. Fragmentos que no existen: {faltan}. Fragmentos sin aprobar: {no_aprobados}.")
    sys.exit(1)

DESTINO.parent.mkdir(exist_ok=True)
with DESTINO.open("w", encoding="utf-8", newline="\n") as f:
    for i, (tipo, turnos, ids) in enumerate(E):
        mensajes = []
        for preg, resp in turnos:
            mensajes += [{"role": "user", "content": preg}, {"role": "assistant", "content": resp.strip()}]
        ej = {"id": f"exi-m{PRIMER_ID + i:03d}", "etapa": "mariel_1980", "tipo": tipo, "messages": mensajes,
              "fuentes": [{"id_fragmento": x, "id_fuente": frag[x]["id_fuente"], "fragmento": frag[x]["texto"]} for x in ids],
              "estado_revision": "pendiente", "revisor": "", "notas": "Lote 4"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
