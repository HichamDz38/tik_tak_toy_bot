#!/bin/python3

import math
import os
import random
import re
import sys

def best_move(M,P,T):
    #print(M,P,T)
    for i in M:
        if i[0]==i[1]==i[2] and i[0]!='_':
            if i[0]!=P:
                return False
    for i in range(3):
        if M[0][i]==M[1][i]==M[2][i] and M[0][i]!='_':
            if M[0][i]!=P:
                return False
    if M[0][0]==M[1][1]==M[2][2] and M[0][0]!='_':
        if M[0][0]!=P:
            return False
    if M[2][0]==M[1][1]==M[0][2] and M[2][0]!='_':
        if M[2][0]!=P:
            return False
    for i in range(3):
        for j in range(3):
            if M[i][j]=='_':
                MP=[m for m in M]
                MP[i][j]=T
                if T=='X':
                    T='0'
                else:
                    T='X'
                D=best_move(MP,P,T)
                if D:
                    return (i,j)
    return True


if __name__ == '__main__':
    M=[]
    p = input() # player
    for i in range(3):
        M+=[[i for i in '.'.join(input()).split('.')]]
    x,y=best_move(M,p,p)
    print(x,y)
