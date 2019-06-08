from Framework.simple_image import SimpleImage
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class OverGround(SimpleImage) :
    def __init__(self) :
        super().__init__("Resources/Images/Ground/overGround.png")

    def whereCollide(self, movedObject) :
        mX = movedObject.getPos()[0]
        mY = movedObject.getPos()[1]
        mSY = movedObject.getSize()[1]

        if self.getPos()[0] + self.getSize()[0] > mX and mY + mSY > self.getPos()[1]:
            return 0
        else :
            return 1

    def getTag(self) :
        return "Ground"
class UnderGround(SimpleImage) :
    def __init__(self) :
        super().__init__("Resources/Images/Ground/underGround.png")

    def whereCollide(self, movedObject) :
        return 1

    def getTag(self) :
        return "Ground"
