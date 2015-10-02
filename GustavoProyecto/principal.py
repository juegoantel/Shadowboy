import pygame
import constantes
import menu
from menu import cMenu, EVENT_CHANGE_STATE


from nivel1 import Level_01
from nivel2 import Level_02 

from funciones_spritesheet import SpriteSheet

from string import center
import jugador
from jugador import Player

def jugar(pantalla, jugador):
    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Player("imagenes/MOVIMIENTOSAJUSTADOS.png")

    letraparapuntos=pygame.font.Font(None,30)
    letragameover=pygame.font.Font(None,60)

    # Creamos todos los niveles del juego
    lista_niveles = []
    lista_niveles.append(Level_01(jugador_principal))
    lista_niveles.append(Level_02(jugador_principal))

    # Seteamos cual es el primer nivel.
    numero_del_nivel_actual = 1
    nivel_actual = lista_niveles[numero_del_nivel_actual]

    lista_sprites_activos = pygame.sprite.Group()
    jugador_principal.nivel = nivel_actual

    jugador_principal.rect.x = 340
    jugador_principal.rect.y = constantes.LARGO_PANTALLA - jugador_principal.rect.height
    lista_sprites_activos.add(jugador_principal)

    #Variable booleano que nos avisa cuando el usuario aprieta el botOn salir.
    salir = False

    clock = pygame.time.Clock()

    # -------- Loop Princiapl -----------
    while not salir:
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: 
                salir = True 

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_principal.retroceder()
                if evento.key == pygame.K_RIGHT:
                    jugador_principal.avanzar()
                if evento.key == pygame.K_UP:
                    jugador_principal.saltar()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador_principal.mover_x < 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_RIGHT and jugador_principal.mover_x > 0:
                    jugador_principal.parar()


        # Actualiza todo el jugador
        lista_sprites_activos.update()


        # Actualiza los elementos del nivel
        nivel_actual.update()


        # Si el jugador se acarca hacia el lado derecho mueve el mundo hacia la izquierda (-x)
        if jugador_principal.rect.x >= 500:
            diff = jugador_principal.rect.x - 500
            jugador_principal.rect.x = 500
            nivel_actual.avance_nivel(-diff)


        # Si el jugador se acarca hacia el lado izquierda mueve el mundo hacia la derecha (-x)
        if jugador_principal.rect.x <= 120:
            diff = 120 - jugador_principal.rect.x
            jugador_principal.rect.x = 120
            nivel_actual.avance_nivel(diff)


        #Si el jugador se mueve hacia el fin del nivel cambia el jugador al siguiente nivel.
        current_position = jugador_principal.rect.x + nivel_actual.posicion_jugador_nivel
        if current_position < nivel_actual.limite_nivel:
            jugador_principal.rect.x = 120
            if numero_del_nivel_actual < len(lista_niveles)-1:
                numero_del_nivel_actual += 1
                nivel_actual = lista_niveles[numero_del_nivel_actual]
                jugador_principal.nivel = nivel_actual

        print "current_position: ", current_position
        
        #print "posicion del personaje: ", current_position
        # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)

        textopuntos=letraparapuntos.render("Score: "+str(jugador_principal.puntos),1,constantes.BLANCO)
        pantalla.blit(textopuntos,(10,10))
        
        textovidas=letraparapuntos.render("life: "+str(jugador_principal.vidas),1,constantes.BLANCO)
        pantalla.blit(textovidas,(10,35))
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.

        clock.tick(60)

        pygame.display.flip()
        
        if jugador_principal.vidas<=0:
            pantalla.fill(constantes.NEGRO)
            texto_gameover= letragameover.render("GAME OVER, good night...",1, constantes.ROJO)
            pantalla.blit(texto_gameover, [100, 250])
            pygame.display.flip()
            pygame.event.wait()
            main()
            
    return salir 
     

def main():
    """ Clase principal en el que se debe ejecutar el juego. """
    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio)

    pygame.display.set_caption("Proyecto Video-Juegos")
    
    sprite_sheetN = SpriteSheet("imagenes/seleccion2.png")
    jugador = sprite_sheetN.obtener_imagen(0,0,50,50)

    
    # menu
    menuJuego = cMenu(250,250,20,5,"vertical",100,pantalla,[("Play Panlo europeo",1,None),("Historia",2,None),("Creditos",3,None),("Salir",4,None)])
    menuJugador = cMenu(0, 0, 20, 5, "horizontal", 4, pantalla, [("Metalero",5,jugador),("Volver",0,None)])
    #historia = cMenu (220,150, 400, 400, 'vertical',5,pantalla,[("Historia",7,historia)])
    #creditos = cMenu (100,125, 630, 348, 'vertical',6,pantalla,[("Creditos",8,creditos)])
    logo = pygame.image.load("imagenes/SBwallpaper.png").convert()
    logo.set_colorkey(constantes.BLANCO)
    alogo = True
    if alogo == True:    
        pantalla.blit(logo,(0,0))
        pygame.display.flip()
        alogo = False
    
    
    estado = 0
    estado_previo = 1 
    
    opcion =  [] 
    jugador = 1
    salir = False
    
    
    while not salir:
        if estado_previo != estado:
            pygame.event.post(pygame.event.Event(menu.EVENT_CHANGE_STATE, key = 0))
            estado_previo = estado
        e = pygame.event.wait()
        
        if e.type == pygame.KEYDOWN or e.type == menu.EVENT_CHANGE_STATE:
            if estado == 0:
                opcion, estado = menuJuego.update(e,estado) 
            elif estado == 1:                
                pantalla.blit(logo,(0,0))
                opcion, estado = menuJugador.update(e, estado)
                pygame.display.flip()

            elif estado == 2:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = historia.update(e, estado)
                pygame.display.flip()

            elif estado == 3:
                pantalla.fill(constantes.NEGRO)
                opcion, estado = creditos.update(e, estado)
                pygame.display.flip()
            else:
                salir = True
                

            """
            elif estado == 5:
                jugar(pantalla, 1)
                
            elif estado == 6:
                jugar(pantalla, 2)
                
            elif estado == 7:
                jugador = 3
                jugar(pantalla, jugador)
                
            elif estado == 8:
                pantalla.fill(constantes.NEGRO)
                estado = 0
                pantalla.blit(logo,(0,0))
                pygame.display.flip()
            """
            
        if e.type == pygame.QUIT:
            salir = True
            
        pygame.display.update(opcion)
    
    
    pygame.quit()

if __name__ == "__main__":
    main()
