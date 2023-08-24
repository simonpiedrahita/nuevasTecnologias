
print("calcular nota definitiva ")

nombre= input("Nombre Estudiante")
nota1= float(input("nota1: " ))
nota2= float(input("nota2: " ))
nota3= float(input("nota3: " ))
definitiva = (nota1 + nota2 + nota3)/3 #la definitiva se calcula 
print("esto es impreso con print \n", " la nota definitiva para el estudiante", nombre , "es:" , definitiva,"\n" )

print(f"esto es impreso con print(f.....)\n es estudiante: {nombre} tiene las sgts notas \n nota1: {nota1} \n nota2: {nota2} \n nota3: {nota3} \n definitiva: {definitiva} \n  ")
 

""" if definitiva >= 3.0:
    print(f"el estudiante {nombre} tiene una calificacion definitiva de :{definiiva}, por lo tanto aprueba")
else: 
    print(f"el estudiante {nombre} tiene una calificacion definitiva de :{definiiva}, por lo tanto no aprueba") """
    
    
if 0 <= definitiva <= 2.0:
    print("Nota definitiva: reprobado",definitiva)
elif 2.0 < definitiva <= 3.0:
    print("Nota definitiva: Bien",definitiva)
elif 3.0 < definitiva <= 4.0:
    print("Nota definitiva: Notable",definitiva)
elif 4.0 < definitiva <= 4.6:
    print("Nota definitiva: Sobresaliente",definitiva)
elif 4.6 < definitiva <= 5.0:
    print("Nota definitiva: Nota excepcional",definitiva)
else:
    print("Nota definitiva:{definitiva} Reprobado")