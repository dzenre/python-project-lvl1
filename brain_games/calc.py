"""Brain calculator game."""
from random import randint, choice


def calc():
    """Generate random expression and return correct answer and question.

    Returns:
        answer : right answer for task
        question : generated question for task
    """
    randnum1 = randint(1, 100)
    randnum2 = randint(1, 100)
    operator = choice('+-*')
    question = '{0} {1} {2}'.format(randnum1, operator, randnum2)
    if operator == '+':
        answer = randnum1 + randnum2
    elif operator == '-':
        answer = randnum1 - randnum2
    elif operator == '*':
        answer = randnum1 * randnum2
    return answer, question


def task_calc():
    """Return task for the game.

    Returns:
        string : task for the game
    """
    return 'What is the result of the expression?'
