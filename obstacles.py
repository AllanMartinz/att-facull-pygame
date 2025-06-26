import pygame
from settings import *
import random



class TopObs(pygame.sprite.Sprite):
    def __init__(self, app, gap_y_pos):
        super().__init__(app.obs_group, app.all_sprites_group)
        self.image = app.top_obs_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = WIDTH, gap_y_pos - HALF_GAP_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect.left -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()

class BottomObs(TopObs):
    def __init__(self, app, gap_y_pos):
        super().__init__(app, gap_y_pos)
        self.image = app.bottom_obs_image
        self.rect.topleft = WIDTH, gap_y_pos + HALF_GAP_HEIGHT - GROUND_HEIGHT

class ObstacleHandler:
    def __init__(self, game):
        self.game = game
        self.obs_dist = DIST_BETWEEN_OBS

    def update(self):
        self.generate_objs()

    @staticmethod
    def get_gap_y_position():
            min_y = HEIGHT // 2  # ou um valor como 200
            max_y = HEIGHT - 100  # para não colar no chão
            return random.randint(min_y, max_y)

    def generate_objs(self):
        if self.game.bat.first_jump:
            self.obs_dist += SCROLL_SPEED
            if self.obs_dist > DIST_BETWEEN_OBS:
                self.obs_dist = 0
                gap_y = self.get_gap_y_position()

                TopObs(self.game, gap_y)
                BottomObs(self.game, gap_y)