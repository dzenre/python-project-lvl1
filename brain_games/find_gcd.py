"""Brain find greatest common divider game."""
from random import randint


def find_gcd():
    """Find greatest common divider of two random numbers.

    Return correct answer and question.

    Returns:
        answer : right answer for task
        question : generated question for task
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = '{0} {1}'.format(num1, num2)
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    answer = num1 + num2
    return answer, question


def task_gcd():
    """Return task for the game.

    Returns:
        string : task for the game
    """
    return 'Find the greatest common divider of given numbers.'
