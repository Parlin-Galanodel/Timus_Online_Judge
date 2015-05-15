# -*- coding: utf-8 -*-
"""
Created on Tue May 05 04:23:28 2015

timus OJ 1083

@author: Galanodel
"""

n, k = raw_input().split(' ')
n, k = int(n), len(k)

def f(n, k):
    t = 1
    while n > k:
        t*=n
        n-=k
    return n*t

print f(n,k)
    