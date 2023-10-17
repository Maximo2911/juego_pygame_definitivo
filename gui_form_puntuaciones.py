import json, pygame
from gui_form import Form
from gui_widget import Widget
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, WHITE

class FormPuntuaciones(Form):
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_PANTALLA, h=ALTO_PANTALLA, color_background=None, imagen_background=None, color_border=None, active=False):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        # Cargar puntuaciones desde un archivo JSON
        self.puntuaciones = self.cargar_puntuaciones("puntuaciones.json")

        #widgets
        self.text_titulo = Widget(master=self, x=50, y=50, w=400, h=50, color_background=None, color_border=None, image_background=None, text="PUNTUACIONES", font="Bahnschrift", font_size=30, font_color=WHITE)
        self.text_puntuaciones = Widget(master=self, x=50, y=120, w=400, h=400, color_background=None, color_border=None, image_background=None, text=self.formatear_puntuaciones(), font="Bahnschrift", font_size=20, font_color=WHITE)
        # self.boton_volver = Widget(master=self, x=50, y=550, w=150, h=50, color_background=None, color_border=None, image_background=None, text="VOLVER", font="Bahnschrift", font_size=20, font_color=WHITE)

        self.lista_widget = [self.text_titulo, self.text_puntuaciones] #, self.boton_volver

    def cargar_puntuaciones(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r') as file:
                puntuaciones = json.load(file)
            return puntuaciones
        except FileNotFoundError:
            print("El archivo de puntuaciones no se encontró.")
            return []

    def formatear_puntuaciones(self):
        if not self.puntuaciones:
            return "No hay puntuaciones disponibles."
        
        formatted_puntuaciones = ""
        for indice, puntuacion in enumerate(self.puntuaciones, start=1):
            nombre = puntuacion['nombre']
            puntos = puntuacion['puntos']
            linea_formateada = f"{indice}. {nombre} - {puntos}\n"
            formatted_puntuaciones += linea_formateada

        return formatted_puntuaciones

    def update(self, lista_eventos, keys, music, delta_ms, timer_1s):
        for widget in self.lista_widget:
            widget.update(lista_eventos)

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("menu")


    def draw(self, master_surface):
        super().draw()
        for widget in self.lista_widget:
            widget.draw()
