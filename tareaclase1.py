#Hacer un programa en el que:
#1-Se pregunte por el nombre de la persona
#2-Se pregunte por el apellido de la persona
#3-Se pregunte por la edad de la persona.
#El formato de salida debe ser:
#"Su nombre es: " + nombre + apellido + "y usted es " {condición de edad}
#La condición de edad es:
#1. Si es menor de 18 escribir menor
#2. Si tiene entre 18 y 65 escribir mayor
#3. Si tiene entre 65 y 120 escribir jubilado
#4. Si tiene más escribir cadaver

print ("Bienvenido")
nombre = input("Digame su nombre ")
apellido = input("Digame su apellido ")
edad = int(input("Digame su edad "))
if edad < 0:
    print("Su nombre es: "+ str(nombre) +" " + str(apellido) + " y usted es no nato")
elif edad < 18:
    print("Su nombre es: "+ str(nombre) +" " + str(apellido) + " y usted es menor de edad")
elif edad < 64:
    print("Su nombre es: "+ str(nombre) +" " + str(apellido) + " y usted es mayor de edad")
elif edad < 120:
    print("Su nombre es: "+ str(nombre) +" " + str(apellido) + " y usted es un jubilado")
else:
    print("Usted es un cadaver")
