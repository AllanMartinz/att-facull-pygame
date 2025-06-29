import pygame
from settings import *

# desenha pontuacao
class Score:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font("assets/images/font/Jersey.ttf", 90)
        self.font_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 12)

    def draw(self):
        score = self.game.obs_handler.passed_obs
        self.text = self.font.render(f"{score}", True, "white")
        self.game.screen.blit(self.text, self.font_pos)

# carrega/toca os sons
class Sound:
    def __init__(self):
        self.music_level = pygame.mixer.Sound("assets/audio/music/Background-Music.mp3")
        self.hit_sound = pygame.mixer.Sound("assets/audio/sound/Death.mp3")
        self.point_sound = pygame.mixer.Sound("assets/audio/sound/Click.mp3")
        self.wing_sound = pygame.mixer.Sound("assets/audio/sound/Fly.mp3")

# classe desenha o fundo
class Background:
    def __init__(self, game):
        self.game = game
        self.x = 0
        self.y = 0
        self.speed = SCROLL_VELOCITY - 2
        self.image = self.game.background_image

    def update(self):
        self.x = (self.x - self.speed) % -SCREEN_WIDTH

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))
        self.game.screen.blit(self.image, (SCREEN_WIDTH + self.x, self.y))

# classe desenha elementos primeiro plano
class Foreground(Background):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.x = 0
        self.y = 0
        self.speed = SCROLL_VELOCITY - 0.5
        self.image = self.game.foreground_image

    def update(self):
        self.x = (self.x - self.speed) % -SCREEN_WIDTH

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))
        self.game.screen.blit(self.image, (SCREEN_WIDTH + self.x, self.y))

# classe para o chao
class Ground(Background):
    def __init__(self, game):
        super().__init__(game)
        # define posicao final da tela
        self.y = GROUND_Y_POS
        # acompanhar obstaculos
        self.speed = SCROLL_VELOCITY
        self.image = self.game.ground_image