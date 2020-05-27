import pygame
class Bird(pygame.sprite.Sprite):
    SIZE = 30

    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([self.SIZE, self.SIZE])
        pygame.draw.circle(self.image, color, (self.SIZE // 2, self.SIZE // 2), self.SIZE // 2)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 0
        self.tick = 0

    def jump(self):
        self.vel = -6
        self.tick = 0

    def move(self):
        self.tick += 1

        displacement = self.vel * self.tick + 0.5 * self.tick ** 2

        if displacement > 16:
            displacement = 16
        # elif displacement < 0:
        #     displacement -= 1

        self.rect.y += displacement