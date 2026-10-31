"""
generar_lote2_balseros.py — Segundo lote de ejemplos de la crisis de los balseros de 1994.

Uso (desde E:\\vertex-exilio):
    python generar_lote2_balseros.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_balseros_1994.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_balseros_lote2.jsonl con todos los ejemplos en estado 'pendiente'.

No hay fragmentos nuevos: reutiliza los ya aprobados con preguntas que el lote 1 no cubría (por qué
Castro dejó de impedir las salidas, el acuerdo de 1987, cuánto costó la crisis, los que volvieron de
Guantánamo a Cuba...). Incluye los dos que estaban sin usar: FR-B023 (EcuRed) y FR-B051 (costo).
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_balseros_1994.jsonl")
DESTINO = Path("datos/borrador_balseros_lote2.jsonl")
PREFIJO = "exi-b"
PRIMER_ID = 16

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

B = "balseros_1994"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(B, "perspectivas", [("¿Por qué Castro dejó de impedir las salidas en agosto de 1994?", """Sobre eso hay versiones distintas, y conviene ver qué dice cada fuente.

Según la GAO, la oficina de auditoría del Congreso de Estados Unidos, en un discurso televisado el 13 de agosto de 1994 Fidel Castro culpó a Estados Unidos de los disturbios y la violencia y amenazó con levantar las restricciones de salida si Estados Unidos no tomaba medidas para frenar las salidas en bote y no devolvía a los secuestradores que habían llegado allí. Según la misma fuente, al no recibir la respuesta que esperaba, Castro indicó que no impediría las salidas, y durante la semana siguiente muchos cubanos fueron a las playas, construyeron embarcaciones improvisadas y se hicieron a la mar.

Según Siro del Castillo, en una ponencia presentada en la FIU, ese mismo 13 de agosto Castro anunció que se retirarían los guardafronteras de las costas y que podría irse del país cualquier persona que quisiera.

La versión del gobierno cubano pone el acento en otro lado. Según EcuRed, su enciclopedia oficial, la presión de la emigración ilegal, los secuestros de embarcaciones y los disturbios llevaron al gobierno a decidir eliminar las restricciones a las salidas, y Castro retó a Clinton a aceptar a todos los cubanos que quisieran ir. En la misma línea, según Wikipedia, Castro culpó de los problemas de Cuba a Estados Unidos, citando el embargo y lo que llamó intentos de provocar desórdenes y salidas ilegales.

Las fuentes coinciden en lo que pasó: Castro anunció que no impediría las salidas y miles se lanzaron al mar. Lo que difiere es la explicación: la GAO lo cuenta como una amenaza a Estados Unidos seguida de la apertura de las costas, y el gobierno cubano, como una respuesta a la presión de las salidas ilegales y a la política de Estados Unidos.""")],
 ["FR-B020", "FR-B022", "FR-B021", "FR-B023", "FR-B019"]),

(B, "perspectivas", [("¿Estados Unidos cumplía el acuerdo de dar 20.000 visas al año a los cubanos antes de 1994?", """Según Siro del Castillo, no, y esa es una de las explicaciones que se dan para la crisis de 1994.

En una ponencia presentada en la FIU, Siro del Castillo sostiene que Estados Unidos no cumplió el acuerdo migratorio de 1987, que permitía hasta 20.000 visas al año: entre 1987 y 1994 solo se otorgaron 11.222 visas. Siro del Castillo lo señala como otra causa del aumento de las salidas ilegales.

El gobierno cubano va más allá. Según EcuRed, su enciclopedia oficial, en los años anteriores Estados Unidos recibió muchos más inmigrantes cubanos indocumentados de los que aceptó por vía legal, y la crisis de 1994 se debió a la política estadounidense de acoger a todo cubano que llegara a sus costas. EcuRed da cifras concretas para eso, pero no tenemos otra fuente que las confirme, así que no las repito.

