#include "../lib/template.cpp"

int main() {
  f file("03/set.txt");

  long r = 0;
  string gamma = "", epsilon = "";
  vector<string> lines;

  string line;
  while (file >> line) {
    lines.p(line);
  }

  FOR(j, 0, lines[0].size()) {
    int ones = 0, zeros = 0;
    FOR(i, lines) {
      if (lines[i][j] == '1') {
        ones++;
      } else {
        zeros++;
      }
    }
    if (ones > zeros) {
      gamma += "1";
      epsilon += "0";
    } else {
      gamma += "0";
      epsilon += "1";
    }
  }

  int dec_gamma = stoi(gamma, nullptr, 2);
  int dec_epsilon = stoi(epsilon, nullptr, 2);

  r = dec_gamma * dec_epsilon;

  cout << "\n" << r << endl;
}
