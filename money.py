from player import *
from auxiliar import *

class Money():
    def __init__(self, x, y, frame_rate_ms) -> None:
        self.money_spining = Auxiliar.getSurfaceFromSeparateFiles("animated_objects/money/{0}.png", from_index=0, quantity=6, flip=False, scale=1.5)

        self.frame = 0
        self.animation = self.money_spining
        
        #rectangulo
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

       # Hitbox money                   | Coordenadas rectangulo |    ANCHO        |      ALTO
        self.collition_rect = pygame.Rect(x + self.rect.width/8, y, self.rect.width/1.2, self.rect.height)
        self.flag_collition = False

        self.time_animations = 0 
        self.frame_rate_ms = frame_rate_ms

    def do_animations(self, delta_ms):
        self.time_animations += delta_ms
        if self.time_animations >= self.frame_rate_ms:
            self.time_animations = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    def check_impact(self, player, musica):
        if self.collition_rect.colliderect(player.collition_rect):
            self.flag_collition = True
            musica.recolectar.play()

    def update(self,delta_ms, player, musica):
        self.do_animations(delta_ms)
        self.check_impact(player, musica)

    def draw(self, screen):
        if not self.flag_collition:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
                # pygame.draw.rect(screen,color=(0,255,0),rect=self.sides_collition_rect)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)