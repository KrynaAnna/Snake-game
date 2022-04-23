import pygame


def eating_sound():
    pygame.mixer.init()
    pygame.mixer.Sound("eating.wav").play()

def over_sound():
    pygame.mixer.init()
    pygame.mixer.Sound("over.wav").play()



