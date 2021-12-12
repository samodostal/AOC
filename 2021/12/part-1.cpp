#include "../lib/template.cpp"

bool path_contains(vector<string> path, string s) {
  for (string p : path) {
    if (p == s)
      return true;
  }
  return false;
}

bool is_capital(string s) { return s[0] >= 'A' && s[0] <= 'Z'; }

void solve(vector<string> path, vector<vector<string>> instructions, int &r) {
  string last_path = path[path.size() - 1];

  if(last_path == "end") {
    r++;
    return;
  }

  FOR(i, instructions) {
    if (instructions[i][0] == last_path) {
      string possible_next = instructions[i][1];

      if (!is_capital(possible_next) && path_contains(path, possible_next)) continue;

      auto path_copy = path;
      path_copy.push_back(possible_next);
      solve(path_copy, instructions, r);
    }
  }
}

int main() {
  f file("12/set.txt");

  int r = 0;

  vector<vector<string>> instructions;

  string line;
  while (getline(file, line)) {
    vector<string> instruction = split(line, "-");
    instructions.push_back({instruction[0], instruction[1]});
    instructions.push_back({instruction[1], instruction[0]});
  }

  solve({"start"}, instructions, r);

  cout << r << endl;
}
