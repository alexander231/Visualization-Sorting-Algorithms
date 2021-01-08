import numpy as np
import random
import time
import pygame

class Algorithm:

    def __init__(self, name):
        # This is a random array of size 1024, with elements from 0 to 1024
        self.array = list(np.random.randint(513, size = 512))
        # The name of the sorting algorithm that whe choose
        self.name = name
    
    def update_screen(self, swap1 = None, swap2 = None):
        # Give the indexes to be swapped into the screen 
        import screen
        screen.update1(self, swap1, swap2)
    
    # Start the timer and the algorithm
    def run(self):

        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed



#checked8
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
#bad
class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array = []):
        if array == []:
            array = self.array
        if len(array) > 1:
    
            # Finding the mid of the array
            mid = len(array)//2
    
            # Dividing the array elements
            L = array[:mid]
            self.update_screen()
            # into 2 halves
            R = array[mid:]
            self.update_screen()
    
            # Sorting the first half
            self.algorithm(L)
            
            # Sorting the second half
            self.algorithm(R)
            
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    
                    i += 1
                else:
                    array[k] = R[j]
                    
                    j += 1
                k += 1
                
                
            # Checking if any element was left
            while i < len(L):
                array[k] = L[i]
                
                i += 1
                k += 1
    
            while j < len(R):
                array[k] = R[j]
                
                j += 1
                k += 1
             
            print(self.array)
            
#checked7
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

#checked6
class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def heapify(self, arr, n, i):
        
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[largest] < arr[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            self.update_screen(arr[i], arr[largest])
            # Heapify the root.
            self.heapify(arr, n, largest)
    
    # The main function to sort an array of given size
 
 
    def algorithm(self, arr =[]):
        if arr == []:
            arr = self.array
        n = len(arr)
    
        # Build a maxheap.
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

#checked5
class ShellSort(Algorithm):
    def __init__(self):
        super().__init__("ShellSort")
    # Start with a big gap, then reduce the gap 
    def algorithm(self, arr = []):
        if arr == []:
            arr = self.array
        n = len(arr) 
        gap = n//2
    
        # Do a gapped insertion sort for this gap size. 
        # The first gap elements a[0..gap-1] are already in gapped  
        # order keep adding one more element until the entire array 
        # is gap sorted 
        while gap > 0: 
    
            for i in range(gap,n): 
    
                # add a[i] to the elements that have been gap sorted 
                # save a[i] in temp and make a hole at position i 
                temp = arr[i] 
    
                # shift earlier gap-sorted elements up until the correct 
                # location for a[i] is found
                
                j = i 
                
                while  j >= gap and arr[j-gap] >temp: 
                    
                    arr[j] = arr[j-gap] 
                    
                    j -= gap 
                    
                # put temp (the original a[i]) in its correct location 
                arr[j] = temp 
                
                
                
                self.update_screen(arr[i], arr[j])    
            gap //= 2
            
#bad
'''class BucketSort(Algorithm):
    def __init__(self):
        super().__init__("BucketSort") 
    def algorithm(self, array = []): 
        if array == []:
            array = self.array
        arr = [] 
        slot_num = 1024 # 10 means 10 slots, each 
                    # slot's size is 0.1 
        for i in range(slot_num): 
            arr.append([]) 
            
        # Put array elements in different buckets  
        for j in array: 
            index_b = int(slot_num * j)  
            arr[index_b].append(j) 
        
        # Sort individual buckets  
        for i in range(slot_num): 
            arr[i] = InsertionSort.algorithm(arr[i]) 
            
        # concatenate the result 
        k = 0
        for i in range(slot_num): 
            for j in range(len(arr[i])): 
                x[k] = arr[i][j] 
                k += 1
        return array '''
'''class RadixSort(Algorithm):
    def __init__(self):
        super().__init__("RadixSort") 
    def algorithm(self, arr = []): 
        if arr == []:
            arr = self.array
        # Find the maximum number to know number of digits 
        max1 = max(arr) 
    
        # Do counting sort for every digit. Note that instead 
        # of passing digit number, exp is passed. exp is 10^i 
        # where i is current digit number 
        exp = 1
        while max1 / exp > 0: 
            
            self.countingSort(arr, exp) 
            exp *= 10
        
             
    def countingSort(self, arr, exp1): 
  
        n = len(arr) 
    
        # The output array elements that will have sorted arr 
        output = [0] * (n) 
    
        # initialize count array as 0 
        count = [0] * (10) 
    
        # Store count of occurrences in count[] 
        for i in range(0, n): 
            index = (arr[i] / exp1) 
            count[int(index % 10)] += 1
    
        # Change count[i] so that count[i] now contains actual 
        # position of this digit in output array 
        for i in range(1, 10): 
            count[i] += count[i - 1] 
    
        # Build the output array 
        i = n - 1
        while i >= 0: 
            
            index = (arr[i] / exp1) 
            
            output[count[int(index % 10)] - 1] = arr[i] 
            count[int(index % 10)] -= 1
            i -= 1
            
    
        # Copying the output array to arr[], 
        # so that arr now contains sorted numbers 
        i = 0
        for i in range(0, len(arr)): 
            arr[i] = output[i] '''
#checked4
class CountingSort(Algorithm):
    def __init__(self):
        super().__init__("CountingSort")

    def algorithm(self, array = []):
        if array == []:
            array = self.array
        size = len(array)
        output = [0] * size

        # Initialize count array
        count = [0] * 1024

        # Store the count of each elements in count array
        for i in range(0, size):
            count[array[i]] += 1

        # Store the cummulative count
        for i in range(1, 1024):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = size - 1
        while i >= 0:
            
            output[count[array[i]] - 1] = array[i]
            self.update_screen(output[count[array[i]] - 1], )
            count[array[i]] -= 1
                    
            i -= 1       

        # Copy the sorted elements into original array
        for i in range(0, size):
            array[i] = output[i]
            self.update_screen(array[i], output[i])
        
#checked3
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
#checked2
class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):

        for i in range(len(self.array)):
            
            for j in range(0, len(self.array) - i - 1):
                
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
            self.update_screen(self.array[j], self.array[j + 1])
            
#checked1
class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            minimum_index = i
            for j in range(i + 1, len(self.array)):
                if self.array[minimum_index] > self.array[j]:
                    minimum_index = j
            self.array[i], self.array[minimum_index] = self.array[minimum_index], self.array[i]
            self.update_screen(self.array[i], self.array[minimum_index])
                # The most important step that renders the rectangles to the screen that gets sorted.
                # pygame.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
                


