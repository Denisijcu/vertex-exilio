"""
generar_lote1_exodo_reciente.py — Primer lote de ejemplos del éxodo reciente (2017 en adelante), 17 ejemplos.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_exodo_reciente.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_exodo_reciente.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_exodo_reciente_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

El lote enseña a dar cifras recientes con su fecha y su fuente, a contar el 11J con la versión de cada
parte, a explicar el debate sobre las causas (embargo, crisis interna) sin tomar partido y a explicar
las vías legales que se abrieron y se cerraron entre 2022 y 2025.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_exodo_reciente.jsonl")
DESTINO = Path("datos/borrador_exodo_reciente_lote1.jsonl")
PREFIJO = "exi-r"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
X = "exodo_reciente"
E = [
(X, "hecho", [("¿Qué es el éxodo cubano de los últimos años?", """Es la ola de emigración que empezó alrededor de 2021 y que se considera la mayor emigración en la historia moderna de Cuba.

Las cifras lo muestran. En el año fiscal 2022 las autoridades de Estados Unidos registraron casi 225.000 encuentros con cubanos en la frontera con México y más de 6.000 intercepciones de cubanos en el mar, cifras que juntas superan las del Mariel en 1980 y la crisis de los balseros de 1994. Según WOLA, una organización de derechos humanos de Washington, casi 425.000 cubanos llegaron a Estados Unidos en los años fiscales 2022 y 2023, y otros 36.000 pidieron asilo en México.

El éxodo coincidió con una crisis económica grave en Cuba, con escasez de alimentos y medicinas, inflación y apagones frecuentes, y con las protestas del 11 de julio de 2021.

La forma de salir también cambió. En noviembre de 2021 Nicaragua eliminó el visado para los cubanos, lo que abrió una ruta aérea hasta Managua y de ahí por tierra hacia Estados Unidos. Y en enero de 2023 Estados Unidos abrió un programa de permiso humanitario (parole) para cubanos, haitianos y nicaragüenses, que se sumó al de venezolanos de octubre de 2022.""")],
 ["FR-R001", "FR-R002", "FR-R003", "FR-R008", "FR-R014", "FR-R024"]),

(X, "perspectivas", [("¿Por qué se están yendo tantos cubanos?", """Las fuentes coinciden en que hay una crisis; lo que se discute es quién tiene la culpa.

Lo que nadie niega es la situación: el éxodo coincidió con una crisis económica grave, con escasez de alimentos y medicinas, inflación y apagones frecuentes. Según Wikipedia, la economía cubana se contrajo un 10,9 % en 2020 y un 2 % en el primer semestre de 2021, por una combinación de factores: menos ayuda de Venezuela, el embargo y las sanciones de Estados Unidos (endurecidas en 2019) y la pandemia, que golpeó el turismo y las remesas.

El gobierno cubano atribuye las salidas masivas, según Wikipedia, al embargo de Estados Unidos y a su política de dar beneficios a los migrantes cubanos, incluso a los que llegan ilegalmente. Estados Unidos, según la misma fuente, culpó del éxodo a la incapacidad del gobierno cubano de garantizar servicios básicos como la electricidad.

Los académicos tampoco piensan igual. La historiadora Lillian Guerra atribuyó la escasez de alimentos a que el gobierno gastaba en hoteles e instalaciones turísticas, mientras que el economista Pavel Vidal sostuvo que tanto el embargo como la falta de reformas en Cuba causan problemas. Y Jorge Duany, director del Instituto de Investigaciones Cubanas de FIU, considera que la razón más inmediata del aumento fueron las protestas de julio de 2021.

Las fuentes no permiten aislar una sola causa; cada una pone el acento donde más le importa.""")],
 ["FR-R008", "FR-R009", "FR-R049", "FR-R048", "FR-R010", "FR-R011"]),

(X, "hecho", [("¿Qué pasó el 11 de julio de 2021 en Cuba?", """Ese día empezaron las mayores protestas contra el gobierno desde el Maleconazo de 1994.

El 11 de julio de 2021 hubo protestas en Cuba desencadenadas por la escasez de alimentos y medicinas y por la situación de la pandemia. Según Wikipedia, empezaron en San Antonio de los Baños y Palma Soriano, se extendieron a al menos 50 ciudades, y muchos manifestantes cantaban "Patria y Vida", canción cuyo título invierte el lema "Patria o Muerte".

