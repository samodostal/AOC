#include <cstdio>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <vector>

using namespace std;

int slope(int slopeX, int slopeY) {
  ifstream file("day_03/set.txt");

  vector<string> mx;
  int curX = 0, curY = 0;
  int maxX;
  long tot = 0;

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

  return tot;
}

int main() {
  long tot0 = slope(1, 1);
  long tot1 = slope(3, 1);
  long tot2 = slope(5, 1);
  long tot3 = slope(7, 1);
  long tot4 = slope(1, 2);

  cout << tot0 * tot1 * tot2 * tot3 * tot4 << endl;
}
