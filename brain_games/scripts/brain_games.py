#!/usr/bin/env python3
"""Main function."""
from brain_games.cli import welcome_user


def main():
    """Enter user name for a greeting."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    welcome_user()


if __name__ == '__main__':
    main()
