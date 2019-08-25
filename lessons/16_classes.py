from classes.fighters import Fighter

goku = Fighter('Goku', 5, 'Spirit Bomb', 300)

# class level attributes, accessible on both instance and class objects
print(goku.attack1)
print(Fighter.attack1)

# instance attributes, only accessible on instance object
print(goku.name)
print(goku.specialAttack)

# instance method, can only be called using instance object
# can access instance and class level attributes
goku.s_punch()
goku.s_kick()

# class method, can be called from instance or class object
# can only access class level attributes
goku.punch()
# Fighter.punch()
goku.kick()
# Fighter.kick()

# static method, can be called from instance or class object
# has no access to attributes in class, only the arguments passed in
goku.randomAttack(goku.name, 'headbutt', 100)
Fighter.randomAttack('Goku', 'flying kick', 200)
