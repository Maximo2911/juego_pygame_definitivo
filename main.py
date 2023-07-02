import pygame, sys
from pygame.locals import *
from player import *
from constantes import *


# configuracion inicial de pygame
pygame.init()
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Jueguito Rico")
clock = pygame.time.Clock() # Creamos un Clock para poder fijar los FPS

corriendo_juego = True
frame_actual = 0

#Seteo jugador a esta posicion
jugador = Player(800, 800, frame_rate_ms = 2000)             #En frame_rate_ms = 1000 se rompe pero imagen bien

# Limito los FPS
clock.tick(FPS)
while corriendo_juego:
    # Manejamos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo_juego = False
            pygame.quit()
            sys.exit()
    
    delta_ms = clock.tick(FPS)
    keys = pygame.key.get_pressed()
    jugador.update(100, keys)

    

    # print(f"{jugador.animation} - {len(jugador.animation) - 1} < {jugador.frame}")
    print(f"{jugador.sliding}")
    # print(jugador.sliding)

    # print(jugador.rect)         |
    # print(jugador.move_x)       |       Sirve para ver desplazamiento
    # print(jugador.flipped)      |
    
    # print(f"{jugador.time_animations} >= {jugador.frame_rate_ms}")


    # jugador.do_animations(delta_ms)
    # print(jugador.animation[jugador.frame])
    pantalla_juego.fill((0, 0, 0))  # Limpiar el fondo de la pantalla
    jugador.draw(pantalla_juego)
    # Mostramos los cambios hechos(Actualizar la pantalla)
    pygame.display.flip()