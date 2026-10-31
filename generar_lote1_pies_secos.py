"""
generar_lote1_pies_secos.py — Primer lote de ejemplos de "pies secos, pies mojados" (1995-2017), 16 ejemplos.

Uso (desde E:\\vertex-exilio):
    python generar_lote1_pies_secos.py

Toma el texto EXACTO de cada fragmento desde fuentes/fragmentos_pies_secos.jsonl y se niega a usar
fragmentos que no estén aprobados. No sobrescribe un borrador que ya tenga revisiones.
Escribe datos/borrador_pies_secos_lote1.jsonl con todos los ejemplos en estado 'pendiente'.

El lote enseña a explicar la política y la Ley de Ajuste sin confundirlas, a contar el caso Elián con
las posturas de cada parte, a presentar el debate sobre las devoluciones y sobre la Ley de Ajuste con
quién dice qué, y a dar la versión de los dos gobiernos sobre el fin de la política en 2017.
"""
import json
import sys
from pathlib import Path

ORIGEN = Path("fuentes/fragmentos_pies_secos.jsonl")
DESTINO = Path("datos/borrador_pies_secos_lote1.jsonl")
PREFIJO = "exi-w"
PRIMER_ID = 1

frag = {}
with ORIGEN.open(encoding="utf-8-sig") as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            frag[d["id"]] = d

