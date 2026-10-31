"""
generar_lote3_transversal.py — Tercer lote de ejemplos transversales: historia y leyes del embargo, el debate
sobre mantenerlo o levantarlo, propiedades confiscadas, misiones médicas, remesas y Venezuela.

Uso (desde E:\\vertex-exilio):
    python generar_lote3_transversal.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_transversal.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_transversal_lote3.jsonl con todos los ejemplos en estado 'pendiente'.

Usa sobre todo FR-T075 a FR-T095 (informe CRS R45657 de 2020), combinados con fragmentos de 2026.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_transversal.jsonl")
DESTINO = Path("datos/borrador_transversal_lote3.jsonl")
PREFIJO = "exi-t"
PRIMER_ID = 26

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "transversal"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "hecho", [("¿Cuándo y cómo empezó el embargo de Estados Unidos a Cuba?", """El embargo se fue armando por pasos a principios de los años sesenta, y hasta la fecha de inicio se cuenta de dos maneras.

Según el Servicio de Investigación del Congreso de Estados Unidos, el presidente Kennedy proclamó el embargo comercial a Cuba en febrero de 1962, con base en la Ley de Asistencia Exterior de 1961. En marzo de 1962 se amplió con la Ley de Comercio con el Enemigo, y en julio de 1963 el Tesoro aprobó el Reglamento de Control de Activos Cubanos, que prohíbe la mayoría de las transacciones financieras con Cuba, congela los activos del gobierno cubano en Estados Unidos y sigue siendo el núcleo del embargo.

La fecha varía según la fuente: el Servicio de Investigación del Congreso sitúa la proclamación del embargo comercial en febrero de 1962, mientras que Noticias ONU dice que Estados Unidos lo mantiene desde 1960. Las fuentes que tenemos no explican de dónde sale la diferencia.

Las relaciones diplomáticas también se rompieron en esos años. Según el mismo informe del Congreso, se rompieron en enero de 1961 y no se restablecieron hasta julio de 2015, durante el gobierno de Obama.

Así que, más que una sola decisión, el embargo fue una serie de medidas entre 1960 y 1963 que después el Congreso reforzó con nuevas leyes.""")],
 ["FR-T075", "FR-T076", "FR-T080"]),

(T, "hecho", [("¿Qué es la Ley Helms-Burton?", """Es la ley de 1996 que convirtió el embargo de Estados Unidos a Cuba en ley permanente, y una de las más criticadas fuera de Estados Unidos.

Según el Servicio de Investigación del Congreso, la Ley Helms-Burton, cuyo nombre oficial es LIBERTAD, se aprobó en 1996 tras el derribo de las avionetas de Hermanos al Rescate. Convirtió el embargo en ley permanente, de modo que el presidente no puede levantarlo sin el Congreso hasta que se cumplan ciertas condiciones democráticas.

Antes ya existía la Ley para la Democracia Cubana de 1992, que, según el mismo informe, prohibió a las filiales de empresas estadounidenses en el extranjero comerciar con Cuba y a los barcos que hubieran comerciado con Cuba en los 180 días anteriores cargar o descargar en Estados Unidos sin licencia.

Una de sus partes más polémicas es el Título III, que permite demandar a quienes usan propiedades confiscadas en Cuba. Según el Servicio de Investigación del Congreso, desde mayo de 2019 se presentaron unas 25 demandas bajo ese título, y la Unión Europea y Canadá criticaron la medida.

La ONU también la menciona. Según Noticias ONU, la resolución anual contra el embargo expresa preocupación por la Ley Helms-Burton de 1996 por sus efectos extraterritoriales sobre otros países.

En resumen: para sus defensores es la garantía de que el embargo no se levante sin cambios en Cuba; para sus críticos, una ley que también castiga a terceros países.""")],
 ["FR-T077", "FR-T086", "FR-T048"]),

(T, "reformulacion", [("Si hay embargo, ¿cómo es que Cuba le compra pollo a Estados Unidos?", """Es una buena pregunta, y la respuesta es que el embargo tiene excepciones desde hace décadas.

