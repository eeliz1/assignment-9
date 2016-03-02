#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 9

Task 4


Elisa Elizondo
"""


def function1(l):
    del l[3:5]
    """Unlike strings and tuples, lists are mutable objects and can therefore
    be altered.  This function changes the original list itself and once run,
    the new list will replace all subsequent calls for the orignal list."""

def function2(l):
    l = l[1:]
    ##return l
    """Function two is assigning the changes it makes to the variable l,
    which must be called from the main function to replace the original list.
    It isn't altering the original list itself, and won't replace that list
    until the variable l is returned to the main loop."""


def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    function1(my_list)
    print("Here is output from function 1:")
    print(my_list)
    function2(my_list)
    print("Here is output from function 2:")
    print(my_list)
    ##print("Test")
    ##print(function2(my_list))


if __name__ == '__main__':
    main()
