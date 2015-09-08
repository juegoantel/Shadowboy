import pygame
import constantes
import platforma
from nivel import Level
import  artefacto

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/mapainicialbeta.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -33848
        self.limitesuelo= 535
        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ #[platforma.GRASS_MIDDLE, 570, 500],
                  #[platforma.GRASS_RIGHT, 640, 500],
                  #[platforma.GRASS_LEFT, 800, 400],
                  #[platforma.GRASS_MIDDLE, 870, 400],
                  #[platforma.GRASS_RIGHT, 940, 400],
                  #[platforma.GRASS_LEFT, 1000, 500],
                  #[platforma.GRASS_MIDDLE, 1070, 500],
                  #[platforma.GRASS_RIGHT, 1140, 500],
                  #[platforma.STONE_PLATFORM_LEFT, 1120, 280],
                  #[platforma.STONE_PLATFORM_MIDDLE, 1190, 280],
                  #[platforma.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
        
        nivel_enemigos = [ [artefacto.pinchos, 4000, 500],  
                           [artefacto.pinchos, 6000, 500], 
                           [artefacto.pinchos, 8000, 500]
                         ] 
                  

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
        
        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for enemigo in nivel_enemigos:
            bloque_enemigo = artefacto.Enemigo(enemigo[0])
            bloque_enemigo.rect.x = enemigo[1]
            bloque_enemigo.rect.y = enemigo[2]
            
            bloque_enemigo.jugador = self.jugador
            self.lista_enemigos.add(bloque_enemigo)

        
            
 

        puntos=platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos.rect.x = 3000
        puntos.rect.y = 280
        puntos.limite_izquierdo = 2900
        puntos.limite_derecho = 3100
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos.rect.x = 3400
        puntos.rect.y = 280
        puntos.limite_izquierdo = 3300
        puntos.limite_derecho = 3500
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos.rect.x = 5400
        puntos.rect.y = 300
        puntos.limite_izquierdo = 5300
        puntos.limite_derecho = 5500
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        puntos.rect.x = 7400
        puntos.rect.y = 300
        puntos.limite_izquierdo = 7300
        puntos.limite_derecho = 7500
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)


        
        # Se agrega una plataforma en movimiento.
        #bloque = platforma.PlataformaConMovimiento(platforma.STONE_PLATFORM_MIDDLE)
        #bloque.rect.x = 1350
        #bloque.rect.y = 280
        #bloque.limite_izquierdo = 1350
        #bloque.limite_derecho = 1600
        #bloque.mover_x = 1
        #bloque.jugador = self.jugador
        #bloque.nivel = self
        #self.lista_plataformas.add(bloque)