import time


# Iterative Factorial Function
def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Recursive Factorial Function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


# ---------------- Main Program ----------------
if __name__ == "__main__":

    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")

    else:
        start_time = time.perf_counter()

        # Iterative Method
        iterative_result = factorial_iterative(n)
        print("\nFactorial using Iterative Method:", iterative_result)

        # Recursive Method
        recursive_result = factorial_recursive(n)
        print("Factorial using Recursive Method:", recursive_result)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print("\nExecution Time: {:.8f} seconds".format(execution_time))
