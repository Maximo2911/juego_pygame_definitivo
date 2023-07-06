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
def escalar_secuencia_imagenes(secuencia, escala):
    secuencia_escalada = []
    for ruta_imagen in secuencia:
        imagen = pygame.image.load(ruta_imagen)
        imagen_escalada = pygame.transform.scale(imagen, escala)
        secuencia_escalada.append(imagen_escalada)
    return secuencia_escalada

w=100
h=200
# print(escalar_secuencia_imagenes(crear_lista_rutas_relativas("sprites/spin/"), (w, h)))
#===============================================================================

