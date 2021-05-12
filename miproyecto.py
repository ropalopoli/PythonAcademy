print ("Bienvenido")
#edad = 21
edad = input("Digame su edad")
#print (edad)
edad = int(edad)
#if edad >= 18:
     #print("Usted es mayor de edad")
     #if edad == 65:
         #print ("Haga el trámite de jubilación")
#else:
    #print("Usted es menor de edad")

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
