"""	Простые делители числа 13195 — это 5, 7, 13 и 29.
Какой самый большой делитель числа 600851475143, являющийся простым числом?"""
import math
import os
import sys

from profiler import profile, timer


@profile
def is_prime(num):
    """Checks if num is prime number"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


@timer
def find_prime_factors(num):
    """Find prime factors of num"""
    result = []
    i = 2
    while i * i <= num:
        if is_prime(i) and not num % i:
            result.append(i)
        i += 1
    return result


if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
    except (TypeError, ValueError, IndexError):
        sys.exit(f"Usage: {os.path.basename(__file__)} number")
    if num < 1:
        sys.exit("Error: number must be greater than zero")

    prime_factors = find_prime_factors(num)

    if len(prime_factors) == 0:
        print(f"Can't find prime factors of {num}")
    else:
        print(f"Answer: {prime_factors[-1]}")
