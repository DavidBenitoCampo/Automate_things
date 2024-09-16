#!/usr/bin/env python3

import sys

num = int(input('Enter a number: '))

def collatz(number):
    if number % 2 == 0:
        print('{0} is Even number'.format(num))
    else:
        print('{0} is Odd number'.format(num))
     

collatz(num)