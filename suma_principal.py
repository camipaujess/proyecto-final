from tkinter import *
from tkinter import simpledialog
import random
import threading
import time

root = Tk()
width = 1024
heigh = 650
canvas = Canvas(root,width = width,heigh = heigh)
canvas.configure(background = '#4542f4')
canvas.pack()

#f = 0
#entry = Entry(root,width = 50,bd = 1,textvariable = f)
answers = ""
def inicio():
    #canvas.create_window(width/2,heigh/2,anchor = CENTER,window = Label(root,text = "Holaa",font =('Arial','70') ))
    boton1 = Button(root,text = "Limpiar",command = limpiar,bg = '#ffffff',fg = 'black')
    boton1_2 = canvas.create_window(0,10,anchor=NW,window = boton1,width = width/2,)
    boton2 = Button(root, text = "Suma",command = suma)
    boton2_2 = canvas.create_window(width/2,10,anchor=NW,window = boton2, width = width/2)

def dibuja_operacion(num1,operador,num2):
     canvas.create_window(width/2,heigh/2,anchor = CENTER,window = Label(root,text = answers,font =('Arial','70') ))
     text = "¿Cuánto es " + str(num1) + operador + str(num2) + "?  "
     canvas.create_window(width/2,50,anchor = CENTER,window = Label(root,text = text))
     root.update()
def limpiar():
    canvas.delete("all")
    inicio()

def suma():
    global answers
    operador = "+"
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
            dibuja_operacion(a,"+",b)
            res1 = simpledialog.askinteger("holas","¿Cuánto es " + str(a) + " + " + str(b) + "?  ",parent = root)
            if res1 is None:
                print("Quiero salir")
                break
                inicio()
            #res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                print( "Respuesta Correcta")
                answers = "Respuesta Correcta"
                puntuacion += 5
                print("Puntuación: " + str(puntuacion))
                answers = "Puntuación: " + str(puntuacion)
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                print( "Intentalo de nuevo" + "\n" )
                answers = "Intentalo de nuevo" + "\n"
                num1 = a
                num2 = b
                result = a+b
                result1 = simpledialog.askinteger("Input","¿Cuánto es " + str(num1) + " + " + str(num2) + "?  ",parent = root)
                #result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
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
                   """Si el elemento del rango es igual al ultimo, el usuario ha terminado las sumas"""
                   print("Terminaste las sumas!")
inicio()
root.mainloop()
