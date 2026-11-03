"""
generar_lote1_caso_ochoa.py — Primer lote de ejemplos de la etapa caso_ochoa_narcotrafico (módulo "Cuba: contexto"):
el juicio de 1989, el viaje a Medellín para ver a Escobar, la versión oficial, las críticas, qué sabían los Castro,
el departamento MC, las acusaciones de EE. UU. que nunca llegaron a juicio y las consecuencias.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_caso_ochoa.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_caso_ochoa.jsonl y se niega a usar fragmentos que
no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_caso_ochoa_lote1.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_caso_ochoa.jsonl")
DESTINO = Path("datos/borrador_caso_ochoa_lote1.jsonl")
PREFIJO = "exi-oc"
PRIMER_ID = 1
NOTA = "caso_ochoa_narcotrafico lote 1"

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "caso_ochoa_narcotrafico"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "hecho", [("¿Qué fue el caso Ochoa?", """Fue el juicio de 1989 en el que el gobierno cubano condenó y fusiló a un general que había sido Héroe de la República y a otros tres oficiales, en un proceso que mezcló narcotráfico, corrupción y la acusación de traición.

En la llamada Causa 1 de 1989, un tribunal militar especial juzgó a 14 oficiales del ejército y del Ministerio del Interior. Cuatro fueron condenados a muerte: el general Arnaldo Ochoa Sánchez, el capitán Jorge Martínez Valdés, el coronel Antonio de la Guardia Font y el mayor Amado Padrón Trujillo. Los otros 10 recibieron penas de entre 10 y 30 años de prisión. Los cuatro fueron fusilados al amanecer del 13 de julio de 1989, después de que el Consejo de Estado ratificara las condenas.

Según la periodista Julia Preston, que cubrió el caso para The New York Review of Books, Ochoa fue arrestado el 12 de junio de 1989 y trece días después confesó todos los cargos ante un tribunal de honor de cuarenta y siete generales y almirantes.

En realidad había dos casos unidos. Según Preston, Tony de la Guardia dirigía el departamento MC del Ministerio del Interior, y el gobierno cubano acusó a su grupo de hacer pasar por Cuba seis toneladas de cocaína colombiana hacia Estados Unidos en los dos años posteriores a abril de 1987, a cambio de 3,4 millones de dólares. A Ochoa, en cambio, los Castro nunca lo acusaron de participar en esos envíos: se le acusó de negocios en el mercado negro de Angola, de quedarse con dinero del ejército sandinista y de planear grandes envíos de cocaína.

Por eso el caso de Ochoa en particular sigue discutiéndose: lo que se probó contra el grupo de De la Guardia fueron envíos concretos de droga; contra Ochoa, sobre todo negocios y planes.""")],
 ["FR-O001", "FR-O002", "FR-O003", "FR-O015", "FR-O018", "FR-O029"]),

(T, "hecho", [("¿Tuvo Pablo Escobar relación con el gobierno cubano?", """Hay un contacto que el propio gobierno cubano reconoció y hay acusaciones mucho más amplias que nunca se probaron en un juicio. Conviene separarlos.

Lo que salió en el juicio de 1989: según la periodista Julia Preston, en mayo de 1988 el capitán Jorge Martínez se reunió en Medellín con Pablo Escobar por orden del general Arnaldo Ochoa. Según Martínez, Escobar quería misiles tierra-aire para derribar helicópteros antidrogas colombianos y refugio en Cuba, y la idea de un laboratorio de cocaína en Cuba o Angola fue rechazada. No salió en el juicio ninguna prueba de que Ochoa llegara a hacer algo por Escobar.

La versión oficial: Fidel Castro, en su discurso ante el Consejo de Estado de julio de 1989, calificó ese viaje de «un hecho de gravedad extrema» y dijo que Ochoa conspiró para transportar droga a través de Cuba, pero no logró realizar ninguna de esas operaciones.

Las acusaciones que van más allá: según AFP, Carlos Lehder, exjefe del cártel de Medellín, afirma en su libro de 2024 que contrató con el gobierno cubano, con autorización de Escobar, una ruta de cocaína hacia las Bahamas, y que no habría podido entrar a Cuba en su avión «sin la venia de Fidel Castro». AFP aclara que esos hechos no han sido juzgados.

