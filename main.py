import pygame
from Framework.sceneManager import SceneManager
from mainScene import mainScene

if __name__ == '__main__' :
    pygame.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096) #Frequency, Size, Channels, BufferSize

    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Hit A Ball")
    clock = pygame.time.Clock()
    run = True

    SceneManager.getInstance().changeScene(mainScene(screen,clock))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pass

        if SceneManager.getInstance().isQuit :
            run = False

        SceneManager.getInstance().update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
