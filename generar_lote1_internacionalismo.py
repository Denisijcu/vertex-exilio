"""
generar_lote1_internacionalismo.py — Primer lote de ejemplos de la etapa internacionalismo_militar (módulo "Cuba:
contexto"): Angola (origen, costo humano, Cuito Cuanavale, fin), Etiopía, Nicaragua, El Salvador y el debate sobre si
Cuba actuaba por cuenta propia o de la URSS.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_internacionalismo.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_internacionalismo.jsonl y se niega a usar fragmentos
que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_internacionalismo_lote1.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_internacionalismo.jsonl")
DESTINO = Path("datos/borrador_internacionalismo_lote1.jsonl")
PREFIJO = "exi-im"
PRIMER_ID = 1
NOTA = "internacionalismo_militar lote 1"

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "internacionalismo_militar"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "hecho", [("¿Por qué Cuba mandó tropas a Angola en 1975?", """Las fuentes coinciden en lo básico: Cuba intervino a petición del MPLA y cuando Sudáfrica ya había invadido Angola. Discrepan en los motivos de fondo.

Según Inter Press Service, el primer contingente militar cubano llegó en octubre de 1975 a petición de Agostinho Neto, líder del MPLA, que fue presidente al declararse la independencia el 11 de noviembre. La llegada de las tropas cubanas se consideró decisiva para que Luanda no cayera en manos de la UNITA, apoyada por Zaire, Estados Unidos y Sudáfrica.

El historiador Piero Gleijeses, el primero en consultar los archivos cubanos cerrados, concluye, según el National Security Archive, que Fidel Castro decidió enviar tropas el 4 de noviembre de 1975 como respuesta a la invasión sudafricana, y no al revés, como sostuvo el gobierno de Ford. Según el resumen de su estudio de 2006 en The Wilson Quarterly, Castro intervino porque la derrota del MPLA habría sido la victoria del apartheid.

La versión oficial cubana va en la misma línea. Fidel Castro dijo en 2005 que, cuando las columnas sudafricanas avanzaban hacia Luanda, solo había en Angola un pequeño grupo de instructores militares cubanos, llegados a petición de Neto para entrenar al nuevo ejército; que ocho murieron en un ataque sudafricano a principios de noviembre de 1975, y que entonces Cuba decidió enviar tropas en la Operación Carlota.

Gleijeses también señala límites: sostiene que, aunque Cuba salvó a Angola de la intervención sudafricana, el MPLA se volvió represivo y corrupto. Es decir, el motivo inmediato de la intervención está bastante documentado; su balance sigue discutiéndose.""")],
 ["FR-I009", "FR-I002", "FR-I008", "FR-I014"]),

(T, "perspectivas", [("¿Cuba fue a África por orden de la Unión Soviética?", """Es una de las grandes discusiones de la Guerra Fría, y los documentos que han salido después cambiaron bastante el debate.

Según el National Security Archive, que resume el trabajo del historiador Piero Gleijeses con archivos cubanos, Cuba tomó la decisión de enviar tropas a Angola sin informar a la Unión Soviética y desplegó sus tropas sin ninguna ayuda soviética durante los dos primeros meses. Según el resumen de su estudio de 2006 en The Wilson Quarterly, el líder soviético Leonid Brezhnev se opuso al envío, y Cuba y la URSS chocaron repetidamente sobre la estrategia en el sur de África. Un estudio interagencias de Estados Unidos de 1978 concluyó que Cuba no actuaba en África «solo ni principalmente» por los soviéticos.

La versión del gobierno cubano coincide en esto: Fidel Castro dijo años después que los soviéticos «no fueron consultados» y que después presionaron «fuertemente» para una retirada rápida.

El Departamento de Estado de Estados Unidos sostenía en 1981 otra visión, al menos para Etiopía: que allí los soviéticos dieron el mando y control general, el material y el transporte a los soldados cubanos, y que las costosas actividades de Cuba en el exterior habrían sido imposibles sin la ayuda soviética.

