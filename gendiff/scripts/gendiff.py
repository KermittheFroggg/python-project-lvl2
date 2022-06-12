#!/usr/bin/env python

from gendiff.generate_diff import generate_diff
from gendiff.parsing import parsing


def main():
    args = parsing()
    print(args)
    print(generate_diff(
        args['first_file'], args['second_file'],
        format=args['format']))


if __name__ == '__main__':
    main()
