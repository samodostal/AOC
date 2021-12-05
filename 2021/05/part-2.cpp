#include "../lib/template.cpp"
#include <algorithm>
#include <string>

void add_to_map(vector<string> &map, int y, int x, int &r) {
  if (map[y][x] == '#') {
    map[y][x] = 'X';
    r++;
  } else if (map[y][x] == '.') {
    map[y][x] = '#';
  }
}

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

    int dx = x2 > x1 ? 1 : -1;
    int dy = y2 > y1 ? 1 : -1;
    if (x1 == x2)
      dx = 0;
    if (y1 == y2)
      dy = 0;

    add_to_map(map, y1, x1, r);
    while (x1 != x2 || y1 != y2) {
      x1 += dx;
      y1 += dy;
      add_to_map(map, y1, x1, r);
    }
  }

  /* FOR(i, map) { cout << map[i] << endl; } */

  cout << r << endl;
}
