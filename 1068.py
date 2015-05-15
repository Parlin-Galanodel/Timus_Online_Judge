# -*- coding: utf-8 -*-
"""
Created on Tue May 05 02:08:30 2015

timus OJ 1068

@author: Galanodel
"""

N = int(raw_input())
# use formular (N+1)*(1+abs(N-1))/2
print (N+1)*(abs(N-1)+1)/2