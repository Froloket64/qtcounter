###  This is a backend part of problem generator  ###
###  used in this project.                        ###

## TODO:
## + Check for all possible errors (like division by zero)
## + Make random a/b flips to make parentheses (look) more ~random~
## + Make all possible optimizations

## NOTEs
## ...

from random import randint, choice


def problem_gen(limit: int, difficulty: int, operations = ('+', '-', '*', '/'), *, do_round: bool = False, allow_null: bool = True, allow_negative: bool = True):
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

        b = randint(int(allow_null), limit)  ## Gen `b` (right operand)
        sign = choice(operations)  ## Pick a random sign between `a` and `b`
        priority_a = randint(0, 1)  ## Randomly add parentheses around `a` (priority)
        if allow_negative:
            negative_b = randint(0, 1)  ## Randomly make `b` negative
        else:
            negative_b = 0


        ## Special case checks
        if str(eval(a)) == a:  ## Basically, if `a` is a single digit,
            priority_a = 0  ## don't ever put parentheses around it
        if b == 0 and sign in ('/', '//'):  ## Don't let 'em divide by zero!
            b = 1


        a = f"{'(' * priority_a}{a}{')' * priority_a}"  ## Wrap parentheses around `a` if `priority_a` is 1
        b = f"{'(-' * negative_b}{b}{')' * negative_b}"  ## ^ But if `b` is negative

        problem = f"{a} {sign} {b}"  ## Concat all together

        times_left -= 1
        if times_left:  ## If there are operands to gen left,
            problem = actual_gen(problem, times_left)  ## RECURSION!

        return problem


    init_a = str( randint(int(allow_null), limit) )  ## Gen initial `a`

    problem = actual_gen(init_a, difficulty)  ## Call our inner function to generate the problem
    solution = eval(problem)  ## Evaluate the string representing the problem, and get its solution

    if do_round:  ## If `do_round` is True,
        solution = round(solution + 0.01)  ## Round the solution (little trick: round 0.5 to 1, but 0.4 to 0)

    return problem.replace('*', '×').replace('/', '÷'), solution  ## Replace "*" and "/" with unicode chars and return it all!
