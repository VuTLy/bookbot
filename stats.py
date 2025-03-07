def count_words(text):
    word = text.split()
    return len(word)

def appearence(text):
    total = {}
    
    for character in text.lower():
        if character in total:
            total[character] += 1
        else:
            total[character] = 1
    return total 