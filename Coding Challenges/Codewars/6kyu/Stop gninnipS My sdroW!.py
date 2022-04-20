# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    sentence = sentence.split()
    for spin in range(len(sentence)):
        if len(sentence[spin]) >= 5:
            sentence[spin] = sentence[spin][::-1]
    return " ".join(sentence)
  # One line List Comprehension:     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
