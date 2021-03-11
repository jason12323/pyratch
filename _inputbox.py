# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame
import pygame.draw
import pygame.event
import pygame.font
import string
from pygame.locals import *


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        elif event.type == QUIT:
            quit()
        else:
            pass


def display_box(screen, message):
    """Print a message in a box in the middle of the screen"""
    fontobject = pygame.font.Font(None, 24)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 150,
                      (screen.get_height() / 2) - 10,
                      300, 20), 0)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 152,
                      (screen.get_height() / 2) - 12,
                      304, 24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, True, (0, 0, 0)),
                    ((screen.get_width() / 2) - 150, (screen.get_height() / 2) - 10))
    pygame.display.flip()


def ask(screen, question):
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + "".join(current_string))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
    return "".join(current_string)

