
# To start a class use the keyword class 
class Pokemon():

    def __init__(self, name, hp, can_evolve): # self is an instane of self and shows the belongs to it.
       self.name = name
       self.hp = hp
       self.evolves = can_evolve

    def attack(self, opponent):
        if opponent.hp > self.hp:
            print(f'{self.name} is paralysed with fear')
        else:
            print(f'{self.name} fought with courage')

    def evolve(self):
        if self.name.lower() == 'magikarp':
            previousName = self.name
            self.name = "Garados"
            self.evolves = False
            print(f'Congrats your {previousName} is now a {self.name}')
        else:
            print(f'{self.name} can not evolve')

    # static method cannot make use of self
    def some_other_method():
        print('.....executed....')












"""
sandslash = Pokemon(name="Sandslash", hp=70, can_evolve=False)
magikarp = Pokemon(name="Magikarp", hp=80, can_evolve=True)

magikarp.attack(sandslash)
magikarp.evolve()
sandslash.evolve()

print(f'{sandslash.name} has {sandslash.hp} HP')
print(f'{magikarp.name} has {magikarp.hp} HP')

# This is a static method
Pokemon.some_other_method()
"""