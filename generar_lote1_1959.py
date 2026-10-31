"""
generar_lote1_1959.py — Primer lote de ejemplos de las etapas 1959-1962 y Pedro Pan (12 ejemplos).

Uso (desde E:\\vertex-exilio):
    python generar_lote1_1959.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_1959_1962.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_1959_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

Pedro Pan es un tema con versiones enfrentadas: el lote enseña a separar el hecho (la ley de la
patria potestad nunca existió), lo que dice cada parte (EcuRed, Walsh) y lo que está documentado
sobre la CIA (el fallo de 1999 y las admisiones de ex agentes).
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_1959_1962.jsonl")
DESTINO = Path("datos/borrador_1959_lote1.jsonl")
PREFIJO = "exi-s"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
("pedro_pan", "hecho", [("¿Qué fue la Operación Pedro Pan?", """La Operación Pedro Pan fue la salida de más de 14.000 niños y adolescentes cubanos que llegaron a Estados Unidos sin sus padres entre diciembre de 1960 y octubre de 1962. La estimación más citada es de 14.048.

Empezó en Miami con un caso concreto. En noviembre de 1960 llegó a la oficina del padre Bryan Walsh, director del Catholic Welfare Bureau, un muchacho cubano de 15 años, Pedro, cuyos familiares no podían mantenerlo. El 12 de diciembre de 1960 Walsh se reunió con James Baker, director de la Academia Ruston de La Habana, que ayudaba a padres cubanos a enviar a sus hijos a Estados Unidos.

Tras la ruptura de relaciones entre Estados Unidos y Cuba, el 3 de enero de 1961, el Departamento de Estado autorizó el 9 de enero al Catholic Welfare Bureau a emitir exenciones de visa: cartas firmadas por Walsh que las aerolíneas aceptaban.

Aproximadamente la mitad de los niños tenía familiares o amigos en Estados Unidos que los acogieron. El resto quedó al cuidado de agencias según su religión, y la agencia católica atendió a algo más de 7.000.

La operación terminó en octubre de 1962, con la Crisis de Octubre, aunque las fechas exactas de inicio y final varían un poco según la fuente.""")],
 ["FR-PP001", "FR-PP003", "FR-PP004", "FR-PP006", "FR-PP002"]),

("pedro_pan", "perspectivas", [("¿Pedro Pan fue una operación de la CIA?", """Es una de las preguntas más discutidas sobre Pedro Pan, y conviene separar lo que dice cada parte de lo que está documentado.

La versión oficial cubana es clara. Según EcuRed, la enciclopedia del gobierno cubano, fue una operación de subversión organizada por el Departamento de Estado, la jerarquía católica de Miami, la CIA y organizaciones opuestas al gobierno revolucionario, que manipuló el tema de la patria potestad.

El padre Bryan Walsh, de la agencia católica de Miami que atendió a algo más de 7.000 de los niños, sostiene en cambio que la Iglesia en Cuba como institución no participó.

Lo documentado matiza las dos versiones. Según recoge Wikipedia, en 1999 un tribunal federal de Illinois concluyó, tras revisar 733 páginas de documentos de la CIA, que la evacuación de los niños no fue una operación de la CIA. Pero varios ex agentes de la CIA admitieron haber editado, impreso y distribuido copias de una falsa ley de la patria potestad. La historiadora Deborah Shnookal sostiene que esa falsa ley circuló primero en Cuba a través de grupos contrarios a Castro y de católicos, y que después la amplificó Radio Swan, una emisora respaldada por la CIA.

En resumen, con lo que tenemos, la salida de los niños no aparece como una operación de la CIA, pero la CIA sí participó en difundir un rumor que pesó en la decisión de muchas familias.""")],
 ["FR-PP013", "FR-PP015", "FR-PP006", "FR-PP012", "FR-PP011", "FR-PP010"]),

("pedro_pan", "reformulacion", [("Mi abuela dice que mandó a mi papá en Pedro Pan porque Fidel iba a quitarle la patria potestad. ¿Eso era verdad?", """Lo que tu abuela temía era real para ella y para miles de familias, pero la ley que se rumoreaba nunca existió.

El gobierno cubano nunca aprobó una ley para quitar a los padres la patria potestad sobre sus hijos. El rumor de que lo haría circuló en aquellos años y pesó en la decisión de muchas familias de enviar a sus hijos solos.

