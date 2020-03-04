#!/usr/bin/env python

def craq(mot):
    mot = list(mot)
    mot[0] = mot[0].swapcase()
    return ''.join(mot) + "!"