Sobre las víctimas hay versiones distintas. Según Wikipedia, el Ministerio del Interior reconoció la muerte de un manifestante, Diubis Laurencio Tejeda, de 36 años, mientras que la organización opositora Cuba Decide estimó cinco muertos.

Con los detenidos pasa lo mismo: Human Rights Watch habla de unos 400 y Cubalex de más de 500, según Wikipedia; otro artículo de Wikipedia dice más de 700, y WOLA habla de cientos. Al menos 710 personas fueron acusadas de delitos, entre ellos sedición.

Las consecuencias se sintieron después. Según Wikipedia, algunos manifestantes recibieron largas penas de prisión en juicios que Amnistía Internacional, activistas y familiares criticaron como injustos; el gobierno levantó temporalmente límites a la importación de alimentos y medicinas, y Estados Unidos impuso nuevas sanciones a funcionarios cubanos.""")],
 ["FR-R037", "FR-R038", "FR-R040", "FR-R041", "FR-R042"]),

(X, "perspectivas", [("¿Cómo explicó cada lado las protestas del 11J?", """Cada parte contó el 11J a su manera, y vale la pena tener las dos versiones.

La versión del gobierno cubano: según Wikipedia, el presidente Miguel Díaz-Canel culpó de la situación al embargo y las sanciones de Estados Unidos, llamó por televisión a los partidarios del gobierno a salir a la calle a enfrentar las protestas, y el gobierno calificó las manifestaciones de contrarrevolucionarias. En general, el gobierno atribuyó la crisis económica al embargo y a su endurecimiento, y a los efectos de la pandemia.

Lo que recogen fuentes independientes es que las protestas tuvieron como detonante la escasez de alimentos y medicinas y la situación de la pandemia, y fueron las mayores desde el Maleconazo de 1994. Según Wikipedia, algunos manifestantes recibieron largas penas de prisión en juicios que Amnistía Internacional, activistas y familiares criticaron como injustos, y Estados Unidos impuso nuevas sanciones a funcionarios cubanos.

Entre los académicos también hay matices. Jorge Duany, de FIU, considera que la razón más inmediata del aumento de la emigración fueron las protestas de julio de 2021. Para él, el 11J no fue solo un hecho político, sino también el arranque de la gran ola migratoria.

Cómo se valore el 11J depende mucho de a qué versión se le dé más peso, y aquí se dan las dos.""")],
 ["FR-R039", "FR-R043", "FR-R037", "FR-R042", "FR-R011"]),

(X, "contexto", [("¿Cómo era la ruta por Nicaragua que usaron tantos cubanos?", """Fue la ruta principal de esos años, porque permitía evitar el mar y la selva del Darién.

En noviembre de 2021 Nicaragua eliminó el visado para los cubanos, lo que abrió una ruta aérea hasta Managua y de ahí por tierra hacia Estados Unidos. Según WOLA, con datos del Diálogo Interamericano, en 2023 hubo un promedio de 50 vuelos chárter al mes entre La Habana y Managua, que llevaron a unas 100.000 personas, y casi 77.000 pasaron por Honduras en los primeros once meses del año. Según Wikipedia, el viaje costaba a cada persona entre 8.000 y 10.000 dólares y causó varias muertes.

Sobre el papel de Nicaragua hay valoraciones. Según WOLA, en Managua el gobierno de Ortega y Murillo cobraba tarifas de entrada arbitrarias antes de dejar que redes de tráfico llevaran a los migrantes hasta Honduras. Según Wikipedia, algunos expertos especularon que Nicaragua podía estar usando a los migrantes para presionar a Estados Unidos a levantar sanciones.

La ruta se fue cerrando. Según WOLA, Costa Rica empezó a exigir visado de tránsito a los cubanos en febrero de 2022, Panamá y República Dominicana en marzo de 2022, y Jamaica y México en marzo y octubre de 2023. El 21 de noviembre de 2023 el Departamento de Estado anunció restricciones de visado contra aerolíneas que facilitaban vuelos chárter a Managua.""")],
 ["FR-R014", "FR-R015", "FR-R016", "FR-R017", "FR-R018", "FR-R020", "FR-R019"]),

(X, "hecho", [("¿Cuántos cubanos se han ido en esta última ola?", """Las cifras más citadas son de 2022 y 2023, y cada fuente cuenta algo un poco distinto, así que conviene darlas con su origen.