De dónde salió el rumor es otra cuestión. La historiadora Deborah Shnookal sostiene que la falsa ley circuló primero en Cuba a través de grupos contrarios a Castro y de católicos, y que después la amplificó Radio Swan, una emisora respaldada por la CIA. Según recoge Wikipedia, varios ex agentes de la CIA admitieron haber editado, impreso y distribuido copias de esa falsa ley.

Pero el miedo de los padres no venía solo del rumor. Según Rita Cauce, los padres querían evitar que sus hijos recibieran adoctrinamiento comunista, y entre los hechos que pesaron cita la campaña de alfabetización y la confiscación de las escuelas privadas y católicas en 1961.

Así que tu abuela no se lo inventó: tomó una decisión muy difícil con la información y el miedo que había en ese momento. Lo que hoy sabemos es que esa ley concreta nunca llegó a existir.""")],
 ["FR-PP010", "FR-PP011", "FR-PP012", "FR-PP009"]),

("pedro_pan", "humano", [("Mi mamá llegó sola en Pedro Pan con 12 años. ¿Qué pasaba con los niños cuando llegaban?", """Tu mamá estaba en la franja de edad más numerosa. Según el padre Bryan Walsh, el 85 por ciento de los 7.000 niños atendidos por su agencia tenía entre 12 y 18 años al llegar, y el 70 por ciento eran varones mayores de 12.

Lo que pasaba al llegar dependía sobre todo de una cosa: si había alguien esperando. Aproximadamente la mitad de los niños tenía familiares o amigos en Estados Unidos que los acogieron. El resto quedó al cuidado de agencias según su religión, y la agencia católica atendió a algo más de 7.000.

En Miami hubo albergues como el campamento de Matecumbe, con unos 400 varones, y el de Florida City. En total, los niños fueron acogidos en hogares y centros de unas 100 ciudades de 35 estados.

Las experiencias no fueron iguales para todos, y no todas fueron buenas. Según recoge Wikipedia, en 1978 el grupo Areíto y Casa de las Américas publicaron 'Contra viento y marea', con testimonios anónimos de cubanos que salieron de niños y que hablaban de soledad, malas condiciones y maltrato mental, físico y sexual.

Si tu mamá quiere contarlo, pregúntale dónde estuvo los primeros días y si la recogió alguien conocido. Esa parte de la historia solo la sabe ella.""")],
 ["FR-PP007", "FR-PP006", "FR-PP008", "FR-PP018"]),

("pedro_pan", "perspectivas", [("¿Los niños de Pedro Pan volvieron a ver a sus padres?", """La mayoría sí, aunque muchos tardaron años, y sobre los casos que no lo lograron las versiones no coinciden.

Según el padre Bryan Walsh, cuando empezaron los Vuelos de la Libertad, el 1 de diciembre de 1965, los padres de los niños de Pedro Pan tuvieron prioridad, y cerca del 90 por ciento de los que seguían a cargo de su agencia se reunió con sus padres para junio de 1966. Walsh atribuye los retrasos sobre todo a que el gobierno cubano demoraba la salida de ciertos profesionales y no dejaba salir con sus padres a los varones de 15 a 26 años por el servicio militar.

Walsh sostiene además que su agencia no tenía constancia de ningún niño perdido, y considera falsos los informes de que muchos niños perdieron el contacto con sus familias.

La versión oficial cubana es otra. Según EcuRed, muchos de los niños nunca volvieron a encontrarse con sus padres.

Las dos afirmaciones vienen de partes interesadas, y no tenemos una cifra independiente de cuántos niños nunca se reunieron con su familia. Lo honesto es dar las dos versiones y no elegir una sin base.""")],
 ["FR-PP016", "FR-PP017", "FR-PP015", "FR-PP013"]),

("pedro_pan", "hecho", [("¿Cómo salían los niños de Cuba si ya no había relaciones con Estados Unidos?", """Por una vía bastante inusual: cartas firmadas por un sacerdote.

Tras la ruptura de relaciones entre Estados Unidos y Cuba, el 3 de enero de 1961, el Departamento de Estado autorizó el 9 de enero al Catholic Welfare Bureau de Miami a emitir exenciones de visa. Eran cartas firmadas por el padre Bryan Walsh que las aerolíneas aceptaban. La autorización era general para los niños de 6 a 16 años; para los de 16 a 18 había que pedir antes una revisión de seguridad.

