# -*- coding: utf-8 -*-
"""
Created on Tue May 05 01:01:43 2015

timus OJ 1001

@author: Galanodel
"""

from sys import stdin
from math import sqrt

numbers = []
for lines in stdin:
    for words in lines.split():
        if words.isalnum():
            numbers.append(float(words))

while len(numbers) > 0:
    print '%.4f' %sqrt(numbers.pop())