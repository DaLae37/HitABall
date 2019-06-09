import pygame
import math
import random
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
        self.powerOn = False
        self.power = 0
        self.degreeOn = False
        self.degree = 0

        self.t = 0
        self.waterAnim = list()

        self.beforeCamX = 0
        self.beforeCamY = 0

        self.load_resources()

    def update(self) :
        CameraManager.getInstance().update()
        self.screen.fill(pygame.Color('white'))
        self.ball.update()

        camX = CameraManager.getInstance().getCameraPos()[0]
        camY = CameraManager.getInstance().getCameraPos()[1]
        for si in self.objectList :
            siX = si.getPos()[0]
            siY = si.getPos()[1]

            if siX > 2500 : #카메라에서 벗어난 객체는 삭제
                self.objectList.remove(si)

            else : #벗어나지 않은 객체는 카메라와의 거리를 고려해 Render
                if not (CameraManager.getInstance().followedObject is si) :
                    si.setPos((siX -(camX - self.beforeCamX) ,siY - (camY - self.beforeCamY)))
                self.screen.blit(si.getSurface(), si.getPos())

            if si.getTag() is "Animation" :
                si.update()

            if si.isCollisionRect(self.ball.getPos()) :
                if si.getTag() is "Ground" :
                    if si.whereCollide(self.ball) is 0 :
                        if self.ball.getIsStart() is False :
                            self.ball.setIsStart(True)
                        if self.ball.getIsMove() is True :
                            self.ball.setIsMove(False)
                            SceneManager.getInstance().setPoint(SceneManager.getInstance().getPoint() + 1)
                        self.ball.setPos((self.ball.getPos()[0], si.getPos()[1] - self.ball.getSize()[1]))

                    else :
                        self.ball.setIsStart(False)
                        self.ball.setPos((si.getPos()[0] + si.getSize()[0], self.ball.getPos()[1]))

                elif si.getTag() is "Animation" :
                    CameraManager.getInstance().releaseObject()
                    CameraManager.getInstance().setCameraPos((0,0))
                    from resultScene import resultScene
                    SceneManager.getInstance().changeScene(resultScene(self.screen,self.clock))
                    return
        self.beforeCamX = camX
        self.beforeCamY = camY

        for ui in self.uiList :
            barPos = ui[1]
            barSize = ui[2]
            borderColor = ui[3]
            barColor = ui[4]
            if ui[0] is "power" :
                gaze = (self.power * 14 % 350) / 350
            elif ui[0] is "degree" :
                gaze = (self.degree * 11.9 % 350) / 350
            self.DrawBar(barPos, barSize, borderColor, barColor, gaze)

        if self.powerOn :
            self.power+=1
            if self.power > 25 : #power의 증가량은 최대 25까지
                self.power = 0

        if self.degreeOn :
            self.degree+=1
            if self.degree > 30 : #degree의 증가량은 최대 30까지
                self.degree = 0

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                SceneManager.getInstance().isQuit = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN :
                self.degreeOn = True

            if event.type == pygame.MOUSEBUTTONUP :
                self.degreeOn = False
                self.ball.setDegree(self.degree + 30)

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    self.powerOn = True
                if event.key == pygame.K_LEFT :
                    for si in self.objectList :
                        si.addPos((10, 0))
                if event.key == pygame.K_RIGHT :
                    for si in self.objectList :
                        si.addPos((-10, 0))

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    self.powerOn = False
                    self.ball.setPower(self.power + 50)

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

        tmpCount = 0
        for i in range(100) :
            tmp = random.randrange(0, 5) + 1
            if i < 2 or tmpCout > 4:
                tmp = 1

            if tmp >= 2 :
                water = Animation(water_list,8)
                water.setPos((1180 - 100 * i ,620))
                self.objectList.append(water)
                tmpCout += 1
            else :
                overGround = OverGround()
                overGround.setPos((1180 - 100 * i, 520))
                self.objectList.append(overGround)

                underGround = UnderGround()
                underGround.setPos((1180 - 100 * i, 620))
                self.objectList.append(underGround)
                tmpCout = 0

        self.ball = Ball()
        self.ball.setPos((1200, 300))
        self.objectList.append(self.ball)
        CameraManager().getInstance().setFollowedObject(self.ball)

        self.uiList.append(["power",(1000, 50),(200, 20),(0, 0, 0),(0, 128, 0)])
        self.uiList.append(["degree",(1000, 100),(200, 20),(0, 0, 0),(128, 0, 0)])

    def DrawBar(self, pos, size, borderC, barC, progress):
        pygame.draw.rect(self.screen, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, pos[1]+3)
        innerSize = ((size[0]-6) * progress, size[1]-6)
        pygame.draw.rect(self.screen, barC, (*innerPos, *innerSize))
