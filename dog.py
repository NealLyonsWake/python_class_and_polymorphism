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

    def species():
        return 'Canis lupus familiarise'

alan = Dog(name="Alan", breed = "Westy", greet = "woof woof", age=2)

# print(alan.bark())
# print(alan.dog_years())

# outside of Dog class call
#print(species()) # <= knackered and doesn't work does it!

# instance of Dog class call
#print(Dog.species())


class TalkingDog(Dog):

    def __init__(self, name, breed, greet, age):
        super().__init__(name, breed,greet, age)
      

    def bark(self, greet):
        return (f'{self.name} says {greet}')


whisper = TalkingDog(name="Whisper", breed="parrot",greet="Hello", age=2)

print(whisper.bark("Hello"))

