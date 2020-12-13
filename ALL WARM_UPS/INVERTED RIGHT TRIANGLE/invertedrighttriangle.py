# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:01:23 2020

@author: Avit_
"""
print("Welcome to the Inverted Rigth Triangle ")

print('*************')
row_input = int(input('Enter The Number of rows: '))

def display_integer_pattern():
#Nested Loop!
    for i in range (row_input):
        for j in range (row_input-i):
            print(j + 0, end="")
        print()
# Calling the Function
display_integer_pattern()