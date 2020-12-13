# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:12:05 2020

@author: Avit_
"""
'''
Python 2 - DAT 129

Week 1: 09/02/2020
Module 1: Icon Manipulation

Assignment: Create a program in Python that uses looping
and Basic Data Structures to display customized 10x10 Student
icons in various scales and orientations...

Output: Display Binary sequences along with Icons

Steps:
    
    1) Create decimal Number and convert into Binary
    2) Generate sequences of Binar numbers: it's going to take
    the n_bits defaulted to 8 ( length of the Binary )
    3) Use Modulo and floor division to generate Zeros and Ones
    4) Create an empty Array aka list: to containt all the bits generated
    5) Create a dictionary: (easier when indexing)
    6) print Binary sequences along with Icons


'''

# This function converts Decimal number into binary
def generate_binary(index, n_bits = 8):
    binary_array = []# Our empty array assigned to its Binding
    num = index 
    # Loopping through the List
    for i in range(n_bits):
        #Modulo Op, for all even numbers 
        bit = num % 2 
        binary_array.append(bit)
        # Floor Division for odd numbers
        num = num//2
    return binary_array[::-1] # Returning the reversed List

def displaying_icon(n_bits = 8):
    binary_dict = {}
    for i in range (2**n_bits):
        binary_dict[i] = generate_binary(i, n_bits)
    return binary_dict

for index, binary_dict in displaying_icon(n_bits = 6).items():
    print(f'{binary_dict}: {"|" * index}')
    
def main():
    generate_binary(index, n_bits = 8)
    displaying_icon(n_bits = 8)

if __name__ == "__main__":
    main()

    