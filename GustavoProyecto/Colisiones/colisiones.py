import pygame
import random
 
# Definimos algunos colores
NEGRO    = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
ROJO      = ( 255,   0,   0)
 
# Esta clase representa          
# Deriva de la clase "Sprite" en Pygame

class Bloque(pygame.sprite.Sprite):
     
    # Constructor. Pasa el color al bloque, y su posicion x e y
    def __init__(self, color, largo, alto):
        # Llama al constructor de la clase padre (Sprite) 
        pygame.sprite.Sprite.__init__(self) 
 
        # Crea una imagen del bloque y lo rellena de color.
        # Esto podria ser tambien una imagen cargada desde el disco duro.
        #self.image = pygame.Surface([largo, alto])
        #self.image.fill(color)
        
                
        self.image = pygame.image.load('imagenes/pajaro.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        
                   
        # Obtenemos el objeto rectangulo que posee las dimensiones de la imagen
        # Actualizamos la posicion de ese objeto estableciendo los valores para 
        # rect.x y rect.y
        self.rect = self.image.get_rect()
 
 
def main():
    # Inicializamos Pygame
    pygame.init()
     
    # Establecemos el alto y largo de la pantalla
    pantalla_largo=800
    pantalla_alto=600
    pantalla=pygame.display.set_mode([pantalla_largo,pantalla_alto])
     
    # Esta es una lista de 'sprites.' Cada bloque en el programa es
    # anadido a la lista. La lista es gestionada por una clase llamada 'Group.'
    bloque_lista = pygame.sprite.Group()
     
    # Esta es una lista de cada uno de los sprites. Asi como del resto de bloques y el bloque protagonista..
    listade_todoslos_sprites = pygame.sprite.Group()
     
    for i in range(50):
        # Esto representa un bloque
        largo_aleatorio = random.randrange(50)
        #largo_aleatorio = random.randint(50,60)
        alto_aleatorio = random.randrange(60)
        bloque = Bloque(NEGRO, largo_aleatorio, alto_aleatorio)
     
        # Establecemos una ubicacion aleatoria para el bloque
        bloque.rect.x = random.randrange(pantalla_largo)
        bloque.rect.y = random.randrange(pantalla_alto)
         
        # Anadimos el  bloque a la lista de objetos
        bloque_lista.add(bloque)
        listade_todoslos_sprites.add(bloque)
         
        
     
    # Creamos un bloque protagonista ROJO
    protagonista = Bloque(ROJO, 100, 115)
    listade_todoslos_sprites.add(protagonista)
     
    # Iteramos hasta que el usuario pulse el boton de salida (flag = bandera)
    hecho = False
     
    #  Se usa para establecer cuan rapido se actualiza la pantalla
    reloj = pygame.time.Clock()
     
    # Lo usamos como contador de colisiones 
    marcador = 0
          
     
    # -------- Bucle principal del Programa -----------
    while hecho==False:
        for evento in pygame.event.get(): # El usuario hizo algo
            if evento.type == pygame.QUIT: # Si el usuario pulso salir
                hecho = True # Marcamos que hemos terminado y salimos del bucle
     
        # Limpiamos la pantalla
        pantalla.fill(BLANCO)
     
        # Obtenemos la posicion actual del raton. Esto devuelve la posicion
        # como una lista de dos numeros.
        pos = pygame.mouse.get_pos()
         
        # Extraemos la x e y de la lista, 
        # Tal como si extrajeramos letras de una cadena de texto.
        # Colocamos al objeto protagonista en la ubicacion del raton.
        protagonista.rect.x = pos[0]
        protagonista.rect.y = pos[1]
         
        # Observamos si el bloque protagonista ha colisionado con algo.
        lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, True)  
         
        # Comprobamos la lista de colisiones
        for bloque in lista_impactos_bloques:
            marcador +=1
            print( marcador )
             
        # Dibujamos todos los sprites
        listade_todoslos_sprites.draw(pantalla)
         
        # Limitamos a 20 fotogramas por segundo
        reloj.tick(60)
     
        # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
     
    pygame.quit()
    
if __name__ == "__main__":
    main()