Según Associated Press, en 1993 los fiscales federales de Miami estudiaron acusar a Raúl Castro y a otros altos mandos de narcotráfico, pero la acusación nunca se presentó, por dudas sobre la credibilidad del testigo y por razones políticas y de inteligencia.

En resumen: el contacto con Escobar en 1988 está documentado; una alianza de los Castro con Escobar es una acusación que no se ha probado.""")],
 ["FR-O019", "FR-O009", "FR-O038", "FR-O035"]),

(T, "perspectivas", [("¿Fue justo el juicio contra Ochoa?", """Es una de las preguntas más discutidas sobre Cuba en los años ochenta, y las respuestas de las partes son opuestas.

La posición del gobierno cubano: Fidel Castro, en su discurso ante el Consejo de Estado de julio de 1989, dijo que el proceso se caracterizó por su «excepcional limpieza» y que «nunca hubo un proceso judicial con tanta participación, con tanta información, con tanta claridad y con tanta equidad». Afirmó que no se ejerció «la más mínima influencia» sobre el tribunal, que los jueces decidieron «con absoluta libertad» y que fueron ellos quienes redujeron el número de condenas a muerte que pedía el fiscal.

Lo que dice Amnistía Internacional: según su informe del 7 de julio de 1989, el juicio duró 4 días ante un tribunal militar especial, la fiscalía pidió la pena de muerte para siete de los catorce acusados, y los cargos incluían alta traición y «actos hostiles contra un Estado extranjero», en referencia a Estados Unidos. La organización, que se opone a la pena de muerte en todos los casos, temía que «consideraciones políticas» hubieran influido en el juicio y que no se respetaran las normas de un juicio con garantías.

La periodista Julia Preston, que siguió el proceso, sostiene que los acusados nunca pudieron dar su propia versión, que sus abogados apenas intervinieron y que la traición «no quedó demostrada por los hechos».

Después del juicio, según Preston, fue arrestado Elizardo Sánchez Santa Cruz, principal figura del movimiento de derechos humanos en Cuba, por criticar ante periodistas estadounidenses la falta de defensa de los acusados.

Cada lector puede pesar estas versiones; lo que nadie discute es que el proceso terminó con cuatro fusilados el 13 de julio de 1989.""")],
 ["FR-O008", "FR-O005", "FR-O006", "FR-O024", "FR-O027", "FR-O002"]),

(T, "perspectivas", [("¿Sabían Fidel y Raúl Castro del narcotráfico que se juzgó en 1989?", """No hay una respuesta probada, y las versiones chocan.

Lo que dijo el gobierno cubano: según la periodista Julia Preston, Fidel Castro afirmó que él y Raúl no supieron de la relación de Ochoa ni de De la Guardia con las drogas hasta después de los arrestos del 12 de junio de 1989. El propio Ochoa declaró ante el tribunal de honor que ni Fidel ni Raúl Castro ni nadie del partido o del gobierno «tuvo nunca nada que ver». Fidel Castro sostuvo en su discurso de julio de 1989 que Estados Unidos empezó «de mala fe» a involucrar el nombre de Raúl, porque los aviones del grupo de De la Guardia aterrizaban en áreas militares.

Lo que se dijo del otro lado: según Preston, Reinaldo Ruiz, uno de los narcotraficantes que trabajaron con ese grupo, dijo a investigadores estadounidenses que Raúl Castro estaba en la base de Varadero cuando llegó el primer cargamento, aunque no trataron directamente con él. Carlos Lehder, exjefe del cártel de Medellín, declaró en 1991 en el juicio de Noriega que era el enlace del cártel con Raúl Castro; reconoció que colaboraba con agentes federales, y el gobierno cubano negó con fuerza sus acusaciones.

Un borrador de acusación de la fiscalía federal de Miami, descrito en 1993 por Knight-Ridder, acusaba a Raúl Castro de dirigir una conspiración con el cártel de Medellín y no nombraba a Fidel Castro. Según Associated Press, esa acusación nunca se presentó, en parte por dudas sobre la credibilidad del testigo.

