def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count



def count_letters(text):
    lower_cases = text.lower()
    letter_count = {}

    for char in lower_cases:
        if char  not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count


def sort_dict(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

        def sort_on(dict):
            return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
        









