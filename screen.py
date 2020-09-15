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




def menu_algorithms():
    global running

    #draw_menu(screen_Menu)
    screen_Menu.fill(BG_COLOR)
    
    
    while running:
        (X_MOUSE, Y_MOUSE) = pygame.mouse.get_pos()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            BubbleSortB = drawTextcenter("BubbleSort", font, (255,255,255), screen_Menu, 100, 100)
            
            if X_MOUSE < 200 and Y_MOUSE < 200:
                pygame.draw.rect(screen_Menu, (255,0,0), (0, 0, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (0, 0, SQUARE_SIZE, SQUARE_SIZE))    
            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE < 200:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (200, 0, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (200, 0, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE < 200:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (400, 0, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (400, 0, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE < 200:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (600, 0, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (600, 0, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 800 and X_MOUSE < 1000 and Y_MOUSE < 200:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (800, 0, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (800, 0, SQUARE_SIZE, SQUARE_SIZE))
            if  X_MOUSE < 200 and Y_MOUSE > 200 and Y_MOUSE < 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (0, 200, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (0, 200, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE > 200 and Y_MOUSE < 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (200, 200, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (200, 200, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE > 200 and Y_MOUSE < 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (400, 200, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (400, 200, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE > 200 and Y_MOUSE < 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (600, 200, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (600, 200, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 800 and Y_MOUSE > 200 and Y_MOUSE < 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (800, 200, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (800, 200, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE < 200 and Y_MOUSE > 400 :
                pygame.draw.rect(screen_Menu, (255, 0, 0), (0, 400, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (0, 400, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE > 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (200, 400, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (200, 400, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE > 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (400, 400, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (400, 400, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE > 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (600, 400, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (0, 0, 0), (600, 400, SQUARE_SIZE, SQUARE_SIZE))
            if X_MOUSE > 800 and Y_MOUSE > 400:
                pygame.draw.rect(screen_Menu, (255, 0, 0), (800, 400, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen_Menu, (22, 100, 100), (800, 400, SQUARE_SIZE, SQUARE_SIZE))


            drawTextcenter("BubbleSort", font, (255,255,255), screen_Menu, 100, 100)
            
            drawTextcenter("OBubbleSort", font, (255,255,255), screen_Menu, 300, 100)

            drawTextcenter("SelectionSort", font, (255,255,255), screen_Menu, 500, 100)

            drawTextcenter("InsertionSort", font, (255,255,255), screen_Menu, 700, 100)

            drawTextcenter("MergeSort", font, (255,255,255), screen_Menu, 900, 100)

            drawTextcenter("QuickSort", font, (255,255,255), screen_Menu, 100, 300)

            drawTextcenter("HeapSort", font, (255,255,255), screen_Menu, 300, 300)

            drawTextcenter("TreeSort", font, (255,255,255), screen_Menu, 500, 300)

            drawTextcenter("ShellSort", font, (255,255,255), screen_Menu, 700, 300)

            drawTextcenter("BucketSort", font, (255,255,255), screen_Menu, 900, 300)

            drawTextcenter("RadixSort", font, (255,255,255), screen_Menu, 100, 500)

            drawTextcenter("CountingSort", font, (255,255,255), screen_Menu, 300, 500)

            drawTextcenter("CubeSort", font, (255,255,255), screen_Menu, 500, 500)
            
            drawTextcenter("TimSort", font, (255,255,255), screen_Menu, 700, 500)

            drawTextcenter("Exit", font, (255,255,255), screen_Menu, 900, 500)

            if X_MOUSE > 800 and Y_MOUSE > 400 and pygame.MOUSEBUTTONDOWN is False:
                
                pass






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
        

        
        
            
