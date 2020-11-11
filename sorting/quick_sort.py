"""
Quick Sort Algorithm in Python

Author: Marcus Moresco Boeno
Last Update: 2020-11-10

Implements functions that sort a list of elements using the 
quick sort algorithm as described on Chapter 7 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""

# Standard library imports
import random


def _partition_quick_sort(A:list, low:int, high:int) -> int:
    """Partioning Subroutine of the Quick Sort Algorithm

    Theta Notation:
        - Partion Subroutine yields "n" (linear) time complexity.

    > Arguments:
        - A (list): List of numbers to be sorted;
        - low (int): Lower index of the subarray;
        - high (int): Higher index of the subarray.
    
    > Output:
        - (int): Pivot index.
    """
    # Identify pivot element (highest) and left barrier (lowest)
    pivot_elem, pivot_index = A[high], low

    # Iterate over elements and find pivot position/index
    for j in range(low, high):
        if A[j] <= pivot_elem:
            A[pivot_index], A[j] = A[j], A[pivot_index]
            pivot_index += 1
    
    # Put pivot element at the correct position/index
    A[pivot_index], A[high] = A[high], A[pivot_index]

    # Return pivot position/index
    return pivot_index


def _quick_sort(A:list, low:int, high:int) -> list:
    """Quick Sort Algorithm

    Big-O Notation:
        - Quick sort yields "n**2" (quadratic) time complexity.
    
    Expected running time of "n*lg(n)".
    
    > Arguments:
        - A (list): List of numbers to be sorted;
        - low (int): Lower index of the subarray;
        - high (int): Higher index of the subarray.
    
    > Output:
        - No outputs, the function sorts in place.
    """
    # Recursively sort the array using the partioning subroutine
    if low < high:
        pivot = _partition_quick_sort(A, low, high)
        _quick_sort(A, low, pivot-1)
        _quick_sort(A, pivot+1, high)


def quick_sort(A:list, method:str="standard") -> list:
    """Quick Sort Algorithm

    Big-O Notation:
        - Quick sort yields "n**2" (quadratic) time complexity.
    
    Expected running time of "n*lg(n)".
    
    Although the worst-case (Big-O) is quadratic, the expected running 
    time of the quick sort algorithm is "n*lg(n)". Also the quick sort
    notably beats others algotihms because it has small hidden constant
    factors in the time complexity notations, and has the advantage of 
    sorting in place (consumes less memory space). So, quick sort is 
    often the best practical choice for sorting.
    
    > Arguments:
        - A (list): List of numbers to be sorted;
        - method (str): Algorithm configuration.
            ---> Options: "standard", "randomized"
            ---> Defaults to "standard"
    
    > Output:
        - (list): Sorted list on ascending order.
    """
    # Standard Approach
    if method == "standard":
        B = A[:]
        _quick_sort(B, 0, len(B)-1)
        return B
    
    # Randomized Approach
    elif method == "randomized":
        B = A[:]
        i = random.randint(0, len(B)-1)
        B[-1], B[i] = B[i], B[-1]
        _quick_sort(B, 0, len(B)-1)
        return B

    # Method not implemented
    else:
        raise NotImplementedError(f"Method '{method}' not implemented!\n")


if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    A = [6, 4, 5, 2.4, 7.5, 10, 7, 4, 9, 8,]
    print("\n>> Quick Sort Examples:")
    print(f"\nOriginal List: {A}")
    print(f"Standard Quick Sort: {quick_sort(A, 'standard')}")
    print(f"Randomized Quick Sort: {quick_sort(A, 'randomized')}\n")