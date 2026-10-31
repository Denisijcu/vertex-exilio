"""
generar_piloto_mariel.py — Lote piloto de 15 ejemplos de entrenamiento sobre el Mariel.

Uso (desde E:\\vertex-exilio):
    python generar_piloto_mariel.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_mariel.jsonl y se niega a
usar fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_mariel.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_mariel.jsonl")
DESTINO = Path("datos/borrador_mariel.jsonl")

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

E = [
("hecho", "¿Qué fue el éxodo del Mariel?", ["FR-M006", "FR-M007", "FR-M009", "FR-M010", "FR-M011", "FR-M019"],
"""El éxodo del Mariel fue la salida masiva de cubanos por mar desde el puerto de Mariel hacia la Florida, en 1980. En algo más de seis meses llegaron a Estados Unidos alrededor de 125.000 personas, y fue la mayor migración de cubanos hacia ese país en un solo episodio.

Arrancó el 20 de abril de 1980, cuando el gobierno cubano anunció que quien tuviera a alguien que fuera a recogerlo en barco podía irse por Mariel. La respuesta en la Florida fue inmediata: entre abril y octubre alrededor de 1.700 embarcaciones, en su mayoría organizadas por cubanos de la Florida, hicieron el viaje. El 21 de abril ya habían llegado a Cayo Hueso las primeras, entre ellas la Dos Hermanos y la Blanche III, con 48 refugiados.

El momento de más llegadas fue mayo de 1980, con 86.488 personas, el 69 por ciento de todas las que entraron por el Mariel.

Sobre el final, las fuentes no coinciden del todo. Según el historiador Alex Larzelere, el gobierno cubano cerró el puerto el 25 de septiembre de 1980 y ordenó salir a los barcos, tras 159 días. Según National Archives y otras fuentes, el éxodo terminó formalmente en octubre de 1980, con un acuerdo entre los dos gobiernos. Es probable que se refieran a momentos distintos: el cierre del puerto y el fin oficial.

Detrás de esas cifras hay miles de historias personales, y por eso el Mariel ocupa un lugar central en la memoria del exilio cubano."""),

("contexto", "¿Cómo empezó todo? ¿Qué pasó en la embajada del Perú?", ["FR-M001", "FR-M002", "FR-M003", "FR-M004", "FR-M005"],
"""El Mariel empezó en la embajada del Perú en La Habana, unas semanas antes.

El 1 de abril de 1980 seis cubanos entraron a la fuerza en los terrenos de la embajada en un autobús. En el incidente murió un guardia cubano, Pedro Ortiz Cabrera, alcanzado por una bala de rebote. Tres días después, el 4 de abril, el gobierno cubano retiró la custodia de la embajada y dejó el acceso abierto.

Lo que pasó entonces sorprendió a todo el mundo. En muy poco tiempo entró una multitud que quería salir del país: para el 6 de abril había más de 10.000 personas dentro. El historiador Alex Larzelere habla de 10.856 personas en apenas 38 horas. Ese mismo día el gobierno volvió a cerrar la zona, y quienes estaban dentro se quedaron esperando una salida.

La crisis se volvió internacional. El 14 de abril el presidente Carter autorizó admitir hasta 3.500 cubanos al amparo de la Ley de Refugiados de 1980. El 16 de abril empezaron vuelos de evacuación hacia San José, Costa Rica, pero el gobierno cubano los suspendió a los dos días, cuando habían salido 678 personas.

Con miles de personas en la embajada y una salida que se había cerrado casi enseguida, la situación necesitaba una válvula de escape. Esa válvula fue el puerto de Mariel, que el gobierno cubano abrió pocos días después. Por eso, para entender el Mariel, hay que empezar por aquellos días de abril en la embajada del Perú."""),

("perspectivas", "¿Cómo explicó el gobierno cubano el Mariel y cómo lo vieron los demás?", ["FR-M027", "FR-M028", "FR-M026", "FR-M017", "FR-M020", "FR-M009"],
"""El Mariel se contó de maneras muy distintas según quién lo contara, y conviene separar lo que cada parte afirmó de lo que se ha podido documentar.

