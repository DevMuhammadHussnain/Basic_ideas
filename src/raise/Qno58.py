"""
Qno.58: Raise an exception if input temperature is below absolute zero (-273.15°C).

Difficult words:
- absolute zero: lowest possible temperature.
"""

def validate_temperature(temp_c):
    if temp_c < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    return True


t = float(input("Enter temperature in °C: "))
try:
    if validate_temperature(t):
        print("Valid temperature")
except ValueError as e:
    print(e)
