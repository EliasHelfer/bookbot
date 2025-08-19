from stats import count_num_words
from stats import count_chars
from stats import sort_by_num
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

    
def main():
    text = (get_book_text("./books/frankenstein.txt"))
    count = count_num_words(text)
    frequency = count_chars(text)
    frequency = sort_chars(frequency)
    print ("============ BOOKBOT ============")
    print (f"Analysing book found at books/frankenstein.txt")
    print ("============ Word Count ============")
    print(f"Found {count} total words in the document")
    print ("============ Character Count ============")
    for item in frequency:
        if item["char"].isalpha() == False:
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")
    print ("============ END ============") 
  

main()