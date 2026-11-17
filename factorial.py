
import sys

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial of", num, "is", factorial(num))
