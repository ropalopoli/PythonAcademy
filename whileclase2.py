i = 1

while i<10:
    print (i)
    #i = i+1
    i +=1

nombre = input("Nombre: ")
adivinar = ""
oportunidades = 6
while nombre != adivinar:
    oportunidades -= 1
    print("oportunidades: " + str(oportunidades))
    adivinar = input("Adivine el nombre: ")
    if oportunidades == -1:
        print("Perdiste!")
        break
else:
    print ("Adivinó!")
