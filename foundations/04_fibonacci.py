# Write a recursive fib(n) function (plain recursion first, no memo yet) that
# that returns the nth Fibonacci number, where fib(0) = 0, fib(1) = 1, and
# fib(n) = fib(n - 1) + fib(n - 2) for anything higher.

# Example: fib(6) -> 8 (sequence is 0, 1, 1, 2, 3, 5, 8).
import time

def fib(n, memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

start = time.time()
print(fib(70))
end = time.time()
print(f"Took {end - start:.2f} seconds")