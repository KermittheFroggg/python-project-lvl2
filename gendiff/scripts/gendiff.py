#!/usr/bin/env python

from gendiff.generate_diff import generate_diff
from gendiff.parsing import parsing


def main():
    args = parsing()
    print(generate_diff(
        args.__dict__['first_file'], args.__dict__['second_file'],
        format=args.__dict__['format']))


if __name__ == '__main__':
    main()
