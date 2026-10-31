"""
agregar_cuba_antes_despues.py — Primer lote del módulo "Cuba: contexto", etapa cuba_antes_despues.

Registra las fuentes F084-F089 y crea fuentes/fragmentos_cuba_antes_despues.jsonl (FR-C001 en adelante):
economía y sociedad de Cuba antes y después de 1959 (indicadores sociales, PIB, azúcar, ganado, comercio).

Uso (desde E:\\vertex-exilio), DESPUÉS de haber corrido agregar_etapas_contexto.py:
    python agregar_cuba_antes_despues.py

Criterios:
  - Mesa-Lago (2009) es la columna vertebral: compara 84 indicadores de 1958 y 2008 y da los dos lados
    (avances sociales y deterioro económico). Sus valoraciones van como postura con actor.
  - El informe del Departamento de Estado (1998, revisado 2002) es gobierno_eeuu: sus cifras (de la ONU y la FAO)
    entran como hecho atribuido; su tesis y su lenguaje valorativo ("enduring myth", "Castro government") no
    entran o van como postura. La afirmación sobre el aborto y la mortalidad infantil NO entra (no la corrobora
    ninguna otra fuente del registro).
  - Lo que dicen Granma, Azcuba o "La Habana" va como postura del gobierno cubano.
  - Falta la postura oficial cubana sobre los logros sociales (EcuRed no bajó): queda pendiente.

Qué hace:
  1. Comprueba que validar.py ya tiene la etapa cuba_antes_despues.
  2. Copia de seguridad del registro (y del archivo de fragmentos si ya existiera).
  3. Añade F084-F089 al registro (si alguna ya existe, no toca nada).
  4. Crea el archivo de fragmentos (o añade al final si existe) en estado 'pendiente'.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_cuba_antes_despues.jsonl")
HOY = "2026-10-30"
T = "cuba_antes_despues"

ML = "Según el economista Carmelo Mesa-Lago (Universidad de Pittsburgh)"
SA = "Según el historiador económico Antonio Santamaría García"
EFE = "Según un reportaje de la agencia EFE publicado por OnCuba en 2021"
DE = "Según un informe del Departamento de Estado de EE. UU. (1998, revisado en 2002)"

FUENTES = [
    ("F084", "Balance económico-social de 50 años de Revolución en Cuba (América Latina Hoy, vol. 52, 2009, pp. 41-61)",
     "Carmelo Mesa-Lago, Universidad de Pittsburgh", "https://www.redalyc.org/articulo.oa?id=30811997003",
     "academica", "revisar (Redalyc, acceso abierto)", "academica", "hechos",
     "Archivo fuentes/docs/MESALAGO_2009_balance50.pdf. Tablas I-IV y secciones II-VII. Compara 1957-58, 1989 y "
     "2007-08 con 84 indicadores y el orden de Cuba entre 20 países de América Latina. El autor advierte que la "
     "comparación es difícil y preliminar. Sus juicios (p. ej. sobre el embargo o la tasa de desempleo) van como postura."),
    ("F085", "Azúcar y Revolución. El sector azucarero de la economía cubana durante los primeros doce años de la "
             "Revolución (1959-1970) (Revista de Historia Económica, XII-1, 1994, pp. 111-141)",
     "Antonio Santamaría García, Instituto Universitario Ortega y Gasset",
     "https://e-archivo.uc3m.es/bitstream/handle/10016/1931/RHE-1994-XII-1-Santamaria.pdf?sequence=1",
     "academica", "revisar (repositorio e-Archivo UC3M)", "academica", "hechos",
     "Archivo fuentes/docs/SANTAMARIA_azucar_1959_1970.pdf (escaneo con OCR: cifras comprobadas contra los cuadros 1, 3 "
     "y 9). El autor usa 'bloqueo norteamericano' con voz propia: no entra."),
    ("F086", "Cuba: la crisis de una industria que no despega (4 de mayo de 2021)", "EFE, publicado por OnCuba News",
     "https://oncubanews.com/cuba/cuba-la-crisis-de-una-industria-que-no-despega/", "periodistica", "revisar",
     "ninguna", "ambos",
     "Archivo fuentes/docs/ONCUBA_2021_azucar.html. Lo que dicen Azcuba y 'estimaciones de La Habana': postura. "
     "Fecha la zafra de 8,5 millones como '1970-71'; el registro usa 1970 (Santamaría, F085). La frase sobre "
     "'bloquear la entrada de divisas' es valoración: no entra."),
    ("F087", "Confirmada tendencia al decrecimiento: menos de tres millones de vacas tras conteo gubernamental "
             "(13 de febrero de 2025)", "Redacción OnCuba",
     "https://oncubanews.com/cuba/economia/confirmada-tendencia-al-decrecimiento-menos-de-tres-millones-de-vacas-tras-conteo-gubernamental/",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/ONCUBA_2025_ganado.html. Cifras del Ministerio de la Agricultura citadas por Granma; las "
     "explicaciones de Granma: postura. Las cifras históricas (1959, 1985, 2006-2014) son de 14ymedio citadas por OnCuba."),
    ("F088", "Cuba loosens regulations on killing cows and selling beef (14 de abril de 2021)", "Marc Frank, Reuters",
     "https://finance.yahoo.com/news/cuba-loosens-regulations-killing-cows-141728315.html", "periodistica", "revisar",
     "ninguna", "hechos",
     "Archivo fuentes/docs/REUTERS_2021_ganado.html (copia de Reuters en Yahoo Finance). 'Communist-run' es "
     "descriptor de agencia: no entra."),
    ("F089", "Zenith and Eclipse: A Comparative Look at Socio-Economic Conditions in Pre-Castro and Present Day Cuba "
             "(9 de febrero de 1998, revisado en junio de 2002)",
     "Departamento de Estado de EE. UU., Oficina de Asuntos Interamericanos",
     "https://webarchive.library.unt.edu/eot2008/20081015151601/http://www.state.gov/p/wha/ci/14776.htm",
     "primaria", "dominio_publico (obra del gobierno de EE. UU.)", "gobierno_eeuu", "ambos",
     "Archivo fuentes/docs/STATE_zenith_eclipse.html (copia en globalsecurity.org; original archivado por la UNT). "
     "Cifras de anuarios de la ONU y la FAO: hecho atribuido. Su tesis es postura del gobierno de EE. UU. y su "
     "lenguaje ('enduring myth', 'Castro government') no entra. La afirmación sobre aborto y mortalidad infantil no "
     "entra: ninguna otra fuente la corrobora."),
]

NUEVOS = [
    # ================= Mesa-Lago: marco general
    dict(id="FR-C001", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Resumen y sección VII 'Balance económico-social'",
         texto=f"{ML}, de 84 indicadores comparados entre 1957-1958 y 2007-2008, la mayoría de los económicos empeoró y la "
               "mayoría de los sociales mejoró: en la economía interna se deterioró el 66 % y mejoró el 34 %, mientras que en "
               "los sociales mejoró el 76 % y empeoró el 24 %; además, entre 1989 y 2008 dos tercios de todos los indicadores "
               "se deterioraron."),
    dict(id="FR-C002", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección II, primer párrafo",
         texto=f"{ML}, en vísperas de la Revolución Cuba estaba entre los primeros países de América Latina en PIB por "
               "habitante, control de la inflación, estabilidad fiscal, inversión, alfabetización, mortalidad infantil, "
               "esperanza de vida y cobertura de pensiones."),
    dict(id="FR-C003", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección II, primer párrafo",
         texto=f"{ML}, la Cuba de 1958 también tenía problemas graves: crecimiento económico bajo que beneficiaba sobre todo "
               "al capital y a los trabajadores empleados y sindicalizados, un sector azucarero estancado, alto desempleo que "
               "se agudizaba después de la zafra, una gran brecha entre zonas urbanas y rurales y una fuerte dependencia del "
               "azúcar y de Estados Unidos."),
    dict(id="FR-C004", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.1",
         texto=f"{ML}, según el censo de 1953 el analfabetismo era del 23,6 % a nivel nacional, pero del 11,6 % en las zonas "
               "urbanas y del 41,8 % en las rurales; la mayoría de estas desigualdades entre campo y ciudad se redujo "
               "notablemente bajo la Revolución."),
    dict(id="FR-C005", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección III",
         texto=f"{ML}, comparar los indicadores de 1958 y 2008 es muy difícil: la última cifra prerrevolucionaria de "
               "alfabetización y vivienda es del censo de 1953, el registro de enfermedades en 1958 era probablemente peor, "
               "casi todos los países de la región progresaron en medio siglo y la población de Cuba creció un 65 %; por eso "
               "el autor compara la posición de Cuba entre 20 países latinoamericanos y presenta su estudio como preliminar."),
    # ================= Mesa-Lago: economía
    dict(id="FR-C006", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección IV.1 y Tabla I",
         texto=f"{ML}, en 1958 el PIB por habitante de Cuba era el tercero de América Latina, detrás de Venezuela y Uruguay, y "
               "en 2007 había bajado al noveno, undécimo o duodécimo lugar según el método; medido en pesos corrientes "
               "convertidos a dólares cayó un 27 % entre 1958 y 2007. El autor advierte que el gobierno cambió al menos cuatro "
               "veces la forma de calcular el producto, y que desde 2003 suma al PIB los servicios sociales gratuitos, lo que "
               "lo sobreestima."),
    dict(id="FR-C007", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección IV.1 y Tabla I",
         texto=f"{ML}, la inversión (formación bruta de capital fijo) era el 17,6 % del PIB en 1957, la quinta más alta de la "
               "región; subió al 25,6 % en 1989 y cayó al 8,2 % en 2007, la menor de los veinte países; el déficit fiscal pasó "
               "de un pequeño superávit en 1958 a cerca del 7 % del PIB en 2008."),
    dict(id="FR-C008", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección II, nota 2",
         texto=f"{ML}, la ayuda de la URSS se estima en 65.000 millones de dólares entre 1960 y 1990, de los cuales solo el 39 % "
               "eran préstamos y solo el 0,6 % se pagó; tras el colapso del campo socialista el PIB cayó un 35 % entre 1989 y "
               "1993, la etapa que el gobierno llamó «Período Especial en Tiempo de Paz»."),
    dict(id="FR-C009", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección IV.2, V.2 y Tablas I-II",
         texto=f"{ML}, la producción de azúcar cayó un 88 % entre 1958 y 2008, de 8 a 1,2 millones de toneladas, y la zafra de "
               "2007 fue la peor desde 1903; el azúcar pasó del 81 % al 5 % de las exportaciones, sobre todo después de la "
               "reestructuración de 2002, que redujo a la mitad las siembras de caña y los centrales."),
    dict(id="FR-C010", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección IV.2 y Tabla I",
         texto=f"{ML}, las cabezas de ganado vacuno por cada mil habitantes bajaron de 835 en 1957-1958 a 465 en 1989 y a 337 "
               "en 2007; por habitante, entre 1958 y 2007 la producción de carne de res cayó un 66 %, la de leche un 57 % y la "
               "de café un 93 %."),
    dict(id="FR-C011", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección IV.2 y V.2",
         texto=f"{ML}, de doce productos agrícolas, ocho estaban en 2007 muy por debajo del nivel de 1957; ese año el 19 % de la "
               "población activa agrícola generaba solo el 3,9 % del PIB, y en 2008 Cuba importó el 84 % de los alimentos de "
               "la canasta básica, con un costo de 2.500 millones de dólares."),
    dict(id="FR-C012", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Secciones IV.2 y V.2",
         texto=f"{ML}, no todo empeoró: entre 1958 y 2007 la producción de níquel por habitante aumentó un 133 %, la generación "
               "de electricidad un 315 % y la de huevos un 339 %, y los minerales, sobre todo níquel, pasaron del 6 % al 57 % "
               "de las exportaciones gracias a la inversión extranjera iniciada en los años noventa."),
    dict(id="FR-C013", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección V.3",
         texto=f"{ML}, el comercio con el socio principal fue el 62 % con Estados Unidos en 1958, el 65 % con la URSS en 1989 y "
               "el 20 % con Venezuela en 2008; la ayuda de Venezuela se estimó en 9.405 millones de dólares en 2008, incluidos "
               "5.650 millones por los servicios de 40.000 médicos, maestros y otros profesionales cubanos y 97.000 barriles "
               "diarios de crudo y derivados."),
    dict(id="FR-C014", tipo="postura", id_fuente="F084", ubicacion="Sección V.5", actor="Carmelo Mesa-Lago (economista)",
         texto=f"{ML}, la dirigencia cubana culpa al embargo estadounidense de los problemas económicos, pero desde 2002 el "
               "grueso de los alimentos importados viene de Estados Unidos; el autor sostiene que, sin restar el efecto "
               "adverso del embargo, la causa fundamental ha sido la política económica: la colectivización y centralización "
               "de casi toda la economía, siete cambios de organización económica y la virtual eliminación del incentivo "
               "individual."),
    # ================= Mesa-Lago: sociedad
    dict(id="FR-C015", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.1 y Tabla III",
         texto=f"{ML}, el salario medio real cayó un 76 % entre 1989 y 2008; las cuotas de la libreta de racionamiento cubrían "
               "más o menos una semana de alimentos al mes y el resto había que comprarlo a precios entre noventa y "
               "trescientas veces mayores; Raúl Castro reconoció que el salario no alcanzaba para las necesidades mínimas."),
    dict(id="FR-C016", tipo="postura", id_fuente="F084", ubicacion="Sección VI.1", actor="Carmelo Mesa-Lago (economista)",
         texto=f"{ML}, el desempleo declarado bajó del 16,4 % en 1956-1957 al 1,6 % en 2008, el más bajo de la región, pero el "
               "autor considera esa tasa «amañada» porque cuenta como ocupados a despedidos en reentrenamiento, estudiantes "
               "y cultivadores de traspatio, y cita a economistas cubanos que estiman innecesario entre el 30 % y el 40 % del "
               "empleo."),
    dict(id="FR-C017", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.1 y Tabla III",
         texto=f"{ML}, el coeficiente de Gini, que mide la desigualdad del ingreso, bajó de 0,550 en 1953 a 0,250 en 1989 y "
               "subió a 0,407 en 1999, según estimaciones académicas porque Cuba no publica esa cifra; esos cálculos excluyen "
               "las remesas, que recibían dos tercios de la población."),
    dict(id="FR-C018", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.2 y Tablas III-IV",
         texto=f"{ML}, la Revolución expandió la educación pública gratuita, expropió las escuelas y universidades privadas y "
               "prohibió la enseñanza privada; la alfabetización pasó del 76,4 % en 1953 al 97,9 % en 2006, la matrícula "
               "secundaria del 29 % al 87 % y Cuba quedó primera de la región en matrícula secundaria y universitaria."),
    dict(id="FR-C019", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.3 y Tablas III-IV",
         texto=f"{ML}, la Revolución expandió la salud pública gratuita, nacionalizó las instalaciones de cooperativas, mutuales y entidades privadas y prohibió "
               "la medicina privada; los hospitales rurales pasaron de uno a sesenta y dos, la mortalidad infantil bajó de "
               "33,4 a 5,3 por mil nacidos vivos y fue la más baja de la región tanto en 1957 como en 2007, la esperanza de "
               "vida subió de 64,0 a 78,3 años y los médicos por cada 10.000 habitantes de 9,2 a 64,0."),
    dict(id="FR-C020", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.3",
         texto=f"{ML}, entre el 35 % y el 48 % de los médicos trabajaba en el exterior, sobre todo en Venezuela, lo que redujo "
               "el acceso a la atención dentro de la isla; las farmacias estatales carecían de la mayoría de las medicinas "
               "básicas; seis enfermedades se erradicaron, pero otras, como la hepatitis y las venéreas, aumentaron."),
    dict(id="FR-C021", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.4 y Tabla III",
         texto=f"{ML}, la cobertura de pensiones era del 63 % de la población activa en 1958, la segunda de la región, y se "
               "estima en un 85 % en 2007, la primera; pero la pensión media real cayó un 62 % entre 1989 y 2008."),
    dict(id="FR-C022", tipo="hecho_atribuido", id_fuente="F084", ubicacion="Sección VI.5 y Tabla IV",
         texto=f"{ML}, se construían 6,3 viviendas por mil habitantes al año en 1946-1953 y 3,8 en 2000-2008; las viviendas en "
               "buen estado eran el 52 % en 1953 y el 57 % en 2007, sin cambio importante, y el déficit superaba el millón de "
               "unidades. En automóviles y periódicos por habitante Cuba bajó del quinto y tercer lugar en 1958 al último y "
               "decimosexto, y en teléfonos fijos del tercero al decimoctavo."),
    # ================= Santamaría: azúcar 1959-1970
    dict(id="FR-C023", tipo="hecho_atribuido", id_fuente="F085", ubicacion="Cuadro 1",
         texto=f"{SA}, Cuba produjo 5,614 millones de toneladas de azúcar en 1958, el 12,63 % de la producción mundial; "
               "6,875 millones en 1961; 3,882 millones en 1963, la peor cosecha del período, y 8,537 millones en 1970."),
    dict(id="FR-C024", tipo="hecho_atribuido", id_fuente="F085", ubicacion="Sección I",
         texto=f"{SA}, que retoma una periodización de Mesa-Lago, entre 1959 y 1963 los dirigentes revolucionarios intentaron "
               "una estrategia de industrialización contraria al azúcar, y desde 1963 volvieron al azúcar y aplazaron la "
               "industria pesada; el autor matiza que la vuelta definitiva al azúcar no llegó hasta 1970, y concluye que el "
               "azúcar sostuvo la economía, pero impidió la diversificación y acentuó la dependencia de un solo producto."),
    dict(id="FR-C025", tipo="hecho", id_fuente="F085", ubicacion="Secciones I y III, cuadro 3", corroborado_por=["F086"],
         texto="En 1970 el gobierno cubano se propuso una zafra de 10 millones de toneladas de azúcar y se lograron unos 8,5 "
               "millones; el historiador Antonio Santamaría García señala que se obtuvo en detrimento de otros sectores y que "
               "retrasó la recuperación de la producción hasta después de 1973."),
    dict(id="FR-C026", tipo="hecho_atribuido", id_fuente="F085", ubicacion="Cuadro 3 y sección III",
         texto=f"{SA}, la URSS pagó por el azúcar cubano un precio estable de 6,1 centavos de dólar por libra desde 1963, "
               "mientras el precio mundial bajó a 2,1 en 1965 y estaba en 3,8 en 1970; esas subvenciones permitieron "
               "financiar la política económica de los años sesenta."),
    dict(id="FR-C027", tipo="hecho_atribuido", id_fuente="F085", ubicacion="Cuadro 9 y sección IV",
         texto=f"{SA}, el azúcar fue el 78 % de las exportaciones cubanas en 1957 y 1958 y el 77 % en 1970, con una media de "
               "81,64 % entre 1957 y 1970; en 1961 la URSS sustituyó a Estados Unidos como mayor comprador, y en 1970 el 76 % "
               "de las exportaciones cubanas iba a la URSS, frente al 77 % que iba a Estados Unidos en 1959."),
    # ================= EFE / OnCuba 2021: industria azucarera
    dict(id="FR-C028", tipo="hecho_atribuido", id_fuente="F086", ubicacion="Entradilla y párrafos 1-2",
         texto=f"{EFE}, de los 156 centrales que operaban antes de 1959 quedaban 56, y solo 38 molían en la zafra 2020-2021, "
               "que no alcanzaría la meta de 1,2 millones de toneladas."),
    dict(id="FR-C029", tipo="hecho_atribuido", id_fuente="F086", ubicacion="Apartado 'La dulce nacionalización'",
         texto=f"{EFE}, a finales de los años cincuenta había en Cuba 161 centrales: 131 eran de cubanos acaudalados y "
               "producían el 60 % del azúcar, frente al 37 % de empresarios estadounidenses; el azúcar era cerca del 80 % de "
               "las exportaciones y su principal mercado era Estados Unidos, con una cuota preferencial."),
    dict(id="FR-C030", tipo="hecho_atribuido", id_fuente="F086", ubicacion="Apartado 'La dulce nacionalización'",
         texto=f"{EFE}, en 1960 Cuba hizo su última exportación de azúcar a Estados Unidos, de 1,9 millones de toneladas; "
               "Washington suspendió la cuota preferencial, Cuba nacionalizó los centrales, incluidos los de propiedad "
               "estadounidense, y la Unión Soviética se comprometió a comprar una parte mayor de la cosecha."),
    dict(id="FR-C031", tipo="hecho_atribuido", id_fuente="F086", ubicacion="Apartados 'Los diez millones' y 'Drástica caída'",
         texto=f"{EFE}, la zafra llegó a 7,4 millones de toneladas en 1980-1981 y a 8,1 millones en 1988-1989; tras la "
               "desaparición de la URSS, cinco años después, cayó a 4,3 millones; en 2002 Fidel Castro anunció el cierre del 70 % de los "
               "centrales, con lo que se redujo a la mitad la capacidad de producción y el 60 % de las tierras de caña pasó a "
               "otros cultivos, y en 2010 hubo la peor zafra en 105 años, con apenas un millón de toneladas."),
    dict(id="FR-C032", tipo="postura", id_fuente="F086", ubicacion="Párrafos 3 y 6-8", actor="gobierno_cubano",
         texto=f"{EFE}, el embargo ha afectado a la industria azucarera con pérdidas de unos 125.000 millones de dólares según "
               "estimaciones de La Habana; el vicepresidente primero del grupo estatal Azcuba, José Carlos Santos, dijo que "
               "Cuba debe sortear «la persecución financiera» del embargo para importar insumos y piezas, y afirmó que desde "
               "el huracán Irma de 2017 se dejaron de producir 700.000 toneladas."),
    dict(id="FR-C033", tipo="hecho_atribuido", id_fuente="F086", ubicacion="Párrafo 4",
         texto=f"{EFE}, además del embargo, frenan al sector la obsolescencia tecnológica, la falta de fertilizantes y "
               "combustible y la escasez de financiamiento, lo que provoca paradas frecuentes en los centrales y caña de mala "
               "calidad."),
    # ================= Ganado: OnCuba 2025 y Reuters 2021
    dict(id="FR-C034", tipo="hecho_atribuido", id_fuente="F087", ubicacion="Párrafos 1-6",
         texto="Según el Ministerio de la Agricultura, citado por OnCuba en febrero de 2025, un conteo hecho entre marzo de "
               "2024 y enero de 2025 en 191.802 propietarios, el 99,7 % del total, halló 2.914.009 cabezas de ganado vacuno; "
               "se registraron 181.854 ilegalidades, entre ellas 43.143 nacimientos sin declarar."),
    dict(id="FR-C035", tipo="postura", id_fuente="F087", ubicacion="Apartado 'Tendencia: decrecimiento de la masa'",
         actor="gobierno_cubano",
         texto="Según OnCuba, el diario oficial Granma atribuye la caída de la masa ganadera a cambios en las tecnologías de "
               "crianza, la falta de insumos veterinarios y alimentos, el deterioro de los indicadores productivos y el hurto "
               "y sacrificio de animales."),
    dict(id="FR-C036", tipo="hecho_atribuido", id_fuente="F087", ubicacion="Apartado 'Tendencia: decrecimiento de la masa'",
         texto="Según cifras del diario independiente 14ymedio citadas por OnCuba, en 1959 había 5,1 millones de cabezas de "
               "ganado vacuno para 6,5 millones de habitantes, en 1985 poco más de cinco millones, y el único período de "
               "ligera recuperación fue entre 2006 y 2014, de 3,7 a 4,1 millones."),
    dict(id="FR-C037", tipo="hecho_atribuido", id_fuente="F088", ubicacion="Párrafos 1-4",
         texto="Según Reuters, en 1963, después de que el huracán Flora matara el 20 % del rebaño, el gobierno prohibió "
               "sacrificar vacas y vender carne de res sin permiso del Estado; la masa ganadera mejoró hasta 1989 y desde "
               "entonces se estancó en torno al 70 % del nivel de 1963; en abril de 2021 se permitió a los ganaderos disponer "
               "de sus animales tras cumplir las cuotas estatales."),
    dict(id="FR-C038", tipo="hecho_atribuido", id_fuente="F088", ubicacion="Párrafos 7-10",
         texto="Según Reuters, Cuba importaba más del 60 % de los alimentos que consumía, el Estado es dueño del 80 % de la "
               "tierra cultivable, y según el gobierno la economía se contrajo un 11 % en 2020."),
    # ================= Departamento de Estado (cifras de la ONU y la FAO)
    dict(id="FR-C039", tipo="hecho_atribuido", id_fuente="F089", ubicacion="Sección 'Health'",
         texto=f"{DE}, con datos de la ONU, la mortalidad infantil de Cuba en 1957, de 32 por mil nacidos vivos, era la más "
               "baja de América Latina y la decimotercera más baja del mundo, por delante de Francia, Bélgica, Alemania "
               "Occidental, Israel, Japón, Austria, Italia y España."),
    dict(id="FR-C040", tipo="hecho_atribuido", id_fuente="F089", ubicacion="Sección 'Consumption' y tabla 3",
         texto=f"{DE}, con datos de la FAO, el consumo diario de calorías por habitante en Cuba era de 2.730 en 1954-1957, el "
               "tercero de once países latinoamericanos, y de 2.417 en 1995-1997, una caída del 11,5 %; entre finales de los años "
               "cuarenta y 1995 el suministro anual de carne por habitante bajó de 33 a 23 kilos y el de tubérculos de 91 a 56."),
    dict(id="FR-C041", tipo="hecho_atribuido", id_fuente="F089", ubicacion="Secciones 'Summary' y 'Health'",
         texto=f"{DE}, en 1957 Cuba tenía 128 médicos y dentistas por cada 100.000 habitantes, el tercer lugar de América "
               "Latina detrás de Uruguay y Argentina, y en los años cincuenta tenía 58 periódicos diarios."),
    dict(id="FR-C042", tipo="postura", id_fuente="F089", ubicacion="Sección 'Summary and introduction'", actor="gobierno_eeuu",
         texto=f"{DE}, Cuba era en 1958 un país relativamente avanzado para América Latina, y el informe sostiene que desde "
               "entonces, como mucho, mantuvo los niveles de salud y educación que ya tenía, a un costo extraordinario para "
               "el bienestar general de la población."),
    # ================= cruces entre fuentes
    dict(id="FR-C043", tipo="cifra_disputada", id_fuente="F084", ubicacion="Tabla III (F084); sección 'Health' (F089)",
         corroborado_por=["F089"],
         texto="La mortalidad infantil de Cuba en 1957 se da con valores distintos según la fuente: 33,4 por mil nacidos vivos "
               "según Carmelo Mesa-Lago y 32 por mil según el Departamento de Estado de EE. UU.; ambas fuentes coinciden en "
               "que era la más baja de América Latina."),
    dict(id="FR-C044", tipo="hecho", id_fuente="F084", ubicacion="Tabla IV (F084); sección 'Education' (F089)",
         corroborado_por=["F089"],
         texto="Antes de 1959 Cuba ocupaba el cuarto lugar de América Latina en alfabetización y medio siglo después había "
               "subido al segundo."),
]

for p in (REG, Path("validar.py")):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)
if f'"{T}"' not in Path("validar.py").read_text(encoding="utf-8"):
    print("validar.py todavía no tiene la etapa cuba_antes_despues. Corre primero: python agregar_etapas_contexto.py")
    sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
ya = {r["id_fuente"] for r in filas}
if any(fu[0] in ya for fu in FUENTES):
    print("Alguna de las fuentes F084-F089 ya está en el registro. No toco nada.")
    sys.exit(0)

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
