# Functions

# Built-in functions
print(max('Hello world'))
print(min('Hello world'))

# Type conversion functions
int('32') # <-- 32
int (3.999999) # <-- 3 ( truncates the rest)

# Math function
import math

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians)) # <-- 0.707106...

# Random numbers
import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10)) # <-- returns an integer between low and high, including both

t = [1, 2, 3]
print(random.choice(t))

# Custom functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print(print_lyrics())

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
print(repeat_lyrics())

# Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)

print(print_twice('Spam'))
print(print_twice('Spam ' * 4))