En resumen, hay testimonios de narcotraficantes que implican a Raúl Castro y una negativa firme del gobierno cubano; ningún tribunal ha llegado a juzgar esas acusaciones.""")],
 ["FR-O021", "FR-O020", "FR-O013", "FR-O017", "FR-O036", "FR-O033", "FR-O035"]),

(T, "contexto", [("¿Qué era el departamento MC del Ministerio del Interior?", """Era la unidad del Ministerio del Interior cubano en la que funcionó la red de narcotráfico que se juzgó en 1989.

Según la periodista Julia Preston, el departamento MC fue creado a principios de los años ochenta para burlar el embargo estadounidense llevando de contrabando tecnología médica e informática desde la Florida, y lo dirigía Antonio «Tony» de la Guardia. El gobierno cubano acusó a su grupo de hacer pasar por Cuba seis toneladas de cocaína colombiana hacia Estados Unidos en los dos años posteriores a abril de 1987, a cambio de 3,4 millones de dólares.

Cómo funcionaba, según Preston: el primer cargamento llegó el 10 de abril de 1987, cuando 240 kilos de cocaína aterrizaron con escolta de la fuerza aérea cubana en la base militar de Varadero y pasaron a lanchas rápidas guiadas por los guardacostas cubanos hacia la Florida. Hubo quince envíos exitosos, más de una tonelada se perdió en decomisos, y tras los arrestos los investigadores recuperaron 156 kilos de cocaína y 1,1 millones de dólares en efectivo.

La red ya estaba vigilada desde Estados Unidos. Según Preston, en febrero de 1988 los cubanoamericanos Reinaldo y Rubén Ruiz fueron arrestados en Miami por introducir drogas del cártel de Medellín a través de Cuba, y un piloto informante de la DEA había volado para ellos a Varadero.

Las fechas no coinciden del todo entre las fuentes: según un reportaje de Knight-Ridder de 1993, los fiscales cubanos hablaron de 6 toneladas entre 1986 y 1989, mientras que Preston habla de los dos años posteriores a abril de 1987.""")],
 ["FR-O015", "FR-O016", "FR-O017", "FR-O023"]),

(T, "reformulacion", [("A Ochoa lo fusilaron por narcotraficante, ¿no?", """Esa es la versión más repetida, pero lo que salió en el juicio es más complicado.

Según la periodista Julia Preston, los Castro nunca sostuvieron que Ochoa participara en los envíos de cocaína del grupo de Tony de la Guardia. A Ochoa se le acusó de enriquecerse en el mercado negro de Angola con recursos del ejército, de quedarse con 161.000 dólares del ejército sandinista por una compra fallida de armas, de los que Martínez depositó 115.000 en una cuenta en Panamá, y de planear grandes envíos de cocaína.

El punto más grave fue el viaje de su ayudante a Medellín. Según Preston, en mayo de 1988 Martínez se reunió con Pablo Escobar por orden de Ochoa, pero no salió en el juicio ninguna prueba de que Ochoa llegara a hacer algo por Escobar. Fidel Castro, en su discurso de julio de 1989, dijo que Ochoa conspiró para transportar droga a través de Cuba pero no logró realizar ninguna de esas operaciones, y que lo grave fue asociarse a la red del Ministerio del Interior en vez de denunciarla. Para justificar la pena, sostuvo que «la traición es vender al país y vendieron al país».

Las fuentes tampoco coinciden: según Inter Press Service, que cita fuentes oficiales cubanas, De la Guardia y Ochoa organizaron dos redes que dejaron pasar seis toneladas de cocaína por Cuba, mientras que Preston dice que los Castro nunca acusaron a Ochoa de participar en esos envíos.

Preston sostiene que la traición «no quedó demostrada por los hechos». En resumen, Ochoa fue condenado por alta traición en un caso de narcotráfico, pero lo que se probó contra él fue sobre todo corrupción y planes, no envíos de droga.""")],
 ["FR-O018", "FR-O019", "FR-O009", "FR-O010", "FR-O022", "FR-O024"]),

(T, "hecho", [("¿Quién era Arnaldo Ochoa?", """Era uno de los militares más condecorados de la Revolución cubana, lo que hizo su caída todavía más impactante.

