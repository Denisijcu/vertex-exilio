# Pendientes por verificar

Sacado de `compendio_exilio_cubano_1980.md`. El compendio no es una fuente: es una lista de pistas.
Nada de aquí entra al dataset hasta que tenga una fuente en el registro y un fragmento aprobado.

## Estados

| Estado | Significa |
|---|---|
| YA | Ya está en un fragmento aprobado. No hay que hacer nada. |
| PENDIENTE | Dato nuevo. Hay que buscarlo en la fuente indicada. |
| CONTRADICE | Choca con lo que tenemos. Hay que ir a la fuente original y decidir. |
| NO USAR | La redacción del compendio añade intención, lenguaje cargado o convierte una postura en hecho. Se puede verificar el dato, pero nunca copiar esa redacción. |

## Lo que aprendimos al revisarlo

- Convierte afirmaciones atribuidas en hechos ("la Casa Blanca denuncia" pasa a "el régimen introduce forzosamente").
- Añade intenciones que ninguna fuente documenta ("en represalia", "para frenar el impacto mediático", "omitiendo deliberadamente").
- Usa lenguaje cargado de un lado ("régimen", "linchamiento moral", "sensacionalismo").
- Mezcla a cubanos que emigraron antes de 1959, o que nacieron en EE. UU., con los exiliados posteriores.
- Al contrastarlo con National Archives descubrimos un error nuestro en FR-M024 (ver PV-031), ya corregido con `corregir_fr_m024.py`.

---

## Presidio político (etapa `presidio_politico`)

| ID | Afirmación (redacción neutral) | Estado | Dónde verificar |
|---|---|---|---|
| PV-001 | El preso político Onofre Pérez encontró un micrófono oculto en la lámpara de su celda, y los plantados desmontaron otros dispositivos de escucha. | PENDIENTE | F016 (Tania Díaz Castro) para atribuirlo; buscar una segunda fuente |
| PV-002 | Ernesto Díaz Rodríguez sacó dos micrófonos de la prisión; llegaron al Comité Cubano Pro Derechos Humanos (Ricardo Bofill) y a la Comisión de Derechos Humanos de la ONU. | EN PARTE | F019 párr. 74 (FR-P029): presos políticos encontraron 15 micrófonos el 28 de mayo de 1988, según documentos del Comité Cubano Pro Derechos Humanos. No nombra a Díaz Rodríguez ni dice que sacara dos: eso sigue solo en F016 |
| PV-003 | Díaz Rodríguez grabó en secreto una entrevista con Mario Chanes de Armas en el Combinado del Este, transmitida por Radio Martí. | CONTRADICE | El compendio dice agosto de 1988; lo que leímos daba junio de 1988. Releer F016 |
| PV-004 | Mario Chanes de Armas participó en el asalto al Moncada y en la expedición del Granma, y fue condenado a 30 años. | PENDIENTE | Biografía en una enciclopedia + un medio; años de condena con dos fuentes |
| PV-005 | La misión de la ONU visitó Cuba del 16 al 25 de septiembre de 1988 y estuvo integrada por Bulgaria, Colombia, Filipinas, Irlanda, Nigeria y Senegal. | VERIFICADO | F019 párr. 3, 12 y 21 (FR-P021, FR-P022) |
| PV-006 | La misión recibió 1.600 solicitudes de audiencia y realizó 868 entrevistas. | CONTRADICE | F019 párr. 19-20 (FR-P023): fueron unos 1.600 testimonios escritos, no solicitudes de audiencia, y 87 personas escuchadas directamente. La cifra de 868 no aparece en el informe |
| PV-007 | La misión visitó el Combinado del Este, la prisión de mujeres de Occidente, Boniato y Kilo 7. | CONTRADICE | F019 párr. 16-18 y 69 (FR-P024): visitó Villa Marista, Combinado del Este y Cinco y Medio (Pinar del Río). Boniato y la prisión de mujeres solo aparecen en la propuesta del gobierno cubano; Kilo 7, en una declaración del ministro del Interior |
| PV-008 | El informe recoge 137 denuncias de tortura y 7 desaparecidos. | EN PARTE | F019 párr. 69 (FR-P025): 137 denuncias de torturas o tratos crueles recibidas, no casos comprobados. La cifra de 7 desaparecidos no aparece; el párr. 68 recoge denuncias sobre 3 (FR-P028). FR-P014 queda para rechazar |
| PV-009 | Más de 360 personas fueron ejecutadas en los primeros meses de 1959 tras juicios de tribunales revolucionarios, muchas en La Cabaña, entonces bajo el mando de Ernesto Guevara. | PENDIENTE | Cuba Archive (pendiente FR-P015) + una fuente académica. NO USAR "opositores": entre los ejecutados hubo militares y policías del gobierno anterior acusados de crímenes; describir quiénes eran según las fuentes |
| PV-010 | Armando Valladares pasó 22 años preso, fue liberado en 1982 por mediación de Francia y publicó "Contra toda esperanza" en 1985. | PENDIENTE | Dos fuentes para los años y la mediación. Que el libro "motivó" la visita de la ONU es una relación causal: necesita una fuente que lo diga, si no, se omite |
| PV-011 | Huber Matos, comandante rebelde, fue condenado a 20 años. | PENDIENTE | Enciclopedia + F014 si su entrevista está en el catálogo |
| PV-012 | El catálogo del proyecto Botifoll registra 112 piezas y UM News habla de 118 entrevistas. | YA | F014 / F015 |

