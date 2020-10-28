"""
Array Randomizers

Author: Marcus Moresco Boeno
Last Update: 2020-10-28

Implements functions to randomize the order of array elements as 
described on Chapter 5 of the book "Introduction to Algorithms" 
by Thomas H. Cormen et al. (2009)

"""

# Standard library imports
import random


def _permute_by_sorting(A:list) -> list:
    """Permute Array Elements by Sorting Random Priorities

    Big-O Notation:
        - Permutation by Sorting yields "n*lg(n)" time complexity.
    
    > Arguments:
        - A (list): Array to be randomly rearranged.
    
    > Output:
        - Rearranged array.
    """
    # Get random element priorities (takes linear time)
    P = random.sample(range(len(A)**3), len(A))
    
    # Returned array through sorting of zip iterator (takes n*lg(n) time)
    return [x for _,x in sorted(zip(P, A))]


def _randomize_inPlace(A:list) -> list:
    """Permute Array Elements without Random Priorities

    Big-O Notation:
        - Randomize in Place yields "n" (linear) time complexity.
    
    > Arguments:
        - A (list): Array to be randomly rearranged.
    
    > Output:
        - Rearranged array.
    """
    # Create a deep copy of A
    X = A[:]

    # Iterating over array elements
    for i in range(len(X)):
        j = random.randint(0, len(X)-1)
        X[i], X[j] = X[j], X[i]
    
    # Return rearranged array
    return X


def array_randomize(A:list, method="in_place") -> list:
    """Rearrange Array Elements

    Big-O Notation:
        - "permute_sort" yields "n*lg(n)" time complexity;
        - "in_place" yields "n" (linear) time complexity
        
    > Arguments:
        - A (list): Array to be randomly rearranged.
        - method (str): Method to get randomized array.
            ---> Options: "permute_sort", "in_place".
            ---> Defaults to "in_place".

    > Output:
        - Rearranged array.
    """
    # Permute Array Elements by Sorting Random Priorities
    if method == "permute_sort":
        return _permute_by_sorting(A)
    
    # Permute Array Elements without Random Priorities
    elif method == "in_place":
        return _randomize_inPlace(A)
        
    # Method not implemented
    else:
        raise NotImplementedError(f"Method '{method}' not implemented!\n")


if __name__ == "__main__":

    # Declare array and get randomized rearrangements
    A = list(range(11))
    
    print("\n>> Array Randomizer Examples:")
    print(f"\nOriginal Array: {A}")
    
    # Permute Array Elements by Sorting Random Priorities
    print(f"\n   > Permute by Sorting: {array_randomize(A, 'permute_sort')}")
    
    # Permute Array Elements without Random Priorities
    print(f"   > Randomize in Place: {array_randomize(A, 'in_place')}\n")
