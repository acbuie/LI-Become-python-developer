# ----- Recursion ----- # 

"""
When a function calls itself
MUST have a breaking point, otherwise infinite loop
"""

# This should be validated for negatives...
# TODO Make countdown function
def countdown(x):
    if x == 0:
        print('Done!')
        return
    else:
        print(x, '...')
        countdown((x - 1))
        # Anything after here will be unwound when function returns
        # Aka, print('hi') will be called x times, after 'Done!'

# countdown(4)

# ----- Power and Factorial ----- #

# TODO Build power func
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * pwr(num, pwr-1)

# TODO Build factorial func
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)