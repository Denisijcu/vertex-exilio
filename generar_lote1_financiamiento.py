"""
generar_lote1_financiamiento.py — Primer lote de ejemplos de la etapa financiamiento_politico (módulo "Cuba:
contexto"): la denuncia de Veja (2005) sobre dólares de Cuba para la campaña de Lula y el documento de Hugo Carvajal
(2025) sobre financiación venezolana de campañas en la región.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_financiamiento.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_financiamiento.jsonl y se niega a usar fragmentos que
no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_financiamiento_lote1.jsonl con todos los ejemplos en estado 'pendiente'.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_financiamiento.jsonl")
DESTINO = Path("datos/borrador_financiamiento_lote1.jsonl")
PREFIJO = "exi-fp"
PRIMER_ID = 1
NOTA = "financiamiento_politico lote 1"

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

T = "financiamiento_politico"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(T, "reformulacion", [("Cuba le pagó la campaña a Lula en 2002, eso se sabe.", """Eso fue lo que denunció una revista brasileña en 2005, pero nunca se probó, y hasta la oposición a Lula admitió que era difícil probarlo.

La denuncia: según Congresso em Foco, que resumió una portada de la revista Veja de octubre de 2005, la campaña de Lula en 2002 habría recibido 3 millones de dólares de Cuba, escondidos en cajas de bebida. Las fuentes eran dos exasesores de Antonio Palocci, Rogério Buratti y Vladimir Poleto, y la revista no logró averiguar cómo habría entrado el dinero al país. Los dos dijeron que conocieron el origen del dinero por otro exasesor, Ralf Barquete, que murió en junio de 2004. Buratti afirmó: «Sei que o dinheiro veio, mas não sei como».

El desmentido: según MercoPress y Agência Brasil, la embajada de Cuba en Brasil calificó la denuncia de «calumnia» y «difamación» y afirmó que Cuba nunca se ha inmiscuido en los asuntos internos de Brasil.

Lo que pasó después: según Congresso em Foco, el senador opositor Álvaro Dias admitió que «as provas são realmente difíceis de serem obtidas». En mayo de 2006 la acusación «ficou pelo caminho»: a diferencia de otras denuncias de la prensa, no sirvió de base para las comisiones parlamentarias ni para el proceso del mensalão.

Así que lo exacto sería decir que en 2005 una revista acusó a Cuba de financiar la campaña de Lula con testimonios de segunda mano, Cuba y el PT lo negaron, y la acusación nunca se probó.""")],
 ["FR-FP001", "FR-FP002", "FR-FP005", "FR-FP009", "FR-FP010"]),

(T, "hecho", [("¿Qué fue el caso de los «dólares de Cuba» en Brasil?", """Fue una denuncia de la revista Veja en 2005 según la cual Cuba habría financiado en secreto la campaña presidencial de Lula de 2002. Nunca se probó.

Según Congresso em Foco, que resumió la portada de Veja, la campaña habría recibido 3 millones de dólares de Cuba escondidos en cajas de bebida. El exasesor de Palocci Vladimir Poleto contó que llevó en avión de Brasilia a Campinas tres cajas, dos de whisky y una de ron Havana Club, y que después supo que había dinero en una de ellas. Según Veja, el dinero habría salido del Partido Comunista de Cuba o del gobierno de Fidel Castro y habría estado en Brasil a cargo del exdiplomático cubano Sérgio Cervantes. Palocci calificó la versión de «fantasiosa». La ley brasileña prohíbe a los partidos recibir dinero del exterior.

Hubo un dato que pareció reforzarla: según Congresso em Foco, el piloto Alécio Fongaro confirmó que voló con Poleto el 31 de julio de 2002 y que Poleto sacó del avión tres cajas de cartón selladas que parecían de bebida, pero dijo: «mas eu não vi o conteúdo». La oposición pidió a la fiscalía federal y al Tribunal Superior Electoral que investigaran.

Pero no llegó a más. Según Congresso em Foco, en mayo de 2006 la acusación «ficou pelo caminho»: no sirvió de base para las comisiones parlamentarias ni para el proceso del mensalão, y la propia oposición admitía la dificultad de probarla.

Es decir, quedó documentado que hubo un vuelo con cajas, pero no qué llevaban ni de dónde salía el dinero, si es que lo había.""")],
 ["FR-FP001", "FR-FP002", "FR-FP003", "FR-FP007", "FR-FP010"]),

(T, "perspectivas", [("¿Era creíble la denuncia de Veja de que Cuba financió a Lula?", """Tenía elementos que la hacían seria y otros que la debilitaban mucho. Conviene ver los dos lados.

Lo que la reforzaba: según Congresso em Foco, el piloto Alécio Fongaro confirmó que voló con Vladimir Poleto el 31 de julio de 2002 y que Poleto sacó del avión tres cajas selladas que parecían de bebida, aunque no vio su contenido. El dueño del avión confirmó que se lo prestó a Antonio Palocci.

