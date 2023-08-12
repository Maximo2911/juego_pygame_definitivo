from player import *
from constantes import *
from auxiliar import Auxiliar
import math
import pygame
from boss import *

class Bullet():
    
    def __init__(self,x_init,y_init,speed,frame_rate_ms,move_rate_ms,direction, width=5,height=5) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0

        # secuencia
        self.bullet_action = Auxiliar.getSurfaceFromSeparateFiles("animated_objects/bullet/{0}.png",0,4,flip=False,scale=2)
        self.bullet_action_left = Auxiliar.getSurfaceFromSeparateFiles("animated_objects/bullet/{0}.png",0,4,flip=True,scale=2)

        self.direction = direction

        #animacion
        if self.direction == "RIGHT":
            self.animation = self.bullet_action
        else:
            self.animation = self.bullet_action_left
       
        self.frame = 0

        #creacion de al bala | movimiento | rectagulo(HITBOX)
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.rect.x = x_init
        self.rect.y = y_init

        self.move_x = speed
        self.move_y = 0

        #refresco de movimiento mediante frames
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        
        #hitbox bullet
        self.collition_rect = pygame.Rect(self.rect.x + self.rect.width/2, y_init + 8, self.rect.width*0.5, self.rect.height*0.5)
        self.is_active = True 



    def change_x (self,delta_x):
        if  self.direction == "LEFT":
            self.x = self.x - delta_x
            self.rect.x = int(self.x)
        
            self.collition_rect.x = int(self.x)
            self.animation = self.bullet_action_left
        else:
            self.x = self.x + delta_x
            self.rect.x = int(self.x)
            self.collition_rect.x = int(self.x)
            self.animation = self.bullet_action


    def change_y(self):
        # self.y = self.y + delta_y
        self.rect.y = int(self.move_y)

    def do_movement(self,delta_ms,plataform_list,enemy_list, player):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            # self.check_impact(plataform_list,enemy_list, player)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0
            
    def check_impact(self,plataform_list,enemy_list, boss, music):
        if self.rect.left > 0 and self.rect.right < ANCHO_PANTALLA: 
            for aux_enemy in enemy_list:
                # if self.collition_rect.colliderect(bullet.collition_rect)
                if(self.is_active and self.collition_rect.colliderect(aux_enemy.collition_rect)):
                    print("IMPACTO ENEMY")
                    self.is_active = False
            if boss != None:
                if(self.is_active and self.collition_rect.colliderect(boss.collition_rect)):
                    print("IMPACTO BOSS")
                    self.is_active = False
            for plataform in plataform_list:
                if(self.is_active and self.collition_rect.colliderect(plataform.collition_rect)):
                    print("IMPACTO PLATAFORM")
                    self.is_active = False
        else:
            self.is_active = False
                
    def update(self,delta_ms,plataform_list,enemy_list, player, music,boss=None):
        self.do_movement(delta_ms,plataform_list,enemy_list, player)
        self.do_animation(delta_ms) 
        self.check_impact(plataform_list, enemy_list, boss, music) #!

    def draw(self,screen):
        if self.is_active:
            if DEBUG:
                pygame.draw.rect(screen,color=(0,255 ,0),rect=self.collition_rect)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
