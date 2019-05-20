from tkinter import *
import random
import time
from multiprocessing.pool import ThreadPool


root = Tk()
width = 1024 # ancho de la pantalla
height = 650 # alto de la pantalla
size = '70' # un tamaño general de letra
root.resizable (0,0)
 # se configura el color
canvas = Canvas(root, width = width, height = height) # se asigna la pantalla sobre la cual se dibuja
dynamicvar = IntVar()
globali = 0
puntuacion = 0 #variable global


def posicion_actual():
    """ lee la posición en la cual se encuentra la ventana principal dentro de la pantalla
    No recibe ningún parámetro.
    """
    string = root.winfo_geometry()
    numero = ""
    lista = []

    for letter in range(len(string)):
        if string[letter] == '+':
            for letra in range(letter,len(string)):

                if letra+1 != len(string) and string[letra+1] != '+':
                    numero += string[letra+1]
                else:
                    lista.append(numero)
                    numero = ""
                    break
    return (lista[0],lista[1])


def obtener_dato(entry,root2):
    """Obtiene lo escrito en el cuadro de texto y lo guarda en la variable global.
    Parámetros:
    Entry -- es un cuadro de texto, lo que hace es convertir a entero y captar mediante un get lo escrito en el cuadro de texto
    Root2 -- pantalla en la cual se toma el dato
    """
    global globali
    if entry == None:
        globali = None
    else:
	    try:
                globali = int(entry.get())
	    except ValueError:
                globali = -1
    root2.destroy()


def pedir_numero ():
    """Ejecuta una pantalla a la vez dando prioridad a el cuadro de texto en el cual se esta a la espera de una entrada (número o respuesta).
    No recibe ningún parámetro.
    """
    pool = ThreadPool(processes = 1)
    assync_result = pool.apply_async(entry_text,(posicion_actual(),))
    res1 = assync_result.get()
    return res1


def entry_text(posicion):
    """Crea una segunda pantalla en la cual se genera el cuadro de texto y los botones respectivos para poder recibir y captar las respuestas del usuario (lo escrito en el cuadro de texto)
    Parámetros:
    Posición – de acuerdo a la posición de la pantalla principal se posiciona esta pantalla.
    """
    global dynamicvar
    root2 = Tk()
    frame = Frame (root2)
    frame.pack()
    root2.wm_attributes('-type', 'splash')
    root2.call('wm', 'attributes', '.', '-topmost', '1')
    root2.geometry("760x100+%d+%d" %(int(posicion[0])+(width/8),int(posicion[1])+6*height/10))
    entry = Entry(frame, width = 5, bd = 1,textvariable = dynamicvar, font = ('Rockwell Condensed', size),  justify = CENTER)
    entry.focus()
    boton = Button(frame, text = "OK",command = lambda : obtener_dato(entry,root2), width = 8, font = ('Rockwell Condensed',30), height = 2)
    boton_cancel = Button(frame, text = "VOLVER",command = lambda : obtener_dato(None,root2), width = 8, font = ('Rockwell Condensed',30), height = 2)
    entry.grid(row = 0,column = 0)
    boton.grid(row = 0,column = 1)
    boton_cancel.grid(row = 0, column = 2)
    root2.mainloop ()
    return globali

def inicio():
    """Se crean los botones de la pantalla principal (suma, resta, multiplicación y división).
    Se configura la pantalla dándole un color predeterminado (azul claro).
    Se crea el diseño general y se asigna un título predeterminado ('Bienvenido al Maravilloso Mundo de las Matemáticas').
    No recibe ningún parámetro.
    """
    colorbk = '#2299FF'  # se configura el color
    canvas.configure(background = colorbk)  # se configura el color de la pantalla
    canvas.pack()
    listacirculo=[10, 50, 90, 130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530, 570, 610, 650, 690, 730, 770, 810, 850, 890, 930, 970, 1010, 1050, 1090, 1130]
    """ se crean los botones de la pantalla principal """
    circulo_pantalla (listacirculo)
    canvas.create_text(width/8, height/8, anchor = NW, text = 'Bienvenido al Maravilloso\nMundo de las\nMatemáticas', font =('Showcard Gothic' , 40))
    boton1 = Button(root, text = "Suma", command = suma, font = ('Showcard Gothic', 20)) #boton suma
    boton1_2 = canvas.create_window(width/8,height/2, anchor=NW, window = boton1, width = width/3)
    boton2 = Button(root, text = "Resta", command = resta, font = ('Showcard Gothic', 20)) #boton resta
    boton2_2 = canvas.create_window(width/2,height/2 , anchor=NW, window = boton2, width = width/3)
    boton2 = Button(root, text = "Multiplicación", command = multiplicacion, font = ('Showcard Gothic', 20)) #boton multiplicacion
    boton2_2 = canvas.create_window(width/8,height*3/4 , anchor=NW, window = boton2, width = width/3)
    boton2 = Button(root, text = "División", command = division, font = ('Showcard Gothic', 20)) #boton division
    boton2_2 = canvas.create_window(width/2,height*3/4 , anchor=NW, window = boton2, width = width/3)


