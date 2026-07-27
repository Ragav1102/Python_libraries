#Encapsulation

import math


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount
    def TotalBalance(self):
        return self.__balance
a=BankAccount(1000)
a.deposit(1000)
print(a.TotalBalance())
print()

#Inheritance

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name+"makes a sound")
class Dog(Animal):
    def speak(self):
        print(self.name+"barks")
class Cat(Animal):
    def speak(self):
        print(self.name+"meow")
a=Animal("Animals ")
d=Dog("Tommy ")
c=Cat("Manoj ")
a.speak()
d.speak()
c.speak()   
print()

#polymorphism

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

r = Circle(5)
print(r.area())

s = Square(4)
print(s.area())
print()

#Abstraction

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start_Engine(self):
        pass
class Car(vehicle):
    def start_Engine(self):
        print("Car engine started")
class ElectricCar(vehicle):
    def start_Engine(self):
        print("Electric car engine started")

a=Car()
b=ElectricCar()

a.start_Engine()
b.start_Engine()





 
 