Las dos cosas no son del todo incompatibles. Según el mismo resumen de Gleijeses, Moscú elogió la intervención en Etiopía y suministró las armas cubanas, aunque el historiador concluye que Cuba no fue un peón del Kremlin, al menos en Angola.

En resumen, los documentos disponibles indican que en Angola Cuba decidió por su cuenta, y que las armas las ponía la URSS.""")],
 ["FR-I002", "FR-I007", "FR-I015", "FR-I027", "FR-I008"]),

(T, "hecho", [("¿Cuántos cubanos murieron en las guerras de África?", """La única cifra oficial es la del gobierno cubano, y no incluye a los heridos ni a los enfermos.

Según Inter Press Service, las cifras del gobierno cubano indican que en todas las misiones «internacionalistas» en África, desde principios de los años sesenta hasta la salida del último soldado de Angola el 25 de mayo de 1991, murieron 2.077 cubanos. Los restos que pudieron recuperarse se repatriaron en diciembre de 1989, en la llamada Operación Tributo.

La cifra no es solo de Angola: abarca todas las misiones en África. El resumen del estudio del historiador Piero Gleijeses en The Wilson Quarterly habla de que Cuba perdió más de 2.000 soldados en África, en línea con la cifra oficial. Fidel Castro dio la misma cifra en su discurso de 2005, cuando dijo que 2.077 cubanos murieron en África.

Lo que no se sabe: según el mismo reportaje de IPS, no hay estadísticas oficiales sobre los heridos, discapacitados o enfermos de la guerra. Lo que sí se sabe es que los primeros casos de VIH/sida detectados en Cuba fueron de soldados que volvían de África a mediados de los años ochenta.

Para poner la cifra en contexto: según IPS, unos 350.000 cubanos participaron en la guerra de Angola entre 1975 y 1988.

En resumen, la cifra de muertos que se repite es la oficial, y las fuentes que tenemos no la verifican de forma independiente; y del costo en heridos y enfermos no hay datos públicos.""")],
 ["FR-I010", "FR-I006", "FR-I017", "FR-I011", "FR-I009"]),

(T, "humano", [("Mi tío estuvo en Angola y nunca habla de eso. Cuando le pregunto cambia el tema. ¿Le pasó algo malo allá?", """No te puedo decir qué vivió tu tío en particular, pero lo que cuentas se parece a lo que han contado otras familias cubanas.

Según un reportaje de Inter Press Service de 2005, un cubano dijo de su hermanastro, que estuvo en Angola, que «nunca menciona la guerra». Otros veteranos lo vivieron distinto: un oficial retirado contó que fue porque quería. No hay una sola forma de cargar con eso.

Algunas cosas sí se saben. Según IPS, no hay estadísticas oficiales sobre los heridos, discapacitados o enfermos de la guerra. Según cifras del gobierno cubano, en todas las misiones en África murieron 2.077 cubanos, desde principios de los años sesenta hasta la salida del último soldado de Angola en 1991. Y aunque alistarse era oficialmente voluntario, negarse costaba la expulsión del Partido o de la Unión de Jóvenes Comunistas, y el que no iba se arriesgaba a que lo llamaran cobarde.

No fueron solo soldados: según IPS, más de 50.000 civiles cubanos participaron en la ayuda no militar a Angola, en salud, educación y construcción.

Si quieres acercarte a él, a veces ayuda no preguntar por la guerra, sino por la vida de entonces: cómo era el lugar, quiénes eran sus compañeros. Y si notas que le pesa mucho, un profesional de la salud mental con experiencia en veteranos puede ayudarlo, si él quiere. Lo que vivió es parte de la historia de muchas familias cubanas, y su silencio también es una forma de contarla.""")],
 ["FR-I012", "FR-I011", "FR-I010", "FR-I013"]),

(T, "reformulacion", [("Todos los que fueron a Angola fueron voluntarios, eso lo sabe todo el mundo.", """Es la versión oficial, pero los testimonios recogidos por la prensa muestran un cuadro más matizado.

