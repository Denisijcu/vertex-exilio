"""
agregar_etapas_contexto.py — Añade al validador (validar.py) las seis etapas del módulo nuevo "Cuba: contexto".

Uso (desde E:\\vertex-exilio):
    python agregar_etapas_contexto.py

Etapas nuevas:
    cuba_antes_despues        economía y sociedad antes y después de 1959 (azúcar, ganado, reforma agraria,
                              indicadores sociales)
    caso_ochoa_narcotrafico   juicio de Ochoa (1989) y acusaciones de narcotráfico
    internacionalismo_militar Angola, Etiopía, guerrillas de Centroamérica
    cuba_venezuela            Fidel y Chávez, Maduro, presencia cubana en Venezuela
    poder_y_riqueza_castro    estimación de Forbes, testimonios (Juan Reinaldo Sánchez), privilegios
    financiamiento_politico   acusaciones de financiación de campañas en la región

Qué hace:
  1. Copia de seguridad de validar.py.
  2. Inserta las seis etapas en el conjunto ETAPAS, justo después de "transversal".
  3. No toca nada más. Si las etapas ya están, no hace nada.
"""
import shutil
import sys
from datetime import datetime
from pathlib import Path

V = Path("validar.py")
ANCLA = '    "transversal",'
NUEVAS = [
    ("cuba_antes_despues", "economía y sociedad antes y después de 1959"),
    ("caso_ochoa_narcotrafico", "juicio de Ochoa (1989) y acusaciones de narcotráfico"),
    ("internacionalismo_militar", "Angola, Etiopía, guerrillas de Centroamérica"),
    ("cuba_venezuela", "Fidel y Chávez, Maduro, presencia cubana en Venezuela"),
    ("poder_y_riqueza_castro", "Forbes, testimonios, privilegios de la dirigencia"),
    ("financiamiento_politico", "acusaciones de financiación de campañas en la región"),
]

if not V.exists():
    print("No encuentro validar.py. ¿Estás en E:\\vertex-exilio? No toco nada.")
    sys.exit(1)

texto = V.read_text(encoding="utf-8")
if all(f'"{e}"' in texto for e, _ in NUEVAS):
    print("Las etapas del módulo 'Cuba: contexto' ya están en validar.py. No toco nada.")
    sys.exit(0)

lineas = texto.splitlines(keepends=True)
idx = [i for i, l in enumerate(lineas) if l.startswith(ANCLA)]
if len(idx) != 1:
    print("No encuentro la línea de 'transversal' dentro de ETAPAS (o aparece más de una vez). No toco nada.")
    sys.exit(1)

marca = datetime.now().strftime("%Y%m%d-%H%M%S")
shutil.copy2(V, V.with_name(f"{V.name}.{marca}.bak"))

bloque = ["    # módulo 'Cuba: contexto'\n"]
for etapa, desc in NUEVAS:
    bloque.append(f'    "{etapa}",'.ljust(32) + f"# {desc}\n")
lineas[idx[0] + 1:idx[0] + 1] = bloque
V.write_text("".join(lineas), encoding="utf-8")

print(f"Añadidas {len(NUEVAS)} etapas a validar.py (copia de seguridad: {V.name}.{marca}.bak):")
for etapa, _ in NUEVAS:
    print(f"  + {etapa}")
