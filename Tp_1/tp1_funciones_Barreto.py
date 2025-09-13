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
    opciones = list(transiciones[actual].keys())
    probabilidades = list(transiciones[actual].values())
    return random.choices(opciones, probabilidades)[0]


    

