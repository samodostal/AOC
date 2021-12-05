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
    int count = 0;
    for(int i = 0; i < pwd.length(); i++) {
      if(pwd[i] == c) {
        count++;
      }
    }

    if(count >= bot && count <= top) {
      all++;
    }
  }

  cout << all << endl;
}
