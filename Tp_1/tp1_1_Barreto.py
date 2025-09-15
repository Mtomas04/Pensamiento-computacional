from tp1_funciones_Barreto import siguiente_clima , climas

clima_actual=input("Ingrese estado inicial: ").capitalize()
cantidad_dias= int(input("Ingrese cantidad de días: "))

if clima_actual not in climas :
    print ("El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado")
elif cantidad_dias<0:
    print ("La cantidad de días debe ser un entero positivo")
else:
    for dia in range(cantidad_dias + 1):
        print(f"Día {dia}: {clima_actual}")
        clima_actual = siguiente_clima(clima_actual)

  