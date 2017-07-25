age = 1
limit = 25

while age < limit:
    if age == 1:
        print(f'you are only {age} year old, kid')
        age += 1
        continue
    if age < 18:
        print(f'you are still only {age} years old, kid')
    else:
        print(f'you are now {age} and old enough to call yourself an adult')
        break
    age += 1
