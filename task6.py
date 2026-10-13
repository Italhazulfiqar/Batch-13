# Task 6: Find the square root of a real or complex number.
import cmath

num = 1 + 2j

# Uncomment below to take input from the user (for example, 1+2j).
# num = complex(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(
    num, num_sqrt.real, num_sqrt.imag
))

# Output:
# The square root of (1+2j) is 1.272+0.786j
