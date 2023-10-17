from player import *
from constantes import *
from auxiliar import Auxiliar
from bullet import *
class Enemy():
    
    # def __init__(self,x,y, path, speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
    def __init__(self, x, y, path, from_index, quantity, p_scale, speed_move,frame_move, frame_rate_ms, gravity, x_init, x_end) -> None:
        self.move = Auxiliar.getSurfaceFromSeparateFiles(path,from_index,quantity,flip=False, scale=p_scale)
        self.move_left = Auxiliar.getSurfaceFromSeparateFiles(path,from_index,quantity,flip=True, scale=p_scale)

        self.death = Auxiliar.getSurfaceFromSeparateFiles("fx/big_explotion/{0}.png",from_index=0,quantity =19,flip=False, scale=1.25)
        # self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,flip=True,scale=p_scale)
        # self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,scale=p_scale)
        # self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,flip=True,scale=p_scale)
        # self.duck = Auxiliar.getSurfaceFromSeparateFiles("sprites/duck/{0}.png",0,3,flip=False,scale=1.5)

        self.contador = 0
        self.frame = 0
        self.lives = 1
        self.move_x = 0
        self.move_y = 0
        
        self.gravity = gravity
        self.animation = self.move
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = frame_move

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general

        self.speed_walk = speed_move
        self.flag_impact = False
        self.flag_one_more = False

        self.x_init = x_init
        self.x_end = x_end
        self.flag_first_touch = True


    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        if not self.flag_one_more:
            
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0
                
                if self.gravity != 0:
                    if(not self.is_on_plataform(plataform_list)):
                        if(self.move_y == 0):
                            self.is_fall = True
                            self.change_y(self.gravity)
                    else:
                        self.is_fall = False
                        self.change_x(self.move_x)
                        if self.rect.x == self.x_init:
                            #print("X_INITTTTTTTTTTTTT") #!
                            self.move_x = self.speed_walk
                            self.animation = self.move
                            self.flag_first_touch = False
                        elif self.rect.x == self.x_end:
                            #print("X_ENDDDDDDDDDDDDDDD")#!
                            self.move_x = -self.speed_walk
                            self.animation = self.move_left
                            self.flag_first_touch = False
                        else:
                            if self.flag_first_touch:
                                self.move_x = self.speed_walk
                else:
                    self.change_y(self.move_y)
                    if self.rect.y == self.x_init:
                        #print("X_INITTTTTTTTTTTTT")#!
                        self.move_y = self.speed_walk
                        self.animation = self.move
                        self.flag_first_touch = False
                    elif self.rect.y == self.x_end:
                        #print("X_ENDDDDDDDDDDDDDDD")#!
                        self.move_y = -self.speed_walk
                        self.animation = self.move_left
                        self.flag_first_touch = False
                    else:
                        if self.flag_first_touch:
                            self.move_y = self.speed_walk
                    #print(f"{self.rect} == {self.x_init}")

                    # if self.contador <= 50:
                    #     self.move_x = -self.speed_walk
                    #     self.animation = self.move_left
                    #     self.contador += 1 
                    # elif self.contador <= 100:
                    #     self.move_x = self.speed_walk
                    #     self.animation = self.move
                    #     self.contador += 1
                    # else:
                    #     self.contador = 0
        
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          


    def recieve_shoot(self, bullet_list, musica):
        for bullet in bullet_list:
            if bullet.collition_rect.colliderect(self.collition_rect):
            # if bullet.rect.x == self.rect.x:
                self.flag_one_more = True
                musica.muerte.play()
                

                # self.flag_impact = True
            
            # if self.rect.x == bullet.rect.x:
            #     self.flag_impact = True

    # def receive_shoot(self):
    #     retorno = False
    #     if 
    def do_animation(self,delta_ms):
        if self.flag_one_more:
            self.animation = self.death
            self.frame_rate_ms = 25
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                    #print(self.frame)
                else: 
                    self.frame = 0
                    self.flag_impact = True
        else:
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                    #print(self.frame)
                else: 
                    self.frame = 0

    def update(self,delta_ms,plataform_list, bullet_list, musica):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms) 
        self.recieve_shoot(bullet_list, musica)

    def draw(self,screen):
        if not self.flag_impact:
            if(DEBUG):
                pygame.draw.rect(screen,color=(128, 0, 255),rect=self.collition_rect)
                pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    # def receive_shoot(self):
    #     self.lives -= 1
