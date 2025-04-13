# main.py
from stats import get_num_words

def get_book_text(book):
    with open(book, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    pages = get_book_text("books/frankenstein.txt")
    words_count = get_num_words(pages)  # Use the imported function here
    print(f"{words_count} words found in the document")

if __name__ == "__main__":
    main()
