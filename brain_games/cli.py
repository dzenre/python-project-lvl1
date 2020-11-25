"""Module to ask player's name."""
import prompt


def welcome_user():
    """Ask player's name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))  # noqa: WPS421 P101
    return name
