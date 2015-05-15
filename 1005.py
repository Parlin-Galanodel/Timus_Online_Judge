# -*- coding: utf-8 -*-
"""
Created on Wed May 06 00:45:00 2015

timus OJ 1005

@author: Galanodel
"""

from sys import stdin
from itertools import combinations
#import io
#
#string =  u'5\n5 8 13 27 14'
#stdin = io.StringIO(string)

n, l = (line for line in stdin)
n = int(n)
l = tuple(int(x) for x in l.split())

total = sum(l)

# sum(pile1)-sum(pile2) 
#  = sum(pile1) - (total - sum(pile1))
#  = 2*sum(pile1) - total
# abs(diff) is the difference 
# enumerate all the combinations and find the min number
# in each cycle which would be appended to dif list
count = 0
dif = []
while count <= n/2:
    dif.append(min(map(abs,map(lambda x: 2*x
    -total, map(sum, tuple(combinations(l,
    count)))))))
    count += 1
    
print min(dif)