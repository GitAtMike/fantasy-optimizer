# Write a recursive function factorial(n) that return n!.
# Example: factorial(5) -> 120.
# It must call itself - no loops

def factorial(n):

    product = 0

    if n == 0 or n == 1:
        return 1
    else:
        product = n * factorial(n-1)

    return product

print(factorial(5))