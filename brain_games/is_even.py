from random import randint
from brain_games.cli import welcome_user
import prompt


def is_even():
    player = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins_count = 0
    while wins_count < 3:
        random_number = randint(1, 1000)
        guess = prompt.string('Question: {}\n'.format(random_number))
        if (random_number % 2 == 0 and guess == 'yes') or (random_number % 2 != 0 and guess == 'no'):
            print('Correct!')
            wins_count += 1
        else:
            if guess == 'yes':
                print(
                    '"{}" is a wrong answer! Correct answer was "no"'.format(guess)
                    )
                print("Let's try again, {}!".format(player))
                wins_count = 0
            elif guess == 'no':
                print(
                    '"{}" is a wrong answer! Correct answer was "yes"'.format(guess)
                    )
                print("Let's try again, {}!".format(player))
                wins_count = 0
            else:
                print(
                    '"{}" is a wrong answer! Check answer format'.format(guess)
                    )
                print("Let's try again, {}!".format(player))
                wins_count = 0
    print('Congratulations, {}!'.format(player))
