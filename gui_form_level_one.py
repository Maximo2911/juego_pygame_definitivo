import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemies import Enemy
from platforms import Plataform
from background import Background
from money import Money
from bullet import Bullet
from gui_widget import Widget

class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background=None,color_border=None,active=False)
        self.name = name
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background

        # --- GAME WIDGETS ---
        # self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background=r"buttoms\mini_house",on_click=self.on_click_boton1,on_click_param="menu",text="BACK",font="Verdana",font_size=30,font_color=WHITE)
        # self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=WHITE)
        self.widget_list = []
        self.boton1 = Button(master=self,x=50,y=0,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_continue\0.png",on_click=self.on_click_boton1,on_click_param="pause",text=None,font=None,font_size=None,font_color=None)
        self.widget_list.append(self.boton1)

        # --- GAME ELEMENTS --- 
        #Seteo jugador a esta posicion
        self.jugador = Player(250, 600, frame_rate_ms = 250, gravity = 5.5, jump_power = 12.5, jump_height = 150)             #En frame_rate_ms = 1000 se rompe pero imagen bien

        self.static_background_back = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA,path="backgrounds/back.png")

        self.plataform_list = []
        self.plataform_list.append(Plataform(x=550,y=550,width=50,height=50,type=5))
        self.plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=5))
        self.plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=5))
        self.plataform_list.append(Plataform(x=100,y=100,width=50,height=50,type=5))
        self.plataform_list.append(Plataform(x=150,y=100,width=50,height=50,type=5))
        self.plataform_list.append(Plataform(x=150,y=200,width=50,height=50,type=10))
        self.plataform_list.append(Plataform(x=100,y=150,width=50,height=50,type=9))


        self.money_list = []
        self.money_list.append(Money(200, 80, 100))
        self.money_list.append(Money(850, 550, 100))
        self.money_list.append(Money(825, 550, 100))

        # boss = Boss(900, 380, 5, 2, 25, 250)

        self.enemy_list = []
        # enemy_list.append(Enemy(x=150,y=600,path="enemies/skeleton/{0}.png",from_index=0,quantity=8,p_scale=1.7,speed_move=5, frame_move=50,frame_rate_ms=100, gravity=5.5, x_init=100, x_end=300))
        self.enemy_list.append(Enemy(x=150,y=300,path="enemies/bat/{0}.png",from_index=0,quantity=5,p_scale=1.7,speed_move=5, frame_move=50,frame_rate_ms=100, gravity=None, x_init=250, x_end=500))

        # enemy_list.append(Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))

        self.plataform_list.append(Plataform(x=0,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=100,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=200,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=300,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=400,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=500,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=600,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=700,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=800,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=900,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=1000,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=1100,y=650,width=100,height=150,type=8))
        self.plataform_list.append(Plataform(x=1200,y=650,width=100,height=150,type=8))

        self.bullets_list = self.jugador.bullet_list
        
        # _____________________________________________________________________________________________________________________________________________________________________________
        self.text1 = Widget(master=self,x=400,y=150,w=100,h=50,color_background=None,color_border=None,image_background=None,text="PAUSA",font="consola",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=450,y=210,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_continue\0.png",on_click=self.on_click_boton1,on_click_param="salir",text=None,font=None,font_size=None,font_color=None)
        # self.boton2 = Button(master=self,x=180,y=130,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Settings_BTN.png",on_click=self.on_click_boton1,on_click_param="pausa",text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=550,y=210,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_quit\0.png",on_click=self.on_click_boton1,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=680,y=210,w=70,h=70,color_background=None,color_border=None,image_background=r"buttoms\mini_house\0.png",on_click=self.on_click_boton1,on_click_param="niveles",text=None)
        
        # self.boton3 = Button(master=self,x=ANCHO_PANTALLA//2-100,y=380,w=200,h=50,color_background=None,color_border=None,image_background=r"buttoms\quit\0.png",on_click=self.on_click_boton2,on_click_param="salir",text="",font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3]
        # _____________________________________________________________________________________________________________________________________________________________________________


    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms, musica):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)
        for enemy in self.enemy_list:
            if enemy.flag_impact:
                self.enemy_list.remove(enemy)
            enemy.update(delta_ms, self.plataform_list, self.bullets_list, musica) #! ver musica

        for money in self.money_list:
            if money.flag_collition:
                self.money_list.remove(money)
            money.update(delta_ms, self.jugador, musica) #! ver musica
        if len(self.money_list) == 0:
            print("HAS GANADO")
            musica.victoria.play()
        
        self.jugador.update(delta_ms, keys, self.plataform_list, self.enemy_list, musica) #! ver musica

        for bullet in self.bullets_list:
            if not bullet.is_active:
                self.bullets_list.remove(bullet)
            bullet.update(delta_ms,self.plataform_list, self.enemy_list, self.jugador, musica) #! ver musica


        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    self.set_active("pausa")
                    print("PAUSEEEEEEEEEE")

    def draw(self, master_surface): 
        super().draw()
        self.static_background_back.draw(master_surface)

        for plataforma in self.plataform_list:
            plataforma.draw(master_surface)

        for enemy in self.enemy_list:
            enemy.draw(master_surface)
    
        for money in self.money_list:
            money.draw(master_surface)

        for bullet in self.bullets_list:
            bullet.draw(master_surface)
        self.jugador.draw(master_surface)

    def resetear(self):
        """
        Este metodo se encarga de crear nuevamente el formulario, con los mismos atributos
        """
        self.__init__(name = self.name, master_surface = self.master_surface)