#include "../lib/template.cpp"

/*  0000 */
/* 1    2*/
/* 1    2*/
/*  3333 */
/* 4    5*/
/* 4    5*/
/*  6666 */

char signals_difference(string larger, string smaller) {
  FOR(i, larger) {
    bool charFound = false;
    FOR(j, smaller) {
      if (larger[i] == smaller[j]) {
        charFound = true;
        break;
      }
    }
    if (!charFound) {
      return larger[i];
    }
  }
  return 'X';
}

vector<char> signals_difference_multiple(string larger, string smaller) {
  vector<char> result;
  FOR(i, larger) {
    bool charFound = false;
    FOR(j, smaller) {
      if (larger[i] == smaller[j]) {
        charFound = true;
        break;
      }
    }
    if (!charFound) {
      result.push_back(larger[i]);
    }
  }
  return result;
}

int main() {
  f file("08/set.txt");

  long r = 0;

  string row;
  while (getline(file, row)) {
    char map[7] = {' ', ' ', ' ', ' ', ' ', ' ', ' '};
    string one, five, six = "", eight;
    string part_four, part_five;
    vector<string> p = split(row, " | ");
    vector<string> signal_strings = split(p[0], " ");
    vector<string> output_strings = split(p[1], " ");
    sort(signal_strings.begin(), signal_strings.end(),
         [](string a, string b) { return a.size() < b.size(); });
    FOR(i, signal_strings) {
      string signal = signal_strings[i];
      if (signal.size() == 2) { // 1
        one = signal;
      } else if (signal.size() == 3) { // 7
        map[0] = signals_difference(signal, one);
      } else if (signal.size() == 4) { // 4
        vector<char> part = signals_difference_multiple(signal, one);
        part_four = string() + part[0] + part[1];
      } else if (signal.size() == 5) { // 2 or 3 or 5
        vector<char> part = signals_difference_multiple(part_four, signal);
        if (part.size() == 1) { // then signal is 2 or 3
          map[1] = part[0];
          map[3] = signals_difference(part_four, string() + map[1]);
        } else { // then signal is 5
          five = signal;
        }
      } else if (signal.size() == 6) { // 0 or 6 or 9
        map[2] = signals_difference(one, five);
        map[5] = signals_difference(one, string() + map[2]);
        string part_nine = string() + map[2] + map[3];
        vector<char> part = signals_difference_multiple(part_nine, signal);
        if (part.size() == 0) { // then signal is 9
          string all = "abcdefg";
          map[4] = signals_difference(all, signal);
          string in_map =
              string() + map[0] + map[1] + map[2] + map[3] + map[4] + map[5];
          map[6] = signals_difference(all, in_map);
        }
      } else if (signal.size() == 7) { // 8
        eight = signal;
      }
    }

    string output = "";
    FOR(i, output_strings) {
      string signal = output_strings[i];
      if (signal.size() == 2) {
        output += "1";
      } else if (signal.size() == 3) {
        output += "7";
      } else if (signal.size() == 4) {
        output += "4";
      } else if (signal.size() == 5) { // 2 or 3 ro 5
        string part = string() + map[1];
        char diff = signals_difference(part, signal);
        if (diff == 'X') {
          output += "5";
          continue;
        }
        part = string() + map[5];
        diff = signals_difference(part, signal);
        if (diff != 'X') {
          output += "2";
          continue;
        }
        output += "3";
      } else if (signal.size() == 6) { // 0 or 6 or 9
        string part = string() + map[3];
        char diff = signals_difference(part, signal);
        if (diff != 'X') {
          output += "0";
          continue;
        }
        part = string() + map[2];
        diff = signals_difference(part, signal);
        if (diff != 'X') {
          output += "6";
          continue;
        }

        output += "9";
      } else if (signal.size() == 7) { // 8
        output += "8";
      }
    }
    r += stoi(output);
  }

  cout << r << endl;
}