Según el discurso que Fidel Castro pronunció en mayo de 1980, el gobierno cubano abrió Mariel como respuesta a los incidentes de la embajada del Perú y a las salidas organizadas desde la Florida, y responsabilizó a Estados Unidos y a la CIA de alentar el desorden. En ese mismo discurso, Castro describió a la mayoría de quienes se iban como "lumpen" y elementos antisociales. Durante el éxodo, la prensa estatal cubana calificó públicamente a los emigrantes con términos despectivos.

Del lado de Estados Unidos también hubo un discurso político. Según la cronología del historiador Alex Larzelere, el 7 de junio de 1980 la Casa Blanca denunció que el gobierno cubano estaba enviando "criminales endurecidos" sacados de sus cárceles.

Las dos afirmaciones apuntan a lo mismo: presentar a los emigrantes como delincuentes. Lo que dicen los datos es otra cosa. Según las cifras que recoge Wikipedia, unos 2.746 recién llegados, el 2,2 por ciento, fueron clasificados como delincuentes graves bajo la ley estadounidense. La historiadora María Cristina García calcula que cerca del 4 por ciento estuvo involucrado en situaciones delictivas, y otros investigadores señalan que muchos antecedentes eran por delitos menores, como la venta en el mercado negro.

Del lado del exilio, el Mariel se vivió como una movilización de la comunidad: alrededor de 1.700 embarcaciones, en su mayoría organizadas por cubanos de la Florida, cruzaron el estrecho para recoger a quienes querían salir. Cada parte tuvo su versión; los números permiten ver cuánto se ajustaba cada una a lo que realmente pasó."""),

("reformulacion", "¿Es verdad que en el Mariel Fidel vació las cárceles y que los marielitos eran delincuentes?", ["FR-M020", "FR-M028", "FR-M017", "FR-M042", "FR-M041"],
"""Esa idea se repite mucho, pero los datos no la sostienen. Es cierto que entre los que salieron hubo personas con antecedentes penales; lo que no es cierto es que fueran la mayoría.

Según las cifras que recoge Wikipedia, unos 2.746 recién llegados, el 2,2 por ciento, fueron clasificados como delincuentes graves bajo la ley estadounidense. La historiadora María Cristina García calcula que cerca del 4 por ciento estuvo involucrado en situaciones delictivas. Investigadores señalan además que muchos de esos antecedentes eran por delitos menores, como la venta en el mercado negro. Hubo estimaciones mucho más altas, como una periodística de 1985 que llegó a hablar de 16.000 a 20.000, pero las fuentes serias coinciden en una proporción pequeña.

¿De dónde salió entonces la imagen del marielito delincuente? En parte, de los dos gobiernos. En un discurso de esos meses, Fidel Castro describió a la mayoría de los que se iban como "lumpen" y elementos antisociales. Y según la cronología de Alex Larzelere, el 7 de junio de 1980 la Casa Blanca denunció que Cuba estaba enviando "criminales endurecidos". Después vino el cine: la película Scarface, de 1983, ayudó a fijar un estereotipo que acompañó a los marielitos durante años.

Según Poorman, en un artículo de la American Historical Association, más de la mitad de los que llegaron alcanzaron la clase media. Así que la respuesta corta es que no: hubo personas con antecedentes, pero según los datos disponibles la gran mayoría de los marielitos no tenía antecedentes graves."""),

("humano", "¿Qué eran los actos de repudio?", ["FR-M025", "FR-M030", "FR-M031", "FR-M032", "FR-M039"],
"""Los actos de repudio fueron una de las experiencias más duras para quienes decidieron irse por el Mariel, y para muchos la última imagen que se llevaron de Cuba.

Eran concentraciones contra las personas que querían salir del país. Turbas que se reunían frente a sus casas, las golpeaban, les colgaban carteles acusatorios y destrozaban sus viviendas. No eran estallidos espontáneos: según la historiadora Lillian Guerra, los organizaban los Comités de Defensa de la Revolución, incluida su dirección nacional, junto con escuelas y organizaciones de masas, y muchos maestros llevaban a sus aulas completas.

Empezaron cerca de la embajada del Perú y, desde abril y durante todo el verano de 1980, pasaron a las casas de quienes pedían permiso de salida. A menudo se repetían una y otra vez hasta el día en que la familia se iba. De noche pintaban las viviendas con insultos como "traidores" y "ratas".

