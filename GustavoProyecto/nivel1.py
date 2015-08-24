import pygame
import constantes
import platforma
from nivel import Level

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/mapainicialprtt.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -12000

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma.GRASS_LEFT, 500, 500],
                  [platforma.GRASS_MIDDLE, 570, 500],
                  [platforma.GRASS_RIGHT, 640, 500],
                  [platforma.GRASS_LEFT, 800, 400],
                  [platforma.GRASS_MIDDLE, 870, 400],
                  [platforma.GRASS_RIGHT, 940, 400],
                  [platforma.GRASS_LEFT, 1000, 500],
                  [platforma.GRASS_MIDDLE, 1070, 500],
                  [platforma.GRASS_RIGHT, 1140, 500],
                  [platforma.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforma.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforma.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        bloque.rect.x = 1350
        bloque.rect.y = 280
        bloque.limite_izquierdo = 1350
        bloque.limite_derecho = 1600
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)