"""Brain calc game."""
from random import randint, choice   # noqa: I001

import prompt

from brain_games.cli import welcome_user


def generate_rand_expression():
    """Generate random expression and ask for guess.

    Returns:
        answer : right answer
        guess: user's answer
    """
    randnum1 = randint(1, 100)  # noqa: S311
    randnum2 = randint(1, 100)  # noqa: S311
    operator = choice('+-*')  # noqa: S311
    if operator == '+':
        answer = randnum1 + randnum2
    elif operator == '-':
        answer = randnum1 - randnum2
    elif operator == '*':
        answer = randnum1 * randnum2
    guess = prompt.string(
        'Question: {0} {1} {2}\n'.format(
            randnum1,
            operator,
            randnum2,
            ),
        )
    return answer, guess


def calc():
    """Ask player to calculate the answer."""
    player = welcome_user()
    print('What is the result of the expression?')  # noqa: WPS421
    wins_count = 0
    while wins_count < 3:
        answer, guess = generate_rand_expression()
        if guess == str(answer):
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        else:
            print(  # noqa: WPS421
                '"{0}" is a wrong! Correct answer was "{1}"'.
                format(guess, answer),
                )
            print("Let's try again, {}!".format(player))  # noqa: WPS421, P101
            wins_count = 0
    print('Congratulations, {}!'.format(player))  # noqa: WPS421, P101
