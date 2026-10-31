"""
generar_lote2_camarioca.py — Segundo lote de ejemplos de Camarioca y los Vuelos de la Libertad (1965-1973).

Uso (desde E:\\vertex-exilio):
    python generar_lote2_camarioca.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_camarioca_vuelos.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_camarioca_lote2.jsonl con todos los ejemplos en estado 'pendiente'.

Usa sobre todo los fragmentos nuevos (FR-V027 a FR-V061): el informe del Contralor General de 1971, más
secciones de Wikipedia, el discurso de Castro del 3 de octubre de 1965, CubaNet y la Guardia Costera.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_camarioca_vuelos.jsonl")
DESTINO = Path("datos/borrador_camarioca_lote2.jsonl")
PREFIJO = "exi-v"
PRIMER_ID = 14

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

C, T = "camarioca_vuelos_libertad", "transversal"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(C, "hecho", [("¿Cómo funcionaba el puente aéreo de Varadero a Miami?", """El puente aéreo nació de un acuerdo entre Estados Unidos y Cuba. Tras negociar a través de la Embajada de Suiza en La Habana, los dos países intercambiaron notas el 6 de noviembre de 1965 y formalizaron un memorando de entendimiento: entre 3.000 y 4.000 cubanos saldrían cada mes en vuelos pagados por Estados Unidos desde el aeropuerto de Varadero, sin límite de tiempo.

Los Vuelos de la Libertad empezaron el 1 de diciembre de 1965, con dos vuelos al día, cinco días a la semana. Según el informe del Contralor General de Estados Unidos de 1971, Varadero está a unas 75 millas al este de La Habana y el trayecto hasta Miami era de unas 195 millas. Hasta el 31 de julio de 1971 el puente aéreo había traído a unos 243.000 refugiados, a un ritmo de unos 850 por semana.

Los vuelos tenían sus particularidades. Según el mismo informe, cada vuelo de ida y vuelta costaba 752 dólares al principio, los contratistas solo podían usar aviones de hélice, y no se había resuelto si el gobierno cubano permitiría usar reactores.

Al llegar, según Wikipedia, los refugiados eran procesados en la Torre de la Libertad, a la que se llamó 'la Ellis Island del Sur', y vivían temporalmente en unas casas instaladas en el Aeropuerto Internacional de Miami.

Según Wikipedia, el gobierno cubano suspendió los vuelos de mayo a diciembre de 1972, y el último aterrizó en Miami el 6 de abril de 1973.""")],
 ["FR-V008", "FR-V014", "FR-V029", "FR-V035", "FR-V046", "FR-V043"]),

(C, "contexto", [("¿Qué oficios tenían los cubanos que llegaron en los Vuelos de la Libertad?", """Según los registros del programa de refugiados, que recoge el informe del Contralor General de Estados Unidos de 1971, el perfil fue cambiando respecto a los primeros refugiados.

De los refugiados llegados por el puente aéreo entre diciembre de 1965 y julio de 1971, el 6,0 por ciento tenía ocupaciones profesionales, semiprofesionales o directivas, y esa proporción fue bajando: era del 7,1 por ciento en los primeros 20 meses y del 4,1 por ciento en el año hasta julio de 1971. El 11,3 por ciento era personal de oficina y ventas, y la gran mayoría, el 64,4 por ciento, eran estudiantes, niños y amas de casa.

El mismo informe dice que el nivel educativo y el dominio del inglés de los refugiados llegados desde que empezó el puente aéreo eran menores que los de los anteriores, lo que reducía sus posibilidades de mantenerse por sí mismos. Un estudio del Departamento de Salud, Educación y Bienestar de 1968, citado por el Contralor, encontró que entre los refugiados que recibían ayuda pública en cinco estados el 40 por ciento no había recibido ninguna educación, frente al 2 por ciento en 1965.

También hubo comerciantes. Según Wikipedia, durante la nacionalización de los pequeños negocios en la Ofensiva Revolucionaria, algunos pequeños comerciantes decidieron irse en el puente aéreo.

Hay que tener en cuenta que el estudio de 1968 habla solo de quienes recibían ayuda pública, no de todos los que llegaron.""")],
 ["FR-V034", "FR-V023", "FR-V033", "FR-V045"]),

(C, "humano", [("Mis bisabuelos llegaron ya mayores en los Vuelos de la Libertad. ¿Llegaba mucha gente mayor?", """Sí, bastante, y las cifras de la época lo muestran.

