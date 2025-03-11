from stats import get_num_words, count_letters, sort_dict


def get_book_text(ptf):
    with open(ptf) as f:
        file_contents = f.read()
    return file_contents







def main():
    contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(contents)
    letter_count = count_letters(contents)
    sorted_chars = sort_dict(letter_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]

        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")
    
    print("============= END ===============")

   
    







main()






































