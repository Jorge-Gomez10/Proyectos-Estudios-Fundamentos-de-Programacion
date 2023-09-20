def temperaturas_promedio(datos_temperaturas):
    promedios_ciudades = {}

    for ciudad, semanas in datos_temperaturas.items():
        promedio_ciudad = calcular_temperatura_promedio(semanas)
        promedios_ciudades[ciudad] = promedio_ciudad

    return promedios_ciudades

def calcular_temperatura_promedio(semanas):
    if not semanas:
        return None  # Devuelve None si no hay datos para calcular el promedio

    suma_total = 0
    total_dias = 0

    for semana in semanas:
        for temperatura in semana:
            suma_total += temperatura
            total_dias += 1

    if total_dias == 0:
        return None  # Evitar la división por cero si no hay datos de temperatura

    promedio = suma_total / total_dias
    return promedio

datos_temperaturas = {
    "New York": [
        [22, 25, 26, 24, 23],  # Semana 1
        [25, 30, 22, 27, 24],  # Semana 2
        [30, 25, 24, 29, 26],  # Semana 3
        [29, 27, 22, 25, 26]   # Semana 4
    ],
    "Los Angeles": [
        [28, 30, 29, 31, 27],  # Semana 1
        [30, 27, 23, 24, 29],  # Semana 2
        [26, 29, 25, 31, 29],  # Semana 3
        [24, 29, 24, 27, 30]   # Semana 4
    ],
    "Chicago": [
        [21, 20, 22, 18, 19],  # Semana 1
        [24, 31, 26, 29, 28],  # Semana 2
        [30, 31, 28, 26, 30],  # Semana 3
        [26, 31, 27, 29, 30]   # Semana 4
    ]
}

promedios_ciudades = temperaturas_promedio(datos_temperaturas)

for ciudad, promedio in promedios_ciudades.items():
    if promedio is not None:
        print(f"La temperatura promedio en {ciudad} es: {promedio:.2f} ºC")
    else:
        print(f"No hay datos de temperatura para calcular el promedio en {ciudad}.")

