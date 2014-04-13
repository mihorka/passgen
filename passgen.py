#! /usr/bin/python
#
#   Passgen
#
#   Copyright 2013, Michael Horka
#
#   The copyright holder(s) do not sell this software or your copy of it,
#   but merely license it. This particular software is however provided
#   free of charge.
#
#   Permission is hereby granted by the copyright holder(s) of this
#   software, to any person who obtains a copy to study the source code
#   without modifying or copying it in whole or in part and to run the
#   binary program. Redistribution of this software in source and/or binary
#   form is hereby prohibited.
#
#   THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY.
#   IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DAMAGES WHATSOEVER OR
#   PERFORMANCE OF THIS SOFTWARE.
#

import argparse
import random
import string


def random_int():
    return random.choice(string.digits)


def generate_password(diff):
    special = '!@#$%&()[]?'
    charset = list(string.ascii_letters + string.digits + special)

    if diff == 'weak':
        with open('easywordlist.txt') as ewl:
            charset = ewl.read().split()
        word = random.choice(charset)
        return word + random_int() + random_int()
    elif diff == 'medium':
        return ''.join(random.sample(charset, 6))
    elif diff == 'hard':
        return ''.join(random.sample(charset, 10))
    elif diff == 'extreme':
        charset += special * 2
        return ''.join(random.sample(charset, 16))


def main():
    parser = argparse.ArgumentParser(description='Take in a difficulty')
    parser.add_argument('-d', '--difficulty',
        help='Enter a difficulty (weak, medium, hard, extreme)')
    args = parser.parse_args()

    diff_values = ['weak', 'medium', 'hard', 'extreme']
    diff = 'medium'
    if args.difficulty:
        diff = args.difficulty
    if diff in diff_values:
        password = generate_password(diff)
        print(password)
    else:
        print('Invalid difficulty, use weak, medium, hard or extreme')

if __name__ == "__main__":
    main()