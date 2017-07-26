from random import shuffle

def randomise(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['kachumbari', 'samaki', 'katlesi', 'sambusa']
anagrams = []

# for loop method
for word in words:
    anagrams.append(randomise(word))
print(anagrams)

anagrams = []

# map method
print(list(map(randomise, words)))

# comprehensions method
print([ randomise(word) for word in words ])
