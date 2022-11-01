#there's about a 1/25 chance for the programm to freeze after you hit solve
#most of the time the puzzle will sovle almost instanly but could take a couple seconds
from tkinter import *
from sudokuSolver import solve
from sudokuMaker import makePuzzel
from sudokuChecker import checkBoard
#global vars
sectionsNums = []
for i in range(9):
    sectionsNums.append([])
    for n in range(3):
        sectionsNums[i].append([" "," "," "])
sectionsBtns = []
currentCoord="000"
numberOfFilledSquares = 17
#create root
root = Tk()
root.title("sudoku")
root.config(background="purple")

#string vars
section = StringVar()
row = StringVar()
col = StringVar()
out = StringVar()

#functions

#when you click on a sudoku square it sets the new cords
def setNewCord(cord):
    global currentCoord
    currentCoord=cord
    section.set(f"Section: {int(currentCoord[0])+1}")
    row.set(f"Row: {round(int(currentCoord[1])+(int(currentCoord[0])-int(currentCoord[0])%3))+1}")
    col.set(f"Column: {int(currentCoord[2])+(int(currentCoord[0])%3)*3+1}")
    out.set("")

#sets number in current square when you click on a num button    
def setNum(num):
    global currentCoord
    global sectionsBtns
    global sectionsNums
    global out
    spot = sectionsBtns[int(currentCoord[0])][int(currentCoord[1])][int(currentCoord[2])]
    if spot.changable:
        spot.config(text=num)
        sectionsNums[int(currentCoord[0])][int(currentCoord[1])][int(currentCoord[2])] = num
        out.set("")
    else:
        out.set("sorry you can't chang ethat square")
    
#sets all the sudoku buttons to the corrisponding values in the section list
def setAllNums():
    global sectionsNums
    global sectionsBtns
    for section in range(len(sectionsBtns)):
        for row in range(len(sectionsBtns[section])):
            for spot in range(len(sectionsBtns[section][row])):
                sectionsBtns[section][row][spot].config(text = sectionsNums[section][row][spot])
                if sectionsNums[section][row][spot].isdigit():
                    sectionsBtns[section][row][spot].config(bg = "Dark Grey")
                    sectionsBtns[section][row][spot].changable = False
                else:
                    sectionsBtns[section][row][spot].config(bg = "Grey")
                    sectionsBtns[section][row][spot].changable = True