Del lado cubano hacía falta que esos papeles llegaran a las familias. Según Rita Cauce, los documentos de los niños se movieron por una red clandestina encabezada por la enfermera británica Penny Powers, que había trabajado en el Kindertransport. Cauce añade que muchos de los miembros de esa red fueron detenidos y cumplieron largas condenas.

Con esos papeles los niños viajaban a Miami, hasta que la operación se detuvo en octubre de 1962, con la Crisis de Octubre. Las fechas exactas varían un poco según la fuente: Walsh sitúa las últimas llegadas el 23 de octubre de 1962 y Cauce dice que todo se detuvo el día 22.""")],
 ["FR-PP004", "FR-PP005", "FR-PP002"]),

("pedro_pan", "reformulacion", [("En Cuba dicen que Pedro Pan fue un robo de niños organizado por la Iglesia y la CIA. ¿Es cierto?", """Esa es, a grandes rasgos, la versión oficial cubana, y conviene separar lo que tiene base de lo que no.

Según EcuRed, la enciclopedia del gobierno cubano, la operación fue organizada por el Departamento de Estado, la jerarquía católica de Miami, la CIA y organizaciones opuestas al gobierno revolucionario, que manipuló el tema de la patria potestad.

Hay partes con base. La ley de la patria potestad que se rumoreaba nunca existió, y según recoge Wikipedia, varios ex agentes de la CIA admitieron haber editado, impreso y distribuido copias de esa falsa ley. También es cierto que una agencia católica de Miami acogió a buena parte de los niños: atendió a algo más de 7.000.

Otras partes no se sostienen con lo que tenemos. Fueron los padres quienes decidieron enviar a sus hijos, muchas veces por miedo a ese rumor o al adoctrinamiento, y aproximadamente la mitad de los niños fue acogida por familiares o amigos en Estados Unidos. Además, en 1999 un tribunal federal de Illinois concluyó, tras revisar 733 páginas de documentos de la CIA, que la evacuación no fue una operación de la CIA.

Lo que sí es real es el sufrimiento de muchas familias separadas. El libro 'Contra viento y marea', de 1978, recogió testimonios anónimos de cubanos que salieron de niños y que hablaban de soledad, malas condiciones y maltrato.""")],
 ["FR-PP013", "FR-PP010", "FR-PP012", "FR-PP006", "FR-PP009", "FR-PP018"]),

("salida_1959_1962", "contexto", [("¿Cuánta gente se fue de Cuba en los primeros años de la revolución?", """Para los primeros años hay una cifra muy citada, que viene del sociólogo Juan Clark: unos 64.000 cubanos habían salido de la isla a finales de 1959, y la cifra llegó a 248.070 a finales de 1962. La recoge Rita Cauce en su trabajo sobre Pedro Pan.

En Miami se notó enseguida. Según un artículo de la Seguridad Social de Estados Unidos de marzo de 1962, la población refugiada en el condado de Dade superaba las 55.000 personas, a pesar de que más de 16.000 habían sido reasentadas en otras zonas por el programa federal y otras 16.000 se habían trasladado por su cuenta.

Después de 1962 hubo una pausa larga. Los vuelos desde Cuba se reanudaron en 1965 y siguieron, con una breve interrupción, hasta el 6 de abril de 1973; según la ficha del Servicio de Parques Nacionales, en más de 3.000 Vuelos de la Libertad llegaron otros 175.000 cubanos.

Conviene tomar la cifra de Clark como una estimación: es la que más se repite, pero todavía no tenemos una segunda fuente independiente que la confirme.""")],
 ["FR-S001", "FR-S006", "FR-S011"]),

("salida_1959_1962", "hecho", [("¿Qué ayuda dio Estados Unidos a los primeros exiliados cubanos?", """Las fuentes de la época describen una ayuda organizada desde muy pronto.

En noviembre de 1960 el presidente Eisenhower encargó a Tracy S. Voorhees estudiar la situación de los refugiados cubanos, y bajo su dirección se creó en Miami un Centro de Emergencia para Refugiados Cubanos, financiado en parte con el Fondo de Contingencia del presidente.

Kennedy amplió el esfuerzo. El 27 de enero de 1961 encargó al secretario de Salud, Educación y Bienestar, Abraham Ribicoff, dirigir las actividades federales para los refugiados, y el 3 de febrero le ordenó poner en marcha un programa de nueve puntos con ayuda económica, salud, educación, empleo, reasentamiento en otras zonas y atención a los niños que llegaban sin sus padres.

