class Fighter:

    # class level attributes, same for all instances of a class
    hp = 1000
    attack1 = dict(name='punch', power=30, accuracy=90)
    attack2 = dict(name='kick', power=40, accuracy=70)

    # init function
    def __init__(self, name, powerMultiplier, specialAttack, specialAttackPower):
        # instance attrs, different for each instance of a class
        self.name = name
        self.powerMultiplier = powerMultiplier
        self.specialAttack = specialAttack
        self.specialAttackPower = specialAttackPower

    # instance methods, can access both instance, and class level attrs
    # can only be called from instance object ie goku.s_punch()
    def s_punch(self):
        damage = self.powerMultiplier * self.attack1['power']
        print(f'{self.name} used special {self.attack1["name"]}...')
        print(f'The enemy lost {damage} HP!\n')

    def s_kick(self):
        damage = self.powerMultiplier * self.attack2['power']
        print(f'{self.name} used special {self.attack2["name"]}...')
        print(f'The enemy lost {damage} HP!\n')

    def s_attack(self):
        damage = self.specialAttackPower
        print(f'{self.name} used {self.specialAttack}...')
        print(f'The enemy lost {damage} HP!\n')

    # classmethods, can only access class level attrs
    # can be called from class and instance object ie Fighter.punch()
    # function the same for all instances of the class
    @classmethod
    def punch(cls):
        print(f'Fighter used {cls.attack1["name"]}...')
        print(f'The enemy lost {cls.attack1["power"]} HP!\n')

    @classmethod
    def kick(cls):
        print(f'Fighter used {cls.attack2["name"]}...')
        print(f'The enemy lost {cls.attack2["power"]} HP!\n')

    # staticmethods, only have access to arguments passed in
    @staticmethod
    def randomAttack(fighter, name, power):
        print(f'{fighter} used {name}...')
        print(f'The enemy lost {power} HP!\n')
