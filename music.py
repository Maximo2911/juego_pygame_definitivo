import pygame
from constantes import *

# AGREGAR MUSICA
class Musica:
    """
    Esta clase sirve para cargar todos los sonidos y musica del juego, asi como ponerles un volumen inicial
    """
    def __init__(self) -> None:
        self.muerte = pygame.mixer.Sound(r"music\dead.wav")
        self.disparo = pygame.mixer.Sound(r"music\shoot.wav")
        self.recolectar = pygame.mixer.Sound(r"music\pick_up.wav")
        # self.puerta_activada = pygame.mixer.Sound(RUTA_MUSICA + r"activado.wav")
        self.victoria = pygame.mixer.Sound(r"music\victory.wav")
        self.disparo_boss = pygame.mixer.Sound(r"music\boss_shoot.wav")
        self.hit = pygame.mixer.Sound(r"music\hit.wav")
        # self.muerte_boss = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_boss.wav")
        self.muerte_enemigo = pygame.mixer.Sound(r"music\dead.wav")
        self.sonidos = [self.disparo,self.hit,self.muerte,self.recolectar,self.victoria,self.disparo_boss,self.muerte_enemigo]
        for sonido in self.sonidos:
            sonido.set_volume(0.3)

    def play_musica(self):
        """
        Este metodo se encarga de reproducir la musica principal del juego
        """
        pygame.mixer.init()
        # pygame.mixer.music.load(r"music\main_music.mp3")
        # pygame.mixer.music.set_volume(0.3)
        # pygame.mixer.music.play(-1)
