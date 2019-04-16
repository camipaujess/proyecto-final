import pygame
import random

Rojo = (255, 0, 0)
morado = (255,0,255)
negro = (0, 0, 0)

def pantallaSuma():
    pygame.init()
    pantalla = pygame.display.set_mode((700,500))
    pygame.display.set_caption("PyMath for children")
    fuente = pygame.font.SysFont("Lucida fax", 25) #tipo de letra y tamano
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        pantalla.fill((79,165,232))

#se comienza a dibujar todo el borde
    #circulos
        cordenadaSupC = [50, 150, 250, 350, 450, 550, 650]
        for cordenada1 in cordenadaSupC:
            """se dibuja la linea superior de circulos"""
            pygame.draw.circle(pantalla, Rojo, [cordenada1, 40], 20, 0)

        cordenadaLatDC = [140, 240, 340, 440]
        for cordenada2 in cordenadaLatDC:
            """se dibuja la linea lateral derecha de circulos"""
            pygame.draw.circle(pantalla, Rojo, [50, cordenada2], 20, 0)

        cordenadaInfC = [150, 250, 350, 450, 550, 650]
        for cordenada3 in cordenadaInfC:
            """se dibuja la linea inferior de circulos"""
            pygame.draw.circle(pantalla, Rojo, [cordenada3, 440], 20, 0)

        cordenadaLatIC = [140, 240, 340, 440]
        for cordenada4 in cordenadaLatIC:
            """se dibuja la linea lateral izquierda"""
            pygame.draw.circle(pantalla, Rojo, [650, cordenada4], 20, 0)

    #triangulos

# TRIANGULO LADO IZQUIERDO
        pygame.draw.polygon(pantalla, morado, [[100, 60],[ 75, 100], [125, 100]], 0)
        pygame.draw.polygon(pantalla, morado, [[100, 160],[ 75, 200], [125, 200]], 0)
        pygame.draw.polygon(pantalla, morado, [[100, 260],[ 75, 300], [125, 300]], 0)
        pygame.draw.polygon(pantalla, morado, [[100, 360],[ 75, 400], [125, 400]], 0)
#TRIANGULO LINEA SUPERIOR
        pygame.draw.polygon(pantalla, morado, [[200, 60],[ 175, 100], [225, 100]], 0)
        pygame.draw.polygon(pantalla, morado, [[300, 60],[ 275, 100], [325, 100]], 0)
        pygame.draw.polygon(pantalla, morado, [[400, 60],[ 375, 100], [425, 100]], 0)
        pygame.draw.polygon(pantalla, morado, [[500, 60],[ 475, 100], [525, 100]], 0)

#TRIANGULO LINEA DERECHA
        pygame.draw.polygon(pantalla, morado, [[600, 60],[ 575, 100], [625, 100]], 0)
        pygame.draw.polygon(pantalla, morado, [[600, 160],[ 575, 200], [625, 200]], 0)
        pygame.draw.polygon(pantalla, morado, [[600, 260],[ 575, 300], [625, 300]], 0)
        pygame.draw.polygon(pantalla, morado, [[600, 360],[ 575, 400], [625, 400]], 0)
#TRIANGULO LADO DE ABAJO
        pygame.draw.polygon(pantalla, morado, [[200, 360],[ 175, 400], [225, 400]], 0)
        pygame.draw.polygon(pantalla, morado, [[300, 360],[ 275, 400], [325, 400]], 0)
        pygame.draw.polygon(pantalla, morado, [[400, 360],[ 375, 400], [425, 400]], 0)
        pygame.draw.polygon(pantalla, morado, [[500, 360],[ 475, 400], [525, 400]], 0)

        #parde de la suma
        puntuacion = 0
        rng = random.Random()
        listapuntuacion = [50, 100, 150, 200]
        rango = [10, 50, 100, 500]
        for puntos in listapuntuacion:
            while puntuacion < puntos:
                c = rango[0]
                a = rng.randrange(1,c)
                b = rng.randrange(1,c)
                res = a+b
                res1 = int(input("¿Cuánto es " + str(a) + " + " + str(b) + "?  "))
                if res1 == res:
                    texto = fuente.render("Respuesta Correcta", True, negro)
                    pantalla.blit(texto, (350, 250))
                    puntuacion += 5
                    print("Puntuación: " + str(puntuacion))
                else:
                    print( "Intentalo de nuevo" + "\n" )
                    num1 = a
                    num2 = b
                    result = a+b
                    result1 = int(input("¿Cuánto es " + str(num1) + " + " + str(num2) + "?  "))
                    if result == result1:
                        texto = fuente.render("Respuesta Correcta", True, negro)
                        pantalla.blit(texto, (350, 250))
                        puntuacion += 5
                        print("Puntuación: " + str(puntuacion))
                    else:
                        print ("Respuesta incorrecta" + "\n" + "La respuesta correcta es: " + str(result))
            if puntuacion == puntos:
                del rango[0]
                print("Siguiente nivel") # esto tiene que ser un boton
                if len(rango)== 0
                    print("Has terminado los niveles de la suma!")
        pygame.display.flip()
    pygame.quit()
pantallaSuma()
