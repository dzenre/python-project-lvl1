"""Game engine."""
import prompt

from brain_games.calc import calc, task_calc
from brain_games.find_gcd import find_gcd, task_gcd
from brain_games.is_prime import is_prime, task_prime
from brain_games.is_even import is_even, task_even
from brain_games.generate_progression import make_string, task_progression

WINS_TO_WIN = 3  # number of continuous wins needed to finish a game


def welcome_user():
    """Ask player's name.

    Returns:
        name : player's name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def answer_question_task(game):
    """Get game name for switch.

    Args:
        game : game name

    Returns:
        answer : correct answer
        guess : player's guess
        task: task for the game
    """
    if game == 'calc':
        answer, question = calc()  # noqa: WPS204
        task_message = task_calc()
    if game == 'find_gcd':
        answer, question = find_gcd()
        task_message = task_gcd()
    if game == 'is_prime':
        answer, question = is_prime()
        task_message = task_prime()
    if game == 'is_even':
        answer, question = is_even()
        task_message = task_even()
    if game == 'generate_progression':
        answer, question = make_string()
        task_message = task_progression()
    return answer, question, task_message


def main_flow(game):
    """Process main game functions.

    Args:
        game : game name to run
    """
    wins_count = 0
    player = welcome_user()
    print(answer_question_task(game)[2])
    while wins_count < WINS_TO_WIN:
        answer, question = answer_question_task(game)[:2]
        guess = prompt.string('Question: {0}\n'.format(question))
        if guess == str(answer):
            print('Correct!')
            wins_count += 1
        else:
            print(
                '"{0}" is a wrong! Correct answer was "{1}"'.
                format(guess, answer),
            )
            print("Let's try again, {0}!".format(player))
            wins_count = 0
    print('Congratulations, {0}!'.format(player))
