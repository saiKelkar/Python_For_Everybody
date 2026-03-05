# Variables, expressions, and statements

# Values and types
# type('Hello, world!') <-- class 'str'
# type(17) <-- class 'int'
# type(3.2) <-- class 'float'

# Variables <-- name that refers to a value
message = 'And now for something completely different' # <-- 'str'
n = 17 # <-- 'int'
pi = 3.1415926535897931 # <-- 'float'

# Operators and operands <-- +, -, *, /, **
# + <-- addition
# - <-- subtraction
# * <-- multiplication
# / <-- division
# ** <-- exponentiation
# // <-- floored division
# % <-- modulus operator, yields a remainder

# String operations
first = 10
second = 15
print(first + second) # <-- 25
first = '100'
second = '150'
print(first + second) # <-- 100150

first = 'Test'
second = 3
print(first * second) # <-- Test Test Test

prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt) # <-- 17
print(int(speed) + 5) # <-- 22
