"""
generar_lote1_poder_riqueza.py — Primer lote de ejemplos de la etapa poder_y_riqueza_castro (módulo "Cuba:
contexto"): la estimación de Forbes y la respuesta de Fidel Castro, el libro del exescolta Juan Reinaldo Sánchez y
quienes lo matizan, y el debate sobre el dinero de GAESA.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_poder_riqueza.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_poder_riqueza.jsonl y se niega a usar fragmentos que
no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_poder_riqueza_lote1.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_poder_riqueza.jsonl")
DESTINO = Path("datos/borrador_poder_riqueza_lote1.jsonl")
PREFIJO = "exi-pr"
PRIMER_ID = 1
NOTA = "poder_y_riqueza_castro lote 1"

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "poder_y_riqueza_castro"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "reformulacion", [("Fidel Castro tenía 900 millones de dólares, lo dijo Forbes.", """Forbes lo estimó, que no es lo mismo que haberlo probado, y la propia revista explicó cómo llegó a esa cifra.

Según Forbes, en su lista de 2006 de fortunas de reyes, reinas y dictadores, la fortuna de Fidel Castro se estimaba en 900 millones de dólares. Para calcularla, la revista asumió que Castro tenía el control económico de una red de empresas estatales, como el Palacio de Convenciones, la corporación comercial Cimex y Medicuba, valoró esas empresas y supuso que una parte de sus ganancias iba a Castro. La propia revista advierte que estas estimaciones son «más arte que ciencia».

Forbes también aclaró qué no contó: exfuncionarios cubanos aseguraban que Castro se quedaba desde hacía años con ganancias de esas empresas y había rumores de cuentas en Suiza, pero la revista no los incluyó en su cálculo. Explicó que hace una lista aparte para gobernantes por la dificultad de separar su fortuna personal de la riqueza del Estado.

Castro respondió con un desafío. Según EFE, dijo en televisión: «Si ellos prueban que yo tengo una cuenta en el exterior de 900 millones de dólares o de un dólar, yo renuncio ahora a todas las funciones que estoy desempeñando».

Así que lo exacto sería decir que Forbes estimó en 2006 que Castro controlaba una fortuna de 900 millones, a partir de suponer que una parte de las ganancias de empresas del Estado era suya; en las fuentes que tenemos no aparece ninguna cuenta personal que lo pruebe, y Castro afirmó que su patrimonio era nulo.""")],
 ["FR-PR001", "FR-PR002", "FR-PR007", "FR-PR004"]),

(T, "perspectivas", [("¿Fidel Castro vivía con lujos o era austero como decía?", """Hay versiones opuestas, y las más detalladas vienen de personas con puntos de vista muy distintos sobre él.

La versión de Fidel Castro: según Al Jazeera, dijo en respuesta a Forbes que su patrimonio era nulo y que ganaba 900 pesos cubanos al mes, unos 40 dólares. Visitantes como el periodista francés Ignacio Ramonet, que lo entrevistó largamente, describieron, según The Guardian, un estilo de vida austero, de lectura, ejercicio y comidas sencillas.

La versión de su exescolta: Juan Reinaldo Sánchez, que fue escolta personal de Castro entre 1977 y 1994 y salió al exilio en Miami en 2008, cuenta en su libro de 2014 que Castro «nunca renunció a las comodidades capitalistas ni eligió vivir en la austeridad», que tenía una isla privada, Cayo Piedra, y que su estilo de vida era un «privilegio loco» mientras los cubanos pasaban penurias en los años noventa. Es su testimonio, y el propio coautor del libro admitió que Sánchez tenía cuentas pendientes con Castro, aunque aseguró haber comprobado su historia.

Una tercera mirada: según The Guardian, la periodista Ann Louise Bardach, que entrevistó a Castro, sostuvo que tenía la mejor comida y atención médica pero no un estilo de vida lujoso, y que su casa cerca de La Habana tenía cuatro habitaciones. Para ella lo importante era otra cosa: «Es el dueño de la isla de Cuba».

En resumen, en las fuentes que tenemos no hay pruebas de una fortuna personal, pero sí testimonios de privilegios que contrastan con la austeridad que Castro predicaba.""")],
 ["FR-PR005", "FR-PR015", "FR-PR008", "FR-PR009", "FR-PR010", "FR-PR013", "FR-PR014"]),

(T, "hecho", [("¿Quién era Juan Reinaldo Sánchez, el escolta que escribió un libro sobre Fidel?", """Fue uno de los escoltas personales de Fidel Castro durante casi dos décadas, y después de caer en desgracia escribió el libro más conocido sobre su vida privada.

