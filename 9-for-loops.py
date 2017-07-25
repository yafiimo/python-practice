fighters = ['Goku', 'Krillin', 'Yamcha', 'Gohan', 'Piccolo', 'Vegeta']

print('\nPrint all fighters:')
for fighter in fighters:
    print(fighter)
print('\n')

print('Print some fighters')
for fighter in fighters[0:4]:
    print(fighter)
print('\n')

print('Print race of fighters')
for fighter in fighters:
    if fighter == 'Goku' or fighter == 'Gohan' or fighter == 'Vegeta':
        print(f'{fighter} - Saiyan')
    elif fighter == 'Piccolo':
        print(f'{fighter} - Namekian')
    else:
        print(f'{fighter} - Human')
print('\n')

print('Break if Namekian')
for fighter in fighters:
    print(fighter)
    if fighter == 'Piccolo':
        break
