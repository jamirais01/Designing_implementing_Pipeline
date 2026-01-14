class Person:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.occupation}"

matti = Person("Matti", "Meikäläinen", 28, "Software Developer")

print("Person created:")
print(matti)

print("\nIndividual attributes:")
print(f"First name: {matti.first_name}")
print(f"Last name: {matti.last_name}")
print(f"Age: {matti.age}")
print(f"Occupation: {matti.occupation}")

matti.age = 29
print(f"\nMatti's new age: {matti.age}")