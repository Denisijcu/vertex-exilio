"""
generar_lote1_balseros.py — Primer lote de ejemplos de la crisis de los balseros de 1994-1995 (15 ejemplos).

Uso (desde E:\\vertex-exilio):
    python generar_lote1_balseros.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_balseros_1994.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_balseros_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

El lote enseña a contar el Maleconazo con las tres versiones de su origen, a manejar cifras que no
coinciden (cuántos llegaron a Guantánamo), a poner frente a frente dos juicios opuestos sobre los
campamentos y a explicar los acuerdos migratorios de 1994 y 1995.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_balseros_1994.jsonl")
DESTINO = Path("datos/borrador_balseros_lote1.jsonl")
PREFIJO = "exi-b"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
B = "balseros_1994"
E = [
(B, "hecho", [("¿Qué fue la crisis de los balseros de 1994?", """Fue la salida masiva de cubanos por mar, en balsas y embarcaciones improvisadas, durante el verano de 1994.

Las salidas venían subiendo desde antes: de unos pocos cientos en 1989 a unos pocos miles en 1993. El 5 de agosto de 1994 estallaron disturbios en La Habana, en la zona del Malecón, el episodio conocido como el Maleconazo. Según Siro del Castillo, en una ponencia en FIU, el 13 de agosto de 1994 Fidel Castro anunció que se retirarían los guardafronteras de las costas y que podría irse del país cualquier persona que quisiera.

La respuesta de Estados Unidos llegó el 19 de agosto de 1994. El presidente Clinton anunció que la Guardia Costera ya no llevaría a Estados Unidos a los balseros interceptados en el mar, sino a la base naval de Guantánamo, lo que invirtió una política de unas tres décadas de acoger a los cubanos que huían.

Cuántos terminaron en Guantánamo depende de la fuente: Siro del Castillo da 32.362 interceptados entre agosto y septiembre de 1994; la GAO, la oficina de auditoría del Congreso, habla de unos 33.000; Wikipedia dice que unos 20.000 quedaron detenidos en la base.

La crisis se cerró con un acuerdo. El 9 de septiembre de 1994 Estados Unidos y Cuba firmaron un acuerdo migratorio: Estados Unidos admitiría al menos 20.000 inmigrantes cubanos al año, y Cuba se comprometió a impedir las salidas inseguras usando principalmente métodos persuasivos.""")],
 ["FR-B001", "FR-B012", "FR-B021", "FR-B024", "FR-B027", "FR-B041"]),

(B, "perspectivas", [("¿Qué provocó el Maleconazo?", """Que hubo disturbios en La Habana el 5 de agosto de 1994, en la zona del Malecón, lo confirman fuentes distintas. Lo que no coincide es cómo empezó, y aquí hay tres versiones.

Según la GAO, la oficina de auditoría del Congreso de Estados Unidos, el disturbio empezó cuando la policía intentó dispersar a una multitud que se había reunido por un rumor falso de que una flotilla de barcos venía a recoger a quienes quisieran irse.

Según Wikipedia, ese día las autoridades descubrieron una vía de salida ilegal que usaban muchos cubanos, cerraron el paso por el Malecón para impedir las salidas y la gente salió a la calle a protestar.

La versión del gobierno cubano está en EcuRed, su enciclopedia oficial. Según EcuRed, todo empezó después de que Radio Martí anunciara que venían barcos a La Habana a recoger a quienes se reunieran en el Malecón; al no llegar ningún barco, la gente apedreó comercios y agredió a personas, entre ellas policías.

Las tres versiones no se excluyen del todo: dos hablan de gente que esperaba barcos que no llegaron. Lo que cambia es quién originó la noticia y qué papel tuvo la policía.

En lo que sí hay coincidencia es en el ambiente de esos meses. Según Wikipedia, durante el Maleconazo se rompieron vidrieras y se saquearon tiendas, los manifestantes gritaron "¡Libertad!" y "¡Abajo los Castro!", y fue el mayor desafío público al gobierno desde 1959.""")],
 ["FR-B012", "FR-B013", "FR-B014", "FR-B015", "FR-B016"]),

(B, "hecho", [("¿Cómo terminó el Maleconazo? ¿Hubo detenidos?", """Sí. Lo que se sabe de cómo terminó viene sobre todo de Wikipedia, así que conviene leerlo con esa atribución.

Según Wikipedia, a los manifestantes los enfrentaron policías armados, agentes de la Seguridad del Estado y paramilitares, y varios videos y testimonios muestran a esas fuerzas disparando y golpeando a manifestantes. La misma fuente dice que el Maleconazo dejó unos 370 arrestos registrados y 30 heridos, 11 de ellos policías, y que los disturbios se calmaron por la tarde, cuando Fidel Castro llegó a la zona.

