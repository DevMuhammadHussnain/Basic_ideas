"""
Qno.61: Create a Person class with name, age, and a method to say hello.

Difficult words:
- class: blueprint/template to create objects.
- attributes: data stored in an object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


p = Person("Ali", 20)
p.say_hello()