Según el Servicio de Investigación del Congreso, desde principios de los años noventa se permiten exportaciones médicas a Cuba con verificación sobre el terreno de su uso, y la ley de 2000 conocida como TSRA autorizó las exportaciones agrícolas. Pero con condiciones: prohíbe la ayuda y el crédito privado estadounidenses y exige pago en efectivo por adelantado o financiación de terceros países.

Con esas reglas el comercio ha sido grande. Según el mismo informe, Cuba compró 6.300 millones de dólares en productos estadounidenses entre 2001 y 2019, sobre todo agrícolas; las exportaciones pasaron de unos 7 millones en 2001 a un máximo de 712 millones en 2008 y fueron de 287 millones en 2019, cuando el pollo supuso el 66 %. Durante muchos años Estados Unidos fue el principal proveedor de productos agrícolas de Cuba.

Ese es uno de los argumentos del gobierno de Estados Unidos. Según Noticias ONU, en 2026 su embajador Mike Waltz afirmó 'No hay bloqueo' y citó más de 876 millones de dólares en exportaciones estadounidenses a Cuba en ocho meses de 2026.

Lo que sí está prohibido es venderle a crédito: la obligación de pagar en efectivo y por adelantado es una de las restricciones que mantiene el embargo, aunque se permita vender comida y medicinas.""")],
 ["FR-T078", "FR-T079", "FR-T049"]),

(T, "perspectivas", [("¿Habría que levantar el embargo a Cuba o mantenerlo?", """Es una de las discusiones más antiguas de la política hacia Cuba, y hay argumentos serios de los dos lados.

Según el Servicio de Investigación del Congreso de Estados Unidos, quienes defienden flexibilizar las sanciones sostienen que más viajes, comercio y diálogo sembrarían reformas en Cuba, que hay que evitar un cambio violento y un éxodo masivo, y que casi 60 años de sanciones no han hecho caer al gobierno cubano. Señalan también el amplio rechazo internacional al embargo, las oportunidades perdidas para las empresas estadounidenses y el sufrimiento que causa al pueblo cubano.

Quienes se oponen a levantarlo, según el mismo informe, sostienen que aislar al gobierno cubano mientras se apoya al pueblo es la mejor vía para el cambio, que suavizar la política sin reformas concretas ayuda a ese gobierno a sobrevivir, que las sanciones pueden funcionar y que las condiciones de vida en Cuba se deben a las fallidas políticas económicas del gobierno cubano y no al embargo.

La opinión del exilio también se ha movido. Según el informe, la mayoría de los estadounidenses apoya normalizar las relaciones, pero entre los cubanoamericanos del sur de la Florida una encuesta de la FIU de 2018 encontró que el 51 % quería mantener el embargo y el 49 % se oponía, frente a 2016, cuando el 63 % quería terminarlo.

Un estudio de 2016 de la Comisión de Comercio Internacional de Estados Unidos aporta un matiz: según el informe, concluyó que limitan el comercio tanto las restricciones estadounidenses como las barreras cubanas, como el control estatal del comercio.

No hay una respuesta que las fuentes den por buena: es una decisión política sobre la que la gente, incluso dentro del exilio, está dividida.""")],
 ["FR-T082", "FR-T083", "FR-T084", "FR-T085"]),

(T, "hecho", [("¿Qué cambió Obama en la relación con Cuba y qué pasó después?", """Obama abrió un acercamiento que duró poco: el gobierno siguiente dio marcha atrás en buena parte.

Según el Servicio de Investigación del Congreso, en diciembre de 2014 el gobierno de Obama giró hacia el acercamiento: en mayo de 2015 sacó a Cuba de la lista de patrocinadores del terrorismo, en julio de 2015 restableció las relaciones diplomáticas, rotas en enero de 1961, y en 2015 y 2016 flexibilizó los viajes, las remesas y el comercio. Obama visitó Cuba en marzo de 2016.

Ese giro se notó en la ONU. En 2015 y 2017 la resolución contra el embargo tuvo su máximo apoyo, con 191 votos a favor y 2 en contra, y en 2016 Estados Unidos se abstuvo por primera vez.

Luego vino el cambio. Según el mismo informe, desde 2017 el primer gobierno de Trump prohibió las transacciones con empresas controladas por los militares cubanos, como el conglomerado GAESA, una lista de 223 entidades entre ellas 109 hoteles. En 2019 eliminó los viajes educativos y los cruceros, limitó los vuelos a La Habana, fijó un tope a las remesas familiares, permitió las demandas por propiedades confiscadas y sancionó el envío de petróleo venezolano a Cuba.

