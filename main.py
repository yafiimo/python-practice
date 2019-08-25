from functools import reduce

# Check if a value is classified as a boolean primitive. Return true or false.
def booWho(x):
  return True if type(x) == bool else False
print('booWho:', booWho(False), booWho(25))

# Create a function that looks through an array and returns the first element
# in the array that passes a truth test
def findElement(arr, func):
  return next((x for x in arr if func(x)), 'undefined')
print('findElement:', findElement([1,2,3], lambda x: x > 10))

# Truncate a string if it is longer than the given maximum string length
def truncateString(string, num):
  return string[0:num] + '...' if len(string) > num else string
print('truncateString:', truncateString('A-tisket a-tasket A green and yellow basket', 8), truncateString('A-tisket', 10))

# repeat a string num times
def repeatString(string, num):
  if num <= 0:
    return ''
  return string + repeatString(string, num - 1)
print('repeatString:', repeatString('yo', 4))

# confirm the ending of a string
def confirmEnding(string, end):
  return string[len(string) - len(end):] == end
print('confirmEnding:', confirmEnding('calculate', 'ulate'))

# Return an array consisting of the largest number from each provided sub-array
def largestOf(arr):
  largest = []
  for i in range(len(arr)):
    largest.append(reduce(lambda num1, num2: num2 if num2 > num1 else num1, arr[i]))
  return largest
print('largestOf:', largestOf([[1,2,3], [66, 8, 100]]))

# convert to celsius
def convertToCelsius(celsius):
  fahrenheit = (celsius) * (9/5) + 32
  return fahrenheit
print('convertToCelsius:', convertToCelsius(-30))

# return the factorial of a number
def factorialise(num):
  if num == 1:
    return 1
  return num * factorialise(num - 1)
print('factorialise:', factorialise(5))

# reverse a string
def reverseString(string):
  # could use string[::-1]
  return ''.join(list(reversed(string)))
print('reverseString:', reverseString('hello'))

# return length of longest word in a string
def longestWord(string):
  words = string.split(' ')
  longest = ''
  for w in words:
    if len(w) > len(longest):
      longest = w
  return len(w)
print('longestWord:', longestWord('this is a sentence'))

# title case a sentence
def titleCase(string):
  words = string.lower().split(' ')
  updatedSentence = []
  for w in words:
    updatedSentence.append(w.replace(w[0], w[0].upper()))  
  return ' '.join(updatedSentence)
print('titleCase:', titleCase('hello there mY naMe is mo'))

# copy each element of the first array into the second array
# starting from index n
def frankenSplice(arr1, arr2, n):
  return arr2[:n] + arr1 + arr2[n:]
print('frankenSplice:', frankenSplice([1,2,3], [100,200,300,400,500], 2))

# remove falsy values
def removeFalsy(arr):
  # return list(filter(lambda x: x, arr))
  # or
  return [x for x in arr if x]
print('removeFalsy:', removeFalsy([1,2,0,False,True]))

# Return the lowest index at which a value (second argument) should be 
# inserted into an array (first argument) once it has been sorted

def getIndexToIns(arr, num):
  sortedArr = sorted(arr)
  return next((i for i,x in enumerate(sortedArr) if num <= x), len(arr))
print('getIndexToIns:', getIndexToIns([9, 8, 7, 6, 5], 7))

# Return true if the string in the first element of the array contains all of 
# the letters of the string in the second element of the array.
def mutation(arr):
  string = arr[0].lower()
  substr = arr[1].lower()
  matches = True
  for x in substr:
    if x not in string:
      matches = False
      break
  return matches
print('mutation:', mutation(['hello', 'who']), mutation(['hello', 'he']))

def chunkArrayInGroups(arr, size):
  newArr = []
  for x in range(0, len(arr), size):
    subArr = arr[x:x+size]
    newArr.append(subArr)

  return newArr
  
print(chunkArrayInGroups([1,2,3,4,5,6,7], 2))