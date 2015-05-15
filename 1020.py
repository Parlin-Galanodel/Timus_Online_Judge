# -*- coding: utf-8 -*-
"""
Created on Wed May 06 14:44:29 2015

timus OJ 1020

@author: Galanodel
"""

from sys import stdin
from math import pi, sqrt

import io
u=u'4 1\n0.0 0.0\n2.0 0.0\n2.0 2.0\n0.0 2.0'
stdin=io.StringIO(u)

inputdata = [line for line in stdin]
N, r = (int(x) for x in inputdata[0].split())
print N, r
print inputdata
list1= tuple(string for string in inputdata[1:])
print list1
tuple1= tuple((x,y) for string in list1 for x,y in string.split())



inputdata = tuple((float(x), float(y)) for string in inputdata [1:] 
            for x,y in string.split())

l = 2*pi*r + sqrt((inputdata[0][0] - inputdata[-1][0])**2 + 
                  (inputdata[0][1] - inputdata[-1][1])**2)
                  
                  
for i in xrange(1,N):
    l += sqrt((inputdata[i][0] - inputdata[i-1][0])**2 
            + (inputdata[i][1] - inputdata[i-1][1])**2)
            
print '%.2f' %l