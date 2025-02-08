def main():
    book_path = input("Eneter relative path to book: ")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count_dict = get_character_count(text.lower())
    aggregate_book_data(book_path, num_words, character_count_dict)


# takes in a file path to a books plain text and returns the read text file
def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

# takes in text string and returns the numbers of words as integer
def get_num_words(text):
    return len(text.split())

# takes in text string and returns a Dictionary of character:integer pairs, counting how many times each unqiue 
# character apears in the text. Prefers being passed a .lower() text string
def get_character_count(text):
    character_count = {}
    for character in text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

# takes the file path to the book, word count of the plain text, and the char count dict and
# generates a clean report 
def aggregate_book_data(book, num_words, char_count_dict):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    for char in alphabet:
        if char in char_count_dict:
            print(f"The '{char}' character was found {char_count_dict[char]} times")
    print("--- End Report ---")



main()