## Mariel (etapa `mariel_1980`)

| ID | Afirmación | Estado | Dónde verificar |
|---|---|---|---|
| PV-013 | El guardia Pedro Ortiz Cabrera murió por una bala de rebote. | YA | FR-M001. NO USAR "fuego cruzado de los guardias del régimen": quién disparó sigue sin verificar |
| PV-014 | Perú se negó a entregar a quienes habían entrado en la embajada. | VERIFICADO | F006 p. 875 (FR-M052): el embajador Pinto Bazurco Rittler se negó a entregarlos pese a las exigencias cubanas. F007 p. 10: Perú les concedió asilo. Contexto en F007 pp. 5-6 (FR-M049) |
| PV-015 | El 4 de abril se retiró la custodia y en unas 48 horas entraron más de 10.800 personas. | YA, con matiz | FR-M002/M003 (Larzelere: 10.856 en 38 horas). "En represalia" es la interpretación de Guerra (F006 p. 875, FR-M052): solo se usa atribuida a ella |
| PV-016 | Los vuelos a Costa Rica se suspendieron tras 678 evacuados. | YA + nuevo | FR-M005 y FR-M047 (F007 p. 35): Costa Rica anunció la suspensión a petición de Cuba. Que fue "por la publicidad negativa" es interpretación de Larzelere: solo se usa atribuida |
| PV-017 | La marcha del 19 de abril pasó frente a la embajada del Perú. | YA | FR-M035. NO USAR "para hostigar e intimidar" |
| PV-018 | Bob Graham declaró la emergencia el 28 de abril. | CONTRADICE | F007 p. 331 (FR-M048): fue el 26 de abril, y declaró "zonas de desastre" Monroe y Dade y activó la Guardia Nacional. Encaja con el "en una semana" de F001 |
| PV-019 | En el discurso del 1 de mayo, Castro usó la palabra "escoria". | VERIFICADO | F002 (FR-M051): en la traducción FBIS dice "scum" una vez, sobre los que entraron en la embajada. Lo que más repite es "lumpen" (FR-M028) |
| PV-020 | El 6 de mayo se activó la agencia FEMA. | CONTRADICE | F007 cronología p. xxix (FR-M043): la FEMA fue designada el 27 de abril. El 6 de mayo es la declaración federal de emergencia que le dio fondos (FR-M014) |
| PV-021 | El 11 de mayo fue el día de más llegadas. | PENDIENTE | F007 no da un día pico; solo dice que en la segunda semana de mayo llegaban miles al día (p. 274). El 11 de mayo, según F007, aviones cubanos hundieron un patrullero de Bahamas: no confundir. Buscar datos diarios del INS o de la Guardia Costera |
| PV-022 | El programa de cinco puntos del 14 de mayo incluía multas e incautación de barcos. | EN PARTE | F007 cronología p. xxxi: incluía transporte alternativo y la decisión de castigar a quienes desobedecieran. No detalla multas. Las incautaciones empezaron antes, el 28 de abril (FR-M044) |
| PV-023 | La marcha del 17 de mayo se llamó "Marcha de los Cinco Millones". | PENDIENTE | F006 (Guerra). Si el nombre lleva una cifra oficial, es postura |
| PV-024 | La Casa Blanca acusó a Cuba de enviar "criminales endurecidos". | YA, como postura | FR-M017. Además, Guerra (F006 p. 876, FR-M054/M055): menos del 40 % fue recogido por familiares, el resto fue obligado a salir o salió por su cuenta, y al menos 20.000 habían pasado por prisiones cubanas, la mayoría sin delitos violentos. NO USAR "vaciando cárceles de máxima seguridad" |
| PV-025 | El estatus se llamaba "Cuban-Haitian Entrant (Status Pending)". | EN PARTE | F007 dice solo "Cuban-Haitian Entrant" (FR-M018). Motivo: el 20 de mayo la Casa Blanca decidió tratarlos como solicitantes de asilo y no como refugiados (FR-M045). "Status Pending" y lo de las cuotas siguen sin fuente |
| PV-026 | El éxodo terminó oficialmente el 31 de octubre de 1980. | PENDIENTE | F007 solo da el 25 de septiembre (cierre de Mariel); F001, "octubre de 1980". Falta la fecha exacta del acuerdo |
| PV-027 | Granma informó de 1.470 personas en la embajada frente a unas 10.800. | YA | FR-M033. NO USAR "omitiendo deliberadamente" ni "registro definitivo" |
| PV-028 | Fotomurales en la antigua embajada / fotos de calles vacías. | YA | FR-M038, FR-M036. NO USAR "reescribir visualmente". Lo de la confiscación del transporte público necesita fuente |
| PV-029 | En los actos de repudio hubo piedras, huevos y cadenas, y participaron la FMC y la Seguridad del Estado. | PENDIENTE | F006 (Guerra). Tenemos CDR, escuelas y organizaciones de masas (FR-M030); lo demás hay que encontrarlo. NO USAR "linchamiento moral" |
| PV-030 | Muchos antecedentes eran por "peligrosidad social predelictiva", desacato o vagancia. | EN PARTE | Guerra (F006 p. 876, FR-M055): la mayoría no eran delitos violentos, sino resistencia al adoctrinamiento político o mercado negro. "Peligrosidad predelictiva", desacato y vagancia siguen sin fuente |
| PV-031 | Junio de 2016: 478 marielitos no admisibles. Enero de 2017: declaración conjunta, Cuba acepta repatriaciones y termina "pies secos, pies mojados". | CORREGIDO + PENDIENTE | Nuestro FR-M024 decía "un acuerdo de ese año (2016)"; F001 no lo dice. Ya corregido. Lo de enero de 2017 (la cifra de 500 incluida) va a la etapa `pies_secos_pies_mojados`, con el texto de la declaración |
| PV-032 | "Bajo custodia o supervisión de ICE". | PENDIENTE | F001 no lo dice |

