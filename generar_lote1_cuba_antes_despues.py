"""
generar_lote1_cuba_antes_despues.py — Primer lote de ejemplos de la etapa cuba_antes_despues (módulo "Cuba: contexto"):
balance general, azúcar, ganado, salud, educación, empleo, dependencia exterior y el debate embargo / política económica.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_cuba_antes_despues.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_cuba_antes_despues.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_cuba_antes_despues_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

Nota: falta la postura oficial cubana con fuente propia sobre los logros sociales; estos ejemplos no la inventan.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_cuba_antes_despues.jsonl")
DESTINO = Path("datos/borrador_cuba_antes_despues_lote1.jsonl")
PREFIJO = "exi-ad"
PRIMER_ID = 1
NOTA = "cuba_antes_despues lote 1"

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "cuba_antes_despues"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "perspectivas", [("¿Cuba estaba mejor antes o después de 1959?", """Depende de qué se mida, y por eso la pregunta no tiene una respuesta de una sola palabra.

El economista Carmelo Mesa-Lago, de la Universidad de Pittsburgh, comparó 84 indicadores entre 1957-1958 y 2007-2008. Según su estudio, la mayoría de los indicadores económicos empeoró y la mayoría de los sociales mejoró: en la economía interna se deterioró el 66 % y mejoró el 34 %, mientras que en los sociales mejoró el 76 % y empeoró el 24 %.

El punto de partida no era el de un país atrasado, pero tampoco el de un país sin problemas. Según el mismo autor, en vísperas de la Revolución Cuba estaba entre los primeros países de América Latina en PIB por habitante, alfabetización, mortalidad infantil y esperanza de vida; a la vez tenía crecimiento bajo, un sector azucarero estancado, alto desempleo después de la zafra, una gran brecha entre el campo y la ciudad y una fuerte dependencia del azúcar y de Estados Unidos.

El Departamento de Estado de Estados Unidos, en un informe de 1998 revisado en 2002, sostiene que Cuba era en 1958 un país relativamente avanzado para América Latina y que desde entonces, como mucho, mantuvo los niveles de salud y educación que ya tenía, a un costo extraordinario para el bienestar general. Es la postura oficial del gobierno de Estados Unidos.

Mesa-Lago advierte, además, que comparar es difícil: la última cifra prerrevolucionaria de alfabetización es del censo de 1953, casi todos los países de la región progresaron en medio siglo y la población de Cuba creció un 65 %. Por eso mide la posición de Cuba entre 20 países latinoamericanos y presenta su estudio como preliminar.

En resumen, los datos muestran avances sociales reales y un deterioro económico también real. Cuánto pesa cada cosa es una valoración que cada persona hace.""")],
 ["FR-C001", "FR-C002", "FR-C003", "FR-C042", "FR-C005"]),

(T, "hecho", [("¿Qué pasó con la producción de azúcar en Cuba después de la Revolución?", """El azúcar, que había sido el centro de la economía cubana, terminó reducido a una fracción de lo que fue, aunque el camino tuvo subidas y bajadas.

Según el historiador económico Antonio Santamaría García, Cuba produjo 5,614 millones de toneladas en 1958, el 12,63 % de la producción mundial; 6,875 millones en 1961; 3,882 millones en 1963, la peor cosecha del período, y 8,537 millones en 1970. Ese año el gobierno se había propuesto 10 millones de toneladas y se lograron unos 8,5 millones.

Según un reportaje de la agencia EFE publicado por OnCuba en 2021, la zafra llegó a 7,4 millones de toneladas en 1980-1981 y a 8,1 millones en 1988-1989. Cinco años después de la desaparición de la URSS cayó a 4,3 millones. En 2002 Fidel Castro anunció el cierre del 70 % de los centrales, con lo que se redujo a la mitad la capacidad de producción, y en 2010 hubo la peor zafra en 105 años, con apenas un millón de toneladas.

El economista Carmelo Mesa-Lago resume la caída de medio siglo: la producción de azúcar cayó un 88 % entre 1958 y 2008, de 8 a 1,2 millones de toneladas, y el azúcar pasó del 81 % al 5 % de las exportaciones. Hay que notar que las cifras de partida no coinciden: Santamaría da 5,614 millones para 1958 y Mesa-Lago habla de 8 millones; las fuentes que tenemos no explican la diferencia.