Así que el deshielo fue un paréntesis de unos dos años dentro de una política de sanciones que viene de los años sesenta.""")],
 ["FR-T080", "FR-T047", "FR-T081"]),

(T, "perspectivas", [("¿Qué pasa con las propiedades que confiscó el gobierno cubano después de 1959?", """Es uno de los temas pendientes entre los dos países, y cada gobierno hace cuentas distintas.

Según el Servicio de Investigación del Congreso de Estados Unidos, una comisión del Departamento de Justicia certificó 5.913 reclamaciones por propiedades estadounidenses expropiadas en Cuba, valoradas en 1.900 millones de dólares, unos 8.000 millones con intereses.

El gobierno cubano no acepta esas cuentas. Según el mismo informe, no reconoce la valoración estadounidense, propone usar el valor fiscal declarado de las propiedades, de casi 1.000 millones de dólares, y sostiene que cualquier negociación debe tener en cuenta las pérdidas que le causó el embargo, que estimaba en 134.500 millones de dólares a precios de 2018. Esa última cifra es una estimación del gobierno cubano.

La Ley Helms-Burton añadió una vía judicial. Según el informe, desde mayo de 2019 se presentaron unas 25 demandas bajo su Título III contra quienes usan propiedades confiscadas, y la Unión Europea y Canadá criticaron la medida. Esa misma ley convirtió el embargo en ley permanente, de modo que el presidente no puede levantarlo sin el Congreso hasta que se cumplan ciertas condiciones democráticas.

Así que, para Estados Unidos, la compensación es una de las condiciones para normalizar; para el gobierno cubano, debe negociarse junto con lo que considera daños del embargo.""")],
 ["FR-T086", "FR-T087", "FR-T077"]),

(T, "perspectivas", [("¿Las misiones médicas cubanas en el exterior son trabajo forzado?", """Hay acusaciones serias y una defensa oficial, y conviene conocer las dos con sus datos.

Primero, el tamaño. Según el Servicio de Investigación del Congreso de Estados Unidos, que cita estadísticas del gobierno cubano, la exportación de servicios de salud generó 6.400 millones de dólares en 2018 y fue la mayor fuente de divisas del país. Casi 30.000 profesionales cubanos trabajaban en 72 países, gratis o al costo en 47 y con beneficio en 27. En Brasil, entre 2013 y 2018, los médicos recibían el 25 % de lo que Brasil pagaba a Cuba, y Cuba retiró a más de 8.000 cuando el nuevo gobierno brasileño exigió pagarles directamente.

Los críticos hablan de explotación. Según el mismo informe, el secretario general de la OEA, Luis Almagro, las llama una forma de esclavitud moderna; el grupo Cuban Prisoners Defenders, con datos de más de 100 participantes, afirma que al 41 % le retuvieron el pasaporte y que más de la mitad dijo que la misión no fue voluntaria. En 2019 el Departamento de Estado bajó a Cuba al nivel 3 en su informe sobre trata de personas.

El gobierno cubano lo niega. Según el informe, una declaración de la cancillería cubana de diciembre de 2019 sostiene que los profesionales participan 'absolutamente por voluntad propia', que siguen cobrando su salario completo en Cuba más un estipendio, y que lo que Cuba cobra sostiene su sistema de salud y las misiones gratuitas en otros países.

Lo que muestran los datos de Brasil es que el Estado cubano se quedaba con la mayor parte de lo que se pagaba por cada médico; si eso es trabajo forzado es justo lo que está en disputa.""")],
 ["FR-T092", "FR-T093", "FR-T094"]),

(T, "reformulacion", [("En 2019 Cuba decía que en Venezuela casi todos eran médicos. ¿Qué se supo después?", """Lo que se supo después contradice esa versión, al menos en parte.

En 2019 esa era la posición oficial. Según el Servicio de Investigación del Congreso de Estados Unidos, funcionarios cubanos afirmaban entonces que la gran mayoría del personal cubano en Venezuela era personal médico. Del otro lado, en marzo de 2019 Pompeo afirmó que los servicios militares y de inteligencia cubanos daban protección física a Maduro.

