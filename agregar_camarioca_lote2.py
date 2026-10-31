"""
agregar_camarioca_lote2.py — Añade fragmentos nuevos a fuentes/fragmentos_camarioca_vuelos.jsonl, sacados de
documentos que ya están registrados (F030, F034, F035, F037, F038, F039). No registra fuentes nuevas.

Uso (desde E:\\vertex-exilio):
    python agregar_camarioca_lote2.py

Documentos releídos (en fuentes/docs):
  - b-164031(3)-095487.pdf (F030): informe del Contralor General de EE. UU. de 1971 sobre el gasto en refugiados
    cubanos. Es un escaneo con OCR: solo se toman cifras que se leen limpias (algunas tablas salen dañadas y se
    dejaron fuera). Páginas = las impresas del informe.
  - WIKI_freedom_flights.html (F037): secciones que no se habían usado. Se deja fuera el lenguaje valorativo
    ('oppressive government', 'climate of fear', 'in pursuit of freedom').
  - CASTRO_discurso_3oct1965.html (F039): más partes del discurso, solo como postura.
  - CAMARIOCA-cubaNet.md (F038) y CAMARIOCA1965.pdf (F034, Guardia Costera).

Qué hace:
  1. Copia de seguridad del archivo de fragmentos.
  2. Añade los fragmentos nuevos (FR-V027 en adelante) en 'pendiente'. Si alguno de esos IDs ya existe, no toca nada.
"""
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

FRAG = Path("fuentes/fragmentos_camarioca_vuelos.jsonl")
C, T, S = "camarioca_vuelos_libertad", "transversal", "salida_1959_1962"

