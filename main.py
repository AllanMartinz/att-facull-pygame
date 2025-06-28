import pygame
import sys
from bat import *
from obstacles import *
from game_objects import *
from settings import *

class FlappyBat:
    def __init__(self):
        pygame.init()

        # janela e relogio
        self.screen = pygame.display.set_mode((WINDOW_SIZE))
        self.title = pygame.display.set_caption("Flappy Bat")
        self.clock = pygame.time.Clock()
        # carega assets
        self.load_assets()
        # score
        self.sound = Sound()
        self.score = Score(self)
        # novo jogo
        self.new_game()

    def load_assets(self):
        #carregas os assets
        # bat
        self.bat_images = [pygame.image.load(f"assets/images/bat/fly/f{i}.png").convert_alpha() for i in range(4)]
        bat_images = self.bat_images[0]
        bat_size = bat_images.get_width() * BAT_SCALE, bat_images.get_height() * BAT_SCALE
        self.bat_images = [pygame.transform.scale(sprite, bat_size) for sprite in self.bat_images]
        '''
         self.background_image = pygame.transform.scale(
            pygame.image.load("package/images/objs/background.png").convert(), WINDOW_SIZE)
        self.ground_image = pygame.transform.scale(
            pygame.image.load("package/images/objs/Terrain.png").convert(), (SCREEN_WIDTH, GROUND_HEIGHT))
        '''
        # background
        self.background_image = pygame.image.load("assets/images/objs/background3.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, WINDOW_SIZE)
        # foreground
        self.foreground_image = pygame.image.load("assets/images/objs/Foreground.png").convert_alpha()
        self.foreground_image = pygame.transform.scale(self.foreground_image, WINDOW_SIZE)
        # ground
        self.ground_image = pygame.image.load("assets/images/objs/Terrain3.png").convert_alpha()
        self.ground_image = pygame.transform.scale(self.ground_image, (SCREEN_WIDTH, GROUND_HEIGHT))
        # obstacles
        self.top_obs_image = pygame.image.load("assets/images/objs/Obstacle_Up.png").convert_alpha()
        self.top_obs_image = pygame.transform.scale(self.top_obs_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.bottom_obs_image = pygame.transform.flip(self.top_obs_image, False, True )
        '''
        self.top_obstacle_image = pygame.transform.scale(
            pygame.image.load("package/images/objs/Obstacle_Up.png").convert_alpha(),
            (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        mask_image = pygame.image.load("package/images/bat/mask.png").convert_alpha()
        mask_size = pygame.transform.scale(mask_raw, frame_size)
        self.mask_image = mask_scaled
        '''
        # bat mask
        mask_image = pygame.image.load("assets/images/bat/mask.png").convert_alpha()
        mask_size = mask_image.get_width() * BAT_SCALE, mask_image.get_height() * BAT_SCALE
        self.mask_image = pygame.transform.scale(mask_image,mask_size)

    def new_game(self):
        # musica
        self.sound.music_level.play()
        # grupo sprite
        self.all_sprites_group = pygame.sprite.Group()
        self.obs_group = pygame.sprite.Group()
        #instancia obj
        self.bat = Bat(self)
        self.background = Background(self)
        self.foreground = Foreground(self)
        self.ground = Ground(self)
        self.obs_handler = ObstacleHandler(self)

    def draw(self):
        # desenha os assets
        self.background.draw()
        self.foreground.draw()
        self.all_sprites_group.draw(self.screen)
        self.ground.draw()
        self.score.draw()
        # atualiza os frames
        pygame.display.update()
        '''
        #testes
        pygame.draw.rect(self.screen, "yellow", self.bat.rect, 4)
        pygame.draw.rect(self.screen, "yellow", self.top_obs_image.rect, 4)
        self.bat.mask.to_surface(self.screen, unsetcolor=None, dest=self.bat.rect, setcolor="yellow")
        pygame.display.flip()
        '''

    def update(self):
        # atualiza o game
        self.background.update()
        self.foreground.update()
        self.all_sprites_group.update()
        self.ground.update()
        self.obs_handler.update()
        self.clock.tick(FRAME_RATE)

    def check_events(self):
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.bat.check_event(event)

    def run(self):
        # loop
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = FlappyBat()
    game.run()


