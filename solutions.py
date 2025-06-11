

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
