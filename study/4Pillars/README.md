# 4 Pillars 

## **OOP basic pillars**

1. Inheritance
2. Abstraction
3. Polymorphism
4. Encapsulation

## OOP - Inheritance

• Purpose: reuse existing code

• Reusable class is generic

• By inheriting some class, the
subclass gets: 

properties and methods from the
super class that are "public" or "protected"

Example:

```py
class Animal:
  sound: str
  def __init__(self, sound: str) -> None:
     self.sound = sound
     return None
def makeSound(self) -> None:
  print(self.sound)
  return None

class Cat(Animal):
  def __init__(self) -> None:
     super().__init__("Meow!")
     return None

class Dog(Animal):
  def __init__(self) -> None:
     super().__init__("Wuff!")
     return None
```

## OOP - Abstraction

Example:
Animal is an abstract class

Cat is Non-abstract, concrete class

• Abstract class can have methods with
implementations in them: difference to interfaces here is that
interfaces can’t have implementations.

• Defining abstract class means that developer may not create instance directly from it.

Abstraction hides complex implementation details and shows only the essential features of an object. 

It’s like using a TV remote – you press buttons without knowing the internal circuits. In code, we often use abstract classes (that cannot be instantiated) to define a blueprint, and then subclasses fill in the details.

```py

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):                 # implement the abstract method
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
# shape = Shape()                  # Error: cannot instantiate abstract class
rect = Rectangle(5, 3)
circ = Circle(2)
print(rect.area())                  # 15
print(circ.area())                   # 12.56

```
## How it shows abstraction:
Shape is an abstract class that defines what a shape should do (area()) but not how. The subclasses provide the concrete implementation. Users of Rectangle or Circle just call area() without worrying about the formula inside.

##  Polymorphism

Polymorphism means "many forms". It allows different classes to be treated as the same type, and the same method name can behave differently based on which object calls it. For example, both Dog and Cat have a speak() method, but they produce different sounds.

```py

class Bird:
    def speak(self):
        return "Chirp"

class Dog:
    def speak(self):
        return "Woof"

def make_sound(animal):
    # The same function works with any object that has a speak() method
    print(animal.speak())

# Usage
bird = Bird()
dog = Dog()
make_sound(bird)   # Chirp
make_sound(dog)    # Woof

```

How it shows polymorphism:
The function make_sound() doesn't care about the type of animal – it just calls speak(). Each object provides its own implementation, so the same method name produces different results.


## Encapsulation

Encapsulation bundles data and methods inside a class and hides the internal details from outside. It's like a capsule - you only expose what is necessary and protect the data from accidental changes. Often done with private variables and public getter/setter methods.

```py

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private attribute (two underscores)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount")

    def get_balance(self):             # public method to access private data
        return self.__balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)                  # Deposited 500. New balance: 1500
print(account.get_balance())           # 1500
# print(account.__balance)             # Error: cannot access private attribute directly

```

How it shows encapsulation:
The __balance attribute is hidden from outside code. You can only change it through the controlled deposit method, and read it via get_balance(). This protects the data from being set to an invalid value.

 [vocabularyOOP1][def]

[def]: ./vocabularyOOP1.png

[vocabularyOOP2][def]
[def]: ./vocabularyOOP2.png