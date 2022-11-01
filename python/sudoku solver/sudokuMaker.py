import random
from sudokuChecker import spotCheck
from vaildBoard import validateBoard
#this will somtimes return an invaild puzzle
#generates vaild puzzle with a certin number of spot
def makePuzzel(numberOSpots):
    values = [i for i in range(1,10)]
    #makes new blank puzzle
    newPuzzle = []
    for i in range(9):
        newPuzzle.append([])
        for _ in range(9):
            newPuzzle[i].append(" ")
            
    #picks random spots untill it has fill the amount put into the function
    for _ in range(numberOSpots):
        r = random.randint(0,8)
        c = random.randint(0,8)
        #makes sure the the picked point is blank
        while newPuzzle[r][c].isdigit():
            r = random.randint(0,8)
            c = random.randint(0,8)
        #picks random number to put in the spot
        if values != []:
            newPuzzle[r][c]=str(random.choice(values))
        else:
            newPuzzle[r][c]=str(random.randint(1,9))
        #makes sure the the number dosen't make the puzzle invalid
        while not(spotCheck(newPuzzle,r,c)):
            if values != []:
                newPuzzle[r][c]=str(random.choice(values))
            else:
                newPuzzle[r][c]=str(random.randint(1,9))
        if int(newPuzzle[r][c]) in values:
            values.remove(int(newPuzzle[r][c]))
    if validateBoard(newPuzzle):
        return newPuzzle
    else:
        return makePuzzel(numberOSpots)