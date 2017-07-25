# functions
def greet():
    print('Good morning user!')
greet()

# functions with parameters
def greet(name, time):
    print(f'Good {time} {name}')
greet('Amad', 'afternoon')

# functions with default parameters
def greet(name='Huss', time='morning'):
    print(f'Good {time} {name}, hope you are well!')
greet()
greet('Alu', 'night')
greet('Shids')
greet(time='evening', name='Rahms')

# using functions for calculations
def calc_area(radius):
    area = 3.142 * radius ** 2
    return area

def calc_volume(area, length):
    volume = area * length
    print(f'Volume = {volume:.2f}')

radius = int(input('What is the radius: '))
length = int(input('What is the length: '))

area = calc_area(radius)                        # can store return value of function in a variable
calc_volume(area, length)
calc_volume(calc_area(radius), length)          # can invoke a function as an argument of another function


# Can use a function as a parameter of a another function
def callFunction(myfunction):
    myfunction()

def printHello():
    print('Hello')

# Passing in the function printHello as an argument to callFunction()
callFunction(printHello)
