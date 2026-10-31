"""
generar_lote1_camarioca.py — Primer lote de ejemplos de Camarioca y los Vuelos de la Libertad (13 ejemplos).

Uso (desde E:\\vertex-exilio):
    python generar_lote1_camarioca.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_camarioca_vuelos.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_camarioca_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

El lote enseña a manejar una cifra muy disputada (el total de los Vuelos de la Libertad), a dar la
versión de cada gobierno sobre Camarioca y a atribuir lo que solo cuenta una fuente.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_camarioca_vuelos.jsonl")
DESTINO = Path("datos/borrador_camarioca_lote1.jsonl")
PREFIJO = "exi-v"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
C = "camarioca_vuelos_libertad"
E = [
(C, "hecho", [("¿Qué pasó en Camarioca en 1965?", """En el otoño de 1965 el puerto cubano de Camarioca se convirtió en una vía de salida por mar hacia Estados Unidos.

El 28 de septiembre de 1965 Fidel Castro anunció que los cubanos que quisieran irse a Estados Unidos podrían hacerlo y que los exiliados podrían recoger a sus familiares en el puerto de Camarioca a partir del 10 de octubre. Esa es la fecha que dan el Departamento de Estado y el historiador Alex Larzelere; CubaNet habla del 3 de octubre.

Desde la Florida salieron enseguida embarcaciones pequeñas. Para el 18 de octubre ya habían llegado más de 700 personas. Según Larzelere y la Guardia Costera de Estados Unidos, quienes salían tenían que dejar sus casas y propiedades al gobierno cubano.

El puente marítimo duró poco. Cuba dejó de admitir barcos en Camarioca a partir del 28 de octubre y prohibió nuevas salidas desde allí el 4 de noviembre. En total salieron 2.979 cubanos antes de que el puerto se cerrara el 15 de noviembre de 1965. Entre el 13 y el 24 de noviembre, Estados Unidos evacuó en barcos fletados a unas 2.000 personas que se habían quedado varadas en el puerto.

Después de Camarioca vinieron los Vuelos de la Libertad, una vía mucho más ordenada.""")],
 ["FR-V001", "FR-V002", "FR-V006", "FR-V013", "FR-V011", "FR-V012"]),

(C, "perspectivas", [("¿Por qué Castro abrió Camarioca en 1965?", """Las fuentes que tenemos no recogen lo que Castro pensaba, solo lo que dijo él y lo que respondió Estados Unidos, así que conviene contarlo así.

La versión del gobierno cubano está en el discurso de Fidel Castro del 3 de octubre de 1965. Según ese discurso, Castro sostuvo que la política de su gobierno sobre la salida del país no había cambiado, que después de la Crisis de Octubre se seguía saliendo por España y México, y que Estados Unidos era el único responsable de que las vías normales estuvieran cerradas, para fomentar salidas clandestinas y peligrosas con fines de propaganda. También sostuvo que la salida de las clases privilegiadas era un hecho histórico en todas las revoluciones.

La respuesta de Estados Unidos llegó ese mismo día. Según el Departamento de Estado, el presidente Johnson declaró en la isla de la Libertad, en Nueva York, que quienes buscaran refugio en Estados Unidos lo encontrarían, y ordenó preparar una entrada ordenada, con prioridad para los familiares directos.

Un dato ayuda a entender el contexto: entre 1959 y el 1 de junio de 1965, la Guardia Costera de Estados Unidos había rescatado o ayudado a 6.862 cubanos que intentaban cruzar por mar. Las salidas peligrosas ya existían antes de Camarioca.

Por qué tomó Castro la decisión en ese momento es una pregunta que cada historiador responde a su manera.""")],
 ["FR-V004", "FR-V005", "FR-V003", "FR-V025"]),

(C, "hecho", [("¿Qué fueron los Vuelos de la Libertad?", """Los Vuelos de la Libertad fueron el puente aéreo entre Cuba y Estados Unidos que sustituyó a la salida por mar de Camarioca.

Tras negociar a través de la Embajada de Suiza en La Habana, Estados Unidos y Cuba intercambiaron notas el 6 de noviembre de 1965 y formalizaron un memorando de entendimiento: entre 3.000 y 4.000 cubanos saldrían cada mes en un puente aéreo pagado por Estados Unidos desde el aeropuerto de Varadero, sin límite de tiempo.

Los vuelos empezaron el 1 de diciembre de 1965, con dos vuelos al día, cinco días a la semana, desde Varadero hasta Miami. Solo en diciembre de 1965 llegaron 3.349 personas por esa vía, y para el 1 de diciembre de 1968 el puente aéreo ya había traído a 131.372 cubanos.

