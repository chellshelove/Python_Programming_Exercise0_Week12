def myfact(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * myfact(n - 1)

# Example usage:
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {myfact(number)}")