La versión oficial cubana pone el foco en otro lado. Según EcuRed, la gente apedreó comercios y agredió a personas, entre ellas policías. Y según Wikipedia, Fidel Castro culpó de los problemas de Cuba a Estados Unidos, citando el embargo y lo que llamó intentos de provocar desórdenes y salidas ilegales.

Después del 5 de agosto de 1994 vino la crisis de los balseros. Según Siro del Castillo, el 13 de agosto de 1994 Fidel Castro anunció que se retirarían los guardafronteras de las costas y que podría irse del país cualquier persona que quisiera.""")],
 ["FR-B017", "FR-B018", "FR-B015", "FR-B019", "FR-B012", "FR-B021"]),

(B, "perspectivas", [("¿Por qué se fueron tantos cubanos en 1994?", """Las fuentes señalan varias causas y no todas les dan el mismo peso.

La primera es la economía. El aumento de las salidas ilegales a principios de los años noventa coincidió con una crisis económica grave en Cuba tras la desaparición del bloque comunista de Europa del Este y de la Unión Soviética, la etapa que el gobierno cubano llamó 'Período Especial'. Según Wikipedia, Cuba perdió cerca del 80 % de su comercio y su principal proveedor de alimentos y combustible, y hubo apagones de hasta veinte horas.

La segunda tiene que ver con las vías legales. Según Siro del Castillo, en una ponencia en FIU, Estados Unidos no cumplió el acuerdo migratorio de 1987, que permitía hasta 20.000 visas al año: entre 1987 y 1994 solo se otorgaron 11.222 visas.

El gobierno cubano pone el acento en la política de Estados Unidos. Según EcuRed, la crisis de 1994 se debió a la política estadounidense de acoger a todo cubano que llegara a sus costas.

Los números muestran cómo creció la presión. Las salidas subieron de unos pocos cientos en 1989 a unos pocos miles en 1993. Según la GAO, en los primeros seis meses de 1993 la Guardia Costera recogió a unos 1.300 balseros cubanos; en el mismo período de 1994 fueron unos 4.700.

Cada fuente subraya la causa que más le importa. Lo prudente es tenerlas todas en cuenta.""")],
 ["FR-B003", "FR-B004", "FR-B005", "FR-B006", "FR-B001", "FR-B002"]),

(B, "hecho", [("¿Qué pasó con el remolcador 13 de Marzo?", """Ocurrió en el verano de 1994, y sobre cómo se hundió hay dos versiones enfrentadas.

Según Wikipedia, el 13 de julio de 1994 un grupo de cubanos se llevó el remolcador '13 de Marzo' para intentar llegar a Estados Unidos, y la embarcación se hundió poco después de salir de la costa con muchos muertos.

Los sobrevivientes, según la misma fuente, afirmaron que la embarcación fue hundida a propósito por los guardafronteras cubanos. El gobierno cubano negó con firmeza que el remolcador hubiera sido hundido a propósito. Las fuentes que tenemos recogen las dos posiciones, pero ninguna las resuelve.

El hundimiento no fue un hecho aislado. En el verano de 1994 hubo varios intentos de llevarse por la fuerza remolcadores y otras embarcaciones de la bahía de La Habana para llegar a Estados Unidos. Según la GAO, entre el 13 de julio y el 8 de agosto de 1994 murieron al menos 37 personas que intentaban salir y 2 funcionarios cubanos en una serie de secuestros de embarcaciones. La GAO no aclara cuántas de esas muertes corresponden al '13 de Marzo'.""")],
 ["FR-B009", "FR-B010", "FR-B011", "FR-B007", "FR-B008"]),

(B, "contexto", [("¿Cómo respondió Estados Unidos cuando Castro abrió las costas en 1994?", """Con un cambio de política que rompió con tres décadas de práctica.

Primero hubo un aviso desde La Habana. Según la GAO, en un discurso televisado el 13 de agosto de 1994 Fidel Castro culpó a Estados Unidos de los disturbios y la violencia y amenazó con levantar las restricciones de salida si Estados Unidos no tomaba medidas para frenar las salidas en bote y no devolvía a los secuestradores que habían llegado allí. Según la misma fuente, al no recibir la respuesta que esperaba, Castro indicó que no impediría las salidas, y durante la semana siguiente muchos cubanos fueron a las playas, construyeron embarcaciones improvisadas y se hicieron a la mar.

