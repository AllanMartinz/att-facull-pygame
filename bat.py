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

        self.falling_velocity = 0
        self.first_jump = False
        self.angle = 0

    def check_collision(self):
        if self.rect.bottom > GROUND_Y or self.rect.top < -self.image.get_height():
            self.game.sound.hit_sound.play()
            pygame.time.wait(1000)
            self.game.new_game()

    def rotate(self):
        if self.first_jump:
            if self.falling_velocity < -BAT_JUMP_VALUE:
                self.angle = BAT_JUMP_ANGLE
            else:
                self.angle = max(-1.5 * self.falling_velocity, -40)
            self.image = pygame.transform.rotate(self.image, self.angle)

    def jump(self):
        self.game.sound.point_sound.play()
        self.game.sound.wing_sound.play()
        self.first_jump = True
        self.falling_velocity = BAT_JUMP_VALUE

    # v = v0 + at --- x = x0 + v0t + 1/2 at^2
    def use_gravity(self):
        if self.first_jump:
            self.falling_velocity += GRAVITY
            self.rect.y += self.falling_velocity + 0.5 * GRAVITY

    def update(self):
        self.check_collision()
        self.use_gravity()

    def animate(self):
        self.images.rotate(-1)
        self.image = self.images[0]

    def check_event(self, event):
        if event.type == self.animation_event:
            self.animate()
            self.rotate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.jump()