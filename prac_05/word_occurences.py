text_string = input("Text: ").lower()
text_string = text_string.split(" ")
text_string.sort()

max_length = max((len(word) for word in text_string))

word_dict = {}
for word in text_string:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word in word_dict:
    print("{:<{}}: {}".format(word, max_length, word_dict[word]))
