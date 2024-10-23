def add(a, b):
    """Returnerar summan av två tal."""
    return a + b

def subtract(a, b):
    """Returnerar skillnaden mellan två tal."""
    return a - b

def multiply(a, b):
    """Returnerar produkten av två tal."""
    return a * b

def divide(a, b):
    """Returnerar kvoten av två tal. Om b är 0, returnera None."""
    if b == 0:
        return None
    return a / b

def is_even(number):
    """Returnerar True om ett tal är jämnt, annars False."""
    return number % 2 == 0

def factorial(n):
    """Returnerar n-fakultet. Om n är negativt, returnera None."""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def reverse_string(s):
    """Returnerar en omvänd version av en sträng."""
    return s[::-1]

def is_palindrome(s):
    """Returnerar True om en sträng är ett palindrom, annars False."""
    return s == s[::-1]

def count_vowels(s):
    """Returnerar antalet vokaler i en sträng."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def calculate_average(numbers):
    """Returnerar medelvärdet av en lista med tal. Returnerar None om listan är tom."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
