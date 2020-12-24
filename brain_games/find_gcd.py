"""Brain even game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def find_greatest_divider(num1, num2):
    """Check if random number is even.

    Args:
        num1 : number to check.
        num2 : number to check.

    Returns:
        gcd : greatest common divider
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2


def find_gcd():  # noqa: WPS210
    """Ask the player for the answer."""
    player = welcome_user()
    print('Find the greatest common divider of given numbers.')  # noqa: WPS421
    wins_count = 0
    while wins_count < 3:
        randnum1 = randint(1, 100)  # noqa: S311
        randnum2 = randint(1, 100)  # noqa: S311
        gcd = find_greatest_divider(randnum1, randnum2)
        guess = prompt.string(
            'Question: {0} {1} \n'.format(
                randnum1,
                randnum2,
            ),
        )
        if guess == str(gcd):
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        else:
            print(  # noqa: WPS421
                '"{0}" is a wrong! Correct answer was "{1}"'.
                format(guess, gcd),
                )
            print("Let's try again, {0}!".format(player))  # noqa: WPS421
            wins_count = 0
    print('Congratulations, {0}!'.format(player))  # noqa: WPS421
