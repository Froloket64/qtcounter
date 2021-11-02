# qtcounter
A simple app that helps to train quick calculations.

## Usage
### Manual
Clone the repo in a folder using
``` sh
git clone https://github.com/Froloket64/qtcounter.git
cd qtcounter/
```
And create a **python** file in there.

The usage is as easy as:
``` py
from problem_gen import problem_gen

print(problem_gen(
    100,                # The max possible number (except results for now)
    3,                  # The amount of numbers in the problem
))
```
This will print a tuple of 2 items:
+ A string representation of the problem
+ The result

Use indexes like `problem_gen(...)[0]` to only take one of them.

Optional args include (only-keyword):
`do_round`   --  Round the results (0.4 -> 0, 0.5 -> 1)
`allow_null` --  Allow nulls as operands

## TODOs
The plans are on making a GUI frontend using PyQt. That's basically the whole point of the project ;)

## PS
This is a school project I'm doing with my friends (or at least started like that).
