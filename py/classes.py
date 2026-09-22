class Animal:
    def __init__(self, breed):
        self.breed = breed
    def displayBreed(self):
        print(f"This animal was a {self.breed}")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(breed)
        self.name = name
    def displayName(self):
        print(f"The name of this {self.breed} is {self.name}.")

ob = Dog("Ralph", "Pumerian")
ob.displayName()
