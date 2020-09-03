import algos
import time
import os
import sys
import pygame

dimensions = [2048, 1024]
algs = {"SelectionSort": algos.SelectionSort(), "BubbleSort": algos.BubbleSort(), "OptimizedBubbleSort": algos.OptimizedBubbleSort(), "InsertionSort": algos.InsertionSort(), "MergeSort": algos.MergeSort(), "QuickSort": algos.QuickSort() }

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algs.keys(): print(key, end = " ")
        print("")
        sys.exit(0)


pygame.init()

display_screen = pygame.display.set_mode((dimensions[0], dimensions[1]))

display_screen.fill(pygame.Color("#fbefcc"))


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



def update(algos, swap1 = None, swap2 = None, display = display_screen):
    display.fill(pygame.Color("#fbefcc"))
    pygame.display.set_caption("Sorting Visualizer    Algorithm: {}     Time: {:.3f}     Status: Sorting...".format(algos.start_time))
    k = int(dimensions[0] / len(algos.array))
    for i in range(len(algos.array)):

        colour = (80, 0, 255)

        if swap1 == algos.array[i]:

            colour = (0, 255, 0)
        
        elif swap2 == algos.array[i]:

            colour = (255, 0, 0)
        pygame.draw.rect(display, colour, (i * k, dimensions[1], k ,-algos.array[i]))

    check_events()
    pygame.display.update()

def keep_ope(algos, display, time):
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.") 
    else:
        try:
            algorithm = algorithms[sys.argv[1]] # Pass the algorithm selected
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error.")

if __name__ == "__main__":
    main()