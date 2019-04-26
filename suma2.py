import random
def suma():
    puntuacion = 0
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250]
    rango = [10, 30, 50, 70, 100]
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c)
            b = rng.randrange(1,c)
            res = a+b
            res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
            if res1 == res:
                print( "Respuesta Correcta")
                puntuacion += 5
                print("Puntuación: " + str(puntuacion))
            else:
                print( "Intentalo de nuevo" + "\n" )
                num1 = a
                num2 = b
                result = a+b
                result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
                if result == result1:
                    print ("Respuesta Correcta")
                    puntuacion += 5
                    print("Puntuación: " + str(puntuacion))
                else:
                    print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
        if puntuacion == puntos:
            if len(rango) != 0:
                del rango[0]
                if puntuacion != listapuntuacion[-1]:
                    print("Siguiente nivel") # esto tiene que ser un boton
                else:
                    print("Terminaste las restas!")
suma ()