En el año fiscal 2022 las autoridades de Estados Unidos registraron casi 225.000 encuentros con cubanos en la frontera con México y más de 6.000 intercepciones en el mar. Según WOLA, casi 425.000 cubanos llegaron a Estados Unidos en los años fiscales 2022 y 2023, y otros 36.000 pidieron asilo en México, sin contar a los que se fueron a Brasil, Rusia, Uruguay y otros países.

El mes récord fue diciembre de 2022, con una pequeña diferencia entre fuentes: WOLA da 44.079 y Wikipedia da 44.064. Para todo el año calendario 2022, Wikipedia da unos 313.000 cubanos (313.488 en el texto del artículo y 313.499 en su tabla).

Por mar también hubo un aumento. Según WOLA, las 13.000 intercepciones y encuentros de cubanos en el mar en los años fiscales 2022 y 2023 son la mayor ola por mar desde 1994.

Sobre cuánta población perdió Cuba, las estimaciones no coinciden: WOLA calcula más del 4 %; Wikipedia da en un lugar casi el 8 % y en otro el 3,5 %. Es mejor no repetir una sola cifra como si fuera segura.""")],
 ["FR-R002", "FR-R003", "FR-R004", "FR-R005", "FR-R021", "FR-R006"]),

(X, "hecho", [("¿Qué era el parole humanitario para cubanos de 2023?", """Era un programa que permitía a algunos cubanos viajar legalmente a Estados Unidos en avión, en lugar de llegar por la frontera.

En enero de 2023 el Departamento de Seguridad Nacional abrió un programa de permiso humanitario (parole) para cubanos, haitianos y nicaragüenses, que se sumó al de venezolanos de octubre de 2022; el de cubanos empezó el 6 de enero de 2023. Según el Migration Policy Institute, permitía venir en avión a quienes tuvieran un patrocinador en Estados Unidos y vivir allí dos años, y admitía hasta 30.000 personas al mes de las cuatro nacionalidades.

Muchos lo usaron. Según el Migration Policy Institute, para finales de agosto de 2023 habían llegado más de 43.000 cubanos, y según WOLA, para diciembre de 2023 ya eran más de 50.000. Según el Registro Federal, entre octubre de 2022 y el 22 de enero de 2025 unas 532.000 personas de las cuatro nacionalidades juntas recibieron autorización para viajar.

El programa tenía otra cara. Según WOLA, desde enero de 2023 Estados Unidos aplicó con rigor el Título 42 para devolver a México a cubanos que llegaban a la frontera, y entre mayo y octubre de 2023 fueron devueltos a México 17.000 ciudadanos de Cuba, Haití, Nicaragua y Venezuela.""")],
 ["FR-R024", "FR-R025", "FR-R026", "FR-R027", "FR-R028"]),

(X, "contexto", [("¿Qué pasó con el parole humanitario en 2025?", """Se terminó. El cambio venía anunciándose desde antes.

Según el Registro Federal, el 4 de octubre de 2024, todavía bajo el gobierno de Biden, ya se había anunciado que no habría renovación del permiso al terminar los dos años iniciales. Luego, el Departamento de Seguridad Nacional dio por terminados los programas para cubanos, haitianos, nicaragüenses y venezolanos el 25 de marzo de 2025, y los permisos que no hubieran vencido terminaban el 24 de abril de 2025, salvo decisión individual en contra.

La razón oficial es la postura del gobierno de Trump. Según el Registro Federal, sostuvo que esos programas no lograron una mejora suficiente y duradera de la seguridad fronteriza y que dejaron dentro del país a una población grande sin una vía clara hacia un estatus estable; la orden ejecutiva 14165, del 20 de enero de 2025, había ordenado terminarlos.

El mismo documento da cifras de la frontera: en diciembre de 2022 la Patrulla Fronteriza encontró a unos 84.000 ciudadanos de Cuba, Haití, Nicaragua y Venezuela en la frontera suroeste, y desde junio de 2024 la cifra estuvo por debajo de 6.000 cada mes. En total, unas 532.000 personas de esas cuatro nacionalidades habían recibido autorización para viajar con el programa. Las fuentes que tenemos no recogen la valoración de los beneficiarios.""")],
 ["FR-R034", "FR-R033", "FR-R035", "FR-R036", "FR-R027"]),

(X, "hecho", [("¿Qué es el I-220A y por qué preocupa a tantos cubanos?", """Es un documento que se dio a muchos cubanos al soltarlos en la frontera, y en 2023 cambió lo que significaba para ellos.