Según el informe del Contralor General de Estados Unidos de 1971, de los unos 243.000 refugiados llegados por el puente aéreo hasta julio de 1971, alrededor del 11 por ciento tenía más de 60 años al llegar y otro 10 por ciento tenía entre 50 y 60.

Una de las razones está en las reglas de salida. Cuba quería excluir del acuerdo de 1965 a los hombres en edad militar y a técnicos y profesionales; Estados Unidos se negó, y Cuba recogió en notas aparte su prohibición de que salieran los hombres en edad militar, ciertos técnicos y los presos políticos. Según Wikipedia, por esas restricciones de salida, entre los refugiados de los Vuelos de la Libertad había más mujeres y personas mayores que hombres en edad de trabajar.

El informe del Contralor también muestra cómo creció la necesidad de ayuda. Según ese informe, los refugiados registrados en el programa pasaron de unos 251.000 en 1967 a unos 475.000 estimados para 1972, y la proporción que recibía ayuda pública subió del 14 por ciento a un 21 por ciento estimado. Además, desde que empezó el puente aéreo unos tres de cada cuatro refugiados fueron reasentados fuera de Miami a los pocos días de llegar, sin las clases de inglés que habían recibido los anteriores.

Si en tu familia alguien recuerda adónde fueron tus bisabuelos al llegar y si se quedaron en Miami o los mandaron a otra ciudad, esa es una parte de la historia que vale la pena guardar.""")],
 ["FR-V032", "FR-V009", "FR-V022", "FR-V038", "FR-V031"]),

(C, "hecho", [("¿Por qué mandaban a los cubanos recién llegados a vivir fuera de Miami?", """Reasentar a los refugiados fuera de Miami fue una política desde el principio del programa federal, y con los Vuelos de la Libertad se hizo más rápido.

Según el informe del Contralor General de Estados Unidos de 1971, reasentarlos fue siempre un objetivo principal del programa. Lo hacían por contrato cuatro agencias voluntarias: la Conferencia Católica de Estados Unidos, el Church World Service, la United HIAS Service y el International Rescue Committee, con ayuda de iglesias, sinagogas y organizaciones cívicas de todos los estados.

La base legal venía de antes. Según el mismo informe, el programa se pagó con fondos de contingencia del presidente hasta junio de 1962, cuando la Ley de Asistencia a la Migración y a los Refugiados le dio autoridad permanente, que incluía pagar el reasentamiento fuera de Miami.

Con el puente aéreo, el ritmo cambió. Desde que empezó, unos tres de cada cuatro refugiados fueron reasentados a los pocos días de llegar, sin las clases de inglés ni la formación profesional que habían recibido los anteriores. Según el informe, los funcionarios lo hacían para reducir el impacto en Miami, aunque reconocían que eso aumentaba el número de reasentados que necesitaban ayuda pública.

El idioma pesaba mucho. Según un estudio de 1968 citado por el Contralor, entre los refugiados que recibían ayuda pública tenía empleo el 44 por ciento de los que hablaban inglés y solo el 24 por ciento de los que no lo hablaban.""")],
 ["FR-V030", "FR-V040", "FR-V031", "FR-V033"]),

(C, "reformulacion", [("Leí que más de un millón de cubanos se inscribió para salir en los Vuelos de la Libertad. ¿Es cierto?", """Es una de las cifras que circulan, pero no es la única, y las fuentes no coinciden.

El número de inscritos varía según la fuente. Un documento interno del Departamento de Estado de 1968 habla de que, cuando empezó el puente aéreo, varios cientos de miles de cubanos se inscribieron para salir. Wikipedia, en cambio, dice que en marzo de 1968 había más de un millón de personas en la lista de espera, y que una encuesta del Chicago Tribune de abril de 1966 encontró que casi dos millones de cubanos querían irse.

Fíjate en que no miden lo mismo: una cosa es cuántos se inscribieron, otra cuántos estaban en lista de espera en una fecha concreta y otra cuántos decían en una encuesta que querían irse.

Tampoco coincide cuándo se cerraron las inscripciones. El documento del Departamento de Estado dice que el gobierno cubano dejó de aceptar nuevas inscripciones en mayo de 1966, y Wikipedia dice que Castro dejó de aceptar solicitudes de visado de salida en mayo de 1969. Según el Departamento de Estado, en diciembre de 1968 todavía había miles en la lista de espera.

