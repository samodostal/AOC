#include "../lib/template.cpp"

int main() {
  f file("07/set.txt");

  int r = 0;

  vector<int> outcomes;
  vector<int> fuels;
  vector<int> crabs;

  int num;
  char c;
  while (file >> num >> c) {
    crabs.push_back(num);
  }

  int max = *max_element(crabs.begin(), crabs.end());
  int min = *min_element(crabs.begin(), crabs.end());

  FOR(i, min, max) {
    int sum = 0;
    FOR(j, 0, crabs.size()) { sum += abs(crabs[j] - i); }
    outcomes.push_back(sum);
  }

  r = *min_element(outcomes.begin(), outcomes.end());

  cout << r << endl;
}
