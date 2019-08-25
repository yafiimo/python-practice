list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8 , 9 , 10]

type(list1)                     # returns <class 'list'>
len(list1)                      # returns length of list1 = 5
list2[3]                        # returns index 3 of list2 = 9
list1[2:4]                      # = [3, 4]
list1[2:]                       # = [3, 4, 5]
list2[-3:]                      # = [8, 9, 10]
list2[-4:-1]                    # = [7, 8, 9]

numbers = list1 + list2         # concatenates lists = [1,2,3,4,5,6,7,8,9,10]
numbers.append(11)              # appends 11 to end of numbers
numbers.pop()                   # removes last item in numbers list
numbers.insert(0, 5)            # inserts the value 5 at index 0
del(numbers[5])                 # deletes index 5 of numbers
numbers.count(2)                # counts the number of times 2 appears in numbers
numbers.remove(7)               # removes first instance of 7 in numbers
list2.index(7)                  # returns index of first occurrence of 7 => 1
next((x for x in [1, 2, 3] if x > 1), 'default if not found') # returns first element which meets condition

random = ['mario', 2, 6, 'luigi', 5, 'bowser']                  # can store different types in lists
nestedList = [list1, list2, ['mario', 'luigi', 'bowser']]       # can nest lists

word = 'hello'
word = list(word)
print(word)
word = ''.join(word)
print(word)