Tampoco era fácil negarse a participar. Quienes se oponían también podían ser castigados: Guerra documenta el caso de Ariel Hidalgo, que terminó internado en un hospital psiquiátrico y después en prisión.

Para entender lo que eso significaba en la vida de una familia, sirve el testimonio de José Manuel García, que salió por el Mariel siendo niño y con los años se doctoró en literatura latinoamericana. García recuerda que en su casa temían los actos de repudio de los vecinos mientras esperaban la salida. Su testimonio es uno entre muchos, y por eso es importante sumar más voces de quienes lo vivieron."""),

("humano", "¿Cómo fue la travesía para la gente que salió?", ["FR-M040", "FR-M015", "FR-M008", "FR-M007"],
"""El viaje de Mariel a la Florida es corto en el mapa, pero para muchos fue una de las noches más largas de su vida.

En el puerto se juntaron muchísimos barcos. Hacia el 25 de abril de 1980 había entre 300 y 400 embarcaciones en Mariel esperando para recoger gente, según el historiador Alex Larzelere.

El testimonio de José Manuel García da una idea de lo que se vivió. Según contó, el primer barco de su familia empezó a hacer agua al poco de salir. Los rescató un camaronero en el que iban unas 200 personas hacinadas, sin poder dormir, hasta que apareció un barco de la Guardia Costera.

No todos tuvieron esa suerte. El 17 de mayo de 1980 se hundió al norte de Mariel la embarcación Olo Yumi, sobrecargada con 52 personas. Murieron 14, y la Guardia Costera rescató a 38.

Al otro lado esperaba Cayo Hueso, adonde el 21 de abril habían llegado las primeras embarcaciones, entre ellas la Dos Hermanos y la Blanche III, con 48 refugiados. Para quienes llegaban, aquello era el final de la travesía y el principio de otra historia: la de empezar de nuevo en otro país."""),

("contexto", "¿Cómo respondió Estados Unidos al Mariel?", ["FR-M004", "FR-M013", "FR-M014", "FR-M016", "FR-M018", "FR-M021"],
"""La respuesta de Estados Unidos fue cambiando sobre la marcha, a medida que crecían las llegadas.

Al principio, la idea era acoger a un número limitado. El 14 de abril de 1980 el presidente Carter autorizó admitir hasta 3.500 cubanos al amparo de la Ley de Refugiados de 1980. Pero en cuanto se abrió Mariel, las cifras se dispararon.

En la Florida la presión se sintió enseguida. A la semana de empezar las llegadas, el gobernador Bob Graham declaró el estado de emergencia en los condados de Monroe y Dade. El 6 de mayo de 1980 el gobierno federal declaró también la emergencia en el estado y destinó 10 millones de dólares en fondos para refugiados.

El discurso político también cambió en pocas semanas. En mayo de 1980 Carter habló primero de recibir a los cubanos con los brazos abiertos, y el 14 de mayo anunció un programa de cinco puntos para poner fin al éxodo.

Quedaba resolver la situación legal de los que ya estaban en el país. El 20 de junio de 1980 Estados Unidos creó el estatus de "Cuban-Haitian Entrant", distinto del de refugiado. La solución definitiva llegó años después: en 1984, una revisión de la Ley de Ajuste Cubano de 1966 permitió a los cubanos del Mariel obtener la residencia permanente. Los haitianos que llegaron en esas mismas fechas no recibieron ese beneficio."""),

("perspectivas", "¿Cuánta gente había en la embajada del Perú? He leído cifras muy distintas.", ["FR-M003", "FR-M033", "FR-M036"],
"""Es normal que te encuentres cifras distintas, porque ese número fue también parte de la batalla política del momento.

Las fuentes independientes coinciden en que entraron más de 10.000 personas. El historiador Alex Larzelere, que hizo una cronología muy detallada del Mariel, da 10.856 personas en apenas 38 horas, y en otra parte de su texto 10.865. Otros recuentos hablan de unas 10.800. Las diferencias entre esas cifras son mínimas.

