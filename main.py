from stats import count_words, appearence, most_common

def get_book_text(file):
    with open(file) as f:
        return f.read()
    

def main():

    path = "books/frankenstein.txt"
    contents = get_book_text(path)
    num_words = count_words(contents)
    appear = appearence(contents)
    most = most_common(appear)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in most:
        print(f"{count['char']}: {count['count']}")    
    print("============= END ===============")

if __name__ == "__main__":
    main()