Las cifras de entonces eran muy dispares: el asesor de seguridad nacional John Bolton habló de 20.000 a 25.000 efectivos de seguridad cubanos, expertos regionales dijeron que la cifra probablemente era mucho menor, y Pompeo habló de 2.300. Según Factchequeado, no hay un conteo definitivo.

La negativa siguió hasta 2024. Según Factchequeado, el 19 de diciembre de 2024 el viceministro Carlos Fernández de Cossío dijo que 'no hay tropas. Cuba no participa en operaciones militares ni en operaciones de seguridad en Venezuela'.

Y en 2026 llegó el reconocimiento. El 4 de enero de 2026 el gobierno cubano confirmó que 32 cubanos, miembros de las Fuerzas Armadas Revolucionarias y del Ministerio del Interior, murieron durante la operación militar de Estados Unidos del 3 de enero en Venezuela, donde cumplían misiones 'a solicitud de órganos homólogos' venezolanos.

Así que la afirmación de 2019 no se sostiene del todo: puede que la mayoría del personal cubano fuera médico, pero había militares y agentes del Ministerio del Interior en tareas de seguridad, algo que La Habana negó hasta que reconoció sus muertos.""")],
 ["FR-T090", "FR-T091", "FR-T089", "FR-T069", "FR-T067"]),

(T, "hecho", [("¿Qué pasó con la embajada de Estados Unidos en La Habana?", """La embajada reabrió con el deshielo de Obama, pero pocos años después quedó casi sin personal, y eso afectó a los cubanos que querían emigrar legalmente.

Según el Servicio de Investigación del Congreso de Estados Unidos, en julio de 2015 el gobierno de Obama restableció las relaciones diplomáticas con Cuba, rotas en enero de 1961.

Poco después empezaron los problemas. Según el mismo informe, entre noviembre de 2016 y mayo de 2018 26 personas de la comunidad de la embajada sufrieron lesiones sin explicar. En septiembre de 2017 Estados Unidos redujo en dos tercios el personal de la embajada, lo que afectó sobre todo a la tramitación de visas, y en octubre ordenó la salida de 15 diplomáticos cubanos de Washington. Cuba niega cualquier responsabilidad en esas lesiones.

Para los cubanos eso tuvo un costo directo: con la embajada casi sin personal, tramitar una visa se volvió mucho más difícil.

Las causas de las lesiones siguen siendo un punto de desacuerdo entre los dos gobiernos: Estados Unidos redujo su presencia por esos incidentes, y Cuba rechaza haber tenido algo que ver.""")],
 ["FR-T080", "FR-T095"]),

(T, "humano", [("Mi familia en Miami dice que ahora es más difícil mandarnos dinero a Cuba. ¿Siempre hubo límites a las remesas?", """No siempre han sido iguales: los límites a las remesas han subido y bajado según el gobierno de turno en Washington.

Con Obama se aflojaron. Según el Servicio de Investigación del Congreso de Estados Unidos, en 2015 y 2016 su gobierno flexibilizó los viajes, las remesas y el comercio con Cuba.

Con el primer gobierno de Trump se endurecieron. Según el mismo informe, en 2019 se fijó un tope de 1.000 dólares por trimestre a las remesas familiares, junto con otras medidas como eliminar los viajes educativos y limitar los vuelos a La Habana.

Y desde 2025 la tendencia volvió a ser de más restricciones. Según el Servicio de Investigación del Congreso, desde enero de 2025 el gobierno de Trump ordenó endurecer las normas sobre viajes y remesas, con el objetivo declarado de promover la democracia, los derechos humanos y la economía de mercado en Cuba.

Las fuentes que tenemos no detallan las reglas exactas que rigen hoy, que además pueden cambiar. Si tu familia quiere estar segura de cuánto y cómo puede enviar, lo mejor es consultar a la empresa de envíos o a un abogado especializado.

Sé que para muchas familias esas remesas son lo que permite resolver el día a día en Cuba, así que entiendo la preocupación.""")],
 ["FR-T080", "FR-T081", "FR-T056"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "transversal lote 3 (historia del embargo)"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
