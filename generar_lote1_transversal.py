"""
generar_lote1_transversal.py — Primer lote de ejemplos transversales (identidad, cultura, generaciones,
remesas y relación del gobierno cubano con los emigrados), 15 ejemplos.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_transversal.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_transversal.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_transversal_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

El lote enseña a distinguir generaciones (antes de 1959, exilio de los sesenta, llegadas recientes,
nacidos en Estados Unidos), a hablar de cultura e identidad sin estereotipos y a tratar la política de
los cubanoamericanos solo con datos atribuidos, sin opinar.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_transversal.jsonl")
DESTINO = Path("datos/borrador_transversal_lote1.jsonl")
PREFIJO = "exi-t"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
T = "transversal"
E = [
(T, "hecho", [("¿Desde cuándo hay cubanos en Estados Unidos?", """Desde mucho antes de 1959. La presencia cubana en lo que hoy es Estados Unidos viene de la época colonial.

Según Wikipedia, la Florida española dependía de la Capitanía General de Cuba, y en 1565 cientos de soldados españoles y sus familias salieron de Cuba para fundar San Agustín.

En el siglo XIX la emigración creció. Según la misma fuente, en 1870 había casi 12.000 inmigrantes cubanos en Estados Unidos, unos 4.500 en Nueva York, 3.000 en Nueva Orleans y 2.000 en Cayo Hueso, y esa emigración tenía causas económicas y políticas. Muchos eran tabaqueros: se instalaron en Cayo Hueso, y en 1885 Vicente Martínez Ybor trasladó su fábrica de tabacos a Tampa, donde fundó Ybor City; Tampa pasó de unos 1.000 habitantes en 1885 a más de 16.000 en 1900.

La emigración siguió en el siglo XX. Según Wikipedia, entre 1900 y 1959 llegaron unos 100.000 cubanos, sobre todo por razones económicas, aunque también había opositores a Batista. En 1958 había registrados unos 125.000 cubanos y descendientes, y más de 50.000 se quedaron después de 1959.

Es decir, cuando empezó el gran exilio de los años sesenta, ya existía una comunidad cubana en Estados Unidos.""")],
 ["FR-T001", "FR-T002", "FR-T003", "FR-T005"]),

(T, "contexto", [("¿Qué papel tuvieron los cubanos de Tampa en la independencia de Cuba?", """Uno importante. Las comunidades de tabaqueros de la Florida fueron un apoyo clave para la causa independentista.

Según Wikipedia, en el siglo XIX muchos tabaqueros cubanos se instalaron en Cayo Hueso, y en 1885 Vicente Martínez Ybor trasladó su fábrica de tabacos a Tampa, donde fundó Ybor City. Tampa pasó de unos 1.000 habitantes en 1885 a más de 16.000 en 1900.

Esas comunidades se involucraron en la lucha. Según Wikipedia, los cubanos de Ybor City y West Tampa apoyaron con dinero, equipos y a veces con su vida la independencia de Cuba, inspirados por José Martí, que visitó la Florida varias veces.

De esa época también quedó algo muy cotidiano. Según la misma fuente, el sándwich cubano se creó y se estandarizó entre los tabaqueros que iban y venían entre Cuba y la Florida, sobre todo en Ybor City, alrededor del cambio del siglo XIX al XX.

Es decir, antes del exilio de los años sesenta, la Florida ya había sido un lugar de emigración y de organización política para los cubanos.""")],
 ["FR-T003", "FR-T004", "FR-T006"]),

(T, "hecho", [("¿Cuántos cubanos y cubanoamericanos hay en Estados Unidos?", """Depende de la fuente y del año, pero la cifra ronda los tres millones.

Los cubanos son el tercer grupo hispano más grande de Estados Unidos, después de los mexicanos y los puertorriqueños. Según Pew Research, en 2024 había 2,9 millones de personas de origen cubano, un 23 % más que en 2019. Wikipedia da una cifra algo mayor, 3.082.802, para 2025. No es exactamente una contradicción: son años distintos, y la comunidad creció mucho con la ola migratoria reciente.

