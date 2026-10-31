"""
generar_lote1_presidio.py — Primer lote de ejemplos de la etapa presidio_politico (y algunos transversales
que salen del mismo archivo de fragmentos).

Uso (desde E:\\vertex-exilio):
    python generar_lote1_presidio.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_presidio.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_presidio_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

Es la primera vez que esta etapa tiene ejemplos. Las fuentes son: Wikipedia ('Plantado'), Tania Díaz
Castro y UPECI (CubaNet, periodismo desde la isla), el informe de la misión de la ONU de 1989 y la
Cuban Heritage Collection de la Universidad de Miami. El lote enseña a separar las denuncias que
recibió la ONU de hechos comprobados (FR-P014 está rechazado por eso) y a decir cuándo las fuentes
no dan una cifra fiable.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_presidio.jsonl")
DESTINO = Path("datos/borrador_presidio_lote1.jsonl")
PREFIJO = "exi-p"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

P, T = "presidio_politico", "transversal"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(P, "hecho", [("¿Quiénes fueron los plantados?", """Se llamó plantados a los presos políticos cubanos que se negaron a cooperar con el sistema penitenciario. Rechazaban el trabajo forzado, los programas de reeducación política y el uniforme de preso común.

Esa negativa tuvo consecuencias concretas. En 1964 empezó en la prisión de Isla de Pinos un plan de trabajo forzado para los presos políticos, y en 1967 fueron repartidos entre otras cárceles del país.

Algunos pasaron décadas presos. Mario Chanes de Armas cumplió 30 años de prisión y fue el último plantado en salir, en 1991. Había participado junto a Fidel Castro en el asalto al cuartel Moncada.

Cuántos fueron es difícil de saber. Las cifras de presos políticos varían mucho: Wikipedia da entre 7.000 y 10.000 en 1964 sin indicar de dónde sale el dato, y la periodista Tania Díaz Castro habla de decenas de miles de presos y de unos 15.000 plantados. Con las fuentes que tenemos no hay una cifra que se pueda dar por buena.

Entre los testimonios publicados, Armando Valladares publicó en 1985 'Contra toda esperanza', uno de los primeros sobre los plantados.""")],
 ["FR-P001", "FR-P002", "FR-P004", "FR-P003", "FR-P016"]),

(P, "hecho", [("¿Cuántos años pasaron en la cárcel algunos de los plantados más conocidos?", """Varios de los plantados más conocidos pasaron entre casi veinte y treinta años presos.

Mario Chanes de Armas cumplió 30 años de prisión y fue el último plantado en salir, en 1991. Eusebio Peñalver Mazorra cumplió 28 años como plantado.

José Pujals Mederos, según Tania Díaz Castro, fue liberado en agosto de 1988 después de 27 años de cárcel.

El caso de Ernesto Díaz Rodríguez muestra cómo podía alargarse una condena. Fue capturado en 1968 durante una infiltración armada en Cuba y condenado a 15 años. En 1974 un tribunal militar le sumó 25 años más por conspirar desde la celda, hasta un total de 40. Cumplió 22 y salió de prisión el 23 de marzo de 1991.

Según la agencia de prensa independiente UPECI, Ángel de Fana Serrano cumplió 20 años de prisión política y Luis Zúñiga Rey, 19.

Estas cifras salen de fuentes distintas: unas están corroboradas por más de una fuente y otras, como las de UPECI o las de Tania Díaz Castro, las da una sola, y por eso van atribuidas. No son una lista completa: son los nombres que aparecen en los documentos que tenemos, y hubo otros presos políticos de los que no se habla aquí.""")],
 ["FR-P004", "FR-P005", "FR-P011", "FR-P006", "FR-P007"]),

(P, "hecho", [("¿Quién es Ernesto Díaz Rodríguez?", """Ernesto Díaz Rodríguez es un poeta cubano y uno de los fundadores de Alpha 66.

Fue capturado en 1968 durante una infiltración armada en Cuba y condenado a 15 años de prisión. En 1974 un tribunal militar le sumó 25 años más por conspirar desde la celda, hasta un total de 40. Cumplió 22 y salió de prisión el 23 de marzo de 1991.

