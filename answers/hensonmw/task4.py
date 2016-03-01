#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This has been edited by Michael Henson for Assignment 9 task4

(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
"""


def function1(l):
    '''
When working with del, this act on the list as something that is passed on.
In other words, using del causes the manipulation to be global rather then
local. What this does is remove anything between the 3rd and 5th postion in the
list and brings itback to the main loop.
    '''
    del l[3:5]


def function2(l):
    '''
Here we are now locally editing "l" and removing "a" from the list. Because we
do not return or print this output we have not modified "my_list" that we
had imported. Therefore, in the main() function we are only calling the edited
version from function1().
    '''
    l = l[1:]
    #print(l)

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
