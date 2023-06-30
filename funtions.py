from constantes import HITBOX_JUGADOR
import pygame, os

def enlistar_sequencia(path_folder) -> list:
    '''
    Funcion que se encarga de analizar archivos que hay en una carpeta especifica 
    Recibe como dato la ruta relativa de la carpeta que se desea analizar
    Retorna lista con los nombres de cada frame dentro la carpeta seleccionada
    '''
    lista_acciones = []
    # Ruta de la carpeta
    ruta = path_folder

    # Obtener la lista de archivos en la carpeta
    lista_archivos = os.listdir(ruta)

    #imprimimos todos los nombres de los archivos dentro de la carpeta
    for acciones in lista_archivos:
        lista_acciones.append(acciones)

    return lista_acciones
# print(enlistar_sequencia("sprits/recotardos_con_asu/attack"))
#===============================================================================
def crear_lista_rutas_relativas(path_folder:str) -> list:
    '''
    Funcion que se encarga de crear una lista con las rutas relativas de cada sprite dentro de la carpeta
    Recibe como dato la ruta de la carpeta de la cual estarán los sprites adentro
    Retorna una lista
    '''
    lista_con_rutas = []
    lista_acciones = enlistar_sequencia(path_folder)
    for indice in lista_acciones:
        path = f"{path_folder}{indice}"
        lista_con_rutas.append(path)
    return lista_con_rutas
# print(crear_lista_rutas_relativas("sprites/run/"))
#===============================================================================
def dar_vuelta_sprites(action:str)-> list:
    '''
    Funcion que se encarga de dar vuelta las secuencias de sprites
    Recibe como funcion la lista de sprites que se quieren dar vuelta
    Retorna la lista de sprites con cada imagen dada vuelta
    '''
    lista_flip = []
    match action:
        case "attack":
            secuencia = crear_lista_rutas_relativas("sprits/recotardos_con_asu/attack/")
        case "run":
            secuencia = crear_lista_rutas_relativas("sprits/recotardos_con_asu/run/")
        case "idle":
            secuencia = crear_lista_rutas_relativas("sprits/recotardos_con_asu/idle/")
    longitud = len(secuencia)
    for i in range(longitud):
        image = secuencia[i]
        image_load = pygame.image.load(image)
        image_flipped = pygame.transform.flip(image_load, True, False)
        lista_flip.append(image_flipped)

    return lista_flip
# print(dar_vuelta_sprites("attack"))
#===============================================================================

