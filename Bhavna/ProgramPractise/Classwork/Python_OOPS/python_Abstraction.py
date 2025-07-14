# 11/07/2025 Session - Absent

"""
Abstraction in Python
# focus on simplify the complex code structure by hiding the import and internal information from the user
# and provide the overview of the particular project.

# In abstraction parent class method will be override by child class, and implimentation will be done inside
# the child class.

"""

class Animal:
    def name(self):
        pass

    def voice(self):
        pass

    def breed(self):
        pass

class Dog(Animal):

    def name(self):
        print("Dog name: Tommy")

    def voice(self):
        print("Voice of Dog: Barking")

    def breed(self):
        print("Breed of dog: Labrador")

obj = Dog()

obj.name()
obj.breed()
obj.voice()