No todos nacieron en Cuba. Según Pew Research, en 2024 el 57 % de las personas de origen cubano en Estados Unidos (1,7 millones) había nacido fuera del país; el resto nació en Estados Unidos.

La mayoría sigue en la Florida. Según Pew, el 61 % (1,8 millones) vive en ese estado y el 8 % en Texas; el área de Miami concentra el 42 % (1,2 millones), y le siguen Tampa (177.000), Nueva York (153.000) y Houston (107.000).""")],
 ["FR-T020", "FR-T026", "FR-T021", "FR-T023"]),

(T, "contexto", [("¿Cómo nació la Pequeña Habana de Miami?", """Nació en los años sesenta, con la llegada del exilio, en un barrio que antes tenía otra cara.

Según Wikipedia, la Pequeña Habana surgió en un barrio de Miami que en los años treinta había sido de clase media baja y con mucha población judía. Los cubanos que llegaban pensaban que su estancia sería temporal, y para 1970 el barrio era cubano en más de un 85 %.

Con el tiempo cambió. Según la misma fuente, cuando quedó claro que no volverían pronto, los cubanos se asentaron en otros barrios de Miami, y la proporción de cubanos entre los hispanos de la Pequeña Habana bajó del 84 % en 1979 al 58 % en 1989, con la llegada de nicaragüenses, hondureños y otros centroamericanos, aunque la mayoría de los negocios seguía en manos cubanas.

Hoy es sobre todo un símbolo. Según Wikipedia, es conocida por la Calle Ocho, el Parque del Dominó (Parque Máximo Gómez), el Festival de la Calle Ocho, los Viernes Culturales y un paseo de la fama con artistas como Celia Cruz, Gloria Estefan y Willy Chirino; en 2017 el National Trust for Historic Preservation la declaró tesoro nacional.""")],
 ["FR-T011", "FR-T012", "FR-T014"]),

(T, "contexto", [("¿Qué diferencia hay entre los cubanos que llegaron en los sesenta y los que llegaron después?", """Llegaron en momentos muy distintos y por razones que no siempre fueron las mismas, así que conviene no meterlos a todos en el mismo saco.

La primera gran ola fue enorme. Según Wikipedia, entre 1960 y 1980 emigró alrededor de un millón de cubanos, cerca del 10 % de la población de la isla, y el 85 % fue a Estados Unidos. Según Pew Research, unos 250.000 llegaron en los años sesenta, tras la Revolución, y otros 250.000 en los setenta; en los ochenta llegaron, entre otros, los 125.000 del Mariel.

Con los años cambiaron también los motivos que se mencionan. Según Wikipedia, en 2008 Jorge Ferragut, fundador de Casa Cuba, una agencia que ayudaba a inmigrantes cubanos en Texas, dijo que muchos cubanos que llegaron en la primera década del siglo XXI se habían ido por razones económicas más que políticas.

Y hay una tercera categoría: los que nacieron en Estados Unidos. Según Pew, en 2024 el 57 % de las personas de origen cubano había nacido fuera del país. Los nacidos en Cuba tienen menos probabilidades que el conjunto de los estadounidenses de tener un título universitario, mientras que los nacidos en Estados Unidos tienen más.

Cada grupo tiene su propia experiencia, y eso puede ayudar a entender algunas diferencias dentro de la comunidad.""")],
 ["FR-T007", "FR-T008", "FR-T015", "FR-T021", "FR-T025"]),

(T, "hecho", [("¿Qué ayudas recibieron los primeros exiliados cubanos en Estados Unidos?", """Recibieron bastante apoyo, tanto del gobierno como de algunos bancos.

Según Wikipedia, el Programa de Refugiados Cubanos dio más de 1.300 millones de dólares en ayuda directa, y los recién llegados también podían recibir asistencia pública, clases de inglés gratis, becas y préstamos universitarios con intereses bajos.

El apoyo también vino del sector privado. Según la misma fuente, algunos bancos dieron préstamos a exiliados que no tenían garantías ni historial de crédito, lo que permitió abrir negocios. Miami y Union City, en Nueva Jersey, apodada "La Habana del Hudson", se convirtieron en los principales centros de la cultura cubanoamericana.

