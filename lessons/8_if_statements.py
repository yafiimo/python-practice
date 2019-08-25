age = int(input('What is your age: '))
print(f'Your age is {age}')

if age <= 10:
    print('\nYou are young, strange one!')
elif age < 20:
    print('The fire in you is strong strange one!\n')
else:
    print('You are very wise, strange one!\n')

jedi = input('Are you a jedi? (y/n): ')

if jedi == 'y':
    print('May the force be with you!')
elif jedi == 'n':
    print('May you master the ways of the jedi!')
else:
    print('That wasn\'t a very smart answer!')