En lo legal, a los cubanos se les autorizó una 'salida voluntaria indefinida', sin límite de tiempo, de modo que no se les abría proceso de deportación. En lo económico, de cada 20 refugiados registrados en el centro de Miami, 17 pedían ayuda en efectivo y 16 la recibían.

El programa evitó crear campamentos de refugiados y puso el acento en reasentar a los cubanos fuera de Miami. En 1962 la administración Kennedy impulsó además la Ley de Asistencia a la Migración y a los Refugiados para dar ayuda a los cubanos que llegaban.""")],
 ["FR-S002", "FR-S003", "FR-S005", "FR-S007", "FR-S006", "FR-S010"]),

("salida_1959_1962", "contexto", [("¿Quiénes fueron los primeros en irse después de 1959?", """Las cifras del propio gobierno estadounidense de la época dan una idea. Según un artículo de la Seguridad Social de 1962, más de un tercio de los cabezas de familia refugiados había trabajado en ocupaciones profesionales, semiprofesionales o directivas; casi un tercio, en trabajos de oficina, ventas o especializados; y menos de una cuarta parte no tenía una calificación especial.

Es decir, en esos primeros años salió una proporción alta de profesionales, aunque también salieron empleados de oficina, trabajadores especializados y personas sin una calificación particular.

Eso no significa que llegaran con dinero. Según el mismo artículo, de cada 20 refugiados registrados en el centro de Miami, 17 pedían ayuda en efectivo y 16 la recibían.

En cuanto al volumen, el sociólogo Juan Clark estima que unos 64.000 cubanos habían salido a finales de 1959 y 248.070 a finales de 1962. Es la cifra más citada, aunque conviene tratarla como una estimación.""")],
 ["FR-S008", "FR-S007", "FR-S001"]),

("salida_1959_1962", "hecho", [("¿Qué era la Torre de la Libertad de Miami?", """La Torre de la Libertad es un edificio de Miami que entre 1962 y 1974 funcionó como centro federal de asistencia a los refugiados cubanos. Los propios refugiados la llamaban 'El Refugio'.

Su función venía de un esfuerzo que había empezado antes. En noviembre de 1960, bajo la dirección de Tracy S. Voorhees, enviado del presidente Eisenhower, se creó en Miami un Centro de Emergencia para Refugiados Cubanos. En 1962 la administración Kennedy impulsó la Ley de Asistencia a la Migración y a los Refugiados para dar ayuda a los cubanos que llegaban, y desde ese año la Torre funcionó como centro.

Su etapa como centro coincidió además con los Vuelos de la Libertad. Los vuelos desde Cuba se reanudaron en 1965 y siguieron, con una breve pausa, hasta el 6 de abril de 1973; según la ficha del Servicio de Parques Nacionales, en más de 3.000 vuelos llegaron otros 175.000 cubanos.

Por eso, para muchas familias del exilio, la Torre de la Libertad es uno de los lugares que mejor resumen aquellos años de llegada.""")],
 ["FR-S009", "FR-S002", "FR-S010", "FR-S011"]),

("salida_1959_1962", "contexto", [("¿Los primeros exiliados pensaban volver pronto a Cuba?", """Lo que pensaba cada persona no lo recogen las fuentes que tenemos, así que no te puedo dar una respuesta general sobre sus intenciones.

Lo que sí está documentado es cómo lo planteó el gobierno de Estados Unidos. Según un artículo de la Seguridad Social de 1962, Kennedy presentó la ayuda como temporal: pidió asegurar a los refugiados que se buscaría facilitar su regreso voluntario a Cuba en cuanto las condiciones lo permitieran.

Al mismo tiempo, el programa federal evitó crear campamentos de refugiados y puso el acento en reasentar a los cubanos fuera de Miami. Según el mismo artículo, de marzo de 1962, más de 16.000 personas habían sido reasentadas por el programa y otras 16.000 se habían trasladado por su cuenta.

Hay también un dato de Pedro Pan que ayuda a entender lo que vino después. Según el padre Bryan Walsh, cuando empezaron los Vuelos de la Libertad, en diciembre de 1965, cerca del 90 por ciento de los niños que seguían a cargo de su agencia se reunió con sus padres para junio de 1966, ya en Estados Unidos.

Para saber qué pensaban de verdad aquellos primeros exiliados, lo mejor son los testimonios de quienes llegaron en esos años.""")],
 ["FR-S004", "FR-S006", "FR-PP016"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "1959-1962 lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