El acuerdo que puso fin a la crisis volvió sobre la misma cifra. El 9 de septiembre de 1994 Estados Unidos y Cuba firmaron un acuerdo migratorio: Estados Unidos admitiría al menos 20.000 inmigrantes cubanos al año, sin contar a los familiares directos de ciudadanos estadounidenses.

Y para cumplirlo hubo que inventar algo nuevo. Según el Servicio de Investigación del Congreso, como el sistema normal de visas no alcanzaba las 20.000 entradas, Estados Unidos creó un sorteo especial de visas; en sus tres convocatorias se inscribieron unas 189.000 personas en 1994, 433.000 en 1996 y 541.000 en 1998.""")],
 ["FR-B005", "FR-B006", "FR-B041", "FR-B045"]),

(B, "hecho", [("¿Cuánto le costó a Estados Unidos la crisis de los balseros?", """Según la GAO, la oficina de auditoría del Congreso de Estados Unidos, el costo adicional de la respuesta estadounidense a la crisis entre agosto de 1994 y septiembre de 1995 superaría los 497 millones de dólares, de los cuales unos 434 millones correspondían al Departamento de Defensa.

Que la mayor parte fuera del Departamento de Defensa tiene que ver con dónde se alojó a los balseros. Desde el 19 de agosto de 1994, por decisión de Clinton, la Guardia Costera ya no llevaba a Estados Unidos a los balseros interceptados en el mar, sino a la base naval de Guantánamo.

La base no estaba preparada. Según Siro del Castillo, en una ponencia presentada en la FIU, cuando llegaron los haitianos y los cubanos la infraestructura de Guantánamo estaba preparada para unas 5.000 personas, y todo había que traerlo de fuera.

Hubo también traslados. Según la GAO, 8.763 cubanos fueron trasladados de Guantánamo a un refugio en Panamá entre septiembre de 1994 y febrero de 1995, y 7.291 fueron devueltos a Guantánamo en febrero de 1995.

Y la salida de la base fue lenta. Según la GAO, al 7 de junio de 1995 quedaban unos 18.500 cubanos en Guantánamo, y salían de 500 a 550 por semana en tres vuelos chárter, porque las autoridades de Florida sostenían que el estado no podía recibir más de 550 por semana.

La cifra de la GAO es una estimación de costos adicionales hecha en 1995; las fuentes que tenemos no dan un balance final.""")],
 ["FR-B051", "FR-B024", "FR-B031", "FR-B029", "FR-B049"]),

(B, "humano", [("Mi abuela dice que en el 94 la gente hacía balsas con cualquier cosa en la playa. ¿Cómo fue aquello?", """Lo que recuerda tu abuela coincide con lo que describen las fuentes de la época.

La crisis venía de antes del verano. En 1994 hubo varios intentos de llevarse por la fuerza remolcadores y otras embarcaciones de la bahía de La Habana para llegar a Estados Unidos. Según la GAO, la oficina de auditoría del Congreso de Estados Unidos, entre el 13 de julio y el 8 de agosto de 1994 murieron al menos 37 personas que intentaban salir y 2 funcionarios cubanos en una serie de secuestros de embarcaciones.

Luego vino el momento que recuerda tu abuela. Según la GAO, cuando Castro indicó que no impediría las salidas, durante la semana siguiente muchos cubanos fueron a las playas, construyeron embarcaciones improvisadas y se hicieron a la mar. Según el Servicio de Investigación del Congreso, el número de cubanos interceptados por la Guardia Costera o la Patrulla Fronteriza llegó a casi 40.000 en 1994, la cifra más alta desde el Mariel.

Terminó casi tan rápido como empezó. El 9 de septiembre de 1994 Estados Unidos y Cuba firmaron un acuerdo migratorio, y según la GAO, a los pocos días la policía cubana volvió a patrullar los caminos hacia las playas con órdenes de arrestar a quienes llevaran balsas o materiales para hacerlas, y cesaron las salidas en balsa.

