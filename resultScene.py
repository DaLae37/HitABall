import pygame
from typing import TYPE_CHECKING
from Framework.sceneManager import Scene, SceneManager
from Framework.soundManager import SoundManager
from Framework.animation import Animation
from Framework.simple_image import SimpleImage

class resultScene(Scene) :

    simple_image_list = []

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        self.load_resources()

    def update(self) :

        for si in self.simple_image_list :
            self.screen.blit(si.getSurface(), si.getPos())

        self.screen.blit(self.title, (350,100))

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.startButton.isCollisionRect(pygame.mouse.get_pos()) :
                    from mainScene import mainScene
                    SceneManager.getInstance().changeScene(mainScene(self.screen, self.clock))
                    return

                if self.exitButton.isCollisionRect(pygame.mouse.get_pos()) :
                    SceneManager.getInstance().isQuit = True
                    return


    def load_resources(self) :
        self.background = SimpleImage("Resources/Images/Background/mainScene.png")
        self.background.setPos((0,0))
        self.background.setSize((1280,720))
        self.simple_image_list.append(self.background)

        self.startButton = SimpleImage("Resources/Images/UI/Start.png")
        self.startButton.setCenterMode(True)
        self.startButton.setPos((640,400))
        self.startButton.setSize((300, 100))
        self.simple_image_list.append(self.startButton)

        self.exitButton = SimpleImage("Resources/Images/UI/Exit.png")
        self.exitButton.setCenterMode(True)
        self.exitButton.setPos((640, 550))
        self.exitButton.setSize((300, 100))
        self.simple_image_list.append(self.exitButton)


        self.title = pygame.font.SysFont("Monospace", 100).render("Score : " + str(SceneManager.getInstance().getPoint()), True, (0,0,0))
