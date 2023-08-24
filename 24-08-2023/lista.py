modulos =["Logica","Base de datos","html5","moviles","Logica","html5","Base de datos","html5"]

""" print(modulos)
print("elemento incial de la lista",modulos[0])
print("elemento final de la lista",modulos[-1])
#len es el equivalente de length en otros lenguajes 
print("numero de elementos que contiene la lista",len(modulos))
print("numero de elementos que contiene la lista",modulos[len(modulos)-1])
print(" agregar un elemento a la lista Metodologias Agiles ") """
modulos.append("Metodologias Agiles")
print(modulos)
#cantidad de veces que se repite un elemento en la lista 
print("cantidad de veces que aparece html5 es:",modulos.count("html5"),"\n")
print("lista ordenada alfabeticamente\n")
modulos.sort()
print(modulos,"\n")
for indice in modulos:
    print(indice)