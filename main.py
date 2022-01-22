import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screen_widgth = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_widgth, screen_height))
pygame.display.set_caption('pong')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