def circulo_pantalla (lista):
    """Se crean círculos con un color predeterminado (rojo y morado).

    Parámetros:
    Lista -– ubicación de los círculos según si el elemento de la lista es par o impar.

    De ser par, se deja fijo el primer y segundo elemento de la lista como parámetro x1 y x2
    en la coordenada (x1, y1), (x2, y2) y los parámetros y1 y y2 van cambiando, recorriendo la lista.

    De ser impar, se deja fijo el segundo y tercer elemento de la lista como parámetro x1 y x2
    en la coordenada (x1, y1), (x2, y2) y los parámetros y1 y y2 van cambiando, recorriendo la lista.
    """
    lista2 = lista.copy()
    for q in lista:
        if lista.index(q)%2 ==0:
            canvas.create_oval (lista2[0], lista[0], lista2[1], lista[1], width =2, fill='red')
            del lista[0]
        else:
            canvas.create_oval(lista2[1], lista[0], lista2[2], lista[1], width=2, fill='purple')
            del lista[0]


def limpiar():
    """ Se borra lo que este en pantalla volviendo al inicio del juego.
    No contiene parámetros.
     """
    canvas.delete("all") # se borra todo


def dibuja_operacion(num1, operador, num2):
    """grafica la operación dada junto con la puntuación.
    Tiene como texto predeterminado “¿cuánto es <num1> <operador> <num2>?”

    Parámetros:
    num1 –- primer sumando
    Operador –- símbolo de la operación aritmética que se desea graficar
    num2 –- ultimo sumando
    """
    global puntuacion #se toma como variable global
    img = PhotoImage(file = "kids.png")
    limpiar ()
    canvas.create_image(width/2, height*3/4, image=img)
    canvas.create_text(0, 0,anchor = NW, text = "Puntuación: " + str(puntuacion), font =('Rockwell Condensed',size))
    text = "¿Cuánto es " + str(num1) + operador + str(num2) + "?  "
    canvas.create_text(width/2, height/3, anchor = CENTER, text = text, font =('Bernard MT Condensed', size))
    root.update()


def dibuja_pantalla (s, sz, font, cond):
    """ Grafica en pantalla la puntuación del usuario junto con el texto que se desee.

    Parámetros:
    S -- texto (str) que se quiere graficar.
    sz -- tamaño de la letra.
    font -- fuente que se desea para el texto.
    cond -- toma un valor booleano, para poder ejecurtar las imagenes (bien o mal)
    """
    global puntuacion #se toma como variable global
    img = PhotoImage(file = "kids.png")
    img_bien = PhotoImage(file = "bien.png")
    img_mal = PhotoImage(file = "mal.png")
    limpiar()
    if cond == True:
        canvas.create_image(width/2, height/5, image=img_bien)
    elif cond == False:
        canvas.create_image(width/2, height/5, image=img_mal)
    elif cond == None:
        pass
    canvas.create_image(width/2, height*3/4, image=img)
    canvas.create_text(0, 0, anchor = NW, text = "Puntuación: " + str(puntuacion), font =('Rockwell Condensed' , size))
    canvas.create_text(width/2, height* 2/3, anchor=CENTER, text = s, font = (font, sz))
    root.update()
    time.sleep(3)


def cambio_nivel (s, listapuntuacion, rango):
    for puntos in listapuntuacion:
        if puntuacion == puntos:
            """para que cambie de nivel, hacemos que los puntos sean iguales a la puntuacion"""
            if len(rango) != 0:
                 """Eliminamos el primer elemento del rango"""
                 del rango[0]
                 if puntuacion != listapuntuacion[-1]:
                     """Verificamos que el elemento del rango sea diferente al ultimo para cambiar de nivel"""
                     dibuja_pantalla("Siguiente nivel", size, 'Bernard MT Condensed', True) # esto tiene que ser un boton
                 else:
                     """Si el elemento del rango es igual al ultimo, el usuario ha terminado las sumas"""
                     dibuja_pantalla(s, size, 'Ink Free', True)
                     limpiar()
                 inicio()
                 #A medida que va completando cierta cantidad de puntos, el usuario va cambiando de nivel


