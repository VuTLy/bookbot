from stats import count_words, appearence, most_common
import sys

#Open file and read in content
def get_book_text(file):
    with open(file) as f:
        return f.read()
    

def main():

    #create commandline argument to pass in path 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    contents = get_book_text(path)
    num_words = count_words(contents)
    appear = appearence(contents)
    most = most_common(appear)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in most: #we format using the two key in the nested dict of char and the count
        print(f"{count['char']}: {count['count']}")    
    print("============= END ===============")

if __name__ == "__main__":
    main()