Desde la cárcel siguió activo. Según relata Tania Díaz Castro, cuando los plantados descubrieron micrófonos escondidos en sus celdas, Ernesto Díaz consiguió sacar dos de ellos, que llegaron al Comité Cubano Pro Derechos Humanos de Ricardo Bofill para enviarlos a la Comisión de Derechos Humanos de la ONU en Ginebra. Según la misma autora, en junio de 1988 grabó en su celda una entrevista con Mario Chanes de Armas que después transmitió Radio Martí.

También dejó su testimonio por escrito. En su libro 'Rehenes de Castro' escribió que contar la historia del presidio político cubano era una tarea penosa por la cantidad de sufrimiento que encerraba.

Su caso muestra algo que conviene tener en cuenta al hablar del presidio político: entre los presos había personas que habían tomado las armas contra el gobierno, como él. Las fuentes que tenemos no permiten decir cuántos.""")],
 ["FR-P006", "FR-P010", "FR-P012", "FR-P017"]),

(P, "hecho", [("¿Qué pasó con los micrófonos que encontraron los presos políticos en sus celdas?", """Hay dos relatos sobre micrófonos en las celdas de los presos políticos, y conviene contarlos por separado porque no está claro que hablen del mismo hecho.

El primero lo cuenta la periodista Tania Díaz Castro. Según ella, el preso Onofre Pérez descubrió un micrófono escondido en la lámpara de su celda y los demás plantados retiraron luego el resto. Ernesto Díaz consiguió sacar dos de esos micrófonos, que llegaron al Comité Cubano Pro Derechos Humanos de Ricardo Bofill para enviarlos a la Comisión de Derechos Humanos de la ONU en Ginebra. Según la misma autora, José Pujals Mederos, liberado en agosto de 1988 después de 27 años de cárcel, mostró otro de esos micrófonos en un acto en Estados Unidos.

El segundo aparece en el informe de la misión de la ONU que visitó Cuba en 1988. Según documentos que el Comité Cubano Pro Derechos Humanos y dos presos políticos entregaron a la misión, el 28 de mayo de 1988 presos políticos encontraron 15 micrófonos en sus celdas y se deshicieron de ellos, y el incidente fue seguido de dos huelgas de hambre.

El informe recoge lo que esos documentos afirman; no dice que la misión lo comprobara por su cuenta. Y el relato de Tania Díaz Castro, tal como lo tenemos, no da fecha ni número de micrófonos, así que no se puede afirmar que sea el mismo episodio.

Lo que sí coincide en las dos versiones es el papel del Comité Cubano Pro Derechos Humanos como canal para hacer llegar esas denuncias a la ONU.""")],
 ["FR-P010", "FR-P011", "FR-P029"]),

(P, "hecho", [("¿Qué fue la misión de la ONU que visitó Cuba en 1988?", """En 1988 la Comisión de Derechos Humanos de la ONU envió una misión a Cuba por su decisión 1988/106. El informe resultante, el documento E/CN.4/1989/46 del 21 de febrero de 1989, tiene 400 páginas.

La misión estuvo presidida por el embajador Alioune Sene, de Senegal, e integrada por representantes de Nigeria, Bulgaria, Filipinas, Irlanda y Colombia, uno por cada grupo regional. Estuvo en Cuba del 16 al 25 de septiembre de 1988, y el día de su partida fue recibida por Fidel Castro y por Carlos Rafael Rodríguez, presidente y vicepresidente del Consejo de Estado.

Según el informe, la misión escuchó directamente a 87 personas, más de 30 de ellas en representación de organizaciones no gubernamentales, y recogió el testimonio escrito de aproximadamente 1.600 personas.

También visitó centros de detención: Villa Marista, sede del Departamento de Seguridad del Estado; la prisión Combinado del Este, donde entrevistó a nueve presos elegidos por ella; y la prisión provincial de Pinar del Río conocida como Cinco y Medio. Pidió visitar además El Morro, La Cabaña y Quivicán, y el ministro de Relaciones Exteriores le informó que estaban cerradas.""")],
 ["FR-P013", "FR-P021", "FR-P022", "FR-P023", "FR-P024"]),

(P, "hecho", [("¿Qué dijo el informe de la ONU de 1989 sobre torturas y fusilamientos en Cuba?", """El informe recoge denuncias y respuestas, y es importante leerlo así: no es un fallo que dé por probada cada denuncia.

