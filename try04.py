#原子番号12はMgだが問題の設定上Miになる
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

words = sentence.split()
for num, word in enumerate(words, 1):
    if num in index:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num

print(result)
