#checks to make sure there ar no duplicates in the list
#sorts the list then sees if the are any of the same numbers next to eachother
#[1,2,3,3,4,5, , , ] would be invalid
#[3,7,8,9, , , , , ] would be valid
def check(listOfSections):
    for l in listOfSections:
        l = sorted(l)
        for i in range(len(l)-1):
            if l[i] == l[i+1] and l[i].isdigit():
                return False
    return(True)

#function used to get section of point
def secColCheck(c):
  if c in range(0,3):
    return 0
  elif c in range(3,6):
    return 1
  else:
    return 2

#splist the board into lists of rows, collums, and sections and runs them through check
#if one of the checks returns False it returns False
#if all return True it returns True
def checkBoard(board):
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
    if check(listoRows) and check(listoCols) and check(listoSecs):
        return True
    else:
        return False
      
#dose the same as checkBoard, but only gets the neccary points to check one spot
def spotCheck(board,r,c):
  if board[r][c] == " ":
    return False
  rowList = board[r]
  colList = []
  secList = []
  for row in board:
    colList.append(row[c])
  secH = r - r%3
  secV = c - c%3
  for sr in range(secH,secH+3):
    for sc in range(secV,secV+3):
      secList.append(board[sr][sc])
  listsToCheck = [rowList,colList,secList]
  return(check(listsToCheck))