# stats.py
def get_num_words(text):
    words = text.split()
    return len(words)
# total number of words ^
def count_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        # checks for char in list, adds or increases the count respectively
    return char_count

def sorted_chars(char_count):
    chars_list = []

    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list