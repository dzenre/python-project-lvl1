#!/usr/bin/env python
"""Main function."""
from brain_games.cli import welcome_user


def main():
    """Enter user name for a greeting."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
