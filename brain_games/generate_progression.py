"""Brain progression game."""
from random import randint


def generate_progression():
    """Generate random linear progression.

    Returns:
        progression : list of generated numbers
    """
    common_dif = randint(1, 50)  # noqa: WPS432
    first_number = randint(0, 30)  # noqa: WPS432
    progression = []
    index = 0
    while index < randint(5, 10):
        progression.append(first_number + common_dif * index)
        index += 1
    return progression


def pick_answer():
    """Pick a random number for an answer and replace it with '..'.

    Returns:
        progression : list of generated numbers with replaced answer
        answer: random position number for right answer
    """
    progression = generate_progression()
    seed = randint(0, len(progression) - 1)
    answer = progression[seed]
    progression[seed] = '..'
    return progression, answer


def make_string():
    """Convert list of number to concatenated string.

    Return correct answer and question.

    Returns:
        answer : right answer for task
        question : generated question for task
    """
    progression, answer = pick_answer()
    list_of_numbers = ''
    for number in progression:  # noqa: WPS519
        list_of_numbers += '{0} '.format(number)
    question = '{0}'.format(list_of_numbers.rstrip())
    return answer, question


def task_progression():
    """Return task for the game.

    Returns:
        string : task for the game
    """
    return 'What number is missing in the progression?'
