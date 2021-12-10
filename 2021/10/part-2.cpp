#include "../lib/template.cpp"

int get_points(char c) {
  if (c == ')') return 1;
  if (c == ']') return 2;
  if (c == '}') return 3;
  if (c == '>') return 4;
  return 0;
}

bool is_opening(char c) {
    return c == '(' || c == '[' || c == '{' || c == '<';
}

char opposite_char(char c) {
    if (c == '[') return ']';
    if (c == ']') return '[';
    if (c == '{') return '}';
    if (c == '}') return '{';
    if (c == '(') return ')';
    if (c == ')') return '(';
    if (c == '<') return '>';
    if (c == '>') return '<';
    throw "Invalid character";
}

int main() {
  f file("10/set.txt");

  vector<long> scores;

  string line;
  while(getline(file, line)) {
    stack<char> stack;
    bool is_valid = true;

    stringstream ss(line);
    char c;
    while(ss >> c) {
      if(!stack.empty() && stack.top() == opposite_char(c)) {
        stack.pop();
      } else {
        if(is_opening(c)) {
          stack.push(c);
        } else {
          is_valid = false;
          break;
        }
      }
    }

    if(!is_valid) continue;

    long r = 0;
    while(!stack.empty()) {
      char c = opposite_char(stack.top());
      r *= 5;
      r += get_points(c);
      stack.pop();
    }
    scores.push_back(r);
  }

  sort(scores.begin(), scores.end());
  cout << scores[scores.size()/2] << endl;
}
