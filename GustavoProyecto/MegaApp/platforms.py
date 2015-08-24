"""
Module for managing platforms.
"""
import pygame

from funciones_spritesheet import SpriteSheetPlataformas

# These constantes define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

LADRILLO1            = (0, 0, 65, 40)
LADRILLO2           = (65, 0, 90, 33)
LADRILLO3          = (0, 39, 130, 24)
PISO               = (0,104,6000,33)
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheetPlataformas("imagenes/plataformaspiso.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3]
                                            )

        self.rect = self.image.get_rect()

class VerticalPlatform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheetPlataformas("imagenes/plataformaspiso.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3]
                                            )
        self.image = pygame.transform.rotate(self.image,90)
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    mover_x = 0
    mover_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    nivel = None
    player = None

    def update(self):
        """ Move the platform.
            If the jugador is in the way, it will shove the jugador
            out of the way. This does NOT handle what happens if a
            platform shoves a jugador into another object. Make sure
            moving platforms have clearance to push the jugador around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.mover_x

        # See if we hit the jugador
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the jugador. Shove the jugador around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.mover_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.mover_y

        # Check and see if we the jugador
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the jugador. Shove the jugador around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.mover_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.mover_y *= -1

        cur_pos = self.rect.x - self.nivel.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.mover_x *= -1
