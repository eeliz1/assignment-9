#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
#Some of the modification made by Pramod Pantha on February 29.
"""


def function1(l):
    """
    This functionl is deleting index 3 and index 4 in my_list but not index 5.
    """
    del l[3:5]


def function2(l):
    """
    This function2 is printing exactly my_list but when functionl is running it
    gives a wrong output. This could be because there is no loop \ no return st
    taement in functionl
    """
    l = l[1:]


def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    function1(my_list)
    print("Here is output from function 1:")
    print(my_list)
    function2(my_list)
    print("Here is output from function 2:")
    print(my_list)


if __name__ == '__main__':
    main()
