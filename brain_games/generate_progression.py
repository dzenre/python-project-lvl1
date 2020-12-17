"""Brain progression game."""
from random import randint

import prompt

from brain_games.cli import welcome_user


def generate_progression():
    progression = []
    size = randint(5, 10)
    for i in range(randint(0, 30), randint(200, 1000), randint(1, 50)):
        progression.append(i)
        if len(progression) >= size:
            break
    return progression


def pick_answer():
    progression = generate_progression()
    seed = randint(0, len(progression) - 1)
    answer = progression[seed]
    progression[seed] = ".."
    return progression, answer


def make_string():
    progression, answer = pick_answer()
    list_of_numbers = ''
    for n in progression:
        list_of_numbers += '{} '.format(n)
    return list_of_numbers.rstrip(), answer


def check_progression():
    player = welcome_user()
    print(
        'What number is missing in the progression?'
        )  # noqa: WPS421
    wins_count = 0
    while wins_count < 3:
        progression, answer = make_string()
        guess = prompt.string('Question: {}\n'.format(progression))
        if guess == str(answer):
            print('Correct!')  # noqa: WPS421
            wins_count += 1
        else:
            print(  # noqa: WPS421
                '"{}" is a wrong! Correct answer was "{}"'.  # noqa: P101
                format(guess, answer),
                )
            print("Let's try again, {}!".format(player))  # noqa: WPS421, P101
            wins_count = 0        
    print('Congratulations, {}!'.format(player))
