class Dog():

    def __init__(self, name, breed, greet, age): 
       self.name = name
       self.breed = breed
       self.greet = greet
       self.age = age

    def bark(self):
        return (f'{self.name} says {self.greet}')

    def dog_years(self):
        return (f'{self.name} is {self.age * 7} in dog years')

alan = Dog(name="Alan", breed = "Westy", greet = "woof woof", age=2)

print(alan.bark())
print(alan.dog_years())