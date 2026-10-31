"""
generar_lote3_mariel.py — Tercer lote de ejemplos sobre el Mariel (11 ejemplos, uno de dos turnos).

Uso (desde E:\\vertex-exilio):
    python generar_lote3_mariel.py

Este lote enseña formas de responder: decir "no lo sé" cuando las fuentes no alcanzan, sostener
una conversación de dos turnos, adaptar el registro (niño, profesor, respuesta breve), ordenar en
el tiempo y señalar lo que sigue en disputa.

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_mariel.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_mariel_lote3.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_mariel.jsonl")
DESTINO = Path("datos/borrador_mariel_lote3.jsonl")
PRIMER_ID = 31

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
("hecho", [("Cuéntame el Mariel en orden, desde el principio hasta el final.", """Va en orden, con las fechas que dan las fuentes.

El 1 de abril de 1980 seis cubanos entraron a la fuerza en un autobús en la embajada del Perú en La Habana; en el incidente murió el guardia Pedro Ortiz Cabrera, alcanzado por una bala de rebote. El 4 de abril el gobierno cubano retiró la custodia de la embajada, y para el 6 de abril había dentro alrededor de 10.000 personas que querían salir del país.

El 16 de abril empezaron vuelos de evacuación hacia San José, Costa Rica, pero el gobierno cubano los suspendió a los dos días, con 678 personas evacuadas. El 20 de abril anunció que el puerto de Mariel quedaba abierto para quien tuviera a alguien que fuera a recogerlo en barco, y el 21 de abril llegaron a Cayo Hueso las primeras embarcaciones, con 48 refugiados.

Mayo fue el mes más intenso: llegaron 86.488 personas. El 14 de mayo Carter anunció un programa de cinco puntos para poner fin al éxodo, y el 17 de mayo se hundió la embarcación Olo Yumi, con 14 muertos. El 20 de junio Estados Unidos creó el estatus de "Cuban-Haitian Entrant" para los recién llegados.

El final tiene dos fechas: según Larzelere, el gobierno cubano cerró Mariel el 25 de septiembre de 1980; según Wikipedia y National Archives, el éxodo terminó en octubre de 1980 tras un acuerdo entre ambos gobiernos.""")],
 ["FR-M001", "FR-M002", "FR-M003", "FR-M005", "FR-M006", "FR-M007", "FR-M010", "FR-M016", "FR-M015", "FR-M018", "FR-M019"]),

("hecho", [("¿Cómo le explico el Mariel a mi hijo de diez años?", """Se le puede contar como la historia de mucha gente que quería irse de su país, sin esconder lo difícil pero sin asustarlo. Algo así:

"Hace mucho tiempo, en 1980, muchas personas en Cuba querían irse a vivir a otro país. Un día, el gobierno de Cuba dijo que quien tuviera a alguien que fuera a buscarlo en barco podía salir por un puerto llamado Mariel.

Entonces pasó algo muy especial: muchos cubanos que vivían en la Florida se subieron a sus barcos y cruzaron el mar para ir a buscar a quienes querían salir. Fueron alrededor de 1.700 barcos, ¡imagínate el puerto lleno de botes!

En pocos meses llegaron a Estados Unidos alrededor de 125.000 personas. Algunas pasaron momentos muy feos antes de salir: había grupos de personas que les colgaban carteles feos y les rompían cosas en sus casas, solo por querer irse. Y el viaje por mar no siempre fue fácil.

Pero llegaron, y allí empezaron una vida nueva."

Si te pregunta algo más difícil, como por qué los trataban así, puedes decirle la verdad con palabras sencillas: que en esa época a muchos de los que querían irse los trataban mal, y que esos actos los organizaban grupos como los Comités de Defensa de la Revolución, junto con escuelas. Y si en tu familia alguien vino en el Mariel, esa es la mejor parte de la historia para contarle.""")],
 ["FR-M006", "FR-M009", "FR-M011", "FR-M025", "FR-M030", "FR-M031"]),

("hecho", [("Resúmeme el Mariel rápido, que no tengo mucho tiempo.", """Va el resumen corto.

