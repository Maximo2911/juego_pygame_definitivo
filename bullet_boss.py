from player import *
from constantes import *
from auxiliar import Auxiliar
# from bullet import Bullet
import math

class BulletBoss():
    def __init__(self,x_init, x_end,y_init, y_end,speed,frame_rate_ms,move_rate_ms, width=5,height=5) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0

        # secuencia
        self.bullet_action = Auxiliar.getSurfaceFromSeparateFiles("enemies/fireball/{0}.png",0,4,flip=False,scale=2)
        self.frame = 0
        self.animation = self.bullet_action
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

        self.x_init = x_init
        self.x_end = x_end
        self.y_init = y_init
        self.y_end = y_end
        self.speed = speed
        self.angle = 0

    def change_x (self,delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)
        self.collition_rect.x = int(self.x)
        self.animation = self.bullet_action

    def change_y(self,delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)
        self.collition_rect.y = int(self.y)
        self.animation = self.bullet_action

    def do_movement(self,delta_ms,plataform_list, player, boss):
        self.angle = math.atan2(player.rect.y - boss.rect.y, player.rect.x - boss.rect.x) #Obtengo el angulo en radianes
        # print('El angulo engrados es:', int(self.angle*180/math.pi)) #! print grados

        self.move_x = math.cos(self.angle)*self.speed
        self.move_y = math.sin(self.angle)*self.speed
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_y(self.move_y)
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
            
    
    def check_impact(self,plataform_list, player, music):
        # if(self.is_active and self.rect.colliderect(player.rect)):
        #     print("IMPACTO PLAYER")
        #     player.receive_shoot()
        #     self.is_active = False
        if self.rect.left > 0 and self.rect.right < ANCHO_PANTALLA: 
            if(self.is_active and self.collition_rect.colliderect(player.collition_rect)):
                print("IMPACTO BOSS")
                music.hit.play()
                self.is_active = False
            for plataform in plataform_list:
                if(self.is_active and self.collition_rect.colliderect(plataform.collition_rect)):
                    print("IMPACTO PLATAFORM")
                    self.is_active = False
        else:
            self.is_active = False
                

    def update(self,delta_ms,plataform_list, player, boss, music):
        self.do_movement(delta_ms,plataform_list, player, boss)
        self.do_animation(delta_ms) 
        self.check_impact(plataform_list, player, music)

    def draw(self,screen):
        if self.is_active:
            if DEBUG:
                pygame.draw.rect(screen,color=(0,255 ,0),rect=self.collition_rect)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
