"""Brain even game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count > 2:
        return 'no'
    return 'yes'


def check_prime():
    player = welcome_user()
    print(
        'Answer "yes" if given number is prime. Otherwise answer "no".'
        )  # noqa: WPS421
    wins_count = 0
    while wins_count < 3:
        randnum = randint(1, 100)
        guess = prompt.string('Question: {}\n'.format(randnum))  # noqa: P101
        answer = is_prime(randnum)
        if is_prime(randnum) and guess == answer:
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
