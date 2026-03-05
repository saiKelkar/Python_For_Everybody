# Conditional execution

# x == y <-- comparision operator
# x != y <-- x is not equal to y
# x > y <-- x is greater than y
# x < y <-- x is less than y
# x >= y <-- x is greater than or equal to y
# x <= y <-- x is less than or equal to y
# x is y <-- x is the same as y
# x is not y <-- x is not the same as y

# = <-- assignment operator
# == <-- if two quantities are equal

# Logical operators

# and, or, not
# and <-- if both are True or both are False
# or <-- if either is True

# Conditional execution

x = 3
y = 5
# if block
if x < 10:
    print('Small')

# if-else block
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')

# if-elif-else block
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

# Nested conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


# try and except
inp = input('Enter Fahrenheit Temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')