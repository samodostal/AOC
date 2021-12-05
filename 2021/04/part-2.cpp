#include "../lib/template.cpp"

class Board {
public:
  int id;
  int most_recent;
  vector<vector<string>> rows;
  Board(int id) { this->id = id; }
  void add_row(string row_unparsed) {
    vector<string> row;
    stringstream ss(row_unparsed);
    string s;
    while (ss >> s) {
      row.push_back(s);
    }
    rows.push_back(row);
  }
  void add_bingo_num(string bingo_num) {
    most_recent = stoi(bingo_num);
    FOR(i, rows) {
      FOR(j, rows[i]) {
        if (rows[i][j] == bingo_num) {
          rows[i][j] = "X";
        }
      }
    }
  }
  bool check_win() { return check_rows() || check_cols(); }
  int result() {
    int total = 0;
    FOR(i, rows) {
      FOR(j, rows[i]) {
        if (rows[i][j] != "X") {
          total += stoi(rows[i][j]);
        }
      }
    }
    return total * most_recent;
  }
  void print_self() {
    FOR(i, rows) {
      FOR(j, rows[i]) { cout << rows[i][j] << " "; }
      cout << endl;
    }
    cout << endl;
  }
  bool check_rows() {
    FOR(i, rows) {
      if (check_row(rows[i])) {
        return true;
      }
    }
    return false;
  }
  bool check_cols() {
    vector<vector<string>> cols;

    FOR(k, rows) {
      vector<string> col;
      FOR(i, rows) { col.push_back(rows[i][k]); }
      cols.push_back(col);
    }

    FOR(i, cols) {
      if (check_row(cols[i])) {
        return true;
      }
    }
    return false;
  }
  bool check_row(vector<string> row) {
    FOR(i, row) {
      if (trim(row[i]) != "X") {
        return false;
      }
    }
    return true;
  }
};

int main() {
  f file("04/set.txt");

  vector<Board> boards;
  string row;

  // First row
  getline(file, row);
  vector<string> bingo_nums = split(row, ",");

  int i = 0;
  // Bingo boards
  while (getline(file, row)) {
    if (row.empty()) {
      Board *board = new Board(i);
      boards.push_back(*board);
      continue;
    }
    Board *board = &boards.back();
    board->add_row(row);
    i++;
  }

  vector<int> boards_that_won;
  Board *losing_board = nullptr;
  // Add bingo numbers and check if won
  FOR(i, bingo_nums) {
    if (losing_board) {
      break;
    }
    FOR(j, boards) {
      Board *board = &boards[j];

      if (find(boards_that_won.begin(), boards_that_won.end(), board->id) !=
          boards_that_won.end()) {
        continue;
      }

      board->add_bingo_num(bingo_nums[i]);
      /* board->print_self(); */
      bool has_won = board->check_win();
      if (has_won) {
        boards_that_won.push_back(board->id);
        if (boards_that_won.size() == boards.size()) {
          losing_board = board;
        }
      }
    }
  }

  cout << losing_board->result() << endl;
}
