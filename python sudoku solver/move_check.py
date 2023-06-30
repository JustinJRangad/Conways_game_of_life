"""functions to check legibility of a number in a position"""
import math
array=[]
def rowcheck(row,column):
    num=array[row][column]
    sublist=array[row]
    for nums in sublist:
        if nums==num:
            return False
    return True
def columncheck(row,column):
    num=array[row][column]
    for rows in range(0,9):
        if array[rows][column] == num:
            return False
    return True
def gridcheck(row,column):
    num=array[row][column]
    lowerC=(math.floor(column/3))*3
    upperC=lowerC+3
    lowerR=(math.floor(row/3))*3
    upperR=lowerC+3
    count=0
    for rows in range(lowerR,upperR):
        for clmns in range(lowerC,upperC):
           if array[rows][clmns]==num:
              count+=1
              if count>=2:
                 return False
    return True
def check(row,column):
    if rowcheck(row,column) and columncheck(row,column) and gridcheck(row,column):
        return True
    else:
        return False
