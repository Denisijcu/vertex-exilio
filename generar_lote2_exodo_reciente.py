"""
generar_lote2_exodo_reciente.py — Segundo lote (corto) de ejemplos del éxodo reciente (2021 en adelante).

Uso (desde E:\\vertex-exilio):
    python generar_lote2_exodo_reciente.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_exodo_reciente.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_exodo_reciente_lote2.jsonl con todos los ejemplos en estado 'pendiente'.

No hay fragmentos nuevos: tres preguntas que el lote 1 no cubría con fragmentos ya aprobados. El ejemplo
del parole advierte que las fuentes llegan a marzo de 2025 y que la situación legal puede haber cambiado.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_exodo_reciente.jsonl")
DESTINO = Path("datos/borrador_exodo_reciente_lote2.jsonl")
PREFIJO = "exi-r"
PRIMER_ID = 18

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

R = "exodo_reciente"

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
E = [
(R, "reformulacion", [("Dicen que de Cuba se está yendo sobre todo la gente joven. ¿Es verdad?", """En buena parte sí, aunque conviene distinguir entre los que se van ahora y los cubanos que ya viven fuera desde hace años.

Sobre la emigración reciente, según Wikipedia, los demógrafos Juan Carlos Albizu-Campos y Sergio Díaz-Briquets calculan que cerca del 80 % de los que emigraron en 2022 tenía entre 15 y 59 años, y economistas y sociólogos cubanos advierten que se están yendo sobre todo jóvenes, estudiantes y profesionales.

Hay datos que apuntan en la misma dirección. Según WOLA, cifras del gobierno cubano indican que el país perdió el 9 % de sus profesionales de la salud entre 2021 y 2022, y que las escuelas tenían falta de maestros.

El panorama cambia si se mira a todos los inmigrantes cubanos en Estados Unidos, no solo a los recién llegados. Según el Migration Policy Institute, en 2021 su edad mediana era de 55 años. Esa cifra incluye a todos los inmigrantes cubanos que viven allí, también a los que llegaron hace décadas, así que no sirve para describir a los que se van ahora.

Cuánto ha perdido Cuba en total tampoco está claro. Las estimaciones no coinciden: WOLA calcula más del 4 % de la población, y Wikipedia da en un lugar casi el 8 % y en otro el 3,5 %.

Así que la frase es bastante cierta para la ola de 2021 en adelante, pero no describe a toda la diáspora cubana.""")],
 ["FR-R007", "FR-R053", "FR-R056", "FR-R006"]),

(R, "reformulacion", [("Leí que esta emigración es más grande que el Mariel y la crisis de los balseros. ¿Es así?", """Según las fuentes que tenemos, sí, y no por poco.

Desde 2020-2021 la salida irregular de cubanos hacia Estados Unidos creció tanto que se considera la mayor emigración en la historia moderna de Cuba. En el año fiscal 2022 las autoridades de Estados Unidos registraron casi 225.000 encuentros con cubanos en la frontera con México y más de 6.000 intercepciones de cubanos en el mar, cifras que juntas superan las del Mariel en 1980 y la crisis de los balseros de 1994.

Y eso es solo un año. Según WOLA, casi 425.000 cubanos llegaron a Estados Unidos en los años fiscales 2022 y 2023, y otros 36.000 pidieron asilo en México entre enero de 2022 y noviembre de 2023, sin contar a los que se fueron a Brasil, Rusia, Uruguay y otros países.

La diferencia principal es la ruta: esta vez la mayoría llegó por tierra y aire. Según WOLA, las 13.000 intercepciones y encuentros de cubanos en el mar en los años fiscales 2022 y 2023 son la mayor ola por mar desde la crisis de los balseros de 1994, aunque mucho menor que la llegada por tierra y aire.

Las cifras exactas varían según la fuente y la forma de contar, pero todas las que tenemos colocan esta ola por encima de las anteriores.""")],
 ["FR-R001", "FR-R002", "FR-R003", "FR-R021"]),

(R, "humano", [("Mi prima llegó con el parole humanitario en 2023 y ahora le dicen que se terminó. ¿Qué pasó con ese programa?", """Entiendo la preocupación. Te cuento lo que dicen las fuentes oficiales que tenemos, con una advertencia importante al final.

El programa empezó en enero de 2023. El Departamento de Seguridad Nacional abrió un programa de permiso humanitario (parole) para cubanos, haitianos y nicaragüenses, que se sumó al de venezolanos de octubre de 2022; el de cubanos empezó el 6 de enero de 2023. Según el Migration Policy Institute, permitía venir en avión a quienes tuvieran un patrocinador en Estados Unidos y vivir allí dos años.

El fin se anunció en dos pasos. Según el Registro Federal, el 4 de octubre de 2024, todavía bajo el gobierno de Biden, ya se había anunciado que no habría renovación del permiso al terminar los dos años iniciales. Después, el Departamento de Seguridad Nacional dio por terminados los programas el 25 de marzo de 2025, y los permisos que no hubieran vencido terminaban el 24 de abril de 2025, salvo decisión individual en contra.

El gobierno de Trump explicó su decisión: según el Registro Federal, sostuvo que esos programas no lograron una mejora suficiente y duradera de la seguridad fronteriza y que dejaron dentro del país a una población grande sin una vía clara hacia un estatus estable.

La advertencia: nuestras fuentes llegan a marzo de 2025, y la situación legal de cada persona puede depender de si pidió asilo u otra vía, y de cambios posteriores. No soy abogado; lo más útil para tu prima es consultar con un abogado de inmigración o una organización de ayuda legal reconocida antes de tomar decisiones.""")],
 ["FR-R024", "FR-R025", "FR-R034", "FR-R033", "FR-R035"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "exodo reciente lote 2"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
