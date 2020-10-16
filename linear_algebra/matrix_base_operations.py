"""
Base operations for 2D Matrices

Author: Marcus Moresco Boeno
Date: 2020-10-16

Implements functions that perform basic operations with 2D matrices

"""

def _matrixMult_std(A:list, B:list) -> list:
    """Standard Multiplication of 2D Matrices

    Theta Notation:
        - Standard approach yields "n**3" (cubic) time complexity.
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - B (matrix): Nested list representing a 2D matrix.
    
    > Output:
        - Matrix with multiplication results.    
    """
    # Check if number of columns in A is equal to the number
    # of rows in B
    if len(A[0]) != len(B):
        raise ValueError(f"Matrices dimensions do not match!\n")
    else:
        # Create empty matrix do store results
        C = [[0 for i in range(len(B[0]))] for j in range(len(B))]

        # Iterate over rows of A
        for i in range(len(A)):

            # Iterate over columns of B
            for j in range(len(B[0])):
                
                # Iterate over elements and add results to C
                tmp = 0
                for k in range(len(A[0])):
                    tmp +=A[i][k]*B[k][j]
                C[i][j] = tmp
        
        # Return results
        return C

def matrix_multiply(A:list, B:list, method="standard") -> list:
    """Maximum Subarray Algorithm
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - B (matrix): Nested list representing a 2D matrix.
        - method (str): Method to multiply matrices.
            ---> Options: "standard";
            ---> Defaults to "standard".
    
    > Output:
        - Tuple with indices and sum of the maximum subarray
    """
    # Standard 2D Multiplication
    if method == "standard":
        return _matrixMult_std(A, B)
    
    # Method not implemented
    else:
        raise NotImplementedError(f"Method '{method}' not implemented!")

if __name__ == "__main__":

    # Declare a list and find the maximum subarray for example purposes
    A = [[2, -1], [1, 3]]
    B = [[1, 2, -1], [3, 4, 0]]
    print("\n>> 2D Matrix Multiplication Examples:")
    print(f"\nMatrix A: {A}")
    print(f"Matrix B: {B}\n")
    print(f"    > Standard Approach: {matrix_multiply(A, B, 'standard')}\n")