El Mariel fue la salida masiva de cubanos por mar hacia Estados Unidos en 1980. Empezó después de una crisis en la embajada del Perú en La Habana, donde para el 6 de abril se habían refugiado alrededor de 10.000 personas que querían salir del país. El 20 de abril el gobierno cubano abrió el puerto de Mariel para quien tuviera a alguien que fuera a recogerlo en barco.

Alrededor de 1.700 embarcaciones, en su mayoría de cubanos de la Florida, hicieron el viaje. En algo más de seis meses llegaron unos 125.000 cubanos, la mayor migración cubana hacia Estados Unidos en un solo episodio.

Antes de salir, muchos sufrieron actos de repudio. Al llegar, cargaron durante años con un estigma de delincuencia que los datos no respaldan: los clasificados como delincuentes graves fueron alrededor del 2,2 por ciento.

Si después quieres profundizar en alguna parte, pregúntame y te la cuento con más detalle.""")],
 ["FR-M003", "FR-M006", "FR-M009", "FR-M011", "FR-M025", "FR-M020", "FR-M041"]),

("contexto", [("¿Qué significa 'marielito'?", """"Marielito" es el nombre con que se conoce a los cubanos que llegaron a Estados Unidos durante el éxodo del Mariel, en 1980. Fueron alrededor de 125.000 personas en algo más de seis meses.

La palabra en sí solo indica por dónde salieron, pero durante años cargó con un peso negativo. La prensa estadounidense exageró la delincuencia entre los recién llegados, y la película Scarface, de 1983, ayudó a fijar estereotipos que no se corresponden con la realidad de la mayoría. A eso se sumaron las declaraciones de los dos gobiernos: en Cuba, Fidel Castro describió a la mayoría de quienes se iban como "lumpen", y en Estados Unidos la Casa Blanca habló de "criminales endurecidos".

Los datos cuentan otra cosa. Según las cifras que recoge Wikipedia, alrededor del 2,2 por ciento fue clasificado como delincuente grave bajo la ley estadounidense, y según Poorman más de la mitad de los marielitos llegó a la clase media.

Por eso, cuando la uses, conviene hacerlo con respeto y con los datos en la mano: es el nombre de un grupo de personas, no un juicio sobre ellas.""")],
 ["FR-M011", "FR-M041", "FR-M028", "FR-M017", "FR-M020"]),

("reformulacion", [
 ("Mi tía dice que en el Mariel solo salieron presos y locos. ¿Qué le digo?", """Puedes decirle, con cariño, que esa idea se repitió mucho pero que los datos no la sostienen.

Sobre los presos: según las cifras que recoge Wikipedia, unos 2.746 recién llegados, el 2,2 por ciento, fueron clasificados como delincuentes graves bajo la ley estadounidense. La historiadora María Cristina García calcula cerca del 4 por ciento involucrado en situaciones delictivas, y muchos antecedentes eran por delitos menores, como la venta en el mercado negro. Es decir, la gran mayoría no tenía antecedentes graves.

Sobre los enfermos mentales: la historiadora Lillian Guerra señala que entre quienes salieron había enfermos mentales y ancianos dependientes, pero no da ninguna cifra, así que lo honesto es no inventar un número.

¿De dónde salió la idea? En parte, de los propios gobiernos. Fidel Castro describió a la mayoría de quienes se iban como "lumpen" y elementos antisociales, y la Casa Blanca denunció que Cuba enviaba "criminales endurecidos". Después, el cine y la prensa reforzaron el estereotipo: Scarface, de 1983, es el ejemplo más conocido.

Y un dato más que puede servirle: según Poorman, más de la mitad de los marielitos llegó a la clase media."""),
 ("¿Y por qué el gobierno cubano decía eso de los que se iban?", """Las fuentes registran lo que dijo el gobierno cubano, no lo que pensaba, así que no te puedo dar su intención con certeza. Lo que sí te puedo contar es qué dijo y cómo lo dijo.

