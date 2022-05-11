# Given a string, detect whether or not it is a pangram. 
# Return True if it is, False if not. Ignore numbers and punctuation.

# Clever Solution:
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))
  
# Small Brain:
def is_pangram(s):
    alpha = list(range(65, 91))
    s = s.upper()
    
    for _ in s:
        if ord(_) in alpha:
            alpha.pop(alpha.index(ord(_)))
    
    if len(alpha) == 0:
        return True
    else:
        return False