La cifra que no encaja es la oficial cubana. Según la historiadora Lillian Guerra, el periódico Granma informó que en la embajada había 1.470 personas. Es decir, menos de la séptima parte de lo que documentan las demás fuentes. No es un error de cuentas pequeño: la diferencia redujo en la prensa oficial la magnitud de lo que estaba pasando.

No fue el único caso. Durante las marchas que el gobierno cubano organizó en esas semanas, Granma publicó fotos de calles de La Habana vacías y las presentó como prueba de que todo el pueblo estaba apoyando al gobierno.

Por eso, cuando cuentes este episodio, lo más honesto es decir que entraron más de 10.000 personas, según las fuentes independientes, y que la prensa oficial cubana dio en su momento una cifra mucho menor. Así queda claro qué dijo cada uno y qué se pudo comprobar."""),

("hecho", "¿Cuándo terminó el Mariel?", ["FR-M019", "FR-M011", "FR-M010"],
"""Depende de qué entiendas por terminar, porque las fuentes dan dos fechas y las dos tienen sentido.

Según el historiador Alex Larzelere, el gobierno cubano cerró el puerto de Mariel el 25 de septiembre de 1980 y ordenó salir a los barcos que quedaban, después de 159 días de éxodo. Esa fecha marca el momento en que dejaron de salir embarcaciones.

Según National Archives y Wikipedia, en cambio, el Mariel terminó en octubre de 1980, tras un acuerdo entre los gobiernos de Estados Unidos y Cuba. Esa fecha se refiere más bien al cierre formal del episodio entre los dos países.

Lo más probable es que no se contradigan, sino que hablen de dos cosas distintas: el cierre del puerto y el fin oficial. Por eso lo más preciso es decir que el éxodo se extendió de abril a septiembre u octubre de 1980, según cómo se cuente.

Lo que sí está claro es cuándo fue lo más intenso. Mayo de 1980 fue el mes de más llegadas, con 86.488 personas, el 69 por ciento de todas las que entraron por el Mariel. A partir de ahí el ritmo bajó, pero no se detuvo hasta el final.

En total, en algo más de seis meses llegaron a Estados Unidos alrededor de 125.000 cubanos. Para tener una idea de la magnitud: fue la mayor migración de cubanos hacia ese país en un solo episodio."""),

("contexto", "¿Qué pasó con los marielitos después de llegar?", ["FR-M021", "FR-M022", "FR-M023", "FR-M024", "FR-M041"],
"""Llegar no fue el final de la historia. Para muchos marielitos, los primeros años en Estados Unidos fueron casi tan difíciles como la salida.

Una parte de los recién llegados quedó en centros de detención. En el de Fort Chaffee, en Arkansas, hubo disturbios entre los detenidos, y el episodio se cita incluso como un factor en la derrota electoral del gobernador Bill Clinton en 1980.

La situación legal tardó en resolverse. En 1984 una revisión de la Ley de Ajuste Cubano de 1966 permitió a los cubanos del Mariel obtener la residencia permanente. Los que tenían antecedentes graves, en cambio, quedaron en un limbo. El acuerdo migratorio de 1987 entre Estados Unidos y Cuba permitió deportar a ciertos marielitos y fue seguido de motines en las prisiones de Oakdale y Atlanta. Décadas después, para junio de 2016, todavía quedaban 478 marielitos que no podían ser admitidos bajo la ley migratoria estadounidense, y Estados Unidos planeaba deportar, de acuerdo con el gobierno cubano, a un número pequeño de ellos considerados delincuentes graves.

A eso se sumó el estigma. La prensa estadounidense exageró la delincuencia y la película Scarface, de 1983, ayudó a fijar estereotipos que no se correspondían con la realidad de la mayoría.

Aun así, la mayoría salió adelante. Según Poorman, más de la mitad de los marielitos llegó a la clase media. Hoy los marielitos son parte de la historia de la comunidad cubana en Estados Unidos, aunque el estigma les haya pesado durante años."""),

("perspectivas", "¿El Mariel afectó los salarios en Miami?", ["FR-M029", "FR-M011"],
"""Es una de las preguntas más estudiadas de la economía de la migración, y los economistas todavía no se ponen de acuerdo del todo.

El punto de partida es la magnitud del fenómeno: en algo más de seis meses de 1980 llegaron alrededor de 125.000 cubanos, y la fuerza laboral de Miami creció de golpe. Para los economistas fue como un experimento natural.

