#include "../lib/template.cpp"

bool is_unique(vector<vector<int>> coords, vector<int> coord) {
  for (auto c : coords) {
    if (c[0] == coord[0] && c[1] == coord[1]) {
      return false;
    }
  }
  return true;
}

int main() {
  f file("13/set.txt");

  int r = 0;
  vector<vector<int>> coords; // {{x, y}, {x, y}, ...}
  string line;
  vector<int> fold_values;
  vector<char> fold_keys;

  while (getline(file, line)) {
    if (line.empty()) {
      while(getline(file, line)) {
        vector<string> s = split(line, "=");
        fold_values.push_back(stoi(s[1]));
        fold_keys.push_back(s[0][s[0].size() - 1]);
      }
    } else {
      vector<string> s = split(line, ",");
      int x = stoi(s[0]);
      int y = stoi(s[1]);
      coords.push_back({x, y});
    }
  }

  vector<vector<int>> new_coords;
  vector<vector<int>> temp_coords = coords;
  FOR(j, fold_keys) {
    new_coords.clear();
    cout << "Fold " << fold_keys[j] << ": " << fold_values[j] << endl;
    FOR(i, temp_coords) {
      vector<int> new_coord = temp_coords[i];
      if(fold_keys[j] == 'y') {
        int y = temp_coords[i][1];
        if (y > fold_values[j]) {
          new_coord[1] = fold_values[j] - (y - fold_values[j]);
        }
      } else {
        int x = temp_coords[i][0];
        if (x > fold_values[j]) {
          new_coord[0] = fold_values[j] - (x - fold_values[j]);
        }
      }
      if(is_unique(new_coords, new_coord)) {
        new_coords.push_back(new_coord);
      }
    }
    temp_coords = new_coords;
  }
  cout << endl;

  FOR(i, 0, 6) {
    FOR(j, 0, 50) {
      if (!is_unique(new_coords, {j, i})) {
        cout << "#";
      } else {
        cout << ".";
      }
    }
    cout << endl;
  }

  cout << endl;
  cout << coords.size() << endl;
  cout << new_coords.size() << endl;
}
