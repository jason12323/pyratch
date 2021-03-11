import pyratch._inputbox as inputbox
import pygame
def getmouseposition():
    return pygame.mouse.get_pos()

def getmousepressed(button=5):
    return pygame.mouse.get_pressed(button)[0]

def setmousevisible(b: bool):
    pygame.mouse.set_visible(b)

def getkeypressed(key):
    a = pygame.key.get_pressed()
    return a[key]

def getkeyspressed():
    return pygame.key.get_pressed()

def iskeydown():
    return True in pygame.key.get_pressed()