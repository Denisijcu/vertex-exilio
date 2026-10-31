"""
generar_lote2_transversal.py — Segundo lote de ejemplos transversales: el embargo de Estados Unidos a Cuba
(que el gobierno cubano llama 'bloqueo') y los militares cubanos en Venezuela.

Uso (desde E:\\vertex-exilio):
    python generar_lote2_transversal.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_transversal.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_transversal_lote2.jsonl con todos los ejemplos en estado 'pendiente'.

Usa los fragmentos FR-T044 a FR-T074. El modelo no da veredicto sobre si el embargo es la causa de la crisis:
pone lo comprobable (votos, medidas, lo que muestra un video, citas con fecha) al lado de lo que dice cada
gobierno. Donde el gobierno cubano dijo una cosa y luego reconoció otra (Venezuela), se muestran las dos citas.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_transversal.jsonl")
DESTINO = Path("datos/borrador_transversal_lote2.jsonl")
PREFIJO = "exi-t"
PRIMER_ID = 16

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "transversal"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "hecho", [("¿Qué pasó en la votación de la ONU sobre el embargo a Cuba en 2026?", """El 28 de octubre de 2026 la Asamblea General de la ONU aprobó por trigésima cuarta vez desde 1992 la resolución presentada por Cuba que pide poner fin al embargo de Estados Unidos. El resultado fue de 130 votos a favor, 17 en contra y 25 abstenciones. Un año antes, el mismo texto había recibido 165 votos a favor, 7 en contra y 12 abstenciones. Es una resolución no vinculante: no obliga a Estados Unidos a nada.

Según Noticias ONU, fue el menor número de votos a favor de los últimos 20 años, y el cambio se notó sobre todo en América Latina.

Según la agencia EFE, votaron en contra, además de Estados Unidos e Israel, Argentina, Colombia, Costa Rica, Ecuador, Paraguay, Hungría, Marruecos, Ucrania y Emiratos Árabes Unidos. Se abstuvieron Chile, Honduras, Perú, Alemania, Grecia, Italia y República Dominicana. Venezuela no votó porque tenía suspendido su derecho a voto por deudas con la ONU.

El contexto pesó. Según EFE, la votación coincidió con dos órdenes ejecutivas de Trump que establecen sanciones contra quienes vendan petróleo a Cuba o comercien con la isla, y Estados Unidos había pedido a los miembros de la ONU que votaran en contra.

Así que la resolución volvió a aprobarse por amplia mayoría, pero con bastante menos apoyo que en años anteriores.""")],
 ["FR-T044", "FR-T045", "FR-T046", "FR-T059"]),

(T, "perspectivas", [("¿A Cuba se le aplica un bloqueo o un embargo?", """Depende de quién hable, y la palabra misma es parte de la discusión.

El gobierno cubano lo llama «bloqueo». Según Noticias ONU, el canciller Bruno Rodríguez culpó al embargo, que su gobierno llama bloqueo, del sufrimiento del pueblo cubano y concluyó en la Asamblea General de 2026: 'Cuba no es una amenaza, el bloqueo sí'.

El gobierno de Estados Unidos rechaza esa palabra. Según Noticias ONU, su embajador ante la ONU, Mike Waltz, afirmó 'No hay bloqueo' y citó más de 876 millones de dólares en exportaciones estadounidenses a Cuba en ocho meses de 2026, además de envíos de Canadá, España, México, China, Rusia, la Unión Europea y la ONU. Según Telemundo, Estados Unidos considera el embargo una herramienta de presión para lograr una transición democrática, elecciones libres, respeto a los derechos humanos y compensación por las propiedades nacionalizadas después de 1959.

La propia resolución de la ONU recoge una de las críticas más concretas. Según Noticias ONU, expresa preocupación por la Ley Helms-Burton de 1996 por sus efectos extraterritoriales sobre otros países, es decir, porque su alcance llega también a otros países.

Por eso, para hablar con neutralidad, lo más preciso es decir 'embargo de Estados Unidos', que es el término técnico, y aclarar que el gobierno cubano lo llama bloqueo. Cada palabra lleva detrás una posición.""")],
 ["FR-T050", "FR-T049", "FR-T058", "FR-T048"]),

(T, "reformulacion", [("El gobierno cubano dice que todos los problemas de Cuba son por el bloqueo. ¿Es así?", """Es lo que sostiene el gobierno cubano, pero no es la única explicación, y las fuentes que tenemos no permiten reducirlo todo a una sola causa.

La versión oficial cubana es clara. Según Europa Press, en septiembre de 2026 el gobierno cubano estimó en unos 8.083 millones de dólares los daños causados por las medidas de Estados Unidos en un año, y en 178.700 millones el daño acumulado. Según Noticias ONU, el canciller afirmó en la ONU que la mortalidad infantil se había duplicado. Son cifras del gobierno cubano que no hemos podido contrastar con otra fuente.

