def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

def count_num_words(input_text):
    word_list = input_text.split()
    num_words = len(word_list)
    return num_words

def main():
    text = (get_book_text("./books/frankenstein.txt"))
    count = count_num_words(text)
    print(f"{count} words found in the document")

main()