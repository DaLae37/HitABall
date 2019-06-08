from Framework.simple_image import SimpleImage
import pygame
import math
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Ball(SimpleImage) :
    instance = None
    def __init__(self) :
        super().__init__("Resources/Images/Ball/Ball.png")
        self.isMove = False
        self.isStart = False
        self.t = 0
        self.power = 50
        self.beforeT = 0

    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = Ball()
        return cls.instance

    def update(self) :

        if self.isStart :
            if self.isMove :
                self.addPos((-100 * math.cos(45), -self.power * math.cos(45) + 9.8 * self.t - self.beforeT))
                self.setSurface(pygame.transform.rotate(self.getSurface(), 90))
        else :
            self.addPos((0,0.5 * 9.8 * (self.t * self.t)))

        self.t+=1

    def setIsMove(self, isMove) :
        self.isMove = isMove
        if self.isMove is False and isMove is True :
            self.beforeT = self.t

    def getIsMove(self) :
        return self.isMove

    def setIsStart(self, isStart) :
        self.isStart = isStart

    def getIsStart(self) :
        return self.isStart
