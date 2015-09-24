'''
Created on 24/09/2015

@author: usuario
'''
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Player
bat            = (0, 0, 145, 43)


class Murcielago(pygame.sprite.Sprite):
    
    avance_jugador = 200
    

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        #sprite_sheet = SpriteSheet("imagenes/pinchos.png")
        
        self.image = pygame.image.load("imagenes/bat1.png").convert()
        self.rect = self.image.get_rect()    


        self.image.set_colorkey(constantes.BLANCO)