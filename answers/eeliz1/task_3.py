#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 9

Task 3

Prints odd numbers of user-entered list of integers

Elisa Elizondo
"""

import argparse

def odds(x):
    for i in x:
        if i % 2 !=0:
            x.remove(i)
    return x

def input():
    parser = argparse.ArgumentParser()
    parser.add_argument("list1", help="Enter list of integers 0-10 with a space in between them", type=int, nargs="+")
    args = parser.parse_args()
    return args.list1

def main():
    x = input()
    print(odds(x))

if __name__ == '__main__':
    main()
