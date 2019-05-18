import pygame
from pygame import Surface
from pygame.color import Color
from pygame.sprite import Sprite

class Animation(Sprite) :
    def __init__(self, images, frames):
        Sprite.__init__(self)
        self.clock = pygame.time.Clock()

        self.images = list()
        self.frames = frames

        for i in images :
            self.images.append(pygame.image.load(i))

        self.image_count = len(images)
        self.current_frame = 0
        self.image = self.images[self.current_frame]

        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        if self.current_frame is self.image_count -1 :
            self.current_frame = 0
        else:
            self.current_frame += 1
        self.image = self.images[self.current_frame]
        self.clock.tick(self.frames)
