import pygame
from constants import ROWS, COLS, SQUARE_SIZE, MENU_DIMENSIONS, SORTING_DIMENSIONS, BG_COLOR, TURQUOISE


def draw_menu(win):
    win.fill(BG_COLOR)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, TURQUOISE, (row * SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def drawTextcenter(text,font, color, screen, x, y):
    textobj=font.render(text,True,color)
    textrect=textobj.get_rect(center=(x,y))
    screen.blit(textobj,textrect)
    