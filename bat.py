import pygame
from settings import *
from collections import deque

class Bat(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.all_sprites_group)
        self.game = game
        self.image = game.bat_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = BAT_POS

        self.images = deque(game.bat_images)
        self.animation_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.animation_event, BAT_ANIMATION_TIME)

    def animate(self):
        self.images.rotate(-1)
        self.image = self.images[0]

    def check_event(self, event):
        if event.type == self.animation_event:
            self.animate()