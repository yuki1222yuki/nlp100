word1 = 'パトカー'
word2 = 'タクシー'
result1 = ''
result2 = ''
for (i, j) in zip(word1, word2):
    result1 += i+j

#zipを知らない場合
for i in range(len(word1)):
    result2 += word1[i] + word2[i]

print(result1, result2)