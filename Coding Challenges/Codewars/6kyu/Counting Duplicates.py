def duplicate_count(text):
    text = list(text)
    text = [ord(text[x]) for x in range(len(text))]
    count = sum([1 for x in list(set(text)) if text.count(x) > 1])
    count += sum(1 for x in text if x == [y-31 for y in text])
    return  count