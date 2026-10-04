import pygame
import random


# --- Константы ---
class WolfAndEggConsts:
    screen_width = 400
    screen_height = 600
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    clock_ticks = 60


# --- Базовый класс для объектов со столкновениями ---
class CollidableObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0

    def collide(self, other):
        """Проверка столкновения с другим объектом"""
        return (other.y + other.height > self.y and
                other.x + other.width > self.x and
                other.x < self.x + self.width and
                self.y < other.y + other.height)

    def get_parameters(self):
        return self.x, self.y, self.width, self.height

    def collide_with_right_border(self):
        # Возвращает True, если объект НЕ касается правой границы (то есть может двигаться вправо)
        return self.x + self.width < WolfAndEggConsts.screen_width

    def collide_with_left_border(self):
        # Возвращает True, если объект НЕ касается левой границы (может двигаться влево)
        return self.x > 0

    def collide_with_bottom_border(self):
        # Возвращает True, если объект коснулся нижней границы
        return self.y + self.height >= WolfAndEggConsts.screen_height


# --- Счётчик очков ---
class Counters:
    score = 0


# --- Класс Яйца ---
class Egg(CollidableObject):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 30
        self.egg_speed = 3
        self.spawn()

    def move(self):
        self.y += self.egg_speed

    def spawn(self):
        self.x = random.randint(0, WolfAndEggConsts.screen_width - self.width)
        self.y = -self.height  # Появляется чуть выше экрана
        # Увеличиваем скорость со временем (опционально, можно убрать)
        # self.egg_speed += 0.1

    def border_touch(self):
        if self.collide_with_bottom_border():
            self.spawn()
            return True
        return False


# --- Класс Игрока (Волка) ---
class Player(CollidableObject):
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 50
        self.x = WolfAndEggConsts.screen_width / 2 - self.width / 2
        self.y = WolfAndEggConsts.screen_height - self.height
        self.player_speed = 7  # Чуть быстрее для удобства

    def move_left(self):
        if self.collide_with_left_border():
            self.x -= self.player_speed

    def move_right(self):
        if self.collide_with_right_border():
            self.x += self.player_speed


# --- Основной класс Игры ---
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WolfAndEggConsts.screen_width, WolfAndEggConsts.screen_height))
        pygame.display.set_caption("Волк и яйца")
        self.font = pygame.font.SysFont(None, 30)

        self.counters = Counters()
        self.player = Player()
        self.egg = Egg()

        self.is_running = True

    def update_scene(self):
        self.screen.fill(WolfAndEggConsts.white)

        # Рисуем игрока (прямоугольник)
        pygame.draw.rect(self.screen, WolfAndEggConsts.black, self.player.get_parameters())

        # Рисуем яйцо (эллипс)
        pygame.draw.ellipse(self.screen, WolfAndEggConsts.red, self.egg.get_parameters())

        # Отрисовка счёта
        score_text = self.font.render(f"Score: {self.counters.score}", True, WolfAndEggConsts.black)
        self.screen.blit(score_text, (10, 10))

        pygame.display.update()
        self.clock.tick(WolfAndEggConsts.clock_ticks)

    def run_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()

        self.egg.move()

        # Проверка столкновений
        if self.player.collide(self.egg):
            self.counters.score += 1
            self.egg.spawn()
        elif self.egg.border_touch():
            # Яйцо упало мимо — штраф
            self.counters.score -= 1
            self.egg.spawn()

    def start_run(self):
        while self.is_running:
            self.run_logic()
            self.update_scene()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start_run()