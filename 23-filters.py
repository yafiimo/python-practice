nums = [8, 76, 23, 5, 98, 1, 85, 42, 63]

def remove_even(number):
    return number % 2 != 0

odd_numbers = []

# for loop method
for num in nums:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)

# comprehensions method
print([ num for num in nums if num % 2 != 0 ])

# filter method
print(list(filter(remove_even, nums)))
