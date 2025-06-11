# COMP 170 SU25 WEEK 02

For this week's assignment focus on last week's reading assignment and work on the following items.

## Function to greet a person

Write a function named `greet` that takes one argument, say `name`, and **returns** a greeting string. For example, `greet("Thomas")` should **return** the string:
```
Hello Thomas. How are you?
```

## Greet a few friends

Create a simple list (not a dictionary) with the names of some friends. For example:
```python
my_friends = ["Frodo", "Sam", "Gandalf"]
```
Then write a function that takes the list of friends and **prints** a greeting for every one of them using function `greet(name)` from earlier.

## Solve an equation

The quadratic equation is defined as $ax^2+bx+c=0$. When $b^2-4ac< 0$ the equation has no solutions among real numbers (and we don't want to deal with *complex numbers,* at least not yet. 

When however,  $b^2-4ac\geq 0$ the solutions to the equation are

$$
x_1 = \frac{-b-\sqrt{b^2-4ac}}{2a}
$$

and

$$
x_2 = \frac{-b+\sqrt{b^2-4ac}}{2a}
$$

Write a function called `solve_quadratic` that takes three arguments, `a`, `b`, and `c`, and **prints** the solutions to the quadratic equation or prints the message "no real solutions".
