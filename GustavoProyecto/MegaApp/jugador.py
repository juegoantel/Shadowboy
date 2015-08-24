
"""
Esta modulo es utilizado para desarrollar el jugador.
"""
import pygame

import constantes
from puntos import Punto
from platforms import MovingPlatform
from funciones_spritesheet import SpriteSheet
from funciones_spritesheet import SpriteSheetNotas


class Player(pygame.sprite.Sprite):

    # -- Atributos
    mover_x = 0
    mover_y = 0
    vida = 60
    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_izq = []
    jugador_frame_der = []
    jugador_frame_izq2 = []
    jugador_frame_der2 = []
    jugador_frame_izq3 = []
    jugador_frame_der3 = []
    puntaje = 0
    
    # Direccion en la que va el jugador.
    direccion = "R"
    salto = False

    # Lista de sprite con las cosas que nos podemos chocar.
    nivel = None

    colision = None
    
    # -- Methods
    def __init__(self, jugador):
        """ Constructor function """

        pygame.sprite.Sprite.__init__(self)
        
        
        if jugador == 1:
            sprite_sheet = SpriteSheetNotas("imagenes/metalerosht.png")
            
            image = sprite_sheet.get_image(0, 0, 39, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(39, 0, 39, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(78, 0, 39, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(118, 0, 39, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(156, 0, 39, 81)
            self.jugador_frame_der.append(image)
            
            #Rotacion 
            image = sprite_sheet.get_image(0, 0, 39, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(39, 0, 39, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(78, 0, 39, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(117, 0, 39, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(156, 0, 39, 81)
            image = pygame.transform.flip(image, True, False)
            
        elif jugador == 2:
            sprite_sheet = SpriteSheetNotas("imagenes/rastasht.png")
            
            image = sprite_sheet.get_image(0, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(46, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(92, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(138, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(183, 0, 45, 81)
            self.jugador_frame_der.append(image)
            
            #Rotacion 
            image = sprite_sheet.get_image(0, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(46, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(92, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(138, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(183, 0, 45, 81)
            image = pygame.transform.flip(image, True, False)
            
        elif jugador == 3:
            sprite_sheet = SpriteSheetNotas("imagenes/raperosht.png")

            image = sprite_sheet.get_image(0, 0, 46, 80)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(46, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(92, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(139, 0, 46, 81)
            self.jugador_frame_der.append(image)
            image = sprite_sheet.get_image(185, 0, 45, 81)
            self.jugador_frame_der.append(image)
            
            #Rotacion 
            image = sprite_sheet.get_image(0, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(46, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(92, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(139, 0, 46, 81)
            image = pygame.transform.flip(image, True, False)
            self.jugador_frame_izq.append(image)
            image = sprite_sheet.get_image(185, 0, 45, 81)
            image = pygame.transform.flip(image, True, False)
            
            
            

        self.jugador_frame_izq.append(image)
        self.image = self.jugador_frame_der[0]
        self.rect = self.image.get_rect()
        self.comidas = pygame.sprite.Group()        self.colision = pygame.mixer.Sound("sonido/sonidocolicion.ogg")
        self.comidas_que_chocan  = pygame.mixer.Sound("sonido/SOL.ogg")
        
        
    def update(self):
        """ Metodo que mueve al jugador. """
        # Gravedad
        self.calc_grav()

        # Movimientos Izquierda/Derecha
        self.rect.x += self.mover_x
        pos = self.rect.x + self.nivel.world_shift
        if self.direccion == "R":
            frame = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[frame]
        else:
            frame = (pos // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[frame]

        # Verficiamos si colisionamos con algo
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            elif self.mover_x < 0:
                self.rect.left = block.rect.right
          
            self.colision.play()
        
        self.rect.y += self.mover_y

        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_y > 0:
                self.rect.bottom = block.rect.top
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom

            self.mover_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.mover_x
             
        lista_de_comidas_a_comer = pygame.sprite.spritecollide(self, self.nivel.lista_de_comidas,False)
        for comidas_que_chocan in lista_de_comidas_a_comer:
            comidas_que_chocan.kill()
            self.puntaje += 1
            self.comidas_que_chocan.play()
        
        
        
    def calc_grav(self):
        """ Calcula el efecto de la gravedad. """
        if self.mover_y == 0:
            if self.salto:
                self.colision.play()
                self.salto = False
            self.mover_y = 2
        else:
            self.mover_y += .34

        # Verificamos si estamos en el suelo.
        if self.rect.y >= constantes.LARGO_PANTALLA - self.rect.height and self.mover_y >= 1:
            self.mover_y = 1
            self.rect.y = constantes.LARGO_PANTALLA - self.rect.height
            

    def jump(self):
        """ Metodo que se llamam si saltamos. """
        
        self.salto = True
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constantes.LARGO_PANTALLA:
            self.mover_y = -10

    def go_left(self):
        """ Se llama cuando movemos hacia la izq. """
        self.mover_x = -6
        self.direccion = "L"

    def go_right(self):
        """ Se llama cuando movemos hacia la der. """
        self.mover_x = 6
        self.direccion = "R"
        

    def stop(self):
        """ Se llama cuando soltamos la tecla. """
        self.mover_x = 0
