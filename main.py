from stats import count_words

def get_book_text(file):
    with open(file) as f:
        return f.read()
    

def main():

    path = "books/frankenstein.txt"
    contents = get_book_text(path)
    num_words = count_words(contents)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()