import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_main_menu import FormMenu
from gui_form_niveles import FormNiveles
from gui_form_options import FormOpciones
from gui_widget import Widget
from gui_form import Form
from gui_form_levels import FormGameLevel
from gui_form_lose import FormLose
from gui_form_win import FormWin
from gui_form_puntuaciones import FormPuntuaciones
from gui_form_pausa import FormPausa
from music import Musica

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

music = Musica()
music.play_musica()
# juego = FordManager(PANTALLA)

timer_1s = pygame.USEREVENT + 0
pygame.time.set_timer(timer_1s,1000)

main_menu = FormMenu("menu", screen, x=0, y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=BLACK, imagen_background=r"buttoms\window\0.png", color_border=BLACK, active=True)
form_niveles = FormNiveles(name="niveles",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=BLACK,imagen_background=r"buttoms\window\0.png",color_border=BLACK,active=False)
form_pausa = FormPausa(name="pause", master_surface= screen, x= 320, y= 125, w=600, h=450, color_background=None, imagen_background=r"buttoms\window\0.png", color_border=None, active=False)
form_options = FormOpciones(name="opciones",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=BLACK,imagen_background=r"buttoms\window\0.png",color_border=BLACK,active=False, main_menu=True)
form_puntuaciones = FormPuntuaciones(name="puntuaciones", master_surface=screen, x=0,y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=BLACK, imagen_background=r"buttoms\window\0.png", color_border=None, active=False)
level_1 = FormGameLevel("level_1", master_surface=screen, x=0, y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=None, imagen_background=None, color_border=None, active=False)
level_2 = FormGameLevel("level_2", master_surface=screen, x=0, y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=None, imagen_background=None, color_border=None, active=False)
level_3 = FormGameLevel("level_3", master_surface=screen, x=0, y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=None, imagen_background=None, color_border=None, active=False)

form_lose= FormLose(name="lose",master_surface = screen,x=320,y=125,w=600,h=450,imagen_background=r"buttoms\window\0.png",color_background=None ,color_border=BLACK,active=False)
form_win= FormWin(name="win",master_surface = screen,x=320,y=125,w=600,h=450,imagen_background=r"buttoms\window\0.png",color_background=None ,color_border=BLACK,active=False)
# form_game_L1 = FormGameLevel1(name="nivel_1",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,color_border=None,active=False)
# form_game_L2 = FormGameLevel2(name="nivel_2",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,color_border=None,active=False)
# form_game_L3 = FormGameLevel3(name="nivel_3",master_surface = screen,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,color_border=None,active=False)

running =True
while running:     
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    active_level_name = FormGameLevel.get_name_level()
    # if active_level_name is not None:
    # print(f"{active_level_name}")

    # if active_level_name == "level_1" or active_level_name == "level_2" or active_level_name == "level_3": #!
    #     form_pausa = FormPausa(name="pause", master_surface= screen, x= 320, y= 125, w=600, h=450, color_background=None, imagen_background=r"buttoms\window\0.png", color_border=None, active=False, level= active_level_name)

    
    aux_form_active = Form.get_active()
    # print(aux_form_active.name)
    if(aux_form_active != None):
        aux_form_active.update(event_list,keys,music,delta_ms,timer_1s)
        aux_form_active.draw(screen)
    # print(aux_form_active)
    pygame.display.flip()