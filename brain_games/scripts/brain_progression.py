#!/usr/bin/env python3
"""Main function."""
from brain_games.generate_progression import check_progression


def main():
    """Enter user name for a greeting."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    check_progression()


if __name__ == '__main__':
    main()
