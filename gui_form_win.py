from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
import sys
from gui_form_levels import FormGameLevel
class FormWin(Form):
    """
    Formulario que aparece cuando el jugador gana el nivel
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master=self,x=180,y=130,w=250,h=50,color_background=None,color_border=None,image_background=None,text="NIVEL COMPLETADO",font="IMPACT",font_size=30,font_color=WHITE)

        self.boton1 = Button(master=self,x=195,y=170,w=200,h=70,color_background=None,color_border=None,image_background=None ,on_click=self.cambiar_nivel,on_click_param="level_1",text="Siguiente Nivel ->",font="8 BIT WONDER NOMINAL",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=205,y=220,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_house\0.png",on_click=self.on_click_boton1,on_click_param="menu",text=None)
        self.boton3 = Button(master=self,x=290,y=220,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_quit\0.png" ,on_click=self.exit_game,on_click_param="niveles",text=None)
        
        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        """
        Este metodo se encarga de obtener un parametro y pasarlo a otro metodo
        Parametro: un str que representa la clave del formulario
        """
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        """
        Este metodo se encarga de resetear el nivel correspondiente y activar el nuevo dependiendo del parametro
        Parametro: recibe un str que representa la clave del formulario a activar
        """
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active(parametro)

    def cambiar_nivel(self,parametro):
        """
        Este metodo se encarga de cambiar el nivel del parametro donde se va a ejecutar este formulario
        Parametro: recibe un str que representa el nivel actual donde trabajara el formulario
        """
        # self.boton1.on_click_param = parametro
        nivel_actual = FormGameLevel.get_name_level()

        print(nivel_actual)
        match nivel_actual:
            case "level_1":
                self.boton1.on_click_param = "level_2"
                self.set_active("level_2")
            case "level_2":
                self.boton1.on_click_param = "level_3"
                self.set_active("level_3")
            case "level_3":
                self.boton1._text = ""

        
    def update(self, lista_eventos,sonidos,delta_ms,keys,timer_1s):
        """
        Este metodo se encarga de actualizar el los distintos widget
        Parametros: recibe una lista de eventos
        """
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        
    def draw(self, master_surface): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

    def exit_game(self,none):
        sys.exit()