# define the decorator

def new_line_dec(func):
    def wrapper(body):
        print('\nYour letter: \n\nDear Person,\n')
        func(body)
        print('\nYours faithfully, \n\nYafiimo')
    return wrapper

# the decorator wraps around to your function and is called whenever the
# function is executed
@new_line_dec
def print_letter(body):
    print(body)

body = input('\nType out the body of your letter:\n\n')

# print_letter() -> new_line_dec() -> wrapper() -> calls print_letter within wrapper code
print_letter(body)
