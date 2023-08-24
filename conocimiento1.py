""" # Definición de valores por destino
valorPersonaAdultoGuajira = 1450000
valorNinoGuajira = 870000
valorPersonaAdultoChicamocha = 1450000
valorNinoChicamocha = 960000
valorPersonaAdultoLlanos = 1200000
valorNinoLlanos = 720000

# Inicialización de variables
cantidadPersonasGuajira = 0
cantidadPersonasChicamocha = 0
cantidadPersonasLlanos = 0
totalGuajira = 0
totalChicamocha = 0
totalLlanos = 0
totalPersonasAdultas = 0
totalNinos = 0
totalDinero = 0

cantidadClientes = int(input("Ingrese la cantidad de clientes: "))

for cliente in range(cantidadClientes):
    nombreCliente = input("Nombre del cliente: ")
    destino = input("Destino del cliente: ")
    numPersonasAdultas = int(input("Número de personas adultas: "))
    numNinos = int(input("Número de niños: "))

    if destino == "guajira":
        cantidadPersonasGuajira += numPersonasAdultas + numNinos
        totalGuajira += (numPersonasAdultas * valorPersonaAdultoGuajira) + (numNinos * valorNinoGuajira)
    elif destino == "cañon del chicamocha":
        cantidadPersonasChicamocha += numPersonasAdultas + numNinos
        totalChicamocha += (numPersonasAdultas * valorPersonaAdultoChicamocha) + (numNinos * valorNinoChicamocha)
    elif destino == "llanos orientales":
        cantidadPersonasLlanos += numPersonasAdultas + numNinos
        totalLlanos += (numPersonasAdultas * valorPersonaAdultoLlanos) + (numNinos * valorNinoLlanos)
    
    totalPersonasAdultas += numPersonasAdultas
    totalNinos += numNinos
    totalDinero += (numPersonasAdultas * valorPersonaAdulto) + (numNinos * valorNino)

print("Cantidad de personas que viajan para la Guajira:", cantidadPersonasGuajira)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", cantidadPersonasChicamocha)
print("Cantidad de personas que viajan para los llanos orientales:", cantidadPersonasLlanos)
print("Total de dinero de los viajes para la Guajira:", totalGuajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", totalChicamocha)
print("Total de dinero de los viajes para los llanos orientales:", totalLlanos)
print("Total de personas Adultas:", totalPersonasAdultas)
print("Total de niños:", totalNinos)
print("Total de dinero de todos los destinos:", totalDinero)
 """
"""  
#version 2
 # Definición de valores por destino
valorPersonaAdultoGuajira = 1450000
valorNinoGuajira = 870000
valorPersonaAdultoChicamocha = 1450000
valorNinoChicamocha = 960000
valorPersonaAdultoLlanos = 1200000
valorNinoLlanos = 720000

# Inicialización de variables
cantidadPersonasGuajira = 0
cantidadPersonasChicamocha = 0
cantidadPersonasLlanos = 0
totalGuajira = 0
totalChicamocha = 0
totalLlanos = 0
totalPersonasAdultas = 0
totalNinos = 0
totalDinero = 0

cantidadClientes = int(input("Ingrese la cantidad de clientes: "))

for cliente in range(cantidadClientes):
    nombreCliente = input("Nombre del cliente: ")
    destino = input("Destino del cliente: ")
    numPersonasAdultas = int(input("Número de personas adultas: "))
    numNinos = int(input("Número de niños: "))

    if numPersonasAdultas + numNinos > cantidadClientes:
        print("El número de adultos y niños supera el número de clientes.")
        continue

    if destino == "guajira":
        cantidadPersonasGuajira += numPersonasAdultas + numNinos
        totalGuajira += (numPersonasAdultas * valorPersonaAdultoGuajira) + (numNinos * valorNinoGuajira)
    elif destino == "cañon del chicamocha":
        cantidadPersonasChicamocha += numPersonasAdultas + numNinos
        totalChicamocha += (numPersonasAdultas * valorPersonaAdultoChicamocha) + (numNinos * valorNinoChicamocha)
    elif destino == "llanos orientales":
        cantidadPersonasLlanos += numPersonasAdultas + numNinos
        totalLlanos += (numPersonasAdultas * valorPersonaAdultoLlanos) + (numNinos * valorNinoLlanos)
    
    totalPersonasAdultas += numPersonasAdultas
    totalNinos += numNinos
    totalDinero += (numPersonasAdultas * valorPersonaAdulto) + (numNinos * valorNino)

print("Cantidad de personas que viajan para la Guajira:", cantidadPersonasGuajira)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", cantidadPersonasChicamocha)
print("Cantidad de personas que viajan para los llanos orientales:", cantidadPersonasLlanos)
print("Total de dinero de los viajes para la Guajira:", totalGuajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", totalChicamocha)
print("Total de dinero de los viajes para los llanos orientales:", totalLlanos)
print("Total de personas Adultas:", totalPersonasAdultas)
print("Total de niños:", totalNinos)
print("Total de dinero de todos los destinos:", totalDinero)
 """

 # Definición de valores por destino
valorPersonaAdultoGuajira = 1450000
valorNinoGuajira = 870000
valorPersonaAdultoChicamocha = 1450000
valorNinoChicamocha = 960000
valorPersonaAdultoLlanos = 1200000
valorNinoLlanos = 720000

# Inicialización de variables
cantidadPersonasGuajira = 0
cantidadPersonasChicamocha = 0
cantidadPersonasLlanos = 0
totalGuajira = 0
totalChicamocha = 0
totalLlanos = 0
totalPersonasAdultas = 0
totalNinos = 0
totalDinero = 0

cantidadClientes = int(input("Ingrese la cantidad de clientes: "))

for cliente in range(cantidadClientes):
    nombreCliente = input("Nombre del cliente: ")
    destino = input("Destino del cliente: ")
    numPersonasAdultas = int(input("Número de personas adultas: "))
    numNinos = int(input("Número de niños: "))

    # if numPersonasAdultas + numNinos > cantidadClientes:
    #     print("El número de adultos y niños supera el número de clientes.")
    #     continue

    if destino == "guajira":
        cantidadPersonasGuajira += numPersonasAdultas + numNinos
        totalGuajira += (numPersonasAdultas * valorPersonaAdultoGuajira) + (numNinos * valorNinoGuajira)
    elif destino == "cañon del chicamocha":
        cantidadPersonasChicamocha += numPersonasAdultas + numNinos
        totalChicamocha += (numPersonasAdultas * valorPersonaAdultoChicamocha) + (numNinos * valorNinoChicamocha)
    elif destino == "llanos orientales":
        cantidadPersonasLlanos += numPersonasAdultas + numNinos
        totalLlanos += (numPersonasAdultas * valorPersonaAdultoLlanos) + (numNinos * valorNinoLlanos)
    
    totalPersonasAdultas += numPersonasAdultas
    totalNinos += numNinos
    totalDinero += (numPersonasAdultas * valorPersonaAdultoGuajira) + (numNinos * valorNinoGuajira)

print("Cantidad de personas que viajan para la Guajira:", cantidadPersonasGuajira)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", cantidadPersonasChicamocha)
print("Cantidad de personas que viajan para los llanos orientales:", cantidadPersonasLlanos)
print("Total de dinero de los viajes para la Guajira:", totalGuajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", totalChicamocha)
print("Total de dinero de los viajes para los llanos orientales:", totalLlanos)
print("Total de personas Adultas:", totalPersonasAdultas)
print("Total de niños:", totalNinos)
print("Total de dinero de todos los destinos:", totalDinero)
