# define a dictionary
ninja_belts = {'ryu': 'black', 'crystal': 'red', 'king': 'purple'}
print(ninja_belts)

# add to dictionary
ninja_belts['paul'] = 'blue'
print(ninja_belts)

# to get a value from a key
ninja_belts['ryu']                  # will return the value 'black'

# to check if a key exists in a dictionary
'paul' in ninja_belts               # returns true as 'paul' exists in ninja_belts
'lee' in ninja_belts                # returns false as 'lee' does not exist

# to get a list of keys for a dictionary
ninja_belts.keys()
print(ninja_belts.keys())           # returns a list of keys, type 'dict_keys'
print(type(ninja_belts.keys()))
print(list(ninja_belts.keys()))     # converts the list of keys to type 'list'

# to get a list of values for a dictionary
ninja_belts.values()
print(ninja_belts.values())           # returns a list of values, type 'dict_values'
print(type(ninja_belts.values()))
print(list(ninja_belts.values()))     # converts the list of values to type 'list'

# to get a list of items for a dictionary
ninja_belts.items()
print(ninja_belts.items())                   # returns a list of items, type 'dict_values'
print(type(ninja_belts.items()))
print(list(ninja_belts.items()))             # converts the list of items to type 'list'
print(type(list(ninja_belts.items())[0]))    # each item in the list is of type tuple: ('key', 'value')


# another way of defining a dictionary
person = dict(name='Amad', age=23, height='5ft10"')
print(person)
