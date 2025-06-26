import pygame
import sys
from bat import *
from obstacles import *
from game_objects import *
from settings import *

class FlappyBat:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN))
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.new_game()

    def load_assets(self):
        #bat
        self.bat_images = [pygame.image.load(f"package/images/bat/{i}.png").convert_alpha() for i in range(4)]
        bat_images = self.bat_images[0]
        bat_size = bat_images.get_width() * BAT_SCALE, bat_images.get_height() * BAT_SCALE
        self.bat_images = [pygame.transform.scale(sprite, bat_size) for sprite in self.bat_images]

        # background
        self.background_image = pygame.image.load("package/images/objs/background.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, WIN)

    def new_game(self):
        self.all_sprites_group = pygame.sprite.Group()
        self.bat = Bat(self)
        self.background = Background(self)

    def draw(self):
        self.background.draw()
        self.all_sprites_group.draw(self.screen)
        pygame.display.update()

    def update(self):
        self.background.update()
        self.all_sprites_group.update()
        self.clock.tick(FRAME_RATE)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.bat.check_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = FlappyBat()
    game.run()


