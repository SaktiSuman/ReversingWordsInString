def reverseWords(sentence):
    words = sentence.split(' ')
    reverse_words = ' '.join(reversed(words))
    return reverse_words
sentence = 'geeks for me'
print(reverseWords(sentence))