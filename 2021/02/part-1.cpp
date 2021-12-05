#include "../lib/template.cpp"

int main() {
  f file("02/set.txt");

  long r = 0;
  int x = 0, y = 0;

  string cmd;
  int num;

  while (file >> cmd >> num) {
    if (cmd == "forward")
      x += num;
    if (cmd == "up")
      y -= num;
    if (cmd == "down")
      y += num;
  }

  r = x * y;
  cout << r << endl;
}
