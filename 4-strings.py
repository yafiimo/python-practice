greeting = 'hello there'
person = 'midge'

#You can slice a string

greeting.upper()                        # returns 'HELLO THERE'
greeting[0:5]                           # returns 'hello'
greeting[1:]                            # returns 'ello there'
greeting[-5:-1]                         # returns 'ther'
person * 2                              # returns 'midgemidge'
sentence = greeting + ' ' + person      # returns 'hello there midge'
len(greeting)                           # returns length of greeting ie 10
type(greeting)                          # returns type of greeting ie <class 'str'>
sentence.split(' ')                     # splits sentence wherever there is a space and returns as a list nb string.split() with no argument returns the same
# cannoy split with empty string '', can instead use list(sentence)
print(list(sentence))
