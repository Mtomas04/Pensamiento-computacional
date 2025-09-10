
climas= ["Soleado",	"Nublado",	"Lluvioso",	"Tormenta"	,"Nevado"]

tipo_clima=input("Ingrese estado inicial: ").capitalize()
cantidad_dias= int(input("Ingrese cantidad de días: "))

if tipo_clima not in climas :
    print ("El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado")
elif cantidad_dias<0:
    print ("La cantidad de días debe ser un entero positivo")

for i in climas:           ###Esto no va
    c=2
    