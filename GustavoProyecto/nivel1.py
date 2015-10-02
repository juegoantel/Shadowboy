import pygame
import constantes
import platforma
import enemigo1
import artefacto
import murcielago
import manosz
import arbolmalo
import espanta


from nivel import Level
from sombramovimiento import SombraConMovimiento 
from murcielagomov import MurcielagoConMovimiento

    

class Level_01(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)
        self.sonido=pygame.mixer.Sound("sonido/musciadeljuego.wav")
        self.sonido.play()
        #Cargamos la imagen de fondo.
        self.fondo = pygame.image.load("imagenes/reworknivel1.png").convert()
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
                           [artefacto.pinchos, 8000, 500],
                           [artefacto.pinchos, 10000, 500],
                           [artefacto.pinchos, 12000, 500],
                           [artefacto.pinchos, 14000, 500],
                           [artefacto.pinchos, 16000, 500],
                           [artefacto.pinchos, 18000, 500],
                           [artefacto.pinchos, 20000, 500],
                           [artefacto.pinchos, 22000, 500],
                           
                           
                          ]   
                           
        
         
                          
        nivel_enemigos1 = [[arbolmalo.arbol, 11000,365],
                           [arbolmalo.arbol, 16000,365],
                           [arbolmalo.arbol, 19000,365]  
                          ]  

#         nivel_enemigos2 = [[espanta.espantapajaros, 1000,365]  
#                           ]  

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

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for enemigo in nivel_enemigos1:
            bloque_enemigo1 = arbolmalo.Enemigo(enemigo[0])
            bloque_enemigo1.rect.x = enemigo[1]
            bloque_enemigo1.rect.y = enemigo[2]
              
            bloque_enemigo1.jugador = self.jugador
            self.lista_enemigos.add(bloque_enemigo1)
            
        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
#         for enemigo in nivel_enemigos2:
#             bloque_enemigo1 = espanta.Enemigo(enemigo[0])
#             bloque_enemigo1.rect.x = enemigo[1]
#             bloque_enemigo1.rect.y = enemigo[2]
#               
#             bloque_enemigo1.jugador = self.jugador
#             self.lista_enemigos.add(bloque_enemigo1)
#             
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
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 9000
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 8750
        nivel_enemigos1.limite_derecho = 9250
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 13500
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 13400
        nivel_enemigos1.limite_derecho = 13600
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 15000
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 14900
        nivel_enemigos1.limite_derecho = 15100
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 17500
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 17400
        nivel_enemigos1.limite_derecho = 17600
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 17500
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 17400
        nivel_enemigos1.limite_derecho = 17600
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1 = SombraConMovimiento(enemigo1.sombra1)
        nivel_enemigos1.rect.x = 21000
        nivel_enemigos1.rect.y = 250
        nivel_enemigos1.limite_izquierdo = 19900
        nivel_enemigos1.limite_derecho = 2200
        nivel_enemigos1.mover_x = 3
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        
        "murcielagos" 
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 2500
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 2400
        nivel_enemigos1.limite_derecho = 2600
        nivel_enemigos1.mover_x = 4
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 4500
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 4300
        nivel_enemigos1.limite_derecho = 4700
        nivel_enemigos1.mover_x = 4
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 5500
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 5400
        nivel_enemigos1.limite_derecho = 5600
        nivel_enemigos1.mover_x = 4
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 11500
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 11400
        nivel_enemigos1.limite_derecho = 11600
        nivel_enemigos1.mover_x = 4
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 14000
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 13900
        nivel_enemigos1.limite_derecho = 14000
        nivel_enemigos1.mover_x = 4
        nivel_enemigos1.jugador = self.jugador
        nivel_enemigos1.nivel = self
        self.lista_enemigos.add(nivel_enemigos1)
        
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1 = MurcielagoConMovimiento(murcielago.bat)
        nivel_enemigos1.rect.x = 16500
        nivel_enemigos1.rect.y = 300
        nivel_enemigos1.limite_izquierdo = 16400
        nivel_enemigos1.limite_derecho = 16600
        nivel_enemigos1.mover_x = 4
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
        #sacaaar 1200
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 12000
        puntos.rect.y = 300
        puntos.limite_izquierdo = 11900
        puntos.limite_derecho = 12100
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 8400
        puntos.rect.y = 300
        puntos.limite_izquierdo = 8300
        puntos.limite_derecho = 8500
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 9000
        puntos.rect.y = 300
        puntos.limite_izquierdo = 8900
        puntos.limite_derecho = 9100
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 9400
        puntos.rect.y = 300
        puntos.limite_izquierdo = 9300
        puntos.limite_derecho = 9500
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 10500
        puntos.rect.y = 300
        puntos.limite_izquierdo = 10400
        puntos.limite_derecho = 10600
        puntos.mover_x = 2
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntaje.add(puntos)
        
        puntos=platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos = platforma.PlataformaConMovimiento(platforma.Diamante)
        puntos.rect.x = 15500
        puntos.rect.y = 300
        puntos.limite_izquierdo = 15400
        puntos.limite_derecho = 15600
        puntos.mover_x = 2
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