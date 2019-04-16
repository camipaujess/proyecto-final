import pygame

def image_and_text ():
    pygame.init()
    Pantalla = pygame.display.set_mode((650,450))
    pygame.display.set_caption("PyMath for children")
    image = pygame.image.load("fondo.jpg")
    fuente = pygame.font.SysFont("Lucida fax", 25) #Tipo de letra y tamaño
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        Pantalla.fill ((0, 200, 255))
        Pantalla.blit(image, (0,0))
        Text = fuente.render ("La suma entre 5 y 10", True, (255,0,0))
        Pantalla.blit(Text, (150,100))
        pygame.display.flip ()

    pygame.quit()

image_and_text()
