from constantes import *
from funtions import *
import pygame

class Auxiliar:

#     @staticmethod
#     def method_scale_image(path_format, min_index_frame, max_index_frame, scale=1, w = 0, h = 0):
#         # lista_frames = crear_lista_rutas_relativas(path_format)
#         lista_frames = []
#         for i in range(min_index_frame, max_index_frame):
#             indice = f"{i}.png"
#             path = path_format.format(indice)
#             surface_frame = pygame.image.load(path)
#             frame_weight_scaled = int(surface_frame.get_rect().w * scale) # Ancho
#             frame_height_scaled = int(surface_frame.get_rect().h * scale) # Alto
#             if(scale == 1 and w != 0 and h != 0):
#                 surface_frame = pygame.transform.scale(surface_frame,(w, h)).convert_alpha()
#             if(scale != 1):
#                 surface_frame = pygame.transform.scale(surface_frame,(frame_weight_scaled, frame_height_scaled)).convert_alpha()

#             print(f"Vuelta{i}")
#             lista_frames.append(surface_frame)
#         return lista_frames
# print(Auxiliar.method_scale_image("sprites/duck/{}", 0, 3, scale = 1))

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            # indice = f"{i}.png"
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista
# print(Auxiliar.method_scale_image("sprites/duck/{}", 0, 3, scale = 1, ))

# print(Auxiliar.getSurfaceFromSeparateFiles("sprites/duck/{0}.png",0,3,flip=False,scale=1))