def suma():
    """Realiza sumas con dos números aleatorios, los cuales son escogidos de acuerdo a un rango.
     Este varía según la puntuación del usuario, aumentando proporcionalmente el rango con respecto a la puntuación

     No contiene parámetros
    """
    global puntuacion
    operador = "+"
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
            #res1 = pedir_numero ()
            while True:
                res1 = pedir_numero()
                if res1 == -1:
                    dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                    dibuja_operacion (a, operador, b)
                else:
                    break
            if res1 is None:
                """se sale del cuadro de texto para las respuestas"""
                listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                limpiar()
                inicio()
                break
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                puntuacion += 5
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                dibuja_pantalla( "Inténtalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed', False)
                num1 = a
                num2 = b
                result = a + b
                dibuja_operacion(num1, operador, num2)
                while True:
                    result1 = pedir_numero()
                    if result1 == -1:
                        dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                        dibuja_operacion(num1, operador, num2)
                    else:
                        break

                if result1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break

                if result == result1:
                    """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                    dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                    puntuacion += 5
                else:
                    """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                    dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '50', 'Gloucester MT Extra Condensed', False)
        cambio_nivel ("Terminaste las sumas!", listapuntuacion, rango)
        #Hace la suma con numero aleatorios, si el usuario se equivoca tendrá la oportunidad de volver a hacerlo
        #Si se vuelve a equivocar, el programa mostrara la respuesta correcta.
