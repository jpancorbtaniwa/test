import random
import string

# def generate_random_string(length=10):
#   letters = string.ascii_lowercase
#   return ''.join(random.choice(letters) for i in range(length))

# def calculate_factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * calculate_factorial(n-1)

# def is_prime(num):
#   if num <= 1:
#     return False
#   for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#       return False
#   return True

def fibonacci(n):
  fib_sequence = [0, 1]
  while len(fib_sequence) < n:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
  return fib_sequence

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

def binary_search(arr, x):
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

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return abs(a*b) // gcd(a, b)

def reverse_string(s):
  return s[::-1]

def is_palindrome(s):
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