Hay que ponerlo en contexto: fue una ola muy grande. Según Wikipedia, entre 1960 y 1980 emigró alrededor de un millón de cubanos, cerca del 10 % de la población de la isla, y el 85 % fue a Estados Unidos. Las fuentes que tenemos describen las ayudas, pero no permiten medir cuánto pesaron frente al esfuerzo de los propios exiliados.""")],
 ["FR-T009", "FR-T010", "FR-T007"]),

(T, "contexto", [("¿Los cubanoamericanos siguen hablando español?", """Sí, en su mayoría, aunque cada vez más son bilingües.

Según Wikipedia, el 89 % de los cubanoamericanos mayores de 18 años habla en casa un idioma distinto del inglés, cerca del 60 % domina el inglés y el 36 % se considera bilingüe. La misma fuente relaciona el uso del español en casa con el deseo de conservar la herencia cultural.

Eso tiene que ver con quiénes forman la comunidad. Según Pew Research, en 2024 el 57 % de las personas de origen cubano en Estados Unidos había nacido fuera del país, así que una gran parte aprendió primero el español.

El interés por las raíces también se ve en otras cosas. Según Wikipedia, en los últimos años creció mucho el interés de los cubanoamericanos por la genealogía, como forma de conservar sus raíces cubanas mientras adoptan la cultura estadounidense.

Es decir, el español sigue siendo una parte importante de la identidad, aunque la forma de vivirlo cambia de una generación a otra.""")],
 ["FR-T016", "FR-T021", "FR-T019"]),

(T, "contexto", [("¿Qué tradiciones culturales mantienen los cubanos en Estados Unidos?", """Muchas, y algunas se notan en la vida diaria de ciudades como Miami.

Una de las más visibles es el café. Según Wikipedia, el café cubano es central en la comunidad: el cafecito o colada, el cortadito (mitad leche, mitad café) y el café con leche. Refrescos de origen cubano como Materva o Jupiña se siguen produciendo en Miami.

La comida también tiene historia propia. Según Wikipedia, el sándwich cubano se creó y se estandarizó entre los tabaqueros que iban y venían entre Cuba y la Florida, sobre todo en Ybor City, alrededor del cambio del siglo XIX al XX.

En la religión hay diversidad. Según la misma fuente, cerca del 49 % de los cubanoamericanos es católico, un 16 % protestante y un 26 % no tiene religión, y algunos practican religiones sincréticas de origen africano como la santería o Ifá.

Y hay lugares que funcionan como centro de esa cultura. Según Wikipedia, la Pequeña Habana es conocida por la Calle Ocho, el Parque del Dominó, el Festival de la Calle Ocho y los Viernes Culturales.""")],
 ["FR-T018", "FR-T006", "FR-T017", "FR-T014"]),

(T, "perspectivas", [("¿Por qué muchos cubanoamericanos votan republicano?", """Es una tendencia conocida, pero no es uniforme, y las cifras muestran diferencias por generación. Aquí van los datos, sin valoraciones.

Según Pew Research, históricamente los cubanoamericanos se han identificado como republicanos más que el conjunto de los hispanos, aunque ese apoyo se ha suavizado en algunos momentos. Según Wikipedia, una explicación que se suele dar es que el fracaso de Bahía de Cochinos en 1961 hizo que buena parte del exilio desconfiara del Partido Demócrata y se acercara al Partido Republicano en la Florida. En Nueva Jersey, en cambio, los congresistas cubanoamericanos han sido sobre todo demócratas, como Albio Sires y Bob Menéndez.

Las generaciones votan distinto. Según Wikipedia, en 2008 Barack Obama obtuvo el 47 % del voto cubanoamericano en la Florida, y según encuestas de Bendixen el 84 % de los votantes cubanoamericanos de Miami-Dade de 65 años o más apoyó a John McCain, mientras que el 55 % de los menores de 30 apoyó a Obama.

En años recientes, según la encuesta Cuba Poll de FIU de 2024 citada por Wikipedia, el 68 % de los probables votantes cubanoamericanos de Miami-Dade apoyaba a Donald Trump y el 55 % estaba a favor de mantener el embargo, mientras que los más jóvenes y nacidos en Estados Unidos estaban más divididos. Según una encuesta de Pew de octubre de 2025, el 40 % aprobaba la política migratoria de Trump, frente al 21 % del conjunto de hispanos.

