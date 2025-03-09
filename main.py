import pygame
LOCAL = [
    800,600,
    "Test game 0.2"
]
speed = 10
playerX = 400
playerY = 300
pygame.init()
pygame.display.set_caption(LOCAL[2])
screen = pygame.display.set_mode((LOCAL[0],LOCAL[1]))
screen_rect = screen.get_rect()
pygame.time.Clock().tick(60)
player = pygame.image.load("image/player.png")
Player = player.get_rect()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Player.y -= speed

    if keys[pygame.K_DOWN]:
        Player.y += speed
    
    if keys[pygame.K_LEFT]:
        Player.x -= speed

    if keys[pygame.K_RIGHT]:
        Player.x += speed

    screen.blit(player,Player)
    pygame.display.update()
pygame.quit()