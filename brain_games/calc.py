from random import randint, choice
from brain_games.cli import welcome_user
import prompt


def calc():
    player = welcome_user()
    print('What is the result of the expression?')
    wins_count = 0
    while wins_count < 3:
        random_number_1 = randint(1, 100)
        random_number_2 = randint(1, 100)
        operation = choice('+-*')
        guess = prompt.string('Question: {} {} {}\n'.format(random_number_1, operation, random_number_2))
        if operation == '+':
            result = random_number_1 + random_number_2
        elif operation == '-':
            result = random_number_1 - random_number_2
        elif operation == '*':
            result = random_number_1 * random_number_2
        if guess == str(result):
            print('Correct!')
            wins_count += 1
        else:
            print(
                '"{}" is a wrong answer! Correct answer was "{}"'.format(guess, result)
                )
            print("Let's try again, {}!".format(player))
            wins_count = 0
    print('Congratulations, {}!'.format(player))
