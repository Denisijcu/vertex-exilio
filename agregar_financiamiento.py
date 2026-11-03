"""
agregar_financiamiento.py — Etapa financiamiento_politico (módulo "Cuba: contexto").

Registra las fuentes F122-F129 y crea fuentes/fragmentos_financiamiento.jsonl (FR-FP001 en adelante):
la denuncia de la revista Veja (2005) sobre dólares de Cuba para la campaña de Lula en 2002, los desmentidos y lo que
pasó después, y el documento de Hugo Carvajal (2025) sobre financiación VENEZOLANA de Evo Morales, Lula y otros.

Uso (desde E:\\vertex-exilio):
    python agregar_financiamiento.py

Criterios:
  - La denuncia de Veja es una acusación nunca probada: todo atribuido, con desmentidos y con la propia oposición
    admitiendo que era difícil probarla.
  - Sobre Evo Morales no hay fuente seria que hable de dinero de CUBA; lo que hay es una acusación contra
    VENEZUELA hecha por un narcotraficante confeso que coopera con la fiscalía de EE. UU. Va así, sin estirarla.
  - No entran: "régimen", "extrema izquierda" (Correo del Sur), "ingredientes fascistas" ni lenguaje partidista.

Qué hace:
  1. Comprueba que validar.py tiene la etapa financiamiento_politico.
  2. Copia de seguridad del registro (y del archivo de fragmentos si ya existiera).
  3. Añade F122-F129 al registro (si alguna ya existe, no toca nada).
  4. Crea el archivo de fragmentos en estado 'pendiente'.
"""
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

REG = Path("fuentes/registro_fuentes.csv")
FRAG = Path("fuentes/fragmentos_financiamiento.jsonl")
HOY = "2026-11-03"
T = "financiamiento_politico"

VJ = "Según Congresso em Foco, que resumió en octubre de 2005 una portada de la revista brasileña Veja firmada por Policarpo Junior"
CF = "Según Congresso em Foco"

