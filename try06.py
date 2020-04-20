def n_gram(target, n):
    result = set()
    for i in range(len(target) - (n-1)):
        sample = tuple(target[i:(i+n)])
        result.add(sample)
    return result

sentenceA = "paraparaparadise"
sentenceB = "paragraph"

X = n_gram(sentenceA, 2)
Y = n_gram(sentenceB, 2)

print(X)
print(Y)
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

target = 'se'
Z = n_gram(target, 2)
print(Z)
#
print(Z <= X)
print(Z <= Y)
