#File: part3.py
#Author: Xavier Mathews
#Date: October 6, 2023
#Description: This script calculates the Greatest Common Divisor (GCD) of two integers using the Middle-School Procedure. It handles special cases where both inputs are 0, returning "Undefined.
#MIT License

import sys

# Function to calculate the GCD using the Middle-School Procedure
def gcd_middle_school(m, n):
    """
       Calculates the GCD of two integers using the Middle-School Procedure.

       Args:
       m (int): First integer input
       n (int): Second integer input

       Returns:
       int or str: GCD of the input integers, or "Undefined" if both inputs are 0.
       """
    m = abs(m)
    n = abs(n)

    if m == 0 and n == 0:
        return "Undefined"

    while n:
        # The Middle-School Procedure involves repeatedly taking the remainder of m divided by n.
        # Swap m and n, and set n as the remainder of m divided by n.
        m, n = n, m % n

    return m


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filename.py m n")
        sys.exit(1)

    try:
        m = int(sys.argv[1])
        n = int(sys.argv[2])
    except ValueError:
        print("Invalid input. Please provide valid integer values for m and n.")
        sys.exit(1)

    # Calculate the GCD using the Middle-School Procedure
    calculated_gcd = gcd_middle_school(m, n)

    # Displaying the result
    print(f"GCD of {m} and {n} is {calculated_gcd}")
