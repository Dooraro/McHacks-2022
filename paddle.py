import pygame
black = (0,0,0)

class paddle(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 10:
            self.rect.y = 10

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 750:
            self.rect.y = 750