Según la periodista Julia Preston, Ochoa combatió desde joven en la Sierra Maestra, fue nombrado Héroe de la República en 1984, dirigió las tropas cubanas en el Ogadén etíope en 1977, encabezó a los asesores militares cubanos en Nicaragua y luego la misión militar en Angola. Iba a asumir el mando del Ejército Occidental el 14 de junio de 1989, dos días después de su arresto.

Su caída fue rápida. Según Preston, fue arrestado el 12 de junio de 1989, y ante el tribunal de honor confesó y declaró que ni Fidel ni Raúl Castro ni nadie del partido o del gobierno «tuvo nunca nada que ver»; dijo que «la traición se paga con la vida» y que, si lo fusilaban, su último pensamiento sería para Fidel.

El gobierno lo presentó como alguien corrompido. Según Preston, Raúl Castro, ministro de las Fuerzas Armadas, pidió ante el tribunal de honor un «castigo ejemplar» para Ochoa, dijo que lo había dominado la «fiebre del oro» y afirmó que «su máxima aspiración era convertirse en un típico empresario capitalista».

Ochoa fue fusilado junto con De la Guardia, Martínez y Padrón al amanecer del 13 de julio de 1989, después de que el Consejo de Estado ratificara las condenas a muerte.""")],
 ["FR-O029", "FR-O003", "FR-O020", "FR-O014", "FR-O002"]),

(T, "hecho", [("¿Qué pasó después del juicio de Ochoa?", """El caso no terminó con los fusilamientos: hubo una sacudida en el Ministerio del Interior y la represión de quienes lo criticaron.

Según la periodista Julia Preston, el 29 de junio de 1989 Fidel Castro destituyó al ministro del Interior, José Abrantes, y lo sustituyó por Abelardo Colomé Ibarra. Abrantes fue arrestado el 31 de julio y el 1 de septiembre condenado a veinte años por negligencia y corrupción, aunque no se presentó prueba de que estuviera vinculado directamente con Ochoa ni con el narcotráfico. Según un reportaje de Knight-Ridder de 1993, Abrantes murió dos años después de un ataque al corazón en su celda.

También hubo consecuencias para los críticos. Según Preston, después del juicio fue arrestado Elizardo Sánchez Santa Cruz, principal figura del movimiento de derechos humanos en Cuba, junto con otros dos disidentes, acusados de «difundir noticias falsas» por criticar en entrevistas la falta de defensa de los acusados. Sánchez había dicho que el juicio fue «un asesinato público vestido de ropa judicial».

Años después el caso seguía abierto en la memoria. Según Inter Press Service, Patricio de la Guardia, hermano gemelo de Antonio, condenado a 30 años por saber de las actividades de su hermano y de Ochoa y no denunciarlas, salió de prisión casi ocho años después. Un profesor universitario dijo a IPS que «el caso Ochoa no es un caso cerrado», y el fiscal del caso, Juan Escalona, lo describió como «traumático» y «un deber amargo».""")],
 ["FR-O025", "FR-O026", "FR-O027", "FR-O028"]),

(T, "contexto", [("¿Hubo acusaciones de narcotráfico contra Cuba antes del caso Ochoa?", """Sí, varias, aunque según las fuentes los funcionarios cubanos acusados nunca llegaron a ser juzgados.

Según la periodista Julia Preston, en 1982 Estados Unidos desarticuló una red del financiero colombiano Jaime Guillot Lara que llevaba marihuana a Estados Unidos y fusiles a la guerrilla colombiana M-19. Un acusado, Johnny Crump, testificó en la Florida que era el enlace con el embajador cubano en Colombia, Fernando Ravelo Renedo, que fue acusado en Estados Unidos pero en 1989 era embajador de Cuba en Nicaragua. Cuba dio refugio a Guillot.

Según un reportaje de Knight-Ridder de 1993, en 1982 cuatro funcionarios cubanos, entre ellos un vicealmirante de la marina, fueron acusados en Estados Unidos de introducir marihuana en la Florida, pero nunca fueron arrestados ni juzgados.

