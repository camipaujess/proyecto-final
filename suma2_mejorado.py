from tkinter import *
from tkinter import simpledialog
import random
import threading
import time

root = Tk()
width = 1024
heigh = 650
size = '70'
colorbk = '#4542f4'
canvas = Canvas(root,width = width,heigh = heigh)
canvas.configure(background = '#4542f4')
canvas.pack()

#f = 0
#entry = Entry(root,width = 50,bd = 1,textvariable = f)
puntuacion = 0
def inicio():
    #canvas.create_window(width/2,heigh/2,anchor = CENTER,window = Label(root,text = "Holaa",font =('Arial','70') ))
    boton1 = Button(root,text = "Limpiar",command = limpiar,bg = '#ffffff',fg = 'black')
    boton1_2 = canvas.create_window(0,10,anchor=NW,window = boton1,width = width/2,)
    boton2 = Button(root, text = "Suma",command = suma)
    boton2_2 = canvas.create_window(width/2,10,anchor=NW,window = boton2, width = width/2)

def dibuja_operacion(num1,operador,num2):
     global puntuacion
     limpiar ()
     canvas.create_text(0, 0,anchor = NW,text = "Puntuacion: " + str(puntuacion),font =('Arial','70' ))
     text = "¿Cuánto es " + str(num1) + operador + str(num2) + "?  "
     canvas.create_text(width/2,heigh/3,anchor = CENTER,text = text,font =('Arial','70' ))
     root.update()
def limpiar():
    canvas.delete("all")
    #inicio()

def dibuja_pantalla (s, size):
    global puntuacion
    limpiar()
    canvas.create_text(0, 0,anchor = NW,text = "Puntuacion: " + str(puntuacion),font =('Arial','70' ))
    canvas.create_text(width/2,heigh* 2/3,anchor=CENTER,text = s,font = ('Arial', size))
    root.update()
    time.sleep(1)
def suma():
    global puntuacion
    operador = "+"
    """Hace sumas aleatorias cada vez más díficiles con respecto a la puntuación (con cierto puntaje se vuelve más díficil)
    """
    puntuacion = 0 #Empieza la puntuación del juego
    rng = random.Random()
    listapuntuacion = [50] #, 100, 150, 200, 250] #El intervalo del puntaje en el que se cambia de nivel
    rango = [10] #, 30, 50, 70, 100] #Cuando se cambia de nivel, cambian los rangos en los que se piden los números
    for puntos in listapuntuacion:
        while puntuacion < puntos:
            c = rango[0]
            a = rng.randrange(1,c)
            b = rng.randrange(1,c)
            res = a+b
            dibuja_operacion(a,"+",b)
            res1 = simpledialog.askinteger("Rrta",None,parent = root)
            if res1 is None:
                print("Quiero salir")
                break
                inicio()
            #res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
            if res1 == res:
                """ Se verifica si la respuesta que dio el usuario es correcta y si lo es, suma la puntuación """
                dibuja_pantalla( "Respuesta Correcta", size )
                puntuacion += 5
                #dibuja_pantalla("Puntuación: " + str(puntuacion))
                answers = "Puntuación: " + str(puntuacion)
            else:
                """ Si se responde incorrectamente, vuelve a preguntar"""
                dibuja_pantalla( "Intentalo de nuevo" + "\n", size )
                num1 = a
                num2 = b
                result = a+b
                dibuja_operacion(num1,"+",num2)
                result1 = simpledialog.askinteger("Rrta",None,parent = root)
                #result1 = simpledialog.askinteger("Input","¿Cuánto es " + str(num1) + " + " + str(num2) + "?  ",parent = root)
                #result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
                if result == result1:
                    """ En el segundo intento si contesta correctamente, imprime que fue correcto y aumenta la puntuación"""
                    dibuja_pantalla ("Respuesta Correcta", size)
                    puntuacion += 5
                    #dibuja_pantalla("Puntuación: " + str(puntuacion))
                else:
                    """ Si el usuario se vuelve a equivocar, le dice cuál era la respuesta correcta"""
                    dibuja_pantalla ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result), '35')
        if puntuacion == puntos:
           """para que cambie de nivel, hacemos que los puntos sean iguales a la puntuacion"""
           if len(rango) != 0:
               """Eliminamos el primer elemento del rango"""
               del rango[0]
               if puntuacion != listapuntuacion[-1]:
                   """Verificamos que el elemento del rango sea diferente al ultimo para cambiar de nivel"""
                   dibuja_pantalla("Siguiente nivel", size) # esto tiene que ser un boton
               else:
                   """Si el elemento del rango es igual al ultimo, el usuario ha terminado las sumas"""
                   dibuja_pantalla("Terminaste las sumas!", size)
                   limpiar()
                   inicio()

inicio()
root.mainloop()