Para 2021, según EFE, de los 156 centrales que operaban antes de 1959 quedaban 56, y solo 38 molían en la zafra 2020-2021, que no alcanzaría la meta de 1,2 millones de toneladas.""")],
 ["FR-C023", "FR-C025", "FR-C031", "FR-C009", "FR-C028"]),

(T, "contexto", [("¿Qué fue la Zafra de los Diez Millones?", """Fue el gran intento del gobierno cubano de apoyar la economía en una cosecha récord de azúcar en 1970, y no alcanzó su meta.

Para entenderla hay que ver lo que pasó antes. Según el historiador económico Antonio Santamaría García, que retoma una periodización del economista Carmelo Mesa-Lago, entre 1959 y 1963 los dirigentes revolucionarios intentaron una estrategia de industrialización contraria al azúcar, y desde 1963 volvieron al azúcar y aplazaron la industria pesada. Santamaría matiza que la vuelta definitiva al azúcar no llegó hasta 1970.

Ese año el gobierno se propuso una zafra de 10 millones de toneladas y se lograron unos 8,5 millones. Santamaría señala que se obtuvo en detrimento de otros sectores y que retrasó la recuperación de la producción hasta después de 1973. Para comparar, según el mismo autor la cosecha de 1963 había sido de 3,882 millones de toneladas, la peor del período.

La apuesta tenía una base económica concreta. Según Santamaría, la URSS pagó por el azúcar cubano un precio estable de 6,1 centavos de dólar por libra desde 1963, mientras el precio mundial bajó a 2,1 en 1965 y estaba en 3,8 en 1970. Esas subvenciones permitieron financiar la política económica de los años sesenta.

La conclusión del autor es que el azúcar sostuvo la economía, pero impidió la diversificación y acentuó la dependencia de un solo producto.""")],
 ["FR-C024", "FR-C025", "FR-C023", "FR-C026"]),

(T, "hecho", [("¿Cómo era la salud en Cuba antes de la Revolución y cómo cambió?", """Cuba ya tenía indicadores de salud buenos para la región antes de la Revolución, y después los mejoró en varios aspectos, aunque con problemas que conviene conocer.

El punto de partida: la mortalidad infantil de 1957 se da con valores distintos según la fuente, 33,4 por mil nacidos vivos según el economista Carmelo Mesa-Lago y 32 por mil según el Departamento de Estado de EE. UU., pero ambas fuentes coinciden en que era la más baja de América Latina. Según el informe del Departamento de Estado, con datos de la ONU, era además la decimotercera más baja del mundo, y en 1957 Cuba tenía 128 médicos y dentistas por cada 100.000 habitantes, el tercer lugar de América Latina.

Lo que cambió: según Mesa-Lago, la Revolución expandió la salud pública gratuita, nacionalizó las instalaciones de cooperativas, mutuales y entidades privadas y prohibió la medicina privada. Los hospitales rurales pasaron de uno a sesenta y dos, la mortalidad infantil bajó a 5,3 por mil y siguió siendo la más baja de la región en 2007, la esperanza de vida subió de 64,0 a 78,3 años y los médicos por cada 10.000 habitantes pasaron de 9,2 a 64,0.

Los problemas: según el mismo autor, entre el 35 % y el 48 % de los médicos trabajaba en el exterior, sobre todo en Venezuela, lo que redujo el acceso a la atención dentro de la isla, y las farmacias estatales carecían de la mayoría de las medicinas básicas. Seis enfermedades se erradicaron, pero otras, como la hepatitis y las venéreas, aumentaron.

En resumen, el sistema partía de una base alta para la región, amplió el acceso y mejoró los indicadores principales, pero, según Mesa-Lago, con carencias de medicinas y de médicos disponibles dentro del país.""")],
 ["FR-C043", "FR-C039", "FR-C041", "FR-C019", "FR-C020"]),

(T, "hecho", [("¿Es verdad que la Revolución alfabetizó a Cuba?", """Es verdad en parte: Cuba ya era de los países más alfabetizados de América Latina antes de la Revolución, y después subió todavía más, sobre todo en el campo.

Antes de 1959 Cuba ocupaba el cuarto lugar de América Latina en alfabetización y medio siglo después había subido al segundo. En eso coinciden el economista Carmelo Mesa-Lago y un informe del Departamento de Estado de EE. UU.

El problema de entonces estaba en las zonas rurales. Según Mesa-Lago, el censo de 1953 daba un analfabetismo del 23,6 % a nivel nacional, pero del 11,6 % en las ciudades y del 41,8 % en el campo; la mayoría de esas desigualdades entre campo y ciudad se redujo notablemente bajo la Revolución.

