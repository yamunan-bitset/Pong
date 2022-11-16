import pygame
pygame.init()
W = 1200
H = 720
display = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
dt = pygame.time.get_ticks()
run = True
paddle = pygame.Rect(50, H / 2, 20, 100)
enemy = pygame.Rect(W - 20 - 50, H / 2, 20, 100)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if paddle.y > 0:
            paddle.move_ip(0,-5)
    if pressed[pygame.K_DOWN]:
        if paddle.y + paddle.h < H:
            paddle.move_ip(0, 5)
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 255, 255), paddle)
    pygame.draw.rect(display, (255, 255, 255), enemy)
    pygame.display.update()
