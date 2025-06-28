import pygame
from settings import *
import random



class TopObs(pygame.sprite.Sprite):
    def __init__(self, app, gap_y_pos):
        super().__init__(app.obs_group, app.all_sprites_group)
        self.image = app.top_obs_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = SCREEN_WIDTH, gap_y_pos - HALF_GAP - GROUND_HEIGHT

    def update(self):
        self.rect.left -= SCROLL_VELOCITY
        if self.rect.right < 0:
            self.kill()

class BottomObs(TopObs):
    def __init__(self, app, gap_y_pos):
        super().__init__(app, gap_y_pos)
        self.image = app.bottom_obs_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = SCREEN_WIDTH, gap_y_pos + HALF_GAP - GROUND_HEIGHT

class ObstacleHandler:
    def __init__(self, game):
        self.game = game
        self.obs_dist = OBSTACLE_SPACING
        self.obstacles = []
        self.passed_obs = 0

    def count_passed_obs(self):
        for obst in self.obstacles:
            if BAT_START_POS[0] > obst.rect.right:
                self.game.sound.point_sound.play()
                self.passed_obs += 1
                self.obstacles.remove(obst)

    def update(self):
        self.generate_objs()
        self.count_passed_obs()

    @staticmethod
    def get_gap_y_position():
            min_y = SCREEN_HEIGHT // 2  # ou um valor como 200
            max_y = SCREEN_HEIGHT - 100  # para não colar no chão
            return random.randint(min_y, max_y)

    def generate_objs(self):
        if self.game.bat.first_jump:
            self.obs_dist += SCROLL_VELOCITY
            if self.obs_dist > OBSTACLE_SPACING:
                self.obs_dist = 0
                gap_y = self.get_gap_y_position()

                TopObs(self.game, gap_y)
                obst = BottomObs(self.game, gap_y)
                self.obstacles.append(obst)