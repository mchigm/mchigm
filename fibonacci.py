def fib(x):
    """
    Print the first x values of the Fibonacci sequence.
    
    Args:
        x: Number of Fibonacci numbers to print
    
    Examples:
        fib(3) prints: 0, 1, 1
        fib(5) prints: 0, 1, 1, 2, 3
    """
    if x <= 0:
        return
    
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    
    # Print Fibonacci numbers
    for i in range(x):
        if i == 0:
            print(a, end='')
        else:
            print(f', {a}', end='')
        a, b = b, a + b
    
    print()  # New line at the end
