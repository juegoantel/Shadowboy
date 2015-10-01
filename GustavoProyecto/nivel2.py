import pygame
import constantes
import platforma
from nivel import Level
import pygame
import constantes
import platforma
import enemigo1
import artefacto
import murcielago
import manosz

from nivel import Level
from sombramovimiento import SombraConMovimiento 
from murcielagomov import MurcielagoConMovimiento

#Clase que define el segundo nivel.

class Level_02(Level):
    ''' Clase que define el primer nivel.
    Se debe definir el fondo, las plataformas y los enemigos que aparezcan.'''

    def __init__(self, jugador):
        """ Metodo que crea el nivel 2 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)
        
        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/Mapa2.png").convert()
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -50848
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
                           [artefacto.pinchos, 8000, 500],
                           [manosz.manos, 3000,500]     
                         ]
        
         
        # Se busca en la lista anterior creada y se le agregan las plataformas al jugador.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.Diamante)
        bloque.rect.x = 1500
        bloque.rect.y = 300
        bloque.limite_superior = 100
        bloque.limite_inferior = 550
        bloque.mover_y = -1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        "sombras"
            
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 6000
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 5750
        nivel_enemigos1.limite_derecho = 6250
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 7000
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 6750
        nivel_enemigos1.limite_derecho = 7250
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        "murcielagos" 
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 1000
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 900
        nivel_enemigos1.limite_derecho = 1100
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
         
            
        "diamantes"

        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 3000
        puntos.rect.y = 280
        puntos.limite_izquierdo = 2900
        puntos.limite_derecho = 3100
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 3400
        puntos.rect.y = 280
        puntos.limite_izquierdo = 3300
        puntos.limite_derecho = 3500
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 5400
        puntos.rect.y = 300
        puntos.limite_izquierdo = 5300
        puntos.limite_derecho = 5500
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 7400
        puntos.rect.y = 300
        puntos.limite_izquierdo = 7300
        puntos.limite_derecho = 7500
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