Si tu abuela vio salir a vecinos o conocidos, pregúntale qué fue de ellos. Esa memoria también es parte de la historia.""")],
 ["FR-B007", "FR-B008", "FR-B022", "FR-B028", "FR-B041", "FR-B043"]),

(B, "reformulacion", [("Oí que a los balseros de Guantánamo los dejaron allí para siempre y nunca entraron a Estados Unidos. ¿Es cierto?", """No. Eso fue lo que se anunció al principio, pero la política cambió y la gran mayoría terminó entrando a Estados Unidos.

Al principio sí se dijo algo parecido. Según la GAO, la oficina de auditoría del Congreso de Estados Unidos, el presidente y la fiscal general dijeron al principio que los cubanos llevados a Guantánamo no tendrían oportunidad de entrar después en Estados Unidos, pero muchos cubanos no creyeron que la nueva política se aplicaría y siguieron saliendo.

Luego empezaron las excepciones. El 14 de octubre de 1994 Clinton anunció que recibirían permiso de entrada los mayores de 70 años, los menores no acompañados y las personas con enfermedades graves y sus cuidadores; el 2 de diciembre se añadieron, caso por caso, los niños y sus familias. Se les llamó los 'cuatro protocolos'.

El cambio grande llegó en 1995. El 2 de mayo el gobierno de Clinton anunció un nuevo acuerdo con Cuba: la mayoría de los cubanos de Guantánamo entrarían en Estados Unidos con permiso humanitario, descontando 5.000 al año durante tres años de las 20.000 entradas anuales. Según Siro del Castillo, la fiscal general Janet Reno anunció que todos los cubanos de la base, salvo los que tuvieran antecedentes penales, podrían viajar a Estados Unidos, y a finales de enero de 1996 el último salió de Guantánamo.

No todos entraron, pero por decisión propia o por otras vías. Según la GAO, hasta el 27 de junio de 1995 unos 622 cubanos habían vuelto de Guantánamo a Cuba por vía diplomática, 1.000 habían regresado por su cuenta y 139 se habían reasentado en terceros países.""")],
 ["FR-B026", "FR-B039", "FR-B047", "FR-B050", "FR-B038"]),

(B, "hecho", [("¿Qué pasó con los balseros que volvieron de Guantánamo a Cuba?", """Hubo balseros que, en lugar de esperar en Guantánamo, volvieron a Cuba, y las fuentes recogen tanto las cifras como las condiciones en que lo hicieron.

Según Siro del Castillo, en una ponencia presentada en la FIU, la incertidumbre y las condiciones de los campamentos causaron ansiedad y depresión en adultos y menores; muchos balseros se lanzaron a los campos minados o al mar para volver a territorio cubano y otros pidieron ser repatriados.

Según la GAO, la oficina de auditoría del Congreso de Estados Unidos, hasta el 27 de junio de 1995 unos 622 cubanos habían vuelto de Guantánamo a Cuba por vía diplomática, 1.000 habían regresado por su cuenta, por tierra o por mar, y 139 se habían reasentado en terceros países.

El acuerdo de mayo de 1995 trató el tema de los que regresaban. Según el Servicio de Investigación del Congreso, ambos gobiernos se comprometieron a que no se tomaran represalias contra los repatriados, a quienes funcionarios estadounidenses informarían cómo emigrar legalmente; los acusados de tráfico de personas sí se exponían a prisión en Cuba. Ese mismo acuerdo estableció que los cubanos interceptados en el mar serían devueltos a Cuba en vez de ir a Guantánamo.

Las fuentes que tenemos no dicen cómo se cumplió en la práctica el compromiso de no tomar represalias, ni qué pasó después con quienes volvieron por su cuenta; para eso harían falta otras fuentes.""")],
 ["FR-B037", "FR-B038", "FR-B048", "FR-B047"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "balseros lote 2"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
