# Task 13: Demonstrate nested if statements.
i = 10

if i == 10:
    # First if statement inside the outer if.
    if i < 15:
        print('i is smaller than 15')

    # Another if statement inside the outer if.
    if i < 12:
        print('i is smaller than 12 too')
    else:
        print('i is greater than or equal to 12')

# Output:
# i is smaller than 15
# i is smaller than 12 too
