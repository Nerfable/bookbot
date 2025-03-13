from stats import get_num_words, get_dict_num_characters, chars_dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    dict_num_characters = get_dict_num_characters(book_text)
    sorted_list = chars_dict_to_sorted_list(dict_num_characters)
    print_report(book_path, num_words, sorted_list)


def get_book_text(file_path):
    with open(file_path) as f: 
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted_list:
        if char["char"].isalpha() == False:
            continue
        
        print(f"{char['char']}: {char['num']}")
    
    print("============= END ===============")









main()






