NUEVOS = [
    # ---------------- informe del Contralor General (GAO), 1971
    dict(id="FR-V027", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 4",
         texto="Según el informe del Contralor General de 1971, hasta octubre de 1962 muchos refugiados llegaban a Miami "
               "en vuelos comerciales entre Cuba y Estados Unidos; con la Crisis de Octubre, Castro prohibió todos los "
               "vuelos comerciales a Estados Unidos, y durante unos tres años, hasta septiembre de 1965, pocos cubanos "
               "pudieron llegar."),
    dict(id="FR-V028", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="pp. 3-4",
         texto="Según el informe del Contralor General de 1971, de los unos 600.000 refugiados cubanos llegados a Estados "
               "Unidos desde 1959, unos 429.000 se habían registrado en el Centro de Emergencia para Refugiados Cubanos de "
               "Miami."),
    dict(id="FR-V029", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="pp. 5, 38",
         texto="Según el informe del Contralor General de 1971, el puente aéreo salía de Varadero, a unas 75 millas al este "
               "de La Habana, y recorría unas 195 millas hasta Miami; hasta el 31 de julio de 1971 había traído a unos "
               "243.000 refugiados, a un ritmo de unos 850 por semana."),
    dict(id="FR-V030", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 6",
         texto="Según el informe del Contralor General de 1971, reasentar a los refugiados fuera de Miami fue siempre un "
               "objetivo principal del programa; lo hacían por contrato cuatro agencias voluntarias (la Conferencia "
               "Católica de Estados Unidos, el Church World Service, la United HIAS Service y el International Rescue "
               "Committee), con ayuda de iglesias, sinagogas y organizaciones cívicas de todos los estados, y la "
               "Universidad de Miami daba cursos de actualización a médicos refugiados."),
    dict(id="FR-V031", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 36",
         texto="Según el informe del Contralor General de 1971, desde que empezó el puente aéreo unos tres de cada cuatro "
               "refugiados fueron reasentados fuera de Miami a los pocos días de llegar, sin las clases de inglés ni la "
               "formación profesional que habían recibido los anteriores; los funcionarios lo hacían para reducir el "
               "impacto en Miami, aunque reconocían que eso aumentaba el número de reasentados que necesitaban ayuda pública."),
    dict(id="FR-V032", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="pp. 32-34",
         texto="Según el informe del Contralor General de 1971, de los unos 243.000 refugiados llegados por el puente aéreo "
               "hasta julio de 1971, alrededor del 11 por ciento tenía más de 60 años al llegar y otro 10 por ciento, entre "
               "50 y 60."),
    dict(id="FR-V033", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 35",
         texto="Según un estudio del Departamento de Salud, Educación y Bienestar de 1968 citado por el Contralor General, "
               "entre los refugiados cubanos que recibían ayuda pública en cinco estados el 40 por ciento no había recibido "
               "ninguna educación, frente al 2 por ciento en 1965; entre ellos tenía empleo el 44 por ciento de los que "
               "hablaban inglés y solo el 24 por ciento de los que no lo hablaban."),
    dict(id="FR-V034", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 37 (tabla)",
         texto="Según los registros del programa recogidos por el Contralor General, de los refugiados llegados por el "
               "puente aéreo entre diciembre de 1965 y julio de 1971, el 6,0 por ciento tenía ocupaciones profesionales, "
               "semiprofesionales o directivas (7,1 por ciento en los primeros 20 meses y 4,1 por ciento en el año hasta "
               "julio de 1971), el 11,3 por ciento era personal de oficina y ventas, y el 64,4 por ciento eran "
               "estudiantes, niños y amas de casa."),
    dict(id="FR-V035", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="Resumen; pp. 38-41",
         texto="Según el informe del Contralor General de 1971, cada vuelo de ida y vuelta del puente aéreo costaba 752 "
               "dólares el 1 de diciembre de 1965, 966 en el año fiscal 1970, 1.530 en el de 1971 y 1.675 en el de 1972; "
               "los contratistas solo podían usar aviones de hélice, y no se había resuelto si el gobierno cubano "
               "permitiría usar reactores."),
    dict(id="FR-V036", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="pp. 8, 38",
         texto="Según el informe del Contralor General de 1971, la interrupción del puente aéreo anunciada en agosto de 1971 "
               "era, según las autoridades cubanas, para terminar de tramitar las últimas listas de personas autorizadas a "
               "salir; los funcionarios del programa calculaban que podían quedar entre 1.000 y 94.000."),
    dict(id="FR-V037", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="Resumen",
         texto="Según el informe del Contralor General de 1971, los pagos federales a las escuelas públicas del condado de "
               "Dade por los niños refugiados pasaron de 7 millones de dólares en el curso 1965-66 a unos 15,5 millones "
               "estimados para el curso 1971-72, y el número de alumnos cubiertos, de 16.673 a 22.100."),
    dict(id="FR-V038", etapa=C, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 33",
         texto="Según el informe del Contralor General de 1971, los refugiados cubanos registrados en el programa pasaron de "
               "unos 251.000 el 1 de julio de 1967 a unos 475.000 estimados para el 30 de junio de 1972, y la proporción "
               "que recibía ayuda pública, del 14 por ciento a un 21 por ciento estimado."),
    dict(id="FR-V039", etapa=C, tipo="cifra_disputada", id_fuente="F037", ubicacion="introducción", corroborado_por=["F030"],
         texto="El costo de los Vuelos de la Libertad varía según la fuente: Wikipedia da un presupuesto de unos 12 millones "
               "de dólares para todo el programa, y el informe del Contralor General de 1971 recoge unos 4,9 millones para "
               "el traslado de refugiados desde Cuba entre los años fiscales 1966 y 1972, con estimaciones para los dos "
               "últimos años."),
    dict(id="FR-V040", etapa=S, tipo="hecho_atribuido", id_fuente="F030", ubicacion="p. 3",
         texto="Según el informe del Contralor General de 1971, el programa de refugiados se pagó con fondos de "
               "contingencia del presidente hasta junio de 1962, cuando la Ley de Asistencia a la Migración y a los "
               "Refugiados le dio autoridad permanente: ayuda económica a refugiados necesitados, ayuda a agencias estatales "
               "y locales, pago del reasentamiento fuera de Miami y cursos de empleo y actualización profesional."),
    # ---------------- Wikipedia, Freedom Flights
    dict(id="FR-V041", etapa=C, tipo="cifra_disputada", id_fuente="F035", ubicacion="p. 732", corroborado_por=["F037"],
         texto="El número de inscritos para salir varía según la fuente: un documento interno del Departamento de Estado de "
               "1968 habla de varios cientos de miles; Wikipedia dice que en marzo de 1968 había más de un millón de personas "
               "en la lista de espera, y que una encuesta del Chicago Tribune de abril de 1966 encontró que casi dos "
               "millones de cubanos querían irse."),
    dict(id="FR-V042", etapa=C, tipo="cifra_disputada", id_fuente="F035", ubicacion="p. 732", corroborado_por=["F037"],
         texto="La fecha en que Cuba dejó de aceptar solicitudes para el puente aéreo varía según la fuente: el documento "
               "del Departamento de Estado de 1968 dice que el gobierno cubano dejó de aceptar nuevas inscripciones en mayo "
               "de 1966, y Wikipedia dice que Castro dejó de aceptar solicitudes de visado de salida en mayo de 1969."),
    dict(id="FR-V043", etapa=C, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'Social effects'",
         texto="Según Wikipedia, el gobierno cubano suspendió los vuelos de mayo a diciembre de 1972, y el último vuelo "
               "aterrizó en el Aeropuerto Internacional de Miami el 6 de abril de 1973."),
    dict(id="FR-V044", etapa=C, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'Social effects'",
         texto="Según Wikipedia, Orlando Torres se inscribió en 1965, al empezar el programa, y tuvo que esperar dos años "
               "para salir; hacia septiembre de 1970, con esperas cada vez más largas, algunos cubanos intentaban irse "
               "cruzando el estrecho de la Florida."),
    dict(id="FR-V045", etapa=C, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'Emigrant motivations'",
         texto="Según Wikipedia, durante la nacionalización de los pequeños negocios en la Ofensiva Revolucionaria, algunos "
               "pequeños comerciantes decidieron irse de Cuba en el puente aéreo."),
    dict(id="FR-V046", etapa=C, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'Processing'",
         texto="Según Wikipedia, los recién llegados en los Vuelos de la Libertad eran procesados en la Torre de la "
               "Libertad, a la que se llamó 'la Ellis Island del Sur', y vivían temporalmente en unas casas instaladas en el "
               "Aeropuerto Internacional de Miami."),
    dict(id="FR-V047", etapa=T, tipo="testimonio", id_fuente="F037", ubicacion="sección 'American backlash'",
         testigo="Luis Botifoll",
         texto="Según contó Luis Botifoll, citado por Wikipedia, algunos les tenían resentimiento porque hablaban español, "
               "hablaban alto y les quitaban trabajos, y recuerda carteles que decían 'No Pets, No Children, and No Cubans' "
               "(no se admiten mascotas, niños ni cubanos)."),
    dict(id="FR-V048", etapa=T, tipo="hecho_atribuido", id_fuente="F037", ubicacion="secciones 'American backlash' y 'Cuban-American culture and politics'",
         texto="Según Wikipedia, el inglés fue el único idioma oficial del condado de Dade hasta 1973, de modo que todos los "
               "documentos oficiales estaban solo en inglés, y en 1973 el condado pasó a ser oficialmente bilingüe."),
    dict(id="FR-V049", etapa=T, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'American backlash'",
         texto="Según Wikipedia, muchos estadounidenses blancos y judíos del condado de Dade se mudaron al norte, a Broward y "
               "Palm Beach, tras la llegada de los cubanos; Hialeah, casi totalmente anglosajona en 1960, sería décadas "
               "después hispana en un 96 por ciento, y Fort Lauderdale tenía un 4 por ciento de población hispana en 1980."),
    dict(id="FR-V050", etapa=T, tipo="testimonio", id_fuente="F037", ubicacion="sección 'Cuban-American culture and politics'",
         testigo="Luis Botifoll",
         texto="Según recuerda Luis Botifoll, citado por Wikipedia, al principio todos pensaban solo en volver a Cuba: nadie "
               "quería comprometerse con un trabajo y vivían al día."),
    dict(id="FR-V051", etapa=C, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'Cuban Adjustment Act'",
         texto="Según Wikipedia, que resume un artículo de la Harvard Law Review de 2001, el trato preferente a los cubanos "
               "en la Ley de Ajuste de 1966 respondió a cuatro razones: la política de la Guerra Fría, reducir trámites, "
               "motivos humanitarios y el aporte económico de los profesionales cubanos; antes, un refugiado cubano tenía que "
               "salir de Estados Unidos, pedir un visado en un consulado en el extranjero y volver a entrar."),
    dict(id="FR-V052", etapa=C, tipo="hecho_atribuido", id_fuente="F037", ubicacion="sección 'Cuban-American culture and politics'",
         texto="Según Wikipedia, Pepín Bosch, jefe de Bacardí a mediados de los años sesenta, ayudó a organizar propaganda y "
               "operaciones paramilitares contra Castro, y a finales de esa década pequeños grupos armados iniciaron acciones "
               "de guerrilla en Cuba."),
    dict(id="FR-V053", etapa=C, tipo="postura", id_fuente="F037", ubicacion="sección 'Formation of Little Havana'", actor="Juan Clark",
         texto="Según el sociólogo Juan Clark, citado por Wikipedia, los cubanos de los Vuelos de la Libertad convirtieron a "
               "Miami en el epicentro de todo el exilio cubano."),
    # ---------------- discurso de Castro del 3 de octubre de 1965 (solo postura)
    dict(id="FR-V054", etapa=C, tipo="postura", id_fuente="F039", ubicacion="discurso del 3 de octubre de 1965",
         actor="gobierno_cubano",
         texto="Según su discurso del 3 de octubre de 1965, Castro rechazó que hiciera falta la Cruz Roja, como había "
               "mencionado Johnson, y afirmó que bastaba con acordar los trámites con los representantes de la Embajada de "
               "Suiza, que representaban los intereses de Estados Unidos en Cuba."),
    dict(id="FR-V055", etapa=C, tipo="postura", id_fuente="F039", ubicacion="discurso del 3 de octubre de 1965",
         actor="gobierno_cubano",
         texto="Según ese mismo discurso, Castro afirmó que Cuba nunca había negado el permiso a quienes querían salir a "
               "visitar a sus familiares y volver, y preguntó a Johnson si Estados Unidos permitiría a los cubanos que vivían "
               "allí visitar a sus familias en Cuba y regresar, y a los ciudadanos estadounidenses visitar Cuba."),
    dict(id="FR-V056", etapa=C, tipo="postura", id_fuente="F039", ubicacion="discurso del 3 de octubre de 1965",
         actor="gobierno_cubano",
         texto="Según ese mismo discurso, Castro dijo que algún día gran parte de los que se habían ido querrían volver, "
               "arrepentidos, y que la idea de que regresaran como libertadores era un sueño."),
    dict(id="FR-V057", etapa=C, tipo="postura", id_fuente="F039", ubicacion="discurso del 3 de octubre de 1965",
         actor="gobierno_cubano",
         texto="Según ese mismo discurso, Castro presentó su propuesta del 28 de septiembre como una respuesta a la "
               "situación de personas que, al suspenderse los vuelos entre Cuba y Miami, habían quedado con un pie en Cuba y "
               "otro en Estados Unidos, y comparó la salida de cubanos con la emigración de puertorriqueños a Estados Unidos."),
    # ---------------- CubaNet y Guardia Costera
    dict(id="FR-V058", etapa=C, tipo="postura", id_fuente="F038", ubicacion="texto", actor="CubaNet",
         texto="Según CubaNet, Camarioca fue la primera vez que Fidel Castro usó la migración masiva como método de presión "
               "sobre Estados Unidos, y repitió la estrategia en 1980 con el Mariel y en 1994 con la crisis de los balseros."),
    dict(id="FR-V059", etapa=C, tipo="hecho_atribuido", id_fuente="F038", ubicacion="texto",
         texto="Según CubaNet, el primer grupo de refugiados de Camarioca llegó a Cayo Marathón el 7 de octubre de 1965, y "
               "el corredor marítimo estuvo abierto 42 días."),
    dict(id="FR-V060", etapa=C, tipo="hecho_atribuido", id_fuente="F034", ubicacion="pies de foto",
         texto="Según la Guardia Costera de Estados Unidos, a finales de agosto de 1965 el guardacostas Ariadne evacuó a 39 "
               "cubanos desde Cayo Sal, en las Bahamas, y en octubre de 1965 rescató a otros 36."),
    dict(id="FR-V061", etapa=C, tipo="hecho_atribuido", id_fuente="F034", ubicacion="pies de foto",
         texto="Según la Guardia Costera de Estados Unidos, que cita un boletín de reasentamiento de febrero de 1967, Lauriano "
               "Ricoy y su esposa salieron de Cuba en un kayak metálico de 8 pies impulsado por un motor de cortadora de "
               "césped, pasaron cinco días en el estrecho de la Florida y los recogió un guardacostas a unas 34 millas al "
               "este de Marathon; después se reasentaron en Nueva Orleans."),
]

if not FRAG.exists():
    print(f"No encuentro {FRAG}. ¿Estás en E:\\vertex-exilio? No toco nada.")
    sys.exit(1)

with FRAG.open(encoding="utf-8-sig") as f:
    lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n["id"] for n in NUEVOS if n["id"] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(FRAG, FRAG.with_name(f"{FRAG.name}.{marca}.bak"))
with FRAG.open("a", encoding="utf-8", newline="\n") as f:
    if lineas and not lineas[-1].endswith("\n"):
        f.write("\n")
    for n in NUEVOS:
        d = {"id": n["id"], "etapa": n["etapa"], "tipo": n["tipo"], "id_fuente": n["id_fuente"],
             "ubicacion": n["ubicacion"], "corroborado_por": n.get("corroborado_por", []), "texto": n["texto"],
             "notas": "", "revisado": False, "estado": "pendiente"}
        if n.get("actor"):
            d["actor"] = n["actor"]
        if n.get("testigo"):
            d["testigo"] = n["testigo"]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Añadidos {len(NUEVOS)} fragmentos nuevos a {FRAG} (en 'pendiente').")
print(f"Ahora: python revisar.py {FRAG}")
