import random
def sumanivel_1():
    puntuacion = 0
    rng = random.Random()
    while puntuacion<50:
        a = rng.randrange(1,10)
        b = rng.randrange(1,10)
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
    while puntuacion<100:
        a = rng.randrange(1,50)
        b = rng.randrange(1,50)
        res = a+b
        res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
        if res1 == res:
            print( "Respuesta Correcta")
            puntuacion += 5
        else:
            print( "Intentalo de nuevo" + "\n" )
            num1 = a
            num2 = b
            result = a+b
            result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
            if result == result1:
                print ("Respuesta Correcta")
            else:
                print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
    print("Siguiente nivel") # esto tiene que ser un boton
    while puntuacion<150:
        a = rng.randrange(1,100)
        b = rng.randrange(1,100)
        res = a+b
        res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
        if res1 == res:
            print( "Respuesta Correcta")
            puntuacion += 5
        else:
            print( "Intentalo de nuevo" + "\n" )
            num1 = a
            num2 = b
            result = a+b
            result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
            if result == result1:
                print ("Respuesta Correcta")
            else:
                print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
    print("Siguiente nivel") # esto tiene que ser un boton
    while puntuacion<200:
        a = rng.randrange(1,500)
        b = rng.randrange(1,500)
        res = a+b
        res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
        if res1 == res:
            print( "Respuesta Correcta")
            puntuacion += 5
        else:
            print( "Intentalo de nuevo" + "\n" )
            num1 = a
            num2 = b
            result = a+b
            result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
            if result == result1:
                print ("Respuesta Correcta")
            else:
                print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
    print("Siguiente nivel") # esto tiene que ser un boton
    while puntuacion<250:
        a = rng.randrange(1,1000)
        b = rng.randrange(1,1000)
        res = a+b
        res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
        if res1 == res:
            print( "Respuesta Correcta")
            puntuacion += 5
        else:
            print( "Intentalo de nuevo" + "\n" )
            num1 = a
            num2 = b
            result = a+b
            result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
            if result == result1:
                print ("Respuesta Correcta")
            else:
                print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
sumanivel_1()