Según la editorial Ediciones Península, el teniente coronel Juan Reinaldo Sánchez nació en La Habana en 1949 y murió en Miami en 2015. Fue escolta personal de Fidel Castro entre 1977 y 1994. Al anunciar su retiro fue detenido y estuvo preso hasta 1996, y en 2008, tras diez intentos fallidos, salió de Cuba hacia Miami. Escribió el libro con el periodista francés Axel Gyldén, del semanario L'Express.

Sánchez cuenta en su libro, según The Guardian, que cuando pidió retirarse cayó en desgracia, fue tachado de «traidor», encarcelado «como un perro», torturado y encerrado en una celda llena de cucarachas. Es su testimonio.

Sobre la credibilidad de su relato: según The Guardian, el coautor Axel Gyldén admitió que Sánchez tenía cuentas pendientes con Castro, pero aseguró que había comprobado su historia, y dijo que era la primera vez que alguien del círculo íntimo de Castro hablaba.

Así que es un testigo de primera mano de la vida privada de Castro, y al mismo tiempo una persona que salió de Cuba enfrentada con él. Por eso lo que cuenta conviene leerlo como su versión de los hechos, no como algo probado.""")],
 ["FR-PR008", "FR-PR012", "FR-PR013"]),

(T, "hecho", [("¿Qué cuenta el libro «La vida oculta de Fidel Castro»?", """Es el testimonio de un exescolta que describe una vida privada de Castro muy distinta de la imagen austera que él daba en público. Lo que sigue es lo que cuenta el autor, no hechos comprobados.

Según cuenta el exescolta Juan Reinaldo Sánchez en su libro de 2014, recogido por The Guardian, Castro «nunca renunció a las comodidades capitalistas ni eligió vivir en la austeridad». Según Sánchez, Castro tenía una isla privada, Cayo Piedra, al sur de Bahía de Cochinos, que él describe como un «jardín del Edén», donde recibía a invitados como Gabriel García Márquez. Viajaba a ella en el yate Aquarama II, con madera de Angola y cuatro motores enviados por Leonid Brezhnev, y tenía además una gran finca en La Habana y un bungaló con marina privada en la costa.

Sánchez también cuenta que Castro tuvo al menos nueve hijos, algo que la prensa cubana tenía prohibido mencionar, que nunca iba a ninguna parte sin al menos 10 escoltas, entre ellos dos «donantes de sangre», y que guardaba diamantes de Angola en una caja de tabacos Cohiba.

Lo que hay que tener en cuenta: según The Guardian, el coautor admitió que Sánchez tenía cuentas pendientes con Castro, aunque aseguró haber comprobado su historia. Y la periodista Ann Louise Bardach, que entrevistó a Castro, sostuvo que no tenía un estilo de vida lujoso, aunque sí la mejor comida y atención médica, y que lo importante era que «es el dueño de la isla de Cuba».

En resumen, el libro es una fuente importante, pero un solo testimonio, de alguien enfrentado con Castro.""")],
 ["FR-PR009", "FR-PR010", "FR-PR011", "FR-PR013", "FR-PR014"]),

(T, "humano", [("Mi abuela siempre dice que Fidel vivía como un cubano más, que era austero. Yo no sé qué creer.", """Es normal no saber qué creer: sobre esto hay versiones muy distintas, y ninguna se puede comprobar del todo.

Lo que dice la versión de tu abuela tiene apoyo en algunas fuentes. Según The Guardian, visitantes como el periodista francés Ignacio Ramonet, que entrevistó largamente a Castro, describieron un estilo de vida austero, de lectura, ejercicio y comidas sencillas. Y según Al Jazeera, el propio Castro dijo, en respuesta a la revista Forbes, que su patrimonio era nulo y que ganaba 900 pesos cubanos al mes, unos 40 dólares.

Hay otra versión. Según cuenta su exescolta Juan Reinaldo Sánchez en un libro de 2014, Castro «nunca renunció a las comodidades capitalistas ni eligió vivir en la austeridad», tenía una isla privada, Cayo Piedra, y un yate, el Aquarama II, y vivía con un «privilegio loco» mientras los cubanos pasaban penurias en los años noventa. Es el testimonio de una persona que terminó enfrentada con él.

