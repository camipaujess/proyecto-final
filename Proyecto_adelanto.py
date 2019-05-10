from tkinter import *
from tkinter import simpledialog
import random
import time


root = Tk()
width = 1024 # ancho de la pantalla
height = 650 # alto de la pantalla
size = '70' # un tamaño general de letra
root.resizable (0,0)
 # se configura el color
canvas = Canvas(root, width = width, height = height) # se asigna la pantalla sobre la cual se dibuja


#f = 0
#entry = Entry(root,width = 50,bd = 1,textvariable = f)
puntuacion = 0 #variable global

#for q in range (10, 601):
#    listacirculo.append (q)
#    a = q +40
#    listacirculo.append (a)
#    q +=40
#print(listacirculo)



def inicio():
    colorbk = '#2299FF'
    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    listacirculo=[10, 50, 90, 130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530, 570, 610, 650, 690, 730, 770, 810, 850, 890, 930, 970, 1010, 1050, 1090, 1130]
    """ se crean los botones de la pantalla principal """
    circulo_pantalla (listacirculo)
    #canvas.create_window(width/2,height/2,anchor = CENTER,window = Label(root,text = "Holaa",font =('Arial',size) ))
    boton1 = Button(root, text = "Suma", command = suma) #boton suma
    boton1_2 = canvas.create_window(width/2, height*3/8, anchor=N, window = boton1, width = width/2)
    boton2 = Button(root, text = "Resta", command = resta) #boton resta
    boton2_2 = canvas.create_window(width/2, height/2, anchor=N, window = boton2, width = width/2)
    boton2 = Button(root, text = "Multiplicacion", command = multiplicacion) #boton multiplicacion
    boton2_2 = canvas.create_window(width/2, height*5/8, anchor=N, window = boton2, width = width/2)
    boton2 = Button(root, text = "Division", command = division) #boton division
    boton2_2 = canvas.create_window(width/2, height*3/4, anchor=N, window = boton2, width = width/2)


def circulo_pantalla (lista):
    lista2 = lista.copy()
    for q in lista:
        if lista.index(q)%2 ==0:
            canvas.create_oval (lista2[0], lista[0], lista2[1], lista[1], width =2, fill='red')
            del lista[0]
        else:
            canvas.create_oval(lista2[1], lista[0], lista2[2], lista[1], width=2, fill='purple')
            del lista[0]


def limpiar():
    """ se borra lo que este en pantalla volviendo al inicio """
    canvas.delete("all") # se borra todo
    #inicio() # se dibuja el inicio


def dibuja_operacion(num1, operador, num2):
    """se grafica la operacion correspondiente, indicando los numeros y el signo al usar la funcion"""
    global puntuacion #se toma como variable global
    limpiar ()
    canvas.create_text(0, 0,anchor = NW, text = "Puntuación: " + str(puntuacion), font =('Rockwell Condensed',size))
    text = "¿Cuánto es " + str(num1) + operador + str(num2) + "?  "
    canvas.create_text(width/2, height/3, anchor = CENTER, text = text, font =('Bernard MT Condensed', size))
    root.update()


def dibuja_pantalla (s, sz, font):
    """ se dibuja la puntuacion del usuario, junto con el str que se quiera graficar, dando tambien un tamaño de letra"""
    global puntuacion #se toma como variable global
    limpiar()
    canvas.create_text(0, 0, anchor = NW, text = "Puntuación: " + str(puntuacion), font =('Rockwell Condensed' , size))
    canvas.create_text(width/2, height* 2/3, anchor=CENTER, text = s, font = (font, sz))
    root.update()
    time.sleep(1)


def cambio_nivel (s, listapuntuacion, rango):
    for puntos in listapuntuacion:
        if puntuacion == puntos:
            """para que cambie de nivel, hacemos que los puntos sean iguales a la puntuacion"""
            if len(rango) != 0:
                 """Eliminamos el primer elemento del rango"""
                 del rango[0]
                 if puntuacion != listapuntuacion[-1]:
                     """Verificamos que el elemento del rango sea diferente al ultimo para cambiar de nivel"""
                     dibuja_pantalla("Siguiente nivel", size, 'Bernard MT Condensed') # esto tiene que ser un boton
                 else:
                     """Si el elemento del rango es igual al ultimo, el usuario ha terminado las sumas"""
                     dibuja_pantalla(s, size, 'Ink Free')
                     limpiar()
                 inicio()


