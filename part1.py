#File: part1.py
#Author: Xavier Mathews
#Date: October 6, 2023
#Description: Program that computes the Extended GCD of two integers and calculates the Bézout coefficients using the extended Euclidean algorithm.
#License: MIT License

import sys


# Function to compute the extended GCD and Bézout coefficients
def extended_gcd(a, b):
    """
        Computes the Extended GCD of two integers and calculates the Bézout coefficients using the extended Euclidean algorithm.

        Args:
        a (int): First integer input
        b (int): Second integer input

        Returns:
        tuple: A tuple (gcd, x, y) where gcd is the GCD of a and b, and x, y are Bézout coefficients for a and b respectively.
        If both a and b are 0, returns ("Undefined", 0, 0).
        """
    if a == 0 and b == 0:
        # Special case: if both a and b are 0, the GCD is undefined.
        return "Undefined", 0, 0
    elif b == 0:
        # Base case: If b is 0, the GCD is a and Bézout coefficients are 1 and 0.
        return a, 1, 0

    # Handle negative inputs by taking their absolute values.
    a = abs(a)
    b = abs(b)

    # Recursive step: Calculate GCD, x1, and y1 using the remainder and recursively find coefficients.
    gcd, x1, y1 = extended_gcd(b, a % b)

    # Calculate Bézout coefficients for the current step.
    x = y1
    y = x1 - (a // b) * y1

    # If either input was negative, adjust the signs of x and y accordingly.
    if a < 0:
        x = -x
    if b < 0:
        y = -y

    return gcd, x, y


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filename.py a b")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("Invalid input. Please provide valid integer values for a and b.")
        sys.exit(1)

    # Calculate the GCD and Bézout coefficients using the extended Euclidean algorithm.
    gcd, x, y = extended_gcd(a, b)

    # Display the results.
    print(f"GCD of {a} and {b} is {gcd}")
    print(f"Bézout coefficients: x = {x}, y = {y}")
