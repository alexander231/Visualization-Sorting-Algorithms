import pygame
import sys
import algos
from menu import draw_menu, draw_text, drawTextcenter
from constants import ROWS, COLS, SQUARE_SIZE, MENU_DIMENSIONS, SORTING_DIMENSIONS, BG_COLOR
algorithms = {"SelectionSort": algos.SelectionSort(), "BubbleSort": algos.BubbleSort(), "OptimizedBubbleSort": algos.OptimizedBubbleSort()}

pygame.init()


#create screen
screen_Sorting = pygame.display.set_mode((SORTING_DIMENSIONS[0], SORTING_DIMENSIONS[1]))
screen_Menu = pygame.display.set_mode((MENU_DIMENSIONS[0], MENU_DIMENSIONS[1]))



running = True
arr = algos.SelectionSort()
k = int(SORTING_DIMENSIONS[0]/len(arr.array))
font = pygame.font.SysFont("freesansbold.ttf", 40)


def draw_button(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def menu_algorithms():
    global running

    draw_menu(screen_Menu)
    BubbleSortB = drawTextcenter("BubbleSort", font, (255,255,255), screen_Menu, 100, 100)
    
    OptimizedBubbleSortB = drawTextcenter("SelectionSort", font, (255,255,255), screen_Menu, 300, 100)
    
    
    
    
    
    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
        pygame.display.update()

def running():
    global running
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            screen.fill(background_color)

            for i in range(len(arr.array)):
                pygame.draw.rect(screenSorting, (255, 0 , 0), (i*k, 500, k, -arr.array[i]))
            pygame.display.update()

menu_algorithms()
        

        
        
            
