import pygame


class Monster(pygame.sprite.Sprite):
    """ Класс одного пришельца """
    def __init__(self, screen):
        """ Инициализируем и задаем начальную позицию """
        super(Monster, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixel_monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """ Вывод пришельца на экран.
         Этот метод работает только для одного монстра, если в файле space_game.py в
         функции run мы создаем объект 1 монстра, то есть вместо monsters = Group()
         мы создаем объект monster = Monster(screen) и дополнительно объявляем его в
         файле controls.py в функции update вместо monsters.draw(screen) пишем
         monster.draw(screen), в противном случае, данный метод не имеет значения.
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Перемещает монстров """
        self.y += 0.03
        self.rect.y = self.y
