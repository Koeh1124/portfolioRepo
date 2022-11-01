from findPS import makePSBoard
from sudokuChecker import secColCheck
#this file is used to reduce the amount of invalid puzzles generated
#makes all the bards and flattens all the lists to check if their vaild
def validateBoard(board):
    psBoard = makePSBoard(board)
    boards = splitBoard(psBoard)
    rows,cols,secs=boards[0],boards[1],boards[2]
    rows,cols,secs = flatten(rows),flatten(cols),flatten(secs)
    if checkIfValid(rows) and checkIfValid(cols) and checkIfValid(secs):
        return True
    return False

#check if 1-9 are in the flattened list
def checkIfValid(flattenedList):
    for row in flattenedList:
        for check in range(1,10):
            if not(str(check) in row):
                return False
    return True
    
#flattens the lists
#turns [[1,2,3],4,[5,6],7,[8,9]] to [1,2,3,4,5,6,7,8,9] but many more number of course
def flatten(listToFlatten):
    flattenedList = []
    for i in range(9):
        flattenedList.append([])
    for row in range(len(listToFlatten)):
        for item in listToFlatten[row]:
            if isinstance(item,str):
                flattenedList[row].append(item)
            else:
                for char in item:
                    flattenedList[row].append(char)
    return flattenedList

#splits the board into compnents(rows collums, sections)
def splitBoard(board):
    listoRows = board
    listoCols = []
    listoSecs = []
    for _ in range(9):
        listoCols.append([])
        listoSecs.append([])
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            listoCols[c].append(board[r][c])
            if r in range(0,3):
                s=secColCheck(c)
            elif r in range(3,6):
              s=secColCheck(c)+3
            else:
              s=secColCheck(c)+6
            #appends to correct section list
            listoSecs[s].append(board[r][c])
    return (listoRows,listoCols,listoSecs)