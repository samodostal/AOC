#include "../lib/template.cpp"

void check_adjacent(vector<vector<int>> &v, int posCol, int posRow, vector<vector<int>> &visited) {
  vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  FOR(i, dirs) {
    int newCol = posCol + dirs[i][0];
    int newRow = posRow + dirs[i][1];

    if (v[newCol][newRow] > v[posCol][posRow] && v[newCol][newRow] != 9) {
      vector<int> point = {newCol, newRow};
      bool was_visited = false;
      FOR(i, visited) {
        vector<int> p = visited[i];
        if(p[0] == point[0] && p[1] == point[1]) {
          was_visited = true;
          break;
        }
      }
      if(!was_visited) {
        visited.push_back(point);
        check_adjacent(v, newCol, newRow, visited);
      }
    }
  }
}

int main() {
  f file("09/set.txt");

  int r = 0;
  vector<int> adj_size;
  vector<vector<int>> rows;

  vector<int> last_row(102, 9);
  rows.push_back(last_row);

  string line;
  while (getline(file, line)) {
    vector<int> row;
    row.push_back(9);
    for (int i = 0; i < line.size(); i++) {
      row.push_back(line[i] - '0');
    }
    row.push_back(9);
    rows.push_back(row);
  }

  rows.push_back(last_row);

  FOR(i, 0, rows.size()) {
    FOR(j, 0, rows[i].size()) {
      if (rows[i][j] < rows[i][j + 1] && rows[i][j] < rows[i][j - 1]) {
        if (rows[i][j] < rows[i - 1][j] && rows[i][j] < rows[i + 1][j]) {
          vector<vector<int>> points;
          vector<int> point = {i, j};
          points.push_back(point);

          check_adjacent(rows, i, j, points);
          adj_size.push_back(points.size());
        }
      }
    }
  }

  sort(adj_size.begin(), adj_size.end());
  reverse(adj_size.begin(), adj_size.end());
  int sum = 1;
  FOR(i, 0, 3) {
    sum *= adj_size[i];
  }

  cout << sum << endl;
}
