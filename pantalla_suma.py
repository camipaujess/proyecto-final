import pygame
import sys
import random

#----------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("intento de letra")
#--------------------------------------------------
# se define la fuente para los numeros
fuente = pygame.font.Font(None, 150)

#se escogen dos numeros al azar lara realizar la suma
aleatorio = random.Random()
numero_1 = aleatorio.randrange(1, 10)
numero_2 = aleatorio.randrange(1, 10)
resultado = numero_1 + numero_2
#print(resultado)

#se transorma todo en un str para poder imprimirlos en pantalla
text = (str(numero_1) + " + " + str(numero_2))
mensaje = fuente.render(text, True, (0, 0, 00))


#----------------------------------------------------
while True:
    evento = pygame.event.poll()
    if evento.type == pygame.QUIT:
        break
    screen.fill((79,165,232))
#---------------------------------------------------
    screen.blit(mensaje, (200, 50)) #se imprime en pantalla
    pygame.display.flip()

pygame.quit()