El 19 de agosto de 1994 el presidente Clinton anunció que la Guardia Costera ya no llevaría a Estados Unidos a los balseros interceptados en el mar, sino a la base naval de Guantánamo. Según Siro del Castillo, en una ponencia en FIU, Clinton afirmó entonces que no permitiría que el gobierno de Cuba aprovechara la tradicional política de 'puertas abiertas' para exportar a la oposición y usar las salidas como válvula de escape en plena crisis económica.

Al principio el mensaje fue tajante. Según la GAO, el presidente y la fiscal general dijeron que los cubanos llevados a Guantánamo no tendrían oportunidad de entrar después en Estados Unidos, pero muchos cubanos no creyeron que la nueva política se aplicaría y siguieron saliendo.""")],
 ["FR-B020", "FR-B022", "FR-B024", "FR-B025", "FR-B026"]),

(B, "hecho", [("¿Cuántos balseros terminaron en Guantánamo?", """No hay una cifra única. Las fuentes dan números distintos, y lo honesto es darlos todos.

Siro del Castillo da 32.362 cubanos interceptados entre agosto y septiembre de 1994 en la operación 'Able Vigil'. La GAO, la oficina de auditoría del Congreso de Estados Unidos, habla de unos 33.000 recogidos en el mar y llevados a la base. Wikipedia dice que unos 20.000 quedaron detenidos en ella, muy por debajo de las otras dos.

Para todo el año la cifra es mayor. Según el Servicio de Investigación del Congreso (CRS), el número de cubanos interceptados por la Guardia Costera o la Patrulla Fronteriza llegó a casi 40.000 en 1994, la cifra más alta desde el Mariel.

No todos se quedaron en Guantánamo. Según la GAO, 8.763 cubanos fueron trasladados a un refugio en Panamá entre septiembre de 1994 y febrero de 1995, y 7.291 fueron devueltos a Guantánamo en febrero de 1995.

Además, los cubanos no estaban solos en la base: ya había haitianos allí. La población total de los campamentos en septiembre de 1994 también varía según la fuente: la GAO habla de unas 45.000 personas, con unos 12.000 haitianos; Siro del Castillo dice que llegó a cerca de 50.000.""")],
 ["FR-B027", "FR-B028", "FR-B029", "FR-B030"]),

(B, "perspectivas", [("¿Cómo eran las condiciones en los campamentos de Guantánamo?", """Depende de quién lo cuente y de qué momento se hable. Hay dos juicios casi opuestos.

Siro del Castillo, en una ponencia en FIU, describe los primeros meses: los refugiados vivían en tiendas de lona sobre la tierra, dormían en catres del ejército dentro de campamentos rodeados de alambre de púas, pocos tenían agua corriente, usaban letrinas portátiles y comían sobre todo raciones militares. Según él, la infraestructura de la base estaba preparada para unas 5.000 personas. Su juicio es duro: las condiciones fueron pésimas y en algunos casos inhumanas, y algunos militares dieron a los refugiados un trato arbitrario y a veces abusivo.

La GAO, la oficina de auditoría del Congreso de Estados Unidos, visitó la base en junio de 1995 y concluyó que las condiciones eran difíciles pero adecuadas, y que en general superaban las pautas mínimas del ACNUR, como 3,5 metros cuadrados de espacio por persona.

Las dos versiones se acercan cuando se mira el tiempo. La propia GAO dice que en septiembre de 1994 los mandos militares describían las condiciones como marginales, porque se levantaban tiendas a medida que llegaba la gente. Según Siro del Castillo, en octubre de 1994 el Departamento de Estado anunció mejoras, como agua corriente en el 75 % de los campamentos cubanos y pisos de madera para las tiendas, y según la GAO el Departamento de Defensa gastó después unos 25,3 millones de dólares en mejoras.

Es decir, uno describe sobre todo el principio y el otro, el campamento ya mejorado.""")],
 ["FR-B032", "FR-B031", "FR-B033", "FR-B035", "FR-B036", "FR-B034"]),

(B, "humano", [("Mi papá estuvo en Guantánamo en el 94 y casi no habla de eso. ¿Cómo fue esperar allí?", """Es normal que le cueste hablarlo. Fue una espera larga y llena de incertidumbre, y no le pasó solo a él.

Al principio nadie sabía qué iba a pasar. Según la GAO, el presidente y la fiscal general de Estados Unidos dijeron que los cubanos llevados a Guantánamo no tendrían oportunidad de entrar después en Estados Unidos. Según Siro del Castillo, que escribió sobre los campamentos, en los primeros meses la gente vivía en tiendas de lona sobre la tierra, dormía en catres del ejército dentro de campamentos rodeados de alambre de púas, y comía sobre todo raciones militares.