Y hay una mirada intermedia: la periodista Ann Louise Bardach, que entrevistó a Castro, sostuvo según The Guardian que tenía la mejor comida y atención médica, pero no un estilo de vida lujoso, y que su casa cerca de La Habana tenía cuatro habitaciones.

Quizás lo que conoció tu abuela fue la imagen pública de Castro, y lo que cuenta Sánchez es lo que él dice haber visto por dentro. Puedes compartirle las dos versiones y conversar sobre qué piensa ella.""")],
 ["FR-PR015", "FR-PR005", "FR-PR009", "FR-PR010", "FR-PR014"]),

(T, "hecho", [("¿Qué es GAESA?", """Es el conglomerado empresarial de las fuerzas armadas cubanas, uno de los actores más poderosos y menos transparentes de la economía de la isla.

Según la economista Emily Morris, de University College London, GAESA se creó en los años noventa, durante el Período Especial, para que militares formados en gestión dirigieran empresas estatales. Las reservas internacionales de Cuba son secreto oficial, por lo que incluso la Economist Intelligence Unit tenía que estimarlas.

Quién la controla: según una investigación del Miami Herald de agosto de 2025, GAESA está supervisada por el Departamento V de las fuerzas armadas, y hasta su muerte en 2022 la dirigió el general Luis Alberto Rodríguez López-Calleja, exyerno de Raúl Castro. Desde entonces la dirige la general de brigada Ania Guillermina Lastres Morera, sin vínculos familiares conocidos con los Castro.

Su peso: según el mismo Herald, basado en documentos internos filtrados, el conglomerado completo declaró 7.200 millones de dólares de beneficio neto en los primeros ocho meses de 2023, y el economista Pavel Vidal estimó que sus beneficios brutos equivalían a cerca del 40 % del PIB oficial. Vidal la describió como «un gobierno paralelo que no rinde cuentas».

La falta de control: según el Herald, la contralora general Gladys Bejerano, que había dicho a EFE que no podía auditar a GAESA, fue destituida poco después sin explicación.

Cuánto dinero tiene realmente se discute, pero que es muy poco transparente lo reconocen tanto sus críticos como economistas que cuestionan las cifras más altas.""")],
 ["FR-PR023", "FR-PR018", "FR-PR016", "FR-PR017"]),

(T, "perspectivas", [("¿Es verdad que los militares cubanos tienen 18.000 millones de dólares guardados?", """Es la cifra de una investigación periodística de 2025, y una economista la ha cuestionado con argumentos técnicos. Hay que conocer las dos versiones.

La investigación: según el Miami Herald, basado en 22 estados financieros internos de GAESA, las empresas del conglomerado militar, sin contar Cimex, tenían en marzo de 2024 activos por 18.000 millones de dólares fácilmente convertibles en efectivo, 14.500 millones de ellos en cuentas bancarias, más que las reservas internacionales de países como Costa Rica, Uruguay o Panamá.

La objeción: según la economista Emily Morris, de University College London, no está nada claro que GAESA tenga esa cifra. El Herald no publicó los documentos, no se sabe con certeza si son auténticos, y el encabezado del único estado financiero visible indica que todo está en pesos cubanos. Si es así, los activos serían unos 746 millones de dólares, y lo depositado en bancos, unos 603 millones.

El propio Herald reconoce un problema parecido con otra parte de los activos: 234.000 millones de pesos equivalían a 9.800 millones de dólares al cambio oficial de 24 pesos, pero a solo 632 millones al cambio informal de unos 370.

La posición del gobierno cubano: según el Herald, la Contraloría y la cancillería no respondieron a sus preguntas, y Díaz-Canel dijo que los problemas de Cuba «no se deben a mala gestión del gobierno» sino a que «no hemos tenido el dinero».

Así que la cifra de 18.000 millones está en disputa. Lo que ninguna de las dos versiones discute es que GAESA es muy poco transparente.""")],
 ["FR-PR016", "FR-PR021", "FR-PR019", "FR-PR024", "FR-PR020"]),

(T, "hecho", [("¿Qué respondió Fidel Castro cuando Forbes dijo que era millonario?", """Respondió en televisión, con un desafío directo a la revista.

Según EFE, Fidel Castro respondió a Forbes el 15 de mayo de 2006 en un programa de televisión de unas cuatro horas y media. Dijo: «Si ellos prueban que yo tengo una cuenta en el exterior de 900 millones de dólares o de un dólar, yo renuncio ahora a todas las funciones que estoy desempeñando». Retó a la revista con «búsquenme un testaferro, una cuenta, búsquenme un dólar», la llamó «libelo» y dijo que era ridículo atribuirle «una fortuna sin herederos».

