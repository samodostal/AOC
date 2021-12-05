#include "../lib/template.cpp"

int main() {
  f file("01/set.txt");

  int r = 0;
  vector<int> ns;

  int n;
  while (file >> n) {
    ns.p(n);
  }

  FOR(i, ns) {
    if (ns[i + 3] > ns[i]) {
      r++;
    }
  }

  cout << r << endl;
}
