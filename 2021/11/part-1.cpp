#include "../lib/template.cpp"

void printRows(vector<string> rows) {
  FOR(i, rows) {
    FOR(j, rows[i]) { cout << rows[i][j]; }
    cout << endl;
  }
  cout << endl;
}

void increaseByOne(vector<string> &rows) {
  FOR(i, rows) {
    string &row = rows[i];
    FOR(j, row) {
      int numVal = row[j] - '0';
      if (numVal == 9) {
        row[j] = 'X';
      } else {
        numVal++;
        row[j] = numVal + '0';
      }
    }
  }
}

void increaseAdjacent(vector<string> &rows, int row, int col) {
  vector<vector<int>> dirs = {{0, 1},  {1, 1},   {1, 0},  {1, -1},
                              {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};

  rows[row][col] = 'Y';
  FOR(i, dirs) {
    int r = row + dirs[i][0];
    int c = col + dirs[i][1];
    if (r >= 0 && r < rows.size() && c >= 0 && c < rows[r].size()) {
      if (rows[r][c] != 'X' && rows[r][c] != 'Y') {
        int numVal = rows[r][c] - '0';
        if (numVal < 9) {
          numVal++;
          rows[r][c] = numVal + '0';
        } else {
          rows[r][c] = 'X';
        }
      }
    }
  }
}

bool findsX(vector<string> rows) {
  FOR(i, rows) {
    FOR(j, rows[i]) {
      if (rows[i][j] == 'X') {
        return true;
      }
    }
  }
  return false;
}

void increaseFlashingAdjacent(vector<string> &rows) {
  vector<vector<int>> coords;
  while (findsX(rows)) {
    FOR(i, rows) {
      FOR(j, rows[i]) {
        if (rows[i][j] == 'X') {
          increaseAdjacent(rows, i, j);
        }
      }
    }
  }
}

int resetFlashing(vector<string> &rows) {
  int numResets = 0;
  FOR(i, rows) {
    string &row = rows[i];
    FOR(j, row) {
      if (row[j] == 'Y') {
        row[j] = '0';
        numResets++;
      }
    }
  }
  return numResets;
}

int main() {
  f file("11/set.txt");

  int r = 0;
  vector<string> rows;

  string line;
  while (getline(file, line)) {
    rows.push_back(line);
  }

  int loopCount = 100;
  while (loopCount--) {
    increaseByOne(rows);
    increaseFlashingAdjacent(rows);
    r += resetFlashing(rows);
  }

  cout << r << endl;
}
