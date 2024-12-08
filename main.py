def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    word_count = count_words(text)
    uses_count = letter_uses(text)

    print(f'Word use report for {file_path}')
    print(f'{word_count} words in file')
    for c in uses_count:
        print(f' {c} used {uses_count[c]} times')

#pulls in text from file_path
def get_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
#counts words from file_path
def count_words(text):
    words = text.split()
    return len(words)

#count uses of letter uses in book
def letter_uses(text):
    dictionary = {}
    lowercase_text = text.lower()
    for i in lowercase_text:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary


main()