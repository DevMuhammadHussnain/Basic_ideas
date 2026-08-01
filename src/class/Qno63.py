"""
Qno.63: Define a Car class with make, model, and drive/stop methods.

Difficult words:
- model: product version/type.
"""

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"{self.make} {self.model} is driving...")

    def stop(self):
        print(f"{self.make} {self.model} has stopped.")


c = Car("Toyota", "Corolla")
c.drive()
c.stop()
