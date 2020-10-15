"""
Maximum Subarray Algorithm in Python

Author: Marcus Moresco Boeno
Date: 2020-10-15

Implements functions that find the maximum subarray (nonempty,
contiguous subarray of A whose values have the largest sum) using
different approaches as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def _maxSubarray_DaC(A:list, low:int, high:int) -> tuple:
    """Divide and Conquer Approach for the Maximum Subarray Algorithm

    Theta Notation:
        - Divide and Conquer yields "n*lg(n)" time complexity.
    
    > Arguments:
        - A (list): Array of numbers (int or float);
        - low (int): Lowest index to consider for the subarray;
        - high (int): Highest index to consider for the subarray.
    
    > Output:
        - Tuple with indices and sum of the maximum subarray.
    """
    # Conquer Step
    #
    # Base case, when there is only one element left
    if low == high:
        return low, high, A[low]
    else:

        # Divide Step
        #
        # Getting left and right max subarrays
        mid = (low+high)//2
        left_low, left_high, left_sum = _maxSubarray_DaC(A, low, mid)
        right_low, right_high, right_sum = _maxSubarray_DaC(A, mid+1, high)

        # Getting Max-Crossing Subarray - Right index
        cross_r_sum, b_sum = float("-inf"), 0
        for j in range(mid+1, len(A)-1):
            b_sum += A[j]
            if b_sum > cross_r_sum:
                cross_r_sum, cross_high = b_sum, j
        
        # Getting Max-Crossing Subarray - Left index
        cross_l_sum, b_sum = float("-inf"), 0
        while mid >= 0:
            b_sum += A[mid]
            if b_sum > cross_l_sum:
                cross_l_sum, cross_low = b_sum, mid
            mid -= 1
        cross_sum = cross_l_sum + cross_r_sum

        # Combine step (Get max subarray)
        #
        # Max subarray is on the left
        if left_sum >= cross_sum and left_sum >= right_sum:
            return left_low, left_high, left_sum
        # Max subarray is on the right
        elif right_sum >= cross_sum and right_sum >= left_sum:
            return right_low, right_high, right_sum
        # Max subarray crosses the middle
        else:
            return cross_low, cross_high, cross_sum


def _maxSubarray_BF(A:list) -> tuple:
    """Brute Force Approach for the Maximum Subarray Algorithm

    Theta Notation:
        - Brute Force yields "n**2" (quadratic) time complexity.
    
    > Arguments:
        - A (list): Array of numbers (int or float).
    
    > Output:
        - Tuple with indices and sum of the maximum subarray.
    """
    # Create variables to store results
    array_sum = float("-Inf")
    
    # Iterate over list using a brute force approach
    for i in range(len(A)-2):
        tmp = A[i]
        for j in range(i+1, len(A)-1):
            tmp += A[j]
            if tmp > array_sum:
                low, high, array_sum = i, j, tmp
    
    # Return sorted list
    return low, high, array_sum


def maximum_subarray(A:list, method="divide_conquer") -> tuple:
    """Maximum Subarray Algorithm
    
    > Arguments:
        - A (list): Array of numbers (int or float);
        - method (str): Method to get maximum subarray.
            ---> Options: "brute_force", "divide_conquer";
            ---> Defaults to "divide_conquer".
    
    > Output:
        - Tuple with indices and sum of the maximum subarray
    """
    # Divide and Conquer Aproach
    if method == "divide_conquer":
        return _maxSubarray_DaC(A, 0, len(A)-1)
    
    # Brute Force Approach
    elif method == "brute_force":
        return _maxSubarray_BF(A)

    # Method not implemented
    else:
        raise NotImplementedError(f"Method '{method}' not implemented!")


if __name__ == "__main__":

    # Declare a list and find the maximum subarray for example purposes
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7,]
    print("\n>> Maximum Subarray Examples:")
    print(f"\nOriginal List: {A}")

    # Brute For Approach
    print(f"\nMaximum Subarray (Brute Force Approach)")
    bf_indices = maximum_subarray(A, "brute_force")
    print(f"    > Subarray: {A[bf_indices[0]:bf_indices[1]+1]}")
    print(f"    > Indices: {bf_indices[0]}:{bf_indices[1]}")
    print(f"    > Sum: {bf_indices[2]}")

    # Divide and Conquer
    print(f"\nMaximum Subarray (Divide-and-Conquer Approach)")
    dc_indices = maximum_subarray(A, "divide_conquer")
    print(f"    > Subarray: {A[dc_indices[0]:dc_indices[1]+1]}")
    print(f"    > Indices: {dc_indices[0]}:{dc_indices[1]}")
    print(f"    > Sum: {dc_indices[2]}\n")
