#File: part2.py
#Author: Xavier Mathews
#Date: October 6, 2023
#Description: Calculates the GCD of two integers using the consecutive Integer Checking Algorithm
#MIT License

import sys

# Function to calculate the GCD using the Consecutive Integer Checking Algorithm
def gcd_consecutive_integer(m, n):
    """
        Calculates the GCD of two integers using the Consecutive Integer Checking Algorithm.

        Args:
        m (int): First integer input
        n (int): Second integer input

        Returns:
        int or str: GCD of the input integers, or "Undefined" if both inputs are 0.
        """
    # Base cases: if m and n are equal or one of them is zero
    if m == n:
        return m
    if m == 0 or n == 0:
        return "Undefined"

    # Handling even numbers using their divisors of 2
    if m % 2 == 0 and n % 2 == 0:
        return 2 * gcd_consecutive_integer(m // 2, n // 2)
    elif m % 2 == 0:
        return gcd_consecutive_integer(m // 2, n)
    elif n % 2 == 0:
        return gcd_consecutive_integer(m, n // 2)
    # Handling odd numbers and the recursive subtraction step
    elif m > n:
        return gcd_consecutive_integer(m - n, n)
    else:
        return gcd_consecutive_integer(m, n - m)

if __name__ == "__main__":
    # Checking command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python filename.py m n")
        sys.exit(1)

    try:
        # Parsing integer values for m and n from command-line arguments
        m = int(sys.argv[1])
        n = int(sys.argv[2])
    except ValueError:
        print("Invalid input. Please provide valid integer values for m and n.")
        sys.exit(1)

    # Handling the special case where both m and n are 0
    if m == 0 and n == 0:
        gcd = "Undefined"
    else:
        # Calculating the GCD using the consecutive integer checking algorithm
        gcd = gcd_consecutive_integer(m, n)

    # Displaying the result
    print(f"GCD of {m} and {n} is {gcd}")