Así que lo más preciso es decir que la demanda para salir era grande y que la cifra exacta depende de la fuente. Decir 'más de un millón' sin aclarar que es la cifra de Wikipedia, y que el Departamento de Estado daba otra, es contar solo una parte.""")],
 ["FR-V041", "FR-V019", "FR-V042"]),

(C, "hecho", [("¿Cómo terminaron los Vuelos de la Libertad?", """Los vuelos no terminaron de golpe: hubo interrupciones antes del final.

El Departamento de Estado anunció el 31 de agosto de 1971 que el puente aéreo se interrumpiría durante varias semanas a partir del 1 de septiembre, y que el número de vuelos restantes dependía de cuántos cubanos dejara salir su gobierno. Según el informe del Contralor General de 1971, las autoridades cubanas explicaron que la interrupción era para terminar de tramitar las últimas listas de personas autorizadas a salir, y los funcionarios del programa calculaban que podían quedar entre 1.000 y 94.000.

Según Wikipedia, el gobierno cubano suspendió los vuelos de mayo a diciembre de 1972, y el último vuelo aterrizó en el Aeropuerto Internacional de Miami el 6 de abril de 1973.

Cuánta gente llegó en total depende de la fuente. El Departamento de Estado da 260.737 refugiados hasta abril de 1973; Larzelere, 260.561 en 3.049 vuelos; Suiza, unos 260.000; Wikipedia, 297.318 en 3.048 vuelos; y la ficha del Servicio de Parques Nacionales, unos 175.000.

Las fuentes que tenemos no explican del todo por qué terminó el programa en 1973, más allá de que el número de vuelos dependía de las listas que autorizaba el gobierno cubano.""")],
 ["FR-V018", "FR-V036", "FR-V043", "FR-V016"]),

(C, "perspectivas", [("¿Por qué Castro no quería que la Cruz Roja participara en la salida de cubanos en 1965?", """El tema de la Cruz Roja fue uno de los puntos de la negociación de 1965, y hay dos lados que contar.

Según un memorando del asesor de seguridad nacional, McGeorge Bundy, al presidente Johnson del 14 de octubre de 1965, Estados Unidos quería limitar la salida a unas 3.000 personas al mes, mientras que Cuba prefería unas 12.000. Cuba anunció también que no dejaría salir a los hombres en edad militar, de 15 a 26 años, y que no quería que participara la Cruz Roja, sino Suiza.

Fidel Castro explicó su posición en público. Según un discurso suyo de octubre de 1965, rechazó que hiciera falta la Cruz Roja, como había mencionado Johnson, y afirmó que bastaba con acordar los trámites con los representantes de la Embajada de Suiza, que representaban los intereses de Estados Unidos en Cuba.

Finalmente la negociación pasó por Suiza. El embajador suizo en Cuba, Emil A. Stadelhofer, negoció en nombre de Estados Unidos el puente aéreo, y Suiza registró a cada persona que salió del país por esa vía. Tras esa negociación, Estados Unidos y Cuba intercambiaron notas el 6 de noviembre de 1965 y formalizaron un memorando de entendimiento: entre 3.000 y 4.000 cubanos saldrían cada mes.

Las fuentes que tenemos recogen lo que dijo cada gobierno, pero no explican qué pensaba la propia Cruz Roja.""")],
 ["FR-V007", "FR-V054", "FR-V010", "FR-V008"]),

(C, "perspectivas", [("¿Camarioca fue una forma de Castro de presionar a Estados Unidos?", """Es lo que sostiene CubaNet, y el gobierno cubano lo explicó de otra manera.

Según CubaNet, Camarioca fue la primera vez que Fidel Castro usó la migración masiva como método de presión sobre Estados Unidos, y repitió la estrategia después con el Mariel y con la crisis de los balseros.

Castro dio su propia versión en un discurso de octubre de 1965. Según ese discurso, presentó su propuesta de abrir Camarioca como una respuesta a la situación de personas que, al suspenderse los vuelos entre Cuba y Miami, habían quedado con un pie en Cuba y otro en Estados Unidos. Sostuvo que la política de su gobierno sobre la salida del país no había cambiado y que Estados Unidos era el único responsable de que las vías normales estuvieran cerradas, para fomentar salidas clandestinas y peligrosas con fines de propaganda.