El gobierno de Estados Unidos dice lo contrario. Según Noticias ONU, su embajador Mike Waltz sostuvo que la crisis cubana se debe al propio gobierno de la isla y que la riqueza del país 'simplemente cambió de manos', de la población a las élites dirigentes.

Hay medidas de 2026 que sí están documentadas. Según el Servicio de Investigación del Congreso de Estados Unidos, el 29 de enero de 2026 Trump firmó una orden que permite imponer aranceles a los países que suministren petróleo a Cuba, y Estados Unidos cortó el petróleo venezolano, que era su principal proveedor. El máximo representante de la ONU en Cuba advirtió de una crisis energética y de un posible colapso humanitario.

Y hay quienes ven las dos cosas a la vez. Según el mismo informe del Congreso, algunos expertos temen las consecuencias humanitarias de más presión económica, mientras otros la apoyan como vía de cambio político.

Lo que muestran las fuentes es que las medidas de 2026 afectaron el suministro de petróleo de la isla; cuánto pesan las medidas de Estados Unidos frente a las decisiones del propio gobierno cubano es justo lo que está en disputa.""")],
 ["FR-T051", "FR-T050", "FR-T049", "FR-T055", "FR-T052", "FR-T057"]),

(T, "contexto", [("¿Siempre ha votado casi todo el mundo contra el embargo en la ONU?", """No siempre, y el apoyo ha subido y bajado según la época.

En 1992, primer año en que se votó la resolución, hubo 59 votos a favor, 3 en contra, 71 abstenciones y 46 ausencias. Es decir, al principio la mayoría de los países no se pronunció.

El máximo apoyo llegó en 2015 y 2017, con 191 votos a favor y 2 en contra, durante el acercamiento entre Estados Unidos y Cuba del gobierno de Obama. En 2016 Estados Unidos se abstuvo por primera vez.

En 2026 hubo un giro. La resolución se aprobó con 130 votos a favor, 17 en contra y 25 abstenciones, frente a 165, 7 y 12 en 2025. Según Noticias ONU, fue el menor apoyo de los últimos 20 años. Según la agencia EFE, entre los que votaron en contra estuvieron Argentina, Colombia, Costa Rica, Ecuador y Paraguay, y entre los que se abstuvieron, Alemania, Italia, Chile y Perú.

Cada gobierno leyó el resultado a su manera. Según Al Jazeera, el embajador estadounidense Mike Waltz dijo que estaba satisfecho de que grandes economías como Corea y Alemania hubieran cambiado de posición: 'La diplomacia lleva tiempo'.

Así que el apoyo ha cambiado con el contexto político: fue máximo durante el acercamiento de Obama y bajó en 2026, en plena presión del gobierno de Trump.""")],
 ["FR-T047", "FR-T044", "FR-T045", "FR-T046", "FR-T066"]),

(T, "hecho", [("¿Qué medidas tomó Estados Unidos contra el gobierno cubano en 2025 y 2026?", """Según las fuentes que tenemos, la presión de Estados Unidos aumentó mucho en esos dos años.

Según el Servicio de Investigación del Congreso de Estados Unidos, desde enero de 2025 el gobierno de Trump mantuvo a Cuba en la lista de Estados patrocinadores del terrorismo, impuso restricciones de visado por el programa cubano de exportación de mano de obra y ordenó endurecer las normas sobre viajes y remesas. El objetivo declarado era promover la democracia, los derechos humanos y la economía de mercado en Cuba.

La medida más fuerte llegó en 2026. Según el mismo informe, el 29 de enero de 2026 Trump firmó una orden ejecutiva que declaró una emergencia nacional respecto a Cuba y creó un sistema para imponer aranceles a los países que suministren petróleo a Cuba directa o indirectamente. Tras la captura de Nicolás Maduro en enero de 2026, Estados Unidos cortó el petróleo venezolano a Cuba, su principal proveedor desde principios de los años 2000.

Según la agencia EFE, para octubre de 2026 había dos órdenes ejecutivas que establecían sanciones contra quienes vendieran petróleo a Cuba o comerciaran con la isla.

Las opiniones sobre estas medidas están divididas. Según el informe del Congreso, algunos expertos, ex funcionarios y organizaciones religiosas cubanas temen sus consecuencias humanitarias y migratorias, mientras que otros, entre ellos un destacado exiliado cubano, las apoyan como la mejor vía para un cambio político; y algunos expertos dudan de que el gobierno cubano caiga solo por medios económicos.""")],
 ["FR-T056", "FR-T055", "FR-T059", "FR-T057"]),

(T, "perspectivas", [("¿Qué pasó con el diplomático cubano que Estados Unidos expulsó en octubre de 2026?", """Hubo dos incidentes seguidos, y conviene separar lo que se vio de lo que dice cada gobierno.

