#!/usr/bin/env python
# utf-8

"""
Assignment 9,task3
Created by Pramod Pantha on 29 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import argparse


def paser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list_of_integers', nargs='+', help="enter a list of \
    integers", type=int)
    args = parser.parse_args()
    return args.list_of_integers


def onlyodd(my_list):
    for i in my_list:
        if i % 2 == 0:
            my_list.remove(i)
            return my_list


def main():
    my_list = paser()
    print(onlyodd(my_list))

if __name__ == '__main__':
    main()
