import random

def resta():
    #Hace restas aleatorias a medida que el puntaje va subiendo, las restas se vuelven mas dificles.
    puntuacion = 0 #contador de la puntuación.
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250] #El intervalo de puntaje en donde se cambia de nivel.
    rango = [10, 30, 50, 70, 100]#Cada vez que cambia de nivel, el rango tam.
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c+1)
            b = rng.randrange(1,c+1)
            if a>b:
                res = a-b
                res1 = int(input("¿Cuánto es " + str(a) + " - " + str(b) + "?  "))
                if res1 == res:
                    """se verifica si la respuesta es correcta y si lo es, suma la puntuacion"""
                    print( "Respuesta Correcta")
                    puntuacion += 5
                    print("Puntuación: " + str(puntuacion))
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer""" 
                    print( "Intentalo de nuevo" + "\n" )
                    num1 = a
                    num2 = b
                    result = a-b
                    result1 = int(input("¿Cuánto es " + str(num1) + " - " + str(num2) + "?  "))
                    if result == result1:
                        """Si en el segundo intento, su respuesta es correcta, suma puntaje"""
                        print ("Respuesta Correcta")
                        puntuacion += 5
                        print("Puntuación: " + str(puntuacion))
                    else:
                        """Si vuelve a fallar, la respuesta se imprime"""
                        print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
            else:
                """Si en la resta anterior b>a, cambiamos b por a para que el resultado sea positivo"""
                res = b-a
                res1 = int(input("¿Cuánto es " + str(b) + " - " + str(a) + "?  "))
                if res1 == res:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    print( "Respuesta Correcta")
                    puntuacion += 5
                    print("Puntuación: " + str(puntuacion))
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer""" 
                    print( "Intentalo de nuevo" + "\n" )
                    num1 = a
                    num2 = b
                    result = b-a
                    result1 = int(input("¿Cuánto es " + str(num2) + " - " + str(num1) + "?  "))
                    if result == result1:
                         """Si en el segundo intento, su respuesta es correcta, suma puntaje"""
                        print ("Respuesta Correcta")
                        puntuacion += 5
                        print("Puntuación: " + str(puntuacion))
                    else:
                        """Si vuelve a fallar, la respuesta se imprime"""
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
                    print("Terminaste las restas!")
resta()
