import pygame
import os
import time
from bird import Bird
from pipe import PipeGenerator

BLACK = (0, 0, 0)
YELLO = (255, 255, 0)
WHITE = (255,255,255)

# pygame.init()
WINDOW_SIZE = (1200, 768)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
running = True

bird = Bird(200, 200, YELLO)
g = pygame.sprite.Group()
g.add(bird)


t = PipeGenerator()
t.generate()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.jump()

    bird.move()
    t.move()

    SCREEN.fill(BLACK)
    SCREEN.blit(bird.image, bird.rect)
    t.draw(SCREEN)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
