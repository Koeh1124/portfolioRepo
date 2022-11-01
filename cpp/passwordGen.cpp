#include <iostream>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
using namespace std;
char getRandomLetter(){
  string letters = "abcdefghijklmnopqurtuvwxyzABCEDFGHIJKLMNOPQURTUVWXYZ1234567890!@#$%^&*()";
  int randomIndex = rand() % (letters.length()-1);
  return letters[randomIndex];
}
int passwordGen() {
  int numOChars;
  cout << "How many characters do you want your passwords to be? ";
  cin >> numOChars;
  for (int i =0;i<numOChars;i++){
    srand (time(NULL)+i);
    cout << getRandomLetter();
    }
}