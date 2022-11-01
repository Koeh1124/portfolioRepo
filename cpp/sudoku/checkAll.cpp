#include <iostream>

using namespace std;
/*
check gaets a section (ros col, or sec)
after making a blank list it loops through each of the items in the section it is given
for each item it sees if it is in the checklist
if it's in there then there are duplicates and we return false
otherwise we add the item to the checklist
then we return true

this essentally compairs each item in the list and if thare are duplicates it returns false

*could be made better if we only use one arry(I'll have to look into that), but it works for now
*/
void printRow(int row[9]){
  for (int i=0;i<9;i++){
    cout << row[i];
  }
  cout<<endl;
}

bool check(int section[9]){
  for (int i=0;i<9;i++){
    for (int c=0;c<9;c++){
      if ((c!=i && section[i] == section[c] && section[i]!=0) || section[i]>9 || section[c]>9){
        return false;
      }
    }
  }
  return true;
}

bool checkRows(int board[9][9]){
  for (int row =0;row<9;row++){
    if (check(board[row])){
      continue;
    }
    else{
      return false;
    }
    }
return true;
}
int secCol(int col){
  if (col-3<0){
    return 0;
  }
  else if (col-6<0){
    return 1;
  }
  return 2;
}

bool checkCols(int board[9][9]){
  int rotatedBoard[9][9];
  for (int r=0;r<9;r++){
    for (int c=0;c<9;c++){
      rotatedBoard[c][r] = board[r][c];
    }
  }
  if (checkRows(rotatedBoard)){
    return true;
  }
  return false;
}

bool checkSections(int board[9][9]){
  int sections[9][9];
  int rowCounter = 0;
  for (int r=0;r<9;r++){
    int colCounter = 0;
    for (int c=0;c<9;c++){
      if ((r-3)<0){
        sections[secCol(c)][colCounter+r%3+rowCounter] = board[r][c];
      }
      else if ((r-6)<0){
        sections[secCol(c)+3][colCounter+r%3+rowCounter] = board[r][c];       
      }
      else{
        sections[secCol(c)+6][colCounter+r%3+rowCounter] = board[r][c];
      }
      colCounter+=1;
      if (colCounter==3){
        colCounter=0;
      }
      }
    rowCounter+=2;
    if(rowCounter>4){
      rowCounter=0;
    }
    }
  for (int i=0;i<9;i++){
    if (check(sections[i])){
      continue;
    }
    else{
      return false;
    }
  }
  return true;
}

bool checkAll(int board[9][9]){
  if (checkRows(board)&&checkCols(board)&&checkSections(board)){
    return true;
  }
  return false;
}