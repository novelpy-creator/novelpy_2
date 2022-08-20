import pygame

def load_image(fn):
    return pygame.image.load('game/images/' + fn)

def color(r, g, b):
    return pygame.color.Color(r, g, b)

def Rect(rect):
    return pygame.Rect(rect)

def draw_rect(surface, color, rect):
    return pygame.draw.rect(surface, color, rect)  