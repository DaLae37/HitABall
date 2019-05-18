import pygame
import random
from Framework.animation import Animation

if __name__ == '__main__' :
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Hit A Ball")
    clock = pygame.time.Clock()
    run = True
    tmp_anim = list()
    for i in range(8) :
        tmp_anim.append('./Resources/Images/Water/'+str(i+1)+'.png')
    new_anim = Animation(tmp_anim,10)
    group = pygame.sprite.Group(new_anim)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pass

        group.update()

        screen.fill(pygame.Color('white'))
        group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
