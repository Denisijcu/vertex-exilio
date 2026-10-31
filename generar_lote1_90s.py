"""
generar_lote1_90s.py — Lote corto con los fragmentos de fuentes/fragmentos_90s.jsonl que aún no se habían
usado: el informe de la CIDH sobre el remolcador '13 de Marzo', el derribo de las avionetas de Hermanos al
Rescate y la historia de Orestes Lorenzo.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_90s.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_90s.jsonl y se niega a usar fragmentos
que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_90s_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

Nota: exi-b005 (balseros lote 1) dice que las fuentes de ese lote no resuelven las dos versiones del
hundimiento del '13 de Marzo'. Este lote añade lo que concluyó la CIDH en 1996, siempre atribuido, y
la versión del gobierno cubano.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_90s.jsonl")
DESTINO = Path("datos/borrador_90s_lote1.jsonl")
PREFIJO = "exi-n"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

B, W, T = "balseros_1994", "pies_secos_pies_mojados", "transversal"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(B, "perspectivas", [("¿Qué concluyó la Comisión Interamericana sobre el hundimiento del remolcador 13 de Marzo?", """La Comisión Interamericana de Derechos Humanos, de la OEA, llegó a una conclusión clara, y el gobierno cubano mantiene una versión opuesta.

Los hechos básicos son estos. El 13 de julio de 1994, de madrugada, un grupo de cubanos salió del puerto de La Habana en el remolcador estatal '13 de Marzo' para intentar llegar a Estados Unidos, y la embarcación se hundió poco después. Las cifras de muertos no coinciden: según la CIDH, a bordo iban 72 personas y murieron 41; Amnistía Internacional habla de al menos 35 muertos, de los que tiene los nombres; el gobierno cubano dio 32 ahogados. Todas las fuentes coinciden en que hubo 31 sobrevivientes.

Según su Informe 47/96, de octubre de 1996, la CIDH concluyó que el hundimiento no fue un accidente sino un acto intencional, atribuible al Estado cubano porque las tripulaciones eran empleados de una empresa estatal, y responsabilizó a Cuba de las 41 muertes. Cuba no respondió al informe.

La versión del gobierno cubano es otra. Según el gobierno, el remolcador había sido robado, tenía filtraciones y se hundió tras chocar con otra embarcación que intentaba detenerlo; Fidel Castro lo calificó de accidente y elogió a las tripulaciones. Según Amnistía Internacional, la prensa oficial lo presentó como un acto de piratería alentado por emisoras anticubanas y por la política migratoria de Estados Unidos.

Hay además un dato que recogen las fuentes: las autoridades cubanas no recuperaron ni los cuerpos de las víctimas ni el remolcador.""")],
 ["FR-N001", "FR-N002", "FR-N005", "FR-N004", "FR-N006"]),

(B, "humano", [("Un amigo me dice que su tía sobrevivió al remolcador 13 de Marzo. ¿Qué les pasó a los sobrevivientes?", """Según contaron los sobrevivientes, varias embarcaciones de una empresa estatal persiguieron al remolcador, lanzaron chorros de agua a presión contra todos los que estaban en cubierta, también contra mujeres y niños, y lo embistieron por los costados hasta hundirlo. Según su relato, las tripulaciones no ayudaron a quienes quedaron en el agua. El gobierno cubano sostiene otra versión: que fue un accidente.

Todas las fuentes coinciden en que hubo 31 sobrevivientes. Según Amnistía Internacional, quedaron bajo custodia de la Seguridad del Estado: las mujeres y los niños salieron ese mismo día y los 20 hombres fueron llevados a Villa Marista. Amnistía pidió una investigación imparcial, juicios justos para los responsables e indemnizaciones para las familias.

Tampoco se recuperó a los muertos: las autoridades cubanas no recuperaron ni los cuerpos de las víctimas ni el remolcador.

Si la tía de tu amigo quiere contar su historia, su testimonio tiene valor. El informe que la Comisión Interamericana de Derechos Humanos publicó sobre el caso recoge los relatos de los sobrevivientes. Pero es algo que ella decide: hay personas que prefieren no volver a hablar de algo así, y eso también hay que respetarlo.""")],
 ["FR-N003", "FR-N004", "FR-N007", "FR-N006", "FR-N005"]),

(W, "hecho", [("¿Qué pasó con las avionetas de Hermanos al Rescate en 1996?", """El 24 de febrero de 1996, cazas MiG de la Fuerza Aérea cubana derribaron dos avionetas Cessna desarmadas de Hermanos al Rescate, una organización del exilio con base en Miami. Murieron sus cuatro ocupantes: Carlos Costa, Armando Alejandre Jr., Mario de la Peña y Pablo Morales. Una tercera avioneta, pilotada por José Basulto, escapó.

Dónde ocurrió el derribo es una de las cuestiones centrales. Según la investigación de la Organización de Aviación Civil Internacional, lo más probable es que ocurriera fuera del espacio aéreo cubano, sobre aguas internacionales. La OACI señaló también que la interceptación debía ser un último recurso y que Cuba no intentó desviar ni hacer aterrizar las avionetas.

La misma investigación recoge el contexto previo: según la OACI, Cuba venía notificando a Estados Unidos violaciones de su espacio aéreo desde mayo de 1994, entre ellas el lanzamiento de octavillas sobre La Habana en julio de 1995.

