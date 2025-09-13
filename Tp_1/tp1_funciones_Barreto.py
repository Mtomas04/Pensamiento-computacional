import random
climas= ["Soleado",	"Nublado",	"Lluvioso",	"Tormenta"	,"Nevado"]
transiciones = {
    "Soleado": {"Soleado": 0.60, "Nublado": 0.30, "Lluvioso": 0.05, "Tormenta": 0.03, "Nevado": 0.02},
    "Nublado": {"Soleado": 0.40, "Nublado": 0.30, "Lluvioso": 0.20, "Tormenta": 0.05, "Nevado": 0.05},
    "Lluvioso": {"Soleado": 0.10, "Nublado": 0.30, "Lluvioso": 0.40, "Tormenta": 0.15, "Nevado": 0.05},
    "Tormenta": {"Soleado": 0.05, "Nublado": 0.10, "Lluvioso": 0.30, "Tormenta": 0.50, "Nevado": 0.05},
    "Nevado":  {"Soleado": 0.05, "Nublado": 0.20, "Lluvioso": 0.20, "Tormenta": 0.10, "Nevado": 0.45}
}

def siguiente_clima(actual):
    ''''''
    opciones = list(transiciones[actual].keys())
    probabilidades = list(transiciones[actual].values())
    return random.choices(opciones, probabilidades)[0]


def simular_dias(estado_inicial, cantidad):
    """
    Simula el clima durante una cantidad de días a partir del estado inicial.
    Retorna una lista con los climas día por día.
    """
    resultado = [estado_inicial]
    actual = estado_inicial
    for _ in range(cantidad):
        actual = siguiente_clima(actual)
        resultado.append(actual)
    return resultado    

def contar_climas(simulacion):
    """
    Cuenta cuántos días hubo de cada tipo de clima en la simulación.
    Retorna un diccionario donde clima es la key y conteo el value.
    """
    conteo = {clima: 0 for clima in climas}
    for estado in simulacion:
        conteo[estado] += 1
    return conteo

def clima_mas_frecuente(conteo):
    """
    Devuelve el clima con mayor cantidad de días.
    """
    return max(conteo, key=conteo.get)

def porcentaje_climas(conteo, total_dias):
    """
    Calcula el porcentaje de aparición de cada clima.
    Retorna un diccionario {clima: porcentaje}.
    """
    return {clima:(conteo[clima]/total_dias)*100 for clima in conteo}