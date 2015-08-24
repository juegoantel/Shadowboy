import pygame

import constantes

class Level():
    """ Super-Clase generica usada para definir los niveles del juego. 
        Se debe crear una clase hija para cada nivel."""

    # Lista de todos los sprites utilizados en todos los niveles.  
    platform_list = []
    enemy_list = []

    # Imagen de fondo
    
    lista_de_comidas = []


    # Valor numerico de que tan lejos avanzo nuestro jugador en el nivel
    world_shift = 0
    limite_nivel = -1000

    def __init__(self, player):
        """ Constructor. Se le debe pasar al jugador para saber sobre que nivel esta. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.lista_de_comidas = pygame.sprite.Group()
        self.player = player


    def update(self):
        """ Actualizar todo sobre el nivel """
        self.platform_list.update()
        self.enemy_list.update()
        self.lista_de_comidas.update()

    def draw(self, screen):
        """ Dibujamos todo sobre el nivel. """

        # Se debe dibujar el fondo.
        screen.fill(constantes.AZUL)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Se dibujan todos los sprite que se cargaron.
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.lista_de_comidas.draw(screen)

    def shift_world(self, shift_x):
        """ Cuando el usuario se mueve de izquierda/derecha se debe mover el nivel """

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        
        for comidas in self.lista_de_comidas:
            comidas.rect.x += shift_x
