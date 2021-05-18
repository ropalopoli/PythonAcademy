#1. Crear un nuevo repositorio
#2. Tomar de base el la tarea de la clase 2
#3. Si es menor de edad, vamos a venderle juguetes
#3.1: preguntarle si es electrónico, color, camina
#4. Si es mayor de edad, vamos a venderle ropa
#4.1: preguntarle si es camisa o pantalon, color y el talle
#5. Si es jubilado vamos a venderle pasajes
#5.1 Preguntarle si quiere viajar a Federación, Cataratas o Santa Teresita
#Mostrar por pantalla los datos de la persona y el producto seleccionado
def jugueteria(edad):
    if edad <18:
        electronico = input("Desea un juguete electrónico? Si/No: ")
        color = input("Digame el color que desea ")
        camina = input("Desea que camine solo? Si/No: ")
    print("Su selección es: "+str(electronico)+" "+str(color)+" "+str(camina))

def tienda_ropa(edad):
    if edad <=64:
        ropa = input("Desea camisa o pantanlon ? ")
    print("Su seleccion es: "+str(ropa))

def pasajes(edad):
    if edad <120:
        pasajes = input("Desea viajar a Federación, Cataratas o Santa Teresita? ")
    print("Su seleccion es: "+str(pasajes))

clientes = int(input("Ingrese número de clientes: "))
for i in range(clientes):
    print(i)
    edad = 0
    while edad <1 or edad>120:
        edad = int(input("Digame su edad: "))
        if edad<18:
            print(jugueteria(edad))
        elif edad <65:
            print(tienda_ropa(edad))
        else:
            print(pasajes(edad))
