import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget

class FormPausa(Form):
    """
    Formulario de pausa que aparece cuando el jugador apreta 'Esc'
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master=self,x=400,y=150,w=100,h=50,color_background=None,color_border=None,image_background=None,text="PAUSA",font="consola",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=450,y=210,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_continue\0.png",on_click=self.on_click_boton1,on_click_param="salir",text=None,font=None,font_size=None,font_color=None)
        # self.boton2 = Button(master=self,x=180,y=130,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Settings_BTN.png",on_click=self.on_click_boton1,on_click_param="pausa",text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=550,y=210,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_quit\0.png",on_click=self.on_click_boton1,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=680,y=210,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_house\0.png",on_click=self.on_click_boton1,on_click_param="niveles",text=None)
        
        # self.boton3 = Button(master=self,x=ANCHO_PANTALLA//2-100,y=380,w=200,h=50,color_background=None,color_border=None,image_background=r"buttoms\quit\0.png",on_click=self.on_click_boton2,on_click_param="salir",text="",font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        """
        Este metodo se encarga de obtener un parametro y pasarlo a otro metodo
        Parametro: un str que representa la clave del formulario
        """
        self.set_active(parametro)
    

    def update(self, lista_eventos):
        """
        Este metodo se encarga de actualizar el los distintos widget
        Parametros: recibe una lista de eventos
        """
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active(self.boton1.on_click_param)

    def draw(self): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()