Hubo interrupciones. El Departamento de Estado anunció el 31 de agosto de 1971 que el puente aéreo se pararía durante varias semanas a partir del 1 de septiembre, y el número de vuelos restantes dependía de cuántos cubanos dejara salir su gobierno.

Sobre el total hay diferencias entre las fuentes: el Departamento de Estado da 260.737 refugiados hasta abril de 1973, pero otras fuentes dan cifras distintas.""")],
 ["FR-V008", "FR-V014", "FR-V015", "FR-V018", "FR-V016"]),

(C, "perspectivas", [("¿Cuántos cubanos llegaron en los Vuelos de la Libertad?", """Depende de la fuente, y la diferencia no es pequeña.

El Departamento de Estado da 260.737 refugiados hasta abril de 1973. El historiador Alex Larzelere da 260.561 en 3.049 vuelos, y Suiza, que negoció el puente aéreo y registró a cada persona que salió, habla de unos 260.000. Wikipedia da 297.318 en 3.048 vuelos. Y la ficha del Servicio de Parques Nacionales de Estados Unidos sobre la Torre de la Libertad habla de unos 175.000.

Las tres primeras cifras coinciden bastante, y una de ellas viene del país que llevó el registro, así que alrededor de 260.000 es la estimación con más respaldo. Las de 297.318 y 175.000 se alejan mucho, y conviene mencionarlas como lo que son: cifras que dan otras fuentes.

Hay además cifras intermedias que ayudan a ver el ritmo. Según el Departamento de Estado, para el 1 de diciembre de 1968 el puente aéreo había traído a 131.372 cubanos. Y según un informe del Contralor General de Estados Unidos de 1971, para ese año habían llegado por el puente aéreo unos 243.000, de un total de unos 600.000 refugiados cubanos desde 1959.

Si tienes que dar un solo número, lo más honesto es decir "unos 260.000, según el Departamento de Estado y Suiza".""")],
 ["FR-V016", "FR-V010", "FR-V015", "FR-V017"]),

(C, "contexto", [("Si Estados Unidos y Cuba no tenían relaciones, ¿quién negoció los vuelos?", """Suiza. Su embajador en La Habana actuó en nombre de Estados Unidos y fue quien hizo de intermediario.

El embajador suizo en Cuba, Emil A. Stadelhofer, negoció en nombre de Estados Unidos el puente aéreo con Cuba en 1965, y Suiza registró además a cada persona que salió del país por esa vía.

La negociación no fue sencilla. Según un memorando del asesor de seguridad nacional, McGeorge Bundy, al presidente Johnson del 14 de octubre de 1965, Estados Unidos quería limitar la salida a unas 3.000 personas al mes, mientras que Cuba prefería unas 12.000. Cuba anunció que no dejaría salir a los hombres en edad militar, de 15 a 26 años, y no quería que participara la Cruz Roja, sino Suiza.

El acuerdo se cerró el 6 de noviembre de 1965 con un memorando de entendimiento: entre 3.000 y 4.000 salidas al mes desde Varadero, sin límite de tiempo. Cuba quería incluir en el memorando la exclusión de los hombres en edad militar y de técnicos y profesionales; Estados Unidos se negó, y Cuba recogió en notas aparte su prohibición de que salieran los hombres en edad militar, ciertos técnicos y los presos políticos.""")],
 ["FR-V010", "FR-V007", "FR-V008", "FR-V009"]),

(C, "contexto", [("¿Por qué no dejaban salir a los muchachos jóvenes en los Vuelos de la Libertad?", """Por una condición que puso el gobierno cubano desde el principio de la negociación.

Según un memorando del asesor de seguridad nacional, McGeorge Bundy, al presidente Johnson del 14 de octubre de 1965, Cuba anunció que no dejaría salir a los hombres en edad militar, de 15 a 26 años.

Cuando se firmó el memorando de entendimiento del 6 de noviembre de 1965, Cuba quiso que esa exclusión apareciera en el texto, junto con la de técnicos y profesionales. Estados Unidos se negó a incluirla, así que Cuba recogió en notas aparte su prohibición de que salieran los hombres en edad militar, ciertos técnicos y los presos políticos.

Por eso, entre quienes llegaron en los Vuelos de la Libertad había proporcionalmente menos hombres jóvenes. Según Wikipedia, por las restricciones de salida había más mujeres y personas mayores que hombres en edad de trabajar.