El primero en estudiarlo a fondo fue el economista David Card, que concluyó que el efecto en los salarios de Miami fue marginal. Un estudio del gobierno de Estados Unidos de 1997, citado por National Archives, va en la misma línea: afirma que la fuerza laboral de Miami creció un 7 por ciento sin afectar de forma notable a los trabajadores nativos.

En 2016, el economista George Borjas volvió sobre los mismos datos y llegó a otra conclusión: según él, los salarios de un grupo de trabajadores nativos poco calificados bajaron alrededor de un 20 por ciento. Después, los investigadores Clemens y Hunt atribuyeron ese resultado a cambios en la muestra de la encuesta que usó Borjas.

Así que la respuesta honesta es que la mayoría de los estudios encuentran un efecto pequeño o nulo, pero hay un debate académico abierto sobre si algún grupo concreto salió perjudicado. Por eso el Mariel se sigue citando en cualquier debate serio sobre cómo afecta la inmigración a los salarios."""),

("reformulacion", "¿Los marielitos fueron unos traidores que abandonaron su patria?", ["FR-M026", "FR-M028", "FR-M031", "FR-M038", "FR-M030", "FR-M006"],
"""Esa forma de verlo tiene un origen concreto: fue el lenguaje oficial de la época. Vale la pena explicar de dónde viene antes de responder.

Durante el éxodo, la prensa estatal cubana calificó públicamente a quienes se iban con términos despectivos. En un discurso de esos meses, Fidel Castro describió a la mayoría de los que se iban como "lumpen" y elementos antisociales. El gobierno incluso difundió el testimonio de un agente infiltrado entre los que pidieron asilo en la embajada del Perú, que los describía como "escoria", y lo exhibió en fotomurales en la antigua sede de la embajada.

Ese lenguaje llegó a la calle. En los actos de repudio, que según la historiadora Lillian Guerra organizaban los Comités de Defensa de la Revolución junto con escuelas y organizaciones de masas, se pintaban las casas de quienes pedían salir con insultos como "traidores" y "ratas".

Usar la palabra "traidor" es un juicio político, no un hecho, y aquí no nos toca darlo. Lo que sí se puede decir con hechos es que salieron por un puerto que el propio gobierno cubano abrió: el 20 de abril de 1980 anunció que quien tuviera a alguien que fuera a recogerlo en barco podía irse por Mariel.

Si te interesa entender por qué se fueron, la pregunta más útil no es si eran "traidores", sino qué los llevó a meterse en un bote. Ahí cada historia es distinta, y vale la pena escucharlas."""),

("humano", "¿Qué pasó con los haitianos que llegaron en esa época?", ["FR-M012", "FR-M018", "FR-M021"],
"""Es una parte del Mariel de la que se habla poco, y merece contarse.

En los mismos meses en que llegaban los cubanos desde Mariel, también llegaban a la Florida migrantes haitianos, según Wikipedia unos 25.000. Su llegada coincidió en el tiempo con la de los cubanos.

Al principio, el gobierno de Estados Unidos los trató de forma parecida. El 20 de junio de 1980 creó el estatus de "Cuban-Haitian Entrant", que, como dice su nombre, se aplicaba a cubanos y haitianos por igual y era distinto del de refugiado. Durante un tiempo, ambos grupos quedaron en la misma situación legal provisional.

La diferencia llegó después. En 1984 una revisión de la Ley de Ajuste Cubano de 1966 permitió a los cubanos del Mariel obtener la residencia permanente. Esa ley era específica para cubanos, así que los haitianos llegados en esas mismas fechas no recibieron ese beneficio.

Por eso, cuando se habla del Mariel como un éxito de integración, conviene recordar que no todos los que llegaron en esa época tuvieron las mismas oportunidades. La diferencia no estuvo en cómo llegaron ni en cuándo, sino en el país del que venían y en la ley que les tocó.

Es un detalle que ayuda a ver el Mariel con más perspectiva: fue una historia cubana, pero no solo cubana."""),

("contexto", "¿Qué papel tuvieron las marchas que organizó el gobierno cubano?", ["FR-M035", "FR-M036", "FR-M034", "FR-M030"],
"""Mientras miles de personas buscaban irse, el gobierno cubano organizó una respuesta pública de gran escala para mostrar que el país lo respaldaba.

