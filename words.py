def print_upper_words(list, chars={'h'}):
    """prints out a list of words all in uppercase, each on a separate line"""

    for word in list:
        for char in chars:
            if word.lower()[0] == char.lower():
                print(word.upper())

print(print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]))
print(print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], chars={'h', 'y'}))