#include "../../2021/lib/template.cpp"

int main() {
  ifstream file("day_04/xmp.txt");

  vector<string> lines = {""};

  string line;
  while (getline(file, line)) {
    if (line.empty()) {
      lines.push_back("");
    } else {
      lines[lines.size() - 1] += line + " ";
    }
  }

  for (string row : lines) {
    vector<string> cmp = split(row, " ");
    FOR(i, cmp) {
      if(empty(cmp[i])) continue;
      vector<string> whole = split(cmp[i], ":");
      string key = whole[0];
      string value = whole[1];
      cout << key << ": " << value << endl;
    }
  }
}