Según Al Jazeera, Castro llamó a la información una «calumnia repugnante», dijo que su patrimonio era nulo y que ganaba 900 pesos cubanos al mes, unos 40 dólares.

El gobierno lo respaldó. Según EFE, el presidente del Banco Central de Cuba, Francisco Soberón, calificó de «burdas y ridículas» las fórmulas de Forbes y afirmó que en la economía centralizada cubana «es totalmente imposible» que un dirigente pueda tener cuentas personales en el exterior.

No era la primera vez. Según Al Jazeera, la estimación de 2006 era casi el doble de la que Forbes daba para la reina Isabel II, y en 2005 la revista le había atribuido 550 millones, por lo que Castro había amenazado entonces con demandarla.

Ninguna de las dos partes presentó pruebas definitivas: Forbes reconocía que su cálculo se basaba en supuestos, y Castro negaba tener nada a su nombre.""")],
 ["FR-PR004", "FR-PR005", "FR-PR006", "FR-PR003"]),

(T, "reformulacion", [("GAESA es el negocio privado de la familia Castro.", """No es exactamente así: GAESA es un conglomerado de las fuerzas armadas, no una empresa privada, aunque la familia Castro ha tenido mucho peso en él.

Según la economista Emily Morris, GAESA se creó en los años noventa, durante el Período Especial, para que militares formados en gestión dirigieran empresas estatales. Es decir, formalmente pertenece al Estado a través de las fuerzas armadas.

El vínculo familiar existe. Según una investigación del Miami Herald, hasta su muerte en 2022 la dirigió el general Luis Alberto Rodríguez López-Calleja, exyerno de Raúl Castro. Pero desde entonces la dirige la general de brigada Ania Guillermina Lastres Morera, sin vínculos familiares conocidos con los Castro, y la supervisa el Departamento V de las fuerzas armadas.

El problema de fondo es la falta de control. Según el Herald, el economista Pavel Vidal la describió como «un gobierno paralelo que no rinde cuentas», y la contralora general que dijo que no podía auditarla fue destituida.

Sobre si alguien se enriquece personalmente con ese dinero: según Emily Morris, los documentos filtrados muestran activos de GAESA pero no prueban corrupción, aunque ella admite que la falta de transparencia es un riesgo real.

Así que lo más exacto sería decir que GAESA es un conglomerado militar que estuvo dirigido por un familiar de Raúl Castro y que no rinde cuentas a los controles civiles; que sea un negocio privado de la familia no lo demuestran las fuentes que tenemos.""")],
 ["FR-PR023", "FR-PR018", "FR-PR017", "FR-PR022"]),

(T, "humano", [("Me da mucha rabia pensar que la cúpula en Cuba vive bien mientras la gente pasa hambre y sin corriente. ¿Hay pruebas de eso o es lo que se dice?", """Entiendo la rabia: la diferencia entre lo que vive la gente y lo que se sabe del poder es muy fuerte. Te cuento lo que hay documentado y lo que se discute.

Lo que dice una investigación: según el Miami Herald, basado en 22 estados financieros internos filtrados, el conglomerado militar GAESA declaró 7.200 millones de dólares de beneficio neto en los primeros ocho meses de 2023. El economista Pavel Vidal lo describió como «un gobierno paralelo que no rinde cuentas», y la contralora que dijo que no podía auditarlo fue destituida.

Lo que dice el gobierno: según el mismo Herald, Díaz-Canel afirmó que los problemas de Cuba «no se deben a mala gestión del gobierno» sino a que «no hemos tenido el dinero» durante años para mantener las termoeléctricas.

Lo que se discute: la economista Emily Morris sostiene que no está claro que GAESA tenga los 18.000 millones que calcula el Herald, que podrían ser unos 746 millones de dólares, y que los documentos no prueban que se le quite dinero al Estado ni que haya corrupción. Aun así, admite que la falta de transparencia es un riesgo real.

Así que hay pruebas de que existe un conglomerado militar con mucho dinero y sin control civil, mientras el gobierno dice no tener fondos para la electricidad. Lo que no está probado es cuánto dinero hay exactamente ni que se use para el enriquecimiento personal de los dirigentes. Lo importante es separar lo que está probado de lo que no.""")],
 ["FR-PR016", "FR-PR017", "FR-PR020", "FR-PR021", "FR-PR022"]),
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
