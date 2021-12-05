#include "../lib/template.cpp"

int main() {
  f file("02/set.txt");

  long r = 0;
  int x = 0, y = 0, a = 0;

  string cmd;
  int num;

  while (file >> cmd >> num) {
    if (cmd == "forward") {
      x += num;
      y += a * num;
    }
    if (cmd == "up")
      a -= num;
    if (cmd == "down")
      a += num;
  }

  r = x * y;
  cout << r << endl;
}
