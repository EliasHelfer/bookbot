from stats import count_num_words
from stats import count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

    
def main():
    text = (get_book_text("./books/frankenstein.txt"))
    count = count_num_words(text)
    frequency = count_chars(text)
    print(f"{count} words found in the document")
    print(frequency)

main()