def resta():
    """Realiza restas con dos números aleatorios, estos cumplen una cierta condición
    el primero numero que se muestre en pantalla tiene que ser mayor al otro, esto para evitar que se realicen restas con números enteros negativos.
    Los números  varían el rango con el cual son escogidos de acuerdo a la puntuación del usuario.

    No contiene parámetros.
    """
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
                while True:
                    res1 = pedir_numero()
                    if res1 == -1:
                        dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                        dibuja_operacion (a, operador, b)
                    else:
                        break
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    """se verifica si la respuesta es correcta y si lo es, suma la puntuacion"""
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                    puntuacion += 5
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    dibuja_pantalla( "Inténtalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed', False)
                    num1 = a
                    num2 = b
                    result = a-b
                    dibuja_operacion (num1, operador, num2)
                    while True:
                        result1 = pedir_numero()
                        if result1 == -1:
                            dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                            dibuja_operacion(num1, operador, num2)
                        else:
                            break
                    if result1 is None:
                        """se sale del cuadro de texto para las respuestas"""
                        listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                        limpiar()
                        inicio()
                        break
                    if result == result1:
                        """Si en el segundo intento, su respuesta es correcta, suma puntaje"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                        puntuacion += 5
                    else:
                        """Si vuelve a fallar, la respuesta se imprime"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '50', 'Gloucester MT Extra Condensed', False)
            else:
                """Si en la resta anterior b>a, cambiamos b por a para que el resultado sea positivo"""
                res = b-a
                dibuja_operacion (b, operador, a)
                while True:
                    res1 = pedir_numero()
                    if res1 == -1:
                        dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                        dibuja_operacion (a, operador, b)
                    else:
                        break
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    """Si la respuesta es correcta, suma puntaje"""
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                    puntuacion += 5
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    dibuja_pantalla( "Inténtalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed', False)
                    num1 = b
                    num2 = a
                    result = b-a
                    dibuja_operacion (num1, operador, num2)
                    while True:
                        result1 = pedir_numero()
                        if result1 == -1:
                            dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                            dibuja_operacion(num1, operador, num2)
                        else:
                            break
                    if result1 is None:
                        """se sale del cuadro de texto para las respuestas"""
                        listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                        limpiar()
                        inicio()
                        break
                    if result == result1:
                        """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                        puntuacion += 5
                    else:
                        """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '50', 'Gloucester MT Extra Condensed', False)

        cambio_nivel ("Terminaste las restas", listapuntuacion, rango)
        #Hace restas con números aleatorios, si el sustraendo es mayor que el minuendo
        #se hace cambio de posicion para que el resultado siempre de un numero entero positivo.


def multiplicacion():
    """Se multiplican dos números escogidos al azar con un cierto rango que varía según la puntuación del usuario
    aumentando proporcionalmente.

    No contiene parámetros.
    """
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
            while True:
                res1 = pedir_numero()
                if res1 == -1:
                    dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                    dibuja_operacion (a, operador, b)
                else:
                    break
            if res1 is None:
                """se sale del cuadro de texto para las respuestas"""
                listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                limpiar()
                inicio()
                break
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                puntuacion += 5
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                dibuja_pantalla( "Inténtalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed', False)
                num1 = a
                num2 = b
                result = a*b
                dibuja_operacion (num1, operador, num2)
                while True:
                    result1 = pedir_numero()
                    if result1 == -1:
                        dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                        dibuja_operacion(num1, operador, num2)
                    else:
                        break
                if result1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if result == result1:
                    """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                    dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                    puntuacion += 5
                else:
                     """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                     dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '50', 'Gloucester MT Extra Condensed', False)
        cambio_nivel ("Terminaste las multiplicaciones!", listapuntuacion, rango)
        #Hace las multiplicaciones con números aleatorios.
        #Si el usuario se equivoca, tendrá oportunidad de volver a hacerlo, si vuelve a equivocarse el programa le mostrara la respuesta


def division():
    """se escogen dos números al azar con un cierto rango que varía según la puntuación, estos dos números tienen que cumplir dos condiciones:
    El primero tiene que ser mayor que el segundo.
    La división entre los números debe ser entera (exacta).

    No contiene parámetros
    """
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
                while True:
                    res1 = pedir_numero()
                    if res1 == -1:
                        dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                        dibuja_operacion (a, operador, b)
                    else:
                        break
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                    puntuacion += 5
                else:
                    """ Si se responde incorrectamente, vuelve a preguntar"""
                    dibuja_pantalla( "Inténtalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed', False)
                    num1 = a
                    num2 = b
                    result = a//b
                    dibuja_operacion (num1, operador, num2)
                    while True:
                        result1 = pedir_numero()
                        if result1 == -1:
                            dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                            dibuja_operacion(num1, operador, num2)
                        else:
                            break
                    if result1 is None:
                        """se sale del cuadro de texto para las respuestas"""
                        listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                        limpiar()
                        inicio()
                        break
                    if result == result1:
                        """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                        puntuacion += 5
                    else:
                        """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '50', 'Gloucester MT Extra Condensed', False)
            elif b % a == 0:
                """Si en la division anterior b>a, cambiamos b por a para que el resultado sea entero"""
                res = b//a
                dibuja_operacion (b, operador, a)
                while True:
                    res1 = pedir_numero()
                    if res1 == -1:
                        dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                        dibuja_operacion (a, operador, b)
                    else:
                        break
                if res1 is None:
                    """se sale del cuadro de texto para las respuestas"""
                    listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                    limpiar()
                    inicio()
                    break
                if res1 == res:
                    dibuja_pantalla( "Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                    puntuacion += 5
                else:
                    """Si la respuesta es incorrecta, la pregunta vuelve a aparecer"""
                    dibuja_pantalla( "Inténtalo de nuevo" + "\n", size, 'Gloucester MT Extra Condensed', False )
                    num1 = b
                    num2 = a
                    dibuja_operacion (num1, operador, num2)
                    result = b//a
                    while True:
                        result1 = pedir_numero()
                        if result1 == -1:
                            dibuja_pantalla ("   Ingresa un\nnúmero entero", size, 'Gloucester MT Extra Condensed', None)
                            dibuja_operacion(num1, operador, num2)
                        else:
                            break
                    if result1 is None:
                        """se sale del cuadro de texto para las respuestas"""
                        listapuntuacion.clear() # se elimina los elementos de la lista para poder salir del for
                        limpiar()
                        inicio()
                        break
                    if result == result1:
                        """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                        dibuja_pantalla ("Respuesta Correcta", size, 'Gloucester MT Extra Condensed', True)
                        puntuacion += 5
                    else:
                        """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                        dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '50', 'Gloucester MT Extra Condensed', True)
        cambio_nivel ("Terminaste las divisiones!", listapuntuacion, rango)
        #Hace divisiones enteras con números aleatorios.
        #si el divisor es mayor que el dividendo, se hace cambio de posisicion para que el resultado siempre de un numero entero positivo.

inicio()
root.mainloop()