Según WOLA, en septiembre de 2023 la Junta de Apelaciones de Inmigración decidió que el documento I-220A no equivale a una admisión legal, por lo que sus portadores no pueden pedir la residencia por la Ley de Ajuste Cubano, y miles quedaron en un limbo legal.

Para entender el tamaño del problema hay que ver cuántos llegaron. Según WOLA, desde el inicio del año fiscal 2022 hasta diciembre de 2023 las autoridades fronterizas registraron 442.977 encuentros con cubanos. No se sabe cuántos recibieron el I-220A y cuántos otro tipo de documento.

Hasta entonces, la mayoría había entrado por la vía ordinaria. Según Wikipedia, en 2022 México no permitía que Estados Unidos expulsara cubanos por la frontera terrestre bajo el Título 42 y Cuba no aceptaba vuelos de expulsión, de modo que cerca del 98 % de los cubanos detenidos en la frontera fueron procesados en Estados Unidos por la ley migratoria ordinaria.

Quien tenga un caso así debería consultar a un abogado de inmigración, porque la situación de cada persona depende de sus documentos.""")],
 ["FR-R031", "FR-R032", "FR-R029"]),

(X, "contexto", [("¿Por qué los cubanos tenían que ir a Guyana a sacar visas?", """Porque durante unos años la embajada de Estados Unidos en La Habana casi no daba servicios consulares.

En 2017 Estados Unidos redujo el personal de su embajada en La Habana tras los problemas de salud que afectaron a sus diplomáticos, suspendió los servicios consulares, y los cubanos tuvieron que viajar a Guyana para tramitar visas, un viaje caro. Según Wikipedia, por ese recorte Estados Unidos no pudo cumplir su compromiso de dar 20.000 visas de inmigrante al año a los cubanos.

El tema volvió a la mesa en 2022. Según el Departamento de Estado, el 21 de abril de 2022 delegaciones de los dos países se reunieron en Washington, en las primeras conversaciones migratorias desde 2018, y Estados Unidos anunció la reanudación limitada de visas de inmigrante a partir de mayo. Según Wikipedia, en esas conversaciones el gobierno cubano pidió cumplir el compromiso de las 20.000 visas, y Estados Unidos pidió a La Habana aceptar a los cubanos deportados.

En enero de 2023 la embajada en La Habana reanudó los servicios regulares de visas y consulares por primera vez en cinco años, y en mayo de 2022 Estados Unidos había anunciado la reanudación del programa de reunificación familiar para cubanos, creado en 2007 y suspendido en 2018.""")],
 ["FR-R012", "FR-R013", "FR-R044", "FR-R047", "FR-R023"]),

(X, "perspectivas", [("¿Qué dicen los gobiernos de Cuba y Estados Unidos en sus conversaciones migratorias?", """Los dos dicen querer una migración ordenada, pero cada uno pone el acento en algo distinto.

Las conversaciones se retomaron en 2022, en las primeras de ese tipo desde 2018. La fecha exacta varía según la fuente: WOLA dice que fueron el 14 de abril de 2022 y el comunicado del Departamento de Estado, el 21 de abril.

La posición de Estados Unidos: según el comunicado del Departamento de Estado, facilitar una migración segura, legal y ordenada era un interés común de los dos países y respondía al interés de Estados Unidos en la reunificación familiar y en un mayor respeto de los derechos humanos en Cuba. Según Wikipedia, en esas conversaciones Estados Unidos pidió a La Habana aceptar a los cubanos deportados por haber llegado ilegalmente, y el gobierno cubano pidió cumplir el compromiso de dar 20.000 visas de inmigrante al año.

La posición de Cuba se ve en la nota de su cancillería sobre una ronda posterior de conversaciones. Según la cancillería cubana, Cuba reafirmó que cumple los acuerdos y denunció que el embargo de Estados Unidos, endurecido en los últimos años, es un incentivo importante para emigrar, junto con la inclusión de Cuba en la lista de países patrocinadores del terrorismo, el trato preferente a los cubanos que entran ilegalmente y la Ley de Ajuste Cubano.

