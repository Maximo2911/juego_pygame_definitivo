import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_widget import Widget
from gui_progressbar import ProgressBar
from player import Player
from enemies import Enemy
from platforms import Plataform
from background import Background
from bullet import Bullet
from money import Money
import json
from auxiliar import Auxiliar
from money import Money
from boss import Boss

class FormGameLevel(Form):
    _last_known_level = None
    def __init__(self,name,master_surface,x=0,y=0,w=ANCHO_PANTALLA,h=ALTO_PANTALLA,color_background=None,imagen_background=None,color_border=None,active=False):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)
        self.name = name
        self.master_surface = master_surface
        self.dicc_level = Auxiliar.cargar_nivel("levels.json",name)
        self.player = self.player_instantiation()
        self.game_time = 60
        self.extra_time = 0
        # --- GUI WIDGET --- 
        # self.text1 = Widget(master=self,x=10,y=10,w=200,h=40,color_background=None,color_border=None,image_background=None,text="Lives:{0}".format(self.player.lives),font="8 BIT WONDER NOMINAL",font_size=25,font_color=WHITE)
        self.text1_image = Widget(master=self,x=110,y=10,w=35,h=35,color_background=None,color_border=None,image_background=r"buttoms\hearts\0.png",text=None,font=None,font_size=None,font_color=None)
        self.corazon2 = Widget(master=self,x=150,y=10,w=35,h=35,color_background=None,color_border=None,image_background=r"buttoms\hearts\0.png",text=None,font=None,font_size=None,font_color=None)
        self.corazon3 = Widget(master=self,x=190,y=10,w=35,h=35,color_background=None,color_border=None,image_background=r"buttoms\hearts\0.png",text=None,font=None,font_size=None,font_color=None)

        self.text2 = Widget(master=self,x=420,y=10,w=400,h=40,color_background=None,color_border=None,image_background=None,text="SCORE  {0}".format(str(self.player.score).zfill(6)),font="8 BIT WONDER NOMINAL",font_size=25,font_color=WHITE)
        self.text3 = Widget(master=self,x=850,y=10,w=270,h=40,color_background=None,color_border=None,image_background=None,text="TIME  {0}".format(self.game_time),font="8 BIT WONDER NOMINAL",font_size=25,font_color=WHITE)
        self.background = Widget(master=self,x=0,y=0,w=ANCHO_PANTALLA,h=50,color_background=BLACK,color_border=None,image_background=None,text=None,font=None,font_size=None,font_color=None)
        self.widget_list = [self.background,self.text1_image,self.text2,self.text3, self.corazon2, self.corazon3] #,self.text1_image,self.text1,self.text2,self.text3

        # --- GAME ELEMENTS --- 
        self.static_background = Background(x=0,y=0,width=ANCHO_PANTALLA,height=ALTO_PANTALLA-60,path=self.dicc_level["background"])
        self.money_list = self.money_instantiation()
        self.enemy_list = self.enemies_instantiation()
        self.plataform_list = self.platform_instantiation()
        if self.name == "level_3":
            self.boss = self.boss_instantiation()
            self.bullets_boss = self.boss.bullet_boss_list
        
        self.bullets_list = self.player.bullet_list

        #banderas
        self.flag_win = True

    def resetear(self):
        """
        Este metodo se encarga de crear nuevamente el formulario, con los mismos atributos
        """
        self.__init__(name = self.name, master_surface = self.master_surface)

    # @staticmethod #!
    # def get_name_level():
    #     last_level = []
    #     active_form = FormGameLevel.get_active()
    #     if isinstance(active_form, FormGameLevel):
    #         last_level.append(active_form.name)
    #         return active_form.name
    #     elif len(last_level) > 0 and active_form.name is None:
    #         return last_level[-1]

    @staticmethod
    def get_name_level():
        active_form = FormGameLevel.get_active()
        if isinstance(active_form, FormGameLevel):
            FormGameLevel._last_known_level = active_form.name
            return active_form.name
        else:
            return FormGameLevel._last_known_level or "level_1"

    def player_instantiation(self):
        #print(self.dicc_level["player"])  #{'pos': [[250, 600]], 'frame_rate_ms': 250, 'gravity': 5.5, 'jump_power': 12.5, 'jump_height': 150}
        
        position = self.dicc_level["player"]["pos"]
        x = position[0][0]
        y = position[0][1]
        frame_rate_ms = self.dicc_level["player"]["frame_rate_ms"]
        gravity = self.dicc_level["player"]["gravity"]
        jump_power = self.dicc_level["player"]["jump_power"]
        jump_height = self.dicc_level["player"]["jump_height"]

        player = Player(x, y, frame_rate_ms, gravity, jump_power, jump_height)
        return player     
    
    def boss_instantiation(self):

        position = self.dicc_level["boss"]["pos"]
        x = position[0][0]
        y = position[0][1]
        p_scale = self.dicc_level["boss"]["p_scale"]
        speed_attack = self.dicc_level["boss"]["speed_attack"]
        frame_move = self.dicc_level["boss"]["frame_move"]
        frame_rate_ms = self.dicc_level["boss"]["frame_rate_ms"]

        boss = Boss(x,y, p_scale, speed_attack, frame_move, frame_rate_ms)
        return boss
                
    def enemies_instantiation(self):
        """
        Este método se encarga de crear a los enemigos
        Retorna: una lista de objetos de enemigos
        """
        aux_enemy_list = []
        for enemy in self.dicc_level["enemies"]:
            position = enemy["pos"]
            x = position[0][0]
            y = position[0][1]
            path = enemy["path"]
            from_index =enemy["from_index"]
            quantity = enemy["quantity"]
            p_scale = enemy["p_scale"]
            speed_move = enemy["speed_move"]
            frame_move = enemy["frame_move"]
            frame_rate_ms = enemy["frame_rate_ms"]
            gravity = enemy["gravity"]
            x_init = enemy["x_init"]
            x_end = enemy["x_end"]
            
            enemy_obj = Enemy(x, y, path, from_index, quantity, p_scale, speed_move, frame_move, frame_rate_ms, gravity, x_init, x_end)
            aux_enemy_list.append(enemy_obj)
        return aux_enemy_list
    
            
    def platform_instantiation(self):
        """
        Este método se encarga de instanciar a las plataformas

        Retorna: una lista de plataformas
        """
        aux_platform_list = []
        for plataforma in self.dicc_level["platforms"]:
            pos = plataforma["pos"]
            w = plataforma["w"]
            h = plataforma["h"]
            type = plataforma["type"]
            aux_platform_object = Plataform(pos[0][0],pos[0][1],w,h,type)
            aux_platform_list.append(aux_platform_object)
        return aux_platform_list
    
    def money_instantiation(self):
        """
        Este método se encarga de instanciar a la money

        Retorna: una lista de money
        """
        aux_list_money = []
        for money in self.dicc_level["money"]:
            pos = money["pos"]
            x = pos[0][0]
            y = pos[0][1]
            frame_rate_ms = money["frame_rate_ms"]
            aux_money_object = Money(x, y, frame_rate_ms)
            aux_list_money.append(aux_money_object)
        return aux_list_money

    def win_condition(self,delta_ms):
        if self.name == "level_1" or self.name == "level_2":
            if len(self.enemy_list)==0 or len(self.money_list)==0:
                self.extra_time +=delta_ms
            if self.extra_time > 2000:
                self.set_active("win")
        if self.name == "level_3":
            # print(self.boss.lives)
            if self.boss.lives == 0:
                self.extra_time +=delta_ms
            if self.extra_time > 2000:
                self.set_active("win")

        #event_list,keys,music,delta_ms,timer_1s
    
    def update(self, event_list,keys,sound_list,delta_ms,timer_1s):
        self.win_condition(delta_ms)
        
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_active("pause")
            # if event.type == timer_1s and len(self.enemy_list) >0:
                self.game_time -= 1
        # print(self.game_time)
        if self.game_time >= 0:
            self.text3._text = "TIME:  {0}".format(self.game_time)
        else:
            self.set_active("lose")

        # print(f"{self.player.lives}") #!
        # self.text1._text="Lives:      {0}".format(self.player.lives)
        self.text2._text="SCORE:  {0}".format(str(self.player.score).zfill(6))
        if self.player.lives == 2:
            self.corazon3.image_background = None
        elif self.player.lives == 1:
            self.corazon2.image_background = None
        elif self.player.lives == 0:
            self.text1_image.image_background = None

        
        if self.player.lives <= 0:
            pygame.mixer.music.pause()
            # pygame.mixer.Sound.play(sound_list[died])
            self.set_active("lose")

        for aux_widget in self.widget_list:
            aux_widget.update(event_list)

        for bullet in self.bullets_list:
            if not bullet.is_active:
                self.bullets_list.remove(bullet)
                self.player.score += 50
            if self.name == "level_3": #!
                bullet.update(delta_ms,self.plataform_list, self.enemy_list, self.player, sound_list, self.boss)
            if self.name == "level_1" or self.name == "level_2":
                bullet.update(delta_ms,self.plataform_list, self.enemy_list, self.player, sound_list)

        # for bullet_element in self.bullet_list:
        #     bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player) #!
        #     if abs(bullet_element.x_init -bullet_element.x) > bullet_element.reach:
        #         self.bullet_list.remove(bullet_element)
        #         del bullet_element

        for enemy in self.enemy_list: #delta_ms,plataform_list, bullet_list, musica
            if enemy.flag_impact:
                self.enemy_list.remove(enemy)
            enemy.update(delta_ms,self.plataform_list,self.bullets_list,sound_list)
        
        for money in self.money_list:
            if money.flag_collition:
                self.money_list.remove(money)
                self.player.score += 100
            money.update(delta_ms, self.player, sound_list)
        if len(self.money_list) == 0:
            print("HAS GANADO")
            if self.flag_win:
                sound_list.victoria.play()
                self.flag_win = False
        # self.player.events(keys,self.enemy_list,self.plataform_list,sound_list)
        if self.name == "level_3":
            for bullets in self.bullets_boss:
                if not bullets.is_active:
                    self.bullets_boss.remove(bullets)
                bullets.update(delta_ms, self.plataform_list, self.player, self.boss, sound_list)
            self.boss.update(delta_ms, self.player, self.bullets_list, sound_list)
            self.player.update(delta_ms, keys,self.plataform_list,self.enemy_list,sound_list, self.bullets_boss)
        if self.name == "level_1" or self.name == "level_2":
            self.player.update(delta_ms, keys,self.plataform_list,self.enemy_list,sound_list)

    def draw(self, master_surface): 
        super().draw()
        self.static_background.draw(self.surface)

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        for money in self.money_list:
            money.draw(self.surface)

        for bullet in self.bullets_list:
            bullet.draw(master_surface)

        if self.name == "level_3":
            for bullets in self.bullets_boss:   
                if not bullets.is_active:
                    self.bullets_boss.remove(bullets)
                bullets.draw(master_surface)
            self.boss.draw(master_surface)

        self.player.draw(master_surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()