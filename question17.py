def word_counter(s):
    list_of_words = s.split(" ")
    return len(list_of_words)


# test
print(word_counter("hello my world. this is book"))