La posición del gobierno cubano: Fidel Castro dijo en su discurso de 2005 que más de 300.000 combatientes y cerca de 50.000 colaboradores civiles cumplieron misión en Angola «de forma absolutamente voluntaria».

Lo que cuenta Inter Press Service en un reportaje desde La Habana en 2005: alistarse para Angola era oficialmente voluntario, pero negarse costaba la expulsión del Partido Comunista o de la Unión de Jóvenes Comunistas, y en una sociedad «machista» el que no iba se arriesgaba a que lo llamaran cobarde. Al mismo tiempo, un oficial retirado contó que fue porque quería.

Las dos cosas pueden ser ciertas a la vez: hubo quienes fueron por convicción y hubo una presión social y política fuerte sobre quienes dudaban. Ninguna de las fuentes que tenemos mide cuántos fueron en cada situación.

Tampoco hay datos completos del costo. Según IPS, no hay estadísticas oficiales sobre los heridos, discapacitados o enfermos de la guerra, y los primeros casos de VIH/sida detectados en Cuba fueron de soldados que volvían de África a mediados de los años ochenta.

Las cifras tampoco coinciden: según IPS participaron unos 350.000 cubanos entre 1975 y 1988, mientras que Fidel Castro habló de más de 300.000 combatientes.

Así que lo más exacto sería decir que la participación era oficialmente voluntaria, pero que negarse tenía consecuencias.""")],
 ["FR-I017", "FR-I012", "FR-I011", "FR-I013", "FR-I018"]),

(T, "perspectivas", [("¿Quién ganó la batalla de Cuito Cuanavale?", """Depende de a quién le preguntes, y cada parte tiene su versión.

La versión cubana: Fidel Castro dijo en 2005 que en 1987-1988 Cuba reunió 55.000 soldados en Angola, cifra que Inter Press Service sitúa en unos 53.000 para la etapa final, y habló de «contundentes victorias» que obligaron a Sudáfrica a negociar los acuerdos firmados en la ONU en diciembre de 1988.

La versión de los veteranos sudafricanos: según el columnista Drew Forrest, exeditor político del Mail & Guardian, la fuerza de defensa sudafricana (SADF) estima sus propias bajas en 31 muertos frente a 4.785 muertos de las fuerzas angolanas. Forrest sostiene que esa comparación es engañosa porque la SADF usó poco su infantería y omite los 3.000 o más muertos de la UNITA.

Lo que pasó en el terreno, según Forrest: Castro envió 15.000 de sus mejores soldados, sin informar a los soviéticos, y entre enero y marzo de 1988 las tropas sudafricanas y de la UNITA lanzaron varios asaltos contra las defensas angolanas y cubanas sin lograr romperlas.

El juicio de Forrest: ningún relato creíble sostiene que la SADF sufriera una «derrota aplastante», pero tampoco fue una victoria sudafricana; la describe como una victoria defensiva angolana y cubana y un serio revés para Sudáfrica.

El resultado político está menos discutido. Según Forrest, la salida de los cubanos se acordó en diciembre de 1988 entre Estados Unidos, Cuba, Angola y Sudáfrica, y Sudáfrica aceptó la independencia de Namibia.

Así que la batalla sigue en disputa, pero no su consecuencia: abrió el camino a la independencia de Namibia.""")],
 ["FR-I016", "FR-I018", "FR-I021", "FR-I020", "FR-I022", "FR-I023"]),

(T, "hecho", [("¿Cómo terminó la presencia militar cubana en Angola?", """Terminó con un acuerdo internacional en 1988 y una retirada que se completó en 1991, aunque las fuentes no coinciden en el mes exacto.