Las dos posiciones conviven en la mesa: una habla de derechos humanos y deportaciones, la otra de embargo y de la Ley de Ajuste.""")],
 ["FR-R044", "FR-R045", "FR-R046", "FR-R047", "FR-R050"]),

(X, "perspectivas", [("¿El embargo de Estados Unidos es la causa de la emigración cubana?", """Es una de las preguntas más discutidas, y las fuentes dan respuestas distintas.

El gobierno cubano dice que sí, en buena parte. Según Wikipedia, atribuye las salidas masivas al embargo de Estados Unidos y a su política de dar beneficios a los migrantes cubanos, incluso a los que llegan ilegalmente. Y según su cancillería, en una ronda posterior de conversaciones migratorias denunció que el embargo, endurecido en los últimos años, es un incentivo importante para emigrar.

Estados Unidos lo ve de otra manera. Según Wikipedia, culpó del éxodo a la incapacidad del gobierno cubano de garantizar servicios básicos como la electricidad.

WOLA, una organización de derechos humanos de Washington, tiene su propia posición: según WOLA, las restricciones del embargo que impiden a Cuba comprar a crédito agravaron el golpe económico de la pandemia, y en Estados Unidos hay poca voluntad política de revisar esas políticas.

Entre los académicos hay matices. La historiadora Lillian Guerra atribuyó la escasez de alimentos a que el gobierno gastaba en hoteles e instalaciones turísticas, y el economista Pavel Vidal sostuvo que tanto el embargo como la falta de reformas en Cuba causan problemas. Según Wikipedia, la contracción económica se explica por una combinación de factores: menos ayuda de Venezuela, el embargo y las sanciones, y la pandemia.

Es decir, hay quien pone el peso en el embargo y quien lo pone en la gestión interna; varias fuentes apuntan a una combinación de las dos cosas.""")],
 ["FR-R049", "FR-R050", "FR-R048", "FR-R052", "FR-R010", "FR-R009"]),

(X, "hecho", [("¿Estados Unidos sigue deportando cubanos a Cuba?", """Sí. Durante un tiempo casi no se podía, pero eso cambió a finales de 2022.

Según Wikipedia, en 2022 México no permitía que Estados Unidos expulsara cubanos por la frontera terrestre bajo el Título 42 y Cuba no aceptaba vuelos de expulsión, de modo que cerca del 98 % de los cubanos detenidos en la frontera fueron procesados en Estados Unidos por la ley migratoria ordinaria. En las conversaciones de abril de 2022, según Wikipedia, Estados Unidos ya había pedido a La Habana aceptar a los cubanos deportados.

En noviembre de 2022 Cuba aceptó recibir vuelos de deportación desde Estados Unidos. Según WOLA, los vuelos se reanudaron el 24 de abril de 2023, siguieron una vez al mes y para diciembre de 2023 habían devuelto a 386 cubanos.

Además, hubo devoluciones a México. Según WOLA, desde enero de 2023 Estados Unidos aplicó con rigor el Título 42 para devolver a México a cubanos que llegaban a la frontera, y tras el fin de esa norma en mayo de 2023 siguió devolviéndolos gracias a un acuerdo con México; entre mayo y octubre de 2023 fueron devueltos a México 17.000 ciudadanos de Cuba, Haití, Nicaragua y Venezuela.""")],
 ["FR-R029", "FR-R047", "FR-R030", "FR-R028"]),

(X, "contexto", [("¿Cuántos cubanos viven en Estados Unidos y dónde?", """Los datos más completos que tenemos son de 2021, del censo estadounidense, recogidos por el Migration Policy Institute.

Según el Migration Policy Institute, en 2021 vivían en Estados Unidos cerca de 1,3 millones de inmigrantes cubanos. En el período 2017-2021 el 76 % vivía en la Florida, el 52 % solo en el condado de Miami-Dade, y una de cada ocho personas del área de Miami había nacido en Cuba.

Si se cuenta a los hijos y nietos, la cifra es mayor: en 2021 unos 2,7 millones de residentes en Estados Unidos habían nacido en Cuba o declaraban ascendencia cubana, y 1,4 millones de ellos (el 52 %) habían nacido en Estados Unidos.