def suma():
    global puntuacion
    operador = "+"
    """Hace sumas aleatorias cada vez más díficiles con respecto a la puntuación (con cierto puntaje se vuelve más díficil)"""
    puntuacion = 0 #Empieza la puntuación del juego
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250] #El intervalo del puntaje en el que se cambia de nivel
    rango = [10, 30, 50, 70, 100] #Cuando se cambia de nivel, cambian los rangos en los que se piden los números
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            """  se escogen los numeros aleatorios para realizar la operacion """
            c = rango[0]
            a = rng.randrange(1,c+1)
            b = rng.randrange(1,c+1)
            res = a+b
            dibuja_operacion(a, operador, b)
            res1 = simpledialog.askinteger("Respuesta", None, parent = root) #cuadro de texto para la respuesta
            if res1 is None:
                """se sale del cuadro de texto para las respuestas"""
                listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                limpiar()
                inicio()
                break
            #res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                puntuacion += 5
                #dibuja_pantalla("Puntuación: " + str(puntuacion))
                #answers = "Puntuación: " + str(puntuacion)
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                dibuja_pantalla( "Intentalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed')
                num1 = a
                num2 = b
                result = a + b
                dibuja_operacion(num1, operador, num2)
                result1 = simpledialog.askinteger("Respuesta", None, parent = root) #cuadro de texto para la respuesta
                #result1 = simpledialog.askinteger("Input","¿Cuánto es " + str(num1) + " + " + str(num2) + "?  ",parent = root)
                #result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
                if result == result1:
                    """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                    dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                    puntuacion += 5
                    #dibuja_pantalla("Puntuación: " + str(puntuacion))
                else:
                    """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                    dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35', 'Gloucester MT Extra Condensed')
                    #time.sleep(6) #se da un tiempo de espera
        cambio_nivel ("Terminaste las sumas!", listapuntuacion, rango)

#def fegs(msg):
#    p = root.Tk()
#    p.wm_title("l")
#    label = ttk.Label(p,text = msg)
def resta():
    global puntuacion
    operador = "-"
    #Hace restas aleatorias a medida que el puntaje va subiendo, las restas se vuelven mas dificles.
    puntuacion = 0 #contador de la puntuación.
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250] #El intervalo de puntaje en donde se cambia de nivel.
    rango = [10, 30, 50, 70, 100]#Cada vez que cambia de nivel, el rango tambien.
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c+1)
            b = rng.randrange(1,c+1)
            if a>b:
                res = a-b
                dibuja_operacion (a, operador, b)
                res1 = simpledialog.askinteger("Respuesta",None,parent = root)
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    """se verifica si la respuesta es correcta y si lo es, suma la puntuacion"""
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                    puntuacion += 5
                    #dibuja_pantalla("Puntuación: " + str(puntuacion), size)
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    dibuja_pantalla( "Intentalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed' )
                    num1 = a
                    num2 = b
                    result = a-b
                    dibuja_operacion (num1, operador, num2)
                    result1 = simpledialog.askinteger("Respuesta",None,parent = root)
                    if result == result1:
                        """Si en el segundo intento, su respuesta es correcta, suma puntaje"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                        puntuacion += 5
                        #dibuja_pantalla("Puntuación: " + str(puntuacion))
                    else:
                        """Si vuelve a fallar, la respuesta se imprime"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35', 'Gloucester MT Extra Condensed')
            else:
                """Si en la resta anterior b>a, cambiamos b por a para que el resultado sea positivo"""
                res = b-a
                dibuja_operacion (b, operador, a)
                res1 = simpledialog.askinteger("Rrta",None,parent = root)
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    """Si la respuesta es correcta, suma puntaje"""
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                    puntuacion += 5
                    #dibuja_pantalla("Puntuación: " + str(puntuacion))
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    dibuja_pantalla( "Intentalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed' )
                    num1 = a
                    num2 = b
                    result = b-a
                    dibuja_operacion (num1, operador, num2)
                    result1 = simpledialog.askinteger("Rrta",None,parent = root)
                    if result == result1:
                        """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                        puntuacion += 5
                        #dibuja_pantalla("Puntuación: " + str(puntuacion))
                    else:
                        """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35', 'Gloucester MT Extra Condensed')

        cambio_nivel ("Terminaste las restas", listapuntuacion, rango)


def multiplicacion():
    global puntuacion
    operador = "x"
    #Hace multiplicaciones aleatorias a medida que el puntaje va subiendo, las multiplicaciones se vuelven mas dificles.
    puntuacion = 0  #Empieza la puntuación del juego
    rng = random.Random()
    listapuntuacion = [50, 100]#El intervalo del puntaje en el que se cambia de nivel
    rango = [10, 30]#Cuando se cambia de nivel, cambian los rangos en los que se piden los números
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c+1)
            b = rng.randrange(1,11)
            res = a * b
            dibuja_operacion (a, operador, b)
            res1 = simpledialog.askinteger ("Respuesta", None, parent= root)
            if res1 is None:
                """se sale del cuadro de texto para las respuestas"""
                listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                limpiar()
                inicio()
                break
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                puntuacion += 5
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                dibuja_pantalla( "Intentalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed' )
                num1 = a
                num2 = b
                result = a*b
                dibuja_operacion (num1, operador, num2)
                result1 = simpledialog.askinteger("Respuesta", None, parent = root)
                if result == result1:
                    """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                    dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                    puntuacion += 5
                else:
                     """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                     dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35', 'Gloucester MT Extra Condensed')
        cambio_nivel ("Terminaste las multiplicaciones!", listapuntuacion, rango)


def division():
    global puntuacion
    operador = "÷"
    """Hace divisiones aleatorias cada vez más díficiles con respecto a la puntuación (con cierto puntaje se vuelve más díficil)"""
    puntuacion = 0 #Empieza la puntuación del juego
    rng = random.Random()
    listapuntuacion = [50, 100, 150, 200, 250] #El intervalo del puntaje en el que se cambia de nivel
    rango = [10, 30, 50, 70, 100] #Cuando se cambia de nivel, cambian los rangos en los que se piden los números
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c+1)
            b = rng.randrange(1,c+1)
            if a % b == 0:
                res = a//b
                dibuja_operacion (a, operador, b)
                """Se verifica que la division sea entera"""
                res1 = simpledialog.askinteger ("Respuesta", None, parent = root)
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                    puntuacion += 5
                else:
                    """ Si se responde incorrectamente, vuelve a preguntar"""
                    dibuja_pantalla( "Intentalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed' )
                    num1 = a
                    num2 = b
                    result = a//b
                    dibuja_operacion (num1, operador, num2)
                    result1 = simpledialog.askinteger ("Respuesta", None, parent = root)
                    if result == result1:
                        """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                        puntuacion += 5
                    else:
                        """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35', 'Gloucester MT Extra Condensed')
            elif b % a == 0:
                """Si en la division anterior b>a, cambiamos b por a para que el resultado sea entero"""
                res = b//a
                dibuja_operacion (b, operador, a)
                res1 = simpledialog.askinteger ("Respuesta", None, parent = root)
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                    puntuacion += 5
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    dibuja_pantalla( "Intentalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed' )
                    num1 = a
                    num2 = b
                    dibuja_operacion (num1, operador, num2)
                    result = b//a
                    result1 = simpledialog.askinteger ("Respuesta", None, parent = root)
                    if result == result1:
                        """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed')
                        puntuacion += 5
                    else:
                        """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35', 'Gloucester MT Extra Condensed')
        cambio_nivel ("Terminaste las divisiones!", listapuntuacion, rango)

inicio()
root.mainloop()
