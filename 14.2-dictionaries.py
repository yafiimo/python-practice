def showFootballers(dict):
    for player, team in dict.items():
        print(f'{player} plays for {team}')

footballers = {}

while True:
    name = input('\nWhat is your footballer name?: ')
    team = input('What team do they play for?: ')
    footballers[name] = team

    while True:
        another = input('\nDo you want to enter another player? (y/n): ')
        if another == 'y' or another == 'n':
            break
        else:
            continue

    if another == 'y':
        continue
    else:
        break

showFootballers(footballers)
