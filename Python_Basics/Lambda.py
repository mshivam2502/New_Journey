# Lambda Functions
# Syntax:
# lambda arguments: expression

# They offer a concise way to define simple, one-time-use functions, often used as arguments to higher-order functions like map(), filter(), or sorted().

# A lambda function to double a number
double = lambda x: x * 2
print(double(5)) # Output: 10

# Using lambda with filter() to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4, 6]