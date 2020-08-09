import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load("images/enemy1.jpg").convert_alpha(), (100, 100))
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.transform.scale(pygame.image.load("images/enemy1_down1.jpg").convert_alpha(), (100, 100)), \
            pygame.transform.scale(pygame.image.load("images/enemy1_down2.jpg").convert_alpha(), (100, 100)), \
            pygame.transform.scale(pygame.image.load("images/enemy1_down3.jpg").convert_alpha(), (100, 100)), \
            pygame.transform.scale(pygame.image.load("images/enemy1_down4.jpg").convert_alpha(), (100, 100)) \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load("images/enemy2.jpg").convert_alpha(), (200, 200))
        self.image_hit = pygame.transform.scale(pygame.image.load("images/enemy2_hit.jpg").convert_alpha(), (200, 200))
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.transform.scale(pygame.image.load("images/enemy2_down1.jpg").convert_alpha(), (200, 200)), \
            pygame.transform.scale(pygame.image.load("images/enemy2_down2.jpg").convert_alpha(), (200, 200)), \
            pygame.transform.scale(pygame.image.load("images/enemy2_down3.jpg").convert_alpha(), (200, 200)), \
            pygame.transform.scale(pygame.image.load("images/enemy2_down4.jpg").convert_alpha(), (200, 200)) \
            ])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-10 * self.height, -self.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 12
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.transform.scale(pygame.image.load("images/enemy3_n1.jpg").convert_alpha(), (250, 250))
        self.image2 = pygame.transform.scale(pygame.image.load("images/enemy3_n2.jpg").convert_alpha(), (250, 250))
        self.image_hit = pygame.transform.scale(pygame.image.load("images/enemy3_hit.jpg").convert_alpha(), (250, 250))
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.transform.scale(pygame.image.load("images/enemy3_down1.jpg").convert_alpha(), (250, 250)), \
            pygame.transform.scale(pygame.image.load("images/enemy3_down2.jpg").convert_alpha(), (250, 250)), \
            pygame.transform.scale(pygame.image.load("images/enemy3_down3.jpg").convert_alpha(), (250, 250)), \
            pygame.transform.scale(pygame.image.load("images/enemy3_down4.jpg").convert_alpha(), (250, 250)), \
            pygame.transform.scale(pygame.image.load("images/enemy3_down5.jpg").convert_alpha(), (250, 250)), \
            pygame.transform.scale(pygame.image.load("images/enemy3_down6.jpg").convert_alpha(), (250, 250)) \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
                        randint(0, self.width - self.rect.width), \
                        randint(-15 * self.height, -5 * self.height)