Según el mismo autor, la Revolución expandió la educación pública gratuita, expropió las escuelas y universidades privadas y prohibió la enseñanza privada. La alfabetización pasó del 76,4 % en 1953 al 97,9 % en 2006, la matrícula secundaria del 29 % al 87 %, y Cuba quedó primera de la región en matrícula secundaria y universitaria.

Mesa-Lago hace una advertencia: la última cifra prerrevolucionaria de alfabetización es del censo de 1953, y casi todos los países de la región progresaron en medio siglo, así que la comparación tiene límites.

En resumen, la idea de que Cuba era un país de analfabetos antes de 1959 no se sostiene con estos datos, pero la expansión de la educación después, sobre todo en el campo, sí fue grande. Al mismo tiempo, toda la enseñanza pasó a manos del Estado.""")],
 ["FR-C044", "FR-C004", "FR-C018", "FR-C005"]),

(T, "humano", [("Mi abuelo siempre dice que antes de Fidel en Cuba había carne y leche para todo el mundo, y que ahora no quedan vacas. ¿Es verdad o es nostalgia?", """Lo que dice tu abuelo tiene bastante base en los números, aunque conviene separar lo que se puede medir de lo que es recuerdo.

Las vacas: según cifras del diario independiente 14ymedio citadas por OnCuba, en 1959 había 5,1 millones de cabezas de ganado vacuno para 6,5 millones de habitantes. Según el Ministerio de la Agricultura, citado por OnCuba en febrero de 2025, un conteo hecho entre marzo de 2024 y enero de 2025 halló 2.914.009 cabezas. El economista Carmelo Mesa-Lago calcula que las cabezas por cada mil habitantes bajaron de 835 en 1957-1958 a 337 en 2007, y que por habitante la producción de carne de res cayó un 66 % y la de leche un 57 %.

Por qué pasó: según Reuters, en 1963, después de que el huracán Flora matara el 20 % del rebaño, el gobierno prohibió sacrificar vacas y vender carne de res sin permiso del Estado. La masa ganadera mejoró hasta 1989 y desde entonces se estancó; en 2021 se permitió a los ganaderos disponer de sus animales tras cumplir las cuotas estatales. Según OnCuba, el diario oficial Granma atribuye la caída a cambios en las tecnologías de crianza, la falta de insumos veterinarios y alimentos, el deterioro de los indicadores productivos y el hurto y sacrificio de animales.

La comida en general: según un informe del Departamento de Estado de EE. UU., con datos de la FAO, el consumo diario de calorías por habitante era de 2.730 en 1954-1957, el tercero de once países latinoamericanos, y de 2.417 en 1995-1997.

Eso sí, son promedios nacionales: no dicen si en el campo se comía igual que en la ciudad. Pero que hoy hay mucho menos ganado que antes de la Revolución está documentado.""")],
 ["FR-C036", "FR-C034", "FR-C010", "FR-C037", "FR-C035", "FR-C040"]),

(T, "perspectivas", [("¿La crisis económica de Cuba es culpa del embargo o del gobierno cubano?", """Es una de las discusiones de fondo sobre Cuba, y cada parte pone el peso en un lado distinto.

La posición del gobierno cubano: según un reportaje de la agencia EFE publicado por OnCuba en 2021, el embargo ha afectado a la industria azucarera con pérdidas de unos 125.000 millones de dólares según estimaciones de La Habana. El vicepresidente primero del grupo estatal Azcuba, José Carlos Santos, dijo que Cuba debe sortear «la persecución financiera» del embargo para importar insumos y piezas.

La posición de un economista académico: según Carmelo Mesa-Lago, la dirigencia cubana culpa al embargo de Estados Unidos de los problemas económicos, pero desde 2002 el grueso de los alimentos importados viene de Estados Unidos. Él sostiene que, sin restar el efecto adverso del embargo, la causa fundamental ha sido la política económica: la colectivización y centralización de casi toda la economía, siete cambios de organización económica y la virtual eliminación del incentivo individual.

Hay datos que ayudan a ver el problema interno. Según Mesa-Lago, de doce productos agrícolas, ocho estaban en 2007 muy por debajo del nivel de 1957; el 19 % de la población activa agrícola generaba solo el 3,9 % del PIB, y en 2008 Cuba importó el 84 % de los alimentos de la canasta básica, con un costo de 2.500 millones de dólares. El mismo reportaje de EFE menciona, además del embargo, la obsolescencia tecnológica, la falta de fertilizantes y combustible y la escasez de financiamiento.

