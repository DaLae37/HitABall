import pygame
from Framework.sceneManager import Scene, SceneManager
from Framework.animation import Animation

class mainScene(Scene) :

    def __init__(self, screen,clock) :
        self.screen = screen
        self.clock = clock

        self.tmp_anim = list()
        for i in range(8) :
            self.tmp_anim.append('./Resources/Images/Water/'+str(i+1)+'.png')
        self.new_anim = Animation(self.tmp_anim,10)
        self.group = pygame.sprite.Group(self.new_anim)

    def update(self) :
        self.group.update()
        self.screen.fill(pygame.Color('white'))
        self.group.draw(self.screen)
