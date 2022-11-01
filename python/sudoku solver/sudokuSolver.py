from importlib.util import find_spec
from sudokuChecker import checkBoard, spotCheck
from findPS import makePSBoard
import time
#backtracking alg to solve the puzzle
def solve(board):
    startTime = time.time()
    #makes ps board to solve the puzzle faster (look at findPS.py file)
    PSBoard = makePSBoard(board)
    #makes copy of the origional board to save the original data
    workingBoard = []
    for i in range(9):
        workingBoard.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
    for r in range(len(board)):
        for c in range(len(board[r])):
            workingBoard[r][c] = board[r][c]

    #initiates vars
    #keeps track of the direction of the alg
    #False is moving left to right top to bottom
    #True is right to left bottom to top
    back = False
    
    #r is the row and c is collum for the index
    r = 0
    c = 0
    firstR = 0
    firstC = 0
    foundFirst = False
    timeOut = False
    #runs untill it reaches the final spot
    while (r!=8 or c !=8) and not(timeOut):
        #makes it so if the alg runs for more than 10 seconds it "times out" and returns the board that was imported
        if time.time()-startTime > 10:
            timeOut = True
        #makes sure that it dosen't get an index higher than the list
        if c == 9:
            c = 0
            r+=1
        #if the point is a string it itterates
        if isinstance(PSBoard[r][c],str):
            #if the programm is going back it moves back
            if back:
                if c == 0:
                    c = 8
                    r -= 1
                else:
                    c -= 1
            #otherwise it continues forward
            else:
                c += 1
        # if the spot is not a number
        else:
            #tells the program where the first itterable spot if for later checking
            if not(foundFirst):
                firstC = c
                firstR = r
                foundFirst = True
            #if it's going back and its the end of the ps list
            if back and workingBoard[r][c] == PSBoard[r][c][-1]:
                #makes the spot blank and continues back
                workingBoard[r][c] = " "
                #if we tried all that we could we return the board that was put in because ther is no solution
                if c == firstC and r == firstR:
                    return board
                #goes back through the list
                if c == 0:
                    c = 8
                    r -= 1
                else:
                    c -= 1
            #if therees more we can do in the spot
            else:
                #if were going bakc
                if back:
                    #makes the index the last index the square itterated through +1
                    i = PSBoard[r][c].index(workingBoard[r][c])+1
                    workingBoard[r][c] = " "
                #other wise we restert
                else:
                  i = 0
                #resets back since we've started itterating again
                back = False
                #wile we haven't found a solution or have ran out of things to itterate
                while not(spotCheck(workingBoard,r,c)) and i <= len(PSBoard[r][c])-1:
                    #keep itterating through the spot and checking if it works
                    workingBoard[r][c] = PSBoard[r][c][i]
                    i += 1
                #if we found a solution
                if spotCheck(workingBoard,r,c):
                    #remove comments for visulisation
                    '''
                    for row in workingBoard:
                        print(row)
                    print("\n"*2)
                    time.sleep(.01)
                    '''
                    #continue to go through the puzzle
                    c += 1
                    if c == 9:
                        c = 0
                        r += 1
                #if we haven't found a solution
                else:
                    #makes spot blank
                    workingBoard[r][c] = " "
                    #tells the programe to go back
                    back = True
                    #starts going back
                    if c == 0:
                        c = 8
                        r -= 1
                    else:
                        c -= 1
    #if the last spot is blank
    if workingBoard[8][8] == " ":
        #loop tjhough 1-9 untill we find whats not in the row
        for check in range(1,10):
            if not(str(check) in workingBoard[8]):
                #make the last spot the correct num
                workingBoard[8][8] = str(check)
    #returns the puzzle
    if timeOut:
        return board
    
    return workingBoard