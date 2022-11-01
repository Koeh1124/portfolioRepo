using namespace std;
//allows me to print out rows
void printRow(int row[9]);
//returns bool if it is a vaild board
bool checkAll(int board[9][9]);
//reads the puzzle from a txt file
void readPuzzle(string puzzleName, int board[9][9]);
//copys a board
void copyBoard(int board1[9][9], int board2[9][9]);