Durante la visita de 1988, la Secretaría de la ONU recibió en nombre de la misión 137 denuncias de torturas, penas o tratos crueles, inhumanos o degradantes. El informe habla de denuncias recibidas.

El informe también recoge denuncias sobre fusilamientos y desapariciones. Según una carta de presos del Combinado del Este, 13 presos políticos fueron fusilados en La Cabaña entre 1980 y 1987, y hay testimonios escritos que denuncian la desaparición de tres personas entre 1964 y 1974.

Las autoridades cubanas respondieron. Según el informe, el ministro del Interior admitió ante la misión que en el pasado algunos detenidos y presos fueron golpeados y que los responsables fueron sancionados, pero afirmó que en Cuba no existen casos de tortura. También dijo que no tenía conocimiento de casos de desaparición forzada y que desde 1982 solo una persona había sido fusilada por delitos contra la seguridad del Estado. El ministro de Relaciones Exteriores afirmó que en Cuba no se producen desapariciones forzadas.

Además, la misión pidió visitar El Morro, La Cabaña y Quivicán, y el ministro de Relaciones Exteriores le informó que estaban cerradas.

Con eso, lo que se puede decir con seguridad es qué se denunció y qué respondió el gobierno, no cuántos casos ocurrieron.""")],
 ["FR-P025", "FR-P028", "FR-P026", "FR-P027", "FR-P024", "FR-P013"]),

(P, "reformulacion", [("Leí que el informe de la ONU de 1989 confirmó 137 casos de tortura en Cuba. ¿Es así?", """No exactamente. La cifra de 137 sí está en el informe, pero no son casos confirmados.

El informe de la misión de la Comisión de Derechos Humanos de la ONU, el documento E/CN.4/1989/46 del 21 de febrero de 1989, dice que durante la visita de 1988 la Secretaría de la ONU recibió en nombre de la misión 137 denuncias de torturas, penas o tratos crueles, inhumanos o degradantes. El informe habla de denuncias recibidas, no de casos comprobados.

La diferencia importa. Una denuncia es lo que alguien afirma ante la misión; el informe no dice que la misión verificara cada una. Por eso, decir que la ONU 'confirmó' 137 torturas va más allá de lo que dice el documento.

Tampoco quiere decir que las denuncias sean falsas. El informe recoge también la respuesta del gobierno: según el documento, el ministro del Interior de Cuba admitió ante la misión que en el pasado algunos detenidos y presos fueron golpeados y que los responsables fueron sancionados, pero afirmó que en Cuba no existen casos de tortura.

Así que lo correcto sería decir algo como: 'la misión de la ONU recibió 137 denuncias de tortura y malos tratos, y el gobierno cubano negó que existiera la tortura'. Esa frase recoge lo que dice el informe sin añadirle ni quitarle nada.""")],
 ["FR-P025", "FR-P013", "FR-P026"]),

(P, "contexto", [("¿Cuántos presos políticos hubo en Cuba?", """Con las fuentes que tenemos, no hay una cifra que se pueda dar por segura, y conviene desconfiar de quien dé una sola sin decir de dónde sale.

Las cifras varían mucho. Wikipedia da entre 7.000 y 10.000 presos políticos en 1964 sin indicar de dónde sale el dato. La periodista Tania Díaz Castro habla de decenas de miles de presos y de unos 15.000 plantados, y según ella en 1959 fueron fusilados más de 360 opositores. Son estimaciones que no coinciden, y la de Wikipedia no indica su fuente.

El informe de la misión de la ONU de 1989 tampoco da un total. Recoge denuncias concretas: según una carta de presos del Combinado del Este, 13 presos políticos fueron fusilados en La Cabaña entre 1980 y 1987, y hay testimonios escritos que denuncian la desaparición de tres personas entre 1964 y 1974.

El gobierno cubano dio su propia versión ante la misión. Según el informe, el ministro del Interior dijo que no tenía conocimiento de casos de desaparición forzada y que desde 1982 solo una persona había sido fusilada por delitos contra la seguridad del Estado.