Ninguna de estas fuentes dice que el embargo no tenga efectos. Lo que se discute es cuánto pesa frente a la forma en que se ha manejado la economía dentro de Cuba.""")],
 ["FR-C032", "FR-C014", "FR-C011", "FR-C033"]),

(T, "reformulacion", [("En Cuba casi no hay desempleo, eso es un logro de la Revolución, ¿no?", """La cifra oficial sí es muy baja, pero hay economistas que la ponen en duda, así que conviene mirarla de cerca.

Según el economista Carmelo Mesa-Lago, el desempleo declarado bajó del 16,4 % en 1956-1957 al 1,6 % en 2008, el más bajo de la región. Antes de la Revolución el desempleo sí era un problema serio: según el mismo autor, la Cuba de 1958 tenía alto desempleo que se agudizaba después de la zafra.

Pero Mesa-Lago considera esa tasa oficial «amañada», porque cuenta como ocupados a despedidos en reentrenamiento, estudiantes y cultivadores de traspatio, y cita a economistas cubanos que estiman innecesario entre el 30 % y el 40 % del empleo.

Además, tener trabajo no es lo mismo que vivir de él. Según Mesa-Lago, el salario medio real cayó un 76 % entre 1989 y 2008; las cuotas de la libreta de racionamiento cubrían más o menos una semana de alimentos al mes y el resto había que comprarlo a precios entre noventa y trescientas veces mayores. Raúl Castro reconoció que el salario no alcanzaba para las necesidades mínimas.

Así que es cierto que el desempleo declarado es muy bajo y que antes de la Revolución era alto. Lo que se discute es cuánto refleja esa cifra la realidad y si ese empleo alcanza para vivir.""")],
 ["FR-C016", "FR-C003", "FR-C015"]),

(T, "hecho", [("¿Cuba dejó de depender de Estados Unidos después de la Revolución?", """Dejó de depender de Estados Unidos, pero pasó a depender de otros socios: primero la URSS y después Venezuela.

Antes de 1959, según un reportaje de la agencia EFE publicado por OnCuba en 2021, el azúcar era cerca del 80 % de las exportaciones y su principal mercado era Estados Unidos, con una cuota preferencial. En 1960 Cuba hizo su última exportación de azúcar a Estados Unidos, de 1,9 millones de toneladas; Washington suspendió la cuota, Cuba nacionalizó los centrales, incluidos los de propiedad estadounidense, y la Unión Soviética se comprometió a comprar una parte mayor de la cosecha.

El cambio de comprador no cambió la dependencia del azúcar. Según el historiador económico Antonio Santamaría García, el azúcar fue el 78 % de las exportaciones en 1957 y 1958 y el 77 % en 1970. En 1961 la URSS sustituyó a Estados Unidos como mayor comprador, y en 1970 el 76 % de las exportaciones cubanas iba a la URSS, frente al 77 % que iba a Estados Unidos en 1959.

Según el economista Carmelo Mesa-Lago, la ayuda soviética se estima en 65.000 millones de dólares entre 1960 y 1990, de los cuales solo el 39 % eran préstamos y solo el 0,6 % se pagó. Cuando se acabó, el PIB cayó un 35 % entre 1989 y 1993, en el llamado «Período Especial».

Después llegó Venezuela. Según Mesa-Lago, el comercio con el socio principal fue el 62 % con Estados Unidos en 1958, el 65 % con la URSS en 1989 y el 20 % con Venezuela en 2008, pero la ayuda venezolana se estimó ese año en 9.405 millones de dólares, incluidos 5.650 millones por los servicios de 40.000 profesionales cubanos y 97.000 barriles diarios de crudo y derivados.""")],
 ["FR-C029", "FR-C030", "FR-C027", "FR-C008", "FR-C013"]),

(T, "contexto", [("¿De quién eran los centrales azucareros antes de 1959 y qué pasó con ellos?", """La mayoría eran de dueños cubanos, y la mayor parte de ellos terminó cerrando.

Según un reportaje de la agencia EFE publicado por OnCuba en 2021, a finales de los años cincuenta había en Cuba 161 centrales: 131 eran de cubanos acaudalados y producían el 60 % del azúcar, frente al 37 % de empresarios estadounidenses. El azúcar era cerca del 80 % de las exportaciones y su principal mercado era Estados Unidos, con una cuota preferencial.

Según el mismo reportaje, en 1960 Washington suspendió esa cuota y Cuba nacionalizó los centrales, incluidos los de propiedad estadounidense, mientras la Unión Soviética se comprometía a comprar una parte mayor de la cosecha.

