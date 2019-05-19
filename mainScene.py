import pygame
import random
from Framework.sceneManager import Scene, SceneManager
from Framework.soundManager import SoundManager
from Framework.animation import Animation

class mainScene(Scene) :

    def __init__(self, screen, clock) :
        self.screen = screen
        self.clock = clock

        self.load_resources()

    def update(self) :
        self.screen.fill(pygame.Color('white'))

    def load_resources(self) :
        SoundManager.getInstance().load_music("Resources/Sounds/bgm.mp3")
