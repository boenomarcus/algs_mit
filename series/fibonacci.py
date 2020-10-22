"""
Fibonacci calculation

Author: Marcus Moresco Boeno
Last Update: 2020-10-22

Implements functions to calculate fibonacci series and elements

"""


def fibo_naive(n:int) -> int:
    """Naive Approach for Fibonacci element calculation

    Theta Notation:
        - Naive approach yields "2**n" (exponential) time complexity.
    
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
        return fibo_naive(n-1) + fibo_naive(n-2)


if __name__ == "__main__":

    print("\n>> Fibonacci Examples:")
    print(f"\n    > Naive Approach:")
    print(f"        - Fib[0:10] = {[fibo_naive(n) for n in range(10)]}")
    print(f"        - Fib[10:20] = {[fibo_naive(n) for n in range(10, 20)]}\n")
    
