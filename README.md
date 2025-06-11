# COMP 170 SU25 WEEK 03

This assignment has two parts: a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.

# Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.

# Code

## Diamond shape

Write a function `draw_diamond` that draws a diamond shape of a specified height passed as a parameter to the function. To solve this problem, first think what instructions you'll give someone drawing the diamong by pressing three keys on their keyboard: the space key, the hash mark key, and the enter key. For example, here's a 5-lines diamond and the keyboard instructions. It's important to *discover* if there is a connection between the line number and the number of spaces and hash marks (hint: there is).

```text
  #     : 1st line : space space hash enter
 ###    : 2nd line : space hash hash hash enter
#####   : 3rd line : hash hash hash hash hash enter
 ###    : 4th line : space hash hash hash enter
  #     : 5th line : space space hash enter
```

Solve this problem on paper first. Avoid the temptation to ask AI or to search online for a solution. It is an easy problem to code and the internet is full of solutions. This exercise however is about designing the solution on paper. Take out a piece of paper. Draw a few vertical and horizontal lines creating a square grid. Fill the squares to produce a diamond shape. Count the number of empty squares (spaces) and the number of filled squares (hashmarks) and discover how they relate to the line you are on (first line, second line etc.)

## Right triangle

Write a function `draw_right_triangle` that draws a right angle triangle whose height is specified as a parameter to the function.


## Compound interest

Write a function `compound_interst` that computes the compound interest for a given amount, a given annual interest rate, and a given period of time. For example, over a 5 year period, an initial investment of $1,000, earning 5% interest will accumulate as follows:

* 1st year: $1,000 principal + $1,000 x 0.05 interest = $1,050
* 2nd year: $1,050 principal + $1,050 x 0.05 interest = $1,102.50
* 3rd year: $1,102.50 principal + $1,102.50 x 0.05 interest = $1,157.62
* 4th year: $1,157.62 principal + $1,157.62 x 0.05 interest = $1,215.50
* 5th year = $1,215.50 principal + $1,215.50 x 0.05 interest = $1,276.27

The amount of $1,276.27 is the compound interest for this specific example. Your function *should not use* any exponential operations. Just loops, additions, and multiplications.

## Hollow square 

Write a function `draw_hollow_square` that draws a square that is empty in the middle. The size of the square's and the thickness of its edge should be given as parameters. For example `draw_hollow_square(8,2)` should produce the following drawing:

```text
########
########
##    ## 
##    ## 
##    ## 
##    ##  
########
########
```

# Reflect

Review the posted [solutions from the previous assignment](./solutions.py). Compare the posted solutions with your solutions. Notice the differences between your code and the solutions code and describe them. Trivial differences like the names of variables are not that important unless your names are really - I mean, *really -* weird.
