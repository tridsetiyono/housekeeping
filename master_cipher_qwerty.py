# -*- coding: utf-8 -*-
"""
Master Cipher QWERTY version
Created on Tue Jul 27 12:48:49 2021

@author: Tri Deri Setiyono
"""

# leaf blank if not requiring these & record for each password these inputs
suffix_num = '1776'
suffix_specialchar = '#!'

#option for lower and upper case
alphanumtext = 'qwertyuiopASDFGHJKLzxcvbnm'

#option for lower case
#alphanumtext = 'qwertyuiopasdfghjklzxcvbnm'


def shift_amount(i):
    ''' Shift based on  the length of ref string '''
    return i%26

def encrypt(inputtext):
    required_shift = 10
    out_string = ''
    inputtext = inputtext.lower()
    for char in inputtext:
        if char not in alphanumtext:
            out_string = out_string + char
        else:
            alpha_index = alphanumtext.find(char)
            out_string = out_string + alphanumtext[shift_amount(alpha_index +required_shift)]
    return out_string

testresuts = encrypt(input('enter input text:')) + suffix_num + suffix_specialchar

print(testresuts);