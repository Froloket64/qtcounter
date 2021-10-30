###  This is a backend part of problem generator  ###
###  used in this project.                        ###

## TODO:
## + Add negative numbers support
## + Check for all possible errors (like division by zero)

## NOTEs
## ...

from random import randint, choice


def problem_gen(limit: int, difficulty: int, *, do_round: bool = False, allow_null: bool = True):
    def actual_gen(a: str, times_left=difficulty, limit=limit):
        b = randint(int(allow_null), limit)
        sign = choice(('+', '-', '*', '/'))
        priority_a = randint(0, 1)

        if str(eval(a)) == a:
            priority_a = 0
        elif sign in ('+', '-'):
            priority_a = 0


        a = f"{'(' * priority_a}{a}{')' * priority_a}"

        problem = f"{a} {sign} {b}"

        times_left -= 1
        if times_left:
            problem = actual_gen(problem, times_left)

        return problem


    init_a = str( randint(int(allow_null), limit) )

    problem = actual_gen(init_a, 3)
    solution = eval(problem)

    if do_round:
        solution = round(solution + 0.01)

    return problem.replace('*', '×').replace('/', '÷'), solution
