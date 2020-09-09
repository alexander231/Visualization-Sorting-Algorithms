import numpy as np
import random
import time

class Algorithm():

    def __init__(self, name):
        # This is a random array of size 1024, with elements from 0 to 1024
        self.array = np.random.randint(500, size = 500)
        # The name of the sorting algorithm that whe choose
        self.name = name
    
    def update_screen(self, swap1 = None, swap2 = None):
        # Give the indexes to be swapped into the screen 
        
        screen.update(self, swap1, swap2)
    
    # Start the timer and the algorithm
    def start(self):

        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            minimum_index = i
            for j in range(i + 1, len(self.array)):
                if self.array[minimum_index] > self.array[j]:
                    minimum_index = j
                self.array[minimum_index], self.array[i] = self.array[i], self.array[minimum_index]
                self.update_screen(self.array[i], self.array[minimum_index])

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):

        for i in range(len(self.array)):
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
            self.update_screen(self.array[j], self.array[j + 1])

class OptimizedBubbleSort(Algorithm):
    def __init__(self):
        super().__init__("OptimizedBubbleSort")
    
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
    
    def algorithm(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            index = i - 1
            while index >= 0 and self.array[index] > key:
                self.array[index + 1] = self.array[index]
                index -= 1
            self.array[index + 1] = key
            self.update_screen(self.array[index + 1], self.array[i])

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")
    
    def partition(self, arr, low, high):

        i = low - 1

        # pivot
        pivot = arr[high] 

        for j in range(low, high):

            if arr[j] < pivot:

                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.update_screen(arr[i], arr[j])
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def algorithm(self, arr = [], low = 0, high = 0):
        if arr == []:
            arr = self.array
            high = len(arr) - 1

        if low < high:

            pi = self.partition(arr, low, high)

            self.algorithm(arr, low, pi - 1)
            self.algorithm(arr, pi + 1, high)

class TimSort(Algorithm):
    pass

class HeapSort(Algorithm):
    pass

class TreeSort(Algorithm):
    pass

class ShellSort(Algorithm):
    pass

class BucketSort(Algorithm):
    pass

class RadixSort(Algorithm):
    pass
class CountingSort(Algorithm):
    pass
class CubeSort(Algorithm):
    pass