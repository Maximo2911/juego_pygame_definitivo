from funtions import crear_lista_rutas_relativas
import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y, frame_rate_ms) -> None:
        self.duck = crear_lista_rutas_relativas("sprites/duck/")
        self.hurt = crear_lista_rutas_relativas("sprites/hurt/")
        self.idle = crear_lista_rutas_relativas("sprites/idle/")
        self.jump = crear_lista_rutas_relativas("sprites/jump/")
        self.ladder = crear_lista_rutas_relativas("sprites/ladder/")
        self.run = crear_lista_rutas_relativas("sprites/run/")
        self.run_shoot = crear_lista_rutas_relativas("sprites/run_shoot/")
        self.shoot = crear_lista_rutas_relativas("sprites/shoot/")
        self.slide = crear_lista_rutas_relativas("sprites/slide/")
        self.spin = crear_lista_rutas_relativas("sprites/spin/")

        #animacion
        self.animation = self.idle
        self.frame = 0
        self.playing_sequence = False
        
        #rectangulo
        self.image = pygame.image.load(self.animation[self.frame])
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
        self.rect.x = x
        self.rect.y = y

        #dar vuelta
        self.flipped = True

        #Manejos de tiempo
        self.time_animations = 0
        self.time_events = 0
        self.frame_rate_ms = frame_rate_ms

        # Accion esperar
        self.playing_idle = False

        # Dar vuelta imagen
        self.flipped = False

    def do_animations(self, delta_ms):
        if self.playing_sequence:
            self.time_animations += delta_ms
            if self.time_animations >= self.frame_rate_ms:
                self.time_animations -= self.frame_rate_ms
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0
                    self.playing_sequence = False
        else:
            self.idle_action()

    def idle_action(self):
        self.animation = self.idle
        if self.frame < len(self.animation) - 1:
            self.frame += 1
        else:
            self.frame = 0
            

    def do_movement(self,delta_ms):
        if self.playing_sequence:
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.playing_sequence = False

    def update(self,delta_ms, keys):
        self.events(keys)
        self.do_animations(delta_ms)
        self.do_movement(delta_ms)

    #Cambiar x ó y
    def change_x(self,delta_x):
        self.rect.x += delta_x
        # self.collition_rect.x += delta_x
        # self.ground_collition_rect.x += delta_x
    def change_y(self,delta_y):
        self.rect.y += delta_y
        # self.collition_rect.y += delta_y
        # self.ground_collition_rect.y += delta_y

    def draw(self, screen):
        if self.flipped:
            self.image = pygame.image.load(self.animation[self.frame])
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = pygame.image.load(self.animation[self.frame])                                  #! CHECK         
        screen.blit(self.image,self.rect)
    

    def events(self, keys):
        if keys[K_RIGHT] and not keys[K_SPACE] and not keys[K_LEFT]: #Correr derecha
            # self.run_action("RUN", 5, 0)
            self.flipped = False
            self.animation = self.run
            self.move_x = 5
            self.move_y = 0
            self.playing_sequence = True
            
        if keys[K_LEFT] and not keys[K_SPACE] and not keys[K_RIGHT]: # Correr izquierda
            # self.run_action("RUN_LEFT",-5, 0)
            self.flipped = True
            self.animation = self.run
            self.move_x = -5
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_LEFT] and keys[K_x] and not keys[K_SPACE]: # Disparo corriendo izquierda
            # self.run_shoot_action(-1, 0)
            self.animation = self.run_shoot
            self.move_x = -1
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_RIGHT] and keys[K_x] and not keys[K_SPACE]: # Disparo corriendo derecha
            # self.run_shoot_action(1, 0)
            self.animation = self.run_shoot
            self.move_x = 1
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_x] and not keys[K_SPACE] and not keys[K_RIGHT] and not keys[K_LEFT]: # Disparo
            # self.shoot_action(0, 0)
            self.animation = self.shoot
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_LEFT] and keys[K_SPACE]: # Salto izquierda
            # self.jump_action(-5, -10)
            self.animation = self.jump
            self.move_x = -5
            self.move_y = -10
            self.playing_sequence = True

        if keys[K_RIGHT] and keys[K_SPACE]: # Salto derecha
            # self.jump_action(5, -10)
            self.animation = self.jump
            self.move_x = 5
            self.move_y = -10
            self.playing_sequence = True

        if keys[K_SPACE] and not keys[K_DOWN] and not keys[K_RIGHT] and not keys[K_LEFT]: # Salto 
            # self.jump_action(0, -10)
            self.animation = self.jump
            self.move_x = 0
            self.move_y = -10
            self.playing_sequence = True

        if keys[K_DOWN] and keys[K_RIGHT] and not keys[K_UP] and not keys[K_LEFT]: # Deslizarce derecha
            # self.slide_action(3, 0)
            self.animation = self.slide
            self.move_x = 3
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_DOWN] and keys[K_LEFT] and not keys[K_UP] and not keys[K_RIGHT]: # Deslizarce izquierda
            # self.slide_action(-3, 0)
            self.animation = self.slide
            self.move_x = -3
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_DOWN] and not keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE]: # Agacharse
            # self.duck_action(0, 0)
            self.animation = self.duck
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True

        if keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE]: #Subir escaleras
            #self.ladder_action(0, -10)
            self.animation = self.ladder
            self.move_x = 0
            self.move_y = -10
            self.playing_sequence = True

        if keys[K_w]: # Vueltita loca
            # self.spin_action(0, 0)
            self.animation = self.spin
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True

        if not keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE] and not keys[K_DOWN] and not keys[K_x]: # Estatico
            self.animation = self.idle
            
    