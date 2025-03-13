def get_num_words(text):
    splitted_text = text.split()
    num_words = len(splitted_text)
    return num_words


def get_dict_num_characters(text):
    characters = text.lower()
    dict_num_chars = {}
    for char in characters:
        if char not in dict_num_chars:
            dict_num_chars[char] = 1
        else: 
            dict_num_chars[char] += 1
    return dict_num_chars


def sort_on(dict):
    return dict["num"]



def chars_dict_to_sorted_list(dict_num_chars):
    sorted_list = []
    for char in dict_num_chars:
        sorted_list.append({"char": char, "num": dict_num_chars[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list




        









