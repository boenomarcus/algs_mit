"""
Maximum Subarray Algorithm in Python

Author: Marcus Moresco Boeno
Date: 2020-10-14

Implements functions that find the maximum subarray (nonempty,
contiguous subarray of A whose values have the largest sum) using
different approaches as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def max_subarray_bf(A:list) -> list:
    """Brute Force Approach for the Maximum Subarray Algorithm
    
    > Arguments:
        - A (list): Array of numbers (int or float).
    
    > Output:
        - Maximum subarray (list).
    """
    # Create variables to store results
    beg, end, diff = 0, 0, 0
    
    # Iterate over list using a brute force approach
    for i in range(len(A)-1):
        tmp = A[i]
        for j in range(i, len(A)-1):
            tmp += A[j]
            if tmp > diff:
                beg, end, diff = i, j, tmp
    
    # Return sorted list
    return A[beg:end+1]


if __name__ == "__main__":

    # Declare a list and find the maximum subarray for example purposes
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7,]
    print("\n>> Maximum Subarray Examples:")
    print(f"\nOriginal List: {A}")
    print(f"Maximum Subarray (Brute Force Approach): {max_subarray_bf(A)}\n")