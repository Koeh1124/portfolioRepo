#add blacklist board to show where we have dead ends
from sudokuChecker import spotCheck
import random
def makePuzzle():
    psBoard, workingBoard, blackBoard = [], [], []
    for _ in range(9):
        psBoard.append([])
        workingBoard.append([])
        blackBoard.append([])
        for i in range(9):
            psBoard[-1].append([str(n) for n in range(1,10)])
            workingBoard[-1].append(" ")
            blackBoard[-1].append([])
    back = False
    r = 0
    c = 0
    while r!= 8 or c!= 8:
        if c == 9:
            c = 0
            r+= 1
        if back and psBoard[r][c] == []:
            workingBoard[r][c] = " "
            blackBoard[r][c] = []
            psBoard = [str(i) for i in range(1,10)]
            if c == 0:
                c = 8
                r-=1
            else:
                c-=1
        else:
      #print("running")
            if back:
                back = False
                while (not(spotCheck(workingBoard,r,c)) and len(psBoard[r][c]) != 0) or workingBoard[r][c] in blackBoard[r][c]:
                    print(len(psBoard[r][c]),workingBoard[r][c],blackBoard[r][c])
                    if not(len(psBoard[r][c]) == 0):
                        print(len(psBoard[r][c]))
                        workingBoard[r][c] = psBoard[r][c].pop(random.randrange(len(psBoard[r][c])))
                    else:
                        workingBoard[r][c] = " "
                blackBoard[r][c].append(workingBoard[r][c])
                if spotCheck(workingBoard,r,c):
                    c+=1
                    if c == 9:
                        c = 0
                        r+=1
                else:
                    print("going back")
                    for row in workingBoard:
                        print(row)
                        print("\n"*2,r,c,psBoard[r][c],psBoard[r][c-1])
                    workingBoard[r][c] = " "
                    blackBoard[r][c] = []
                    if c == 0:
                        c = 8
                        r-=1
                    else:
                        c-=1
    for check in  range(1,10):
        if not(str(check) in workingBoard[8]):
            workingBoard[8][8] = str(check)
    return workingBoard

print(makePuzzle())