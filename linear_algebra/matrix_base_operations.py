"""
Base operations for 2D Matrices

Author: Marcus Moresco Boeno
Last Update: 2020-10-18

Implements functions for basic operations with 2D matrices

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
    # Check if matrices dimensions match
    if _dimChecker(A, B, operation="multiply"):

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

    # Raise an error if the dimensions do not match
    else:
        raise ValueError(f"Matrices dimensions do not match!\n")


def _squarePadding(A:list, l:int, padding=0) -> list:
    """Square-Padding Function
    
    Rezises matrix to an even-square matrix.
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - l (int): Resize factor (matrix will become size lxl);
        - padding (int): Integer to be added to matrix.
            ---> Defaults to 0.
    
    > Output:
        - Resized matrix (do not share content with original matrix).
    """
    # Check if resize factor is valid
    if len(A) > l or len(A[0]) > l:
        # Raise an error if the resize factor is out of bounds 
        raise ValueError(f"Resize factor (l = {l}) is out of bounds\n")
    
    # Check if resizing is necessary
    elif len(A) == l and len(A[0]) == l:
        # Return a deep copy of the original matrix
        return [row[:] for row in A]
    
    # Resizing when necessary
    else:
        # Make a deep copy of A
        B = [row[:] for row in A]
        
        # Adding columns
        cols_diff = l - len(A[0])
        for row in B:
            row.extend(cols_diff*[padding])

        # Adding rows
        rows_diff = l - len(A)
        B.extend(rows_diff*[l*[padding]])
        
        # Return resized matrix
        return B


def _dimChecker(*m:list, operation:str) -> bool:
    """2D Matrix Dimension Checker
    
    Checks whether matrices have matching dimensions for the
    desired operation or not.
    
    > Arguments:
        - m (list): List of 2D matrices;
        - operation (str): Desired operation.
            ---> Options: "add", "subtract", "multiply".
    
    > Output:
        - Boolean indicating if the operation is feasible.
    """
    # Check conditions for matrices addition and subtraction
    if operation in ["add", "subtract"]:
        rows, cols = len(m[0]), len(m[0][0])
        for i in range(1, len(m)):
            if len(m[i]) != rows or len(m[i][0]) != cols:
                # Return False when matrices dimension do not match
                return False
        # Return True when matrices dimensions match
        return True 

    # Test conditions for matrices multiplication
    elif operation == "multiply":
        if len(m[0][0]) != len(m[1]):
            # Return False when matrices dimension do not match
            return False
        # Return True when matrices dimensions match
        return True

    # Operation not implemented
    else:
        raise NotImplementedError(f"Operation {operation} not implemented!\n")


def matrix_add(*m:list) -> list:
    """Addition of 2D Matrices

    Theta Notation:
        - Addition yields "n**2" (quadratic) time complexity.
    
    > Arguments:
        - m (list): List of 2D matrices.
    
    > Output:
        - Matrix with addition results
    """
    # Check if matrices dimensions match
    if _dimChecker(m, operation="add"):
        # Return results
        #   obs:
        #     - lcs: Elements for a given i,j position
        #     - ls: List of elements for a given i (line) position
        #     - *m: List of 2D matrices
        return [[sum(lcs) for lcs in zip(*ls)] for ls in zip(*m)]
    
    # Raise an error if the dimensions do not match
    else:
        raise ValueError("Matrices dimensions do not match!\n")


def matrix_multiply(A:list, B:list, method="standard") -> list:
    """Multiplication of 2D Matrices

    Theta Notation:
        - "standard" yields "n**3" (cubic) time complexity;
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - B (matrix): Nested list representing a 2D matrix.
        - method (str): Method to multiply matrices.
            ---> Options: "standard";
            ---> Defaults to "standard".
    
    > Output:
        - Matrix with multiplication results
    """
    # Standard 2D Multiplication
    if method == "standard":
        return _matrixMult_std(A, B)
    
    # Method not implemented
    else:
        raise NotImplementedError(f"Method '{method}' not implemented!\n")


if __name__ == "__main__":

    # Declare matrices and apply some basic operations
    A = [[2, -1], [1, 3]]
    B = [[1, 2, -1], [3, 4, 0]]
    C = [[5, 0, -3], [4, 3, 2]]
    D = [[-2, 1, 4], [0, 7, -4]]

    # Multiplication
    print("\n>> 2D Matrix Multiplication Examples:")
    print(f"\nMatrix A: {A}")
    print(f"Matrix B: {B}\n")
    print(f"  > Standard Approach (A.B): {matrix_multiply(A, B, 'standard')}\n")

    # Addition
    print(">> 2D Matrix Addition Example:")
    print(f"\nMatrix B: {B}")
    print(f"Matrix C: {C}")
    print(f"Matrix D: {D}\n")
    print(f"  > B+C+D: {matrix_add(B, C, D)}\n")
