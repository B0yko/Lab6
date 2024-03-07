# Task 1
def sumN(n):
    return n * (n + 1) // 2
def sumNCubes(n):
    return (n * (n + 1) // 2) ** 2
def main():
    n = int(input("Enter a number: "))
    sum_n = sumN(n)
    print(f"Sum of the first {n} natural numbers: {sum_n}")

    sum_n_cubes = sumNCubes(n)
    print(f"Sum of the cubes of the first {n} natural numbers: {sum_n_cubes}")

    fibonacci_n = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {fibonacci_n}")

    result = factorial(n)
    print(f"The factorial of {n} is: {result}")

#Task 2
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        fib_prev = 0
        fib_current = 1
        for _ in range(2, n):
            fib_prev, fib_current = fib_current, fib_prev + fib_current
        return fib_current

#Task 3
def factorial(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
main()
