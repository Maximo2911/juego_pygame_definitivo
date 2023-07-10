import pygame, sys
from pygame.locals import *
from player import *
from enemies import Enemy
from constantes import *
from auxiliar import *
from background import *
from platforms import *
from money import *


# configuracion inicial de pygame
pygame.init()
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Jueguito Rico")
clock = pygame.time.Clock() # Creamos un Clock para poder fijar los FPS

corriendo_juego = True
contador_money = 0

#Seteo jugador a esta posicion
jugador = Player(250, 600, frame_rate_ms = 250, gravity = 5.5, jump_power = 12.5, jump_height = 150)             #En frame_rate_ms = 1000 se rompe pero imagen bien

static_background_back = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/back.png")
static_background_far = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/far.png")
static_background_middle = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/middle.png")

plataform_list = []
plataform_list.append(Plataform(x=550,y=600,width=50,height=50,type=5))
plataform_list.append(Plataform(x=450,y=500,width=50,height=25,type=1))

money_list = []
money_list.append(Money(800, 550, 100))
money_list.append(Money(850, 550, 100))
money_list.append(Money(825, 550, 100))


enemy_list = []
enemy_list.append(Enemy(x=150,y=600,path="enemies/skeleton/{0}.png",from_index=0,quantity=8,p_scale=1.7,speed_move=5, frame_move=50,frame_rate_ms=100, gravity=5.5, x_init=100, x_end=300))
enemy_list.append(Enemy(x=150,y=300,path="enemies/bat/{0}.png",from_index=0,quantity=5,p_scale=1.7,speed_move=5, frame_move=50,frame_rate_ms=100, gravity=None, x_init=250, x_end=500))

# enemy_list.append(Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))

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

bullets_list = jugador.bullet_list
# Clase bullet
# bullet = Bullet(int(jugador.collition_rect.x)+5, int(jugador.collition_rect.y)+5, ANCHO_PANTALLA, 5, 500, 5, 5, 5)
# print(bullet.frame_rate_ms)

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
    delta_ms = clock.tick(FPS)

    for plataforma in plataform_list:
        plataforma.draw(pantalla_juego)
        # print(f"{jugador.collition_rect.top} == {plataforma.collition_rect.bottom}")

    for enemy in enemy_list:
        if enemy.flag_impact:
            enemy_list.remove(enemy)
        enemy.update(delta_ms, plataform_list, bullets_list)
        enemy.draw(pantalla_juego)
        print(enemy.rect)

    
    for money in money_list:
        if money.flag_collition:
            money_list.remove(money)
            # contador_money += 1
        money.update(delta_ms, jugador)
        money.draw(pantalla_juego)
    if len(money_list) == 0:
        print("HAS GANADO")

    for bullet in bullets_list:
    # print(bullet.rect.x)
        if not bullet.is_active:
            bullets_list.remove(bullet)
        # print(bullet.is_active)
        bullet.update(delta_ms,plataform_list, enemy_list, jugador)
        bullet.draw(pantalla_juego)
        # print(f"{bullet.tiempo_transcurrido_animation} >= {bullet.frame_rate_ms}")
        # print(f"-----------------{bullet.is_active}")

    keys = pygame.key.get_pressed()
    jugador.update(delta_ms, keys, plataform_list, enemy_list)
    # bullet.update(delta_ms, plataform_list, 0, jugador)

    

    # print(f"{jugador.animation} - {len(jugador.animation) - 1} < {jugador.frame}")
    # print(f"{jugador.flipped}")

    # print(jugador.rect.x)      |
    # print(jugador.rect.y)      |


    # print(jugador.rect)         |
    # print(jugador.move_x)       |       Sirve para ver desplazamiento
    # print(jugador.flipped)      |
    
    # print(jugador.is_jump)

    # print(jugador.flag_jump)
    # print("----------")
    # print(jugador.flag_repeat)
    # print(f"{jugador.flag_impact}")
    

    # jugador.do_animations(delta_ms)
    # print(jugador.animation[jugador.frame])
    # pantalla_juego.fill((0, 0, 0))  # Limpiar el fondo de la pantalla
    

    jugador.draw(pantalla_juego)
    # bullet.draw(pantalla_juego)
    # Mostramos los cambios hechos(Actualizar la pantalla)
    pygame.display.flip()


