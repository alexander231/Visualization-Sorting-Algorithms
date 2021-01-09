import numpy as np
import random
import time

# The sorting algorithms will be subclasses of the class Algorithm
class Algorithm:

    def __init__(self, name):
        # This is a random array of size 512, with elements from 0 to 512
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



#checked 9
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

        self.update_screen()

#checked 8
class MergeSort(Algorithm):

    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, a = []): 
        if a == []:
            a = self.array
        current_size = 1
        
        # Outer loop for traversing Each 
        # sub array of current_size 
        while current_size < len(a) - 1: 
            
            left = 0
            # Inner loop for merge call 
            # in a sub array 
            # Each complete Iteration sorts 
            # the iterating sub array 
            while left < len(a)-1: 
                
                # mid index = left index of 
                # sub array + current sub 
                # array size - 1 
                mid = min((left + current_size - 1),(len(a)-1))
                
                # (False result,True result) 
                # [Condition] Can use current_size 
                # if 2 * current_size < len(a)-1 
                # else len(a)-1 
                right = ((2 * current_size + left - 1, 
                        len(a) - 1)[2 * current_size 
                            + left - 1 > len(a)-1]) 
                                
                # Merge call for each sub array 
                self.merge(a, left, mid, right) 
                left = left + current_size*2
                
            # Increasing sub array size by 
            # multiple of 2 
            current_size = 2 * current_size 
        
    # Merge Function
    def merge(self, a, l, m, r): 
        n1 = m - l + 1
        n2 = r - m 
        L = [0] * n1 
        R = [0] * n2 
        for i in range(0, n1): 
            L[i] = a[l + i] 
        for i in range(0, n2): 
            R[i] = a[m + i + 1] 
    
        i, j, k = 0, 0, l 
        while i < n1 and j < n2: 
            if L[i] > R[j]: 

                self.update_screen(a[k], R[j])

                a[k] = R[j] 
                j += 1
                
            else: 

                self.update_screen(a[k], L[i])

                a[k] = L[i]  
                i += 1
            k += 1
            
        while i < n1: 
            a[k] = L[i] 
            i += 1
            k += 1
    
        while j < n2: 
            a[k] = R[j] 
            j += 1
            k += 1
        self.update_screen()
            
#checked 7
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

        self.update_screen()

        return i + 1

    def algorithm(self, arr = [], low = 0, high = 0):

        if arr == []:
            arr = self.array
            high = len(arr) - 1

        if low < high:

            pi = self.partition(arr, low, high)

            self.algorithm(arr, low, pi - 1)
            self.algorithm(arr, pi + 1, high)

#checked 6
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

        self.update_screen()

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

#checked 5
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
        self.update_screen()
            
#checked 4
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

        self.update_screen()
#checked 3
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

        self.update_screen()

#checked 2
class BubbleSort(Algorithm):

    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):

        for i in range(len(self.array)):

            for j in range(0, len(self.array) - i - 1):
                
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

            self.update_screen(self.array[j], self.array[j + 1])

        self.update_screen()       

#checked 1
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
                
        self.update_screen()

