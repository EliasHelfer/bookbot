def count_num_words(input_text):
    word_list = input_text.split()
    num_words = len(word_list)
    return num_words

def count_chars(input_text):
    frequency = {}
    ready_text = input_text.lower()
    for char in ready_text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