Según el discurso de Fidel Castro de mayo de 1980, el gobierno abrió Mariel como respuesta a los incidentes de la embajada del Perú y a las salidas organizadas desde la Florida, y responsabilizó a Estados Unidos y a la CIA de alentar el desorden. En ese mismo discurso describió a la mayoría de quienes se iban como "lumpen" y elementos antisociales.

Ese lenguaje no quedó en un discurso. Durante el éxodo, la prensa estatal calificó públicamente a quienes se iban con términos despectivos, y el gobierno difundió el testimonio de un agente infiltrado entre los que pidieron asilo en la embajada del Perú, que los describía como "escoria", y lo exhibió en fotomurales en la antigua sede de la embajada.

Lo que sí se puede ver es el contraste: el discurso oficial presentaba a los que se iban como lo peor de la sociedad, y los datos posteriores muestran que la gran mayoría eran personas sin antecedentes graves. Por qué el gobierno eligió ese discurso es una pregunta que cada historiador responde a su manera, y aquí prefiero no inventar una respuesta.""")],
 ["FR-M020", "FR-M028", "FR-M017", "FR-M041", "FR-M027", "FR-M026", "FR-M038", "FR-M055"]),

("humano", [("¿Hubo marielitos que se arrepintieron de haber salido de Cuba?", """Es una buena pregunta, pero en las fuentes que hemos revisado no hay datos sobre eso, así que no te puedo dar una respuesta con base, y prefiero no inventarla.

Lo que sí sabemos de cómo les fue después es parcial. Según Poorman, más de la mitad de los marielitos llegó a la clase media, y muchos cargaron durante años con un estigma que la prensa estadounidense alimentó exagerando la delincuencia. Y una minoría siguió con su situación migratoria sin resolver durante décadas: para junio de 2016 todavía quedaban 478 marielitos que no podían ser admitidos bajo la ley migratoria estadounidense.

Pero llegar a la clase media o pasar dificultades no dice nada, por sí solo, de si alguien se arrepintió. Eso solo lo pueden contar ellos.

Si te interesa de verdad, la mejor fuente son los testimonios en primera persona. El estudio de la antropóloga Mercedes Cros Sandoval, que entrevistó a 439 refugiados del Mariel entre 1980 y 1982, y las historias orales que guardan archivos como la Cuban Heritage Collection de la Universidad de Miami, son un buen lugar para empezar. Y si conoces a algún marielito, preguntarle directamente es lo mejor de todo.""")],
 ["FR-M041", "FR-M024", "FR-M037"]),

("reformulacion", [("¿Es verdad que en el Mariel obligaron a gente a subir a los barcos?", """Sí, hay fuentes que lo sostienen, aunque conviene distinguir bien qué dice cada una.

La historiadora Lillian Guerra, que cita un estudio de Clark, Lasaga y Reque de 1981, afirma que menos del 40 por ciento de los refugiados del Mariel fueron recogidos por sus familiares. Según ella, el resto fueron obligados a salir por el gobierno o salieron por iniciativa propia, después de "demostrar" ante la policía que estaban contra el gobierno, muchas veces con confesiones falsas o exageradas de conductas que la ley consideraba antisociales.

A eso se suma una acusación política. Según la cronología del historiador Alex Larzelere, el 7 de junio de 1980 la Casa Blanca denunció que el gobierno cubano estaba enviando "criminales endurecidos" sacados de sus cárceles. Esa fue la postura del gobierno de Estados Unidos.

El marco oficial de la salida era otro: el 20 de abril de 1980 el gobierno cubano anunció que el puerto de Mariel quedaba abierto para quien tuviera a alguien que fuera a recogerlo en barco, y alrededor de 1.700 embarcaciones, en su mayoría organizadas por cubanos de la Florida, fueron a buscar gente.

