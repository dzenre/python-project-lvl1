"""Brain even game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def is_even(num):
    """Check if number is even."""  # noqa: DAR101, DAR201
    if num % 2 == 0:
        answer = 'yes'
        return True, answer
    answer = 'no'
    return False, answer


def check_even():
    """Ask the player for the answer."""
    player = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')  # noqa: WPS421, E501
    wins_count = 0
    while wins_count < 3:
        randnum = randint(1, 1000)  # noqa: S311
        guess = prompt.string('Question: {}\n'.format(randnum))  # noqa: P101
        answer = is_even(randnum)[1]
        if is_even(randnum) and guess == answer:
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        elif not is_even(randnum) and guess == answer:
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        else:
            print(  # noqa: WPS421
                '"{}" is a wrong! Correct answer was "{}"'.  # noqa: P101
                format(guess, answer),
                )
            print("Let's try again, {}!".format(player))  # noqa: WPS421, P101
            wins_count = 0
    print('Congratulations, {}!'.format(player))  # noqa: WPS421, P101
