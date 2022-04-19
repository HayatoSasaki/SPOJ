# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. 

# One line: idk why I did so many braindead conversions.
def narcissistic( value ):
    return value == sum([int(str(value)[n]) ** len(str(value)) for n in range(len(str(value)))])
    
# Decent:
def narcissistic( value ):
    value = str(value)
    narciso = 0
    for n in range(len(value)):
        narciso += int(value[n]) ** len(value)
    return narciso == int(value)    
