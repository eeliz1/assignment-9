#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 9

Created by Michael Henson on 29 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse


def user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
           '-list_of_numbers',
           nargs='+',
           type=int,
           help='Give the list of numbers from Brant'
       )
    args = parser.parse_args()
    return args.list_of_numbers
    # accepts user input and sends it  to main


def removing_odds(numbers):
    # this function uses iteration to find even numbers & remove them
    for x in numbers:
        if x % 2 == 0:
            numbers.remove(x)
    return numbers


def main():
    numbers = (user_input())
    odds = removing_odds(numbers)
    print(odds)

if __name__ == '__main__':
    main()
