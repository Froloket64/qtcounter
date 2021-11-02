###  This is a backend part of problem generator  ###
###  used in this project.                        ###

## TODO:
## + Add negative numbers support
## + Check for all possible errors (like division by zero)
## + Make random a/b flips

## NOTEs
## ...

from random import randint, choice


def problem_gen(limit: int, difficulty: int, operations = ('+', '-', '*', '/'), *, do_round: bool = False, allow_null: bool = True):
    '''
    `a` - left operand
    `b` - right operand
    '''
    def actual_gen(a: str, times_left=difficulty - 1, limit=limit):  ## "difficulty - 1" because it does `difficulty` + 1 iterations
        '''
        `a` - left operand
        `times_left` - actually amount of operands left to generate
        `limit` - maximum possible number
        '''
        print(times_left)
        b = randint(int(allow_null), limit)  ## Gen `b` (right operand)
        sign = choice(operations)  ## Pick a random sign between `a` and `b`
        priority_a = randint(0, 1)  ## Parentheses around `a` (priority)

        if str(eval(a)) == a:  ## Basically, if `a` is a single digit...
            priority_a = 0  ## don't ever put parentheses around it
        #  elif sign in ('+', '-'):
            #  priority_a = 0


        a = f"{'(' * priority_a}{a}{')' * priority_a}"  ## Wrap parentheses around `a` if `priority_a` is 1

        problem = f"{a} {sign} {b}"  ## Concat all together

        times_left -= 1
        if times_left:  ## If there are operands to gen left...
            problem = actual_gen(problem, times_left)  ## RECURSION!

        return problem


    init_a = str( randint(int(allow_null), limit) )  ## Gen initial `a`

    problem = actual_gen(init_a, difficulty)  ## Call our inner function to generate the problem
    solution = eval(problem)  ## Evaluate the string representing the problem, and get its solution

    if do_round:  ## If `do_round` is True...
        solution = round(solution + 0.01)  ## Round the solution (little trick: round 0.5 to 1, but 0.4 to 0)

    return problem.replace('*', '×').replace('/', '÷'), solution  ## Replace "*" and "/" with unicode chars and return it all!
