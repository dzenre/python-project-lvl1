"""Brain even game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def find_greatest_divider(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    gcd = num1 + num2
    return gcd


def find_gcd():
    player = welcome_user()
    print('Find the greatest common divider of given numbers.')  # noqa: WPS421
    wins_count = 0
    while wins_count < 3:
        randnum1 = randint(1, 100)
        randnum2 = randint(1, 100)
        gcd = find_greatest_divider(randnum1, randnum2)
        guess = prompt.string(
            'Question: {} {} \n'.format(  # noqa: P101
                randnum1,
                randnum2,
            ),
        )
        if guess == str(gcd):
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        else:
            print(  # noqa: WPS421
                '"{}" is a wrong! Correct answer was "{}"'.  # noqa: P101
                format(guess, gcd),
                )
            print("Let's try again, {}!".format(player))  # noqa: WPS421, P101
            wins_count = 0
    print('Congratulations, {}!'.format(player))  # noqa: WPS421, P101
