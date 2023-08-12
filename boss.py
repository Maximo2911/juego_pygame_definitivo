from player import *
from constantes import *
from auxiliar import Auxiliar
from bullet_boss import BulletBoss
import math

class Boss():
    
    # def __init__(self,x,y, path, speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
    def __init__(self, x, y, p_scale, speed_attack,frame_move, frame_rate_ms) -> None:
        self.idle = Auxiliar.getSurfaceFromSeparateFiles("enemies/lizard/{0}.png",0,2,flip=False, scale=p_scale)
        self.shoot = Auxiliar.getSurfaceFromSeparateFiles("enemies/lizard_shoot/{0}.png",0 ,4,flip=False, scale=p_scale)
        self.death = Auxiliar.getSurfaceFromSeparateFiles("fx/big_explotion/{0}.png",from_index=0,quantity =18,flip=False, scale=1.25)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        
        self.animation = self.idle
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width,self.rect.height)
       
        self.speed = speed_attack

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_shoot = 0
        self.move_rate_ms = frame_move

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0           # en base al tiempo transcurrido general

        self.flag_impact = False
        self.flag_one_more = False

        self.flag_ready = True
        self.bullet_boss_list = []
        self.is_shooting = False
        

    def shooting(self, delta_ms, player, music):
        self.tiempo_transcurrido_shoot += delta_ms
        if(self.tiempo_transcurrido_shoot >= 2000):
            self.tiempo_transcurrido_shoot = 0
            self.animation = self.shoot
        if self.frame == 3 and self.animation == self.shoot:                                
            # print("SHOOTING")
            # self.is_shooting = True

            if self.flag_ready == True:
                bullet_boss = BulletBoss(x_init=self.rect.x, x_end=player.rect.x, y_init=self.rect.y + 35, y_end=self.rect.y, speed=5, frame_rate_ms=100, move_rate_ms=75, width=10, height=10)
                self.bullet_boss_list.append(bullet_boss)
                music.disparo_boss.play()
                self.flag_ready = False
                # print(bullet_boss)

    def recieve_shoot(self, bullet_list, music):
        for bullet in bullet_list:
            if bullet.collition_rect.colliderect(self.collition_rect):
            # if bullet.rect.x == self.rect.x:
                self.lives -= 1
                music.hit.play()
                if self.lives == 0:
                    self.flag_one_more = True
                    music.muerte_enemigo.play()


    def do_animation(self,delta_ms):
        # if self.is_shooting:
        #     self.animation = self.shoot
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
                    self.flag_ready = True
                    self.animation = self.idle
                    self.is_shooting = False

    def update(self,delta_ms,player, bullet_list, music):
        # self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms) 
        self.recieve_shoot(bullet_list, music)
        self.shooting(delta_ms, player, music)

    def draw(self,screen):
        if not self.flag_impact:
            if(DEBUG):
                pygame.draw.rect(screen,color=(128, 0, 255),rect=self.collition_rect)
                # pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
            
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    # def receive_shoot(self):
    #     self.lives -= 1
