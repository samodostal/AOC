#include "../lib/template.cpp"

int get_points(char c) {
  if (c == ')') return 3;
  if (c == ']') return 57;
  if (c == '}') return 1197;
  if (c == '>') return 25137;
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

  int r = 0;

  string line;
  while(getline(file, line)) {
    stack<char> stack;

    stringstream ss(line);
    char c;
    while(ss >> c) {
      if(!stack.empty() && stack.top() == opposite_char(c)) {
        stack.pop();
      } else {
        if(is_opening(c)) {
          stack.push(c);
        } else {
          r += get_points(c);
          break;
        }
      }
    }
  }

  cout << r << endl;
}
