# Definición de precio por destino
valorGuajiraAdulto = 1450000;valorGuajiraNino = 870000;valorChicamochaAdulto = 1450000;valorChicamochaNino = 960000;valorLlanosAdulto = 1200000;valorLlanosNino = 720000
cantGuajira = 0;cantChicamocha = 0;cantLlanos = 0;totalGuajira = 0;totalChicamocha = 0;totalLlanos = 0;totalAdultos = 0;totalNinos = 0
totalDinero = 0

cantClientes = int(input("Ingresa cantidad de clientes: "))

for i in range(cantClientes):
    nombre = input("Nombre del cliente: ")
    destino = input("Destino del cliente: ")
    adultos = int(input("Cantidad de adultos: "))
    ninos = int(input("Cantidad de niños: "))

    if destino == "guajira":
        cantGuajira += adultos + ninos
        totalGuajira += (adultos * valorGuajiraAdulto) + (ninos * valorGuajiraNino)
    elif destino == "cañon del chicamocha":
        cantChicamocha += adultos + ninos
        totalChicamocha += (adultos * valorChicamochaAdulto) + (ninos * valorChicamochaNino)
    elif destino == "llanos orientales":
        cantLlanos += adultos + ninos
        totalLlanos += (adultos * valorLlanosAdulto) + (ninos * valorLlanosNino)
    
    totalAdultos += adultos
    totalNinos += ninos
    totalDinero += (adultos * valorGuajiraAdulto) + (ninos * valorGuajiraNino)

   

print("|-----------------------------------------------------|")
print("|Guajira:", cantGuajira, "personas|")
print("|-----------------------------------------------------|")
print("|Cañón del Chicamocha:", cantChicamocha, "personas|")
print("|-----------------------------------------------------|")
print("|Llanos Orientales:|", cantLlanos, "personas|")
print("|-----------------------------------------------------|")
print("|Total dinero Guajira:|", totalGuajira,"|")
print("|-----------------------------------------------------|")
print("|Total dinero Cañón del Chicamocha:|", totalChicamocha,"|")
print("|-----------------------------------------------------|")
print("|Total dinero Llanos Orientales:|", totalLlanos,"|")
print("|-----------------------------------------------------|")
print("|Total personas Adultas:|", totalAdultos,"|")
print("|-----------------------------------------------------|")
print("|Total niños:\t|", totalNinos,"|")
print("|-----------------------------------------------------|")
print("|Total dinero todos los destinos:|", totalDinero,"|")
print("|-----------------------------------------------------|")