import pygame
import constantes
import platforma
from nivel import Level

#Clase que define el segundo nivel.

class Level_02(Level):
    ''' Clase que define el primer nivel.
    Se debe definir el fondo, las plataformas y los enemigos que aparezcan.'''

    def __init__(self, jugador):
        """ Metodo que crea el nivel 2 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)
        
        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/background_02.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -1000

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma.STONE_PLATFORM_LEFT, 500, 550],
                  [platforma.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforma.STONE_PLATFORM_RIGHT, 640, 550],
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

        # Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        bloque.rect.x = 1500
        bloque.rect.y = 300
        bloque.limite_superior = 100
        bloque.limite_inferior = 550
        bloque.mover_y = -1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)