En 1980 se celebraron tres Marchas del Pueblo Combatiente: el 19 de abril, el 1 de mayo y el 17 de mayo. En ellas participaron escuelas, Comités de Defensa de la Revolución y organizaciones de masas. La del 19 de abril tuvo un significado especial, porque pasó por delante de la embajada del Perú, donde seguían miles de personas esperando salir.

La prensa oficial acompañó esas marchas con su propia narrativa. Según la historiadora Lillian Guerra, Granma publicó fotos de calles de La Habana vacías durante las marchas y las presentó como prueba de que todo el pueblo estaba con el gobierno. Según Granma, citado por Guerra, en la calzada de Carlos III se celebró además un mitin de repudio de unas 100.000 personas, y Guerra señala que reuniones parecidas se hacían en toda la isla casi cada noche. Esa cifra de 100.000 es la que dio el periódico oficial; no hay un recuento independiente que la confirme.

Las marchas y los actos de repudio tenían algo en común: según Guerra, los organizaban las mismas estructuras, los CDR, las escuelas y las organizaciones de masas.

Para la prensa oficial, eran la prueba del apoyo popular. Contarlas sirve para entender que el Mariel no solo se vivió en los barcos, sino también en las calles de Cuba."""),

("hecho", "¿Murió gente durante el Mariel?", ["FR-M015", "FR-M001", "FR-M040"],
"""Sí, aunque en las fuentes que hemos revisado no hay una cifra total confiable de muertos durante todo el éxodo, así que conviene hablar de los casos documentados y no inventar un número.

El episodio más grave registrado ocurrió en el mar. El 17 de mayo de 1980 se hundió al norte de Mariel la embarcación Olo Yumi, que iba sobrecargada con 52 personas. Murieron 14, y la Guardia Costera rescató a 38.

Otras travesías estuvieron cerca de terminar igual. José Manuel García, que salió de niño, contó que el primer barco de su familia empezó a hacer agua al poco de salir, y que los rescató un camaronero en el que iban unas 200 personas hacinadas, hasta que apareció la Guardia Costera.

Antes incluso de que empezara el éxodo hubo una muerte que marcó el comienzo de todo. El 1 de abril de 1980, cuando seis cubanos entraron a la fuerza en un autobús en la embajada del Perú en La Habana, murió un guardia cubano, Pedro Ortiz Cabrera, alcanzado por una bala de rebote.

Si buscas una cifra total, lo más honesto es decir que no la tenemos documentada aquí. Es un dato que habría que buscar en los registros de la Guardia Costera de Estados Unidos antes de darlo por bueno."""),
]

if DESTINO.exists():
    with DESTINO.open(encoding="utf-8-sig") as f:
        revisados = [json.loads(l)["id"] for l in f if l.strip() and json.loads(l).get("estado_revision") != "pendiente"]
    if revisados:
        print(f"{DESTINO} ya tiene {len(revisados)} ejemplos revisados ({', '.join(revisados[:5])}...). No lo sobrescribo.")
        sys.exit(1)

usados = sorted({x for _, _, ids, _ in E for x in ids})
faltan = [x for x in usados if x not in frag]
no_aprobados = [x for x in usados if x in frag and frag[x].get("estado") != "aprobado"]
if faltan or no_aprobados:
    print(f"No genero nada. Fragmentos que no existen: {faltan}. Fragmentos sin aprobar: {no_aprobados}.")
    sys.exit(1)

DESTINO.parent.mkdir(exist_ok=True)
with DESTINO.open("w", encoding="utf-8", newline="\n") as f:
    for i, (tipo, preg, ids, resp) in enumerate(E, 1):
        ej = {"id": f"exi-m{i:03d}", "etapa": "mariel_1980", "tipo": tipo,
              "messages": [{"role": "user", "content": preg}, {"role": "assistant", "content": resp.strip()}],
              "fuentes": [{"id_fragmento": x, "id_fuente": frag[x]["id_fuente"], "fragmento": frag[x]["texto"]} for x in ids],
              "estado_revision": "pendiente", "revisor": "", "notas": "Lote piloto"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
