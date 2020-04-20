def generate_sentence(x, y, z):
    #x時のyはz
    return '{hour}時の{index}は{value}'.format(hour=x, index=y, value=z)

x = 12
y = '気温'
z = 22.4

print(generate_sentence(x, y, z))
