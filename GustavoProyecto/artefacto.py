'''
Created on 27/08/2015

@author: usuario
'''
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Player
pinchos            = (0, 0, 210, 170)


class Enemigo(pygame.sprite.Sprite):


  def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        #sprite_sheet = SpriteSheet("imagenes/pinchos.png")
        
        self.image = pygame.image.load("imagenes/pinchos.png").convert()
        self.rect = self.image.get_rect()    


        self.image.set_colorkey(constantes.BLANCO)