## Estadísticas y economía (etapas `transversal` y por ola)

| ID | Afirmación | Estado | Dónde verificar |
|---|---|---|---|
| PV-033 | Cifras por ola: 1959–62 ~248.000; Vuelos de la Libertad ~260.600; Mariel ~124.800; balseros 1994 ~35.000; 1995–2017 ~500.000; 2021 en adelante +514.000. | PENDIENTE | Cada cifra con su fuente (Pew, MPI, CBP, DHS). Ojo: el Mariel aquí es 124.800, nosotros tenemos ~125.000 (F001) y 125.266 (F009) |
| PV-034 | 20.000 visas anuales tras los acuerdos migratorios. | PENDIENTE | Texto de los acuerdos de 1994–1995. "Lotería de visas" es otra cosa (el sorteo); no mezclar |
| PV-035 | Población de origen cubano en EE. UU.: 2,94 millones; 61 % en Florida; 57 % nacidos en Cuba. | PENDIENTE | Censo / ACS más reciente, con año. Las cifras cambian: siempre con fecha |
| PV-036 | Ingreso mediano, 33 % con título universitario, 66 % naturalizados. | PENDIENTE | Pew / ACS, con año |
| PV-037 | Más de 300.000 empresas fundadas por cubanos. | PENDIENTE | Cifra dudosa. Buscar en el Census (Survey of Business Owners). Si no aparece, se descarta |
| PV-038 | Tendencia de voto. | PENDIENTE | Solo como dato de encuesta, con fuente y año (FIU Cuba Poll, Pew). NO USAR "sólidamente republicana" ni "único grupo hispano conservador" sin el dato que lo diga |
| PV-039 | Card (1990), Borjas (bajada de entre 10 y 30 %, media del 20 %), Clemens y Hunt (cambio en la muestra de la CPS). | YA, con matiz | FR-M029. El detalle de la muestra y "discriminación estructural" son interpretación: ir a los artículos originales antes de añadirlos |
| PV-040 | "El INS clasificó a 2.746". | CONTRADICE | Nuestra fuente es "las cifras que recoge Wikipedia". No atribuirlo al INS hasta tener el documento |

