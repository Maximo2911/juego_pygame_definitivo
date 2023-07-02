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
        self.time_idle = 0
        # Accion esperar
        self.playing_idle = False

        # Dar vuelta imagen
        self.flipped = False

        #Variables acciones
        self.jumping = False
        self.sliding = False
        self.ducking = False
        self.shooting = False
        self.run_shooting = False
        self.running = False
        self.ladder_action = False

    def do_animations(self, delta_ms):
        if self.playing_sequence:
            self.time_animations += delta_ms
            if self.time_animations >= self.frame_rate_ms:
                self.time_animations = 0
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0
                    
                    self.playing_sequence = False

                    
                    
    

    def do_movement(self,delta_ms):
        if self.playing_sequence:
            # self.time_animations += delta_ms
            # if(self.time_animations >= self.frame_rate_ms):
            #     self.time_animations = 0
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
    


    #====================================================
    def idle_action(self):
        if self.jumping == False and self.sliding == False and self.shooting == False and self.ducking == False and self.run_shooting == False and self.ladder_action == False and self.running == False:
            if self.animation != self.idle:
                self.frame = 0
                self.animation = self.idle
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True
            print("IDLING")

            
        
    
    def run_sequence(self, direction):
        if self.jumping == False and self.sliding == False and self.ducking == False and self.shooting == False and self.run_shooting == False and self.ladder_action == False:
            self.running  = True
            if self.animation != self.run:
                self.frame = 0
                self.animation = self.run
            if direction == "RIGHT":
                self.flipped = False
                self.move_x = 5
                self.move_y = 0
                self.playing_sequence = True
            elif direction == "LEFT":
                self.flipped = True
                self.move_x = -5
                self.move_y = 0
                self.playing_sequence = True
            print("RUNNING")


    def shoot_sequence(self):
        if self.jumping == False and self.sliding == False and self.ducking == False and self.running == False and self.run_shooting  == False and self.ladder_action == False:
            self.shooting = True
            if self.animation != self.shoot:
                self.frame = 0
                self.animation = self.shoot
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True
            print("SHOOTING")

           

    def run_shoot_sequence(self, direction):
        if self.jumping == False and self.sliding == False and self.ducking == False and self.running == True and self.shooting  == False and self.ladder_action  == False:
            self.run_shooting_left  = True
            if self.animation != self.run_shoot:
                self.frame = 0
                self.animation = self.run_shoot
            if direction == "RIGHT":
                self.move_x = 1
                self.move_y = 0
                self.playing_sequence = True
            elif direction == "LEFT":
                self.move_x = -1
                self.move_y = 0
                self.playing_sequence = True
            print("RUN SHOOTING")


    def jump_sequence(self, direction):
        if self.sliding == False and self.ducking == False and self.running == False and self.ladder_action == False and self.shooting == False and self.run_shooting  == False:
            self.jumping = True
            if self.animation != self.jump:
                self.frame = 0
                self.animation = self.jump
            if direction == "RIGHT":
                self.move_x = 5
                self.move_y = -10
                self.playing_sequence = True
            elif direction == "LEFT":
                self.move_x = -5
                self.move_y = -10
                self.playing_sequence = True
            elif direction == "MIDDLE":
                self.move_x = 0
                self.move_y = -10
                self.playing_sequence = True
            print("JUMPING")


    def slide_sequence(self, direction):
        print("ENTRÉ")
        if self.jumping == False and self.ducking == False and self.running == False and self.ladder_action == False and self.shooting == False and self.run_shooting  == False:
            self.sliding = True
            if self.animation != self.slide:
                self.frame = 0
                self.animation = self.slide
            if direction == "RIGHT":
                self.move_x = 3
                self.move_y = 0
                self.playing_sequence = True
            elif direction == "LEFT":
                self.move_x = -3
                self.move_y = 0
                self.playing_sequence = True
            print("SLINDING")


    def duck_sequence(self):
        if self.jumping == False and self.sliding == False and self.running == False and self.ladder_action == False and self.shooting == False and self.run_shooting  == False:
            self.ducking = True
            if self.animation != self.duck:
                self.frame = 0
                self.animation = self.duck
            
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True
            print("DUCK")


    def ladder_sequence(self):
        if self.jumping == False and self.sliding == False and self.running == False and self.ducking == False and self.shooting == False and self.run_shooting  == False:
            self.ladder_action = True
            if self.animation != self.ladder:
                self.frame = 0
                self.animation = self.ladder
            self.move_x = 0
            self.move_y = -10
            self.playing_sequence = True
            print("LADDER")


    def events(self, keys):
        # self.idle_action(False)
        # self.jump_sequence(False, "-")
        # self.slide_sequence(False, "-")
        # self.duck_sequence(False)
        # self.shoot_sequence(False)
        # self.run_shoot_sequence(False, "-")
        # self.run_sequence(False, "-")
        # self.ladder_sequence(False)

        self.jumping = False
        self.sliding = False
        self.ducking = False
        self.shooting = False
        self.run_shooting = False
        self.running = False
        self.ladder_action = False
        if keys[K_RIGHT] and not keys[K_SPACE] and not keys[K_LEFT] and not keys[K_DOWN]: #Correr derecha
            self.run_sequence( "RIGHT")
            
        if keys[K_LEFT] and not keys[K_SPACE] and not keys[K_RIGHT] and not keys[K_DOWN]: # Correr izquierda
            self.run_sequence( "LEFT")

        if keys[K_LEFT] and keys[K_x] and not keys[K_SPACE] and not keys[K_DOWN]: # Disparo corriendo izquierda
            self.run_shoot_sequence( "LEFT")

        if keys[K_RIGHT] and keys[K_x] and not keys[K_SPACE] and not keys[K_DOWN]: # Disparo corriendo derecha
            self.run_shoot_sequence( "RIGHT")

        if keys[K_x] and not keys[K_SPACE] and not keys[K_RIGHT] and not keys[K_LEFT]: # Disparo
            self.shoot_sequence()

        if keys[K_LEFT] and keys[K_SPACE]: # Salto izquierda
            self.jump_sequence( "LEFT")

        if keys[K_RIGHT] and keys[K_SPACE]: # Salto derecha
            self.jump_sequence( "RIGHT")

        if keys[K_SPACE] and not keys[K_DOWN] and not keys[K_RIGHT] and not keys[K_LEFT]: # Salto 
            self.jump_sequence( "MIDDLE")

        if keys[K_DOWN] and keys[K_RIGHT] and not keys[K_UP] and not keys[K_LEFT]: # Deslizarce derecha
            self.slide_sequence( "RIGHT")
            print("HOLA")

        if keys[K_DOWN] and keys[K_LEFT] and not keys[K_UP] and not keys[K_RIGHT]: # Deslizarce izquierda
            self.slide_sequence( "LEFT")

        if keys[K_DOWN] and not keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE]: # Agacharse
            self.duck_sequence()

        if keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE]: #Subir escaleras
            self.ladder_sequence()
            
        if keys[K_w]: # Vueltita loca
            self.animation = self.spin
            self.move_x = 0
            self.move_y = 0
            self.playing_sequence = True

        if not keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE] and not keys[K_DOWN] and not keys[K_x] and not keys[K_w]: # Estatico
            self.idle_action()
            # print("IDLING")