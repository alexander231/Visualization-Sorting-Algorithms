import numpy as np
import random
import visualizer
import time

class Algorithm():

    def __init__(self, name):
        # This is a random array of size 1024, with elements from 0 to 1024
        self.array = np.random.rand.randint(1024, size = 1024)
        # The name of the sorting algorithm that whe choose
        self.name = name
    
    def update_screen(self, swap1 = None, swap2 = None):
        # Give the indexes to be swapped into the visualizer 
        viusalizer.update(self, swap1, swap2)
    
    # Start the timer and the algorithm
    def start(self):

        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

class BubbleSort(Algorithm):
    def __init__(self):
        super.__init__("BubbleSort")

    def algorithm(self):

        for i in range(len(self.array)):
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
            self.update_screen(self.array[j], self.array[j + 1])

class OptimizedBubbleSort(Algorithm):
    def __init__(self):
        super.__init__("OptimizedBubbleSort")
    
    def algorithm(self):

        for i in range(len(self.array)):
            swapped = True
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j +1], self.array[j]
                    swapped = False

                    if swapped:
                        break
            self.update_screen(self.array[j], self.array[j + 1])



class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")