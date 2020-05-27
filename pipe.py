import pygame
import random

BLACK = (0, 0, 0)
YELLO = (255, 255, 0)
WHITE = (255,255,255)

class Pipe(pygame.sprite.Sprite):
    SIZE = (60, 650)

    def __init__(self, x, y):
        super().__init__();
        self.image = pygame.Surface(self.SIZE)
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PipeGenerator():
    def __init__(self):
        self.pipes = []
        self.pipesGroup = pygame.sprite.Group()

    def generate(self):
        height = random.randrange(400)
        topPip = Pipe(1100, height - Pipe.SIZE[1])
        bottomPip = Pipe(1100, 150 + height)

        self.pipes.append(topPip)
        self.pipes.append(bottomPip)
        self.pipesGroup.add(topPip)
        self.pipesGroup.add(bottomPip)

    def draw(self, screen:pygame.Surface):
        self.pipesGroup.draw(screen)

    def move(self):
        for pip in self.pipes:
            pip.rect.x -= 5