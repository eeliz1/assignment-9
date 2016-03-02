#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 9

Task 1

Demonstrates 5 string methods

Elisa Elizondo
"""

quote = "The most beautiful thing we can experience is the mysterious.  It is the source of all true art and science."

def method1(quote):
    quote1 = quote.split(' ')
    return quote1

def method2(quote):
    quote2 = quote.count("e")
    return quote2

def method3(quote):
    quote3 = quote.upper()
    return quote3

def method4(quote):
    quote4 = quote.find('t')
    return quote4

def method5(quote):
    quote5 = 'most' in quote
    return quote5


def main():
    print(method1(quote))
    print(method2(quote))
    print(method3(quote))
    print(method4(quote))
    print(method5(quote))

if __name__ == '__main__':
    main()
