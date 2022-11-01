#include <iostream>
#include "sudokuFunctions.h"
#include <chrono>
#include <cstdint>
//https://stackoverflow.com/questions/19555121/how-to-get-current-timestamp-in-milliseconds-since-1970-just-the-way-java-gets
uint64_t timeSinceEpochMillisec() {
  using namespace chrono;
  return duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
}

using namespace std;
/*
Planning
-----------------------
Puzzle formatted as 2d table 9*9
0 represents a blank space
*/
int main() {
  long int start;
  start = timeSinceEpochMillisec();

  //makes the board and reads ing the correct puzzle
  int board[9][9];
  readPuzzle("puzzle.txt",board);
  int workingBoard[9][9];
  copyBoard(board,workingBoard);
  int r=0;
  int c=0;
  int i;
  bool back=false;
  while (r<9||c<9){
    //cout<<"looping"<<endl;
    if (c==9){
      c=0;
      r++;
    }
    if (board[r][c]){
      if (back){
        if (c){
          c--;
        }
        else{
          c=8;
          r--;
        }
      }
     else{
        c++;
      }   
    }
  else{
    //cout<<r<<c<<endl;
    if (back){
      //cout<<"let me try this again"<<endl;
      //cout<<r<<c<<workingBoard[r][c]<<endl;
      i = workingBoard[r][c]+1;
    }
    else{
      i=1;
    }
    back = false;
    workingBoard[r][c] = i;
    while (!checkAll(workingBoard) && !(i>9)){
      workingBoard[r][c] = i;
      i++;
    }
    if (checkAll(workingBoard)){
      //for (int r=0;r<9;r++){
        //printRow(workingBoard[r]);
      //}
      //cout<<"this one works"<<endl;
      c++;
      if (c==9){
        c=0;
        r++;
      }
      }
    else{
      //cout<<"nothing works here"<<endl;
      workingBoard[r][c] = 0;
      back = true;
      if (!c){
        c=8;
        r--;
      }
      else{
        c--;
      }
    }
    }
  }
  long int end;
  end = timeSinceEpochMillisec();
  cout << "Runtime: "<<end-start<<"ms"<<endl;
  for (int r=0;r<9;r++){
    printRow(workingBoard[r]);
  }
}