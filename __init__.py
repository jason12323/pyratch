import pygame
import threading
import time
import pyratch.inputs as inputs
import pyratch.objects as objects
from typing import IO, Union
import os

isgame = True
event = None
events = []
location = os.getcwd()+"/"

def setfilelocation(l: Union[IO, str]):
    global location
    location = l

class sprite:
    x = 0
    y = 0
    direction = 0
    surface = None
    pic = []
    ind = 0
    def __init__(self, src: [str, list], size=(0, 0)):
        if type(src) == str:
            self.surface = pygame.transform.scale(pygame.image.load(location+src), size)
            self.pic = [self.surface]
        else:
            for i in src:
                self.pic.append(pygame.transform.scale(pygame.image.load(location+i), size))
            self.surface = self.pic[0]
        self.rect = self.surface.get_rect()

    def turn(self, degree):
        self.direction += degree
        while self.direction > 360:
            self.direction -= 360
        self.surface = pygame.transform.rotate(self.surface, self.direction)

    def goto(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

    def next_shape(self):
        self.ind += 1
        if self.ind >= len(self.pic):
            self.ind = 0
        self.surface = self.pic[self.ind]

    def goto_sprite(self, othersp):
        self.x = othersp.x
        self.y = othersp.y

    def hit(self, other="Mouse"):
        if other == "Mouse":
            return self.rect.collidepoint(pygame.mouse.get_pos())
        elif type(other) == sprite:
            return self.rect.colliderect(other.rect)
        else:
            return self.rect.collidepoint(other[0], other[1])

    def click(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(5)[0]

    def maincodeloop(self, func):
        def returntrue():
            return True
        when(func, returntrue)


class picture:
    def __init__(self, src: str, size=(100, 100)):
        self.surface = pygame.transform.scale(pygame.image.load(location+src), size)


class window:
    def __init__(self, size: tuple, caption="", icon: Union[picture, sprite] = None, background: Union[picture, sprite] = None):
        self.sc = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
        if icon is not None:
            pygame.display.set_icon(icon.surface)
        self.background = background
        if self.background is not None:
            self.background = pygame.transform.scale(self.background.surface, size)

    def blit_sprite(self, spritee):
        self.sc.blit(spritee.surface, (spritee.x, spritee.y))

    def update(self, tim=0):
        if not isgame:
            exit()
        pygame.display.flip()
        time.sleep(tim)
        self.sc.fill((255, 255, 255))
        if self.background is not None:
            self.sc.blit(self.background, (0, 0))
        pygame.display.flip()
        global event, events
        events = pygame.event.get()
        event = pygame.event.poll()
        for i in events:
            if i == pygame.event.Event(objects.QUIT):
                pyexit()
                exit()

    def set_background(self, pic: picture):
        self.background = pygame.transform.scale(pic.surface, size)

    def ask(self, qu: str):
        _inputbox.ask(self.sc, qu)

    def drawtext(self, text, position, color=(0, 0, 0), size=24):
        pygame.font.init()
        self.sc.blit(pygame.font.Font(None, size).render(text, True, color), position)

    def drawrect(self, x: int, y: int, size: Union[tuple, list], color=(0, 0, 0), wid=1):
        pygame.draw.rect(self.sc, color, (x, y, size[0], size[1]), width=wid)


def isevent(eventname):
    return Event(eventname) in events

def when(func, b, *args, **kwargs):
    def asd(*args, **kwargs):
        while isgame:
            if b(*args, **kwargs):
                func()
    threading.Thread(target=asd, args=args, kwargs=kwargs).start()

def Event(code: int):
    return pygame.event.Event(code)

def play_sound(src):
    pygame.mixer.Sound(src).play()

def sleep(secs):
    time.sleep(secs)

def pyexit():
    global isgame
    isgame = False