Hubo más. Según Preston, el panameño José Blandón declaró ante el Senado de Estados Unidos que en junio de 1984 Fidel Castro medió en La Habana en una disputa entre Manuel Noriega y el cártel de Medellín, algo que Castro negó rotundamente. Y una acusación federal de abril de 1989 en Jacksonville sostuvo que Carlos Lehder pasó una tonelada y media de cocaína por Cuba en 1984 con ayuda de Robert Vesco.

Estas acusaciones son el contexto en el que se produjo el juicio de 1989. Según un reportaje de Knight-Ridder de 1993, Fidel Castro había negado durante años que su gobierno permitiera el narcotráfico.""")],
 ["FR-O030", "FR-O031", "FR-O032", "FR-O033"]),

(T, "reformulacion", [("En 1993 Estados Unidos acusó a Raúl Castro de narcotráfico, ¿verdad?", """No exactamente: se preparó un borrador de acusación, pero nunca se presentó ante un tribunal.

Según un reportaje de Jeff Leen (Knight-Ridder, abril de 1993) sobre un borrador de acusación de la fiscalía federal de Miami, ese borrador, de 17 páginas, acusaba al gobierno cubano de ser una organización criminal y a Raúl Castro de dirigir durante diez años una conspiración con el cártel de Medellín para pasar al menos 7,5 toneladas de cocaína por Cuba entre 1980 y 1990, con 15 funcionarios como coconspiradores, entre ellos Manuel Piñeiro, Abelardo Colomé y José Abrantes. No nombraba a Fidel Castro.

Según el mismo reportaje, el borrador hablaba de frecuencias de radio especiales para los narcotraficantes, avisos por radar sobre los guardacostas estadounidenses y jefes del cártel viviendo en Cuba, y se basaba en viejos casos de Miami, en desertores cubanos y en el testimonio de Carlos Lehder.

Según Associated Press, la acusación nunca se presentó, por dudas sobre la credibilidad del testigo y por el temor a poner en riesgo operaciones de inteligencia y el acercamiento del gobierno de Clinton.

Incluso los detalles varían entre fuentes: según el borrador, Lehder viajó a Cuba por primera vez en 1979, mientras que en su propio testimonio de 1991 dijo que fue en 1981.

Así que lo correcto es decir que en 1993 los fiscales de Miami prepararon una acusación contra Raúl Castro por narcotráfico, pero que nunca llegó a presentarse.""")],
 ["FR-O033", "FR-O034", "FR-O035", "FR-O037"]),

(T, "humano", [("Mi papá era militar en Cuba en el 89 y dice que nadie se creyó el juicio de Ochoa, que todo el mundo esperaba que lo perdonaran. ¿Eso es cierto?", """Las dudas que recuerda tu papá aparecen también en lo que escribieron quienes cubrieron el caso, aunque la versión oficial dice lo contrario.

Según la periodista Julia Preston, el juicio se grabó y se transmitió por televisión en Cuba con dos días de retraso para editarlo, en total más de veintitrés horas, y Fidel Castro admitió que se cortaron partes. Preston sostiene que los acusados nunca pudieron dar su propia versión y que no había forma de saber qué presiones produjeron las confesiones.

Sobre el perdón, las fuentes que tenemos no miden qué esperaba la gente, pero sí cuentan cómo se decidió. Según el Deseret News, los 29 miembros del Consejo de Estado votaron por unanimidad ratificar las condenas a muerte, y Fidel Castro sostuvo que los cuatro debían ser fusilados para restaurar la fe en la Revolución y asegurar la disciplina en las fuerzas armadas. Fidel Castro afirmó además que, antes de decidir, consultó al Buró Político, al Comité Central y a los diputados, y que casi todos pidieron la pena más severa. Esa es la versión oficial, y en las fuentes que tenemos no hay forma independiente de comprobarla.

La duda no se apagó con los años. Según Inter Press Service, cuando Patricio de la Guardia salió de prisión en 1997, un profesor universitario dijo que «el caso Ochoa no es un caso cerrado».

Así que tu papá no está solo en su recuerdo: hubo dudas desde el principio y siguen existiendo. Si conserva recuerdos de esos días en el ejército, son un testimonio valioso de cómo se vivió el caso dentro de las fuerzas armadas.""")],
 ["FR-O004", "FR-O024", "FR-O007", "FR-O011", "FR-O028"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": NOTA}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
