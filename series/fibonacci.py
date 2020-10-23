"""
Fibonacci calculation

Author: Marcus Moresco Boeno
Last Update: 2020-10-23

Implements functions to calculate fibonacci series

"""


def _fibo_recursive(n:int) -> int:
    """Recursive Approach for Fibonacci Series Calculation

    Theta Notation:
        - Recursive approach yields "2**n" (expo) time complexity.
    
    > Arguments:
        - n (int): Index of the fibonacci sequence.
    
    > Output:
        - Fibonacci number for the given index.
    """
    # Conquer step for base cases (n == 0 or n == 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Divide and combine steps
    else:
        return _fibo_recursive(n-1) + _fibo_recursive(n-2)


def _fibo_bottom_up(n:int) ->list:
    """Bottom-Up Approach for Fibonacci Calculation

    Theta Notation:
        - Bottom-Up approach yields "n" (linear) time complexity.
    
    > Arguments:
        - n (int): Index of the fibonacci sequence.
    
    > Output:
        - Fibonacci number for the given index.
    """
    # Check for base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Compute fibonacci for cases where n >= 2
    else:
        # Create variables to store last two indices
        a, b = 0, 1
        for i in range(2, n+1):
            c = a+b
            a, b = b, c
        
        # Return results
        return c


def fibo(n:int, method="bottom-up") -> int:
    """Fibonacci Numbers Computation

    Theta Notation:
        - "recursive" yields "2**n" (exponential) time complexity;
        - "bottom-up" yields "n" (linear) time complexity.
    
    > Arguments:
        - n (int): Index of the fibonacci sequence;
        - method (str): Method to calculate the fibonacci number.
            ---> Options: "recursive", "bottom-up";
            ---> Defaults to "bottom-up".
    
    > Output:
        - Fibonacci number for the given index
    """
    # Recursive Algorithm
    if method == "recursive":
        return _fibo_recursive(n)
        
    # Bottom-Up Algorithm
    elif method == "bottom-up":
        return _fibo_bottom_up(n)
        
    # Method not implemented
    else:
        raise NotImplementedError(f"Method '{method}' not implemented!\n")


if __name__ == "__main__":

    print("\n>> Fibonacci Examples:")

    # Recursive Approach
    print(f"\n  > Recursive Approach:")
    print(f"    - Fib[0:11] = {[fibo(n, 'recursive') for n in range(11)]}")
    print(f"    - Fib[10:21] = {[fibo(n, 'recursive') for n in range(10, 21)]}")
    print(f"    - Fib[30] = {fibo(30, 'recursive')}")

    # Bottom-Up Approach
    print(f"\n  > Bottom-Up Approach:")
    print(f"    - Fib[0:11] = {[fibo(n, 'bottom-up') for n in range(11)]}")
    print(f"    - Fib[10:21] = {[fibo(n, 'bottom-up') for n in range(10, 21)]}")
    print(f"    - Fib[30] = {fibo(30, 'bottom-up')}\n")
    
