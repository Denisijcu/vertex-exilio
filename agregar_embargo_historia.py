"""
agregar_embargo_historia.py — Registra la fuente F083 (informe del Servicio de Investigación del Congreso de
EE. UU. R45657, mayo de 2020) y añade fragmentos a fuentes/fragmentos_transversal.jsonl (FR-T075 en adelante):
historia y leyes del embargo, exportaciones permitidas, los argumentos a favor y en contra, las reclamaciones de
propiedades, las misiones médicas cubanas y las cifras de 2019 sobre cubanos en Venezuela.

Uso (desde E:\\vertex-exilio):
    python agregar_embargo_historia.py

El informe es de una oficina del Congreso de EE. UU.: datos y leyes como hechos atribuidos; su lenguaje
valorativo ('repressive communist dictatorship', 'regime') no entra. Las posiciones de cada parte (gobierno cubano,
gobierno de EE. UU., partidarios y críticos del embargo) van como postura.

Qué hace:
  1. Copia de seguridad del registro y del archivo de fragmentos.
  2. Añade F083 al registro (si ya existe, no toca nada).
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
    ("F083", "Cuba: U.S. Policy in the 116th Congress (R45657, 14 de mayo de 2020)", "Congressional Research Service",
     "https://www.everycrsreport.com/files/20200514_R45657_4e686770e0ecf08f077e9e7deba75f7f56fd26aa.html", "primaria",
     "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/CRS_R45657_2020.html. Secciones usadas: 'Background on U.S.-Cuban Relations', 'Obama "
     "Administration', 'Trump Administration', 'Debate on the Direction of U.S. Policy', 'U.S. Exports and Sanctions', "
     "'Property Claims', 'Trafficking in Persons and Cuba's Foreign Medical Missions'. Lenguaje valorativo "
     "('repressive communist dictatorship', 'regime') no entra. Recoge también posiciones del gobierno cubano: postura."),
]

NUEVOS = [
    # ---------------- origen y leyes del embargo
    dict(id="FR-T075", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Background on U.S.-Cuban Relations'",
         texto="Según el Servicio de Investigación del Congreso, el presidente Kennedy proclamó el embargo comercial a Cuba en "
               "febrero de 1962, con base en la Ley de Asistencia Exterior de 1961; en marzo de 1962 se amplió con la Ley de "
               "Comercio con el Enemigo, y en julio de 1963 el Tesoro aprobó el Reglamento de Control de Activos Cubanos, que "
               "prohíbe la mayoría de las transacciones financieras con Cuba, congela los activos del gobierno cubano en "
               "Estados Unidos y sigue siendo el núcleo del embargo."),
    dict(id="FR-T076", tipo="cifra_disputada", id_fuente="F083", ubicacion="'Background on U.S.-Cuban Relations'",
         corroborado_por=["F072"],
         texto="La fecha de inicio del embargo se da de forma distinta según la fuente: el Servicio de Investigación del "
               "Congreso sitúa la proclamación del embargo comercial en febrero de 1962, mientras que Noticias ONU dice que "
               "Estados Unidos lo mantiene desde 1960."),
    dict(id="FR-T077", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Background on U.S.-Cuban Relations'",
         texto="Según el Servicio de Investigación del Congreso, la Ley para la Democracia Cubana de 1992 prohibió a las filiales "
               "de empresas estadounidenses en el extranjero comerciar con Cuba y a los barcos que hubieran comerciado con Cuba "
               "en los 180 días anteriores cargar o descargar en Estados Unidos sin licencia; la Ley Helms-Burton (LIBERTAD) de "
               "1996, aprobada tras el derribo de las avionetas de Hermanos al Rescate, convirtió el embargo en ley permanente, "
               "de modo que el presidente no puede levantarlo sin el Congreso hasta que se cumplan ciertas condiciones "
               "democráticas."),
    dict(id="FR-T078", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Background' y 'U.S. Exports and Sanctions'",
         texto="Según el Servicio de Investigación del Congreso, desde principios de los años noventa se permiten exportaciones "
               "médicas a Cuba con verificación sobre el terreno de su uso, y la ley de 2000 conocida como TSRA autorizó las "
               "exportaciones agrícolas, pero prohíbe la ayuda y el crédito privado estadounidenses y exige pago en efectivo por "
               "adelantado o financiación de terceros países; esa misma ley prohíbe los viajes de turismo a Cuba."),
    dict(id="FR-T079", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'U.S. Exports and Sanctions'",
         texto="Según el Servicio de Investigación del Congreso, Cuba compró 6.300 millones de dólares en productos "
               "estadounidenses entre 2001 y 2019, sobre todo agrícolas; las exportaciones pasaron de unos 7 millones en 2001 a "
               "un máximo de 712 millones en 2008 y fueron de 287 millones en 2019, cuando el pollo supuso el 66 %; durante "
               "muchos años Estados Unidos fue el principal proveedor de productos agrícolas de Cuba."),
    dict(id="FR-T080", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Obama Administration: Shift Toward Engagement'",
         texto="Según el Servicio de Investigación del Congreso, en diciembre de 2014 el gobierno de Obama giró hacia el "
               "acercamiento: en mayo de 2015 sacó a Cuba de la lista de patrocinadores del terrorismo, en julio de 2015 "
               "restableció las relaciones diplomáticas, rotas en enero de 1961, y en 2015 y 2016 flexibilizó los viajes, las "
               "remesas y el comercio; Obama visitó Cuba en marzo de 2016."),
    dict(id="FR-T081", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Trump Administration: Increased Sanctions'",
         texto="Según el Servicio de Investigación del Congreso, desde 2017 el primer gobierno de Trump prohibió las "
               "transacciones con empresas controladas por los militares cubanos, como el conglomerado GAESA (una lista de 223 "
               "entidades, entre ellas 109 hoteles); en 2019 eliminó los viajes educativos y los cruceros, limitó los vuelos a "
               "La Habana, fijó un tope de 1.000 dólares por trimestre a las remesas familiares, permitió desde el 2 de mayo de "
               "2019 las demandas por propiedades confiscadas y sancionó el envío de petróleo venezolano a Cuba."),
    # ---------------- el debate
    dict(id="FR-T082", tipo="postura", id_fuente="F083", ubicacion="'Debate on the Direction of U.S. Policy'",
         actor="partidarios de flexibilizar el embargo",
         texto="Según el Servicio de Investigación del Congreso, quienes defienden flexibilizar las sanciones sostienen que más "
               "viajes, comercio y diálogo sembrarían reformas en Cuba, que hay que evitar un cambio violento y un éxodo masivo, "
               "que casi 60 años de sanciones no han hecho caer al gobierno cubano, y señalan el amplio rechazo internacional "
               "al embargo, las oportunidades perdidas para las empresas estadounidenses y el sufrimiento que causa al pueblo "
               "cubano."),
    dict(id="FR-T083", tipo="postura", id_fuente="F083", ubicacion="'Debate on the Direction of U.S. Policy'",
         actor="partidarios de mantener el embargo",
         texto="Según el Servicio de Investigación del Congreso, quienes se oponen a levantar las sanciones sostienen que aislar "
               "al gobierno cubano mientras se apoya al pueblo es la mejor vía para el cambio, que suavizar la política sin "
               "reformas concretas ayuda a ese gobierno a sobrevivir, que las sanciones pueden funcionar y que las condiciones "
               "de vida en Cuba se deben a las fallidas políticas económicas del gobierno cubano y no al embargo."),
    dict(id="FR-T084", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Debate on the Direction of U.S. Policy'",
         texto="Según el Servicio de Investigación del Congreso, las encuestas muestran que la mayoría de los estadounidenses "
               "apoya normalizar las relaciones con Cuba; entre los cubanoamericanos del sur de la Florida, una encuesta de la FIU "
               "de 2018 encontró que el 51 % quería mantener el embargo y el 49 % se oponía, frente a 2016, cuando el 63 % "
               "quería terminarlo y el 37 % lo apoyaba."),
    dict(id="FR-T085", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'U.S. Exports and Sanctions'",
         texto="Según el Servicio de Investigación del Congreso, un estudio de 2016 de la Comisión de Comercio Internacional de "
               "Estados Unidos concluyó que las restricciones estadounidenses dejan fuera a proveedores que podrían competir en "
               "Cuba, pero que también limitan el comercio las barreras cubanas, como el control estatal del comercio y los "
               "límites a la inversión extranjera; sin las restricciones de Estados Unidos, las exportaciones podrían llegar a "
               "casi 1.800 millones de dólares al año, y a unos 2.200 millones si además Cuba bajara sus barreras."),
    # ---------------- propiedades confiscadas
    dict(id="FR-T086", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Property Claims and Titles III and IV'",
         texto="Según el Servicio de Investigación del Congreso, una comisión del Departamento de Justicia certificó 5.913 "
               "reclamaciones por propiedades estadounidenses expropiadas en Cuba, valoradas en 1.900 millones de dólares, unos "
               "8.000 millones con intereses; desde mayo de 2019 se presentaron unas 25 demandas bajo el Título III de la Ley "
               "Helms-Burton, y la Unión Europea y Canadá criticaron la medida."),
    dict(id="FR-T087", tipo="postura", id_fuente="F083", ubicacion="'Property Claims and Titles III and IV'", actor="gobierno_cubano",
         texto="Según el Servicio de Investigación del Congreso, el gobierno cubano no reconoce la valoración estadounidense de "
               "las reclamaciones, propone usar el valor fiscal declarado de las propiedades, de casi 1.000 millones de dólares, "
               "sostiene que cualquier negociación debe tener en cuenta las pérdidas que le causó el embargo y las estimaba en "
               "134.500 millones de dólares a precios de 2018."),
    # ---------------- humanitario y COVID
    dict(id="FR-T088", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Increased Sanctions in 2019 and 2020'",
         texto="Según el Servicio de Investigación del Congreso, durante la pandemia de COVID-19 funcionarios de la ONU, entre "
               "ellos la alta comisionada Michelle Bachelet, pidieron a Estados Unidos aliviar las restricciones que dificultaban "
               "a Cuba conseguir equipos y medicinas; el gobierno estadounidense respondió que las sanciones ya permitían esas "
               "exportaciones, y 27 congresistas pidieron confirmar que las empresas extranjeras no estaban impedidas de enviar "
               "ayuda humanitaria."),
    # ---------------- Venezuela en 2019
    dict(id="FR-T089", tipo="cifra_disputada", id_fuente="F083", ubicacion="'Increased Sanctions in 2019 and 2020'",
         corroborado_por=["F080"],
         texto="Las cifras de personal cubano de seguridad en Venezuela en 2019 varían mucho: según el Servicio de Investigación "
               "del Congreso, el asesor de seguridad nacional John Bolton habló de 20.000 a 25.000, expertos regionales dijeron "
               "que la cifra probablemente era mucho menor, y el secretario de Estado Mike Pompeo habló de 2.300 que daban "
               "seguridad a Maduro; Factchequeado recoge que en 2015 se habló de unos 20.000 combatientes y que no hay un conteo "
               "definitivo."),
    dict(id="FR-T090", tipo="postura", id_fuente="F083", ubicacion="'Increased Sanctions in 2019 and 2020'", actor="gobierno_cubano",
         texto="Según el Servicio de Investigación del Congreso, en 2019 funcionarios cubanos afirmaban que la gran mayoría del "
               "personal cubano en Venezuela era personal médico."),
    dict(id="FR-T091", tipo="postura", id_fuente="F083", ubicacion="'Increased Sanctions in 2019 and 2020'", actor="gobierno_eeuu",
         texto="Según el Servicio de Investigación del Congreso, en marzo de 2019 Pompeo afirmó que los servicios militares y de "
               "inteligencia cubanos estaban profundamente arraigados en el Estado venezolano y daban protección física a Maduro, "
               "y en abril de 2019 Trump amenazó con un embargo 'total y completo' si Cuba no dejaba de apoyar militarmente a "
               "Maduro."),
    # ---------------- misiones médicas
    dict(id="FR-T092", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Trafficking in Persons and Cuba's Foreign Medical Missions'",
         texto="Según el Servicio de Investigación del Congreso, según estadísticas del gobierno cubano la exportación de "
               "servicios de salud generó 6.400 millones de dólares en 2018 y fue la mayor fuente de divisas del país; casi "
               "30.000 profesionales cubanos trabajaban en 72 países, gratis o al costo en 47 y con beneficio en 27; en Brasil, "
               "entre 2013 y 2018, los médicos recibían el 25 % de lo que Brasil pagaba a Cuba, y Cuba retiró a más de 8.000 "
               "cuando el nuevo gobierno brasileño exigió pagarles directamente."),
    dict(id="FR-T093", tipo="postura", id_fuente="F083", ubicacion="'Trafficking in Persons and Cuba's Foreign Medical Missions'",
         actor="críticos de las misiones médicas",
         texto="Según el Servicio de Investigación del Congreso, críticos como el secretario general de la OEA, Luis Almagro, "
               "llaman a las misiones médicas una forma de esclavitud moderna; el grupo Cuban Prisoners Defenders, con datos de "
               "más de 100 participantes, afirma que al 41 % le retuvieron el pasaporte y que más de la mitad dijo que la misión "
               "no fue voluntaria; en 2019 el Departamento de Estado bajó a Cuba al nivel 3 en su informe sobre trata de personas."),
    dict(id="FR-T094", tipo="postura", id_fuente="F083", ubicacion="'Trafficking in Persons and Cuba's Foreign Medical Missions'",
         actor="gobierno_cubano",
         texto="Según el Servicio de Investigación del Congreso, una declaración de la cancillería cubana de diciembre de 2019 "
               "sostiene que los profesionales participan en las misiones 'absolutamente por voluntad propia', que siguen "
               "cobrando su salario completo en Cuba más un estipendio en el país de destino, y que lo que Cuba cobra sostiene "
               "su sistema de salud y las misiones gratuitas en otros países."),
    # ---------------- incidentes de salud en la embajada
    dict(id="FR-T095", tipo="hecho_atribuido", id_fuente="F083", ubicacion="'Trump Administration' (incidentes de salud)",
         texto="Según el Servicio de Investigación del Congreso, entre noviembre de 2016 y mayo de 2018 26 personas de la "
               "comunidad de la embajada de Estados Unidos en La Habana sufrieron lesiones sin explicar; en septiembre de 2017 "
               "Estados Unidos redujo en dos tercios el personal de la embajada, lo que afectó sobre todo a la tramitación de "
               "visas, y en octubre ordenó la salida de 15 diplomáticos cubanos de Washington; Cuba niega cualquier "
               "responsabilidad."),
]

for p in (REG, FRAG):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
if any(fu[0] in {r["id_fuente"] for r in filas} for fu in FUENTES):
    print("La fuente F083 ya está en el registro. No toco nada.")
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

print(f"Registrada la fuente F083.")
print(f"Añadidos {len(NUEVOS)} fragmentos nuevos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
