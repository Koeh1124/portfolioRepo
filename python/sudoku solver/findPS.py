#uses the list of intersections to find all poossible sulutions
def getPS(Intersections):
    listOPS = []
    #checks if 1-9 are in the list of intersections and returns all the ones the dont
    for check in range(1,10):
        if not(str(check) in Intersections):
            listOPS.append(str(check))
    return listOPS
  
#gets intersections for specific spot on the board
#intersections are all numbers the "intersect" the spot and if put in the spot would make the puzzle invalid
def getIntersections(board,r,c):
    listOIntersects = []
    for char in board[r]:
        listOIntersects.append(char)
    for row in board:
        listOIntersects.append(row[c])
    secH = r - r%3
    secV = c - c%3
    for sr in range(secH,secH+3):
        for sc in range(secV,secV+3):
            listOIntersects.append(board[sr][sc])
    return listOIntersects

#makes board whith all blank spots replaced with lists of the possible solutios for that spot
def makePSBoard(board):
    PSBoard = []
    for r in range(len(board)):
        PSBoard.append([])
        for c in range(len(board[r])):
            if board[r][c].isdigit():
                PSBoard[r].append(board[r][c])
            else:
                PSBoard[r].append(getPS(getIntersections(board,r,c)))
    return PSBoard