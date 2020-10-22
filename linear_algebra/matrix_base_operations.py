"""
Base operations for 2D Matrices

Author: Marcus Moresco Boeno
Last Update: 2020-10-22

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
    # Make a deep copy of B
    C = [row[:] for row in B]

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


def _matrixMult_DaC(A:list, B:list) -> list:
    """Divide and Conquer Approach for 2D Matrices Multiplication

    Theta Notation:
        - DaC approach yields "n**3" (cubic) time complexity.
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - B (matrix): Nested list representing a 2D matrix.
    
    > Output:
        - Matrix with multiplication results.    
    """
    
    # Conquer Step
    if len(A) == 2:
        # Return standard multiplication for 2x2 square matrix
        return _matrixMult_std(A, B)

    # Divide and Combine Steps
    else:

        # Get matrices dimensions
        n, m, p, q = len(A[0]), len(A), len(B[0]), len(B)

        # Get max dimension to apply padding
        l = max([n, m, p, q])
        if l%2 != 0:
            l += 1
        
        # Apply padding
        A_pad, B_pad = _squarePadding(A, l, 0), _squarePadding(B, l, 0)

        # Divide Step
        mid = len(A_pad)//2
        
        # Dividing A matrix
        a11 = [X[:mid] for X in A_pad[:mid]]
        a12 = [X[mid:] for X in A_pad[:mid]]
        a21 = [X[:mid] for X in A_pad[mid:]]
        a22 = [X[mid:] for X in A_pad[mid:]]

        # Dividing B matrix
        b11 = [X[:mid] for X in B_pad[:mid]]
        b12 = [X[mid:] for X in B_pad[:mid]]
        b21 = [X[:mid] for X in B_pad[mid:]]
        b22 = [X[mid:] for X in B_pad[mid:]]
            
        # Creating C Matrix elements
        c11 = matrix_add(
            _matrixMult_DaC(a11, b11),
            _matrixMult_DaC(a12, b21)
            )
        c12 = matrix_add(
            _matrixMult_DaC(a11, b12), 
            _matrixMult_DaC(a12, b22)
            )
        c21 = matrix_add(
            _matrixMult_DaC(a21, b11), 
            _matrixMult_DaC(a22, b21)
            )
        c22 = matrix_add(
            _matrixMult_DaC(a21, b12), 
            _matrixMult_DaC(a22, b22)
            )

        # Combine Step
        C = [a+b for a,b in zip(c11, c12)] + [a+b for a,b in zip(c21, c22)]

        # Return results
        return [row[:p] for row in C[:q]]


def _matrixMult_Strassen(A:list, B:list) -> list:
    """Strassen's Method for 2D Matrices Multiplication

    Theta Notation:
        - Strassen's approach yields "n**lg(7)" time complexity.
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - B (matrix): Nested list representing a 2D matrix.
    
    > Output:
        - Matrix with multiplication results.    
    """
    
    # Conquer Step
    if len(A) == 2:
        # Return standard multiplication for 2x2 square matrix
        return _matrixMult_std(A, B)

    # Divide and Combine Steps
    else:

        # Get matrices dimensions
        n, m, p, q = len(A[0]), len(A), len(B[0]), len(B)

        # Get max dimension to apply padding
        l = max([n, m, p, q])
        if l%2 != 0:
            l += 1
        
        # Apply padding
        A_pad, B_pad = _squarePadding(A, l, 0), _squarePadding(B, l, 0)

        # Divide Step
        mid = len(A_pad)//2
        
        # Dividing A matrix
        a11 = [X[:mid] for X in A_pad[:mid]]
        a12 = [X[mid:] for X in A_pad[:mid]]
        a21 = [X[:mid] for X in A_pad[mid:]]
        a22 = [X[mid:] for X in A_pad[mid:]]

        # Dividing B matrix
        b11 = [X[:mid] for X in B_pad[:mid]]
        b12 = [X[mid:] for X in B_pad[:mid]]
        b21 = [X[:mid] for X in B_pad[mid:]]
        b22 = [X[mid:] for X in B_pad[mid:]]
        
        # Base additions
        s1 = matrix_subtract(b12, b22)
        s2 = matrix_add(a11, a12)
        s3 = matrix_add(a21, a22)
        s4 = matrix_subtract(b21, b11)
        s5 = matrix_add(a11, a22)
        s6 = matrix_add(b11, b22)
        s7 = matrix_subtract(a12, a22)
        s8 = matrix_add(b21, b22)
        s9 = matrix_subtract(a11, a21)
        s10 = matrix_add(b11, b12)

        # Base multiplications
        p1 = _matrixMult_Strassen(a11, s1)
        p2 = _matrixMult_Strassen(s2, b22)
        p3 = _matrixMult_Strassen(s3, b11)
        p4 = _matrixMult_Strassen(a22, s4)
        p5 = _matrixMult_Strassen(s5, s6)
        p6 = _matrixMult_Strassen(s7, s8)
        p7 = _matrixMult_Strassen(s9, s10)

        # Creating C Matrix elements
        c11 = matrix_add(p5, matrix_subtract(p4, p2), p6)
        c12 = matrix_add(p1, p2)
        c21 = matrix_add(p3, p4)
        c22 = matrix_add(p5, matrix_subtract(p1, p3, p7))

        # Combine Step
        C = [a+b for a,b in zip(c11, c12)] + [a+b for a,b in zip(c21, c22)]

        # Return results
        return [row[:p] for row in C[:q]]


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
    # Check if only one matrix was provided
    if len(m) > 1:

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
    
    # Raise an error if only one matrix was provided
    else:
        raise ValueError("Not enough matrices to make computation!\n")


def matrix_subtract(*m:list) -> list:
    """Subtraction of 2D Matrices

    Theta Notation:
        - Subtraction yields "n**2" (quadratic) time complexity.
    
    > Arguments:
        - m (list): List of 2D matrices.
    
    > Output:
        - Matrix with subtraction results
    """
    # Check if only one matrix was provided
    if len(m) > 1:

        # Check if matrices dimensions match
        if _dimChecker(m, operation="subtract"):
            # Return results
            #   obs:
            #     - lcs: Elements for a given i,j position
            #     - ls: List of elements for a given i (line) position
            #     - *m: List of 2D matrices
            return [[lcs[0]-sum(lcs[1:]) for lcs in zip(*ls)] for ls in zip(*m)]

        # Raise an error if the dimensions do not match
        else:
            raise ValueError("Matrices dimensions do not match!\n")
    
    # Raise an error if only one matrix was provided
    else:
        raise ValueError("Not enough matrices to make computation!\n")


def matrix_multiply(A:list, B:list, method="standard") -> list:
    """Multiplication of 2D Matrices

    Theta Notation:
        - "standard" yields "n**3" (cubic) time complexity;
        - "divide_conquer" yields "n**3" (cubic) time complexity.
    
    > Arguments:
        - A (matrix): Nested list representing a 2D matrix;
        - B (matrix): Nested list representing a 2D matrix.
        - method (str): Method to multiply matrices.
            ---> Options: "standard", "divide_conquer", "strassen";
            ---> Defaults to "standard".
    
    > Output:
        - Matrix with multiplication results
    """
    # Check if matrices dimensions match
    if _dimChecker(A, B, operation="multiply"):

        # Standard 2D Multiplication
        if method == "standard":
            return _matrixMult_std(A, B)
        
        # Divide and Conquer Approach
        elif method == "divide_conquer":
            return _matrixMult_DaC(A, B)
        
        # Strassen's Approach
        elif method == "strassen":
            return _matrixMult_Strassen(A, B)
        
        # Method not implemented
        else:
            raise NotImplementedError(f"Method '{method}' not implemented!\n")
    
    # Raise an error if the dimensions do not match
    else:
        raise ValueError(f"Matrices dimensions do not match!\n")


if __name__ == "__main__":

    # Declare matrices and apply some basic operations
    A = [[2, -1], [1, 3]]
    B = [[1, 2, -1], [3, 4, 0]]
    C = [[2, 3, 3], [3, 1, 3], [-2, 0, 4]]
    D = [[3, 1], [2, 2], [1, 3]]
    E = [[5, 0, -3], [4, 3, 2]]
    F = [[-2, 1, 4], [0, 7, -4]]

    # Multiplication
    print("\n>> 2D Matrix Multiplication Examples:")
    print(f"\nMatrix A: {A}")
    print(f"Matrix B: {B}")
    print(f"Matrix C: {C}")
    print(f"Matrix D: {D}\n")
    print(f"  > Standard Approach (A.B): {matrix_multiply(A, B, 'standard')}")
    print("  > Divide and Conquer Approach (A.B): {}".format(
        matrix_multiply(A, B, 'divide_conquer')
        )
    )
    print("  > Strassen's Approach (A.B): {}\n".format(
        matrix_multiply(A, B, 'strassen')
        )
    )
    print(f"  > Standard Approach (C.D): {matrix_multiply(C, D, 'standard')}")
    print("  > Divide and Conquer Approach (C.D): {}".format(
        matrix_multiply(C, D, 'divide_conquer')
        )
    )
    print("  > Strassen's Approach (C.D): {}\n".format(
        matrix_multiply(C, D, 'strassen')
        )
    )
    
    # Addition
    print(">> 2D Matrix Addition Example:")
    print(f"\nMatrix B: {B}")
    print(f"Matrix E: {E}")
    print(f"Matrix F: {F}\n")
    print(f"  > B+E+F: {matrix_add(B, E, F)}\n")

    # Subtraction
    print(">> 2D Matrix Subtraction Example:")
    print(f"\nMatrix B: {B}")
    print(f"Matrix E: {E}")
    print(f"Matrix F: {F}\n")
    print(f"  > B-E-F: {matrix_subtract(B, E, F)}\n")
