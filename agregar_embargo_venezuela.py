"""
agregar_embargo_venezuela.py — Registra once fuentes nuevas (F072-F082) y añade fragmentos a
fuentes/fragmentos_transversal.jsonl (FR-T044 en adelante) sobre dos temas:

  1. El embargo de Estados Unidos a Cuba (que el gobierno cubano llama 'bloqueo'): la votación de la ONU del
     28 de octubre de 2026, lo que dice cada gobierno, las medidas de 2026 y el incidente del 27 de octubre en la
     Asamblea General que terminó con la expulsión de un diplomático cubano.
  2. Los militares cubanos en Venezuela: las negativas oficiales (2019-2024) y el reconocimiento de 32 muertos
     de las FAR y el MININT en la operación de Estados Unidos del 3 de enero de 2026.

Uso (desde E:\\vertex-exilio):
    python agregar_embargo_venezuela.py

Reglas aplicadas:
  - Lo que afirma el gobierno cubano (canciller, misión ante la ONU, Presidencia) va SOLO como postura.
  - Lo que afirma el gobierno de Estados Unidos (Waltz, Rubio, Trump) también va como postura cuando no está
    comprobado por otra fuente.
  - Los hechos (votos, fechas, lo que muestra un video según el medio que lo describe) van atribuidos o
    corroborados. 'Bloqueo' solo dentro de citas o atribuido.
  - Faltan por descargar (Chrome): WIKI_embargo.html, WIKI_crisis_2026.html, IRISHTIMES_2026_negacion.html.

Qué hace:
  1. Copia de seguridad del registro y del archivo de fragmentos.
  2. Añade F072-F082 al registro (si alguna ya existe, no toca nada).
  3. Añade los fragmentos nuevos en 'pendiente' (si alguno de los IDs ya existe, no toca nada).
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_transversal.jsonl")
HOY = "2026-10-30"
T = "transversal"

FUENTES = [
    ("F072", "La ONU vuelve a rechazar el embargo de Estados Unidos a Cuba (28 de octubre de 2026)", "Noticias ONU",
     "https://news.un.org/es/story/2026/10/1542113", "periodistica", "revisar", "organismo_internacional", "hechos",
     "Archivo fuentes/docs/UN_2026_votacion.html. Usa 'bloqueo' con voz propia en algunos pasajes: solo se toman "
     "datos (votos, historia de las votaciones, contenido de la resolución) y las declaraciones, atribuidas."),
    ("F073", "El embargo de Estados Unidos a Cuba vuelve a la ONU (27 de octubre de 2026)", "Noticias ONU",
     "https://news.un.org/es/story/2026/10/1542112", "periodistica", "revisar", "organismo_internacional", "hechos",
     "Archivo fuentes/docs/UN_2026_debate.html. Las cifras sanitarias que da son de 'autoridades cubanas': postura."),
    ("F074", "UN votes to condemn embargo of Cuba despite US lobbying push (28 de octubre de 2026)",
     "Al Jazeera y Reuters", "https://www.aljazeera.com/news/2026/10/28/un-votes-to-condemn-embargo-of-cuba-despite-us-lobbying-push",
     "periodistica", "revisar", "ninguna", "hechos",
     "Archivo fuentes/docs/ALJAZEERA_2026_votacion.html. Habla de 'energy blockade' con voz propia: no entra."),
    ("F075", "La ONU aprueba la resolución contra el embargo de EEUU a Cuba pese a perder apoyos clave (28 de octubre de 2026)",
     "EFE (publicado por Infobae)",
     "https://www.infobae.com/america/agencias/2026/10/28/la-onu-aprueba-la-resolucion-contra-el-embargo-de-eeuu-a-cuba-pese-a-perder-apoyos-clave/",
     "periodistica", "revisar", "ninguna", "hechos",
     "Archivo fuentes/docs/INFOBAE_2026_votacion.html. Lista de países que votaron en contra y se abstuvieron."),
    ("F076", "Cuba denuncia ante ONU el 'acoso' a uno de sus diplomáticos por parte de EE.UU. (28 de octubre de 2026)",
     "teleSUR (recoge la protesta de la Misión de Cuba ante la ONU)", "https://www.telesurtv.net/cuba-denuncia-onu-acoso-diplomatico-eeuu/",
     "periodistica", "revisar", "gobierno_cubano", "postura",
     "Archivo fuentes/docs/TELESUR_2026_incidente.html. Medio estatal venezolano alineado con La Habana: SOLO para "
     "documentar la versión del gobierno cubano sobre el incidente."),
    ("F077", "EEUU expulsa a diplomático cubano tras acusaciones de agresión en la ONU (28 de octubre de 2026)",
     "Telemundo 51", "https://www.telemundo51.com/noticias/cuba/eeuu-ordena-expulsar-diplomatico-cubano-agresion-onu/2841336/",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/TELEMUNDO_2026_expulsion.html. Describe el video del segundo incidente; las acusaciones de "
     "Waltz van como postura del gobierno de EE. UU."),
    ("F078", "Cuba denuncia daños de 7.000 millones por las sanciones y el bloqueo de EEUU desde marzo de 2025 (7 de septiembre de 2026)",
     "Europa Press (publicado por Diario Estrategia)",
     "https://www.diarioestrategia.cl/texto-diario/mostrar/6006643/cuba-denuncia-danos-7000-millones-sanciones-bloqueo-eeuu-desde-marzo-2025",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/EUROPAPRESS_2026_danos.html. Las cifras de daños son del gobierno cubano: solo postura. "
     "El titular dice 7.000 millones (euros) y el texto 8.083 millones de dólares; la cita del canciller dice "
     "'8.083.300 dólares' (unidad confusa)."),
    ("F079", "U.S. Policy Toward Cuba: Recent Developments and Congressional Considerations (IN12650, 3 de febrero de 2026)",
     "Congressional Research Service", "https://www.everycrsreport.com/reports/IN12650.html", "primaria",
     "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/CRS_IN12650_2026.html. Orden ejecutiva del 29 de enero de 2026 y medidas desde 2025. "
     "'Authoritarian regime' es lenguaje del texto: no entra sin atribución."),
    ("F080", "Militares cubanos en Venezuela: de la negación oficial al duelo nacional (7 de enero de 2026)",
     "Factchequeado (con El Toque)", "https://factchequeado.com/teexplicamos/20260107/militares-cubanos-ataque-venezuela-muerte/",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/FACTCHEQUEADO_2026_militares_venezuela.html. Recoge con fecha y cita las negativas "
     "oficiales cubanas (2019 y 2024). Usa 'régimen' con voz propia: no entra. Las estimaciones de efectivos "
     "cubanos que cita no tienen conteo definitivo."),
    ("F081", "Cuba reconoce la muerte de 32 militares en la operación de EEUU en Venezuela (5 de enero de 2026)",
     "Infobae (agencias)", "https://www.infobae.com/america/agencias/2026/01/05/cuba-reconoce-la-muerte-de-32-militares-en-la-operacion-de-eeuu-en-venezuela-para-capturar-a-maduro/",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/INFOBAE_2026_32_militares.html. Reproduce el comunicado de la Presidencia de Cuba: lo que "
     "dice el comunicado, solo como postura."),
    ("F082", "Cuba pays tribute to 32 soldiers killed in US attack on Venezuela (15 de enero de 2026)",
     "Al Jazeera y agencias", "https://www.aljazeera.com/news/2026/1/15/cuba-pays-tribute-to-soldiers-killed-in-us-attack-on-venezuela",
     "periodistica", "revisar", "ninguna", "hechos",
     "Archivo fuentes/docs/ALJAZEERA_2026_homenaje_32.html. Usa 'abduction' para la captura de Maduro: no entra."),
]

NUEVOS = [
    # ---------------- la votación de la ONU (28 de octubre de 2026)
    dict(id="FR-T044", tipo="hecho", id_fuente="F072", ubicacion="texto", corroborado_por=["F075", "F074"],
         texto="El 28 de octubre de 2026 la Asamblea General de la ONU aprobó por trigésima cuarta vez desde 1992 la "
               "resolución presentada por Cuba que pide poner fin al embargo de Estados Unidos, con 130 votos a favor, 17 "
               "en contra y 25 abstenciones; en 2025 el mismo texto había recibido 165 votos a favor, 7 en contra y 12 "
               "abstenciones. Es una resolución no vinculante."),
    dict(id="FR-T045", tipo="hecho_atribuido", id_fuente="F072", ubicacion="texto",
         texto="Según Noticias ONU, la resolución de 2026 salió adelante con el menor número de votos a favor de los "
               "últimos 20 años, y el cambio se notó sobre todo entre los países de América Latina."),
    dict(id="FR-T046", tipo="hecho_atribuido", id_fuente="F075", ubicacion="texto",
         texto="Según la agencia EFE, en 2026 votaron en contra de la resolución, además de Estados Unidos e Israel, "
               "Argentina, Colombia, Costa Rica, Ecuador, Paraguay, Hungría, Marruecos, Ucrania y Emiratos Árabes Unidos; "
               "se abstuvieron Chile, Honduras, Perú, Alemania, Grecia, Italia y República Dominicana, y Venezuela no votó "
               "porque tenía suspendido su derecho a voto por deudas con la ONU."),
    dict(id="FR-T047", tipo="hecho", id_fuente="F072", ubicacion="texto", corroborado_por=["F073"],
         texto="En 1992, primer año en que se votó la resolución contra el embargo, hubo 59 votos a favor, 3 en contra, 71 "
               "abstenciones y 46 ausencias; el máximo apoyo llegó en 2015 y 2017, con 191 votos a favor y 2 en contra, "
               "durante el acercamiento del gobierno de Obama, y en 2016 Estados Unidos se abstuvo por primera vez."),
    dict(id="FR-T048", tipo="hecho_atribuido", id_fuente="F072", ubicacion="texto",
         texto="Según Noticias ONU, la resolución expresa preocupación por la Ley Helms-Burton de 1996 por sus efectos "
               "extraterritoriales sobre otros países, y por el endurecimiento de las medidas estadounidenses desde 2017, "
               "después de la flexibilización de 2015 y 2016; Noticias ONU fecha el embargo en 1960."),
    dict(id="FR-T049", tipo="postura", id_fuente="F072", ubicacion="texto", actor="gobierno_eeuu",
         texto="Según Noticias ONU, el embajador de Estados Unidos ante la ONU, Mike Waltz, afirmó 'No hay bloqueo', citó "
               "más de 876 millones de dólares en exportaciones estadounidenses a Cuba en ocho meses de 2026 y envíos de "
               "Canadá, España, México, China, Rusia, la Unión Europea y la ONU, sostuvo que la crisis cubana se debe al "
               "propio gobierno de la isla y dijo que la riqueza del país 'simplemente cambió de manos', de la población a "
               "las élites dirigentes."),
    dict(id="FR-T050", tipo="postura", id_fuente="F072", ubicacion="texto", actor="gobierno_cubano",
         texto="Según Noticias ONU, el canciller cubano Bruno Rodríguez culpó al embargo, que su gobierno llama bloqueo, "
               "del sufrimiento del pueblo cubano, afirmó que la mortalidad infantil se había duplicado y que decenas de "
               "miles de cirugías se habían retrasado o cancelado, mostró en pantalla un costo de 22,9 millones de dólares "
               "solo durante el debate y concluyó: 'Cuba no es una amenaza, el bloqueo sí'."),
    dict(id="FR-T051", tipo="postura", id_fuente="F078", ubicacion="texto", actor="gobierno_cubano",
         texto="Según Europa Press, en septiembre de 2026 el gobierno cubano estimó en unos 8.083 millones de dólares los "
               "daños causados por las medidas de Estados Unidos entre el 1 de marzo de 2025 y el 28 de febrero de 2026, "
               "una cifra que llamó récord, y en 178.700 millones el daño acumulado; el canciller habló de 'largos meses' "
               "con solo 2 o 3 horas diarias de electricidad."),
    dict(id="FR-T052", tipo="hecho_atribuido", id_fuente="F073", ubicacion="texto",
         texto="Según Noticias ONU, el máximo representante de la ONU en Cuba, Francisco Pichón, advirtió en 2026 de una "
               "crisis energética y de un posible colapso humanitario en la isla, y la Organización Mundial de la Salud "
               "alertó de que la escasez de energía estaba afectando a la salud."),
    dict(id="FR-T053", tipo="postura", id_fuente="F073", ubicacion="texto", actor="gobierno_cubano",
         texto="Según Noticias ONU, las autoridades cubanas señalaron el aplazamiento de más de 100.000 intervenciones "
               "quirúrgicas hasta mayo de 2026, retrasos en la vacunación y falta de un suministro estable de medicamentos "
               "para enfermos crónicos."),
    dict(id="FR-T054", tipo="postura", id_fuente="F073", ubicacion="texto", actor="expertos de derechos humanos de la ONU",
         texto="Según Noticias ONU, varios altos comisionados de derechos humanos, relatores y expertos independientes de "
               "la ONU han considerado el embargo y las sanciones unilaterales de Estados Unidos 'una amenaza para los "
               "derechos a la salud, la vida, la alimentación y el desarrollo' del pueblo cubano."),
    dict(id="FR-T055", tipo="hecho_atribuido", id_fuente="F079", ubicacion="texto",
         texto="Según el Servicio de Investigación del Congreso, el 29 de enero de 2026 Trump firmó una orden ejecutiva que "
               "declaró una emergencia nacional respecto a Cuba y creó un sistema para imponer aranceles a los países que "
               "suministren petróleo a Cuba directa o indirectamente; tras la captura de Nicolás Maduro en enero de 2026, "
               "Estados Unidos cortó el petróleo venezolano a Cuba, su principal proveedor desde principios de los años 2000."),
    dict(id="FR-T056", tipo="hecho_atribuido", id_fuente="F079", ubicacion="texto",
         texto="Según el Servicio de Investigación del Congreso, desde enero de 2025 el gobierno de Trump mantuvo a Cuba en la "
               "lista de Estados patrocinadores del terrorismo, impuso restricciones de visado por el programa cubano de "
               "exportación de mano de obra y ordenó endurecer las normas sobre viajes y remesas, con el objetivo declarado "
               "de promover la democracia, los derechos humanos y la economía de mercado en Cuba."),
    dict(id="FR-T057", tipo="postura", id_fuente="F079", ubicacion="texto", actor="expertos citados por el CRS",
         texto="Según el Servicio de Investigación del Congreso, algunos expertos, ex funcionarios estadounidenses y "
               "organizaciones religiosas cubanas temen las consecuencias humanitarias y migratorias de aumentar la presión "
               "económica, mientras que otros, entre ellos un destacado exiliado cubano, la apoyan como la mejor vía para un "
               "cambio político; algunos expertos dudan de que el gobierno cubano caiga solo por medios económicos."),
    dict(id="FR-T058", tipo="postura", id_fuente="F077", ubicacion="texto", actor="gobierno_eeuu",
         texto="Según Telemundo, Estados Unidos considera el embargo una herramienta de presión para lograr cambios políticos "
               "en Cuba, entre ellos una transición democrática, elecciones libres, respeto a los derechos humanos y "
               "compensación por las propiedades estadounidenses nacionalizadas después de 1959."),
    dict(id="FR-T059", tipo="hecho_atribuido", id_fuente="F075", ubicacion="texto",
         texto="Según la agencia EFE, la votación de 2026 coincidió con dos órdenes ejecutivas de Trump que establecen "
               "sanciones contra quienes vendan petróleo a Cuba o comercien con la isla, y Estados Unidos había pedido a los "
               "miembros de la ONU que votaran en contra de la resolución."),
    # ---------------- el incidente del 27 de octubre y la expulsión
    dict(id="FR-T060", tipo="hecho", id_fuente="F073", ubicacion="texto", corroborado_por=["F075", "F077"],
         texto="El 27 de octubre de 2026, durante el debate sobre el embargo en la Asamblea General, el canciller cubano Bruno "
               "Rodríguez interrumpió con una moción de orden el discurso del embajador estadounidense Mike Waltz; hubo un "
               "enfrentamiento a gritos y el presidente de la Asamblea suspendió brevemente la sesión."),
    dict(id="FR-T061", tipo="hecho_atribuido", id_fuente="F077", ubicacion="texto",
         texto="Según Telemundo, Waltz mostraba imágenes de bienes de lujo y propiedades que atribuyó a dirigentes cubanos y "
               "sus familiares cuando el canciller Rodríguez y el embajador cubano Ernesto Soberón se acercaron al podio; "
               "Waltz respondió: 'Esto no es La Habana. No me vas a intimidar'."),
    dict(id="FR-T062", tipo="hecho_atribuido", id_fuente="F077", ubicacion="texto",
         texto="Según Telemundo, en un video difundido por Waltz se ve al primer secretario de la misión cubana, Richard Tur "
               "de la Concepción, golpear o apartar varias veces el teléfono de una persona que lo estaba grabando, "
               "identificada como portavoz del embajador estadounidense, mientras protesta por la grabación y pide la "
               "intervención de seguridad alegando una invasión de su espacio personal."),
    dict(id="FR-T063", tipo="postura", id_fuente="F077", ubicacion="texto", actor="gobierno_eeuu", corroborado_por=["F074"],
         texto="Según Telemundo, Waltz anunció que el secretario de Estado Marco Rubio había firmado la expulsión de Richard "
               "Tur de la Concepción, a quien acusó de haber empujado e intentado agredir a un diplomático estadounidense, y "
               "dijo que en 24 horas estaría en un avión rumbo a La Habana."),
    dict(id="FR-T064", tipo="postura", id_fuente="F076", ubicacion="texto", actor="gobierno_cubano",
         texto="Según teleSUR, la Misión de Cuba ante la ONU protestó formalmente ante el secretario general por lo que llamó "
               "'acoso, acecho e invasión del espacio personal' de John P. Freire, portavoz de Waltz, contra Richard Tur; "
               "afirmó que Freire lo persiguió y grabó de forma invasiva, que tuvo que intervenir la seguridad de la ONU, y "
               "lo presentó como parte de una campaña de Estados Unidos para restar credibilidad a Cuba."),
    dict(id="FR-T065", tipo="postura", id_fuente="F074", ubicacion="texto", actor="gobierno_cubano",
         texto="Según Al Jazeera, tras la votación el canciller Bruno Rodríguez escribió que Estados Unidos estaba 'una vez "
               "más aislado en su intento de seguir estrangulando al pueblo cubano', y funcionarios cubanos acusaron a "
               "Estados Unidos de amenazar a otros países con aranceles y restricciones de visado si votaban a favor."),
    dict(id="FR-T066", tipo="postura", id_fuente="F074", ubicacion="texto", actor="gobierno_eeuu",
         texto="Según Al Jazeera, Waltz dijo tras la votación que estaba satisfecho de que grandes economías como Corea y "
               "Alemania hubieran cambiado de posición, y que esperaba que la tendencia siguiera creciendo: 'La diplomacia "
               "lleva tiempo'."),
    # ---------------- militares cubanos en Venezuela
    dict(id="FR-T067", tipo="hecho", id_fuente="F080", ubicacion="texto", corroborado_por=["F081", "F082"],
         texto="El 4 de enero de 2026 el gobierno cubano confirmó que 32 cubanos, miembros de las Fuerzas Armadas "
               "Revolucionarias y del Ministerio del Interior, murieron durante la operación militar de Estados Unidos del 3 "
               "de enero de 2026 en Venezuela, en la que Nicolás Maduro fue capturado; según el gobierno cubano cumplían "
               "misiones 'a solicitud de órganos homólogos' venezolanos, y Díaz-Canel decretó dos días de duelo nacional."),
    dict(id="FR-T068", tipo="hecho_atribuido", id_fuente="F080", ubicacion="texto",
         texto="Según Factchequeado, en abril de 2019 Miguel Díaz-Canel escribió que 'no hay operaciones militares, ni tropas "
               "cubanas en Venezuela'; Johana Tablada, entonces subdirectora de Estados Unidos en la cancillería, dijo que 'no "
               "es posible retirar tropas que son inexistentes', y el canciller Bruno Rodríguez negó la presencia de tropas y "
               "exigió pruebas a Estados Unidos."),
    dict(id="FR-T069", tipo="hecho_atribuido", id_fuente="F080", ubicacion="texto",
         texto="Según Factchequeado, el 19 de diciembre de 2024 el viceministro de Relaciones Exteriores Carlos Fernández de "
               "Cossío dijo que 'nadie ha visto nunca un batallón cubano en Venezuela' y que 'no hay tropas. Cuba no "
               "participa en operaciones militares ni en operaciones de seguridad en Venezuela'."),
    dict(id="FR-T070", tipo="postura", id_fuente="F081", ubicacion="texto", actor="gobierno_cubano",
         texto="Según el comunicado de la Presidencia de Cuba recogido por Infobae, los cubanos 'cayeron, tras férrea "
               "resistencia, en combate directo contra los atacantes o como resultado de los bombardeos'; Díaz-Canel dijo que "
               "protegían la vida de Maduro y de su esposa 'por solicitud de esa hermana nación' y llamó a la operación "
               "'criminal ataque'."),
    dict(id="FR-T071", tipo="hecho_atribuido", id_fuente="F082", ubicacion="texto",
         texto="Según Al Jazeera, el 15 de enero de 2026 los restos llegaron a La Habana en ataúdes cubiertos con la bandera; "
               "Díaz-Canel y Raúl Castro los recibieron con uniforme militar, miles de personas se alinearon en la avenida al "
               "paso de la caravana y el ministro del Interior, Lázaro Alberto Álvarez, dijo que habían combatido 'hasta la "
               "última bala'."),
    dict(id="FR-T072", tipo="postura", id_fuente="F080", ubicacion="texto", actor="gobierno_eeuu",
         texto="Según Factchequeado, antes de que Cuba confirmara las muertes, Trump dijo que 'muchos cubanos murieron' en la "
               "operación y Marco Rubio afirmó que los guardias de Maduro y toda su agencia de espionaje 'estaban llenos de "
               "cubanos'."),
    dict(id="FR-T073", tipo="hecho_atribuido", id_fuente="F080", ubicacion="texto",
         texto="Según Factchequeado, antes del reconocimiento oficial ya había informes sobre la presencia militar y de "
               "inteligencia cubana en Venezuela: Reuters reveló dos acuerdos de mayo de 2008 que dieron a Cuba amplio acceso "
               "al sector militar venezolano, y un experto de la Misión de Determinación de Hechos de la ONU sobre Venezuela "
               "dijo que ex funcionarios de la inteligencia militar venezolana declararon haber sido adiestrados por personal "
               "militar cubano; la cancillería cubana calificó de 'falsas' esas denuncias."),
    dict(id="FR-T074", tipo="hecho_atribuido", id_fuente="F080", ubicacion="texto",
         texto="Según Factchequeado, no existe un conteo definitivo de cuántos militares y agentes cubanos había en Venezuela; "
               "en 2015 El Nuevo Herald habló de unos 20.000 combatientes cubanos, con base en estimaciones de un general "
               "venezolano retirado."),
]

for p in (REG, FRAG):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
if any(fu[0] in {r["id_fuente"] for r in filas} for fu in FUENTES):
    print("Alguna de las fuentes F072-F082 ya está en el registro. No toco nada.")
    sys.exit(0)

with FRAG.open(encoding="utf-8-sig") as f:
    lineas = [l for l in f if l.strip()]
existentes = {json.loads(l)["id"] for l in lineas}
repetidos = [n["id"] for n in NUEVOS if n["id"] in existentes]
if repetidos:
    print(f"Estos IDs ya están en {FRAG}: {', '.join(repetidos[:5])}... No toco nada.")
    sys.exit(0)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(REG, REG.with_name(f"{REG.name}.{marca}.bak"))
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

print(f"Registradas {len(FUENTES)} fuentes (F072 a F082).")
print(f"Añadidos {len(NUEVOS)} fragmentos nuevos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
