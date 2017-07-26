print('\nloops from n=0 to n=4, ie up to 5 non-inclusive of 5')
for n in range(5):
    print(n)

print('\nloops from 1 to 6 non-inclusive of 6')
for n in range(1,6):
    print(n)

print('\nloop from 0 to 20 in steps of 4')
for n in range(0, 21, 4):
    print(n)

print('\nloop through list like a for loop')
food = ['chapatti', 'sambusa', 'katlesi', 'biryani', 'samaki']

for n in range(len(food)):
    print(n, food[n])

print('\nloop through list backwards')
for n in range(len(food) - 1, -1, -1):
    print(n, food[n])
    # starting from n=4, loop in steps of -1 until n=-1 non-inclusive
    # which covers all items in food array going backwards

# range(x, y, z)
# x is the starting point
# y is the end point non-inclusive
# z is the step size


# LOOPING BACKWARDS THROUGH A LIST
# using len(list)-1 as x makes the starting point the index of the last item in the list
# using -1 as z makes the loop go backwards
# using -1 as y (end point) loops through whole list including index 0
