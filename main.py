from stats import word_count
from stats import number_for_each_character
from stats import sort_Dict
from stats import print_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_information = f.read()
        return book_information

def main():
    if len(sys.argv) != 2:
        print("- 'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)

    book_filepath = sys.argv[1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_filepath}...")
    text = get_book_text(book_filepath)
    print(f"----------- Word Count ----------")
    word_count(text)
    print("--------- Character Count -------")
    result = number_for_each_character(text)
    print(print_dict(result))
    print("============= END ===============")


if __name__ == "__main__":
    main()