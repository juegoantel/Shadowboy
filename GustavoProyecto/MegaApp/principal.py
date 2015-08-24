import pygame
import menu
import constantes

from nivel1 import Level_01
from nivel2 import Level_02 
import time
from jugador import Player
from menu import cMenu, EVENT_CHANGE_STATE
from string import center
from funciones_spritesheet import SpriteSheet
from funciones_spritesheet import SpriteSheetNotas


def jugar(screen, jugador):
    sonido = pygame.mixer.Sound("sonido/sonifofondoprovicional.ogg") 
    sonido.play()
    letraParaMarcador = pygame.font.Font(None, 36)
    letraTiempo = pygame.font.Font(None, 36)
    letraVida = pygame.font.Font(None,36)

    # Create the player
    player = Player(jugador)
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.nivel = current_level
    player.rect.x = 340
    player.rect.y = constantes.LARGO_PANTALLA - player.rect.height
    active_sprite_list.add(player)
    #Loop until the user clicks the close button.
    done = False # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    starting_point = time.time() + 400
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.mover_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.mover_x > 0:
                    player.stop()
        
        # Update the jugador.
        active_sprite_list.update()
        # Update items in the level
        current_level.update()
        # If the jugador gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)
        # If the jugador gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
        # If the jugador gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        #print current_position
        if current_position < current_level.level_limit:
            player.rect.x = 120
            """INSERTAR SONIDO DE FINAL DE LVL AQUI"""
            
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.nivel = current_level # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        text = letraParaMarcador.render("Puntos: " + str(player.puntaje), 1, constantes.ROJO)
        screen.blit(text, (100, 0)) 
        
        elapsed_time = starting_point - time.time ()
        elapsed_time_int = int(elapsed_time)
        textotiempo = letraTiempo.render("Tiempo: "+ str(elapsed_time_int), 1, constantes.ROJO)
        screen.blit(textotiempo, (255,0))
        
        marcadorVida = letraVida.render("Vida: " + str(player.vida), 1, constantes.ROJO)
        screen.blit(marcadorVida, (450,0))
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        # Limit to 60 frames per second
        clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        if elapsed_time <= 0:
            screen.fill(constantes.NEGRO)
            texto_gameover = letraParaMarcador.render("GAME OVER!,  Presione una tecla para volver a jugar.", 1, constantes.ROJO)
            screen.blit(texto_gameover, [100, 250])
            pygame.display.flip()
            pygame.event.wait()
            done = True
        
        if player.vida <= 0:
            screen.fill(constantes.NEGRO)
            texto_gameover = letraParaMarcador.render("GAME OVER!,  Presione una tecla para volver a jugar.", 1, constantes.ROJO)
            screen.blit(texto_gameover, [100, 250])
            pygame.display.flip()
            pygame.event.wait()
            done = True
            
    return done
def main():
    """ Programa principal """
    pygame.init()
    # Set the height and width of the screen6 +
    size = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Meggap")
    
    sprite_sheet = SpriteSheetNotas("imagenes/metalerosht.png")
    metalero = sprite_sheet.get_image(0,0,36,81)
    sprite_sheet = SpriteSheetNotas("imagenes/rastasht.png")
    rasta = sprite_sheet.get_image(0,0,36,81)
    sprite_sheet = SpriteSheetNotas("imagenes/raperosht.png")
    rapero = sprite_sheet.get_image(0,0,38,81)
    historia = pygame.image.load("imagenes/historia.png").convert()
    creditos = pygame.image.load("imagenes/creditos.png").convert()
    logo = pygame.image.load("imagenes/meggap.png").convert()
    logo.set_colorkey(constantes.BLANCO)
    alogo = True
    if alogo == True:
        screen.blit(logo,(250,20))
        pygame.display.flip()
        alogo = False
    
    menuJuego = cMenu(50,50,20,5,"vertical",100,screen,[("Jugar",1,None),("Historia",2,None),("Creditos",3,None),("Salir",4,None)])
    menuJugador = cMenu(30, 350, 100, 5, "horizontal", 4, screen, [("Metalero",5,metalero),("Rastafari",6,rasta),("Rapero",7,rapero),("Volver",0,None)])
    historia = cMenu (220,150, 400, 400, 'vertical',5,screen,[("Historia",8,historia)])
    creditos = cMenu (100,125, 630, 348, 'vertical',6,screen,[("Creditos",8,creditos)])
    
    #Alineamos el menu
    
    
    
    #"""menuPrueba = cMenu(x, y, h_pad, v_pad, orientation, number, background, buttonList)"""
    menuJuego.set_center(True, True)
    menuJuego.set_alignment("center", "center")
    
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
                screen.fill(constantes.NEGRO)
                opcion, estado = menuJugador.update(e, estado)
                screen.blit(logo,(250,20))
                pygame.display.flip()

            elif estado == 2:
                screen.fill(constantes.NEGRO)
                opcion, estado = historia.update(e, estado)
                pygame.display.flip()

            elif estado == 3:
                screen.fill(constantes.NEGRO)
                opcion, estado = creditos.update(e, estado)
                pygame.display.flip()

            elif estado == 5:
                jugador = 1
                jugar(screen, jugador)
            elif estado == 6:
                jugador = 2
                jugar(screen, jugador)
            elif estado == 7:
                jugador = 3
                jugar(screen, jugador)
            elif estado == 8:
                screen.fill(constantes.NEGRO)
                estado = 0
                screen.blit(logo,(250,20))
                pygame.display.flip()

            else:
                salir = True
            
        if e.type == pygame.QUIT:
            salir = True
            
        pygame.display.update(opcion)
            
    
    pygame.quit()

if __name__ == "__main__":
    main()
