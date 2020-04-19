sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.split(' ')
result = [len(word.strip('.,')) for word in words]
print(result)
