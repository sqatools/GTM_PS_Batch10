"""
Abstraction in Python
# focus on simplify the complex code structure by hiding the import and internal information from the user
# and provide the overview of the particular project.

# In abstraction parent class method will be override by child class, and implimentation will be done inside
# the child class.

"""
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def voice(self):
       pass

    @abstractmethod
    def breed(self):
        pass


class Dog(Animal):

    def name(self):
        print("Dog name : Sheru")

    def voice(self):
        print("voice of dog : Barking")

    def breed(self):
        print("Breed of the dog :German Sheferred")



#obj = Dog()

obj = Animal()
obj.name()

obj.name()
obj.breed()
obj.voice()