Esa incertidumbre pesó mucho. Según del Castillo, causó ansiedad y depresión en adultos y menores; muchos balseros se lanzaron a los campos minados o al mar para volver a territorio cubano y otros pidieron ser repatriados.

También hubo quien buscó cómo seguir adelante. Según Wikipedia, algunos detenidos montaron gimnasios improvisados, galerías de arte, periódicos y una emisora de radio, y organizaron lecturas de poesía.

Poco a poco se abrieron salidas. El 14 de octubre de 1994 Clinton anunció que recibirían permiso de entrada los mayores de 70 años, los menores no acompañados y las personas con enfermedades graves y sus cuidadores; el 2 de diciembre se añadieron, caso por caso, los niños y sus familias.

Si tu papá quiere contarlo algún día, estos datos pueden ayudarte a entender de dónde viene su silencio.""")],
 ["FR-B026", "FR-B032", "FR-B037", "FR-B040", "FR-B039"]),

(B, "hecho", [("¿Qué decía el acuerdo migratorio de septiembre de 1994?", """El acuerdo se firmó el 9 de septiembre de 1994 y buscaba cerrar la crisis de los balseros con una vía legal y ordenada.

El punto central fue un intercambio: Estados Unidos admitiría al menos 20.000 inmigrantes cubanos al año, sin contar a los familiares directos de ciudadanos estadounidenses, y Cuba se comprometió a impedir las salidas inseguras 'usando principalmente métodos persuasivos'.

Según el Servicio de Investigación del Congreso (CRS), el acuerdo también incluyó cooperar contra el tráfico ilegal de personas y en el regreso voluntario de cubanos, y seguir negociando sobre los cubanos no admisibles bajo la ley migratoria estadounidense, punto en el que no hubo acuerdo.

Según la GAO, la Sección de Intereses de Estados Unidos en La Habana calculó que las 20.000 entradas anuales se repartirían en unos 7.000 refugiados y familiares, 8.000 visas de inmigrante con sus familias y 5.000 personas elegidas por un sorteo especial.

El efecto en las costas fue rápido. Según la GAO, a los pocos días del acuerdo la policía cubana volvió a patrullar los caminos hacia las playas con órdenes de arrestar a quienes llevaran balsas o materiales para hacerlas, y cesaron las salidas en balsa.""")],
 ["FR-B041", "FR-B042", "FR-B044", "FR-B043"]),

(B, "hecho", [("¿Cómo funcionaba el sorteo de visas para cubanos que salió del acuerdo de 1994?", """El sorteo nació porque las vías normales no alcanzaban. Según el Servicio de Investigación del Congreso (CRS), como el sistema normal de visas no llegaba a las 20.000 entradas anuales prometidas en el acuerdo de 1994, Estados Unidos creó un sorteo especial de visas.

Según la GAO, la Sección de Intereses de Estados Unidos en La Habana calculaba que de esas 20.000 entradas, 5.000 serían personas elegidas por el sorteo; el resto serían unos 7.000 refugiados y familiares y 8.000 visas de inmigrante con sus familias.

Los requisitos, según el CRS, eran tener entre 18 y 55 años y cumplir dos de tres condiciones: haber terminado la enseñanza secundaria, tener al menos tres años de experiencia laboral o tener familiares en Estados Unidos.

El interés creció en cada convocatoria. Según el CRS, se inscribieron unas 189.000 personas en 1994, 433.000 en 1996 y 541.000 en 1998. En cada convocatoria hubo muchos más inscritos que las 5.000 plazas anuales previstas para el sorteo.""")],
 ["FR-B045", "FR-B044", "FR-B046"]),

(B, "hecho", [("¿Qué pasó con los cubanos de Guantánamo al final?", """La mayoría terminó entrando en Estados Unidos, gracias a un segundo acuerdo.

El 2 de mayo de 1995 el gobierno de Clinton anunció un nuevo acuerdo con Cuba: la mayoría de los cubanos de Guantánamo entrarían en Estados Unidos con permiso humanitario, descontando 5.000 al año durante tres años de las 20.000 entradas anuales, y los cubanos interceptados en el mar serían devueltos a Cuba en vez de ir a Guantánamo.

Según Siro del Castillo, la fiscal general Janet Reno anunció que todos los cubanos de la base, salvo los que tuvieran antecedentes penales, podrían viajar a Estados Unidos.

La salida fue lenta. Según la GAO, al 7 de junio de 1995 quedaban unos 18.500 cubanos en Guantánamo, y salían de 500 a 550 por semana en tres vuelos chárter, porque las autoridades de Florida sostenían que el estado no podía recibir más de 550 por semana. Según Siro del Castillo, a finales de enero de 1996 el último salió de la base.

