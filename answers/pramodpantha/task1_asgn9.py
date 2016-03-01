#!/usr/bin/env python
# utf-8

"""
Assignment 9,task1
Created by Pramod Pantha on 29 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


def upper(arg):
    # to capitalize every letter in the given quote
    u = arg.upper()
    return u


def lower(arg):
    # to make lowercase for every given alphabate in the quote
    l = arg.lower()
    return l


def count(arg):
    # to count numbers of letter in the given quote
    c = arg.count('e')
    return c


def split(arg):
    # splits quote in its character
    s = arg.split(' ')
    return s


def strip(arg):
    # helps to remove the unnecessary character from the quote
    t = arg.strip('@').strip(' ').strip('!')
    return t


def main():
    arg = "Python is interesting to learn, although it is not easy !!! @@@"
    a = upper(arg)
    print("upper method: ", a)
    b = lower(arg)
    print('lower method: ', b)
    c = count(arg)
    print('count method: ', c)
    d = split(arg)
    print('split method: ', d)
    e = strip(arg)
    print('strip method: ', e)


if __name__ == '__main__':
    main()
