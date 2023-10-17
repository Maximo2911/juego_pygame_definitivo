import pygame
from constantes import *
from pygame.locals import *
# from gui_form_levels import FormGameLevel

class Form():
    forms_dict = {}
    active_level = None  # Variable para almacenar la instancia activa de FormGameLevel
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.imagen_background = imagen_background

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active

        if self.imagen_background != None:
            self.imagen_background = pygame.image.load(imagen_background)
            self.imagen_background = pygame.transform.scale(self.imagen_background,(self.w,self.h)).convert_alpha()
            self.surface = self.imagen_background
        elif(self.color_background != None):
            self.surface.fill(self.color_background)
    
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    # @staticmethod
    # def get_name_level():
    #     # Verifica si la instancia activa de FormGameLevel está almacenada y si está activa
    #     if Form.active_level and Form.active_level.active:
    #         return Form.active_level.name
    #     return None

    @staticmethod
    def get_active():
        for aux_form in Form.forms_dict.values():
            if(aux_form.active):
                # if isinstance(aux_form, FormGameLevel):
                #     # Almacena la instancia activa de FormGameLevel
                #     Form.active_level = aux_form
                return aux_form
        return None
    
    def render(self):
        pass

    def update(self,lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)