Lo que las fuentes no permiten es decir cuántas personas exactamente salieron obligadas. Y en cuanto a antecedentes penales graves, las cifras disponibles hablan de alrededor del 2,2 por ciento.""")],
 ["FR-M017", "FR-M006", "FR-M009", "FR-M020", "FR-M054"]),

("perspectivas", [("¿Qué cosas del Mariel todavía no están claras o se discuten?", """Varias, y conviene conocerlas para no dar por cerrado lo que sigue abierto.

La primera es cuándo terminó. Según el historiador Alex Larzelere, el gobierno cubano cerró Mariel el 25 de septiembre de 1980; según Wikipedia y National Archives, el éxodo terminó en octubre de 1980 tras un acuerdo entre ambos gobiernos.

La segunda, y la más polémica, es cuántos tenían antecedentes penales. Las cifras van desde el 2,2 por ciento clasificado como delincuente grave hasta una estimación periodística de 1985 de 16.000 a 20.000. En medio, la historiadora María Cristina García calcula cerca del 4 por ciento involucrado en situaciones delictivas.

La tercera es cuánta gente hubo en la embajada del Perú. Según la historiadora Lillian Guerra, Granma informó de 1.470, mientras que otros recuentos hablan de unas 10.800, y Larzelere da 10.856.

La cuarta es económica: si el Mariel afectó los salarios en Miami. David Card concluyó que el efecto fue marginal; George Borjas encontró una bajada en un grupo de trabajadores poco calificados, y Clemens y Hunt atribuyeron ese resultado a cambios en la muestra.

Y hay cifras que solo da una parte, como el mitin de repudio de unas 100.000 personas en la calzada de Carlos III, que es la cifra de Granma, sin un recuento independiente.

En todos estos casos, lo honesto es dar los distintos valores con su fuente y no elegir uno sin base.""")],
 ["FR-M019", "FR-M020", "FR-M033", "FR-M029", "FR-M034"]),

("perspectivas", [("Soy profesor de historia. ¿Cómo explico el Mariel en clase de forma equilibrada?", """Una buena manera es separar con claridad tres cosas: lo que está documentado, lo que dijo cada parte y lo que sigue en debate. Así los estudiantes aprenden el tema y, de paso, a leer fuentes.

Los hechos documentados son la base: en algo más de seis meses de 1980 llegaron a Estados Unidos alrededor de 125.000 cubanos por el Mariel, en unas 1.700 embarcaciones organizadas en su mayoría por cubanos de la Florida.

Después, las versiones de cada parte. El gobierno cubano, según el discurso de Fidel Castro de mayo de 1980, presentó la apertura como respuesta a los incidentes de la embajada del Perú, culpó a Estados Unidos y a la CIA, y describió a la mayoría de los que se iban como "lumpen". La Casa Blanca, según Larzelere, denunció que Cuba enviaba "criminales endurecidos". Contrastarlas con los datos es un buen ejercicio: según las cifras disponibles, alrededor del 2,2 por ciento fue clasificado como delincuente grave.

Conviene también mostrar lo que se vivió dentro de Cuba: según la historiadora Lillian Guerra, los actos de repudio contra los que pedían salir los organizaban los CDR, junto con escuelas y organizaciones de masas.

Y para terminar, un debate abierto que funciona muy bien en clase: el efecto del Mariel en los salarios de Miami, en el que economistas como David Card y George Borjas llegaron a conclusiones distintas. Así los estudiantes ven que la historia no siempre tiene una sola respuesta.""")],
 ["FR-M011", "FR-M009", "FR-M027", "FR-M028", "FR-M017", "FR-M020", "FR-M030", "FR-M029"]),

("hecho", [("¿Qué pasó el 17 de mayo de 1980?", """Ese día coincidieron dos hechos del Mariel, uno en el mar y otro en las calles de Cuba.

En el mar, ocurrió una de las tragedias más conocidas del éxodo. Se hundió al norte de Mariel la embarcación Olo Yumi, que iba sobrecargada con 52 personas. Murieron 14, y la Guardia Costera rescató a 38.

