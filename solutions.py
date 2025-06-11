"""
Function to greet a person
Write a function named greet that takes one argument, say name, and returns a greeting string. For example, greet("Thomas") should return the string:

Hello Thomas. How are you?
Greet a few friends
Create a simple list (not a dictionary) with the names of some friends. For example:

my_friends = ["Frodo", "Sam", "Gandalf"]
Then write a function that takes the list of friends and prints a greeting for every one of them using function greet(name) from earlier.

Solve an equation
 the equation has no solutions among real numbers (and we don't want to deal with complex numbers, at least not yet.

Write a function called solve_quadratic that takes three arguments, a, b, and c, and prints the solutions to the quadratic equation or prints the message "no real solutions".
"""

def greet(name: str) -> str:
  return f"Hello {name}. How re you?"

my_friends = ["rodo", "Sam", "Gandalf", "Saruman", "Elrond"]

def greet_friends(friends: list) -> None:
  for name in friends:
    print(greet(name))

def solve_quadratic(a: float, b: float, c: float) -> None:
  discriminant = b*b-4*a*c
  if discriminant < 0:
    print "no real solutions"
  else:
    common_factor = sqrt(discriminant)/(2*a)
    x1 = -b+ common_factor
    x2 = -b- common_factor
    print(f"{x1=}\n{x2=}")