Las décadas siguientes fueron de altibajos y luego de caída. Según EFE, tras la desaparición de la URSS la zafra se desplomó, y en 2002 Fidel Castro anunció el cierre del 70 % de los centrales, con lo que se redujo a la mitad la capacidad de producción y el 60 % de las tierras de caña pasó a otros cultivos.

El resultado se ve en las cifras de 2021: de los 156 centrales que operaban antes de 1959 quedaban 56, y solo 38 molían en la zafra 2020-2021. El mismo reportaje da dos cifras cercanas, 161 centrales a finales de los cincuenta y 156 operativos antes de 1959, sin explicar la diferencia.

En resumen, la industria pasó de manos privadas, sobre todo cubanas, al Estado en 1960, y medio siglo después había perdido la mayor parte de sus fábricas.""")],
 ["FR-C029", "FR-C030", "FR-C031", "FR-C028"]),

(T, "hecho", [("¿Qué tan rica era Cuba en 1958 comparada con el resto de América Latina?", """Estaba entre los países más avanzados de la región, aunque con desigualdades fuertes, y en varias medidas fue perdiendo posiciones después.

Según el economista Carmelo Mesa-Lago, en 1958 el PIB por habitante de Cuba era el tercero de América Latina, detrás de Venezuela y Uruguay, y en 2007 había bajado al noveno, undécimo o duodécimo lugar según el método; medido en pesos corrientes convertidos a dólares cayó un 27 % entre 1958 y 2007. El autor advierte que el gobierno cambió al menos cuatro veces la forma de calcular el producto, y que desde 2003 suma al PIB los servicios sociales gratuitos, lo que lo sobreestima.

La inversión siguió un camino parecido. Según Mesa-Lago, era el 17,6 % del PIB en 1957, la quinta más alta de la región; subió al 25,6 % en 1989 y cayó al 8,2 % en 2007, la menor de los veinte países.

En bienes de consumo la caída de posiciones fue más clara: en automóviles y periódicos por habitante Cuba bajó del quinto y tercer lugar en 1958 al último y decimosexto, y en teléfonos fijos del tercero al decimoctavo.

Pero el promedio no lo dice todo. Según el mismo autor, la Cuba de 1958 tenía crecimiento bajo que beneficiaba sobre todo al capital y a los trabajadores sindicalizados, alto desempleo después de la zafra y una gran brecha entre el campo y la ciudad.

En resumen, Cuba era un país de ingreso relativamente alto para América Latina, con problemas de reparto, y en lo económico quedó por detrás de buena parte de la región en las décadas siguientes.""")],
 ["FR-C006", "FR-C007", "FR-C022", "FR-C003"]),

(T, "humano", [("Mi tía está jubilada en Cuba y dice que la pensión no le alcanza ni para la comida. ¿Siempre fue así?", """Siento lo de tu tía. Lo que ella cuenta coincide con lo que han medido los economistas, aunque la comparación con antes de la Revolución tiene límites.

Lo que mejoró es quién tiene pensión. Según el economista Carmelo Mesa-Lago, la cobertura de pensiones era del 63 % de la población activa en 1958, la segunda de la región, y se estima en un 85 % en 2007, la primera.

Lo que empeoró es cuánto vale. Según el mismo autor, la pensión media real cayó un 62 % entre 1989 y 2008, y el salario medio real cayó un 76 % en el mismo período. Las cuotas de la libreta de racionamiento cubrían más o menos una semana de alimentos al mes, y el resto había que comprarlo a precios entre noventa y trescientas veces mayores. Raúl Castro reconoció que el salario no alcanzaba para las necesidades mínimas.

Parte de esa caída viene de la crisis de los noventa. Según Mesa-Lago, cuando se acabó la ayuda soviética el PIB cayó un 35 % entre 1989 y 1993, en el llamado «Período Especial».

También creció la desigualdad. Según Mesa-Lago, el coeficiente de Gini bajó de 0,550 en 1953 a 0,250 en 1989 y subió a 0,407 en 1999, y esos cálculos ni siquiera incluyen las remesas, que recibían dos tercios de la población.

Sobre si siempre fue así: las fuentes que tenemos no dan el valor real de la pensión en 1958, así que no se puede comparar bien con aquella época. Lo que sí está medido es la caída fuerte desde 1989.""")],
 ["FR-C021", "FR-C015", "FR-C008", "FR-C017"]),
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
