import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()  # инициализация игры
    screen = pygame.display.set_mode((700, 800))  # размер игрового окна
    pygame.display.set_caption("Космические защитники")  # заголовок игры
    bg_color = (0, 0, 0)  # фоновый цвет окна
    gun = Gun(screen)  # создаем объект пушки
    bullets = Group()  # создаем объект пуль
    monsters = Group()  # создаем объект монстров
    controls.create_army(screen, monsters)  # создаем армию монстров
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()  # обновление позиции пушки
            controls.update(bg_color, screen, stats, sc, gun, monsters, bullets)  # вызываем функцию обновления экрана
            controls.update_bullets(screen, stats, sc, monsters, bullets)
            controls.update_monsters(stats, screen, sc, gun, monsters, bullets)


run()
