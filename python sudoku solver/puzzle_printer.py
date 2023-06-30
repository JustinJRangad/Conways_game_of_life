"""puzzle printer"""
def puzzleprint(array):
    for row in range(0, 9):
        if row%3==0 :
            for i in range(0,12):
                print(' -',end='')
            print()
        for column in range(0, 9):
            if column % 3 == 0 :
                print("|", end=' ')
                print(array[row][column], end=' ')
            else:
                print(str(array[row][column]), end=' ')
            if column==8:
                print("|", end=' ')
        print()
        if row==8:
            for i in range(0,12):
                print(' -',end='')
            print()

