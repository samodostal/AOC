#include <fstream>
#include <iostream>

using namespace std;

int main() {
  ifstream file("day_02/set.txt");

  int bot, top;
  char t, c;
  string pwd;

  int all = 0;

  while(file >> bot >> t >> top >> c >> t >> pwd) {
    bool isBot = false, isTop = false;

    if(pwd[bot - 1] == c) {
      isBot = true;
    } 
    if(pwd[top - 1] == c) {
      isTop = true;
    }

    if(isBot != isTop) {
      all++;
    }
  }

  cout << all << endl;
}
