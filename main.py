import pygame, sys
from pygame.locals import *
from player import *
from constantes import *
from auxiliar import *
from background import *
from platforms import *

# configuracion inicial de pygame
pygame.init()
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Jueguito Rico")
clock = pygame.time.Clock() # Creamos un Clock para poder fijar los FPS

corriendo_juego = True
frame_actual = 0

#Seteo jugador a esta posicion
jugador = Player(500, 600, frame_rate_ms = 250, gravity = 8, jump_power = 10, jump_height = 150)             #En frame_rate_ms = 1000 se rompe pero imagen bien

static_background_back = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/back.png")
static_background_far = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/far.png")
static_background_middle = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/middle.png")

plataform_list = []
plataform_list.append(Plataform(x=550,y=600,width=50,height=50,type=5))
plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=1))

plataform_list.append(Plataform(x=0,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=100,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=200,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=300,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=400,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=500,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=600,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=700,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=800,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=900,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=1000,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=1100,y=650,width=100,height=50,type=8))
plataform_list.append(Plataform(x=1200,y=650,width=100,height=50,type=8))




# Limito los FPS
clock.tick(FPS)
while corriendo_juego:
    # Manejamos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo_juego = False
            pygame.quit()
            sys.exit()
    static_background_back.draw(pantalla_juego)
    # static_background_far.draw(pantalla_juego)
    # static_background_middle.draw(pantalla_juego)

    for plataforma in plataform_list:
        plataforma.draw(pantalla_juego)
    delta_ms = clock.tick(FPS)
    keys = pygame.key.get_pressed()
    jugador.update(delta_ms, keys, plataform_list)

    

    # print(f"{jugador.animation} - {len(jugador.animation) - 1} < {jugador.frame}")
    # print(f"{jugador.flipped}")

    # print(jugador.rect.x)      |
    # print(jugador.rect.y)      |


    # print(jugador.rect)         |
    # print(jugador.move_x)       |       Sirve para ver desplazamiento
    # print(jugador.flipped)      |
    
    # print(jugador.is_on_plataform(plataform_list))

    # print(jugador.flag_jump)
    # print("----------")
    # print(jugador.flag_repeat)
    # print("__________")
    print(jugador.is_jump)

    # jugador.do_animations(delta_ms)
    # print(jugador.animation[jugador.frame])
    # pantalla_juego.fill((0, 0, 0))  # Limpiar el fondo de la pantalla
    

    jugador.draw(pantalla_juego)
    # Mostramos los cambios hechos(Actualizar la pantalla)
    pygame.display.flip()


