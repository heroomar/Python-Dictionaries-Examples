sentence = "my name is ahmad,I am full stack developer"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)