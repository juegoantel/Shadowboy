"""
Funciones para convertir sprite de un sprite sheet
"""

import pygame

import constantes

class SpriteSheet(object):
    """ Clase utilizada para obtener las imagenes de la hoja de sprite. """
    # Este atributo hace referencia al sprite sheet.
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor de la clase. Se debe pasar la ruta del la hoja del sprite """

        # Carga el sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Obtiene una sola imagen del spritesheet. 
            Se pasa la x,y como ubicacion de la sprite
            y el ancho y largo del sprite. """

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Asumimos que tiene un fondo negro y lo queremos hacer transparente. 
        image.set_colorkey(constantes.NEGRO)

        return image

class SpriteSheetPlataformas(object):
    """ Clase utilizada para obtener las imagenes de la hoja de sprite. """
    # Este atributo hace referencia al sprite sheet.
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor de la clase. Se debe pasar la ruta del la hoja del sprite """

        # Carga el sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Obtiene una sola imagen del spritesheet. 
            Se pasa la x,y como ubicacion de la sprite
            y el ancho y largo del sprite. """

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Asumimos que tiene un fondo negro y lo queremos hacer transparente. 
        image.set_colorkey(constantes.NEGRO)

        return image

class SpriteSheetNotas(object):
    """ Clase utilizada para obtener las imagenes de la hoja de sprite. """
    # Este atributo hace referencia al sprite sheet.
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor de la clase. Se debe pasar la ruta del la hoja del sprite """

        # Carga el sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Obtiene una sola imagen del spritesheet. 
            Se pasa la x,y como ubicacion de la sprite
            y el ancho y largo del sprite. """

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Asumimos que tiene un fondo negro y lo queremos hacer transparente. 
        image.set_colorkey(constantes.BLANCO)

        return image