Algunas cifras históricas tampoco coinciden: para el voto a George W. Bush en 2000, un artículo de Wikipedia da el 75 % y otro, el 80 %.""")],
 ["FR-T027", "FR-T029", "FR-T030", "FR-T031", "FR-T028", "FR-T032"]),

(T, "perspectivas", [("¿Qué pasó con las remesas a Cuba en 2025?", """Western Union dejó de enviarlas, y cada gobierno lo explicó a su manera.

Según OnCuba, en febrero de 2025 Western Union suspendió indefinidamente el envío de remesas a Cuba por un cambio en las regulaciones de sanciones de Estados Unidos, después de que la empresa Orbit, que procesaba las remesas en la isla, fuera incluida en la lista de entidades restringidas. No era la primera vez: según OnCuba, con información de EFE, el servicio se había reanudado en mayo de 2024, después de suspenderlo en 2020, cuando Estados Unidos restringió a Fincimex por pertenecer al conglomerado GAESA, controlado por las Fuerzas Armadas cubanas.

La posición de Estados Unidos: según OnCuba, el secretario de Estado Marco Rubio afirmó que Orbit actúa para las fuerzas militares cubanas o en su nombre; la declaración oficial cubana no lo confirmó ni lo negó.

La posición del gobierno cubano: según OnCuba, la cancillería lamentó la suspensión, dijo que afectaría a "incontables familias", la atribuyó a lo que llamó una política de línea dura irracional del gobierno de Estados Unidos y aseguró que la decisión "se veía venir".

Para muchas familias el efecto es directo. Según OnCuba, las remesas son un aporte fundamental para una parte de la población cubana, aunque desde hace años una gran parte de ese dinero se mueve por canales informales.""")],
 ["FR-T033", "FR-T034", "FR-T035", "FR-T036", "FR-T037"]),

(T, "perspectivas", [("¿Cómo se relaciona el gobierno cubano con los cubanos que viven fuera?", """Es una relación que ha cambiado con los años y que todavía tiene puntos de fricción con los emigrados.

El gobierno cubano organiza encuentros con la emigración. Según OnCuba, en diciembre de 2019 el presidente Miguel Díaz-Canel convocó la IV Conferencia "La Nación y la Emigración" para abril de 2020 en La Habana, en continuidad con los primeros diálogos entre el gobierno y emigrados de 1978. Según la convocatoria oficial, la conferencia tendría un significado especial para los jóvenes nacidos fuera de Cuba que se identifican con el país de sus padres y abuelos, y el gobierno presentó el acercamiento a los emigrados como algo natural e inevitable.

También tomó medidas. Según OnCuba, eliminó la "habilitación" del pasaporte para los emigrados que viajaban a la isla, permitió entrar a quienes habían salido ilegalmente, salvo los que salieron por la base de Guantánamo, y dejó de exigir aprobación para que los hijos de cubanos nacidos fuera obtuvieran la ciudadanía.

Pero quedan controversias. Según OnCuba, la emigración reclama más presencia en la economía, la inversión y la vida política, y critica el costo y los trámites del pasaporte y la pérdida de la residencia y la ciudadanía cubanas. Además, el gobierno se reunía sobre todo con emigrados que no tenían una posición abiertamente contraria a él.""")],
 ["FR-T039", "FR-T040", "FR-T041", "FR-T042"]),

(T, "humano", [("Nací en Miami, mis padres son cubanos y no hablo bien español. A veces siento que no soy cubano de verdad. ¿Es normal?", """Es muy normal, y no eres el único. Muchos hijos de cubanos nacidos fuera de la isla sienten eso en algún momento.

Para empezar, tu caso es muy común. Según Pew Research, en 2024 el 57 % de las personas de origen cubano en Estados Unidos había nacido fuera del país, lo que significa que el resto, una parte muy grande, nació aquí, como tú. Según Wikipedia, cerca del 60 % de los cubanoamericanos domina el inglés y el 36 % se considera bilingüe, así que hay muchas formas distintas de vivir los dos idiomas.

