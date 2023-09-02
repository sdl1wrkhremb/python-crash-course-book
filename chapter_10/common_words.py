from pathlib import Path


def count_words(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        number_of_words = len(words)
        print(f"The file {path} contains about {number_of_words} words.")


def count_word(path, word):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        word_count = contents.lower().count(word)
        print(f"The file {path} contains '{word}' about {word_count} times.")


count_words(Path('alice.txt'))
count_word(Path('alice.txt'), 'the')