# Cada ejemplo: (etapa, tipo, [(pregunta, respuesta), ...], [fragmentos])
P = "pies_secos_pies_mojados"
E = [
(P, "hecho", [("¿Qué era la política de pies secos, pies mojados?", """Era la forma en que Estados Unidos trató, hasta 2017, a los cubanos que intentaban llegar sin visa.

La regla dependía de dónde te encontraran. Los cubanos interceptados en el mar eran devueltos a Cuba salvo que alegaran un temor fundado de persecución, y en ese caso se les consideraba para reasentarlos en terceros países. Los que llegaban a tierra eran inspeccionados y en general podían quedarse en Estados Unidos.

Quedarse no era lo mismo que ser admitido formalmente. Según el Servicio de Investigación del Congreso (CRS), a los que llegaban con "pies secos" normalmente se les daba un permiso de entrada temporal (parole) y, al cabo de un año, podían pedir la residencia permanente por la Ley de Ajuste Cubano. Esa ley de 1966 permite a los cubanos que llevan al menos un año en Estados Unidos pedir la residencia sin que los patrocine un familiar o un empleador.

La política terminó el 12 de enero de 2017. Desde ese día, los cubanos que intentaran entrar ilegalmente y no calificaran para protección humanitaria quedaban sujetos a deportación, y el gobierno cubano aceptó recibir a los que tuvieran orden de expulsión.""")],
 ["FR-W001", "FR-W002", "FR-W003", "FR-W049"]),

(P, "hecho", [("¿La Ley de Ajuste Cubano se acabó con pies secos, pies mojados?", """No. Son dos cosas distintas, y la Ley de Ajuste siguió vigente.

La Ley de Ajuste Cubano de 1966 permite a los cubanos que llevan al menos un año en Estados Unidos pedir la residencia permanente sin que los patrocine un familiar o un empleador, una vía que no tiene ninguna otra nacionalidad. Según el CRS, en el año fiscal 2014 unos 40.000 cubanos y sus dependientes obtuvieron la residencia por esa ley.

"Pies secos, pies mojados" era otra cosa: la práctica de devolver a los interceptados en el mar y dejar quedarse a los que llegaban a tierra. Cuando esa práctica terminó en enero de 2017, el Departamento de Seguridad Nacional aclaró que la Ley de Ajuste Cubano y ciertas leyes cubanas seguían vigentes.

Para quitarla haría falta el Congreso o un cambio en Cuba. Una ley de 1996 dispuso que la Ley de Ajuste quedaría derogada solo cuando el presidente de Estados Unidos determine que en Cuba gobierna un gobierno elegido democráticamente. Y según el CRS, en el Congreso de 2015-2016 se presentaron proyectos para derogarla, pero a diciembre de 2016 ninguno se había aprobado.""")],
 ["FR-W003", "FR-W004", "FR-W052", "FR-W005", "FR-W048", "FR-W049"]),

(P, "perspectivas", [("¿La Ley de Ajuste Cubano es justa o es un privilegio?", """Es una de las discusiones más viejas de la emigración cubana, y hay argumentos de varios lados.

Lo que nadie discute es lo que hace la ley: la Ley de Ajuste Cubano de 1966 permite a los cubanos que llevan al menos un año en Estados Unidos pedir la residencia permanente sin que los patrocine un familiar o un empleador, una vía que no tiene ninguna otra nacionalidad.

Según el Servicio de Investigación del Congreso (CRS), algunos críticos en Estados Unidos sostenían que la ley estaba obsoleta y anclada en la Guerra Fría, que era discriminatoria porque daba a los cubanos una ventaja que no tenía ninguna otra nacionalidad, y que funcionaba como un imán para cubanos que de otro modo no podrían entrar.

Según el mismo informe, sus defensores sostenían que derogarla mandaría un mensaje equivocado a los cubanos y que el compromiso de admitir al menos 20.000 cubanos al año dependía de poder ajustar a los beneficiarios del permiso de entrada por esa ley.

El gobierno cubano tiene su propia posición. Según su declaración del 12 de enero de 2017, para normalizar las relaciones migratorias el Congreso de Estados Unidos también debía derogar la Ley de Ajuste Cubano de 1966.

Si es justa o un privilegio depende de cómo se pese cada argumento, y esa valoración le toca a cada quien.""")],
 ["FR-W003", "FR-W043", "FR-W044", "FR-W055", "FR-W049"]),

(P, "contexto", [("¿Por qué tantos cubanos empezaron a llegar por la frontera de México?", """Porque cruzar el estrecho de la Florida dejó de ser la única opción, y llegar por tierra tenía una ventaja.

Según el CRS, muchos cubanos buscaron una ruta distinta: navegaban hasta la península de Yucatán, en México, y seguían por tierra hasta la frontera de Estados Unidos, donde los inspeccionaban aunque no tuvieran documentos y en general los dejaban entrar. Según un diario mexicano citado por el CRS, en 2007 México ya era la ruta principal. Según Wikipedia, a los que llegaban así se les llamaba "pies polvorientos".

En los años más recientes hubo otra ruta. Según Pew Research, muchos volaban a Ecuador, por su política migratoria abierta, y seguían hacia el norte por Centroamérica y México; cuando algunos países centroamericanos cerraron sus fronteras, muchos quedaron varados en el camino.

La mayoría terminaba en Texas. Según Pew, dos tercios (28.371) de los que entraron por tierra en el año fiscal 2015 lo hicieron por el sector de Laredo, y el 64 % en el 2016. Según el CRS, los cubanos sin documentos que se presentaban en puertos de entrada pasaron de 24.277 en el año fiscal 2014 a 46.590 en el 2016, contando este último solo hasta el 31 de julio.""")],
 ["FR-W011", "FR-W012", "FR-W015", "FR-W016", "FR-W013"]),

(P, "hecho", [("¿Por qué aumentó tanto la emigración cubana entre 2014 y 2016?", """Las fuentes coinciden en una causa principal: el miedo a que la puerta se cerrara.

En diciembre de 2014 el presidente Obama anunció un cambio de política para restablecer las relaciones con Cuba. El aumento de las llegadas de cubanos a partir de 2014 se atribuye sobre todo al temor de que Estados Unidos terminara pronto con la política que permitía quedarse a quienes llegaban a su territorio.

Los números subieron rápido. Según Pew Research, 56.406 cubanos entraron por puertos de entrada en el año fiscal 2016, un 31 % más que los 43.159 del 2015, que a su vez habían subido un 78 % frente a los 24.278 del 2014. Por mar pasó lo mismo: según el CRS, las intercepciones casi se cuadruplicaron entre el año fiscal 2013 y el 2016, de 1.357 a 5.213, la cifra más alta de todo el período 1995-2016.

Sobre las intercepciones de 2016 hay una pequeña diferencia: el CRS da 5.213 y Pew Research da 5.263.

El temor tenía fundamento. El 12 de enero de 2017 el gobierno de Obama puso fin a la política de "pies secos, pies mojados".""")],
 ["FR-W018", "FR-W017", "FR-W014", "FR-W009", "FR-W010", "FR-W049"]),

(P, "hecho", [("¿Qué pasó con Elián González?", """Es el caso más conocido de esos años. Empezó con un naufragio y terminó en los tribunales.

Según Wikipedia, el 21 de noviembre de 1999 Elián, de seis años, salió de Cárdenas con su madre y otras doce personas en un bote pequeño de aluminio con el motor defectuoso. Su madre y otras diez personas murieron, y a él lo rescataron dos pescadores cuando flotaba en una cámara de neumático.

A finales de noviembre de 1999 la Guardia Costera lo llevó a Estados Unidos, en vez de a Cuba, junto con otros dos sobrevivientes, y Elián quedó al cuidado de su tío abuelo Lázaro González en Miami.

Cuando su padre llegó a Estados Unidos en abril de 2000 para recuperar la custodia, Lázaro González desobedeció la orden del gobierno de entregar al niño, y la fiscal general Janet Reno ordenó sacarlo de la casa de Miami en la madrugada del 22 de abril de 2000. Según Wikipedia, en el operativo participaron más de 130 agentes del Servicio de Inmigración, y una foto tomada por Alan Diaz, de Associated Press, ganó el premio Pulitzer en 2001.

El 1 de junio de 2000 un tribunal federal de apelaciones rechazó la apelación de los familiares de Miami, el 28 de junio la Corte Suprema dejó en pie esa decisión, y ese mismo día Elián volvió a Cuba con su padre.""")],
 ["FR-W026", "FR-W025", "FR-W029", "FR-W032", "FR-W030"]),

(P, "perspectivas", [("¿Quién tenía razón en el caso Elián?", """Es una pregunta que todavía divide a mucha gente, y lo justo es dar las posiciones de cada parte.

Una parte del exilio en Miami quería que se quedara. Según Wikipedia, Lázaro González, con el respaldo de cubanoamericanos de Miami, sostuvo que el niño debía quedarse en Estados Unidos y no ser devuelto a su padre.

El padre quería que volviera. Según la misma fuente, Juan Miguel González, con el apoyo de las autoridades cubanas, exigió que su hijo fuera devuelto a Cuba. Según Wikipedia, durante la disputa las encuestas mostraron que la mayoría de los estadounidenses creía que Elián debía volver con su padre.

Lo que dijo Elián de adulto también se discute. Según Wikipedia, ha dicho que no se arrepiente de haber vuelto a Cuba, y en 2013 describió su tiempo en Estados Unidos como una etapa muy triste y culpó a la Ley de Ajuste Cubano de haberle negado el derecho a estar con su padre. Su tía Angela González dudó de que una entrevista que dio en 2005 reflejara lo que realmente pensaba, por los controles que el gobierno cubano impone sobre la información.

El caso tuvo peso político en los dos países. Según Wikipedia, en Cuba generó una movilización popular por el regreso del niño, y Fidel Castro lanzó a partir de ella una campaña llamada la Batalla de Ideas.

En lo legal, los tribunales estadounidenses resolvieron el caso: el 1 de junio de 2000 un tribunal federal de apelaciones rechazó la apelación de los familiares de Miami, y el 28 de junio la Corte Suprema dejó en pie esa decisión. El juicio moral sobre el caso sigue dividiendo opiniones.""")],
 ["FR-W027", "FR-W028", "FR-W031", "FR-W035", "FR-W036", "FR-W034", "FR-W030"]),

(P, "perspectivas", [("¿Estaba bien que la Guardia Costera devolviera a los balseros a Cuba?", """Fue una de las partes más discutidas de la política, y las fuentes recogen opiniones opuestas.

La regla era clara: los cubanos interceptados en el mar eran devueltos a Cuba salvo que alegaran un temor fundado de persecución. Algunos casos llegaron a los periódicos. En junio de 1999 la Guardia Costera usó gas pimienta y un cañón de agua para impedir que seis cubanos llegaran a la playa de Surfside, en la Florida. En enero de 2006 encontró a 15 cubanos en un puente viejo de los Cayos que ya no estaba unido a tierra, los consideró "pies mojados" y los devolvió; el CRS fecha el hallazgo el 5 de enero y Wikipedia, el 7. Según Wikipedia, en protesta el activista Ramón Saúl Sánchez hizo una huelga de hambre de once días.

Según el CRS, quienes defendían las devoluciones en Estados Unidos sostenían que eran clave para disuadir la migración ilegal y peligrosa en embarcaciones precarias o sobrecargadas. Los críticos afirmaban que Estados Unidos y Cuba negaban a esas personas su derecho a un proceso justo y a una audiencia, y algunos pedían terminar con la política de intercepción y repatriación.

En algunos casos la devolución se negoció con el gobierno cubano. En julio de 2003, tras interceptar a doce personas que se habían llevado una embarcación y secuestrado a tres vigilantes, Estados Unidos las devolvió cuando el gobierno cubano ofreció condenarlas a 10 años de prisión.""")],
 ["FR-W001", "FR-W024", "FR-W039", "FR-W040", "FR-W041", "FR-W042", "FR-W038"]),

(P, "hecho", [("¿Qué pasó en 2003 con los que secuestraron una lancha en La Habana?", """En 2003 hubo dos casos que muestran lo difícil que se volvió la salida por mar en esos años.

El primero terminó en ejecuciones. El 11 de abril de 2003 el gobierno cubano fusiló a tres hombres que el 2 de abril habían secuestrado una lancha en La Habana para intentar llegar a Estados Unidos, tras juicios sumarios a puerta cerrada. Amnistía Internacional, Human Rights Watch, México, la Unión Europea y la Comunidad del Caribe condenaron las ejecuciones.

El segundo ocurrió en julio de 2003. Doce personas se llevaron una embarcación de una marina cubana y secuestraron a los tres vigilantes. Tras interceptarlos, Estados Unidos los devolvió cuando el gobierno cubano ofreció condenarlos a 10 años de prisión.

Los dos casos ocurrieron bajo la regla de "pies secos, pies mojados": los cubanos interceptados en el mar eran devueltos a Cuba salvo que alegaran un temor fundado de persecución. Según el CRS, quienes defendían esas devoluciones sostenían que eran clave para disuadir la migración ilegal y peligrosa, mientras que los críticos afirmaban que Estados Unidos y Cuba negaban a esas personas su derecho a un proceso justo.""")],
 ["FR-W037", "FR-W038", "FR-W001", "FR-W041", "FR-W042"]),

(P, "perspectivas", [("¿Qué dijeron Washington y La Habana cuando se acabó pies secos, pies mojados?", """Los dos gobiernos anunciaron el cambio el mismo día, el 12 de enero de 2017, pero lo explicaron de forma muy distinta.

Lo que se decidió fue esto: los cubanos que intentaran entrar ilegalmente en Estados Unidos y no calificaran para protección humanitaria quedaban sujetos a deportación, y el gobierno cubano aceptó recibir a los que tuvieran orden de expulsión.

Según su declaración, Obama sostuvo que la política había sido diseñada para otra época y que con el cambio se trataba a los migrantes cubanos igual que a los de otros países.

Según la declaración del gobierno cubano, "pies secos, pies mojados" violaba los acuerdos migratorios firmados entre los dos países en los años noventa, estimulaba la migración irregular y el tráfico de personas, y daba a los cubanos un trato preferente que no recibían los ciudadanos de otros países. La misma declaración sostuvo que, para normalizar las relaciones migratorias, el Congreso de Estados Unidos también debía derogar la Ley de Ajuste Cubano, y recordó que los acuerdos migratorios anteriores seguían vigentes, incluido el compromiso de Estados Unidos de garantizar una migración regular.

Por su parte, el Departamento de Seguridad Nacional aclaró que la Ley de Ajuste Cubano seguía vigente, aunque Cuba pedía derogarla. Es decir, el fin de la política no cerró todas las vías legales.""")],
 ["FR-W049", "FR-W051", "FR-W053", "FR-W055", "FR-W057", "FR-W052"]),

(P, "contexto", [("¿Qué era el programa de parole para médicos cubanos y por qué lo quitaron?", """Era un programa especial de permiso de entrada a Estados Unidos para profesionales cubanos de la salud. Terminó el mismo día que "pies secos, pies mojados".

El 12 de enero de 2017 Estados Unidos terminó el programa de permiso de entrada para profesionales cubanos de la salud (Cuban Medical Professional Parole), junto con el fin de la política que permitía quedarse a los que llegaban a tierra.

Los dos gobiernos lo vieron de forma distinta. Según su declaración de ese día, Obama dijo que el programa contradecía la cooperación sanitaria entre los dos países y que corría el riesgo de perjudicar al pueblo cubano. Según la declaración del gobierno cubano, el programa era un intento de quitarle a Cuba sus profesionales de la salud y un ataque a sus misiones médicas en otros países.

Es decir, por motivos distintos, los dos gobiernos estuvieron de acuerdo en que el programa terminara. Las fuentes de este tema no recogen cuántos médicos usaron el programa ni la opinión de los propios profesionales.""")],
 ["FR-W050", "FR-W051", "FR-W054", "FR-W049"]),

(P, "hecho", [("Aparte de llegar por mar o por la frontera, ¿qué vías legales tenían los cubanos?", """Había varias, aunque ninguna era fácil.

Una era pedir refugio sin salir de la isla. Desde las conversaciones migratorias de 1994-1995, Estados Unidos tramita solicitudes de refugio dentro de Cuba para categorías como antiguos presos políticos, miembros de minorías religiosas perseguidas y activistas de derechos humanos. Ese programa tuvo altibajos: según el CRS, tras los atentados del 11 de septiembre de 2001 en el año fiscal 2003 solo llegaron 305 refugiados cubanos, y en 2004 se aprobaron 5.670 de 8.658 solicitudes, pero solo llegaron 2.980; en esos años también se reportaron problemas para obtener el permiso de salida del gobierno cubano.

El asilo, en cambio, se concedió poco. Según el CRS, el máximo fue de 886 en el año fiscal 1996, y entre 2002 y 2014 cada año lo recibieron menos de 100. Y los interceptados en el mar que demostraban temor de persecución iban a terceros países: de mayo de 1995 a julio de 2003 unos 170 fueron reasentados en 11 países, entre ellos España, Venezuela, Australia y Nicaragua.

Aun así, Cuba siguió siendo un origen importante de inmigrantes. Según el CRS, 49.500 cubanos obtuvieron la residencia permanente en el año fiscal 2008, y Cuba fue el quinto país de origen de nuevos residentes ese año.""")],
 ["FR-W020", "FR-W021", "FR-W022", "FR-W006", "FR-W023"]),

(P, "contexto", [("¿Es verdad que a los cubanos les daban mucho dinero al llegar a Estados Unidos?", """Es una pregunta frecuente, y las fuentes la matizan bastante.

Lo que sí es cierto es que los cubanos tenían un trato especial en la ayuda pública. Leyes de 1980 y de 1996 hicieron que los "entrantes cubanos y haitianos" tuvieran derecho a la misma ayuda de reasentamiento y a ciertos beneficios federales en las mismas condiciones que los refugiados. Además, según el CRS, a los que llegaban con "pies secos" normalmente se les daba un permiso de entrada temporal y podían pedir la residencia al cabo de un año.

Sobre las cantidades, según el CRS había acusaciones de que algunos cubanos usaban la ayuda federal en efectivo para pagar a traficantes, que según la prensa cobraban hasta 15.000 dólares por persona. El mismo informe aclara que esa ayuda se pagaba por meses, durante un máximo de ocho, y en la Florida era de 95 a 180 dólares al mes para una persona sola.

Es decir, había un acceso especial a la ayuda, pero no se trataba de una suma grande entregada de una vez.""")],
 ["FR-W007", "FR-W002", "FR-W047"]),

(P, "humano", [("Mi primo salió de Cuba en 2015 y cruzó media Centroamérica para llegar. ¿Por qué se fue tanta gente justo en ese momento?", """La historia de tu primo es la de miles de cubanos de esos años. Había una razón muy concreta para el apuro.

En diciembre de 2014 el presidente Obama anunció un cambio de política para restablecer las relaciones con Cuba. Mucha gente pensó que, con el acercamiento, se iba a acabar el trato especial a los cubanos. El aumento de las llegadas a partir de 2014 se atribuye sobre todo a ese temor de que Estados Unidos terminara pronto con la política que permitía quedarse a quienes llegaban a su territorio.

La ruta que probablemente hizo tu primo era muy común. Según Pew Research, muchos volaban a Ecuador, por su política migratoria abierta, y seguían hacia el norte por Centroamérica y México; cuando algunos países centroamericanos cerraron sus fronteras, muchos quedaron varados en el camino. Según la misma fuente, 43.159 cubanos entraron por puertos de entrada en el año fiscal 2015, un 78 % más que los 24.278 del 2014.

El temor resultó cierto. El 12 de enero de 2017 el gobierno de Obama puso fin a la política de "pies secos, pies mojados", y desde ese día los cubanos que intentaran entrar ilegalmente quedaban sujetos a deportación. Tu primo llegó antes de ese cambio.""")],
 ["FR-W018", "FR-W017", "FR-W015", "FR-W014", "FR-W049"]),

(P, "perspectivas", [("¿Por qué se suspendieron las conversaciones migratorias entre Cuba y Estados Unidos en 2004?", """Cada gobierno culpó al otro, y las fuentes recogen las dos versiones.

Según el CRS, las conversaciones migratorias se hicieron dos veces al año durante una década, hasta que el Departamento de Estado canceló la ronda de enero de 2004 alegando que Cuba se negaba a discutir cinco temas, entre ellos los permisos de salida y la aceptación de cubanos expulsables.

La versión cubana es otra. Según el mismo informe, funcionarios cubanos calificaron de irresponsable la cancelación y afirmaron que Cuba estaba dispuesta a discutir todos los temas planteados por Estados Unidos. Y según la declaración con la que el gobierno cubano anunció el fin de "pies secos, pies mojados", Cuba había propuesto varias veces un nuevo acuerdo migratorio, y la primera de esas propuestas la rechazó el presidente George W. Bush.

La situación cambió con el acercamiento. En diciembre de 2014 el presidente Obama anunció un cambio de política para restablecer las relaciones con Cuba. Según la declaración cubana, el nuevo acuerdo se alcanzó tras casi un año de negociaciones, después de que los dos países restablecieran sus relaciones diplomáticas.""")],
 ["FR-W045", "FR-W046", "FR-W056", "FR-W018"]),

(P, "contexto", [("¿Cuántos cubanos viven en Estados Unidos hoy?", """La cifra más reciente que tenemos en nuestras fuentes es de 2015, así que conviene tomarla con esa fecha.

Según Pew Research, en 2015 vivían en Estados Unidos unos 2 millones de hispanos de origen cubano. La misma fuente señala un cambio importante: la proporción de nacidos fuera del país bajó del 68 % en 2000 al 57 % en 2015, porque el crecimiento venía ya sobre todo de cubanoamericanos nacidos en Estados Unidos.

En esos años siguieron llegando nuevos inmigrantes. Según el CRS, 49.500 cubanos obtuvieron la residencia permanente en el año fiscal 2008, y en el 2014 unos 40.000 cubanos y sus dependientes la obtuvieron por la Ley de Ajuste Cubano.

Es decir, la comunidad cubana en Estados Unidos es cada vez más una mezcla de quienes llegaron de la isla en distintas épocas y de sus hijos y nietos nacidos allí. Para una cifra actualizada habría que consultar datos más recientes del censo estadounidense.""")],
 ["FR-W019", "FR-W023", "FR-W004"]),
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
              "estado_revision": "pendiente", "revisor": "", "notas": "Pies secos, pies mojados, lote 1"}
        f.write(json.dumps(ej, ensure_ascii=False) + "\n")
print(f"Generados {len(E)} ejemplos en {DESTINO}, usando {len(usados)} fragmentos aprobados.")
print(f"Ahora: python validar.py {DESTINO}")
