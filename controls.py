import pygame
import sys
from bullet import Bullet
from monster import Monster
import time


def events(screen, gun, bullets):
    """ Обработка событий """

    for event in pygame.event.get():  # события пользователя
        if event.type == pygame.QUIT:  # если пользователь нажимает крестик, что бы закрыть игру, то
            sys.exit()  # этот метод закрывает игру

        elif event.type == pygame.KEYDOWN:
            #  движение вправо
            if event.key == pygame.K_d:
                gun.mright = True
                #  движение влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            #  движение вправо
            if event.key == pygame.K_d:
                gun.mright = False
                #  движение влево
            elif event.key == pygame.K_a:
                gun.mleft = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)


def update(bg_color, screen, stats, sc, gun, monsters, bullets):
    """ Обновление экрана """
    screen.fill(bg_color)  # фоновый цвет (заливка)
    sc.show_score()  # отрисовываем счет на экране
    for bullet in bullets.sprites():
        bullet.update_up()
        bullet.draw_bullet()
    gun.output()  # отрисовываем пушку на экране
    monsters.draw(screen)  #отрисовываем монстров на экране
    pygame.display.flip()  # прорисовка последнего экрана
    bullets.remove()


def update_bullets(screen, stats, sc, monsters, bullets):
    """ Обновление позиции пули """
    bullets.update()  # обновление позиции пуль
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, monsters, True, True)  # Словарь где первый аргумент пули, второй группа монстров, 3 -4 аругменты это активные состояния, если пули Фолс, то пуля не пропадает и пушит дальше, а если монстры Фолс, то они не воспринимают пули.
    if collisions:
        for monsters in collisions.values():
            stats.score += 10 * len(monsters)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_health_points()

    if len(monsters) == 0:
        time.sleep(1)
        bullets.empty()
        stats.health += 1
        if stats.health > 5:
            stats.health = 5
        sc.image_health_points()
        create_army(screen, monsters)


def gun_kill(stats, screen, sc, gun, monsters, bullets):
    """ Столкновение пушки и армии """
    if stats.health > 0:
        stats.health -= 1
        sc.image_health_points()
        monsters.empty()
        bullets.empty()
        create_army(screen, monsters)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_monsters(stats, screen, sc, gun, monsters, bullets):
    """ Обновляет позицию монстров """
    monsters.update()
    if pygame.sprite.spritecollideany(gun, monsters):
        gun_kill(stats, screen, sc, gun, monsters, bullets)
    monsters_check(stats, screen, sc, gun, monsters, bullets)


def monsters_check(stats, screen, sc, gun, monsters, bullets):
    """ Проверка касания армии конца игрового экрана """
    screen_rect = screen.get_rect()
    for monster in monsters.sprites():
        if monster.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, monsters, bullets)
            break


def create_army(screen, monsters):
    """ Создание армии монстров """
    monster = Monster(screen)
    monster_width = monster.rect.width
    number_monster_x = int((700 - 2 * monster_width) / monster_width)
    monster_height = monster.rect.height
    number_monster_y = int((800 - 80 - 10 * monster_height) / monster_height)

    for row_number in range(number_monster_y):  # кол-во рядов
        for monster_number in range(number_monster_x-1):  # кол-во монстров в 1 ряду
            monster = Monster(screen)
            monster.x = monster_width + monster_width * monster_number
            monster.y = monster_height + monster_height * row_number + 30  # Расположение изображения на экране по оси Y во время движения
            monster.rect.x = monster.x + 25  # Расположение изображения на экране по оси X
            monster.rect.y = monster.rect.height + monster.rect.height * row_number + 30  # Расположение изображения на экране по оси Y
            monsters.add(monster)


def check_high_score(stats, sc):
    """ Проверка новых рекордов """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('high_score.txt', 'w') as file:
            file.write(str(stats.high_score))
