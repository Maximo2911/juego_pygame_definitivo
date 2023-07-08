import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    def __init__(self, x, y,width, height,  type=1):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("structures/{0}.png",1,11,flip=False,w=width,h=height)   #TODO CAMBIAR
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        

        # self.plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=0))      #! TIENE UNA CARPETA CON TODOS LAS ESTRUCTURAS
        # self.plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=1))
        # self.plataform_list.append(Plataform(x=500,y=500,width=50,height=50,type=2))   
        # self.plataform_list.append(Plataform(x=600,y=430,width=50,height=50,type=12))
        # self.plataform_list.append(Plataform(x=650,y=430,width=50,height=50,type=14))
        # self.plataform_list.append(Plataform(x=750,y=360,width=50,height=50,type=12))
        # self.plataform_list.append(Plataform(x=800,y=360,width=50,height=50,type=13))
        # self.plataform_list.append(Plataform(x=850,y=360,width=50,height=50,type=13))
        # self.plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=14))