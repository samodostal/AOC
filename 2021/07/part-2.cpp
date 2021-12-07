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
    FOR(j, 0, crabs.size()) {
      int crab_price = 0;
      auto crabs_copy = crabs;
      int k = 1;
      while (crabs_copy[j] != i) {
        int add = crabs_copy[j] > i ? -1 : 1;
        crabs_copy[j] += add;
        crab_price += k;
        k++;
      }
      sum += crab_price;
    }
    outcomes.push_back(sum);
  }

  r = *min_element(outcomes.begin(), outcomes.end());
  cout << r << endl;
}
