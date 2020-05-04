import pygame
from pygame.locals import *
from sonic import Player

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

# Ecran
screen = pygame.display.set_mode((1000, 707))
pygame.display.set_caption("Sonic Green Hills")

#Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

image = pygame.image.load("greenhillzone.png")
imagex = 0
imagey = 0
direction = "left"




player = Player()

while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(image, (imagex, imagey))
    pygame.display.update()
    fpsClock.tick(FPS)