Algunos rasgos de los inmigrantes cubanos en 2021: la edad mediana era de 55 años, el 66 % eran ciudadanos estadounidenses, el ingreso mediano de sus hogares era de 52.000 dólares, frente a unos 70.000 del conjunto de inmigrantes, y el 16 % vivía en la pobreza. En el año fiscal 2022 obtuvieron la residencia permanente 36.600 cubanos, el 40 % por una vía humanitaria.

Estos datos son anteriores a buena parte del éxodo reciente, así que la cifra actual seguramente es mayor.""")],
 ["FR-R054", "FR-R055", "FR-R056", "FR-R057"]),

(X, "humano", [("Me fui por Nicaragua en 2022 y mi mamá se quedó sola en Cuba. A veces siento culpa. ¿Fue un error irme?", """Lo que sientes es muy común entre quienes se fueron en estos años, y no tiene una respuesta única. Lo que sí puedo hacer es darte algo de contexto.

No te fuiste solo. En noviembre de 2021 Nicaragua eliminó el visado para los cubanos, y por esa ruta salieron muchísimas personas. En el año fiscal 2022 las autoridades de Estados Unidos registraron casi 225.000 encuentros con cubanos en la frontera con México. Según Wikipedia, los demógrafos Juan Carlos Albizu-Campos y Sergio Díaz-Briquets calculan que cerca del 80 % de los que emigraron en 2022 tenía entre 15 y 59 años: gente en edad de trabajar, como tú, que muchas veces deja atrás a padres mayores.

Las razones eran reales. El éxodo coincidió con una crisis económica grave en Cuba, con escasez de alimentos y medicinas, inflación y apagones frecuentes. Según WOLA, funcionarios cubanos llegaron a advertir de apagones de 8 a 10 horas diarias.

Si fue un error o no, solo lo puedes valorar tú, con lo que sabías y lo que vivías entonces. Muchas personas en tu situación encuentran alivio en mantener el contacto frecuente con quien se quedó, y en hablar de esto con otros cubanos que pasaron por lo mismo. Si la culpa te pesa mucho, hablarlo con un profesional también puede ayudar.""")],
 ["FR-R014", "FR-R002", "FR-R007", "FR-R008", "FR-R053"]),

(X, "contexto", [("¿A qué otros países se van los cubanos, además de Estados Unidos?", """Estados Unidos es el destino principal, pero no el único.

Según el Migration Policy Institute, con estimaciones de la ONU de 2020, después de Estados Unidos los principales destinos de los cubanos en el exterior eran España (162.000), Italia (39.000), Chile (24.000) y Canadá (19.000).

En la ola reciente también aparecen otros destinos. Según WOLA, además de los casi 425.000 cubanos que llegaron a Estados Unidos en los años fiscales 2022 y 2023, otros 36.000 pidieron asilo en México entre enero de 2022 y noviembre de 2023, y hay que sumar a los que se fueron a Brasil, Rusia, Uruguay y otros países, sin una cifra exacta.

Las rutas cambian según las reglas de visado de cada país. Según WOLA, Costa Rica empezó a exigir visado de tránsito a los cubanos en febrero de 2022, Panamá y República Dominicana en marzo de 2022, y Jamaica y México en marzo y octubre de 2023, mientras que Guyana seguía sin pedir visado.""")],
 ["FR-R058", "FR-R003", "FR-R020"]),

(X, "hecho", [("¿Todavía salen balseros de Cuba?", """Sí, aunque en esta última ola la mayoría salió por tierra y por aire.

Según WOLA, las 13.000 intercepciones y encuentros de cubanos en el mar en los años fiscales 2022 y 2023 son la mayor ola por mar desde la crisis de los balseros de 1994, aunque mucho menor que la llegada por tierra y aire. Solo en el año fiscal 2022 hubo más de 6.000 intercepciones de cubanos en el mar, frente a casi 225.000 encuentros en la frontera con México. Según Wikipedia, entre octubre de 2021 y diciembre de 2022 llegaron por mar 9.164 migrantes cubanos.

La diferencia con 1994 es la ruta. En noviembre de 2021 Nicaragua eliminó el visado para los cubanos, lo que abrió una ruta aérea hasta Managua y de ahí por tierra hacia Estados Unidos, que evitaba el mar y la selva del Darién. Por eso, aunque el número de balseros fue el más alto en casi tres décadas, la mayor parte del éxodo no fue por el estrecho de la Florida.""")],
 ["FR-R021", "FR-R002", "FR-R022", "FR-R014"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "Éxodo reciente, lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
