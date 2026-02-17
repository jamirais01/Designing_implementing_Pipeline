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
### How it shows abstraction:
Shape is an abstract class that defines what a shape should do (area()) but not how. The subclasses provide the concrete implementation. Users of Rectangle or Circle just call area() without worrying about the formula inside.