## Cultura y deporte (etapa `transversal`)

Regla: antes de usar a cualquiera de estas personas hay que clasificarla con una fuente:

1. **Exilio posterior a 1959**: salió de Cuba después de 1959.
2. **Emigración anterior a 1959**: emigró antes de la revolución.
3. **Nacido en EE. UU.** de familia cubana.

El compendio los mezcla a todos como "aportes del exilio". Eso no es correcto.

| ID | Personas | Estado | Qué verificar |
|---|---|---|---|
| PV-041 | Gloria Estefan, Celia Cruz, Chano Pozo | PENDIENTE | Año de salida de Cuba y categoría (1, 2 o 3) |
| PV-042 | Desi Arnaz, Andy García, Eva Mendes, Cameron Diaz, Ana de Armas | PENDIENTE | Categoría de cada uno; varios no son exiliados |
| PV-043 | Oscar Hijuelos (Pulitzer de Ficción 1990), Reinaldo Arenas, Cristina García | PENDIENTE | Categoría y el dato del Pulitzer ("primer hispano") |
| PV-044 | Esteban Bellán, Minnie Miñoso, Tony Pérez, Orlando Hernández, José Canseco | PENDIENTE | Categoría y logros con fuente (Salón de la Fama, etc.) |
| PV-045 | Yordan Álvarez, Randy Arozarena, Jorge Soler, José Abreu, José Fernández | PENDIENTE | Cómo y cuándo salieron, y premios (MVP de la Serie Mundial 2021, MVP de la Liga Americana 2020) |
| PV-046 | Joel Casamayor, Yordenis Ugás, Guillermo Rigondeaux, Danell Leyva | PENDIENTE | Categoría y medallas o títulos |
| PV-047 | Miami como centro bilingüe y de medios en español. | PENDIENTE | Fuente académica; sin superlativos |

## Otros proyectos de historia oral (etapas `exodo_reciente` / `presidio_politico`)

| ID | Afirmación | Estado | Dónde verificar |
|---|---|---|---|
| PV-048 | Human Rights Oral History Project: Primavera Negra de 2003 (Grupo de los 75), Damas de Blanco. | PENDIENTE | F015 menciona el proyecto; los detalles, en el catálogo de CHC |
| PV-049 | Movimiento San Isidro (2018–2021), en respuesta al Decreto 349. | PENDIENTE | F015 + una fuente sobre el Decreto 349. "Censura estatal" se atribuye |

---

## Orden de trabajo propuesto

1. **F019, el informe de la ONU** (PV-005 a PV-008): un solo documento resuelve cuatro pendientes.
2. **F002 y F007** (PV-018 a PV-026): cierran casi todo lo que queda del Mariel.
3. **Cuba Archive** (PV-009) para el presidio.
4. Las cifras por ola (PV-033 a PV-036) se verifican al abrir cada etapa, no antes.
5. Cultura y deporte (PV-041 a PV-047), con la etapa `transversal`.
