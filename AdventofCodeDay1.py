#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:33:53 2020

@author: matthewayala
"""
from itertools import combinations

expenses = input()
expenses = expenses.split('\n')

# Part 1
i = list(combinations(expenses,2))

for pair in i:
    if(int(pair[0]) + int(pair[1])) == 2020:
        print('Part 1 Solution:', int(pair[0]) * int(pair[1]))

# Part 2
t = list(combinations(expenses,3))


for triplet in t:
    if(int(triplet[0]) + int(triplet[1]) + int(triplet[2])) == 2020:
        print('Part 2 Solution:', int(triplet[0]) * int(triplet[1]) *int(triplet[2]))

