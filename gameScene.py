import pygame
import random
from Framework.sceneManager import Scene, SceneManager
from Framework.animation import Animation

class gameScene(Scene) :

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        load_resources()

    def update(self) :
        self.group.update()
        self.new_anim.set_position((random.randrange(0, 200),100))
        self.screen.fill(pygame.Color('white'))
        self.group.draw(self.screen)

    def load_resources(self) :
        self.water_list = list()
        for i in range(8) :
            self.water_list.append('./Resources/Images/Water/'+str(i+1)+'.png')
        self.top_water = Animation(self.water_list,10)
        self.group = pygame.sprite.Group(self.top_water)
