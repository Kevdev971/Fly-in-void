import pygame
LOCAL = [
    400,300,
    "Test game 0.1"
]
pygame.init()
pygame.display.set_caption(LOCAL[2])
pygame.display.set_mode((LOCAL[0],LOCAL[1]))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            print("KEY")
        if event.type == pygame.KEYDOWN:
            print("KEY")
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()