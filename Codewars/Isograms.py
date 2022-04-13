# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(word):
    return len(word) == len(set(word.lower())) 
# If there is any repeating letter the lenght will be different, because of set, and return False.
