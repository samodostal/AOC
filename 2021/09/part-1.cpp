#include "../lib/template.cpp"

int main() {
  f file("09/set.txt");

  int r = 0;
  vector<vector<int>> rows;

  vector<int> last_row(102, 9);
  rows.push_back(last_row);

  string line;
  while(getline(file, line)) {
    vector<int> row;
    row.push_back(9);
    for(int i = 0; i < line.size(); i++) {
      row.push_back(line[i] - '0');
    }
    row.push_back(9);
    rows.push_back(row);
  }

  rows.push_back(last_row);

  FOR(i, 0, rows.size()) {
    FOR(j, 0, rows[i].size()) {
      if(rows[i][j] < rows[i][j + 1] && rows[i][j] < rows[i][j - 1]) {
        if(rows[i][j] < rows[i - 1][j] && rows[i][j] < rows[i + 1][j]) {
          r += rows[i][j] + 1;
        }
      }
    }
  }


  cout << r << endl;
}
