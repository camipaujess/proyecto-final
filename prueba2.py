import pygame

def image_in_frame ():
    pygame.init()
    Frame = pygame.display.set_mode((650,450))
    pygame.display.set_caption("PyMath for children")
    image = pygame.image.load("fondo.jpg")
    fuente = pygame.font.SysFont("Lucida fax", 25) #Tipo de letra y tamaño
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        Frame.fill ((0, 200, 255))
        Frame.blit(image, (0,0))
        texto = fuente.render ("La suma entre 5 y 10", True, (0,0,0))
        Frame.blit(texto, (150,100))
        pygame.display.flip ()

    pygame.quit()

image_in_frame()
