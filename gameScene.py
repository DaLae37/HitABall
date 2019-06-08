import pygame
import random
import math
from Objects.ball import Ball
from Objects.ground import UnderGround, OverGround
from Framework.sceneManager import Scene, SceneManager
from Framework.animation import Animation
from Framework.simple_image import SimpleImage
from Framework.cameraManager import CameraManager

class gameScene(Scene) :

    objectList = []
    uiList = [] #barPos = ui[0] barSize = ui[1] borderColor = ui[2] barColor = ui[3]

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock
        self.isMove = False
        self.t = 0
        self.waterAnim = list()
        self.load_resources()

    def update(self) :
        CameraManager.getInstance().update()
        self.screen.fill(pygame.Color('white'))
        self.ball.update()

        camX = CameraManager.getInstance().getCameraPos()[0]
        camY = CameraManager.getInstance().getCameraPos()[1]

        for si in self.objectList :
            if si.getTag() is "Animation" :
                si.update()

            if si.isCollisionRect(self.ball.getPos()) :
                if si.getTag() is "Ground" :
                    if si.whereCollide(self.ball) is 0 :
                        if self.ball.getIsStart() is False :
                            self.ball.setPos((self.ball.getPos()[0], si.getPos()[1] - self.ball.getSize()[1]))
                            self.ball.setIsStart(True)
                    else :
                        if self.ball.getIsMove(True) :
                            self.ball.setIsMove(False)

            if CameraManager.getInstance().followedObject is si :
                self.screen.blit(si.getSurface(), si.getPos())
            else :
                siX = si.getPos()[0]
                siY = si.getPos()[1]
                if siX - camX > 2500 :
                    self.objectList.remove(si)
                else :
                    self.screen.blit(si.getSurface(), (siX -camX, siY - camY))
        for ui in self.uiList :
            barPos = ui[0]
            barSize = ui[1]
            borderColor = ui[2]
            barColor = ui[3]
            self.DrawBar(barPos, barSize, borderColor, barColor, (self.t % 350) / 100)
        self.t+=1

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                pass
            if event.type == pygame.MOUSEBUTTONUP :
                pass
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    pass
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    pass
                if event.key == pygame.K_RETURN :
                    self.ball.setIsMove(True)

    def load_resources(self) :
        for i in range(10) :
            underBackground = SimpleImage("Resources/Images/Background/underBackground.png")
            underBackground.setPos((0 - 1280 * i,0))
            self.objectList.append(underBackground)

            background = SimpleImage("Resources/Images/Background/background.png")
            background.setPos((0 - 1280 * i,-500))
            self.objectList.append(background)

        water_list = list()
        for i in range(8) :
            water_list.append('Resources/Images/Water/'+str(i+1)+'.png')
        for i in range(100) :
            water = Animation(water_list,8)
            water.setPos((1180 - 100 * i ,620))
            self.objectList.append(water)

        for i in range(10) :
            overGround = OverGround()
            overGround.setPos((1180 - 100 * i * i, 520))
            self.objectList.append(overGround)

            underGround = UnderGround()
            underGround.setPos((1180 - 100 * i * i, 620))
            self.objectList.append(underGround)

        self.ball = Ball.getInstance()
        self.ball.setPos((1200, 300))
        self.objectList.append(self.ball)
        CameraManager().getInstance().setFollowedObject(self.ball)
        self.uiList.append([(120, 360),(200, 20),(0, 0, 0),(0, 128, 0)])

    def DrawBar(self, pos, size, borderC, barC, progress):
        pygame.draw.rect(self.screen, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(self.screen, barC, (*innerPos, *innerSize))
