# Tablas de pruebas

Programa probado: `gale-shapley_ordenado.py`

## Tabla 1. Prueba de ordenamiento de preferencias

| Caso | Entrada | Resultado esperado | Resultado |
|---|---|---|---|
| 1 | `Hospital A: [(Ana, 90), (Luis, 70), (Sofia, 85)]` | `Hospital A: [Ana, Sofia, Luis]` | Correcto |
| 2 | `Hospital B: [(Ana, 80), (Luis, 95), (Sofia, 60)]` | `Hospital B: [Luis, Ana, Sofia]` | Correcto |
| 3 | `Hospital C: [(Ana, 75), (Luis, 65), (Sofia, 100)]` | `Hospital C: [Sofia, Ana, Luis]` | Correcto |
| 4 | `Ana: [(Hospital A, 95), (Hospital B, 80), (Hospital C, 70)]` | `Ana: [Hospital A, Hospital B, Hospital C]` | Correcto |
| 5 | `Luis: [(Hospital A, 60), (Hospital B, 100), (Hospital C, 75)]` | `Luis: [Hospital B, Hospital C, Hospital A]` | Correcto |
| 6 | `Sofia: [(Hospital A, 85), (Hospital B, 65), (Hospital C, 90)]` | `Sofia: [Hospital C, Hospital A, Hospital B]` | Correcto |

## Tabla 2. Prueba principal del programa

| Elemento | Preferencias originales | Preferencias ordenadas |
|---|---|---|
| Hospital A | Ana 90, Luis 70, Sofia 85 | Ana, Sofia, Luis |
| Hospital B | Ana 80, Luis 95, Sofia 60 | Luis, Ana, Sofia |
| Hospital C | Ana 75, Luis 65, Sofia 100 | Sofia, Ana, Luis |
| Ana | Hospital A 95, Hospital B 80, Hospital C 70 | Hospital A, Hospital B, Hospital C |
| Luis | Hospital A 60, Hospital B 100, Hospital C 75 | Hospital B, Hospital C, Hospital A |
| Sofia | Hospital A 85, Hospital B 65, Hospital C 90 | Hospital C, Hospital A, Hospital B |

## Tabla 3. Emparejamiento esperado del caso principal

| Hospital | Alumno asignado | Justificacion |
|---|---|---|
| Hospital A | Ana | Hospital A propone a Ana y Ana lo prefiere sobre los otros hospitales. |
| Hospital B | Luis | Hospital B propone a Luis y Luis lo tiene como primera opcion. |
| Hospital C | Sofia | Hospital C propone a Sofia y Sofia lo tiene como primera opcion. |

Resultado esperado:

```text
Hospital A - Ana
Hospital B - Luis
Hospital C - Sofia
```

## Tabla 4. Casos de prueba adicionales

| Caso | Descripcion | Entrada resumida | Resultado esperado |
|---|---|---|---|
| 1 | Caso minimo | 1 hospital y 1 alumno. Ambos se prefieren entre si. | `Hospital 1 - Alumno 1` |
| 2 | Caso principal | 3 hospitales y 3 alumnos con las preferencias del programa. | `Hospital A - Ana`, `Hospital B - Luis`, `Hospital C - Sofia` |
| 3 | Conflicto por el mismo alumno | H1 y H2 proponen primero a A1, pero A1 prefiere H2. | `H2 - A1`, `H1 - A2` |
| 4 | Rechazo de propuesta | Un alumno ya emparejado rechaza a un hospital que prefiere menos. | El hospital rechazado propone a su siguiente opcion. |
| 5 | Preferencias vacias | Diccionarios de hospitales y alumnos vacios. | `{}` |

## Tabla 5. Prueba de estabilidad

| Pareja final | Revision | Cumple |
|---|---|---|
| Hospital A - Ana | Ana prefiere Hospital A sobre Hospital B y Hospital C. | Si |
| Hospital B - Luis | Luis prefiere Hospital B sobre Hospital A y Hospital C. | Si |
| Hospital C - Sofia | Sofia prefiere Hospital C sobre Hospital A y Hospital B. | Si |

Conclusion: el emparejamiento es estable porque no existe una pareja hospital-alumno que se prefieran mutuamente por encima de sus asignaciones finales.

## Tabla 6. Complejidad esperada

| Parte del programa | Funcion | Complejidad esperada |
|---|---|---|
| Ordenar preferencias | `merge_sort` | `O(n log n)` por lista |
| Ordenar todas las listas | `obtener_nombres` | `O(n^2 log n)` |
| Emparejar hospitales y alumnos | `gale_shapley` | `O(n^2)` |
| Programa completo | Merge Sort + Gale-Shapley | `O(n^2 log n)` |

## Tabla 7. Formato sugerido para mediciones

| Numero de hospitales y alumnos | Operaciones registradas |
|---:|---:|
| 1 | Registrar valor de `times` |
| 10 | Registrar valor de `times` |
| 20 | Registrar valor de `times` |
| 30 | Registrar valor de `times` |
| 40 | Registrar valor de `times` |
| 50 | Registrar valor de `times` |
| 75 | Registrar valor de `times` |
| 100 | Registrar valor de `times` |

Nota: como los datos se generan aleatoriamente, las operaciones pueden cambiar en cada ejecucion. Para obtener una tabla reproducible se puede agregar `random.seed(12)` antes del ciclo de mediciones.

## Tabla 8. Analisis de complejidad en espacio

| Parte del programa | Estructuras utilizadas | Espacio utilizado | Complejidad espacial |
|---|---|---:|---|
| Datos de entrada | Diccionarios `Hospitales` y `alumnos` con listas de preferencias | Se guardan `n` listas con `n` preferencias para hospitales y `n` listas con `n` preferencias para alumnos. | `O(n^2)` |
| Ordenamiento de preferencias | Listas `izquierda`, `derecha` y `resultado` dentro de `merge_sort` y `merge` | Durante el ordenamiento se crean sublistas y listas auxiliares. Para una lista de tamano `n`, el espacio auxiliar principal es proporcional a `n`. | `O(n)` por lista |
| Preferencias ordenadas | Diccionario `preferencias_ordenadas` creado en `obtener_nombres` | Guarda las mismas preferencias, pero solo con nombres y ya ordenadas. Hay `n` listas de tamano `n`. | `O(n^2)` |
| Hospitales libres | Lista `hospitales_libres` | Puede almacenar hasta `n` hospitales. | `O(n)` |
| Siguiente propuesta | Diccionario `siguiente_propuesta` | Guarda una posicion por cada hospital. | `O(n)` |
| Ranking de alumnos | Diccionario `nivel_preferencias` | Guarda, para cada alumno, la posicion de cada hospital en sus preferencias. | `O(n^2)` |
| Emparejamiento | Diccionario `emparejamiento` y diccionario `resultado` | Guardan como maximo `n` parejas. | `O(n)` |
| Programa completo | Preferencias, rankings, listas auxiliares y emparejamientos | Las estructuras dominantes son las matrices de preferencias y el ranking de alumnos. | `O(n^2)` |
