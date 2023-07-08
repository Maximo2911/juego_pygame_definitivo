from funtions import crear_lista_rutas_relativas
import pygame
from pygame.locals import *
from auxiliar import *
from constantes import *
import math



class Player:
    def __init__(self, x, y, frame_rate_ms, gravity, jump_power, jump_height) -> None:

        
        # self.duck = crear_lista_rutas_relativas("sprites/duck/")
        # self.hurt = crear_lista_rutas_relativas("sprites/hurt/")
        # self.idle = crear_lista_rutas_relativas("sprites/idle/")
        # self.jump = crear_lista_rutas_relativas("sprites/jump/")
        # self.ladder = crear_lista_rutas_relativas("sprites/ladder/")
        # self.run = crear_lista_rutas_relativas("sprites/run/")
        # self.run_shoot = crear_lista_rutas_relativas("sprites/run_shoot/")
        # self.shoot = crear_lista_rutas_relativas("sprites/shoot/")
        # self.slide = crear_lista_rutas_relativas("sprites/slide/")
        # self.spin = crear_lista_rutas_relativas("sprites/spin/")

        # Auxiliar.getSurfaceFromSeparateFiles("sprites/duck/{0}.png",0,3,flip=False,scale=1


        self.duck = Auxiliar.getSurfaceFromSeparateFiles("sprites/duck/{0}.png",0,3,flip=False,scale=1.5)
        self.duck_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/duck/{0}.png",0,3,flip=True,scale=1.5)
        self.hurt = Auxiliar.getSurfaceFromSeparateFiles("sprites/hurt/{0}.png",0,2,flip=False,scale=1.5)
        self.hurt_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/hurt/{0}.png",0,2,flip=True,scale=1.5)
        self.idle = Auxiliar.getSurfaceFromSeparateFiles("sprites/idle/{0}.png",0,6,flip=False,scale=1.5)
        self.idle_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/idle/{0}.png",0,6,flip=True,scale=1.5)
        self.jump = Auxiliar.getSurfaceFromSeparateFiles("sprites/jump/{0}.png",0,2,flip=False,scale=1.5)
        self.jump_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/jump/{0}.png",0,2,flip=True,scale=1.5)
        self.ladder = Auxiliar.getSurfaceFromSeparateFiles("sprites/ladder/{0}.png",0,4,flip=False,scale=1.5)
        # self.ladder_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/ladder/{0}.png",0,4,flip=True,scale=1.5)
        self.run = Auxiliar.getSurfaceFromSeparateFiles("sprites/run/{0}.png",0,6,flip=False,scale=1.5)
        self.run_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/run/{0}.png",0,6,flip=True,scale=1.5)
        self.run_shoot = Auxiliar.getSurfaceFromSeparateFiles("sprites/run_shoot/{0}.png",0,6,flip=False,scale=1.5)
        self.run_shoot_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/run_shoot/{0}.png",0,6,flip=True,scale=1.5)
        self.shoot = Auxiliar.getSurfaceFromSeparateFiles("sprites/shoot/{0}.png",0,3,flip=False,scale=1.5)
        self.shoot_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/shoot/{0}.png",0,3,flip=True,scale=1.5)
        self.slide = Auxiliar.getSurfaceFromSeparateFiles("sprites/slide/{0}.png",0,4,flip=False,scale=1.5)
        self.slide_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/slide/{0}.png",0,4,flip=True,scale=1.5)
        self.spin = Auxiliar.getSurfaceFromSeparateFiles("sprites/spin/{0}.png",0,8,flip=False,scale=1.5)
        self.spin_left = Auxiliar.getSurfaceFromSeparateFiles("sprites/spin/{0}.png",0,8,flip=True,scale=1.5)

        #animacion
        self.animation = self.idle
        self.frame = 0
        
        
        #rectangulo
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
        self.rect.x = x
        self.rect.y = y

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

        # Variables relacionadas con el salto
        self.gravity = gravity
        self.jump_power = jump_power
        self.jump_height = jump_height
        self.y_start_jump = 0
        self.is_fall = False
        self.flag_jump = False
        self.flag_repeat = False 
        self.is_jump = False


        
       


        # Hitbox personaje                | Coordenadas rectangulo |    ANCHO        |      ALTO
        self.collition_rect = pygame.Rect(x + self.rect.width/8, y, self.rect.width/1.2, self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)           # Se crea otro rectangulo
        self.ground_collition_rect.height = GROUND_COLLIDE_H                    # Ajusta la altura del nuevo objeto
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H  # Coordenadas de el nuevo rect
        
        
        # self.ground_collition_rect.width = SIDE_COLLIDE_W
        # self.ground_collition_rect.x = x + self.rect.width - SIDE_COLLIDE_W

    def do_animations(self, delta_ms):
        
            self.time_animations += delta_ms
            if self.time_animations >= self.frame_rate_ms:
                self.time_animations = 0
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0
                    


    def do_movement(self, delta_ms, plataform_list):
        
            # self.time_animations += delta_ms
            # if(self.time_animations >= self.frame_rate_ms):
            #     self.time_animations = 0
            self.flag_repeat = True                                        #self.jumping
            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
                self.flag_repeat = False
                

          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if not self.is_on_plataform(plataform_list):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if self.flag_jump: 
                    self.flag_jump = False
                    self.is_fall = False
                    self.is_jump = False
                    self.jumping = False
            


    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if self.ground_collition_rect.bottom >= GROUND_LEVEL:                       
            retorno = True     
        else:
            for plataforma in plataform_list:
                if self.ground_collition_rect.colliderect(plataforma.ground_collition_rect):
                    retorno = True
                    break       
        return retorno    


    def update(self,delta_ms, keys, plataform_list):
        self.events(keys, plataform_list)
        self.do_animations(delta_ms)
        self.do_movement(delta_ms, plataform_list)
        

    #Cambiar x ó y
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x
    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def draw(self, screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)                                #! CHECK         
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
    #====================================================
    def idle_action(self):
        if not self.is_jump:
            if self.animation != self.idle and self.animation != self.idle_left:
                self.frame = 0
                if self.flipped == True:
                    self.animation = self.idle_left
                else:
                    self.animation = self.idle
            self.move_x = 0
            self.move_y = 0
            
            # print("IDLING")

    
    def run_sequence(self, direction):
        if not self.is_jump:
        
            if self.animation != self.run and self.animation != self.run_left:
                self.frame = 0
                if direction == "RIGHT":
                    self.animation = self.run
                    self.flipped = False
                if direction == "LEFT":
                    self.animation = self.run_left
                    self.flipped = True
            if direction == "RIGHT" and self.rect.x < 1240:
                self.move_x = 5
                self.move_y = 0
                
            elif direction == "LEFT" and self.rect.x > 0:
                self.move_x = -5
                self.move_y = 0
                
            # print("RUNNING")


    def shoot_sequence(self):
        if not self.is_jump:
        
            if self.animation != self.shoot and self.animation != self.shoot_left:
                self.frame = 0
                if self.flipped == True:
                    self.animation = self.shoot_left
                else:
                    self.animation = self.shoot
            self.move_x = 0
            self.move_y = 0
            
            # print("SHOOTING")
           

    def run_shoot_sequence(self, direction):
        if not self.is_jump:
        
            if self.animation != self.run_shoot and self.animation != self.run_shoot_left:
                self.frame = 0
                if self.flipped == True:
                    self.animation = self.run_shoot_left
                else:
                    self.animation = self.run_shoot
            if direction == "RIGHT" and self.rect.x < 1240:
                self.move_x = 1
                self.move_y = 0
                
            elif direction == "LEFT" and self.rect.x > 0:
                self.move_x = -1
                self.move_y = 0
                
            # print("RUN SHOOTING")

    # def jump_movement(self):



    def jump_sequence(self, direction, plataform_list):
        if self.is_on_plataform(plataform_list):
        
            if self.animation != self.jump and self.animation != self.jump_left:
                self.frame = 0
                if self.flipped:
                    self.animation = self.jump_left
                else:
                    self.animation = self.jump
            

            if self.rect.y > 0:
                if direction == "RIGHT":
                    if self.flag_repeat:
                        self.move_x = int(5 / 2)
                        self.move_y = -self.jump_power
                        

                elif direction == "LEFT":
                    if self.flag_repeat:
                        self.move_x = int(-5 / 2)
                        self.move_y = -self.jump_power
                        

                elif direction == "MIDDLE":
                    if self.flag_repeat:
                        self.move_x = 0
                        self.move_y = -self.jump_power
                        
            

            if not self.flag_jump:
                self.flag_jump = True
                self.is_jump = True
                self.y_start_jump = self.rect.y
                
            # print("JUMPING")


    def slide_sequence(self, direction):
        if not self.is_jump:
        
            if self.animation != self.slide and self.animation != self.slide_left:
                self.frame = 0
                if self.flipped == True:
                    self.animation = self.slide_left
                else:
                    self.animation = self.slide

            if direction == "RIGHT" and self.rect.x < 1240:
                self.move_x = 3
                self.move_y = 0
                
            elif direction == "LEFT" and self.rect.x > 0:
                self.move_x = -3
                self.move_y = 0
                
            # print("SLINDING")


    def duck_sequence(self):
        if not self.is_jump:
        
            if self.animation != self.duck and self.animation != self.duck_left:
                self.frame = 0
                if self.flipped == True:
                    self.animation = self.duck_left
                else:
                    self.animation = self.duck
            self.move_x = 0
            self.move_y = 0
            
            # print("DUCK")


    def ladder_sequence(self):
        if not self.is_jump:
        
            if self.animation != self.ladder:
                self.frame = 0
                self.animation = self.ladder
            if self.rect.y > 0:
                self.move_x = 0
                self.move_y = -10
                
            # print("LADDER")

    def events(self, keys, plataform_list):
        self.jumping = False
        self.sliding = False
        self.ducking = False
        self.shooting = False
        self.run_shooting = False
        self.running = False
        self.ladder_action = False

        if keys[K_RIGHT] and not keys[K_SPACE] and not keys[K_LEFT] and not keys[K_DOWN]: #Correr derecha
            self.run_sequence("RIGHT")
            
        if keys[K_LEFT] and not keys[K_SPACE] and not keys[K_RIGHT] and not keys[K_DOWN]: # Correr izquierda
            self.run_sequence("LEFT")

        if keys[K_LEFT] and keys[K_x] and not keys[K_SPACE] and not keys[K_DOWN]: # Disparo corriendo izquierda
            self.run_shoot_sequence("LEFT")

        if keys[K_RIGHT] and keys[K_x] and not keys[K_SPACE] and not keys[K_DOWN]: # Disparo corriendo derecha
            self.run_shoot_sequence("RIGHT")

        if keys[K_x] and not keys[K_SPACE] and not keys[K_RIGHT] and not keys[K_LEFT]: # Disparo
            self.shoot_sequence()

        if keys[K_LEFT] and keys[K_SPACE]: # Salto izquierda
            self.jump_sequence("LEFT", plataform_list)

        if keys[K_RIGHT] and keys[K_SPACE]: # Salto derecha
            self.jump_sequence("RIGHT", plataform_list)

        if keys[K_SPACE] and not keys[K_DOWN] and not keys[K_RIGHT] and not keys[K_LEFT]: # Salto 
            self.jump_sequence( "MIDDLE", plataform_list)

        if keys[K_DOWN] and keys[K_RIGHT] and not keys[K_UP] and not keys[K_LEFT]: # Deslizarce derecha
            self.slide_sequence("RIGHT")

        if keys[K_DOWN] and keys[K_LEFT] and not keys[K_UP] and not keys[K_RIGHT]: # Deslizarce izquierda
            self.slide_sequence("LEFT")

        if keys[K_DOWN] and not keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE]: # Agacharse
            self.duck_sequence()

        if keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE]: #Subir escaleras
            self.ladder_sequence()
            
        if keys[K_w]: # Vueltita loca
            self.animation = self.spin
            

        if not keys[K_UP] and not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_SPACE] and not keys[K_DOWN] and not keys[K_x] and not keys[K_w]: # Estatico
            self.idle_action()
            # print("IDLING")

# print(Auxiliar.method_scale_image("sprites/duck/{}", 0, 3, scale = 2))
# print(Auxiliar.getSurfaceFromSeparateFiles("sprites/duck/{0}.png",0,3,flip=False,scale=2))
