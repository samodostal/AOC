#include "../lib/template.cpp"
#include <algorithm>
#include <string>

int main() {
  f file("05/set.txt");

  int r = 0;
  int x1, y1, x2, y2;
  char c;
  string s;

  vector<string> valid_vectors;

  string column(1000, '.');
  vector<string> map(1000, column);

  while (file >> x1 >> c >> y1 >> s >> x2 >> c >> y2) {
    string whole = to_string(x1) + "," + to_string(y1) + "," + to_string(x2) +
                   "," + to_string(y2);
    valid_vectors.push_back(whole);
  }

  FOR(j, valid_vectors) {
    string vec = valid_vectors[j];
    std::vector<string> vec_split = split(vec, ",");
    x1 = stoi(vec_split[0]);
    y1 = stoi(vec_split[1]);
    x2 = stoi(vec_split[2]);
    y2 = stoi(vec_split[3]);

    int min_x = min(x1, x2);
    int max_x = max(x1, x2);
    int min_y = min(y1, y2);
    int max_y = max(y1, y2);

    if (x1 == x2 || y1 == y2) {
      FOR(i, min_x, max_x + 1) {
        FOR(k, min_y, max_y + 1) {
          if (map[k][i] == '#') {
            r++;
            map[k][i] = 'X';
          } else if (map[k][i] == '.') {
            map[k][i] = '#';
          }
        }
      }
    }
  }

  /* FOR(i, map) { cout << map[i] << endl; } */

  cout << r << endl;
}