Hubo reacciones internacionales. Según el resumen de Wikipedia, el Consejo de Seguridad de la ONU aprobó la Resolución 1067 (1996), que condenó a Cuba, aunque algunos miembros pidieron que el llamado se hiciera a ambas partes. La Comisión Interamericana de Derechos Humanos concluyó que usar armas de combate contra civiles desarmados fue un uso desproporcionado de la fuerza. El 1 de marzo de 1996 el presidente Clinton declaró una emergencia nacional con la Proclamación 6867.""")],
 ["FR-N008", "FR-N009", "FR-N010", "FR-N013"]),

(W, "perspectivas", [("¿Las avionetas de Hermanos al Rescate estaban violando el espacio aéreo cubano cuando las derribaron?", """Sobre eso hay versiones enfrentadas, y conviene separar lo que dice cada parte de lo que concluyó la investigación internacional.

El gobierno cubano sostiene que sí. Según su versión, las avionetas de Hermanos al Rescate violaron su espacio aéreo y sus pilotos fueron advertidos antes del derribo; fuentes cubanas describieron los vuelos como intentos de desestabilizar al gobierno.

Desde el exilio, la organización lo explica de otra manera. Según José Basulto, fundador de Hermanos al Rescate, sus vuelos eran actos de desobediencia civil.

La Organización de Aviación Civil Internacional investigó el caso. Según la OACI, lo más probable es que los derribos ocurrieran fuera del espacio aéreo cubano, sobre aguas internacionales. Señaló también que la interceptación debía ser un último recurso y que Cuba no intentó desviar ni hacer aterrizar las avionetas.

La OACI recogió a la vez el contexto que alegaba Cuba: según la investigación, Cuba venía notificando a Estados Unidos violaciones de su espacio aéreo desde mayo de 1994, entre ellas el lanzamiento de octavillas sobre La Habana en julio de 1995.

Así que hay dos cuestiones distintas. Una es si hubo vuelos anteriores sobre territorio cubano, y la propia OACI recoge que Cuba los venía notificando. Otra es dónde estaban las avionetas cuando fueron derribadas, y ahí la conclusión de la OACI es que lo más probable es que estuvieran sobre aguas internacionales.""")],
 ["FR-N011", "FR-N012", "FR-N009", "FR-N010", "FR-N008"]),

(W, "hecho", [("¿Qué consecuencias tuvo el derribo de las avionetas de Hermanos al Rescate?", """El derribo del 24 de febrero de 1996, en el que murieron cuatro miembros de Hermanos al Rescate, tuvo consecuencias en la ONU, en la OEA y en Washington.

Según el resumen de Wikipedia, el Consejo de Seguridad de la ONU aprobó la Resolución 1067 (1996), que condenó a Cuba, aunque algunos miembros pidieron que el llamado se hiciera a ambas partes.

La Comisión Interamericana de Derechos Humanos concluyó que usar armas de combate contra civiles desarmados fue un uso desproporcionado de la fuerza.

En Estados Unidos, el 1 de marzo de 1996 el presidente Clinton declaró una emergencia nacional con la Proclamación 6867.

Hubo además un giro en la historia del propio grupo. Según el resumen de Wikipedia, Juan Pablo Roque, miembro de Hermanos al Rescate que regresó a Cuba el día antes del derribo, fue señalado después como un espía cubano infiltrado en el grupo.

Los muertos fueron Carlos Costa, Armando Alejandre Jr., Mario de la Peña y Pablo Morales. Una tercera avioneta, pilotada por José Basulto, escapó.

Las fuentes que tenemos aquí resumen estas reacciones, pero no detallan qué medidas concretas se tomaron después de la declaración de emergencia; para eso harían falta otras fuentes.""")],
 ["FR-N008", "FR-N013", "FR-N014"]),

(T, "hecho", [("¿Quién es Orestes Lorenzo?", """Orestes Lorenzo es un piloto cubano que desertó en un avión de combate y que, casi dos años después, volvió a Cuba en una avioneta a buscar a su familia.

El 20 de marzo de 1991, siendo mayor de la Fuerza Aérea cubana, despegó de la base de Santa Clara en un MiG-23 y aterrizó en la Estación Aeronaval de Boca Chica, cerca de Cayo Hueso, en Estados Unidos.

Según contó él mismo, se fue desencantado con el gobierno, preocupado por el futuro de sus hijos y después de que se negaran una y otra vez los permisos de salida para su familia. Según la agencia AP, tras su deserción el gobierno cubano lo había condenado a muerte.

Su familia se quedó en Cuba. El 19 de diciembre de 1992 Lorenzo volvió en una avioneta Cessna 310 que le facilitó la Fundación Valladares, aterrizó en una carretera costera cerca de Varadero y recogió a su esposa, Victoria, y a sus dos hijos, Reyniel y Alejandro, para llevarlos a Estados Unidos.

Contó su historia en el libro 'Wings of the Morning'.

Las fuentes que tenemos sobre su caso son la crónica de la AP y un artículo de General Aviation News; no tenemos aquí una declaración del gobierno cubano sobre la deserción o el rescate.""")],
 ["FR-N015", "FR-N016", "FR-N018", "FR-N017", "FR-N019"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "90s lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
