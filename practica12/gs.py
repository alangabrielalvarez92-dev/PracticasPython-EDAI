def gale_shapley(preferencias_hombres, preferencias_mujeres):
    hombres_libres = list(preferencias_hombres.keys())
    parejas = {}  # mujer -> hombre
    siguiente_propuesta = {hombre: 0 for hombre in preferencias_hombres} #inicializa el diccionario

    # Para comparar rápido qué hombre prefiere cada mujer
    ranking_mujeres = {}
    for mujer, lista in preferencias_mujeres.items():
        ranking_mujeres[mujer] = {
            hombre: posicion for posicion, hombre in enumerate(lista)
        }

    while hombres_libres:
        hombre = hombres_libres.pop(0)

        # Mujer mejor posicionada a la que aún no le ha propuesto
        mujer = preferencias_hombres[hombre][siguiente_propuesta[hombre]]
        siguiente_propuesta[hombre] += 1

        # Si la mujer está libre
        if mujer not in parejas:
            parejas[mujer] = hombre

        else:
            hombre_actual = parejas[mujer]

            # Si la mujer prefiere al nuevo hombre
            if ranking_mujeres[mujer][hombre] < ranking_mujeres[mujer][hombre_actual]:
                parejas[mujer] = hombre
                hombres_libres.append(hombre_actual)
            else:
                hombres_libres.append(hombre)

    # Convertir de mujer -> hombre a hombre -> mujer
    resultado = {}
    for mujer, hombre in parejas.items():
        resultado[hombre] = mujer

    return resultado


preferencias_hombres = {
    "A": ["X", "Y", "Z"],
    "B": ["Y", "X", "Z"],
    "C": ["X", "Z", "Y"]
}

preferencias_mujeres = {
    "X": ["B", "A", "C"],
    "Y": ["A", "B", "C"],
    "Z": ["A", "C", "B"]
}

resultado = gale_shapley(preferencias_hombres, preferencias_mujeres)

print("Parejas finales:")
for hombre, mujer in resultado.items():
    print(hombre, "-", mujer)