# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.

def order(sentence):
    sentence = list(sentence.split())
    ordered = []
    for x in range(1, len(sentence)+1): 
        for s in range(len(sentence)): 
            if sentence[s].find(str(x)) != -1: 
                ordered.append(sentence[s])
    
    return " ".join(ordered)