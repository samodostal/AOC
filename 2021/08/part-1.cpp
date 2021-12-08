#include "../lib/template.cpp"

int main() {
  f file("08/set.txt");

  int r = 0;

  vector<int> outputSizes;

  string row;
  while (getline(file, row)) {
    string secondPart = split(row, " | ")[1];
    stringstream ss(secondPart);
    string token;
    while (ss >> token) {
      outputSizes.push_back(token.size());
    }
  }

  FOR(i, outputSizes) {
    auto val = outputSizes[i];
    if (val == 2 || val == 4 || val == 3 || val == 7) {
      r++;
    }
  }

  cout << r << endl;
}
