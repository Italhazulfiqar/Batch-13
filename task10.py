# Task 10: Convert kilometers to miles.
kilometers = float(input('Enter value in kilometers: '))

# Conversion factor.
conv_fac = 0.621371

miles = kilometers * conv_fac
print('{0} kilometers is equal to {1:.3f} miles'.format(kilometers, miles))

# Output:
# Enter value in kilometers: 10
# 10.0 kilometers is equal to 6.214 miles
