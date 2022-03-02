# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:16:16 2022

@author: Coding
"""
from matplotlib import pyplot as plt
from scipy import linalg
import numpy as np
i = 0.0
Y1 = np.array([])
Y2 = np.array([])
while(i<5.1):
    rA = np.matrix([[6,3,4],[3,6,3],[4,3,6]])
    A = np.matrix([[6+i,3,4],[3,6+i,3],[4,3,6+i]])
    c = np.matrix([[9],[6],[8]])
    b = linalg.solve(A,c)
    print(b.T)
    temp = np.matmul(rA,b)-c
    y1 = np.dot(temp.T, temp)
    y2 = np.dot(b.T,b)
    Y1 = np.append(Y1,y1)
    Y2 = np.append(Y2,y2)
    i=i+0.2
X = np.array(range(26))
X = X/5
plt.title("Graph with regulation parameterA") 
plt.xlabel("Regulation parameter") 
plt.ylabel("||Ab-c||^2 and ||b||^2") 
plt.plot(X,Y1)
plt.plot(X,Y2)
plt.show()