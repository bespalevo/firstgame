import pygame.font
from pygame.sprite import Group
from health import Health


class Scores():
    """ Вывод игровой информации """
    def __init__(self, screen, stats):
        """ Инициализируем подсчет очков """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 0)  # Цвет счета очков
        self.font = pygame.font.SysFont(None, 36)  # первый аргумент - шрифт (None (по умолчанию)), второй аргумент размер шрифта
        self.image_score()
        self.image_high_score()
        self.image_health_points()

    def image_score(self):
        """ Преобразовывает текст счета в графическое изображение """
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))  # 1 - аргумент шритф как строковый тип, 3 - аргмент какого цвета текст, 4 аргумент - цвет фона изображения
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40  # Расположение очков счета в правом стороне экрана
        self.score_rect.top = 20  # Расположение очков счета в верхней стороне экрана

    def image_high_score(self):
        """ Преобразует рекорд в графическое изображение """
        self.transformation_hige_scrore_in_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.transformation_hige_scrore_in_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # Расположение картинки по оси X с лучшим счетом игры
        self.high_score_rect.top = self.screen_rect.top + 20  # Расположение картинки по оси Y с лучшим счетом игры

    def image_health_points(self):
        """ Кол-во жизней """
        self.health = Group()
        for health_num in range(self.stats.health):
            health = Health(self.screen)
            health.rect.x = 15 + health_num * health.rect.width  # Расположение очков жизни на экране по оси X
            health.rect.y = 20  # Расположение очков жизни на экране по оси X
            self.health.add(health)

    def show_score(self):
        """ Вывод счета на экран """

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.transformation_hige_scrore_in_image, self.high_score_rect)
        self.health.draw(self.screen)


