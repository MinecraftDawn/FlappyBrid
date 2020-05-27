import pygame
import os
import time
from bird import Bird

BLACK = (0, 0, 0)
YELLO = (255, 255, 0)
WHITE = (255,255,255)

# pygame.init()
WINDOW_SIZE = (800, 800)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
running = True

bird = Bird(200, 200, YELLO)
g = pygame.sprite.Group()
g.add(bird)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    SCREEN.fill(BLACK)
    SCREEN.blit(bird.image, bird.rect)
    bird.move()

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