El primero está comprobado. El 27 de octubre de 2026, durante el debate sobre el embargo en la Asamblea General, el canciller cubano Bruno Rodríguez interrumpió con una moción de orden el discurso del embajador estadounidense Mike Waltz; hubo un enfrentamiento a gritos y el presidente de la Asamblea suspendió brevemente la sesión. Según Telemundo, Waltz mostraba imágenes de bienes de lujo que atribuyó a dirigentes cubanos cuando Rodríguez y el embajador cubano se acercaron al podio, y Waltz respondió: 'Esto no es La Habana. No me vas a intimidar'.

El segundo quedó en video. Según Telemundo, en las imágenes difundidas por Waltz se ve al primer secretario de la misión cubana, Richard Tur de la Concepción, golpear o apartar varias veces el teléfono de una persona que lo grababa, identificada como portavoz del embajador estadounidense, mientras protesta por la grabación y pide la intervención de seguridad.

Cada gobierno lo cuenta a su manera. Según Telemundo, Waltz anunció que Marco Rubio había firmado la expulsión de Tur, a quien acusó de haber empujado e intentado agredir a un diplomático estadounidense, con 24 horas para salir hacia La Habana. Según teleSUR, la misión del gobierno cubano protestó ante el secretario general de la ONU por lo que llamó 'acoso, acecho e invasión del espacio personal' del portavoz de Waltz contra Tur.

Lo que muestra el video, según el medio que lo describe, es que Tur golpeó o apartó el teléfono mientras lo grababan. Si hubo además un empujón a una persona es lo que afirma Washington; que la grabación fuera acoso es lo que afirma La Habana.""")],
 ["FR-T060", "FR-T061", "FR-T062", "FR-T063", "FR-T064"]),

(T, "hecho", [("¿Había militares cubanos en Venezuela?", """Sí. El propio gobierno cubano lo reconoció en enero de 2026, después de años de negarlo.

El 4 de enero de 2026 el gobierno cubano confirmó que 32 cubanos, miembros de las Fuerzas Armadas Revolucionarias y del Ministerio del Interior, murieron durante la operación militar de Estados Unidos del 3 de enero de 2026 en Venezuela, en la que Nicolás Maduro fue capturado. Según el gobierno cubano, cumplían misiones 'a solicitud de órganos homólogos' venezolanos, y Díaz-Canel decretó dos días de duelo nacional.

Ya había indicios antes. Según Factchequeado, Reuters reveló dos acuerdos de mayo de 2008 que dieron a Cuba amplio acceso al sector militar venezolano, y un experto de la Misión de Determinación de Hechos de la ONU sobre Venezuela dijo que ex funcionarios de la inteligencia militar venezolana declararon haber sido adiestrados por personal militar cubano. La cancillería cubana calificó entonces de 'falsas' esas denuncias.

Lo que no se sabe es cuántos eran. Según Factchequeado, no existe un conteo definitivo; en 2015 El Nuevo Herald habló de unos 20.000 combatientes cubanos, con base en estimaciones de un general venezolano retirado.

Estados Unidos lo había dicho antes de la confirmación cubana. Según Factchequeado, Trump dijo que 'muchos cubanos murieron' en la operación, y Marco Rubio afirmó que los guardias de Maduro y toda su agencia de espionaje 'estaban llenos de cubanos'.""")],
 ["FR-T067", "FR-T073", "FR-T074", "FR-T072"]),

(T, "reformulacion", [("¿Es verdad que Cuba negó tener militares en Venezuela y después reconoció que murieron 32?", """Sí, las dos cosas están documentadas, con fechas y citas.

Primero lo negó. Según Factchequeado, en abril de 2019 Miguel Díaz-Canel escribió que 'no hay operaciones militares, ni tropas cubanas en Venezuela'. Johana Tablada, entonces subdirectora de Estados Unidos en la cancillería, dijo que 'no es posible retirar tropas que son inexistentes', y el canciller Bruno Rodríguez negó la presencia de tropas y exigió pruebas a Estados Unidos.

La negativa siguió años después. Según Factchequeado, el 19 de diciembre de 2024 el viceministro de Relaciones Exteriores Carlos Fernández de Cossío dijo que 'nadie ha visto nunca un batallón cubano en Venezuela' y que 'no hay tropas. Cuba no participa en operaciones militares ni en operaciones de seguridad en Venezuela'.