FUENTES = [
    ("F122", "PT recebeu doação de Cuba, diz revista (29 de octubre de 2005)", "Congresso em Foco",
     "https://www.congressoemfoco.com.br/noticia/99401/pt-recebeu-doacao-de-cuba-diz-revista", "periodistica",
     "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/CEF_2005_veja_cuba.html. Resume la denuncia de Veja: acusación, nunca probada."),
    ("F123", "Cuban government replies that accusations in Veja constitute slander and defamation (30 de octubre de 2005)",
     "Nelson Motta, Agência Brasil", "https://memoria.ebc.com.br/agenciabrasil//noticia/2005-10-30/cuban-government-replies-accusations-veja-constitute-slander-and-defamation",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/ABR_2005_respuesta_cuba.html. Agencia pública brasileña. La nota de la embajada cubana: postura."),
    ("F124", "Cuba denies money contribution to Lula's campaign (31 de octubre de 2005)", "MercoPress",
     "https://en.mercopress.com/2005/10/31/cuba-denies-money-contribution-to-lula-s-campaign", "periodistica",
     "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/MERCOPRESS_2005_cuba_niega.html. Desmentido cubano y del PT: postura."),
    ("F125", "Dólares de Cuba: piloto confirma voo (5 de noviembre de 2005)", "Congresso em Foco (con información de Veja)",
     "https://www.congressoemfoco.com.br/noticia/101697/dolares-de-cuba-piloto-confirma-voo", "periodistica",
     "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/CEF_2005_piloto.html. El piloto confirma el vuelo y las cajas, no su contenido."),
    ("F126", "Alvaro Dias admite dificuldade para se comprovar denúncia contra o PT (29 de octubre de 2005)",
     "Congresso em Foco",
     "https://www.congressoemfoco.com.br/noticia/99397/alvaro-dias-admite-dificuldade-para-se-comprovar-denuncia-contra-o-pt",
     "periodistica", "revisar", "ninguna", "ambos", "Archivo fuentes/docs/CEF_2005_alvaro_dias.html."),
    ("F127", "PT vai processar Veja por danos morais (29 de octubre de 2005)", "Congresso em Foco",
     "https://www.congressoemfoco.com.br/noticia/99395/pt-vai-processar-veja-por-danos-morais", "periodistica",
     "revisar", "ninguna", "ambos", "Archivo fuentes/docs/CEF_2005_pt_demanda.html."),
    ("F128", "Em um ano, repertório variado de denúncias (22 de mayo de 2006)", "Congresso em Foco",
     "https://www.congressoemfoco.com.br/noticia/97965/em-um-ano-repertorio-variado-de-denuncias", "periodistica",
     "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/CEF_2006_balance.html. Fecha la denuncia de Veja en 'noviembre'; fue a fines de octubre "
     "de 2005: esa fecha no entra."),
    ("F129", "Evo recibió dinero del chavismo y el narcotráfico venezolano, revela exjefe de inteligencia (18 de octubre de 2025)",
     "Correo del Sur (Bolivia), con información de The Objective e Infobae",
     "https://correodelsur.com/politica/20251018/evo-recibio-dinero-del-chavismo-y-el-narcotrafico-venezolano-revela-exjefe-de-inteligencia.html",
     "periodistica", "revisar", "ninguna", "ambos",
     "Archivo fuentes/docs/CDS_2025_carvajal.html. Acusación de un narcotraficante confeso que coopera con la fiscalía; "
     "no da montos ni pruebas, y no menciona a Cuba. 'Régimen' y 'extrema izquierda' son lenguaje de la nota."),
]

NUEVOS = [
    # ================= la denuncia de Veja (2005)
    dict(id="FR-FP001", tipo="hecho_atribuido", id_fuente="F122", ubicacion="Párrafos 1-3",
         texto=f"{VJ}, la campaña de Lula en 2002 habría recibido 3 millones de dólares de Cuba entre agosto y septiembre de "
               "ese año, escondidos en cajas de bebida; las fuentes eran el abogado Rogério Buratti y el economista Vladimir "
               "Poleto, exasesores de Antonio Palocci en la alcaldía de Ribeirão Preto, y la revista no logró averiguar cómo "
               "habría entrado el dinero al país."),
    dict(id="FR-FP002", tipo="hecho_atribuido", id_fuente="F122", ubicacion="Párrafos 4-6 y 8",
         texto=f"{VJ}, Poleto contó que llevó en avión de Brasilia a Campinas tres cajas, dos de whisky y una de ron Havana Club, "
               "y que después supo que había dinero en una de ellas; él calculaba 1,4 millones de dólares y Buratti 3 "
               "millones; los dos dijeron que conocieron el origen del dinero por otro exasesor de Palocci, Ralf Barquete, "
               "que murió en junio de 2004, y Buratti afirmó: «Sei que o dinheiro veio, mas não sei como»."),
    dict(id="FR-FP003", tipo="hecho_atribuido", id_fuente="F122", ubicacion="Párrafos 3, 6-7 y 11",
         texto=f"{VJ}, el dinero habría salido del Partido Comunista de Cuba o del gobierno de Fidel Castro y habría estado en "
               "Brasil a cargo del exdiplomático cubano Sérgio Cervantes; Poleto dijo que las cajas se entregaron al "
               "tesorero del PT, Delúbio Soares, que lo niega, y Palocci calificó la versión de «fantasiosa»; la ley "
               "brasileña prohíbe a los partidos recibir dinero del exterior."),
    dict(id="FR-FP004", tipo="postura", id_fuente="F122", ubicacion="Párrafo 6", actor="Sérgio Cervantes (exdiplomático cubano)",
         texto=f"{VJ}, el exdiplomático cubano Sérgio Cervantes negó cualquier ayuda financiera a Lula: dijo que Cuba "
               "necesitaba dinero y no podía mandarlo, y que «isso não é verdade»."),
    dict(id="FR-FP005", tipo="postura", id_fuente="F124", ubicacion="Párrafos 1-3 y 8-9", actor="gobierno_cubano",
         corroborado_por=["F123"],
         texto="Según MercoPress y Agência Brasil, la embajada de Cuba en Brasil calificó la denuncia de «calumnia» y "
               "«difamación», afirmó que Cuba nunca se ha inmiscuido en los asuntos internos de Brasil y la atribuyó a "
               "planes del imperialismo contra Cuba y contra Lula, y a un intento de desviar la atención antes de la visita "
               "del presidente George W. Bush a Brasil."),
    dict(id="FR-FP006", tipo="postura", id_fuente="F127", ubicacion="Párrafos 1-2", actor="Partido de los Trabajadores (PT)",
         corroborado_por=["F124"],
         texto=f"{CF} y MercoPress, el presidente del PT, Ricardo Berzoini, negó que Cuba financiara la campaña de 2002, dijo "
               "que Veja no tenía pruebas ni credibilidad y anunció que el partido demandaría a la revista: «Vamos processar "
               "a revista por causar danos à imagem do partido»."),
    dict(id="FR-FP007", tipo="hecho_atribuido", id_fuente="F125", ubicacion="Párrafos 2-6",
         texto=f"{CF} (noviembre de 2005), el piloto Alécio Fongaro confirmó a Veja que voló con Poleto el 31 de julio de 2002 "
               "de Brasilia a Campinas y que Poleto sacó del avión tres cajas de cartón selladas que parecían de bebida, "
               "«mas eu não vi o conteúdo»; el dueño del avión, Roberto Colnaghi, confirmó que se lo prestó a Palocci, y la "
               "oposición pidió a la fiscalía federal y al Tribunal Superior Electoral que investigaran."),
    dict(id="FR-FP008", tipo="cifra_disputada", id_fuente="F122", ubicacion="Párrafo 1 (F122); párrafo 6 (F125)",
         corroborado_por=["F125"],
         texto="La fecha del supuesto traslado del dinero se da de forma distinta: la primera denuncia de Veja hablaba de "
               "agosto y septiembre de 2002, y después el dueño del avión corrigió que el vuelo fue el 31 de julio de 2002."),
    dict(id="FR-FP009", tipo="postura", id_fuente="F126", ubicacion="Párrafos 1-2", actor="Álvaro Dias (senador opositor del PSDB)",
         texto=f"{CF}, el senador opositor Álvaro Dias, del PSDB, admitió que sería difícil probar que el PT recibió dinero de "
               "Cuba, porque el gobierno lo negaría y «as provas são realmente difíceis de serem obtidas»."),
    dict(id="FR-FP010", tipo="hecho_atribuido", id_fuente="F128", ubicacion="Apartado sobre Cuba",
         texto=f"{CF} (mayo de 2006), la acusación de los dólares de Cuba «ficou pelo caminho»: a diferencia de otras denuncias "
               "de la prensa, no sirvió de base para las comisiones parlamentarias de investigación ni para el proceso del "
               "mensalão, y la propia oposición admitía la dificultad de probarla."),
    # ================= el documento de Carvajal (2025)
    dict(id="FR-FP011", tipo="hecho_atribuido", id_fuente="F129", ubicacion="Párrafos 1-4",
         texto="Según el diario boliviano Correo del Sur (octubre de 2025), que cita a The Objective, el exjefe de inteligencia "
               "venezolano Hugo Carvajal escribió en un documento enviado a un juez federal de Nueva York que «el Gobierno "
               "venezolano ha financiado ilegalmente movimientos políticos de izquierda en el mundo durante al menos 15 "
               "años», entre ellos las campañas de Evo Morales, Lula da Silva, Gustavo Petro, Cristina Fernández y Pedro "
               "Sánchez; la nota no menciona a Cuba ni da montos o pruebas concretas."),
    dict(id="FR-FP012", tipo="hecho_atribuido", id_fuente="F129", ubicacion="Párrafos 3 y 5-6",
         texto="Según Correo del Sur, Hugo Carvajal fue detenido en Madrid en 2021, se declaró culpable en Estados Unidos de "
               "cuatro delitos de narcotráfico y coopera con las autoridades estadounidenses, y la nota sostiene que hizo "
               "esas revelaciones para evitar una posible cadena perpetua; su sentencia, prevista para el 29 de octubre de "
               "2025, se pidió aplazar."),
]

for p in (REG, Path("validar.py")):
    if not p.exists():
        print(f"No encuentro {p}. ¿Estás en E:\\vertex-exilio? No toco nada.")
        sys.exit(1)
if f'"{T}"' not in Path("validar.py").read_text(encoding="utf-8"):
    print(f"validar.py no tiene la etapa {T}. Corre primero: python agregar_etapas_contexto.py")
    sys.exit(1)

with REG.open(encoding="utf-8-sig", newline="") as f:
    filas = list(csv.DictReader(f))
    campos = list(filas[0].keys())
ya = {r["id_fuente"] for r in filas}
if any(fu[0] in ya for fu in FUENTES):
    print(f"Alguna de las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]} ya está en el registro. No toco nada.")
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
        if n.get("testigo"):
            d["testigo"] = n["testigo"]
        f.write(json.dumps(d, ensure_ascii=False) + "\n")

print(f"Registradas las fuentes {FUENTES[0][0]}-{FUENTES[-1][0]}.")
print(f"Añadidos {len(NUEVOS)} fragmentos a {FRAG} (en 'pendiente').")
print(f"Ahora: python validar.py {FRAG}")
