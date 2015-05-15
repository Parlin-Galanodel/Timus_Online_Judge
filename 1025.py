# -*- coding: utf-8 -*-
"""
Created on Tue May 05 04:03:14 2015

@author: Galanodel
"""

from sys import stdin
K, l = (x for x in stdin)

K = int(K)/2 + 1
l = [int(x) for x in l.split()]

l.sort()

print (sum(l[:K]) + K) / 2
