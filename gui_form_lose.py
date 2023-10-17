from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
import sys
class FormLose(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)
        
        #self.text1 = Widget(master=self,x=25,y=60,w=250,h=50,color_background=None,color_border=None,image_background= None,text="GAME OVER",font="Bahnschrift",font_size=60,font_color=WHITE)
        self.text1 = Widget(master=self,x=225,y=170,w=175,h=50,color_background=None,color_border=None,image_background=None,text="GAME OVER",font="Bahnschrift",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=165,y=255,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_continue\0.png",on_click=self.on_click_reset,on_click_param="level_1",text=None,font=None,font_size=None,font_color=None)
        # self.boton2 = Button(master=self,x=180,y=130,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Settings_BTN.png",on_click=self.on_click_boton1,on_click_param="pausa",text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=265,y=255,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_house\0.png",on_click=self.on_click_boton1,on_click_param="menu",text=None)
        self.boton3 = Button(master=self,x=365,y=255,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_quit\0.png",on_click=self.exit_game,on_click_param="salir",text=None,font=None,font_size=None,font_color=None)
        
        # self.boton3 = Button(master=self,x=ANCHO_PANTALLA//2-100,y=380,w=200,h=50,color_background=None,color_border=None,image_background=r"buttoms\quit\0.png",on_click=self.on_click_boton2,on_click_param="salir",text="",font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
       
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active(parametro)

    def cambiar_nivel(self,parametro):
        self.boton1.on_click_param = parametro

    def update(self, lista_eventos,sonidos,delta_ms,keys,timer_1s):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
    
    def exit_game(self,none):
        sys.exit()

    def draw(self, master_surface): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()