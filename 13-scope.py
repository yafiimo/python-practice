myName = 'Mario'

def changeName():
    myName = 'Luigi'
    print(f'My name is {myName}')

changeName()
print(f'My name is {myName}')

# From above, defining variable myName again inside the function scope
# has no effect on the global variable myName

myName2 = 'Toad'

def changeName2():
    global myName2
    myName2 = 'Koopa'
    print(f'My name 2 is {myName2}')

changeName2()
print(f'My name 2 is {myName2}')

# Using the global myName2 in changeName2() allows the global variable
# myName2 to be changed from within the function
