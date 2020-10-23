"""
Fibonacci calculation

Author: Marcus Moresco Boeno
Last Update: 2020-10-22

Implements functions to calculate fibonacci series

"""


def fibo_naive(n:int) -> int:
    """Naive Approach for Fibonacci Series Calculation

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


def fibo_caching(n:int, out="series") ->list:
    """Naive Approach with Cache for Fibonacci Series Calculation

    Theta Notation:
        - Naive approach with cache yields "n" (linear) time complexity.
    
    > Arguments:
        - n (int): Index of the fibonacci sequence;
        - out (str): Type of desired output.
            ---> Options: "series", "element";
            ---> Defaults to "series".
    
    > Output:
        - Fibonacci series from 0 up to the given index.
    """
    # Check if output type specified is valid
    if out in ["series", "element"]:
        # Iterating over indexes
        for i in range(n+1):
            if i == 0:
                fib = [0]
            elif i == 1:
                fib.append(1)
            else:
                fib.append(fib[i-1] + fib[i-2])
        
        if out == "series":
            # Return results
            return fib
        else:
            return fib[n]
    
    # Raise Error if type of output not allowed
    else:
        raise ValueError("Output type invalid, choose 'series' or 'element'\n")


if __name__ == "__main__":

    print("\n>> Fibonacci Examples:")

    # Naive Approach
    print(f"\n    > Naive Approach:")
    print(f"        - Fib[0:11] = {[fibo_naive(n) for n in range(11)]}")
    print(f"        - Fib[10:21] = {[fibo_naive(n) for n in range(10, 21)]}")
    print(f"        - Fib[30] = {fibo_naive(30)}")

    # Naive Approach with Cache
    print(f"\n    > Naive Approach with Cache:")
    print(f"        - Fib[0:11] = {fibo_caching(10, 'series')}")
    print(f"        - Fib[10:21] = {fibo_caching(20, 'series')[10:21]}")
    print(f"        - Fib[30] = {fibo_caching(30, 'element')}\n")
    
