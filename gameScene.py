import pygame
import random
import math
from Framework.sceneManager import Scene, SceneManager
from Framework.animation import Animation
from Framework.simple_image import SimpleImage

class gameScene(Scene) :

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock
        self.isMove = False
        self.t = 0
        self.load_resources()

    def update(self) :
        self.group.update()
        self.top_water.set_position((500,500))
        self.screen.fill(pygame.Color('white'))
        self.group.draw(self.screen)

        self.screen.blit(self.ball.getSurface(),self.ball.getPos())

        if self.isMove :
            self.ball.addPos((-200 * math.cos(45), -200 * math.cos(45) + 9.8 * self.t))
            self.t+=1

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                self.isMove = True

    def load_resources(self) :
        self.water_list = list()
        for i in range(8) :
            self.water_list.append('Resources/Images/Water/'+str(i+1)+'.png')
        self.top_water = Animation(self.water_list,math.sqrt(9.8*100/(2 * math.pi) * math.tanh(2 * math.pi)))
        self.group = pygame.sprite.Group(self.top_water)

        self.ball = SimpleImage("Resources/Images/Object/Ball.png")
        self.ball.setPos((1200, 600))
