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
      for (int k : ns) {
        if (i + j + k == 2020) {
          cout << i * j * k << endl;
          return 0;
        }
      }
    }
  }
}
