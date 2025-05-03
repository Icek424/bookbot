def get_num_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return (word_count)




def num_of_characters(text):

    num_char = {}

    for char in text:
        low_char = char.lower()
        if low_char not in num_char:
          num_char[low_char] = 1
        else:
          num_char[low_char] += 1
    return num_char


def sorted_dictionary(char_count):
    char_list = []
    
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=lambda x: x["num"])

    return char_list

    
