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
        self.degree = 0

    def update(self) :

        if self.isStart :
            if self.isMove :
                self.addPos((-self.power * math.cos(self.degree * math.pi / 180), -self.power * math.sin(self.degree * math.pi / 180) + 9.8 * (self.t - self.beforeT)))
        else :
            self.addPos((0,0.5 * 9.8 * (self.t * self.t)))

        self.t+=1

    def setIsMove(self, isMove) :
        if self.isMove is False and isMove is True :
            self.beforeT = self.t
        self.isMove = isMove

    def getIsMove(self) :
        return self.isMove

    def setIsStart(self, isStart) :
        if self.isStart is True :
            self.t = 0
        self.isStart = isStart

    def getIsStart(self) :
        return self.isStart

    def setPower(self, power) :
        self.power = power

    def setDegree(self, degree) :
        self.degree = degree