En la práctica, eso podía separar a las familias: los padres podían salir, pero un hijo en edad militar tenía que quedarse.""")],
 ["FR-V007", "FR-V009", "FR-V022", "FR-V008"]),

(C, "humano", [("Mi abuela esperó años para salir en los Vuelos de la Libertad. ¿Por qué tardaba tanto?", """Lo que vivió tu abuela encaja con lo que cuentan las fuentes: había muchos más inscritos que plazas.

El memorando de entendimiento de 1965 fijaba entre 3.000 y 4.000 salidas al mes. Pero según un documento interno del Departamento de Estado de 1968, cuando empezó el puente aéreo varios cientos de miles de cubanos se inscribieron para salir. El gobierno cubano dejó de aceptar nuevas inscripciones en mayo de 1966, y en diciembre de 1968 todavía había miles en la lista de espera.

Además, el ritmo no dependía solo de los aviones. Cuando el Departamento de Estado anunció en 1971 una interrupción del puente aéreo, señaló que el número de vuelos restantes dependía de cuántos cubanos dejara salir su gobierno.

La espera tampoco era fácil. Según Wikipedia, quienes se inscribían para salir eran despedidos de sus trabajos y hostigados por los Comités de Defensa de la Revolución, y sus propiedades se confiscaban al salir. Ese dato lo da una sola fuente, así que conviene contarlo atribuido.

Si tu abuela está dispuesta, pregúntale cuánto esperó y qué pasó en esos años. Su relato vale más que cualquier cifra.""")],
 ["FR-V008", "FR-V019", "FR-V018", "FR-V020"]),

(C, "reformulacion", [("¿Es verdad que a los que pedían irse en los años sesenta los mandaban a campos de trabajo?", """Hay una fuente que lo recoge, pero conviene contarlo con precisión y atribuido.

Según Wikipedia, quienes se inscribían para salir en la época de los Vuelos de la Libertad eran despedidos de sus trabajos, considerados enemigos del Estado y hostigados por los Comités de Defensa de la Revolución; algunos fueron internados en campamentos lejos de sus familias, y sus propiedades se confiscaban al salir. Wikipedia añade que Castro llamaba "gusanos" a quienes se iban y decía que Cuba estaba mejor sin ellos.

Lo de las propiedades tiene más respaldo: según el historiador Alex Larzelere y la Guardia Costera de Estados Unidos, ya en Camarioca quienes salían tenían que dejar sus casas y propiedades al gobierno cubano.

Lo que no tenemos es una cifra de cuántas personas fueron enviadas a esos campamentos, ni una segunda fuente que describa cómo funcionaban. Así que lo correcto es decir que hay fuentes que lo afirman, no dar un número ni generalizar a todos los que se inscribieron.

Si en tu familia alguien pasó por eso, su testimonio es justamente el tipo de dato que ayudaría a completarlo.""")],
 ["FR-V020", "FR-V021", "FR-V013"]),

(C, "contexto", [("¿Quiénes llegaron en los Vuelos de la Libertad? ¿Eran como los primeros exiliados?", """No exactamente. Las fuentes describen un perfil distinto al de la primera ola.

Según Wikipedia, por las restricciones de salida, entre los refugiados de los Vuelos de la Libertad había más mujeres y personas mayores que hombres en edad de trabajar. Alrededor del 57 por ciento era de clase trabajadora, y los cubanos negros eran menos del 3 por ciento de los migrantes cubanos en Estados Unidos en 1970.

Las restricciones venían de Cuba: el gobierno cubano recogió en notas aparte al memorando de 1965 su prohibición de que salieran los hombres en edad militar, ciertos técnicos y los presos políticos.

El gobierno de Estados Unidos también notó el cambio. Según un informe del Contralor General de 1971, el nivel educativo y el dominio del inglés de los refugiados llegados desde que empezó el puente aéreo, en diciembre de 1965, eran menores que los de los anteriores, lo que reducía sus posibilidades de mantenerse por sí mismos.

En resumen, los Vuelos de la Libertad trajeron sobre todo mujeres y personas mayores, con mucho peso de la clase trabajadora.""")],
 ["FR-V022", "FR-V009", "FR-V023"]),

(C, "perspectivas", [("¿Qué dijeron Johnson y Castro en octubre de 1965 sobre la salida de cubanos?", """Los dos hablaron el mismo día, el 3 de octubre de 1965, y conviene oír a cada uno.

Según el Departamento de Estado, el presidente Johnson, en la firma de una ley de inmigración en la isla de la Libertad, en Nueva York, declaró al pueblo de Cuba que quienes buscaran refugio en Estados Unidos lo encontrarían. Ordenó preparar una entrada ordenada, con prioridad para los familiares directos.

