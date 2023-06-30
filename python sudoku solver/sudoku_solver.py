import move_check
import puzzle_printer
array=eval(input("enter the puzzle:"))
puzzleprint(array)
"""using the backtracking algorithm to solve the puzzle"""
def findval(array):
    for row in array:
        for column in row:
            if num==0:
                for val in range(1,10):
                    if  check(row,column):
                        array[row,column]=val
                        findval(array)
                        array[row,column]=0
                return
puzzleprint(array)