En tierra, ese mismo día se celebró la tercera de las Marchas del Pueblo Combatiente que el gobierno cubano organizó en 1980. Las otras dos habían sido el 19 de abril y el 1 de mayo, y en todas participaron escuelas, Comités de Defensa de la Revolución y organizaciones de masas.

Que los dos hechos ocurrieran el mismo día no significa que estuvieran relacionados, y las fuentes que hemos revisado no los vinculan. Pero juntos muestran las dos caras de esas semanas: mientras miles de personas cruzaban el estrecho, con riesgos como el que acabó en el hundimiento del Olo Yumi, en Cuba el gobierno sacaba a la calle a escuelas, CDR y organizaciones de masas.

Mayo de 1980 fue, además, el mes de más llegadas del Mariel: 86.488 personas, el 69 por ciento de todas las que entraron por esa vía.""")],
 ["FR-M015", "FR-M035", "FR-M010"]),

("contexto", [("¿Qué es la Ley de Ajuste Cubano y qué tuvo que ver con los marielitos?", """La Ley de Ajuste Cubano es una ley de Estados Unidos de 1966 que permite a los cubanos obtener la residencia permanente. En el caso del Mariel fue la pieza que terminó de resolver la situación legal de la mayoría.

Al llegar en 1980, los marielitos no recibieron el estatus de refugiados. El 20 de junio de 1980 Estados Unidos creó para ellos la categoría de "Cuban-Haitian Entrant", distinta de la de refugiado, que incluía también a los haitianos llegados en esos mismos meses, unos 25.000.

La solución definitiva llegó en 1984, cuando una revisión de la Ley de Ajuste Cubano de 1966 permitió a los cubanos del Mariel obtener la residencia permanente. Los haitianos que llegaron en esas fechas no recibieron ese beneficio.

Para una minoría, sin embargo, el caso no se cerró: para junio de 2016 todavía quedaban 478 marielitos que no podían ser admitidos bajo la ley migratoria estadounidense, y Estados Unidos planeaba deportar, de acuerdo con el gobierno cubano, a un número pequeño de ellos considerados delincuentes graves.

En resumen, para la gran mayoría de los marielitos la Ley de Ajuste fue la puerta a una vida legal estable en Estados Unidos; para unos pocos, el problema siguió abierto durante décadas.""")],
 ["FR-M021", "FR-M018", "FR-M012", "FR-M024"]),
]

if DESTINO.exists():
    with DESTINO.open(encoding="utf-8-sig") as f:
        revisados = [json.loads(l)["id"] for l in f if l.strip() and json.loads(l).get("estado_revision") != "pendiente"]
    if revisados:
        print(f"{DESTINO} ya tiene {len(revisados)} ejemplos revisados ({', '.join(revisados[:5])}...). No lo sobrescribo.")
        sys.exit(1)

usados = sorted({x for _, _, ids in E for x in ids})
faltan = [x for x in usados if x not in frag]
no_aprobados = [x for x in usados if x in frag and frag[x].get("estado") != "aprobado"]
if faltan or no_aprobados:
    print(f"No genero nada. Fragmentos que no existen: {faltan}. Fragmentos sin aprobar: {no_aprobados}.")
    sys.exit(1)

DESTINO.parent.mkdir(exist_ok=True)
with DESTINO.open("w", encoding="utf-8", newline="\n") as f:
    for i, (tipo, turnos, ids) in enumerate(E):
        mensajes = []
        for preg, resp in turnos:
            mensajes += [{"role": "user", "content": preg}, {"role": "assistant", "content": resp.strip()}]
        ej = {"id": f"exi-m{PRIMER_ID + i:03d}", "etapa": "mariel_1980", "tipo": tipo, "messages": mensajes,
              "fuentes": [{"id_fragmento": x, "id_fuente": frag[x]["id_fuente"], "fragmento": frag[x]["texto"]} for x in ids],
              "estado_revision": "pendiente", "revisor": "", "notas": "Lote 3"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