Fidel Castro habló esa misma noche, en la presentación del Comité Central del Partido Comunista de Cuba. Según su discurso, sostuvo que la política de su gobierno sobre la salida del país no había cambiado, que después de la Crisis de Octubre se seguía saliendo por España y México, y que Estados Unidos era el único responsable de que las vías normales estuvieran cerradas, para fomentar salidas clandestinas y peligrosas con fines de propaganda.

En ese mismo discurso, Castro sostuvo que la salida de las clases privilegiadas era un hecho histórico en todas las revoluciones, y pidió a Johnson que permitiera a los cubanos que vivían en Estados Unidos viajar a Cuba para visitar a sus familiares.

A pesar del choque de discursos, un mes después los dos gobiernos firmaron, a través de Suiza, el acuerdo que dio origen a los Vuelos de la Libertad.""")],
 ["FR-V003", "FR-V004", "FR-V005", "FR-V008"]),

(C, "hecho", [("¿Cuánto le costó a Estados Unidos ayudar a los refugiados cubanos?", """Hay una cifra oficial de la época. Según un informe del Contralor General de Estados Unidos de 1971, el programa de refugiados cubanos había costado unos 730 millones de dólares, incluidas las estimaciones para los años fiscales 1971 y 1972.

Ese mismo informe da una idea del volumen: unos 600.000 refugiados cubanos habían llegado a Estados Unidos desde 1959, unos 243.000 de ellos por el puente aéreo.

El puente aéreo era una parte importante del programa. Los Vuelos de la Libertad empezaron el 1 de diciembre de 1965, con dos vuelos al día, cinco días a la semana, desde Varadero hasta Miami, y según el memorando de entendimiento de ese año los pagaba el gobierno de Estados Unidos.

El informe señala también que los refugiados llegados desde que empezó el puente aéreo tenían menor nivel educativo y menos dominio del inglés que los anteriores, lo que reducía sus posibilidades de mantenerse por sí mismos.""")],
 ["FR-V017", "FR-V014", "FR-V008", "FR-V023"]),

(C, "contexto", [("¿Qué tuvo que ver la Ley de Ajuste Cubano con los Vuelos de la Libertad?", """La Ley de Ajuste Cubano se aprobó en 1966, en plena época de los Vuelos de la Libertad, y resolvió un problema que esos vuelos hicieron más grande.

Según Wikipedia, los cubanos habían entrado como "parolees", con un permiso temporal, porque se suponía que volverían pronto a la isla. La Ley de Ajuste Cubano de 1966 cambió esa situación y les abrió una vía propia para obtener la residencia permanente.

El contexto ayuda a entender por qué hacía falta. Los Vuelos de la Libertad empezaron el 1 de diciembre de 1965 y, según un documento interno del Departamento de Estado de 1968, varios cientos de miles de cubanos se inscribieron para salir. Los vuelos salían de Varadero dos veces al día, cinco días a la semana, y para el 1 de diciembre de 1968 el puente aéreo ya había traído a 131.372 cubanos. Toda esa gente necesitaba una situación legal estable, y la ley se la dio.""")],
 ["FR-V024", "FR-V014", "FR-V019", "FR-V015"]),

(C, "hecho", [("¿Cómo se salía de Cuba entre 1962 y 1965, antes de Camarioca?", """Con mucha más dificultad. Después de la Crisis de Octubre, las vías que quedaban eran indirectas o peligrosas.

Según el discurso de Fidel Castro del 3 de octubre de 1965, en esos años se seguía saliendo por España y México. Es la versión del gobierno cubano, y no tenemos una cifra independiente de cuántos usaron esas rutas. Ese mismo día, según el Departamento de Estado, el presidente Johnson declaró que quienes buscaran refugio en Estados Unidos lo encontrarían.

La otra vía era el mar. Según la Guardia Costera de Estados Unidos, entre 1959 y el 1 de junio de 1965 había rescatado o ayudado a 6.862 cubanos que intentaban cruzar por mar; el primer rescate fue el 22 de julio de 1959, cerca de las Dry Tortugas.

Esa situación es la que cambió en el otoño de 1965. El 28 de septiembre Fidel Castro anunció que los exiliados podrían recoger a sus familiares en el puerto de Camarioca a partir del 10 de octubre, y poco después los dos gobiernos acordaron los Vuelos de la Libertad.""")],
 ["FR-V004", "FR-V003", "FR-V025", "FR-V001"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "Camarioca y Vuelos de la Libertad, lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
