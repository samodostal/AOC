#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> ns;
  ifstream file("day_01/set.txt");

  int n;
  while (file >> n) {
    ns.push_back(n);
  }

  for (int i : ns) {
    for (int j : ns) {
      if (i + j == 2020) {
        cout << i * j << endl;
        return 0;
      }
    }
  }
}
