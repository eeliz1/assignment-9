#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 9

Created by Michael Henson on 29 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.
"""


def caps(mystring):
	return mystring.upper()


def lowercase(mystring):
    	return mystring.lower()


def whereis(mystring):
    return mystring.find("experience")


def title(mystring):
	return mystring.title()


def is_lowercase(mystring):
        return mystring.islower()


def main():

	mystring = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."

    #first example
	print(caps(mystring))

    #second example
	print(lowercase(mystring))

    #third example
	print(whereis(mystring))

    #fourth example
	print(title(mystring))

    #fifth example
	print(is_lowercase(mystring))


if __name__ == '__main__':
    main()