#runs the puzzle through the solving alg
def solvePuzzle():
    global sectionsNums
    global out
    if checkBoard(convertBoardToSolve()):
        #copy's board to save data
        copyOboard = []
        for i in range(9):
            copyOboard.append([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
        for s in range(len(sectionsNums)):
            for r in range(len(sectionsNums[s])):
                for c in range(len(sectionsNums[s][r])):
                    copyOboard[s][r][c] = sectionsNums[s][r][c]
                    
        readListORows(solve(convertBoardToSolve()))    
        setAllNums()
        #if nopthing changed then there was no solution found
        if sectionsNums == copyOboard:
            out.set("sorry, no solution was found")
        else:
            out.set("Puzzle is solved :)")
    else:
        out.set("Puzzle is invalid :(")
        
#used to help change between the diffrent board formats
def secColCheck(c):
    if c in range(0,3):
        return 0
    elif c in range(3,6):
        return 1
    else:
        return 2

#converts sectionNums to a readiable format for the solver (a list of rows rather than a list of sections)
def convertBoardToSolve():
    global sectionsNums
    listORows=[]
    for _ in range(9):
        listORows.append([])
    for s in range(len(sectionsNums)):
        for r in range(len(sectionsNums[s])):
            for c in sectionsNums[s][r]:
                listORows[((s-s%3))+r].append(c)
    return listORows
       
#reformats the list of rows back to a list of sections
def readListORows(board):
    global sectionsNums
    for r in range(len(board)):
        for c in range(len(board[r])):
            if r in range(0,3):
                s=secColCheck(c)
            elif r in range(3,6):
                s=secColCheck(c)+3
            else:
                s=secColCheck(c)+6
            sectionsNums[s][r%3][c%3] = board[r][c]

#generates a new puzzle
def newPuzzle():
    global out
    global numberOfFilledSquares
    readListORows(makePuzzel(numberOfFilledSquares))
    setAllNums()
    out.set("have fun :)")
             
#makes the board blank
def clearBoard():
    global sectionsNums
    sectionsNums = []
    for i in range(9):
        sectionsNums.append([])
        for n in range(3):
            sectionsNums[i].append([" "," "," "])
    out.set("look at that clean board :)")
    setAllNums()

#checks the current board
def check():
    global sectionsNums
    global out
    notSolved = False
    done = False
    if checkBoard(convertBoardToSolve()):
        while not(notSolved or done):
            for sec in sectionsNums:
                for row in sec:
                    for char in row:
                        if char == " ":
                            notSolved = True
            done = True
        if notSolved:
            out.set("Looks good so far")
        else:
            out.set("Great work!")
    else:
        out.set("you messed up somewhere")
#boring stuff

#sudoku buttom board
sudokuFrame = Frame(root,height=30,width=60,bg="purple")
sudokuFrame.pack()
for i in range(9):
    sectionFrame = Frame(sudokuFrame,bd=3,height=10,width=20,bg="purple")
    if i<3:
        sectionFrame.grid(row=0, column=i%3)
    elif i<6:
        sectionFrame.grid(row=1, column=i%3)
    else:
        sectionFrame.grid(row=2, column=i%3)
    sectionsBtns.append([[],[],[]])
    for n in range(9):
        sudokuBTN = Button(sectionFrame,bd=5,width=6,height=3)
        if n<3:
            sudokuBTN.grid(row=0, column=n%3,padx=2,pady=2)
            sudokuBTN.cord = f"{i}0{n%3}"
            sudokuBTN.changable = True
            sudokuBTN.config(command= lambda cord = sudokuBTN.cord: setNewCord(cord))
            sectionsBtns[i][0].append(sudokuBTN)
        elif n<6:
            sudokuBTN.grid(row=1, column=n%3,padx=2,pady=2)
            sudokuBTN.cord = f"{i}1{n%3}"
            sudokuBTN.changable = True
            sudokuBTN.config(command= lambda cord = sudokuBTN.cord: setNewCord(cord))
            sectionsBtns[i][1].append(sudokuBTN)
        else:
            sudokuBTN.grid(row=2, column=n%3,padx=2,pady=2)
            sudokuBTN.cord = f"{i}2{n%3}"
            sudokuBTN.changable = True
            sudokuBTN.config(command= lambda cord = sudokuBTN.cord: setNewCord(cord))
            sectionsBtns[i][2].append(sudokuBTN)

#coord system lables
coordFrame = Frame(root,height=3,width=60,bg="purple")
coordFrame.pack()
secLable = Label(coordFrame,height=2,width=20,textvariable= section,fg="white",bg="purple").grid(row=0,column=0)
rowLable = Label(coordFrame,height=2,width=20,textvariable= row,fg="white",bg="purple").grid(row=0,column=1)
colLable = Label(coordFrame,height=2,width=20,textvariable= col,fg="white",bg="purple").grid(row=0,column=2)

#number button board
numFrame = Frame(root,height=3,width=60,bg="purple")
numFrame.pack()
for i in range(1,11):
    if i != 10:
        numBtn =Button(numFrame,bd=5,width=5,height=3,text=str(i))
        numBtn.text = str(i)
    else:
        numBtn =Button(numFrame,bd=5,width=5,height=3,text="")
        numBtn.text = " "
        numBtn.changable = True
    numBtn.config(command= lambda num = numBtn.text:setNum(num))
    numBtn.grid(row=0,column=i-1,padx=2,pady=2)

for s in range(len(sectionsBtns)):
    for r in range(len(sectionsBtns[s])):
        for c in range(len(sectionsBtns[s][r])):
            sectionsBtns[s][r][c].config(text=sectionsNums[s][r][c])

outFrame = Frame(root,height=3,width=60,bg = "purple")
outFrame.pack()
outDisplay = Label(bg = "purple",textvariable= out,justify = "center")
outDisplay.pack()

checkFrame = Frame(root,height=3,width=60,bg = "purple")
checkFrame.pack()
checkBtn = Button(checkFrame,bd=5,width=11,height=5,text="Check", command = check)
checkBtn.grid(row = 0,column= 0,padx=10)
solveBtn = Button(checkFrame,bd=5,width=11,height=5,text="Solve", command = solvePuzzle)
solveBtn.grid(row = 0,column= 1,padx=10)
genBtn = Button(checkFrame,bd=5,width=11,height=5,text="New Puzzle", command = newPuzzle)
genBtn.grid(row = 0,column= 2,padx=10)
clearBtn = Button(checkFrame,bd=5,width=11,height=5,text="Clear", command = clearBoard)
clearBtn.grid(row = 0,column= 3,padx=10)
root.mainloop()