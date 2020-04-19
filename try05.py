def n_gram(target, n):
    result = {}
    for i in range(len(target) - (n-1)):
        sample = tuple(target[i:(i+n)])
        if sample not in result:
            result[sample] = 1
        else:
            result[sample] += 1
    return result

sentence= "I am an NLPer"
words = sentence.split(' ')

word_bi_gram = n_gram(words, 2)
letter_bi_gram = n_gram(sentence, 2)

print(word_bi_gram)
print(letter_bi_gram)
