#Básicamente es un pedazo de código al cual le vamos a dar una funcionalidad y se va a llamar cada vez que se necesite
#Scope de la variable: donde vive la variable. En este caso vive dentro de la funcion

def mi_funcion():
    print("Entraste a la funcion")

def sumar (primer_numero, segundo_numero)
    suma =primer_numero + segundo_numero
    print (suma)

def estado(edad):
    if edad<0:
        estado = "usted no nacio"
    elif edad <18:
        estado = "Usted es menor de edad"
    elif edad <65:
        estado = "usted es mayor de edad"
    else:
        estado = "usted es jubilado"
    return estado

clientes = int(input("Ingrese número de clientes: "))
for i in range(clientes):
    print(i)
    edad = 0
    while edad <1 or edad>120:
        edad = int(input("Digame su edad "))
    print (estado(edad))
    #estado_final = estado(edad)
