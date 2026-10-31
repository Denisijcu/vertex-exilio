"""
generar_lote3_1959.py — Tercer lote de ejemplos de Pedro Pan (etapa pedro_pan).

Uso (desde E:\\vertex-exilio):
    python generar_lote3_1959.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_1959_1962.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_1959_lote3.jsonl con todos los ejemplos en estado 'pendiente'.

No hay fragmentos nuevos: reutiliza los ya aprobados con preguntas que los lotes 1 y 2 no cubrían
(quién era Walsh, cuándo se hizo pública la operación, qué hizo el gobierno de Kennedy por los niños,
de dónde salió la campaña de la patria potestad, si fue el mayor éxodo de niños, la película de la USIA,
los Pedro Pan de Nuevo México). Usa cuatro que estaban sin usar: FR-PP014, FR-PP020, FR-PP028 y FR-PP042.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_1959_1962.jsonl")
DESTINO = Path("datos/borrador_1959_lote3.jsonl")
PREFIJO = "exi-s"
PRIMER_ID = 30

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

P = "pedro_pan"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(P, "hecho", [("¿Quién era el padre Bryan Walsh?", """Bryan O. Walsh fue un sacerdote católico de Miami y uno de los organizadores de la Operación Pedro Pan.

Según Rita Cauce, de la FIU, Walsh nació en Irlanda en 1930 y murió en 2001. En 1960 era director del Catholic Welfare Bureau de Miami, la agencia católica de bienestar social. En noviembre de ese año llegó a su oficina un muchacho cubano de 15 años, Pedro, cuyos familiares en Miami no podían mantenerlo, y el 12 de diciembre de 1960 Walsh se reunió con James Baker, director de la Academia Ruston de La Habana, que ayudaba a padres cubanos a enviar a sus hijos a Estados Unidos.

De ahí salió el plan. Según Cauce, la idea original era sacar a unos 200 niños con visas de estudiante: Walsh consiguió formularios de matrícula de la escuela secundaria de Coral Gables y firmó cartas asumiendo la responsabilidad de los menores. También insistió en que los niños fueran atendidos por agencias de bienestar infantil con licencia y en que se respetara su religión, para no repetir lo ocurrido con niños de la revolución húngara de 1956.

Walsh dio su propia versión de la operación. Según él, su agencia no tenía constancia de ningún niño perdido, ningún menor fue dado en adopción y la Iglesia en Cuba como institución no participó.

Según Cauce, sus papeles sobre Pedro Pan están en el archivo de Barry University, y los expedientes personales de los niños están restringidos hasta 2050.""")],
 ["FR-PP044", "FR-PP003", "FR-PP023", "FR-PP022", "FR-PP015"]),

(P, "hecho", [("¿Cuándo se supo públicamente de la Operación Pedro Pan y de dónde viene el nombre?", """Durante más de un año la operación se mantuvo en silencio, y el nombre con que se la conoce no lo pusieron sus organizadores sino la prensa.

Entre diciembre de 1960 y octubre de 1962 llegaron a Estados Unidos sin sus padres más de 14.000 niños y adolescentes cubanos; la estimación más citada es de 14.048.

Según Wikipedia, el programa se mantuvo en secreto hasta febrero de 1962, cuando lo dio a conocer el diario The Plain Dealer, y el 9 de marzo de 1962 el periodista Gene Miller, del Miami Herald, acuñó el nombre de Operación Pedro Pan.

La historia había empezado con un muchacho llamado Pedro. En noviembre de 1960 llegó a la oficina del padre Bryan Walsh, director del Catholic Welfare Bureau de Miami, un muchacho cubano de 15 años, Pedro, cuyos familiares en Miami no podían mantenerlo. Las fuentes que tenemos no dicen si el nombre tiene que ver con él.

En Cuba la operación se conoce de otra forma. La enciclopedia oficial cubana, EcuRed, la llama Operación Peter Pan y, según EcuRed, fue una operación de subversión organizada por el Departamento de Estado, la jerarquía católica de Miami, la CIA y organizaciones opuestas al gobierno revolucionario.

Así que la operación tiene hasta dos nombres, Pedro Pan y Peter Pan, y cada parte la cuenta de forma muy distinta.""")],
 ["FR-PP001", "FR-PP028", "FR-PP003", "FR-PP013"]),

(P, "hecho", [("¿Qué hizo el gobierno de Kennedy por los niños de Pedro Pan?", """El gobierno federal asumió desde muy pronto el cuidado de los niños que llegaban solos.

El programa de nueve puntos que Kennedy ordenó en febrero de 1961 para los refugiados cubanos incluía, en el punto 8, ayuda económica para el cuidado y la protección de los niños que llegaban sin acompañante, a los que llamó 'el grupo más indefenso' entre los refugiados.

El sistema funcionaba a través de agencias. Según Rita Cauce, de la FIU, la ayuda la supervisaba el Departamento de Bienestar Público de la Florida en nombre del gobierno federal, y cuatro agencias se encargaban del cuidado: el Catholic Welfare Bureau de los niños católicos, el Children's Service Bureau de Dade de los protestantes, y el Jewish Family and Children's Service y la HIAS de los judíos.

Las cifras de finales de 1961 dan una idea del volumen. Según el boletín de la Seguridad Social de 1962, al 31 de diciembre de 1961 había 2.309 niños refugiados en hogares de acogida o en instituciones, un tercio en el área de Miami; el programa había atendido a unos 3.000, y cerca de 1.000 ya se habían reunido con sus familias.

