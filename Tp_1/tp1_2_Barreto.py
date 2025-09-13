from tp1_funciones_Barreto import climas,simular_dias, contar_climas, clima_mas_frecuente

estado_inicial = "Soleado"
dias_a_simular = 500

simulacion= simular_dias(estado_inicial, dias_a_simular)
conteo= contar_climas(simulacion)
total_dias=len(simulacion)
porcentajes = contar_climas(simulacion)

mas_frecuente = clima_mas_frecuente(conteo)

for clima, cantidad in conteo.items():

    print(f"Días {clima.lower()}s: {cantidad} ({porcentajes[clima]:.2f}%)")

print(f"\nEl clima más frecuente fue: {mas_frecuente}")
