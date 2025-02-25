import sys
from stats import count_words
from stats import count_characters
from stats import chars_dict_to_sorted_list

def main():
    # Checks if the program is getting the argument that represents the path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Reads the text file and save it inside file_contents
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    
    # Outputs a report of total words and characters that the book has
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
    characters_dictionary = count_characters(file_contents)
    sorted_list = chars_dict_to_sorted_list(characters_dictionary)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["number"]}")
    print("============= END ===============")

main()
