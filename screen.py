import pygame
import time

import sys
import algos
from menu import draw_menu, draw_text, draw_Text_center
from constants import ROWS, COLS, SQUARE_SIZE, MENU_DIMENSIONS, SORTING_DIMENSIONS, BG_COLOR
algorithms = {"SelectionSort": algos.SelectionSort(), "BubbleSort": algos.BubbleSort(), "OptimizedBubbleSort": algos.OptimizedBubbleSort()}

pygame.init()


#create screen





running = True
arr = algos.SelectionSort()
k = int(SORTING_DIMENSIONS[0]/len(arr.array))
font = pygame.font.SysFont("freesansbold.ttf", 40)




def menu_algorithms():
    screen_Menu = pygame.display.set_mode((MENU_DIMENSIONS[0], MENU_DIMENSIONS[1]))
    running1 = True

    #draw_menu(screen_Menu)
    screen_Menu.fill(BG_COLOR)
    
    
    while running1:
        (X_MOUSE, Y_MOUSE) = pygame.mouse.get_pos()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()
                sys.exit()
            
    
            
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


            draw_Text_center("BubbleSort", font, (255,255,255), screen_Menu, 100, 100)
            
            draw_Text_center("OBubbleSort", font, (255,255,255), screen_Menu, 300, 100)

            draw_Text_center("SelectionSort", font, (255,255,255), screen_Menu, 500, 100)

            draw_Text_center("InsertionSort", font, (255,255,255), screen_Menu, 700, 100)

            draw_Text_center("MergeSort", font, (255,255,255), screen_Menu, 900, 100)

            draw_Text_center("QuickSort", font, (255,255,255), screen_Menu, 100, 300)

            draw_Text_center("HeapSort", font, (255,255,255), screen_Menu, 300, 300)

            draw_Text_center("TreeSort", font, (255,255,255), screen_Menu, 500, 300)

            draw_Text_center("ShellSort", font, (255,255,255), screen_Menu, 700, 300)

            draw_Text_center("BucketSort", font, (255,255,255), screen_Menu, 900, 300)

            draw_Text_center("RadixSort", font, (255,255,255), screen_Menu, 100, 500)

            draw_Text_center("CountingSort", font, (255,255,255), screen_Menu, 300, 500)

            draw_Text_center("CubeSort", font, (255,255,255), screen_Menu, 500, 500)
            
            draw_Text_center("TimSort", font, (255,255,255), screen_Menu, 700, 500)

            draw_Text_center("Exit", font, (255,255,255), screen_Menu, 900, 500)
           
                

            
            if X_MOUSE < 200 and Y_MOUSE < 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                sorting()
                running1 = False
                

                

            if X_MOUSE > 800 and Y_MOUSE > 400 and event.type == pygame.MOUSEBUTTONDOWN:
                
                running1 = False
                pygame.quit()
                sys.exit()






            pygame.display.update()

def sorting():
    
    screen_Sorting = pygame.display.set_mode((SORTING_DIMENSIONS[0], SORTING_DIMENSIONS[1]))

    running2 = True
    screen_Sorting.fill(BG_COLOR)
    while running2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
                pygame.quit()
                sys.exit()
            

        '''for i in range(len(arr.array)):
            pygame.draw.rect(screen_Sorting, (22, 100, 100), (i*k, 512, k, -arr.array[i]))
            pygame.display.update()'''
        for i in range(len(arr.array)):
            minimum_index = i
            for j in range(i + 1, len(arr.array)):
                if arr.array[minimum_index] > arr.array[j]:
                    minimum_index = j
            swap1 = arr.array[i]
            swap2 = arr.array[minimum_index]
            arr.array[i], arr.array[minimum_index] = arr.array[minimum_index], arr.array[i]
            
            for _ in range(len(arr.array)):
                if arr.array[_] == swap1:
                    colour = (255, 0, 0)
                elif arr.array[_] == swap2:
                    colour = (0, 0, 255)
                else:
                    colour = (0, 255, 0)
                pygame.draw.rect(screen_Sorting, colour, (_*k, 512, k, -arr.array[_]))
            pygame.display.update()
            screen_Sorting.fill(BG_COLOR)
        for _ in range(len(arr.array)):
            colour = (0, 255, 0)
            pygame.draw.rect(screen_Sorting, colour, (_*k, 512, k, -arr.array[_]))
        pygame.display.update()
        for _ in range(len(arr.array)):
            colour = (255, 0, 0)
            pygame.draw.rect(screen_Sorting, colour, (_*k, 512, k, -arr.array[_]))
            pygame.display.update()
             
        time.sleep(2)
        running2 = False
        

        
        '''for i in range(len(arr.array)):
            colour = (80, 0, 255)
            pygame.draw.rect(screen_Sorting, colour, (i*k, 512, k, -arr.array[i]))
        pygame.display.update()
        running2 = False'''
            
            
            
menu_algorithms()
        

        
        
            
