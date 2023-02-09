

class Stats():
    """ Отслеживание статистики """
    def __init__(self):
        """ Инициализирует статистику """
        self.health = 3  # Кол-во жизней
        self.score = 0  # Счет с начала новой сессии
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """ Статистика, изменяющаяся во время игры """
        return self.health, self.score







