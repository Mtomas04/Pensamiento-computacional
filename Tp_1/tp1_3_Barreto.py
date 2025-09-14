from tp1_funciones_Barreto import simular_dias, analizar_rachas

estado_inicial = "Soleado"
dias_a_simular = 10000

simulacion= simular_dias(estado_inicial, dias_a_simular)

max_racha, clima_max, cant_rachas = analizar_rachas(simulacion)

print(f"Racha más larga: {max_racha} días de {clima_max}")
print(f"Rachas de más de 4 días: {cant_rachas}")