Después lo reconoció. El 4 de enero de 2026 el gobierno cubano confirmó que 32 cubanos, miembros de las Fuerzas Armadas Revolucionarias y del Ministerio del Interior, murieron durante la operación militar de Estados Unidos del 3 de enero de 2026 en Venezuela, y decretó dos días de duelo nacional.

En su comunicado, según Infobae, la Presidencia de Cuba dijo que los cubanos 'cayeron, tras férrea resistencia, en combate directo contra los atacantes o como resultado de los bombardeos', y Díaz-Canel dijo que protegían la vida de Maduro y de su esposa 'por solicitud de esa hermana nación'.

Puestas una al lado de la otra, las declaraciones de 2019 y 2024 y el reconocimiento de 2026 no se pueden conciliar: decir que Cuba 'no participa en operaciones de seguridad en Venezuela' y luego que sus militares murieron protegiendo a Maduro son afirmaciones contradictorias.""")],
 ["FR-T068", "FR-T069", "FR-T067", "FR-T070"]),

(T, "perspectivas", [("¿Cómo presentó el gobierno cubano la muerte de sus militares en Venezuela?", """El gobierno cubano los presentó como héroes caídos en defensa de un país aliado, y Estados Unidos dio otra lectura de su presencia allí.

El 4 de enero de 2026 el gobierno cubano confirmó que 32 cubanos, miembros de las Fuerzas Armadas Revolucionarias y del Ministerio del Interior, murieron durante la operación militar de Estados Unidos del 3 de enero en Venezuela, y decretó dos días de duelo nacional.

Según el comunicado de la Presidencia de Cuba recogido por Infobae, los cubanos 'cayeron, tras férrea resistencia, en combate directo contra los atacantes o como resultado de los bombardeos'. Díaz-Canel dijo que protegían la vida de Maduro y de su esposa 'por solicitud de esa hermana nación' y llamó a la operación 'criminal ataque'.

El homenaje fue público. Según Al Jazeera, el 15 de enero de 2026 los restos llegaron a La Habana en ataúdes cubiertos con la bandera; Díaz-Canel y Raúl Castro los recibieron con uniforme militar, miles de personas se alinearon al paso de la caravana y el ministro del Interior, Lázaro Alberto Álvarez, dijo que habían combatido 'hasta la última bala'.

La versión de Estados Unidos se centra en lo que hacían allí. Según Factchequeado, antes de la confirmación cubana Trump dijo que 'muchos cubanos murieron' y Marco Rubio afirmó que los guardias de Maduro y toda su agencia de espionaje 'estaban llenos de cubanos'.

Lo que ninguna de las dos partes discute es que había militares cubanos protegiendo a Maduro; lo que cambia es cómo se juzga: misión solidaria para La Habana, aparato de seguridad cubano en Venezuela para Washington.""")],
 ["FR-T067", "FR-T070", "FR-T071", "FR-T072"]),

(T, "humano", [("Mi primo en Cuba dice que casi no tienen corriente. ¿Por qué hay tantos apagones en 2026?", """Lo que vive tu primo coincide con lo que describen las fuentes de 2026, y sobre las causas cada gobierno da una explicación distinta.

Hay un hecho importante ese año: el petróleo. Según el Servicio de Investigación del Congreso de Estados Unidos, el 29 de enero de 2026 Trump firmó una orden que permite imponer aranceles a los países que suministren petróleo a Cuba, y tras la captura de Nicolás Maduro, Estados Unidos cortó el petróleo venezolano, que era el principal proveedor de Cuba desde principios de los años 2000.

La ONU dio la voz de alarma. Según Noticias ONU, el máximo representante de la ONU en Cuba, Francisco Pichón, advirtió de una crisis energética y de un posible colapso humanitario, y la Organización Mundial de la Salud alertó de que la escasez de energía estaba afectando a la salud.

El gobierno cubano lo atribuye a Estados Unidos. Según Europa Press, el canciller habló de 'largos meses' con solo 2 o 3 horas diarias de electricidad y culpó a las medidas estadounidenses.

El gobierno de Estados Unidos lo ve de otra manera. Según Noticias ONU, su embajador Mike Waltz sostuvo que la crisis cubana se debe al propio gobierno de la isla.

Así que, por lo que dicen las fuentes, 2026 combinó el corte del petróleo venezolano con una crisis energética que la propia ONU consideró muy grave; cuánto se debe a las medidas de Estados Unidos y cuánto a decisiones del gobierno cubano es parte de lo que se discute. Ojalá a tu primo le llegue pronto un poco de alivio.""")],
 ["FR-T055", "FR-T052", "FR-T051", "FR-T049"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "transversal lote 2 (embargo y Venezuela)"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
