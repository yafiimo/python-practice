def initCap(word):
    return word[0].upper() + word[1:]

sentence = ['hello', 'my', 'name', 'is', 'amad']

# Using a function already defined, in map
print(' '.join(list(map(initCap, sentence))))

# lambdas can be used as inline, anonymous functions
print(' '.join(list(map(lambda word: word[0].upper() + word[1:], sentence))))