Según el columnista Drew Forrest, del Mail & Guardian, la salida de los cubanos de Angola se acordó en diciembre de 1988 entre Estados Unidos, Cuba, Angola y Sudáfrica. La fuerza de defensa sudafricana ya había salido de Angola en agosto de 1988, y Sudáfrica aceptó la independencia de Namibia bajo la Resolución 435 de la ONU.

La fecha de la salida del último soldado cubano se da de forma distinta: según cifras del gobierno cubano citadas por Inter Press Service fue el 25 de mayo de 1991, mientras que Forrest escribe que las últimas tropas cubanas se fueron en julio de 1991.

Para entonces la presencia cubana había sido enorme. Según IPS, en la etapa final había unos 53.000 soldados cubanos en el país, y más de 50.000 civiles cubanos participaron en la ayuda no militar a Angola. En julio de 1991 Nelson Mandela viajó a La Habana para agradecer a Fidel Castro el papel de Cuba en la lucha contra el apartheid.

El costo humano fue alto. Según cifras del gobierno cubano citadas por IPS, en todas las misiones en África murieron 2.077 cubanos, y los restos que pudieron recuperarse se repatriaron en diciembre de 1989, en la llamada Operación Tributo.""")],
 ["FR-I023", "FR-I019", "FR-I013", "FR-I010"]),

(T, "contexto", [("¿Qué hizo Cuba en Etiopía?", """Cuba envió miles de soldados en 1977 para ayudar al gobierno etíope a rechazar la invasión somalí del Ogadén, una intervención menos conocida que la de Angola y más discutida.

Según el estudio de país sobre Etiopía de la Biblioteca del Congreso de EE. UU., en 1977 una guerrilla somalí apoyada por Somalia tomó gran parte del Ogadén. Desde finales de noviembre llegaron a Etiopía una ayuda militar soviética masiva y tropas cubanas trasladadas desde Angola, que junto al ejército etíope frenaron la ofensiva. El 13 de febrero de 1978 Somalia envió su ejército regular, pero fue rechazado, y tras la recuperación de Jijiga a principios de marzo Somalia retiró sus fuerzas.

Cuántos cubanos fueron se da de forma distinta: 16.000 según el resumen del estudio del historiador Piero Gleijeses, 17.000 a finales de 1977 según la Biblioteca del Congreso y entre 13.000 y 15.000 según el Departamento de Estado en 1981.

El papel soviético también se discute. El Departamento de Estado sostenía que en Etiopía los soviéticos dieron el mando y control general, el material y el transporte a los soldados cubanos.

El balance de Gleijeses es incómodo: dice que Cuba defendió las fronteras pero sostuvo a un gobierno brutal, que con ese apoyo desató una guerra de terror contra los rebeldes de Eritrea, y que no puede condenar ni aplaudir ese papel. Según la Biblioteca del Congreso, al final de la guerra Etiopía quedó convertida en cliente militar de Moscú.""")],
 ["FR-I024", "FR-I025", "FR-I026", "FR-I027", "FR-I008"]),

(T, "hecho", [("¿Cuba ayudó a los sandinistas a llegar al poder en Nicaragua?", """Sí, y eso lo reconocen tanto las fuentes estadounidenses como los estudios académicos, aunque difieren en la escala y el momento.

La versión del gobierno de Estados Unidos: según el Departamento de Estado, en su Informe Especial n.º 90 de diciembre de 1981, Cuba ayudó a unificar las tres facciones del Frente Sandinista en 1977-1978, montó una red de suministro de armas a través de Panamá y Costa Rica, organizó una «brigada internacionalista» que combatió con los sandinistas en 1979 y puso asesores militares con sus columnas. Según el mismo informe, después del triunfo había en Nicaragua unos 5.000 cubanos, entre asesores, maestros y médicos, de ellos más de 1.500 asesores militares y de seguridad. Es la postura del gobierno de Estados Unidos.

Un matiz académico: según el politólogo William LeoGrande, en una reseña de 2011 de un estudio basado en entrevistas con comandantes del FMLN, Cuba limitó su ayuda directa a la revolución nicaragüense hasta los últimos seis meses para no provocar una intervención de Estados Unidos.

