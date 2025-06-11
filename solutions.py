
def greet(name: str) -> str:
  return f"Hello {name}. How re you?"

my_friends = ["Frodo", "Sam", "Gandalf", "Saruman", "Elrond"]

def greet_friends(friends: list[str]) -> None:
  for name in friends:
    print(greet(name))

def solve_quadratic(a: float, b: float, c: float) -> None:
  # Compute the discriminant -- it's important to determine if the equation 
  # has no real solutions
  discriminant = b * b - 4 * a * c
  # Check for real solutions
  if discriminant < 0:
    print ("no real solutions")
  else:
    # Group common operations together
    common_factor = math.sqrt(discriminant)/(2*a)
    x1 = - b + common_factor
    x2 = - b - common_factor
    print(f"{x1=}\n{x2=}")