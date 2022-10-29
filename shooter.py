import pygame

class Shooter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/enemy/cangaciro2.png")
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (490, 520))


    def createb(self):
        return Bullets(self.rect.x, self.rect.y)
    
    def prepare(self):
        self.image = pygame.image.load("sprites/enemy/cangaciro1.png")

    def wait(self):
        self.image = pygame.image.load("sprites/enemy/cangaciro2.png")

class Bullets(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()
        self.image = pygame.image.load("sprites/enemy/bullet.png")
        self.rect = self.image.get_rect(center = (px + 40, py + 18))

    def update(self, xx):
        self.rect.x += 15

        if self.rect.x > 700:
            self.image = pygame.image.load("sprites/enemy/firebullet.png")
        
        if self.rect.x > 1020:
            self.image = pygame.image.load("sprites/enemy/explosion.png")

        if self.rect.x > 1050:
            self.kill()
    
    def location(self):
        return (self.rect.x, self.rect.y)