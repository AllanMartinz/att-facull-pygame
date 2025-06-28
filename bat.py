import pygame
from settings import *
from collections import deque

class Bat(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.all_sprites_group)
        self.game = game
        self.image = game.bat_images[0]
        self.mask = pygame.mask.from_surface(game.mask_image)
        self.rect = self.image.get_rect()
        self.rect.center = BAT_START_POS

        self.images = deque(game.bat_images)
        self.animation_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.animation_event, BAT_FLAP_INTERVAL)

        self.falling_velocity = 0
        self.first_jump = False
        self.angle = 0

    def check_collision(self):
        hit = pygame.sprite.spritecollide(self, self.game.obs_group, False, collided=pygame.sprite.collide_mask)
        if hit or self.rect.bottom > GROUND_Y_POS or self.rect.top < -self.image.get_height():
            self.game.sound.hit_sound.play()
            pygame.time.wait(1000)
            self.game.new_game()

    def rotate(self):
        if self.first_jump:
            if self.falling_velocity < -BAT_JUMP_VELOCITY:
                self.angle = BAT_ROTATE_ANGLE
            else:
                self.angle = max(-1.5 * self.falling_velocity, -40)
            self.image = pygame.transform.rotate(self.image, self.angle)

            # new mask
            mask_image = pygame.transform.rotate(self.game.mask_image, self.angle)
            self.mask = pygame.mask.from_surface(mask_image)

    def jump(self):
        # self.game.sound.point_sound.play()
        self.game.sound.wing_sound.play()
        self.first_jump = True
        self.falling_velocity = BAT_JUMP_VELOCITY

    # v = v0 + at --- x = x0 + v0t + 1/2 at^2
    def use_gravity(self):
        if self.first_jump:
            self.falling_velocity += GRAVITY_FORCE
            self.rect.y += self.falling_velocity + 0.5 * GRAVITY_FORCE

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