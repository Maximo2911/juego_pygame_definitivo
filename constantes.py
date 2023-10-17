import pygame as py

FPS = 60
ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 720
HITBOX_JUGADOR = (80, 80)
GROUND_LEVEL = 650

# platforms.py
GROUND_COLLIDE_H = 5 # Aprox Gravedad/2 + 1
SIDE_COLLIDE_W = 10
DEBUG = False

# Prueba nivel
LEVEL_ONE = True

COOLDOWN_DISPARO = 500 
COOLDOWN_JUMP = 1500

#====================[GUI]=========================
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
RUTA_IMAGEN = "backgrounds/desktop-wallpaper-dungeons-and-dragons-1920x1080-dd.png"


#mouse states
M_STATE_NORMAL = 1
M_STATE_HOVER = 2
M_STATE_CLICK = 3
M_BRIGHT_HOVER = 1
M_BRIGHT_CLICK = 2