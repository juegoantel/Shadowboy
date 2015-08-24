'''
Created on 15/09/2014

@author: rodrigo
'''

import pygame
import constantes
import platforms
import platforms2
from levels import Level
from comida import *
import enemigos
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("imagenes/fondonivel2.png").convert()
        self.level_limit = -32000

        # Enemigos
        #ene = enemigos.MovingPlatform()
        #ene.rect.x = 2610
        #ene.rect.y = 390
        #ene.boundary_left = 
        #ene.boundary_right = 2680
        #ene.mover_x = 1
        #ene.player = self.player
        #ene.nivel = self
        
        #self.enemy_list.add(ene)

        #COMIDAS
        
        self.lista_de_comidas.add(Negro(620,380))
        self.lista_de_comidas.add(Verde2(1250,150))
        self.lista_de_comidas.add(Azul3(2300,150))
        self.lista_de_comidas.add(Rojo2(2300,410))
        self.lista_de_comidas.add(Violeta(2650,100))
        self.lista_de_comidas.add(Naranja(2660,350))
        self.lista_de_comidas.add(Azul(3000,420))
        self.lista_de_comidas.add(Amarillo2(3400,420))
        
        # Array with type of platform, and x, y location of the platform.
        level = [ 
                 [platforms.PISO, -5850, 490],
                 [platforms.PISO, -150, 490],
                 [platforms.PISO, 4500, 490],
                 [platforms.PISO, 10050, 490],
                 [platforms.PISO, 16050, 490],
                 [platforms.PISO, 22050, 490],
                 [platforms.PISO, 28050, 490],
                 [platforms.PISO, 34050, 490]
                  
                  ]
           # Go through the array above and add platforms


        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
            
            
            
            
            
        level = [ 
                 [platforms2.TORRE, 600, 420],
                 [platforms2.BASICO1, 880, 280],
                 [platforms2.LARGO1, 1200, 200],
                 [platforms2.MEDIANO1, 1520, 335],
                 [platforms2.LARGO1, 2600, 150],
                 [platforms2.LARGO1, 2600, 400],
                 [platforms2.TORRE, 2900, 430],
                 [platforms2.TORRE, 2900, 359],
                 [platforms2.TORRE, 2900, 288],
                 [platforms2.TORRE, 3500, 430],
                 [platforms2.TORRE, 3549, 430],
                 [platforms2.TORRE, 3549, 359],
                 [platforms2.TORRE, 3598, 288],
                 [platforms2.TORRE, 3598, 359],
                 [platforms2.TORRE, 3598, 430],
                 [platforms2.BASICO1, 3880, 380],
                 [platforms2.MEDIANO1, 4600, 210],
                 [platforms2.TORRE, 4800, 288],
                 [platforms2.TORRE, 4800, 359],
                 [platforms2.TORRE, 4800, 430],
                 [platforms2.TORRE, 5100, 440],
                 [platforms2.TORRE, 5100, 120],
                 [platforms2.BASICO1, 5600, 380],
                 [platforms2.BASICO1, 5900, 280],
                 [platforms2.LARGO1, 6200, 220],
                 [platforms2.LARGO1, 6310, 220],
                 [platforms2.MEDIANO1, 6600, 380],
                 [platforms2.TORRE, 6800, 430],
                 [platforms2.TORRE, 7000, 430],
                 [platforms2.TORRE, 7200, 430],
                 [platforms2.BASICO1, 7500, 280],
                 [platforms2.MEDIANO1, 7700, 350],
                 [platforms2.LARGO1, 7880, 250],
                 [platforms2.MEDIANO1, 8100, 340],
                 [platforms2.TORRE, 8400, 288],
                 [platforms2.TORRE, 8400, 359],
                 [platforms2.TORRE, 8400, 430],
                 [platforms2.TORRE, 8900, 288],
                 [platforms2.TORRE, 8900, 359],
                 [platforms2.TORRE, 8900, 430],
                 [platforms2.BASICO1, 9200, 380],
                 [platforms2.BASICO1, 9400, 300],
                 [platforms2.LARGO1, 9700, 250],
                 [platforms2.LARGO1, 10000, 200],
                 [platforms2.BASICO1, 10700, 380],
                 [platforms2.TORRE, 11000, 430],
                 [platforms2.TORRE, 11350, 430],
                 [platforms2.LARGO1, 12010, 120],
                 [platforms2.LARGO1, 12135, 120],
                 [platforms2.TORRE, 12500, 288],
                 [platforms2.TORRE, 12500, 359],
                 [platforms2.TORRE, 12500, 430],
                 [platforms2.BASICO1, 13000, 400],
                 [platforms2.BASICO1, 13400, 400],
                 [platforms2.BASICO1, 13800, 400],
                 [platforms2.BASICO1, 14200, 400],
                 [platforms2.LARGO1, 15500, 300],
                 [platforms2.BASICO1, 15800, 320],
                 [platforms2.LARGO1, 16000, 300],
                 [platforms2.MEDIANO1, 16300, 380],
                 [platforms2.MEDIANO1, 16600, 280],
                 [platforms2.TORRE, 17600, 288],
                 [platforms2.TORRE, 17600, 359],
                 [platforms2.TORRE, 17600, 430],
                 [platforms2.MEDIANO1, 17800, 400],
                 [platforms2.BASICO1, 18100, 350],
                 [platforms2.LARGO1, 18400, 300],
                 [platforms2.BASICO1, 18850, 244],
                 [platforms2.BASICO1, 19200, 320],
                 [platforms2.BASICO1, 19400, 410],
                 [platforms2.LARGO1, 19700, 300],
                 [platforms2.MEDIANO1, 20100, 350],
                 [platforms2.TORRE, 20350, 430],
                 [platforms2.TORRE, 20500, 430],
                 [platforms2.TORRE, 20650, 430],
                 [platforms2.BASICO1, 20800, 380],
                 [platforms2.MEDIANO1, 21000, 280],
                 [platforms2.LARGO1, 21300, 250],
                 [platforms2.LARGO1, 21600, 180], 
                 [platforms2.LARGO1, 22100, 200],
                 [platforms2.LARGO1, 22100, 355],
                 [platforms2.LARGO1, 22300, 279],
                 [platforms2.BASICO1, 22550, 400],
                 [platforms2.BASICO1, 22750, 380],
                 [platforms2.MEDIANO1, 22990, 350],
                 [platforms2.LARGO1, 23300, 270],
                 [platforms2.TORRE, 23600, 288],
                 [platforms2.TORRE, 23600, 359],
                 [platforms2.TORRE, 23600, 430],
                 [platforms2.MEDIANO1, 23800, 350],
                 [platforms2.TORRE, 24000, 288],
                 [platforms2.TORRE, 24000, 359],
                 [platforms2.TORRE, 24000, 430],
                 [platforms2.BASICO1, 24400, 380],
                 [platforms2.MEDIANO1, 24750, 280],
                 [platforms2.LARGO1, 25000, 250],
                 [platforms2.TORRE, 25350, 430],
                 [platforms2.TORRE, 25500, 430],
                 [platforms2.TORRE, 25650, 430],
                 [platforms2.TORRE, 25800, 430],
                 [platforms2.TORRE, 25950, 430],
                 [platforms2.TORRE, 26150, 430],
                 [platforms2.TORRE, 26300, 430],
                 [platforms2.TORRE, 26450, 430],
                 [platforms2.TORRE, 26600, 430],
                 [platforms2.LARGO1, 26900, 300],
                 [platforms2.LARGO1, 27100, 350],
                 [platforms2.LARGO1, 27300, 300],
                 [platforms2.BASICO1, 27550, 380],
                 [platforms2.MEDIANO1, 27800, 280],
                 [platforms2.LARGO1, 28100, 250],
                 [platforms2.BASICO1, 28450, 380],
                 [platforms2.MEDIANO1, 28800, 280],
                 [platforms2.LARGO1, 29150, 250],
                 [platforms2.BASICO1, 29350, 380],
                 [platforms2.LARGO1, 29600, 250],

                 
                 


                 
                 
                 
                 
                  ]
                         
            
        for platform in level:
            block = platforms2.Platform2(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            

        level = [ [platforms.PISO, -20, 0]

                  ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.VerticalPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
            
        block = platforms2.MovingPlatform2(platforms2.LARGO1)
        block.rect.x = 1820
        block.rect.y = 245
        block.boundary_left = 1820
        block.boundary_right = 2000
        block.mover_x = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
    
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 2300
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 400
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms2.MovingPlatform2(platforms2.LARGO1)
        block.rect.x = 3950
        block.rect.y = 250
        block.boundary_left = 3950
        block.boundary_right = 4300
        block.mover_x = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 5100
        block.rect.y = 175
        block.boundary_top = 175
        block.boundary_bottom = 440
        block.mover_y = -4
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 6800
        block.rect.y = 100
        block.boundary_top = 100
        block.boundary_bottom = 430
        block.mover_y = -3
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 7000
        block.rect.y = 100
        block.boundary_top = 100
        block.boundary_bottom = 430
        block.mover_y = -3
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 7200
        block.rect.y = 100
        block.boundary_top = 100
        block.boundary_bottom = 430
        block.mover_y = -3
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.MEDIANO1)
        block.rect.x = 8700
        block.rect.y = 220
        block.boundary_top = 220
        block.boundary_bottom = 355
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 10450
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 400
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.BASICO1)
        block.rect.x = 11800
        block.rect.y = 100
        block.boundary_top = 100
        block.boundary_bottom = 444
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
    
        block = platforms2.MovingPlatform2(platforms2.BASICO1)
        block.rect.x = 12400
        block.rect.y = 100
        block.boundary_top = 100
        block.boundary_bottom = 444
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.BASICO1)
        block.rect.x = 14600
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 444
        block.mover_y = -3
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms2.MovingPlatform2(platforms2.MEDIANO1)
        block.rect.x = 14900
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 444
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms2.MovingPlatform2(platforms2.BASICO1)
        block.rect.x = 15200
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 444
        block.mover_y = -3
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)  
        
        block = platforms2.MovingPlatform2(platforms2.LARGO1)
        block.rect.x = 16800
        block.rect.y = 300
        block.boundary_left = 16800
        block.boundary_right = 17380
        block.mover_x = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 20350
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)  

        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 20500
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 20650
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block) 
        
        block = platforms2.MovingPlatform2(platforms2.BASICO1)
        block.rect.x = 21900
        block.rect.y = 150
        block.boundary_top = 100
        block.boundary_bottom = 380
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)  
        
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 25350
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)  

        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 25500
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 25650
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block) 
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 25800
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block) 
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 25950
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 26150
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)  

        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 26300
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block) 
          
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 26450
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block) 
        
        block = platforms2.MovingPlatform2(platforms2.TORRE)
        block.rect.x = 26600
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 430
        block.mover_y = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block) 
        
        block = platforms2.MovingPlatform2(platforms2.LARGO1)
        block.rect.x = 29800
        block.rect.y = 300
        block.boundary_left = 29800
        block.boundary_right = 32000
        block.mover_x = -2
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        # Add a custom moving platform 20350
        #block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        #block.rect.x = 1500
        #block.rect.y = 300
        #block.boundary_top = 100
        #block.boundary_bottom = 550
        #block.mover_y = -1
        #block.player = self.player
        #block.nivel = self
        #self.platform_list.add(block)