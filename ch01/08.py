#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(sysin):
    s = ""
    for c in sysin:
        if c.islower():
            s += str(219 - ord(c))
        else:
            s += c
    return s

def decrypt(sysin):
    s = ""
    count = 2
    for i in range(len(sysin)):
        if sysin[i].isdigit() and count == 2:
            s += chr(219-int(sysin[i:i+3]))
            count -= 1
        elif sysin[i].isdigit() and count != 2:
            if count == 0:
                count = 2
            else:
                count -= 1
        else:
            s += sysin[i]
    return s

sentence = "TestCase"
ci = cipher(sentence)
print decrypt(ci)
