'''
Created on 27/08/2015

@author: usuario
'''
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Player
sombra1            = (10, 10, 600, 750)


class Enemigo1(pygame.sprite.Sprite):
    
    avance_jugador = 1
    

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        #sprite_sheet = SpriteSheet("imagenes/pinchos.png")
        
        self.image = pygame.image.load("imagenes/sombraenemigo.png").convert()
        self.rect = self.image.get_rect()    

        self.image.set_colorkey(constantes.BLANCO)
        