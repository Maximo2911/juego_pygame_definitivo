import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_main_menu import FormMenu
from gui_form_niveles import FormNiveles
from gui_form_options import FormOpciones
from gui_widget import Widget
from gui_form import Form
from gui_form_level_one import FormGameLevel1
from gui_form_level_two import FormGameLevel2
from gui_form_level_three import FormGameLevel3

from gui_form_pausa import FormPausa
from music import Musica


flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

musica = Musica()
musica.play_musica()
# juego = FordManager(PANTALLA)


timer_1s = pygame.USEREVENT + 0
pygame.time.set_timer(timer_1s,1000)
main_menu = FormMenu("menu", screen, x=0, y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=BLACK, imagen_background=r"buttoms\window\0.png", color_border=BLACK, active=True)
form_niveles = FormNiveles(name="niveles",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=BLACK,imagen_background=r"buttoms\window\0.png",color_border=BLACK,active=False)
form_options = FormOpciones(name="opciones",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=BLACK,imagen_background=r"buttoms\window\0.png",color_border=BLACK,active=False)

form_game_L1 = FormGameLevel1(name="nivel_1",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,color_border=None,active=False)
form_game_L2 = FormGameLevel2(name="nivel_2",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,color_border=None,active=False)
form_game_L3 = FormGameLevel3(name="nivel_3",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,color_border=None,active=False)

form_pausa = FormPausa(name="pausa", master_surface= screen, x= 320, y= 125, w=600, h=450, color_background=None, imagen_background=r"buttoms\window\0.png", color_border=None, active=False)
while True:     
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    # print(form_pausa.active)
    if(main_menu.active):
        # print(main_menu.update(events))
        main_menu.update(events)
        main_menu.draw()

    elif(form_options.active):
        form_options.update(events,musica.sonidos)
        form_options.draw()

    elif(form_niveles.active):
        form_niveles.update(events)
        form_niveles.draw()

    # elif(form_niveles.active):
    #     form_niveles.update(events)
    #     form_niveles.draw()

    elif(form_game_L1.active):
        form_game_L1.update(events, keys, delta_ms, musica)
        form_game_L1.draw(screen)
        # print(form_pausa.active)
        if(form_pausa.active):
            print("ENTRÓ")
            form_pausa.update(events)
            form_pausa.draw()

    elif(form_game_L2.active):
        form_game_L2.update(events, keys, delta_ms, musica)
        form_game_L2.draw(screen)
        if(form_pausa.active):
            form_pausa.update(events)
            form_pausa.draw()
    
    elif(form_game_L3.active):
        form_game_L3.update(events, keys, delta_ms, musica)
        form_game_L3.draw(screen)
        if(form_pausa.active):
            form_pausa.update(events)
            form_pausa.draw()

    # elif(form_pausa.active):
    #     form_pausa.update(events)
    #     form_pausa.draw()

    pygame.display.update()


    




    


  