El gobierno de Estados Unidos respondió ese mismo día. Según el Departamento de Estado, en la firma de una ley de inmigración en Nueva York, el presidente Johnson declaró al pueblo de Cuba que quienes buscaran refugio en Estados Unidos lo encontrarían, y ordenó preparar una entrada ordenada, con prioridad para los familiares directos.

Que fuera o no una forma de presión es una interpretación. Las fuentes que tenemos muestran lo que dijo cada parte, pero no un documento interno del gobierno cubano que explique sus motivos.""")],
 ["FR-V058", "FR-V057", "FR-V004", "FR-V003"]),

(C, "hecho", [("¿Cuánto costaron los Vuelos de la Libertad?", """No hay una cifra única, porque las fuentes no miden lo mismo.

El costo varía según la fuente: Wikipedia da un presupuesto de unos 12 millones de dólares para todo el programa, y el informe del Contralor General de Estados Unidos de 1971 recoge unos 4,9 millones para el traslado de refugiados desde Cuba entre los años fiscales 1966 y 1972, con estimaciones para los dos últimos años. Una cifra abarca todo el programa y la otra solo una parte del periodo, así que no se pueden comparar directamente.

El informe del Contralor da también el precio de cada vuelo. Cada vuelo de ida y vuelta costaba 752 dólares el 1 de diciembre de 1965, 966 en el año fiscal 1970, 1.530 en el de 1971 y 1.675 en el de 1972. Los contratistas solo podían usar aviones de hélice, y no se había resuelto si el gobierno cubano permitiría usar reactores.

Para dar una idea del volumen: según el mismo informe, hasta el 31 de julio de 1971 el puente aéreo había traído a unos 243.000 refugiados, a un ritmo de unos 850 por semana, en un trayecto de unas 195 millas entre Varadero y Miami.""")],
 ["FR-V039", "FR-V035", "FR-V029"]),

(T, "contexto", [("¿Cómo recibió Miami a los cubanos de los Vuelos de la Libertad?", """La recepción tuvo dos caras: un sistema para acogerlos y, al mismo tiempo, rechazo por parte de algunos vecinos.

Al llegar, según Wikipedia, los refugiados eran procesados en la Torre de la Libertad, a la que se llamó 'la Ellis Island del Sur', y vivían temporalmente en unas casas instaladas en el Aeropuerto Internacional de Miami.

Pero no todos los recibieron bien. Según contó Luis Botifoll, citado por Wikipedia, algunos les tenían resentimiento porque hablaban español, hablaban alto y les quitaban trabajos, y recuerda carteles que decían 'No Pets, No Children, and No Cubans', es decir, que no se admitían mascotas, niños ni cubanos.

El idioma era otra barrera. Según Wikipedia, el inglés fue el único idioma oficial del condado de Dade hasta 1973, de modo que todos los documentos oficiales estaban solo en inglés, y en 1973 el condado pasó a ser oficialmente bilingüe.

La llegada cambió también la composición de la zona. Según Wikipedia, muchos estadounidenses blancos y judíos de Dade se mudaron al norte, a Broward y Palm Beach; Hialeah, casi totalmente anglosajona en 1960, sería décadas después hispana en un 96 por ciento.

Con el tiempo, Miami se convirtió en el centro del exilio. Según el sociólogo Juan Clark, citado por Wikipedia, los cubanos de los Vuelos de la Libertad convirtieron a Miami en el epicentro de todo el exilio cubano.""")],
 ["FR-V046", "FR-V047", "FR-V048", "FR-V049", "FR-V053"]),

(C, "humano", [("Mi abuelo decía que al principio en Miami nadie compraba muebles porque pensaban volver pronto a Cuba. ¿Era así?", """Lo que cuenta tu abuelo se parece a lo que recordaba otro exiliado de esa época, Luis Botifoll.

Según recuerda Botifoll, citado por Wikipedia, al principio todos pensaban solo en volver a Cuba: nadie quería comprometerse con un trabajo y vivían al día.

La situación legal reflejaba esa idea. Según Wikipedia, los cubanos habían entrado como 'parolees', con un permiso temporal, porque se suponía que volverían pronto a la isla. La Ley de Ajuste Cubano de 1966 cambió eso y les abrió una vía propia para obtener la residencia permanente.

