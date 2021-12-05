#include "../lib/template.cpp"

int main() {
  f file("03/set.txt");

  long r = 0;
  string oxygen = "", scrubber = "";
  vector<string> lines;

  string line;
  while (file >> line) {
    lines.p(line);
  }

  vector<string> lines_oxygen = lines;
  int currentIndex = 0;
  while (lines_oxygen.size() > 1) {
    int ones = 0, zeros = 0;
    FOR(i, lines_oxygen) {
      if (lines_oxygen[i][currentIndex] == '1') {
        ones++;
      } else {
        zeros++;
      }
    }
    filter(lines_oxygen, [currentIndex, ones, zeros](string s) {
      return (ones >= zeros) ? s[currentIndex] == '1' : s[currentIndex] == '0';
    });
    currentIndex++;
  }

  vector<string> lines_scrubber = lines;
  currentIndex = 0;
  while (lines_scrubber.size() > 1) {
    int ones = 0, zeros = 0;
    FOR(i, lines_scrubber) {
      if (lines_scrubber[i][currentIndex] == '1') {
        ones++;
      } else {
        zeros++;
      }
    }
    filter(lines_scrubber, [currentIndex, ones, zeros](string s) {
      return (ones >= zeros) ? s[currentIndex] == '0' : s[currentIndex] == '1';
    });
    currentIndex++;
  }

  int dec_oxygen = stoi(lines_oxygen[0], nullptr, 2);
  int dec_scrubber = stoi(lines_scrubber[0], nullptr, 2);

  r = dec_oxygen * dec_scrubber;

  cout << "\n" << r << endl;
}
