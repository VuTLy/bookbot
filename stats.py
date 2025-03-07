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

def most_common(appear):
    sort_list = []
    for char in appear:
        if char.isalpha():
            mini_dict = {"char": char, "count": appear[char]}
            sort_list.append(mini_dict)
    sort_list.sort(reverse=True, key=lambda x: x['count'])

    return sort_list