Según Wikipedia, que resume un artículo de la Harvard Law Review de 2001, el trato preferente de esa ley respondió a cuatro razones: la política de la Guerra Fría, reducir trámites, motivos humanitarios y el aporte económico de los profesionales cubanos. Antes, un refugiado cubano tenía que salir de Estados Unidos, pedir un visado en un consulado en el extranjero y volver a entrar.

Desde La Habana también se hablaba de volver, pero de otra forma. Según un discurso de aquella época, Fidel Castro dijo que algún día gran parte de los que se habían ido querrían volver, arrepentidos, y que la idea de que regresaran como libertadores era un sueño.

Así que lo de tu abuelo encaja con lo que también contó Botifoll: la sensación de que el exilio sería corto. Si recuerda cuándo se dio cuenta de que no iba a ser así, esa parte de su historia vale mucho.""")],
 ["FR-V050", "FR-V024", "FR-V051", "FR-V056"]),

(C, "hecho", [("¿Cómo era cruzar el estrecho de la Florida antes de los Vuelos de la Libertad?", """Antes del puente aéreo, muchos cubanos cruzaron por mar, y la Guardia Costera de Estados Unidos dejó registro de esos rescates.

Antes de Camarioca, entre 1959 y el 1 de junio de 1965, la Guardia Costera había rescatado o ayudado a 6.862 cubanos que intentaban cruzar por mar; el primer rescate fue el 22 de julio de 1959, cerca de las Dry Tortugas. Según la Guardia Costera, a finales de agosto de 1965 el guardacostas Ariadne evacuó a 39 cubanos desde Cayo Sal, en las Bahamas, y en octubre de 1965 rescató a otros 36.

Hay historias que muestran hasta dónde llegaba la gente. Según la Guardia Costera, que cita un boletín de reasentamiento de febrero de 1967, Lauriano Ricoy y su esposa salieron de Cuba en un kayak metálico de 8 pies impulsado por un motor de cortadora de césped, pasaron cinco días en el estrecho y los recogió un guardacostas a unas 34 millas al este de Marathon; después se reasentaron en Nueva Orleans.

Luego llegó Camarioca. Según CubaNet, el primer grupo llegó a Cayo Marathón el 7 de octubre de 1965, y el corredor estuvo abierto 42 días. Cuba dejó de admitir barcos en Camarioca a partir del 28 de octubre y prohibió nuevas salidas desde allí el 4 de noviembre; entre el 13 y el 24 de noviembre Estados Unidos evacuó en barcos fletados a unas 2.000 personas que se habían quedado varadas.

Después llegaron los Vuelos de la Libertad, en diciembre de 1965.""")],
 ["FR-V025", "FR-V060", "FR-V061", "FR-V059", "FR-V011"]),

(C, "contexto", [("¿A cuántos refugiados cubanos atendió el programa federal hasta principios de los setenta?", """Las cifras del informe del Contralor General de Estados Unidos de 1971 dan una buena idea del tamaño del programa.

Según ese informe, de los unos 600.000 refugiados cubanos llegados a Estados Unidos desde 1959, unos 429.000 se habían registrado en el Centro de Emergencia para Refugiados Cubanos de Miami. Los registrados en el programa pasaron de unos 251.000 el 1 de julio de 1967 a unos 475.000 estimados para el 30 de junio de 1972, y la proporción que recibía ayuda pública, del 14 por ciento a un 21 por ciento estimado.

El programa tenía una base legal desde 1962. Según el informe, se pagó con fondos de contingencia del presidente hasta junio de ese año, cuando la Ley de Asistencia a la Migración y a los Refugiados le dio autoridad permanente: ayuda económica a refugiados necesitados, ayuda a agencias estatales y locales, pago del reasentamiento fuera de Miami y cursos de empleo y actualización profesional.

Una parte grande del gasto local fue en educación. Los pagos federales a las escuelas públicas del condado de Dade por los niños refugiados pasaron de 7 millones de dólares en el curso 1965-66 a unos 15,5 millones estimados para el curso 1971-72, y el número de alumnos cubiertos, de 16.673 a 22.100.

Son cifras de un informe oficial de Estados Unidos, con estimaciones para los últimos años; no hay en nuestras fuentes un recuento independiente para comparar.""")],
 ["FR-V028", "FR-V038", "FR-V040", "FR-V037"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "camarioca lote 2"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
