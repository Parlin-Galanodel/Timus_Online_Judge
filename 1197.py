# -*- coding: utf-8 -*-
"""
Created on Wed May 06 10:24:52 2015

timus OJ 1197

@author: Galanodel
"""

from sys import stdin

inputdata = [line for line in stdin]

N, l = int(inputdata[0]), tuple(inputdata[1:])
del inputdata

dr = (2, 2, -2, -2, 1, 1, -1, -1)
dc = (1, -1, 1, -1, 2, -2, 2, -2)

def attacked(p):
    count = 0
    for i in xrange(8):
        x = ord(p[0]) + dr[i]
        y = int(p[1]) + dc[i]
        if (ord('a') <= x <= ord('h')) and \
           (1 <= y <= 8):
               count += 1
    return count
    
    
for i in xrange(N):
    print attacked(l[i])