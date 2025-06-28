import pygame
from settings import *
import random


# classe obstaculo superior
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

# classe obstaculo inferior
class BottomObs(TopObs):
    def __init__(self, app, gap_y_pos):
        super().__init__(app, gap_y_pos)
        self.image = app.bottom_obs_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = SCREEN_WIDTH, gap_y_pos + HALF_GAP - GROUND_HEIGHT

#classe controla criacao/verificao obstaculos
class ObstacleHandler:
    def __init__(self, game):
        self.game = game
        self.obs_dist = OBSTACLE_SPACING
        self.obstacles = []
        self.passed_obs = 0
    '''
    def spawn_if_needed(self):
        if self.game.bat.first_flap:
            self.distance_since_last += SCROLL_VELOCITY
            if self.distance_since_last >= OBSTACLE_SPACING:
                self.distance_since_last = 0
                gap_y = self.get_gap_y_position()

                ObstacleTop(self.game, gap_y)
                bottom = ObstacleBottom(self.game, gap_y)
                self.spawned_obstacles.append(bottom)
    '''
    def count_passed_obs(self):
        # verifica se passou de algum obstaculo(score)
        for obst in self.obstacles:
            if BAT_START_POS[0] > obst.rect.right:
                self.game.sound.point_sound.play()
                self.passed_obs += 1
                self.obstacles.remove(obst) # removepara nao contar denovo

    def update(self):
        # atualiza logica obstaculos
        self.generate_objs()
        self.count_passed_obs()

    @staticmethod
    def get_gap_y_position():
            # posicao aleatoria dos obstaculos
            min_y = SCREEN_HEIGHT - 500
            max_y = SCREEN_HEIGHT - 100
            return random.randint(min_y, max_y)

    def generate_objs(self):
        # gera obstaculos apos primeiro pulo
        if self.game.bat.first_jump:
            self.obs_dist += SCROLL_VELOCITY
            # cria novos obstaculos apos certa distancia
            if self.obs_dist > OBSTACLE_SPACING:
                self.obs_dist = 0
                gap_y = self.get_gap_y_position()
                # cria obstaculos cima e baixo
                TopObs(self.game, gap_y)
                obst = BottomObs(self.game, gap_y)
                #conatgem pontos apaertir do obstaculo unferior
                self.obstacles.append(obst)

