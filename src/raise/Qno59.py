"""
Qno.59: Raise an exception if task description is empty or too long.

Difficult words:
- description: detailed text about something.
"""

def validate_task_description(text):
    if text.strip() == "":
        raise ValueError("Task description cannot be empty.")
    if len(text) > 200:
        raise ValueError("Task description is too long (max 200 characters).")
    return True


desc = input("Enter task description: ")
try:
    if validate_task_description(desc):
        print("Task description is valid")
except ValueError as e:
    print(e)
