"""Brain is number prime game."""
from random import randint


def is_prime():
    """Check if random number is prime and return correct answer and question.

    Returns:
        answer : right answer for task
        question : generated question for task
    """
    count = 0
    randnum = randint(1, 100)
    question = '{0}'.format(randnum)
    for index in range(1, randnum + 1):
        if randnum % index == 0:
            count += 1
    if count > 2:
        answer = 'no'
    else:
        answer = 'yes'
    return answer, question


def task_prime():
    """Return task for the game.

    Returns:
        string : task for the game
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
