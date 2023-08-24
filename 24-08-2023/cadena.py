mensaje = "             Bienvenido a python "

# # Metodo len = Imprime el tamaño de longitud del string
# print("El tamaño del texto es de ", len(mensaje))

# # Metodo strip = Quita espacios al inicio y al final del texto
sinEspacios =  mensaje.strip()

# print("El tamaño del texto sin espacios ", sinEspacios)
# print("El tamaño del texto sin espacios es de ", len(sinEspacios))

# # Metodo upper = Mayuscula sostenida
# print("\n Texto en MAYUSCULA sostenida")
# print(sinEspacios.upper())

# # Metodo lower = Minuscula sostenida
# print("\n Texto en minuscula sostenida")
# print(sinEspacios.lower())

# # Metodo title = Inicial de cada palabra queda en MAYUSCULA
# print("\n Texto en Mayuscula inicial cada palabra")
# print(sinEspacios.title())

# # Metodo capitalize = Inicial de texto empieza en MAYUSCULA
# print("\n Texto en Mayuscula inicial en el texto")
# print(sinEspacios.capitalize())

parrafo = sinEspacios.split("...")
print(parrafo[0])
print(parrafo[1])
