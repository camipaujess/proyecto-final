import random
def suma():
    """Hace sumas aleatorias cada vez más díficiles con respecto a la puntuación (con cierto puntaje se vuelve más díficil)
    """
    puntuacion = 0 #Empieza la puntuación del juego
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250] #El intervalo del puntaje en el que se cambia de nivel
    rango = [10, 30, 50, 70, 100] #Cuando se cambia de nivel, cambian los rangos en los que se piden los números 
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c)
            b = rng.randrange(1,c)
            res = a+b
            res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                print( "Respuesta Correcta")
                puntuacion += 5
                print("Puntuación: " + str(puntuacion))
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                print( "Intentalo de nuevo" + "\n" )
                num1 = a
                num2 = b
                result = a+b
                result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
                if result == result1:
                    """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                    print ("Respuesta Correcta")
                    puntuacion += 5
                    print("Puntuación: " + str(puntuacion))
                else:
                    """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                    print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
        if puntuacion == puntos:
           """para que cambie de nivel, hacemos que los puntos sean iguales a la puntuacion"""
            if len(rango) != 0:
                 """Eliminamos el primer elemento del rango"""
                del rango[0]
                if puntuacion != listapuntuacion[-1]:
                    """Verificamos que el elemento del rango sea diferente al ultimo para cambiar de nivel"""
                    print("Siguiente nivel") # esto tiene que ser un boton
                else:
                    """Si el elemento del rango es igual al ultimo, el usuario ha terminado las restas"""
                    print("Terminaste las sumas!")
suma ()
