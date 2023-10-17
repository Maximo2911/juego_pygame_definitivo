import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
import sys
from gui_form_levels import *

class FormPausa(Form):
    """
    Formulario de pausa que aparece cuando el jugador apreta 'Esc'
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active): #! level
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        # self.level = level #!
        # print(self.level)
        self.text1 = Widget(master=self,x=250,y=170,w=100,h=50,color_background=None,color_border=None,image_background=None,text="PAUSA",font="Bahnschrift",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=165,y=255,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_continue\0.png",on_click=self.click_continue,on_click_param= "level_1",text=None,font=None,font_size=None,font_color=None)
        # self.boton2 = Button(master=self,x=180,y=130,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Settings_BTN.png",on_click=self.on_click_boton1,on_click_param="pausa",text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=265,y=255,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_house\0.png",on_click=self.on_click_boton1,on_click_param="menu",text=None)
        self.boton3 = Button(master=self,x=365,y=255,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_quit\0.png",on_click=self.exit_game,on_click_param="salir",text=None,font=None,font_size=None,font_color=None)
        # self.reset = Button(master=self,x=250,y=370,w=100,h=50,color_background=None,color_border=None,image_background=None,on_click=self.on_click_reset,on_click_param="nivel_1",text="RESET",font="Consola",font_size=20,font_color=WHITE)
        
        # self.boton3 = Button(master=self,x=ANCHO_PANTALLA//2-100,y=380,w=200,h=50,color_background=None,color_border=None,image_background=r"buttoms\quit\0.png",on_click=self.on_click_boton2,on_click_param="salir",text="",font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        """
        Este metodo se encarga de obtener un parametro y pasarlo a otro metodo
        Parametro: un str que representa la clave del formulario
        """
        # nivel_actual = FormGameLevel.get_name_level()
        # if nivel_actual:
        #     print(f"Nivel actual: {nivel_actual}")
        #     self.boton1.on_click_param = nivel_actual
        #     self.set_active(nivel_actual)
        # else:
        print(f"Parámetro: {parametro}")
        self.set_active(parametro)

    def click_continue(self, parametro):
        """
        Este metodo se encarga de obtener el nombre del nivel actual y establecerlo como on_click_param del boton1
        """
        nivel_actual = FormGameLevel.get_name_level()
        self.boton1.on_click_param = nivel_actual
        self.set_active(nivel_actual)

    
    
    # def on_click_reset(self,parametro):
    #     # self.forms_dict[self.boton1.on_click_param].resetear()
    #     # self.set_active(parametro)
    #     nivel_actual = FormGameLevel.get_name_level()
    #     if nivel_actual:
    #         # Reiniciar el nivel
    #         self.forms_dict[nivel_actual].resetear()
    #         # Restablecer el temporizador del juego u otros estados relevantes
    #         self.forms_dict[nivel_actual].game_time = 60
    #         self.set_active(nivel_actual)

    def update(self, lista_eventos, keys, music, delta_ms, timer_1s):
        """
        Este metodo se encarga de actualizar el los distintos widget
        Parametros: recibe una lista de eventos
        """
        # print(FormGameLevel.get_name_level())
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    nivel_actual = FormGameLevel.get_name_level()
                    
                    print(f"Activando pausa. Nivel actual: {nivel_actual}")
                    self.set_active(nivel_actual)
                    
                # print(self.set_active(self.boton1.on_click_param))

    def exit_game(self,none):
        sys.exit()

    def draw(self, master_surface): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()