También es normal que la segunda generación viva la identidad de otra manera. Según Wikipedia, los cubanoamericanos de segunda generación se fueron mudando de barrios como la Pequeña Habana a zonas residenciales, y en los últimos años creció mucho su interés por la genealogía, como forma de conservar sus raíces cubanas mientras adoptan la cultura estadounidense.

La identidad no se mide solo por cómo hablas el idioma. Se construye también con la historia de tu familia, las costumbres que vives en casa y lo que tú decides conservar. Si quieres reforzar el español o conocer mejor la historia de tus padres, nunca es tarde para empezar.""")],
 ["FR-T021", "FR-T016", "FR-T013", "FR-T019"]),

(T, "contexto", [("¿Hay muchos cubanos indocumentados en Estados Unidos?", """Hoy sí, y es algo nuevo en la historia de la emigración cubana.

Según Pew Research, antes de 2017 casi no había inmigrantes cubanos indocumentados en Estados Unidos, pero en julio de 2023 se calculaban 475.000, y al menos 250.000 más entraron hasta finales de 2024.

Eso cambia la cara de la comunidad. Según Pew, en 2024 el 57 % de las personas de origen cubano en Estados Unidos (1,7 millones) había nacido fuera del país, y una parte de los que llegaron recientemente no tiene un estatus estable.

La preocupación se nota en las encuestas. Según una encuesta de Pew Research de octubre de 2025, el 47 % de los cubanoamericanos temía que ellos o alguien cercano fuera deportado, frente al 52 % del conjunto de hispanos. La misma encuesta muestra que el 40 % aprobaba la política migratoria del gobierno de Trump, frente al 21 % de los hispanos; es decir, dentro de la comunidad hay opiniones distintas sobre ese tema.""")],
 ["FR-T022", "FR-T021", "FR-T028"]),

(T, "contexto", [("¿Por qué la comunidad cubana en Estados Unidos es de más edad que otros grupos hispanos?", """Tiene que ver con la historia de su emigración.

Según Pew Research, los cubanos son el grupo hispano de mayor edad en Estados Unidos, con una edad mediana de 38,2 años frente a 30,2 del conjunto de hispanos, por la llegada de inmigrantes mayores y una fecundidad baja.

Parte de la explicación está en lo antigua que es la emigración. Según Pew, unos 250.000 cubanos llegaron en los años sesenta, tras la Revolución, y otros 250.000 en los setenta; en los ochenta llegaron, entre otros, los 125.000 del Mariel. Muchos de los que llegaron entonces son hoy personas mayores.

A la vez, la comunidad se renueva. Según Pew, en 2024 el 57 % de las personas de origen cubano había nacido fuera del país, y con la ola reciente llegaron muchos más. Por eso conviven en la misma comunidad personas que llegaron hace más de sesenta años, recién llegados y nacidos en Estados Unidos.""")],
 ["FR-T024", "FR-T008", "FR-T021"]),

(T, "hecho", [("¿Las remesas a Cuba bajaron con la pandemia?", """Sí, según las fuentes que tenemos, aunque no hay una cifra exacta en ellas.

Según Wikipedia, la pandemia de 2020-2022 provocó caídas bruscas de las remesas y del turismo en Cuba, y el PIB cubano cayó más de un 10 % entre 2018 y 2024.

Hubo además otros golpes. Según OnCuba, con información de EFE, Western Union había suspendido el servicio en 2020, cuando Estados Unidos restringió a Fincimex por pertenecer al conglomerado GAESA, controlado por las Fuerzas Armadas cubanas; lo reanudó en mayo de 2024 y volvió a suspenderlo en febrero de 2025, después de que la empresa Orbit fuera incluida en la lista de entidades restringidas.

Mientras tanto, el dinero buscó otros caminos. Según OnCuba, las remesas son un aporte fundamental para una parte de la población cubana en medio de la crisis económica y energética, aunque desde hace años una gran parte de ese dinero se mueve por canales informales.""")],
 ["FR-T038", "FR-T034", "FR-T033", "FR-T037"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "Transversal, lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