Así que la ayuda cubana existió y fue importante, sobre todo al final. Lo que estas fuentes no miden es cuánto pesó esa ayuda frente a las causas internas de la revolución nicaragüense.""")],
 ["FR-I028", "FR-I033"]),

(T, "perspectivas", [("¿Es verdad que Cuba armó a la guerrilla de El Salvador?", """Sí, Cuba ayudó a la guerrilla salvadoreña, y el propio gobierno cubano lo reconoció. Lo que se discutió fue la escala y lo que eso significaba.

La acusación de Estados Unidos: según el Libro Blanco del Departamento de Estado de febrero de 1981, varios países comunistas se comprometieron a dar a la guerrilla cerca de 800 toneladas de armas, y cerca de 200 toneladas llegaron en secreto, sobre todo a través de Cuba y Nicaragua, antes de la ofensiva de enero de 1981.

Las críticas: según The Christian Science Monitor, el Wall Street Journal y el Washington Post concluyeron que el Libro Blanco era, en el mejor de los casos, defectuoso; su responsable, Jon Glassman, admitió que partes podían ser «engañosas», y los críticos dijeron que no había apoyo concreto para la cifra de 200 toneladas. El Departamento de Estado mantuvo sus conclusiones.

Lo que reconoció La Habana: según el Departamento de Estado, en abril de 1981 Fidel Castro admitió ante un enviado de la Internacional Socialista que Cuba había enviado armas a la guerrilla. El politólogo William LeoGrande lo corrobora: Castro lo reconoció ante representantes de la Unión Interparlamentaria, y Carlos Rafael Rodríguez lo confirmó en 1982 a una delegación de la que él formaba parte.

El matiz académico: según LeoGrande, que reseña un estudio basado en entrevistas con comandantes del FMLN, Cuba suspendió la ayuda militar semanas después de la ofensiva y presionó por negociar, y la reanudó cuando Washington rechazó esos acercamientos. Para él, el debate real era si la guerra nacía de las condiciones internas de El Salvador o de La Habana y Moscú.""")],
 ["FR-I031", "FR-I032", "FR-I030", "FR-I035", "FR-I033", "FR-I034"]),

(T, "contexto", [("¿Desde cuándo estaba Cuba metida militarmente en África?", """Desde mucho antes de Angola: la intervención de 1975 fue la más grande, pero no la primera.

Según el National Security Archive, que resume el libro del historiador Piero Gleijeses basado en archivos cubanos, la política africana de Cuba incluyó ayuda a los rebeldes argelinos que luchaban contra Francia en 1961, una guerra secreta entre La Habana y Washington en Zaire en 1964-1965 y una contribución decisiva a la guerra de independencia de Guinea-Bisáu entre 1966 y 1974.

Gleijeses pudo reconstruirlo porque, según la misma fuente, fue el primer investigador con acceso a archivos cubanos cerrados, entre ellos los del Comité Central del Partido, las fuerzas armadas y la cancillería, y trabajó también en archivos de Estados Unidos y de varios países europeos.

En Angola el enfrentamiento con Estados Unidos fue directo. Según el National Security Archive, Estados Unidos conocía los planes de la invasión encubierta de Sudáfrica y colaboró militarmente con sus tropas, en contra de lo que el secretario de Estado Henry Kissinger declaró ante el Congreso en 1976.

Incluso el tamaño del primer despliegue en Angola se cuenta de forma distinta: el National Security Archive, resumiendo el libro de Gleijeses de 2002, habla de 30.000 cubanos en 1975-1976, mientras que el resumen de su estudio de 2006 habla de 36.000 soldados.

En resumen, cuando Cuba llegó a Angola ya llevaba más de una década de presencia en África.""")],
 ["FR-I004", "FR-I001", "FR-I003", "FR-I005"]),
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
