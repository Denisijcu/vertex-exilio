"""
actualizar_m015.py — Rehace el ejemplo exi-m015 ("¿Murió gente durante el Mariel?") que Denis
rechazó, incorporando el remolcador "13 de Marzo" (1994) y Hermanos al Rescate (1996).

Uso (desde E:\\vertex-exilio):
    python actualizar_m015.py

- Usa SOLO fragmentos aprobados (de fragmentos_mariel.jsonl y fragmentos_90s.jsonl).
- La versión rechazada no se borra: pasa a datos/rechazados_mariel.jsonl con su motivo.
- La versión nueva entra en datos/borrador_mariel.jsonl como 'pendiente' para que la revises.
"""
import json
import sys
from pathlib import Path

BORRADOR = Path("datos/borrador_mariel.jsonl")
RECHAZADOS = Path("datos/rechazados_mariel.jsonl")
FRAG = [Path("fuentes/fragmentos_mariel.jsonl"), Path("fuentes/fragmentos_90s.jsonl")]

frag = {}
for p in FRAG:
    with p.open(encoding="utf-8-sig") as f:
        for l in f:
            if l.strip():
                d = json.loads(l)
                frag[d["id"]] = d

IDS = ["FR-M015", "FR-M040", "FR-M001", "FR-N001", "FR-N002", "FR-N003", "FR-N004", "FR-N008", "FR-N009", "FR-N011"]
PREGUNTA = "¿Murió gente durante el Mariel?"
RESPUESTA = """Sí, aunque en las fuentes que hemos revisado no hay una cifra total confiable de muertos durante todo el éxodo, así que conviene hablar de los casos documentados y no inventar un número.

El episodio más grave registrado ocurrió en el mar. El 17 de mayo de 1980 se hundió al norte de Mariel la embarcación Olo Yumi, que iba sobrecargada con 52 personas. Murieron 14, y la Guardia Costera rescató a 38. Otras travesías estuvieron cerca de terminar igual: José Manuel García, que salió de niño, contó que el primer barco de su familia empezó a hacer agua y que los rescató un camaronero con unas 200 personas hacinadas.

Antes incluso de que empezara el éxodo hubo una muerte que marcó el comienzo de todo. El 1 de abril de 1980, cuando seis cubanos entraron a la fuerza en un autobús en la embajada del Perú, murió el guardia cubano Pedro Ortiz Cabrera, alcanzado por una bala de rebote.

El Mariel, sin embargo, no fue la tragedia más grave del exilio en el mar. Para entender la historia completa hay que conocer dos casos posteriores, de otra etapa del exilio.

El 13 de julio de 1994 se hundió frente a La Habana el remolcador '13 de Marzo', en el que un grupo de cubanos intentaba llegar a Estados Unidos. Las cifras de muertos varían: 41 según la Comisión Interamericana de Derechos Humanos, al menos 35 según Amnistía Internacional y 32 según el gobierno cubano; sobrevivieron 31. Según contaron los sobrevivientes, embarcaciones de una empresa estatal les lanzaron agua a presión y los embistieron hasta hundirlos. Según el gobierno cubano, fue un accidente.

Y el 24 de febrero de 1996, cazas MiG de la Fuerza Aérea cubana derribaron dos avionetas desarmadas de Hermanos al Rescate, una organización del exilio con base en Miami, y murieron sus cuatro ocupantes. Según la investigación de la Organización de Aviación Civil Internacional, lo más probable es que ocurriera sobre aguas internacionales; según el gobierno cubano, las avionetas violaron su espacio aéreo y fueron advertidas.

Del Mariel en sí, lo más honesto es decir que no tenemos documentada aquí una cifra total de muertos; habría que buscarla en los registros de la Guardia Costera de Estados Unidos antes de darla por buena."""

faltan = [x for x in IDS if x not in frag]
no_aprob = [x for x in IDS if x in frag and frag[x].get("estado") != "aprobado"]
if faltan or no_aprob:
    print(f"No hago nada. Fragmentos que no existen: {faltan}. Sin aprobar: {no_aprob}.")
    sys.exit(1)

with BORRADOR.open(encoding="utf-8-sig") as f:
    ejemplos = [json.loads(l) for l in f if l.strip()]
pos = next((i for i, e in enumerate(ejemplos) if e["id"] == "exi-m015"), None)
if pos is None:
    print("No encuentro exi-m015 en el borrador.")
    sys.exit(1)
viejo = ejemplos[pos]
if viejo.get("estado_revision") != "rechazado":
    print(f"exi-m015 está '{viejo.get('estado_revision')}', no rechazado. No lo toco.")
    sys.exit(1)

viejo["id"] = "exi-m015-v1"
with RECHAZADOS.open("a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(viejo, ensure_ascii=False) + "\n")

ejemplos[pos] = {
    "id": "exi-m015", "etapa": "mariel_1980", "tipo": "hecho",
    "messages": [{"role": "user", "content": PREGUNTA}, {"role": "assistant", "content": RESPUESTA.strip()}],
    "fuentes": [{"id_fragmento": x, "id_fuente": frag[x]["id_fuente"], "fragmento": frag[x]["texto"]} for x in IDS],
    "estado_revision": "pendiente", "revisor": "",
    "notas": "v2: incorpora el remolcador '13 de Marzo' (1994) y Hermanos al Rescate (1996), separados del Mariel por fecha, a pedido de Denis. La v1 está en datos/rechazados_mariel.jsonl.",
}
with BORRADOR.open("w", encoding="utf-8", newline="\n") as f:
    for e in ejemplos:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
print("exi-m015 rehecho (v2, pendiente). La v1 rechazada está en", RECHAZADOS)
print("Ahora: python validar.py datos\\borrador_mariel.jsonl  y  python revisar.py datos\\borrador_mariel.jsonl")
