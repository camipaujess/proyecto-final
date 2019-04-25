import random
def multiplicacion():
    puntuacion = 0
    rng = random.Random()
    listapuntuacion = [50, 100]
    rango = [10, 30]
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c+1)
            b = rng.randrange(1,11)
            res = a * b
            res1 = int(input("¿Cuánto es " + str(a) + " x " + str(b) + "?  "))
            if res1 == res:
                print( "Respuesta Correcta")
                puntuacion += 5
                print("Puntuación: " + str(puntuacion))
            else:
                print( "Intentalo de nuevo" + "\n" )
                num1 = a
                num2 = b
                result = a*b
                result1 = int(input("¿Cuánto es " + str(num1) + " x " + str(num2) + "?  "))
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
                    print("Terminaste las multiplicaciones")
multiplicacion ()
