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
subclass gets: Properties and methods from the
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