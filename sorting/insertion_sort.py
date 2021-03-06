"""
Insertion Sort Algorithm in Python

Author: Marcus Moresco Boeno
Last Update: 2020-11-09

Implements a function that sorts a list of elements using the 
insertion sort algorithm as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def insertion_sort(A:list) -> list:
    """Insertion sort algorithm

    Big-O Notation:
        - Insertion sort yields "n*2" (quadratic) time complexity.
    
    > Arguments:
        - A (list): List of numbers to be sorted.
    
    > Output:
        - (list): Sorted list on ascending order.
    """
    # Iterate from second to last element
    for j in range(1, len(A)):

        # Retrieve element as a key
        key = A[j]
        i = j - 1

        # Shuffle positions until find insertion point
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        
        # Insert element into right position
        A[i+1] = key

    # Return sorted list
    return A


if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    A = [6, 4, 5, 2.4, 7.5, 10, 7, 4, 9, 8,]
    print("\n>> Insertion Sort Example:")
    print(f"\nOriginal List: {A}")
    print(f"Sorted List: {insertion_sort(A)}\n")