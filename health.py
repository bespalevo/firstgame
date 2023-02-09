import pygame
from pygame.sprite import Sprite


class Health(Sprite):
    def __init__(self, screen):
        """ Инициализация жизней """
        super(Health, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/healthPng.png')
        self.rect = self.image.get_rect()
        self.rect.width = 40  # Расстояние между изображениями "жизни"
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom



    def output(self):
        """ Рисование health """
        self.screen.blit(self.image, self.rect)
