#!/usr/bin/env python3
def print_fibonacci(length):
    fib_sequence = [0, 1]
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(fib_sequence)

# Example usage
print_fibonacci(10)