Lo honesto es reconocer el vacío: las cifras disponibles en nuestras fuentes son estimaciones de periodistas o enciclopedias, denuncias recogidas por la ONU y declaraciones del gobierno. Ninguna de ellas es un conteo verificado del total de presos políticos.""")],
 ["FR-P003", "FR-P015", "FR-P028", "FR-P027", "FR-P013"]),

(P, "contexto", [("¿Por qué en Cuba se conoce poco la historia de los plantados?", """Según un activista de derechos humanos de la isla, porque en 2002 esa historia circulaba sobre todo por vías no oficiales.

Según Lázaro Ricardo Pérez García, presidente de la Fundación Cubana de Derechos Humanos en Isla de la Juventud, en 2002 la población solo podía conocer la historia de los plantados por documentales y libros que entraban de forma clandestina, porque la Aduana confiscaba el material que consideraba «contrarrevolucionario». Es su versión; no tenemos una respuesta oficial sobre ese punto.

Hubo intentos de mostrarla dentro de Cuba. Según la agencia de prensa independiente UPECI, en septiembre de 2002 se exhibió en Nueva Gerona el documental 'En un lugar sin almas', de 45 minutos, con testimonios de ex presos políticos, entre ellos las ex presas Vivian Castro, Reina Peñate, Marta de la Paz y Anet Escandón.

También hubo testimonios publicados mucho antes. Armando Valladares publicó en 1985 'Contra toda esperanza', uno de los primeros testimonios publicados sobre los plantados. Y según Tania Díaz Castro, en junio de 1988 Ernesto Díaz grabó en su celda una entrevista con Mario Chanes de Armas que después transmitió Radio Martí.

Así que, según estas fuentes, buena parte de lo que se sabe llegó por libros, por la radio o por documentales que circulaban por canales no oficiales.""")],
 ["FR-P009", "FR-P008", "FR-P016", "FR-P012"]),

(P, "humano", [("Mi tío abuelo fue plantado. ¿Qué significaba eso?", """Que tu tío abuelo fuera plantado quiere decir que, estando preso por razones políticas, se negó a cooperar con el sistema penitenciario. Los plantados rechazaban el trabajo forzado, los programas de reeducación política y el uniforme de preso común.

En 1964 empezó en la prisión de Isla de Pinos un plan de trabajo forzado para los presos políticos, y en 1967 fueron repartidos entre otras cárceles del país.

Los que vivieron aquello lo han contado de distintas maneras. Ernesto Díaz Rodríguez, uno de ellos, escribió en su libro 'Rehenes de Castro' que contar la historia del presidio político cubano era una tarea penosa por la cantidad de sufrimiento que encerraba. Según la agencia UPECI, en 2002 se exhibió en Nueva Gerona el documental 'En un lugar sin almas', con testimonios de ex presos y ex presas políticas.

Si quieres conservar su historia, hay sitios que la recogen. Desde 2008 la Cuban Heritage Collection de la Universidad de Miami graba historias orales del exilio. Su proyecto Luis J. Botifoll reúne entrevistas, sobre todo de la primera generación de exiliados, entre ellos presos políticos como Huber Matos.

Si tu familia guarda cartas, fotos o recuerdos de él, o si alguien recuerda en qué cárceles estuvo y cuántos años, esa memoria vale mucho. Es justo el tipo de historia que esos archivos intentan no perder.""")],
 ["FR-P001", "FR-P002", "FR-P017", "FR-P008", "FR-P018"]),

(P, "contexto", [("¿Los plantados eran todos enemigos de la revolución desde el principio?", """No, y las fuentes que tenemos muestran trayectorias muy distintas.

Mario Chanes de Armas, que cumplió 30 años de prisión y fue el último plantado en salir, en 1991, había participado junto a Fidel Castro en el asalto al cuartel Moncada. Es decir, era alguien que había luchado del mismo lado que Castro antes de terminar preso.

Ernesto Díaz Rodríguez, en cambio, llegó a la cárcel por una acción armada contra el gobierno: poeta y uno de los fundadores de Alpha 66, fue capturado en 1968 durante una infiltración armada en Cuba y condenado a 15 años de prisión, que después se alargaron.

