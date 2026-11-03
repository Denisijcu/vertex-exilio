"""
agregar_cuba_venezuela.py — Etapa cuba_venezuela (módulo "Cuba: contexto").

Registra las fuentes F109-F114 y crea fuentes/fragmentos_cuba_venezuela.jsonl (FR-VZ001 en adelante):
Fidel y Chávez (1994), petróleo a cambio de profesionales (2000-2025), los acuerdos militares de 2008 y la DGCIM,
las negativas oficiales sobre militares cubanos, los 32 muertos de enero de 2026 y lo que pasó después.
También reutiliza fuentes ya registradas: F080, F081, F082, F083 y F084.

Uso (desde E:\\vertex-exilio):
    python agregar_cuba_venezuela.py

Criterios:
  - Lo que dicen los gobiernos de Cuba, Venezuela y EE. UU. va como postura (actor), aunque lo recoja una agencia.
  - La investigación de Reuters de 2019 se basa en documentos y fuentes anónimas: hecho atribuido a Reuters.
  - Las condiciones de los médicos en 2005 vienen del relato de una persona a Guillermoprieto: atribuido así.
  - No entran: el informe de 2007 publicado por la KAS (análisis partidista con cifras inconsistentes), La Patilla
    (sin autor ni fecha), "abduction" (Al Jazeera), "terroristas en uniforme imperial" (fuera de cita) ni
    "dictators" (Trump) fuera de cita.

Qué hace:
  1. Comprueba que validar.py tiene la etapa cuba_venezuela.
  2. Copia de seguridad del registro (y del archivo de fragmentos si ya existiera).
  3. Añade F109-F114 al registro (si alguna ya existe, no toca nada).
  4. Crea el archivo de fragmentos en estado 'pendiente'.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_cuba_venezuela.jsonl")
HOY = "2026-11-03"
T = "cuba_venezuela"

AG = "Según la periodista Alma Guillermoprieto (The New York Review of Books, octubre de 2005)"
R19 = "Según una investigación de Reuters (Angus Berwick, agosto de 2019) basada en documentos y en exfuncionarios"
ML = "Según el economista Carmelo Mesa-Lago (Universidad de Pittsburgh, 2009)"
CRS = "Según el Servicio de Investigación del Congreso de EE. UU. (mayo de 2020)"
R26A = "Según Reuters (11 de enero de 2026)"
R26B = "Según Reuters (21 de febrero de 2026), que cita a 11 fuentes"

FUENTES = [
    ("F109", "The Cuban Connection (The New York Review of Books, 20 de octubre de 2005)", "Alma Guillermoprieto",
     "https://www.nybooks.com/articles/2005/10/20/the-cuban-connection/", "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/NYRB_2005_guillermoprieto.html. Las condiciones de los médicos las cuenta una amiga cubana "
     "de la autora: van atribuidas así. Las valoraciones de la autora, como postura."),
    ("F110", "Venezuelan president recalls 30 years of Fidel and Chavez embrace (diciembre de 2024)", "Radio Rebelde",
     "https://www.radiorebelde.cu/english/?p=7075", "periodistica", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/RADIOREBELDE_abrazo_1994.html. Emisora estatal cubana que reproduce palabras de Maduro y "
     "de Fidel Castro: todo como postura."),
    ("F111", "Venezuelan oil supply to Cuba jumps in July, according to news agencies (8 de agosto de 2025)",
     "OnCuba Staff (con datos de Reuters)",
     "https://oncubanews.com/en/cuba/economy/venezuelan-oil-supply-to-cuba-jumps-in-july-according-to-news-agencies",
     "periodistica", "revisar", "ninguna", "hechos",
     "Archivo fuentes/docs/ONCUBA_2025_petroleo.html. Cifras de exportación de PDVSA según Reuters (seguimiento de "
     "buques y documentos internos)."),
    ("F112", "Cuba defiant after Trump says island to receive no more Venezuelan oil or money (11 de enero de 2026)",
     "Dave Sherwood y Marianna Parraga, Reuters (publicado por The Star)",
     "https://www.thestar.com.my/news/world/2026/01/11/trump-says-no-more-venezuelan-oil-or-money-to-go-to-cuba-pushes-for-deal",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/REUTERS_2026_trump_petroleo.html. Lo que dicen Trump, Díaz-Canel y Bruno Rodríguez: postura "
     "de cada gobierno. 'Communist-run' es descriptor de agencia: no entra."),
    ("F113", "Exclusive: Cuban security forces exit Venezuela as US pressure mounts (21 de febrero de 2026)",
     "Sarah Kinosian, Julia Symmes Cobb y Laura Gottesdiener, Reuters (publicado por The Star)",
     "https://www.thestar.com.my/news/world/2026/02/21/exclusive-cuban-security-forces-exit-venezuela-as-us-pressure-mounts",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/REUTERS_2026_salida_cubanos.html. Basado en 11 fuentes; ningún gobierno respondió a Reuters."),
    ("F114", "How Cuba taught Venezuela to quash military dissent (agosto de 2019)",
     "Angus Berwick, Reuters (publicado por The Peninsula, Qatar)",
     "https://thepeninsulaqatar.com/article/26/08/2019/How-Cuba-taught-Venezuela-to-quash-military-dissent",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/REUTERS_2019_dgcim.html. Investigación basada en documentos y fuentes anónimas. La cifra de "
     "'más de 21.000 millones de dólares' en petróleo se calcula con cifras oficiales y precios medios: va atribuida. "
     "'Authoritarian rule' es lenguaje de la nota: no entra."),
]

NUEVOS = [
    # ================= Fidel y Chávez
    dict(id="FR-VZ001", tipo="hecho_atribuido", id_fuente="F114", ubicacion="Párrafos 35-40",
         texto=f"{R19}, en 1994, meses después de salir de prisión por un indulto presidencial, Hugo Chávez viajó a La Habana, "
               "donde Fidel Castro lo recibió en el aeropuerto en su primer encuentro en persona; en un discurso en la "
               "Universidad de La Habana, Chávez llamó a Cuba «un bastión de la dignidad latinoamericana»."),
    dict(id="FR-VZ002", tipo="postura", id_fuente="F110", ubicacion="Párrafos 1-8", actor="gobiernos de Venezuela y de Cuba",
         texto="Según la emisora estatal cubana Radio Rebelde, Nicolás Maduro recordó en diciembre de 2024 que Chávez fue "
               "recibido por Fidel Castro «con honores de jefe de Estado» la noche del 13 de diciembre de 1994 y habló del "
               "inicio de una historia de «unidad, solidaridad y liberación»; Fidel Castro había dicho que aceptar aquella "
               "invitación fue para Chávez «un acto de valentía»."),
    dict(id="FR-VZ003", tipo="hecho_atribuido", id_fuente="F114", ubicacion="Párrafos 5-8 y 39-44",
         texto=f"{R19}, Castro fue mentor de Chávez antes de que llegara a la presidencia y vio en el petróleo venezolano un "
               "posible alimento para una economía cubana golpeada por el fin de la URSS; tras su elección en 1998, Chávez "
               "estrechó los vínculos con Cuba, y desde entonces Venezuela envió al menos 55.000 barriles diarios de "
               "petróleo, más de 21.000 millones de dólares según cifras oficiales y precios medios, mientras Cuba mandaba "
               "miles de médicos, maestros y especialistas agrícolas."),
    dict(id="FR-VZ004", tipo="hecho_atribuido", id_fuente="F109", ubicacion="Párrafos 2-3",
         texto=f"{AG}, Chávez le escribió a Fidel Castro que no sabía si llamarlo «hermano o padre»; los dos hablaban "
               "constantemente por teléfono, y en seis años hubo media docena de visitas de Estado."),
    # ================= petróleo por profesionales
    dict(id="FR-VZ005", tipo="hecho_atribuido", id_fuente="F109", ubicacion="Párrafo 4",
         texto=f"{AG}, desde octubre de 2000 Cuba recibe petróleo venezolano a precio de mercado pero con un crédito muy "
               "fácil, 90.000 barriles diarios en 2005, y desde 2001 Venezuela paga además en efectivo bienes y servicios "
               "cubanos, desde casas prefabricadas hasta entrenadores deportivos."),
    dict(id="FR-VZ006", tipo="hecho_atribuido", id_fuente="F083", ubicacion="Secciones 'Cuba's economy' y 'Venezuela'",
         texto=f"{CRS}, en 2000 Cuba y Venezuela firmaron un acuerdo petrolero preferencial, en esencia un trueque de petróleo "
               "por personal médico, que dio a Cuba entre 90.000 y 100.000 barriles diarios, cerca de dos tercios de su "
               "consumo; un estudio de Brookings de 2014 estimó que había unos 40.000 profesionales cubanos en Venezuela, el "
               "75 % de ellos en salud."),
    dict(id="FR-VZ007", tipo="hecho_atribuido", id_fuente="F109", ubicacion="Párrafos 5-6",
         texto=f"{AG}, en 2003, cuando Chávez estaba en serios problemas políticos, con la economía en caída y la oposición "
               "reuniendo firmas para un referendo revocatorio, Fidel Castro aceptó enviarle cerca de 30.000 "
               "internacionalistas, entre médicos, enfermeros, entrenadores deportivos, maestros y alfabetizadores; la "
               "Misión Barrio Adentro llevó atención médica a casi todos los barrios pobres del país."),
    dict(id="FR-VZ008", tipo="hecho_atribuido", id_fuente="F109", ubicacion="Párrafo 7",
         texto=f"{AG}, una cubana que vivía en Venezuela y tenía dos primos médicos le contó a la autora que los médicos "
               "dejaban a su familia en Cuba y no podían visitarla en los dos o tres años de contrato, y que recibían 200 "
               "dólares al mes del gobierno venezolano más 100 dólares depositados en una cuenta en Cuba, cuando en Cuba un "
               "médico ganaba unos 15 dólares al mes."),
    dict(id="FR-VZ009", tipo="hecho_atribuido", id_fuente="F109", ubicacion="Párrafos 6 y 9",
         texto=f"{AG}, en los barrios había consenso en que los médicos cubanos eran trabajadores y competentes, y eran «muy "
               "queridos», aunque evitaban a la prensa; en julio de 2005 el ministro de Defensa venezolano restó importancia "
               "en público a que una promoción de cadetes se llamara «Promoción Fidel Castro»."),
    dict(id="FR-VZ010", tipo="postura", id_fuente="F109", ubicacion="Párrafos 8-9", actor="Alma Guillermoprieto (periodista)",
         texto=f"{AG}, el petróleo venezolano ayuda a Fidel Castro a mantenerse en el poder un poco más, y los cubanos le "
               "ahorran a Chávez tener que trabajar con instituciones que no sean las que él mismo creó; la autora sostiene "
               "que Chávez paga el precio más alto ante su propio alto mando militar, al que la presencia cubana incomoda."),
    dict(id="FR-VZ011", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección V.3",
         texto=f"{ML}, la ayuda de Venezuela a Cuba en créditos, subsidios e inversión se estimó en 9.405 millones de dólares en "
               "2008, más que en cualquier año de la relación con la URSS: 5.650 millones por los servicios de 40.000 "
               "médicos, maestros y otros profesionales cubanos, 97.000 barriles diarios de crudo y derivados, el 65 % de la "
               "demanda cubana, con un subsidio de precios de 2.400 millones, e inversiones en 76 proyectos por 1.355 "
               "millones."),
    dict(id="FR-VZ012", tipo="postura", id_fuente="F084", ubicacion="Sección V.3", actor="Carmelo Mesa-Lago (economista)",
         texto=f"{ML}, la dependencia de Cuba respecto a Venezuela era muy fuerte, y si la ayuda venezolana terminaba o se "
               "reducía mucho, Cuba podría enfrentar un segundo «Período Especial»."),
    # ================= los acuerdos militares y la DGCIM
    dict(id="FR-VZ013", tipo="hecho_atribuido", id_fuente="F114", ubicacion="Párrafos 54-59",
         texto=f"{R19}, tras perder un referendo en diciembre de 2007 Chávez pidió consejo a Fidel Castro, y el 26 de mayo de "
               "2008 el ministro de Defensa venezolano, Gustavo Rangel, y el viceministro de Defensa cubano, general Álvaro "
               "López, firmaron dos acuerdos: por el primero, Cuba supervisaría la reestructuración de la inteligencia "
               "militar venezolana (DIM) y grupos de hasta 40 oficiales se entrenarían en La Habana hasta tres meses; por el "
               "segundo, un grupo de ocho «expertos militares» cubanos inspeccionaría unidades y entrenaría soldados."),
    dict(id="FR-VZ014", tipo="hecho_atribuido", id_fuente="F114", ubicacion="Párrafos 24-30 y 58-63",
         texto=f"{R19}, según cinco personas que conocían los cursos, los instructores cubanos dijeron a los agentes "
               "venezolanos que su misión sería infiltrar y controlar a las fuerzas armadas; en 2011 la DIM pasó a llamarse "
               "DGCIM, de contrainteligencia, y según exfuncionarios creció de unos cientos de agentes a por lo menos 1.500; "
               "al menos 200 militares estaban detenidos según la Asamblea Nacional opositora, y más de 300 según la "
               "organización Control Ciudadano."),
    dict(id="FR-VZ015", tipo="postura", id_fuente="F114", ubicacion="Párrafo 18", actor="gobierno_cubano",
         texto=f"{R19}, en marzo de 2019 el canciller cubano Bruno Rodríguez escribió que rechazaba «firmemente» las "
               "«reiteradas y falsas acusaciones» de que militares cubanos entrenaran, controlaran o intimidaran en "
               "Venezuela; los funcionarios cubanos no respondieron a las preguntas de Reuters."),
    dict(id="FR-VZ016", tipo="hecho_atribuido", id_fuente="F114", ubicacion="Párrafos 16 y 66",
         texto=f"{R19}, Nicolás Maduro dijo en un discurso de 2017 que estaba agradecido a las Fuerzas Armadas "
               "Revolucionarias de Cuba; Chávez se operó cuatro veces en Cuba antes de morir en 2013, y Fidel Castro lo "
               "llamó en una columna «el mejor amigo que tuvo el pueblo cubano en su historia»."),
    # ================= cuántos cubanos y las negativas
    dict(id="FR-VZ017", tipo="hecho_atribuido", id_fuente="F083", ubicacion="Sección 'Trump Administration'",
         texto=f"{CRS}, en 2019 el asesor de Seguridad Nacional John Bolton dijo que Cuba tenía entre 20.000 y 25.000 efectivos "
               "de seguridad en Venezuela, aunque expertos regionales consideraban la cifra mucho menor y sin capacidad de "
               "combate; el secretario de Estado Pompeo habló después de 2.300, y los funcionarios cubanos sostenían que la "
               "gran mayoría del personal cubano en Venezuela era sanitario."),
    dict(id="FR-VZ018", tipo="postura", id_fuente="F080", ubicacion="Apartado 'Los que negaron presencia militar cubana'",
         actor="gobierno_cubano",
         texto="Según Factchequeado, en abril de 2019 el presidente Miguel Díaz-Canel escribió que «no hay operaciones "
               "militares, ni tropas cubanas en Venezuela», la diplomática Johana Tablada afirmó que «no es posible retirar "
               "tropas que son inexistentes», y el 19 de diciembre de 2024 el viceministro de Exteriores Carlos Fernández de "
               "Cossío dijo: «No hay tropas. Cuba no participa en operaciones militares ni en operaciones de seguridad en "
               "Venezuela»."),
    dict(id="FR-VZ019", tipo="cifra_disputada", id_fuente="F083", ubicacion="Secciones citadas (F083); V.3 (F084); párrafo 5 (F109)",
         corroborado_por=["F084", "F109"],
         texto="El número de cubanos en Venezuela nunca se ha conocido con exactitud: según el Servicio de Investigación del "
               "Congreso, un estudio de 2014 estimó unos 40.000 profesionales, y en 2019 Bolton habló de 20.000 a 25.000 "
               "efectivos de seguridad y Pompeo de 2.300; Mesa-Lago menciona 40.000 profesionales en 2008, y Alma "
               "Guillermoprieto cerca de 30.000 en 2003."),
    # ================= enero de 2026
    dict(id="FR-VZ020", tipo="hecho", id_fuente="F081", ubicacion="Párrafos 1-2 (F081); párrafos 1-3 (F082)",
         corroborado_por=["F082"],
         texto="El 3 de enero de 2026 una operación militar de Estados Unidos en Caracas capturó a Nicolás Maduro; el "
               "gobierno cubano informó que 32 miembros de sus Fuerzas Armadas Revolucionarias y del Ministerio del Interior "
               "murieron en esa operación y decretó duelo nacional."),
    dict(id="FR-VZ021", tipo="postura", id_fuente="F081", ubicacion="Párrafos 2-3", actor="gobierno_cubano",
         texto="Según el comunicado de la Presidencia de Cuba recogido por Infobae, los 32 cubanos cumplían misiones «a "
               "solicitud de órganos homólogos» de Venezuela y «cayeron, tras férrea resistencia, en combate directo contra "
               "los atacantes o como resultado de los bombardeos a las instalaciones»."),
    dict(id="FR-VZ022", tipo="hecho_atribuido", id_fuente="F112", ubicacion="Párrafos 1-12",
         texto=f"{R26A}, Trump escribió que «no habrá más petróleo ni dinero para Cuba» y que Cuba vivió durante años de grandes "
               "cantidades de petróleo y dinero de Venezuela; Díaz-Canel respondió que «nadie nos dicta lo que hacemos», y el "
               "canciller Bruno Rodríguez negó que Cuba hubiera recibido compensación financiera o «material» por servicios "
               "de seguridad prestados a cualquier país; Cuba dijo que los 32 muertos se ocupaban de «seguridad y defensa», "
               "sin detallar el acuerdo."),
    dict(id="FR-VZ023", tipo="hecho_atribuido", id_fuente="F112", ubicacion="Párrafos 2 y 14-18",
         texto=f"{R26A}, Venezuela seguía siendo el mayor proveedor de petróleo de Cuba, con unos 26.500 barriles diarios en "
               "2025 según datos de seguimiento de buques y documentos internos de PDVSA, cerca del 50 % del déficit "
               "petrolero cubano, pero desde la captura de Maduro no había salido ningún cargamento hacia Cuba; México se "
               "había vuelto un proveedor alternativo, en volúmenes pequeños."),
    dict(id="FR-VZ024", tipo="hecho_atribuido", id_fuente="F111", ubicacion="Párrafos 1-7",
         texto="Según OnCuba (agosto de 2025), con datos de Reuters, las exportaciones de petróleo de PDVSA a Cuba fueron de "
               "unos 56.000 barriles diarios en 2023 y de 24.000 en 2024, bajaron a unos 10.000 en enero de 2025 y a 8.000 en "
               "junio, y subieron a 31.000 en julio de 2025."),
    dict(id="FR-VZ025", tipo="hecho_atribuido", id_fuente="F113", ubicacion="Párrafos 1-7",
         texto=f"{R26B}, asesores de seguridad y médicos cubanos estaban saliendo de Venezuela bajo la presión de Washington "
               "sobre el gobierno de la presidenta interina Delcy Rodríguez, que confió su protección a escoltas venezolanos, "
               "a diferencia de Maduro y de Chávez, que dependían de fuerzas cubanas de élite; algunos asesores cubanos fueron "
               "apartados de sus puestos en la DGCIM, aunque otros seguían en Venezuela."),
    dict(id="FR-VZ026", tipo="hecho_atribuido", id_fuente="F113", ubicacion="Párrafos 3, 10-15",
         texto=f"{R26B}, los 32 cubanos muertos formaban parte de un acuerdo de seguridad iniciado a finales de los años 2000; "
               "desde mediados de diciembre de 2025 Estados Unidos bloqueaba los envíos de petróleo venezolano a Cuba, y "
               "Cuba condenaba ese bloqueo, se decía abierta al diálogo en pie de igualdad y prometía resistir; Delcy "
               "Rodríguez y Díaz-Canel dijeron que los dos países seguían «unidos»."),
    dict(id="FR-VZ027", tipo="postura", id_fuente="F113", ubicacion="Párrafo 4", actor="Alejandro Velasco (historiador)",
         texto=f"{R26B}, el historiador Alejandro Velasco, de la Universidad de Nueva York y experto en Venezuela, considera que "
               "la influencia cubana fue «absolutamente esencial» para la supervivencia del gobierno chavista."),
]

for p in (REG, Path("validar.py")):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)
if f'"{T}"' not in Path("validar.py").read_text(encoding="utf-8"):
    print(f"validar.py no tiene la etapa {T}. Corre primero: python agregar_etapas_contexto.py")
    sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
ya = {r["id_fuente"] for r in filas}
if any(fu[0] in ya for fu in FUENTES):
    print(f"Alguna de las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]} ya está en el registro. No toco nada.")
    sys.exit(0)
faltan = [f for f in ("F080", "F081", "F082", "F083", "F084") if f not in ya]
if faltan:
    print(f"Faltan en el registro las fuentes {faltan}, que estos fragmentos reutilizan. No toco nada.")
    sys.exit(1)

lineas = []
if FRAG.exists():
    with FRAG.open(encoding="utf-8-sig") as f:
        lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n["id"] for n in NUEVOS if n["id"] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(REG, REG.with_name(f"{REG.name}.{marca}.bak"))
if FRAG.exists():
    shutil.copy2(FRAG, FRAG.with_name(f"{FRAG.name}.{marca}.bak"))

for fid, titulo, autor, url, tipo, lic, persp, uso, notas in FUENTES:
    filas.append({"id_fuente": fid, "titulo": titulo, "autor_institucion": autor, "url": url, "tipo": tipo,
                  "licencia": lic, "perspectiva": persp, "uso": uso, "fecha_consulta": HOY, "notas": notas})
tmp = REG.with_suffix(".csv.tmp")
with tmp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
    w.writeheader()
    w.writerows(filas)
tmp.replace(REG)

with FRAG.open("a", encoding="utf-8", newline="\n") as f:
    if lineas and not lineas[-1].endswith("\n"):
        f.write("\n")
    for n in NUEVOS:
        d = {"id": n["id"], "etapa": T, "tipo": n["tipo"], "id_fuente": n["id_fuente"],
             "ubicacion": n["ubicacion"], "corroborado_por": n.get("corroborado_por", []), "texto": n["texto"],
             "notas": "", "revisado": False, "estado": "pendiente"}
        if n.get("actor"):
            d["actor"] = n["actor"]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]}.")
print(f"Añadidos {len(NUEVOS)} fragmentos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
