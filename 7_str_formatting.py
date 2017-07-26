num1 = 23.456655
num2 = 9.1287789

# Previous printing method
print('num 1 is', num1, 'and num 2 is', num2)

# FORMATTING METHOD
print('num 1 is {0} and num 2 is {1}'.format(num1, num2))       # num1 has index 0, num2 has index 1
print('num 1 is {1} and num 2 is {0}'.format(num2, num1))       # num1 has index 1, num2 has index 0

print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))     # add colon for formatting, .3 meaning 3 digits
print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))     # add colon for formatting, .3f meaning 3 dp

# F-STRINGS
print(f'num 1 is {num1} and num 2 is {num2}')       # add the f before string to allow variables within string
print(f'num 1 is {num1:.4} and num 2 is {num2:.4}')     # same formatting available
print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}')

person1 = dict(name='Amad', age='23', height='5ft10')
person2 = dict(name='Huss', age='19', height='5ft5')
person3 = dict(name='Alu', age='21', height='5ft1')

# :20 for strings makes string take up 20 characters
print(f'{"Name":20} {"Age":20} {"Height:":20}')
print(f'{person1["name"]:20} {person1["age"]:20} {person1["height"]:20}')
print(f'{person2["name"]:20} {person2["age"]:20} {person2["height"]:20}')
print(f'{person3["name"]:20} {person3["age"]:20} {person3["height"]:20}')
