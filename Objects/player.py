import os, sys
import pygame

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Framework.animation import Animation

class Player() :
    instance = None

    def __init__(self) :
        pass
        
    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = SceneManager()
        return cls.instance

    def load_images(self) :
        pass
