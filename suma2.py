import random
def suma():
    puntuacion = 0
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250]
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            a = rng.randrange(1,10)#hay que cambiar esto
            b = rng.randrange(1,10)# y esto tambien 
            res = a+b
            res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
            if res1 == res:
                print( "Respuesta Correcta")
                puntuacion += 5
                print(puntuacion)
            else:
                print( "Intentalo de nuevo" + "\n" )
                num1 = a
                num2 = b
                result = a+b
                result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
                if result == result1:
                    print ("Respuesta Correcta")
                    print(puntuacion)
                else:
                    print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
        print("Siguiente nivel") # esto tiene que ser un boton
