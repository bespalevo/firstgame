import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """ Создаем пулю в текущей позиции пушки """
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 20)  # 0, 0 это координаты появления пули. 2 пикселя ширины пули. 12 пикселей высота пули.
        self.color = 37, 51, 183
        self.speed = 4
        self.rect.centerx = gun.rect.centerx  # Координаты появления пули

        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update_up(self):
        """ Перемещение пули вверх """
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Рисуем пулю на экране """
        pygame.draw.rect(self.screen, self.color, self.rect)

