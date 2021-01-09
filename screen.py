# Here are the methods for creating the GUI and its elements
import pygame
import time
import sys
import algos
from constants import ROWS, COLS, SQUARE_SIZE, MENU_DIMENSIONS, SORTING_DIMENSIONS, BG_COLOR, BLACK, RED, TURQUOISE, WHITE

pygame.init()

# Create screen

screen_Menu = pygame.display.set_mode((MENU_DIMENSIONS[0], MENU_DIMENSIONS[1]))
pygame.display.set_caption("Sorting Visualizer")
font = pygame.font.SysFont("freesansbold.ttf", 40)

def draw_Text_center(text,font, color, screen, x, y): # For centering the text in the buttons
    textobj=font.render(text,True,color)
    textrect=textobj.get_rect(center=(x,y))
    screen.blit(textobj,textrect)
    
def check_events(): # Check if the pygame window was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update1(algorithm, swap1=None, swap2=None, display=screen_Menu): # Draws the elements of the array
    
    display = pygame.display.set_mode((SORTING_DIMENSIONS[0], SORTING_DIMENSIONS[1]))
    display.fill(BLACK)
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(SORTING_DIMENSIONS[0]/len(algorithm.array))

    for i in range(len(algorithm.array)):

        colour = TURQUOISE

        if swap1 == algorithm.array[i]:
            colour = WHITE
        elif swap2 == algorithm.array[i]:
            colour = RED

        # The elements of the array are rendered as rectangles .
        # pygame.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle) (size_of_rectanlge = (left, top, width, height))

        pygame.draw.rect(display, colour, (i*k, SORTING_DIMENSIONS[1], k, -algorithm.array[i]))

    check_events()   
    pygame.display.update()

def keep_open(algorithm, display, time): # Keep the screen open until sorting is done

    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()
        

def menu_algorithms(): # The menu from which the user chooses what sorting algorithm will be visualized
    
    while True:

        (X_MOUSE, Y_MOUSE) = pygame.mouse.get_pos() # Get the mouse position
       
        for event in pygame.event.get(): # Check if the cursor is above a button or if that button is clicked

            if event.type == pygame.QUIT:
            
                pygame.quit()
                sys.exit()
            # Draw all the buttons and text for the Menu 

            if X_MOUSE < 200 and Y_MOUSE < 200:

                pygame.draw.rect(screen_Menu, RED, (0, 0, SQUARE_SIZE, SQUARE_SIZE))
                
            else:

                pygame.draw.rect(screen_Menu, TURQUOISE, (0, 0, SQUARE_SIZE, SQUARE_SIZE))    
                
            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE < 200:

                pygame.draw.rect(screen_Menu, RED, (200, 0, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, BLACK, (200, 0, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE < 200:

                pygame.draw.rect(screen_Menu, RED, (400, 0, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, TURQUOISE, (400, 0, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE < 200:

                pygame.draw.rect(screen_Menu, RED, (600, 0, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, BLACK, (600, 0, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 800 and X_MOUSE < 1000 and Y_MOUSE < 200:

                pygame.draw.rect(screen_Menu, RED, (800, 0, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, TURQUOISE, (800, 0, SQUARE_SIZE, SQUARE_SIZE))

            if  X_MOUSE < 200 and Y_MOUSE > 200 and Y_MOUSE < 400:

                pygame.draw.rect(screen_Menu, RED, (0, 200, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, BLACK, (0, 200, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE > 200 and Y_MOUSE < 400:

                pygame.draw.rect(screen_Menu, RED, (200, 200, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, TURQUOISE, (200, 200, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE > 200 and Y_MOUSE < 400:

                pygame.draw.rect(screen_Menu, RED, (400, 200, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, BLACK, (400, 200, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE > 200 and Y_MOUSE < 400:

                pygame.draw.rect(screen_Menu, RED, (600, 200, SQUARE_SIZE, SQUARE_SIZE))

            else:

                pygame.draw.rect(screen_Menu, TURQUOISE, (600, 200, SQUARE_SIZE, SQUARE_SIZE))

            if X_MOUSE > 800 and Y_MOUSE > 200 and Y_MOUSE < 400:

                pygame.draw.rect(screen_Menu, RED, (800, 200, SQUARE_SIZE, SQUARE_SIZE))

            else:
                pygame.draw.rect(screen_Menu, BLACK, (800, 200, SQUARE_SIZE, SQUARE_SIZE))
            
            draw_Text_center("BubbleSort", font, WHITE, screen_Menu, 100, 100)
            
            draw_Text_center("OBubbleSort", font, WHITE, screen_Menu, 300, 100)

            draw_Text_center("SelectionSort", font, WHITE, screen_Menu, 500, 100)

            draw_Text_center("InsertionSort", font, WHITE, screen_Menu, 700, 100)

            draw_Text_center("QuickSort", font, WHITE, screen_Menu, 900, 100)

            draw_Text_center("HeapSort", font, WHITE, screen_Menu, 100, 300)

            draw_Text_center("ShellSort", font, WHITE, screen_Menu, 300, 300)

            draw_Text_center("MergeSort", font, WHITE, screen_Menu, 500, 300)

            draw_Text_center("CountingSort", font, WHITE, screen_Menu, 700, 300)

            draw_Text_center("EXIT", font, WHITE, screen_Menu, 900, 300)

            # Check if a button is pressed then, if that is the case start the chosen sorting algorithm

            if X_MOUSE < 200 and Y_MOUSE < 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.BubbleSort()
                
                time_elapsed = algorithm.run()[1]
    
                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE < 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.OptimizedBubbleSort()
                
                time_elapsed = algorithm.run()[1]
    
                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE < 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.SelectionSort()
                
                time_elapsed = algorithm.run()[1]
    
                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE < 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.InsertionSort()
                
                time_elapsed = algorithm.run()[1]
    
                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 800 and Y_MOUSE < 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.QuickSort()
                
                time_elapsed = algorithm.run()[1]
    
                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE < 200 and Y_MOUSE > 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.HeapSort()
                
                time_elapsed = algorithm.run()[1]
    
                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 200 and X_MOUSE < 400 and Y_MOUSE > 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.ShellSort()
                
                time_elapsed = algorithm.run()[1]

                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 400 and X_MOUSE < 600 and Y_MOUSE > 200 and event.type == pygame.MOUSEBUTTONDOWN:
                
                algorithm = algos.MergeSort()
                
                time_elapsed = algorithm.run()[1]

                keep_open(algorithm, screen_Menu, time_elapsed)
                
            if X_MOUSE > 600 and X_MOUSE < 800 and Y_MOUSE > 200 and event.type == pygame.MOUSEBUTTONDOWN:

                algorithm = algos.CountingSort()

                time_elapsed = algorithm.run()[1]

                keep_open(algorithm, screen_Menu, time_elapsed)

            if X_MOUSE > 800 and  Y_MOUSE > 200 and event.type == pygame.MOUSEBUTTONDOWN:

                pygame.quit()
                sys.exit()

            pygame.display.update()
                  
if __name__ == "__main__":
    menu_algorithms()
    
        
        
            