Hubo también una película. Según Wikipedia, el fiscal general Robert F. Kennedy aprobó fondos para una película de la Agencia de Información de Estados Unidos, 'The Lost Apple', sobre niños del campamento de Florida City, para explicarles por qué estaban allí; Wikipedia la califica de propaganda y señala que no menciona lo que pasaba en Cuba.

El programa federal para niños cubanos siguió funcionando muchos años: hasta 1982 según Cauce y hasta 1981 según Wikipedia.""")],
 ["FR-PP020", "FR-PP021", "FR-PP030", "FR-PP042", "FR-PP035"]),

(P, "perspectivas", [("¿De dónde salió el rumor de que el gobierno cubano iba a quitar la patria potestad?", """Lo primero que hay que tener claro es que la ley nunca existió. El gobierno cubano nunca aprobó una ley para quitar a los padres la patria potestad sobre sus hijos, aunque el rumor circuló en aquellos años y pesó en la decisión de muchas familias de enviar a sus hijos solos.

Sobre el origen del rumor hay varias versiones.

La historiadora Deborah Shnookal, citada por Wikipedia, sostiene que la falsa ley circuló primero en Cuba a través de grupos contrarios a Castro y de católicos, y que después la amplificó Radio Swan, una emisora respaldada por la CIA.

La versión del gobierno cubano va más lejos. Según EcuRed, su enciclopedia oficial, la campaña empezó en Radio Swan con mensajes dirigidos a las madres cubanas, la falsa ley se redactó en Estados Unidos y la introdujo en Cuba José Pujals Mederos; EcuRed cita a Ángel Fernández Varela, a quien llama agente de la CIA, como uno de sus redactores.

Hay un punto en el que las fuentes se acercan. Según Wikipedia, en 1999 un tribunal federal de Illinois concluyó, tras revisar 733 páginas de documentos de la CIA, que la evacuación de los niños no fue una operación de la CIA; aun así, varios ex agentes de la CIA admitieron haber editado, impreso y distribuido copias de la falsa ley.

Así que, con lo documentado, la CIA participó en difundir el rumor, aunque no organizara la salida de los niños. Quién redactó la primera versión de la falsa ley es algo que las fuentes cuentan de forma distinta.""")],
 ["FR-PP010", "FR-PP011", "FR-PP014", "FR-PP012"]),

(P, "reformulacion", [("Dicen que Pedro Pan fue el mayor éxodo de niños de la historia de América. ¿Es así?", """Es una afirmación que hace una persona concreta, y hay quien lo compara con otros casos de forma muy distinta.

La frase viene de Carlos Eire, profesor de Yale, que salió de niño en Pedro Pan. Según Rita Cauce, de la FIU, Eire afirmó que fue el mayor éxodo de niños en la historia de América y que pasó casi inadvertido. Es su valoración; las fuentes que tenemos no comparan Pedro Pan con otros movimientos de niños del continente para comprobarla.

Las cifras sí son grandes. Entre diciembre de 1960 y octubre de 1962 llegaron a Estados Unidos sin sus padres más de 14.000 niños y adolescentes cubanos; la estimación más citada es de 14.048. Wikipedia calcula además que unos 25.000 niños pasaron en total por el programa federal para niños cubanos, que siguió funcionando años después de Pedro Pan.

La enciclopedia oficial cubana hace otra comparación. Según EcuRed, a diferencia de otras salidas de niños, como la de niños vascos o la de niños judíos de Alemania a finales de los años treinta, la Operación Peter Pan se hizo sin ninguna justificación política, ética ni moral.

Así que lo que se puede decir con seguridad es que fue una salida de niños muy numerosa. Si fue la mayor de América es la opinión de Eire, y cómo se compara con los casos europeos depende de quién haga la comparación.""")],
 ["FR-PP037", "FR-PP001", "FR-PP035", "FR-PP046"]),

(P, "humano", [("Mi tío fue un Pedro Pan y terminó en Nuevo México. ¿Mandaron a muchos niños tan lejos?", """Sí, y Nuevo México no fue un caso raro: fue el segundo estado que más niños de Pedro Pan recibió.

Según Rita Cauce, de la FIU, Nuevo México fue el segundo estado, después de la Florida, en recibir niños de Pedro Pan, con 374, y la alcaldía de Albuquerque proclamó el 18 de mayo de 2012 'Día de Pedro Pan'.

El reparto fue muy amplio. Los niños de Pedro Pan fueron acogidos en hogares y centros de unas 100 ciudades de 35 estados; en Miami hubo albergues como el campamento de Matecumbe, con unos 400 varones, y el de Florida City.

Que tu tío terminara lejos tiene que ver con cómo funcionaba el sistema. Aproximadamente la mitad de los niños tenía familiares o amigos en Estados Unidos que los acogieron; el resto quedó al cuidado de agencias según su religión, y el Catholic Welfare Bureau atendió a algo más de 7.000.

Hoy hay una red de antiguos Pedro Pan. Según Cauce, en 1991 fundaron Operation Pedro Pan Group, que mantiene el contacto con más de 2.000 de ellos, y gracias a su trabajo el sitio del albergue de Florida City fue declarado lugar histórico de la Florida.

Si tu tío quiere reconstruir su historia, ese grupo puede ser un buen punto de partida, y en Nuevo México quizá haya otros que compartieron con él aquellos años.""")],
 ["FR-PP040", "FR-PP008", "FR-PP006", "FR-PP039"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "1959-1962 lote 3"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
