"""
@author: Bryan Quille
"""

# Finding the n-th number from Fibonacci serie

def fibonacci(n):
    
    if type(n) != int:
        print('You must enter a positive integer number.')
    elif n == 0:
        fib = [n]
        return f'The {n}-th Fibonacci number is: {fib[n]}'
    else:
        if n < 0:
            print('You must enter a positive integer number.')
        else:        
            fib = [0] * (n+1)    
            n0 = 0
            n1 = 1
            
            for i in range(n+1):
                if i == 0:
                    fib[i] = n0
                if i == 1:
                    fib[i] = n1
                else:
                    fib[i] = fib[i-1] + fib[i-2]
            return f'The {n}-th Fibonacci number is: {fib[n]}'




