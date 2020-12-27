"""Brain is number even game."""
from random import randint


def is_even():
    """Check if random number is even and return correct answer and question.

    Returns:
        answer : right answer for task
        question : generated question for task
    """
    randnum = randint(1, 1000)
    question = '{0}'.format(randnum)
    if randnum % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer, question


def task_even():
    """Return task for the game.

    Returns:
        string : task for the game
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'
