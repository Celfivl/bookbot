# main.py
from stats import get_num_words, count_chars, sorted_chars
import sys

def get_book_text(book):
    with open(book, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    pages = get_book_text(sys.argv[1])
    
    words_count = get_num_words(pages)  # Use the imported function here
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    char_counts = count_chars(pages)

    sorted_list = sorted_chars(char_counts)

    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()




