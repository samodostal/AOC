#include "../lib/template.cpp"

int main() {
  f file("14/set.txt");

  string templ;
  map<string, long> combinations;
  map<string, long> combinations_empty;
  map<string, char> rules;

  getline(file, templ);

  string line;
  while (getline(file, line)) {
    if (line.empty()) continue;
    vector<string> rule = split(line, " -> ");
    combinations[rule[0]] = 0;
    rules[rule[0]] = rule[1][0];
  }

  FOR(i, templ) {
      if(i == templ.size() - 1) continue;
      string key = string(1, templ[i]) + templ[i + 1];
      combinations[key]++;
  }

  int steps = 40;
  FOR(steps) {
    map<string, long> new_combinations = combinations_empty;
    for (auto &i : combinations) {
      if(i.second == 0) continue;
      string new_pair1 = string(1, i.first[0]) + rules[i.first];
      string new_pair2 = string(1, rules[i.first]) + i.first[1];
      new_combinations[new_pair1] += i.second;
      new_combinations[new_pair2] += i.second;
    }
    combinations = new_combinations;
  }

  long max_count = 0;
  long min_count = LONG_MAX;
  char max_char, min_char = ' ';
  for (auto &i : combinations) {
    long count = 0;
    for(auto &j : combinations) {
      if(i.first[0] == j.first[0]) count += j.second;
    }
    if(count > max_count) {
      max_count = count;
      max_char = i.first[0];
    }
    if(count < min_count) {
      min_count = count;
      min_char = i.first[0];
    }
  }

  cout << "Max: " << max_char << " " << max_count << endl;
  cout << "Min: " << min_char << " " << min_count << endl;
  cout << max_count - min_count + 1 << endl; //why +1?
}
