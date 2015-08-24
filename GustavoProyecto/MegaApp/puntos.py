'''
Created on 21/10/2014

@author: manuelgpn1
'''

import random
import pygame


from funciones_spritesheet import  SpriteSheet

class Punto (pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(0, 0, 39, 50)
        self.image = sprite_sheet.get_image(39, 0, 39, 50)
        self.image = sprite_sheet.get_image(78, 0, 39, 50)
        self.image = sprite_sheet.get_image(117, 0, 39, 50)
        self.image = sprite_sheet.get_image(156, 0, 39, 50)
        self.image = sprite_sheet.get_image(195, 0, 39, 50)
        self.image = sprite_sheet.get_image(234, 0, 39, 50)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y 
        