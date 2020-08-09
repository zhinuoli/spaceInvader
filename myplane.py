import pygame

class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.transform.scale(pygame.image.load("images/me1.jpg").convert_alpha(), (100, 100))
        self.image2 = pygame.transform.scale(pygame.image.load("images/me2.jpg").convert_alpha(), (100, 100))
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.transform.scale(pygame.image.load("images/me_destroy_1.jpg").convert_alpha(), (100, 100)), \
            pygame.transform.scale(pygame.image.load("images/me_destroy_2.jpg").convert_alpha(), (100, 100)), \
            pygame.transform.scale(pygame.image.load("images/me_destroy_3.jpg").convert_alpha(), (100, 100)), \
            pygame.transform.scale(pygame.image.load("images/me_destroy_4.jpg").convert_alpha(), (100, 100)) \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True