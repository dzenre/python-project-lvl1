#!/usr/bin/env python3
"""Main function."""
from brain_games.is_prime import check_prime


def main():
    """Enter user name for a greeting."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    check_prime()


if __name__ == '__main__':
    main()
