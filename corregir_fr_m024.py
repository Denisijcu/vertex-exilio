"""
corregir_fr_m024.py — Corrige el fragmento FR-M024 y los ejemplos que lo usan.

Uso (desde E:\\vertex-exilio):
    python corregir_fr_m024.py

El error: FR-M024 decía que "un acuerdo de ese año (2016) permitió deportar" a los delincuentes
graves. National Archives (F001) no dice eso: dice que en junio de 2016 había 478 marielitos que no
podían ser admitidos bajo la ley migratoria y que Estados Unidos PLANEABA deportar, de acuerdo con
el gobierno cubano, a un número pequeño de ellos.

Qué hace:
  1. Copia de seguridad (.bak) de cada archivo que va a tocar.
  2. Corrige el texto de FR-M024, guarda el anterior en 'texto_original' y lo deja 'pendiente'.
  3. En cada ejemplo que usa FR-M024: corrige la respuesta, actualiza el fragmento citado y lo deja
     'pendiente' para que lo revises otra vez.
  4. Corrige también los generadores, para que no reintroduzcan el error.
Es todo o nada: si alguna sustitución no encaja, no escribe nada.
"""
import json
import shutil
import sys
from pathlib import Path

FRAG = Path("fuentes/fragmentos_mariel.jsonl")
DATOS = [Path("datos/borrador_mariel.jsonl"), Path("datos/borrador_mariel_lote2.jsonl"),
         Path("datos/borrador_mariel_lote3.jsonl")]
GENERADORES = [Path("generar_piloto_mariel.py"), Path("generar_lote2_mariel.py"),
               Path("generar_lote3_mariel.py")]

NUEVO = ("Según National Archives, para junio de 2016 quedaban 478 marielitos que no podían ser admitidos "
         "bajo la ley migratoria estadounidense, y Estados Unidos planeaba deportar, de acuerdo con el "
         "gobierno cubano, a un número pequeño de ellos considerados delincuentes graves.")

# Sustituciones en las respuestas, en este orden.
SUST = [
    ("con orden de exclusión bajo la ley migratoria estadounidense",
     "que no podían ser admitidos bajo la ley migratoria estadounidense"),
    ("con orden de exclusión",
     "que no podían ser admitidos bajo la ley migratoria estadounidense"),
    (", y un acuerdo de ese año permitió deportar a los considerados delincuentes graves",
     ", y Estados Unidos planeaba deportar, de acuerdo con el gobierno cubano, a un número pequeño "
     "de ellos considerados delincuentes graves"),
]
PROHIBIDO = ["orden de exclusión", "acuerdo de ese año"]
NOTA = "Corrección FR-M024: no hubo 'acuerdo de 2016'; F001 dice que EE. UU. planeaba deportar."


def leer(p):
    with p.open(encoding="utf-8-sig") as f:
        return [json.loads(l) for l in f if l.strip()]


def escribir(p, filas):
    tmp = p.with_suffix(p.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as f:
        for d in filas:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    tmp.replace(p)


def corregir(texto):
    for a, b in SUST:
        texto = texto.replace(a, b)
    return texto


for p in [FRAG] + DATOS + GENERADORES:
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)

# 1. Fragmento
frags = leer(FRAG)
fr = next((d for d in frags if d["id"] == "FR-M024"), None)
if fr is None:
    print("No encuentro FR-M024. No toco nada.")
    sys.exit(1)
if fr["texto"] == NUEVO:
    print("FR-M024 ya estaba corregido. No toco nada.")
    sys.exit(0)
fr.setdefault("texto_original", fr["texto"])
fr["texto"] = NUEVO
fr["estado"] = "pendiente"
fr["revisado"] = False
fr["notas"] = (fr.get("notas", "") + " | " + NOTA).strip(" |")

# 2. Ejemplos
cambios, nuevos_datos = [], {}
for p in DATOS:
    filas = leer(p)
    for d in filas:
        if not any(x["id_fragmento"] == "FR-M024" for x in d.get("fuentes", [])):
            continue
        for m in d["messages"]:
            if m["role"] == "assistant":
                m["content"] = corregir(m["content"])
        resto = [t for t in PROHIBIDO for m in d["messages"] if t in m["content"]]
        if resto:
            print(f"{d['id']}: quedó '{resto[0]}' sin corregir. No toco nada.")
            sys.exit(1)
        for x in d["fuentes"]:
            if x["id_fragmento"] == "FR-M024":
                x["fragmento"] = NUEVO
        d["estado_revision"] = "pendiente"
        d["notas"] = (d.get("notas", "") + " | " + NOTA).strip(" |")
        cambios.append(f"{p.name}: {d['id']}")
    nuevos_datos[p] = filas

# 3. Generadores
nuevos_gen = {}
viejo_frag = fr["texto_original"]
for p in GENERADORES:
    s = p.read_text(encoding="utf-8")
    s2 = corregir(s.replace(viejo_frag, NUEVO))
    if any(t in s2 for t in PROHIBIDO):
        print(f"{p.name}: quedó texto sin corregir. No toco nada.")
        sys.exit(1)
    nuevos_gen[p] = s2

# Escribir todo (con copia de seguridad)
for p in [FRAG] + DATOS + GENERADORES:
    shutil.copy2(p, p.with_suffix(p.suffix + ".bak"))
escribir(FRAG, frags)
for p, filas in nuevos_datos.items():
    escribir(p, filas)
for p, s in nuevos_gen.items():
    p.write_text(s, encoding="utf-8", newline="\n")

print("FR-M024 corregido y en 'pendiente'.")
print(f"Ejemplos devueltos a 'pendiente' ({len(cambios)}):")
for c in cambios:
    print("  " + c)
print("Copias de seguridad: *.bak junto a cada archivo.")
print("Ahora revisa el fragmento y luego los ejemplos con revisar.py.")
