"""Brain progression game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def generate_progression(common_dif, first_number):
    """Generate random linear progression.

    Args:
        common_dif : common difference of progression
        first_number : first number of progression

    Returns:
        progression : list of generated numbers
    """
    progression = []
    progression.append(first_number)
    index = 0
    while index < randint(5, 10):  # noqa: S311
        progression.append(first_number + common_dif)
        index += 1
    return progression


def pick_answer():
    """Pick a random number for an answer and replace it with '..'.

    Returns:
        progression : list of generated numbers with replaced answer
        answer: random position number for right answer
    """
    progression = generate_progression(
        randint(1, 50), randint(0, 30),  # noqa: S311, WPS432
        )
    seed = randint(0, len(progression) - 1)  # noqa: S311
    answer = progression[seed]
    progression[seed] = '..'
    return progression, answer


def make_string():
    """Convert list of number to concatenated string.

    Returns:
        list_of_numbers.rstrip() : list of numbers as string
        answer: random position number for right answer
    """
    progression, answer = pick_answer()
    list_of_numbers = ''
    for number in progression:  # noqa: WPS519
        list_of_numbers += '{0} '.format(number)
    return list_of_numbers.rstrip(), answer


def check_progression():
    """Ask the player for the answer."""
    player = welcome_user()
    print(  # noqa: WPS421
        'What number is missing in the progression?',
        )  # noqa: WPS421
    wins_count = 0
    while wins_count < 3:
        progression, answer = make_string()
        guess = prompt.string('Question: {0}\n'.format(progression))
        if guess == str(answer):
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        else:
            print(  # noqa: WPS421
                '"{0}" is a wrong! Correct answer was "{1}"'.
                format(guess, answer),
                )
            print("Let's try again, {0}!".format(player))  # noqa: WPS421
            wins_count = 0
    print('Congratulations, {0}!'.format(player))  # noqa: WPS421
