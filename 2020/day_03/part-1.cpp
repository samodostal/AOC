#include <cstdio>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
  ifstream file("day_03/set.txt");

  vector<string> mx;
  int curX = 0, curY = 0;
  int slopeX = 3, slopeY = 1;
  int maxX;
  int tot = 0;

  string line;
  while(getline(file, line)) {
    mx.push_back(line);
  }

  maxX = mx[0].size();

  while(curY <= mx.size()) {
    if(mx[curY][curX % maxX] == '#') {
      tot++;
    }
    curX += slopeX;
    curY += slopeY;
  }

  cout << tot << endl;
}
