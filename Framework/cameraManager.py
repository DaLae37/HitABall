import pygame
from Framework import define
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class CameraManager() :
    isFollowing = False
    followedObject = None
    instance = None
    cameraX = 0
    cameraY = 0
    dX = 0
    dy = 0
    def update(self) :
        if self.isFollowing :
            x = self.followedObject.getPos()[0]
            y = self.followedObject.getPos()[1]
            self.setCameraPos((x + self.dX , y + self.dY))

    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = CameraManager()
        return cls.instance

    def setCameraPos(self, pos) :
        self.cameraX = pos[0]
        self.cameraY = pos[1]

    def addCameraPos(self, pos) :
        self.cameraX += pos[0]
        self.cameraY += pos[1]

    def getCameraPos(self) :
        return (self.cameraX, self.cameraY)

    def setFollowedObject(self, obj) :
        self.followedObject = obj
        self.dX = self.cameraX - obj.getPos()[0]
        self.dY = self.cameraY - obj.getPos()[1]
        self.isFollowing = True

    def releaseObject(self) :
        self.followedObject = None
        self.isFollowing = False
