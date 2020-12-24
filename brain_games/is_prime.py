"""Brain even game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def is_prime(num):
    """Check if random number is prime.

    Args:
        num : number to check.

    Returns:
        string : 'yes' if number is prime, else 'no'
    """
    count = 0
    for index in range(1, num + 1):
        if num % index == 0:
            count += 1
    if count > 2:
        return 'no'
    return 'yes'


def check_prime():
    """Ask player for answer."""
    player = welcome_user()
    print(  # noqa: WPS421
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        )
    wins_count = 0
    while wins_count < 3:
        randnum = randint(1, 100)  # noqa: S311
        guess = prompt.string('Question: {0}\n'.format(randnum))
        answer = is_prime(randnum)
        if is_prime(randnum) and guess == answer:
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
