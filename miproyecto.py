clientes = int(input("Ingrese número de clientes: "))
for i in range(clientes):
    print (i)
    print ("Bienvenido")
    edad = input("Digame su edad")
    edad = int(edad)

    if edad<0:
        print ("usted no nacio")
    elif edad <18:
        print ("Usted es menor de edad")
    elif edad <65:
        print ("usted es mayor de edad")
    elif edad <120:
        print ("usted es jubilado")
    else:
        print ("usted esta en el otro mundo")
        break
else:
    print ("Proceso de carga finalizado")
