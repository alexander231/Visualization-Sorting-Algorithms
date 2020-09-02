import algos
import time
import os
import sys
import pygame

dimensions = [2048, 1024]
algos = {"SelectionSort": algos.SelectionSort(), "BubbleSort": algos.BubbleSort(), "OptimizedBubbleSort": algos.OptimizedBubbleSort(), "InsertionSort": algos.InsertionSort(), "MergeSort": algos.MergeSort(), "QuickSort": algos.QuickSort() }

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algo.keys(): print(key, end=" ")
        print("")
        sys.exit(0)

pygame.init()

display_screen = pygame.display.set_mode((dimensions[0], dimensions[1]))

display_screen.fill(pygame.Color("#f0efef"))