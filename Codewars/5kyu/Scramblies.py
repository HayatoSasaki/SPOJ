# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

def scramble(s1, s2):
    for x in set(s2):
        if s2.count(x) > s1.count(x):
            return False
    return True