No todos esperaron. Según la GAO, hasta el 27 de junio de 1995 unos 622 cubanos habían vuelto a Cuba por vía diplomática, 1.000 habían regresado por su cuenta, por tierra o por mar, y 139 se habían reasentado en terceros países.""")],
 ["FR-B047", "FR-B050", "FR-B049", "FR-B038"]),

(B, "hecho", [("¿La política de pies secos, pies mojados salió de la crisis de los balseros?", """En buena parte sí, aunque las fuentes no la fechan igual.

De los acuerdos de 1994 y 1995 surgió la práctica conocida como 'pies secos, pies mojados': los cubanos interceptados en el mar eran devueltos a Cuba salvo que expresaran temor a ser perseguidos, y los que llegaban a tierra en general podían quedarse y pedir la residencia al año siguiente por la Ley de Ajuste Cubano.

La pieza clave fue el acuerdo de mayo de 1995. El 2 de mayo de 1995 el gobierno de Clinton anunció que los cubanos interceptados en el mar serían devueltos a Cuba en vez de ir a Guantánamo. Según el Servicio de Investigación del Congreso (CRS), ambos gobiernos se comprometieron a que no se tomaran represalias contra los repatriados, a quienes funcionarios estadounidenses informarían cómo emigrar legalmente.

Sobre cuándo empezó exactamente hay diferencias. Siro del Castillo dice que el gobierno estadounidense la practica desde abril de 1999; el CRS la describe como una práctica que fue surgiendo de los acuerdos de 1994 y 1995; Wikipedia la atribuye a Clinton como respuesta a la crisis de 1994. Lo que todas comparten es que nació de cómo se cerró la crisis de los balseros.""")],
 ["FR-B054", "FR-B047", "FR-B048", "FR-B055"]),

(B, "contexto", [("¿Por qué muchos cubanos aprobados para emigrar en 1995 no podían salir enseguida?", """Porque tener la aprobación no bastaba: había que pagar el viaje y los trámites, y esos costos subieron.

Según la GAO, en febrero de 1995 el gobierno cubano subió el pasaje de ida La Habana-Miami de 150 a 990 dólares, y en junio de 1995 impuso cobros de 400 dólares por el examen médico (250 para niños), 250 por el permiso de salida y documentos y 50 por el pasaporte.

La valoración de Washington quedó recogida en el mismo informe. Según la GAO, funcionarios estadounidenses consideraron que algunos cobros por servicios antes gratuitos podían ser razonables, pero que los impuestos por Cuba serían un obstáculo serio para quienes querían emigrar. Las fuentes que tenemos no recogen la explicación del gobierno cubano sobre esos cobros.

El problema afectaba a una vía que se había abierto hacía poco. Con el acuerdo de septiembre de 1994, la Sección de Intereses de Estados Unidos en La Habana calculó que las 20.000 entradas anuales se repartirían en unos 7.000 refugiados y familiares, 8.000 visas de inmigrante con sus familias y 5.000 personas elegidas por un sorteo especial.""")],
 ["FR-B052", "FR-B053", "FR-B044", "FR-B041"]),

(B, "contexto", [("¿Los cubanos fueron los únicos balseros interceptados en el Caribe en esos años?", """No. Antes de los balseros cubanos de 1994, Estados Unidos ya interceptaba en el mar a migrantes haitianos.

Según Siro del Castillo, en una ponencia en FIU, entre octubre de 1991 y junio de 1992 Estados Unidos interceptó a 36.596 haitianos en alta mar, y entre junio de 1993 y noviembre de 1994 llevó a 21.638 a los campamentos de Guantánamo. Cuando llegaron los cubanos, compartieron la base con ellos: según la GAO, en septiembre de 1994 los campamentos tenían unas 45.000 personas, con unos 12.000 haitianos; del Castillo dice que llegó a cerca de 50.000.

La comparación entre los dos grupos genera debate. Según Siro del Castillo, el trato especial que reciben los cubanos que llegan a Estados Unidos contrasta con el trato que considera discriminatorio hacia dominicanos y haitianos, a quienes se deporta sin la misma oportunidad de pedir asilo. Es su valoración, y las fuentes de este tema no recogen una respuesta oficial de Estados Unidos a esa crítica.

Lo que muestra este contexto es que la crisis de 1994 ocurrió en un Caribe donde varias poblaciones intentaban llegar a Estados Unidos por mar al mismo tiempo.""")],
 ["FR-B056", "FR-B030", "FR-B057"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "Balseros 1994, lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