Lo que los unía como plantados no era su pasado sino su conducta en prisión: se negaron a cooperar con el sistema penitenciario y rechazaban el trabajo forzado, los programas de reeducación política y el uniforme de preso común.

Hay una parte que nuestras fuentes no cubren: la posición del gobierno cubano sobre los plantados como grupo. Lo que sí tenemos es lo que sus ministros dijeron a la misión de la ONU en 1988, por ejemplo que en el pasado algunos detenidos y presos fueron golpeados y que los responsables fueron sancionados, aunque negaron que en Cuba existiera la tortura.

Con esas fuentes, lo más preciso es decir que entre los plantados había personas de orígenes políticos distintos, unidas por su negativa a aceptar las reglas de la cárcel.""")],
 ["FR-P004", "FR-P006", "FR-P001", "FR-P026", "FR-P013"]),

# ------------------------------------------------------------------ transversal (mismo archivo de fragmentos)
(T, "hecho", [("¿Dónde se guardan los testimonios del exilio cubano y de los presos políticos?", """Uno de esos archivos está en la Universidad de Miami.

Desde 2008 la Cuban Heritage Collection de esa universidad graba historias orales del exilio. Su proyecto Luis J. Botifoll reúne entrevistas, sobre todo de la primera generación de exiliados, entre ellos presos políticos como Huber Matos. Sobre su tamaño hay dos cifras: el catálogo registra 112 piezas y UM News, el medio de la universidad, habla de 118 entrevistas.

Según UM News, la colección tiene también un proyecto de historia oral sobre derechos humanos y otro sobre el Movimiento San Isidro, que cubre las protestas en Cuba entre 2018 y 2021. Es decir, no se limita a la primera ola de exiliados.

Además de los archivos, hay testimonios publicados. Armando Valladares publicó en 1985 'Contra toda esperanza', uno de los primeros testimonios publicados sobre los plantados.

Y hay material que circuló dentro de Cuba. Según la agencia de prensa independiente UPECI, en septiembre de 2002 se exhibió en Nueva Gerona el documental 'En un lugar sin almas', de 45 minutos, con testimonios de ex presos políticos, entre ellos las ex presas Vivian Castro, Reina Peñate, Marta de la Paz y Anet Escandón.

Estos son los que aparecen en nuestras fuentes; no es una lista completa de archivos ni de testimonios.""")],
 ["FR-P018", "FR-P019", "FR-P016", "FR-P008"]),

(T, "perspectivas", [("¿El gobierno cubano dejaba salir a la gente en los años ochenta?", """Sobre eso hay versiones distintas en el informe de la misión de la ONU que visitó Cuba en 1988, y vale la pena ver las dos.

Del lado de los ciudadanos, el dato más llamativo es este: de las más de 1.600 personas que presentaron denuncias ante la misión, 1.183 afirmaron tener dificultades para salir de Cuba, temporal o definitivamente, o tener familiares que querían visitar Cuba y no podían. Es decir, más de la mitad de quienes presentaron denuncias.

Del lado del gobierno cubano, según el informe, Fidel Castro dijo a la misión que su gobierno autoriza por lo general la salida de quienes quieren irse, con excepciones como profesionales y científicos, ex oficiales de las Fuerzas Armadas, personas con secretos militares, desertores o sus familiares y jóvenes en edad de servicio militar, y responsabilizó a Estados Unidos de no conceder visas.

En la misma línea, según el informe, Carlos Rafael Rodríguez afirmó que 35.000 cubanos salieron del país entre 1983 y 1988 y 5.932 entre enero y septiembre de 1988, y atribuyó a Estados Unidos que no se llegara a las 20.000 salidas anuales previstas en el acuerdo entre ambos países. Esas cifras son las que dio él; el informe no las verifica.

Así que las dos cosas aparecen en el mismo documento: muchos cubanos se quejaban de no poder salir, y el gobierno sostenía que la mayoría podía hacerlo y que el freno estaba en los visados de Estados Unidos.""")],
 ["FR-P030", "FR-P031", "FR-P032", "FR-P013"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "presidio lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
