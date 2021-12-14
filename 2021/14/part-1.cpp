#include "../lib/template.cpp"

int main() {
  f file("14/set.txt");

  string templ;
  vector<vector<string>> rules;

  getline(file, templ);

  string line;
  while (getline(file, line)) {
    if (line.empty()) continue;
    vector<string> rule = split(line, " -> ");
    rules.push_back(rule);
  }

  int steps = 10;
  FOR(steps) {
    int inserted = 0;
    string templ_copy = templ;
    FOR(i, templ) {
      if(i == templ.size() - 1) continue;
      string templ_rule = string(1, templ[i]) + templ[i + 1];
      FOR(j, rules) {
        if(rules[j][0] == templ_rule) {
          templ_copy.insert(i + 1 + inserted, rules[j][1]);
          inserted++;
        }
      }
    }
    templ = templ_copy;
  }

  int max_count = 0;
  int min_count = INT_MAX;
  char max_char, min_char = ' ';
  FOR(i, templ) {
    int count = 0;
    FOR(j, templ) {
      if(templ[i] == templ[j]) count++;
    }
    if(count > max_count) {
      max_count = count;
      max_char = templ[i];
    }
    if(count < min_count) {
      min_count = count;
      min_char = templ[i];
    }
  }

  cout << max_count - min_count << endl;
}
