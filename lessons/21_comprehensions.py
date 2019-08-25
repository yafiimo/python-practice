
nums = [1,2,3,4,5,6,7, 8]
doubled_nums = []

# double numbers in a list using a for loop
for num in nums:
    doubled_nums.append(num*2)
print(f'\n{"for loop method":30} {doubled_nums}')

doubled_nums = []
# double numbers in a list using comprehensions
doubled_nums = [ num * 2 for num in nums ]
print(f'{"comprehensions method":30} {doubled_nums}')


even_squared_nums = []
# squared even nums for loop method
for num in nums:
    num = num**2
    if num % 2 == 0:
        even_squared_nums.append(num)
print(f'{"for loop method":30} {even_squared_nums}')

even_squared_nums = []
# squared even nums comprehensions method
even_squared_nums = [ num ** 2 for num in nums if (num ** 2) % 2 == 0 ]
print(f'{"comprehensions method":30} {even_squared_nums}')
