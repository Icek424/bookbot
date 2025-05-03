import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    from stats import get_num_words
    from stats import num_of_characters
    from stats import sorted_dictionary

    # Check if correct number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    char_count = num_of_characters(text)
    sorted_characters =sorted_dictionary(char_count)
    for item in sorted_characters:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    

    print("============= END ===============")

main()