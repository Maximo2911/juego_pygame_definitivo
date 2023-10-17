import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget


class FormNiveles(Form):
    """
    Formulario de la seleccion de nivel
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master=self,x=ANCHO_PANTALLA//2-100,y=20,w=200,h=50,color_background=None,color_border=None,image_background=None,text="NIVELES",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=380,y=200,w=100,h=350,color_background=None,color_border=None,image_background=r"buttoms\level_one\1.png",on_click=self.on_click_boton_nivel,on_click_param="level_1",text="1",font="Anonymus Pro",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=ANCHO_PANTALLA//2- 55,y=200,w=100,h=350,color_background=None,color_border=None,image_background=r"buttoms\level_two\1.png",on_click=self.on_click_boton_nivel,on_click_param="level_2",text="2",font="Anonymus Pro",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=780,y=200,w=100,h=350,color_background=None,color_border=None,image_background=r"buttoms\level_three\1.png",on_click=self.on_click_boton_nivel,on_click_param="level_3",text="3",font="Anonymus Pro",font_size=30,font_color=WHITE)
        
        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3]

    def update(self, lista_eventos, keys, music, delta_ms, timer_1s):
        """
        Este metodo se encarga de actualizar el los distintos widget
        Parametros: recibe una lista de eventos
        """
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("menu")

    def on_click_boton_nivel(self,parametro):
        """
        Este metodo se encarga de resetear el nivel y activar el pasado por parametro y 
        tambien cambiar el parametro donde van a trabajar de los formularios de pausa, you_win y you_lose
        """
        # self.forms_dict[parametro].resetear()
        self.set_active(parametro)
        # self.forms_dict["pausa"].cambiar_nivel(parametro)
        # self.forms_dict["you_win"].cambiar_nivel(parametro)
        # self.forms_dict["you_lose"].cambiar_nivel(parametro)

    def draw(self, master_surface): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()