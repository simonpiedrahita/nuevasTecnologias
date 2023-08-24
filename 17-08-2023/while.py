respuesta=1

while respuesta == 1 :
    respuesta = int(input("1.si 3\n 2. si no \n escriba el numero para continuar"))

    while respuesta!= 1 and respuesta!= 2:
        print("algo salio mal")
        respuesta = int(input("1.si 3\n 2. si no \n escriba el numero para continuar"))
        