Lo que la debilitaba: según el resumen de Congresso em Foco, los dos testigos principales dijeron que conocieron el origen del dinero por otro exasesor que ya había muerto, y uno de ellos, Rogério Buratti, afirmó: «Sei que o dinheiro veio, mas não sei como». Las fechas tampoco coincidieron: la primera denuncia hablaba de agosto y septiembre de 2002, y el dueño del avión corrigió que el vuelo fue el 31 de julio.

La posición del gobierno cubano: según MercoPress y Agência Brasil, la embajada de Cuba calificó la denuncia de «calumnia» y la atribuyó a planes contra Cuba y contra Lula, y a un intento de desviar la atención antes de la visita a Brasil del presidente de Estados Unidos George W. Bush. El exdiplomático cubano señalado como intermediario dijo que Cuba necesitaba dinero y no podía mandarlo.

La posición del PT: según Congresso em Foco y MercoPress, su presidente, Ricardo Berzoini, dijo que Veja no tenía pruebas y anunció una demanda.

Y la de la oposición: el senador Álvaro Dias admitió que las pruebas eran «realmente difíceis de serem obtidas». La denuncia nunca se probó.""")],
 ["FR-FP007", "FR-FP002", "FR-FP008", "FR-FP005", "FR-FP004", "FR-FP006", "FR-FP009"]),

(T, "reformulacion", [("Cuba financió la campaña de Evo Morales.", """En las fuentes que tenemos no hay nada que diga eso. Lo que existe es una acusación contra Venezuela, no contra Cuba.

Según el diario boliviano Correo del Sur, que en octubre de 2025 citó a The Objective, el exjefe de inteligencia venezolano Hugo Carvajal escribió en un documento enviado a un juez federal de Nueva York que «el Gobierno venezolano ha financiado ilegalmente movimientos políticos de izquierda en el mundo durante al menos 15 años», entre ellos las campañas de Evo Morales, Lula da Silva, Gustavo Petro, Cristina Fernández y Pedro Sánchez. La nota no menciona a Cuba ni da montos o pruebas concretas.

Hay que considerar quién lo dice. Según el mismo diario, Carvajal fue detenido en Madrid en 2021, se declaró culpable en Estados Unidos de cuatro delitos de narcotráfico y coopera con las autoridades estadounidenses, y la nota sostiene que hizo esas revelaciones para evitar una posible cadena perpetua. Eso no quiere decir que mienta, pero sí que su testimonio necesita pruebas que lo respalden.

La nota tampoco recoge una respuesta de Evo Morales, por lo que no sabemos qué contestó.

Así que lo exacto sería decir que un narcotraficante confeso acusó al gobierno de Venezuela, no al de Cuba, de financiar la campaña de Evo Morales y de otros líderes, sin que hasta ahora se hayan publicado pruebas concretas.""")],
 ["FR-FP011", "FR-FP012"]),

(T, "humano", [("Vi en redes que Cuba financió a Lula, a Evo, a Petro y a medio continente. Me lo creo, pero quiero saber si hay pruebas.", """Es bueno que preguntes antes de darlo por cierto. En lo que tenemos documentado hay dos cosas distintas que en redes se suelen mezclar.

Lo de Lula y Cuba: en 2005 la revista brasileña Veja acusó a Cuba de haber enviado 3 millones de dólares a la campaña de Lula en 2002, escondidos en cajas de bebida. Según MercoPress y Agência Brasil, la embajada de Cuba lo calificó de «calumnia» y «difamación». Según Congresso em Foco, en mayo de 2006 la acusación «ficou pelo caminho»: no sirvió de base para ninguna comisión parlamentaria, y hasta la oposición admitía que era difícil probarla.

Lo de Evo, Petro y otros: según el diario boliviano Correo del Sur, en octubre de 2025 el exjefe de inteligencia venezolano Hugo Carvajal escribió ante un juez de Nueva York que «el Gobierno venezolano ha financiado ilegalmente movimientos políticos de izquierda en el mundo durante al menos 15 años», entre ellos las campañas de Evo Morales, Lula, Gustavo Petro y otros. La acusación es contra Venezuela, no contra Cuba, y la nota no da montos ni pruebas. Carvajal es un narcotraficante confeso que coopera con la fiscalía estadounidense.

Así que en lo que tenemos no hay pruebas de que Cuba financiara a medio continente. Hay una acusación sobre Lula que nunca se probó y otra, contra Venezuela, que todavía no tiene pruebas públicas. Puede que en el futuro aparezcan, pero hoy lo honesto es decir que son acusaciones.""")],
 ["FR-FP001", "FR-FP005", "FR-FP010", "FR-FP011", "FR-FP012"]),
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
