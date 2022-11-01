#include <iostream>
#include <fstream> //let's us read a file in
using namespace std;
int asciiToInt(char i){
  return (0+(i-48));
}
void readPuzzle(string puzzleName, int board[9][9]){
  string x;
  ifstream inFile;
  inFile.open(puzzleName);
  //this reads in the lines
  int r = 0;
  while (inFile >> x) {
    for (int c = 0;c<x.length();c++){
      board[r][c]=asciiToInt(x[c]);
    }
    r++;
  }
}

void copyBoard(int board1[9][9], int board2[9][9]){
  for (int r=0;r<9;r++){
    for (int c=0;c<9;c++){
      board2[r][c] = board1[r][c];
    }
  }
}