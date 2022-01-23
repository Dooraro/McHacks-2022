import pygame, sys
from paddle import paddle
from ball import Ball

pygame.init()
clock = pygame.time.Clock()

BLACK = (0,255,0)
WHITE = (255, 0,255)

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('pong')

paddleA = paddle(WHITE, 10, 200)
paddleA.rect.x = 20
paddleA.rect.y = 530

paddleB = paddle(WHITE, 10, 200)
paddleB.rect.x = 1250
paddleB.rect.y = 530

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.KEYDOWN:
                carryOn=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 1250:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 950:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [639, 0], [639, 960], 5)
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (540, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (710, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
