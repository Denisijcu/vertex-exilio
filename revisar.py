"""
revisar.py — Revisión humana de fragmentos del dataset del Exilio Cubano (vertex-exilio).

Solo librería estándar (Python 3.10+).

Uso (desde E:\\vertex-exilio):
    python revisar.py fuentes\\fragmentos_mariel.jsonl            # solo los pendientes
    python revisar.py fuentes\\fragmentos_mariel.jsonl --todos    # todos, incluso revisados
    python revisar.py fuentes\\fragmentos_mariel.jsonl --desde FR-M020
    python revisar.py datos\\borrador_mariel.jsonl                # también ejemplos de entrenamiento

Teclas:
    a  aprobar                  r  rechazar (pide motivo)
    e  editar el texto          t  cambiar el tipo
    n  añadir una nota          c  añadir fuente que corrobora
    s  saltar (queda pendiente) v  volver al anterior
    q  guardar y salir

Seguridad:
    - Al abrir, guarda una copia: <archivo>.<fecha>.bak
    - Guarda después de cada cambio, de forma atómica (no deja el archivo a medias).
    - Rechazar NO borra: marca el fragmento como rechazado y guarda el motivo.
    - Editar guarda el texto anterior en 'texto_original'.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import sys
import tempfile
import textwrap
from datetime import datetime
from pathlib import Path

TIPOS = ["hecho", "hecho_atribuido", "postura", "cifra_disputada", "testimonio"]
REVISOR = "Denis"
ANCHO = 92

if os.name == "nt":
    os.system("")  # activa los colores ANSI en la consola de Windows
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

B, D, R, G, Y, C, X = "\033[1m", "\033[2m", "\033[31m", "\033[32m", "\033[33m", "\033[36m", "\033[0m"


def cargar_fuentes(ruta: Path) -> dict[str, dict]:
    with ruta.open(encoding="utf-8-sig", newline="") as f:
        return {fila["id_fuente"].strip(): fila for fila in csv.DictReader(f)}


def cargar(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8-sig") as f:
        return [json.loads(l) for l in f if l.strip()]


def guardar(ruta: Path, frags: list[dict]) -> None:
    fd, tmp = tempfile.mkstemp(dir=ruta.parent, prefix=ruta.name, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
        for d in frags:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    os.replace(tmp, ruta)


def envolver(texto: str, sangria: str = "   ") -> str:
    return textwrap.fill(texto, width=ANCHO, initial_indent=sangria, subsequent_indent=sangria)


def describir_fuente(fid: str, fuentes: dict[str, dict]) -> str:
    f = fuentes.get(fid)
    if not f:
        return f"{R}{fid}: NO ESTÁ EN EL REGISTRO{X}"
    color = {"postura": Y, "pendiente": R}.get(f.get("uso", ""), G)
    return (f"{fid} {color}[{f.get('uso')}]{X} {D}({f.get('perspectiva')}){X} {f.get('titulo')}\n"
            f"        {D}{f.get('autor_institucion')} — {f.get('url')}{X}")


def mostrar(fr: dict, fuentes: dict[str, dict], pos: int, total: int) -> None:
    print("\n" + "=" * ANCHO)
    estado = fr.get("estado", "pendiente" if not fr.get("revisado") else "revisado")
    print(f"{B}{fr['id']}{X}  ({pos}/{total})   etapa: {fr.get('etapa')}   "
          f"tipo: {C}{fr.get('tipo')}{X}   estado: {estado}")
    if fr.get("actor"):
        print(f"   actor: {fr['actor']}")
    if fr.get("testigo"):
        print(f"   testigo: {fr['testigo']}")
    print("-" * ANCHO)
    print(B + envolver(fr.get("texto", "")) + X)
    print("-" * ANCHO)
    print(f"Fuente: {describir_fuente(fr.get('id_fuente', ''), fuentes)}   {D}{fr.get('ubicacion', '')}{X}")
    corr = fr.get("corroborado_por", [])
    if corr:
        print("Corroboran:")
        for c in corr:
            print(f"   {describir_fuente(c, fuentes)}")
    else:
        print(f"{Y}Corroboran: ninguna (una sola fuente){X}")
    if fr.get("notas"):
        print(f"Notas:\n{envolver(fr['notas'])}")
    if fr.get("motivo_rechazo"):
        print(f"{R}Motivo de rechazo: {fr['motivo_rechazo']}{X}")
    print(f"\n{D}[a]probar [r]echazar [e]ditar [t]ipo [n]ota [c]orrobora [s]altar [v]olver [q]salir{X}")


def es_ejemplo(d: dict) -> bool:
    return "messages" in d


def mostrar_ejemplo(ej: dict, fuentes: dict[str, dict], pos: int, total: int) -> None:
    print("\n" + "=" * ANCHO)
    print(f"{B}{ej['id']}{X}  ({pos}/{total})   etapa: {ej.get('etapa')}   "
          f"tipo: {C}{ej.get('tipo')}{X}   estado: {ej.get('estado_revision')}")
    for m in ej["messages"]:
        print("-" * ANCHO)
        quien = f"{Y}PREGUNTA{X}" if m["role"] == "user" else f"{G}RESPUESTA{X} ({len(m['content'].split())} palabras)"
        print(quien)
        for parrafo in m["content"].split("\n"):
            print(envolver(parrafo) if parrafo.strip() else "")
    print("-" * ANCHO)
    print("Fragmentos en que se apoya:")
    for f in ej.get("fuentes", []):
        print(f"   {f.get('id_fragmento', '?')} ← {describir_fuente(f.get('id_fuente', ''), fuentes)}")
    if ej.get("notas"):
        print(f"Notas:\n{envolver(ej['notas'])}")
    if ej.get("motivo_rechazo"):
        print(f"{R}Motivo de rechazo: {ej['motivo_rechazo']}{X}")
    print(f"\n{D}[a]probar [r]echazar [n]ota [s]altar [v]olver [q]salir   "
          f"(para editar una respuesta, recházala con el cambio que quieres){X}")


def marcar(fr: dict, estado: str) -> None:
    if es_ejemplo(fr):
        fr["estado_revision"] = estado
        fr["revisor"] = REVISOR
        fr["fecha_revision"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        return
    fr["revisado"] = True
    fr["estado"] = estado
    fr["revisor"] = REVISOR
    fr["fecha_revision"] = datetime.now().strftime("%Y-%m-%d %H:%M")


def pedir(mensaje: str) -> str:
    try:
        return input(mensaje).strip()
    except EOFError:
        return ""


def main() -> int:
    ap = argparse.ArgumentParser(description="Revisión de fragmentos del dataset del exilio cubano")
    ap.add_argument("archivo", type=Path)
    ap.add_argument("--fuentes", type=Path, default=Path("fuentes/registro_fuentes.csv"))
    ap.add_argument("--todos", action="store_true", help="incluir los ya revisados")
    ap.add_argument("--desde", help="empezar en este id (ej. FR-M020)")
    args = ap.parse_args()

    if not args.archivo.exists():
        print(f"No encuentro {args.archivo}")
        return 2
    fuentes = cargar_fuentes(args.fuentes)
    frags = cargar(args.archivo)

    copia = args.archivo.with_name(f"{args.archivo.name}.{datetime.now():%Y%m%d-%H%M%S}.bak")
    shutil.copy2(args.archivo, copia)
    print(f"{D}Copia de seguridad: {copia}{X}")

    def pendiente(d: dict) -> bool:
        if es_ejemplo(d):
            return d.get("estado_revision") == "pendiente"
        # Un fragmento está pendiente si nunca se revisó o si su estado no es final
        # (por ejemplo, porque un script de corrección lo devolvió a 'pendiente').
        return not d.get("revisado") or d.get("estado") not in ("aprobado", "rechazado")

    cola = [i for i, f in enumerate(frags) if args.todos or pendiente(f)]
    if args.desde:
        ids = [frags[i]["id"] for i in cola]
        if args.desde not in ids:
            print(f"{args.desde} no está entre los fragmentos a revisar")
            return 2
        cola = cola[ids.index(args.desde):]
    if not cola:
        print(f"{G}No queda nada pendiente en {args.archivo}. Usa --todos para repasar.{X}")
        return 0

    cambios = {"aprobado": 0, "rechazado": 0, "editado": 0}
    p = 0
    while 0 <= p < len(cola):
        fr = frags[cola[p]]
        if es_ejemplo(fr):
            mostrar_ejemplo(fr, fuentes, p + 1, len(cola))
        else:
            mostrar(fr, fuentes, p + 1, len(cola))
        op = pedir("> ").lower()[:1]
        if es_ejemplo(fr) and op in ("e", "t", "c"):
            print(f"{Y}En ejemplos solo: aprobar, rechazar, nota, saltar, volver, salir.{X}")
            continue

        if op == "a":
            marcar(fr, "aprobado")
            fr.pop("motivo_rechazo", None)
            cambios["aprobado"] += 1
            guardar(args.archivo, frags)
            print(f"{G}Aprobado.{X}")
            p += 1
        elif op == "r":
            motivo = pedir("Motivo del rechazo: ")
            if not motivo:
                print(f"{Y}Hace falta un motivo; no se rechazó.{X}")
                continue
            marcar(fr, "rechazado")
            fr["motivo_rechazo"] = motivo
            cambios["rechazado"] += 1
            guardar(args.archivo, frags)
            print(f"{R}Rechazado.{X}")
            p += 1
        elif op == "e":
            print(f"{D}Escribe el texto nuevo en una sola línea (vacío = cancelar):{X}")
            nuevo = pedir("texto> ")
            if nuevo:
                fr.setdefault("texto_original", fr.get("texto", ""))
                fr["texto"] = nuevo
                cambios["editado"] += 1
                guardar(args.archivo, frags)
                print(f"{G}Texto cambiado. Sigue en este fragmento para aprobarlo.{X}")
        elif op == "t":
            for i, t in enumerate(TIPOS, 1):
                print(f"   {i}. {t}")
            sel = pedir("Tipo nuevo (número): ")
            if sel.isdigit() and 1 <= int(sel) <= len(TIPOS):
                fr["tipo"] = TIPOS[int(sel) - 1]
                if fr["tipo"] == "testimonio" and not fr.get("testigo"):
                    fr["testigo"] = pedir("¿Quién lo contó? (o 'anónimo'): ") or "anónimo"
                if fr["tipo"] == "postura" and not fr.get("actor"):
                    fr["actor"] = pedir("¿De quién es la postura? (ej. gobierno_cubano): ")
                guardar(args.archivo, frags)
                print(f"{G}Tipo cambiado a {fr['tipo']}.{X}")
        elif op == "n":
            nota = pedir("Nota: ")
            if nota:
                fr["notas"] = (fr.get("notas", "") + " | " if fr.get("notas") else "") + f"[{REVISOR}] {nota}"
                guardar(args.archivo, frags)
        elif op == "c":
            fid = pedir("Id de la fuente que lo corrobora (ej. F009): ").upper()
            if fid not in fuentes:
                print(f"{R}{fid} no está en el registro de fuentes.{X}")
            elif fid == fr.get("id_fuente") or fid in fr.get("corroborado_por", []):
                print(f"{Y}{fid} ya está en este fragmento.{X}")
            else:
                fr.setdefault("corroborado_por", []).append(fid)
                guardar(args.archivo, frags)
                print(f"{G}Añadida {fid}.{X}")
        elif op == "s":
            p += 1
        elif op == "v":
            p = max(p - 1, 0)
        elif op == "q":
            break
        else:
            print(f"{Y}Tecla no válida.{X}")

    pendientes = sum(1 for f in frags if pendiente(f))
    print("\n" + "=" * ANCHO)
    print(f"Sesión: {cambios['aprobado']} aprobados, {cambios['rechazado']} rechazados, "
          f"{cambios['editado']} editados. Quedan {pendientes} pendientes en {args.archivo.name}.")
    sufijo = "" if frags and es_ejemplo(frags[0]) else " --fragmentos"
    print(f"Ahora corre: python validar.py {args.archivo}{sufijo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
