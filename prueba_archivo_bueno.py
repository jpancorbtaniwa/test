import random
import string

def generate_random_string(length: int = 10) -> str:
    """
    Generate a random string of lowercase letters.

    Parameters:
    length (int): Length of the random string to generate. Default is 10.

    Returns:
    str: Randomly generated string.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    letters = string.ascii_lowercase
    return ''.join(random.choices(letters, k=length))

def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: Factorial of the given number.
    """
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Parameters:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n: int) -> list:
    """
    Generate a list of Fibonacci numbers up to the nth number.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: List of Fibonacci numbers.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def bubble_sort(arr: list) -> list:
    """
    Sort a list of numbers using the bubble sort algorithm.

    Parameters:
    arr (list): The list of numbers to sort.

    Returns:
    list: Sorted list of numbers.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(arr: list, x: int) -> int:
    """
    Perform binary search on a sorted list to find the index of a given element.

    Parameters:
    arr (list): The sorted list to search.
    x (int): The element to search for.

    Returns:
    int: Index of the element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The GCD of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple (LCM) of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The LCM of the two numbers.
    """
    return abs(a*b) // gcd(a, b)

def reverse_string(s: str) -> str:
    """
    Reverse a given string.

    Parameters:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

def main():
    print("Random String:", generate_random_string())
    print("Factorial of 5:", calculate_factorial(5))
    print("Is 7 prime?:", is_prime(7))
    print("First 10 Fibonacci numbers:", fibonacci(10))
    print("Bubble Sort [64, 34, 25, 12, 22, 11, 90]:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print("Binary Search for 22 in [11, 12, 22, 25, 34, 64, 90]:", binary_search([11, 12, 22, 25, 34, 64, 90], 22))
    print("GCD of 54 and 24:", gcd(54, 24))
    print("LCM of 54 and 24:", lcm(54, 24))
    print("Reverse of 'hello':", reverse_string('hello'))
    print("Is 'racecar' a palindrome?:", is_palindrome('racecar'))

if __name__ == "__main__":
    main()
