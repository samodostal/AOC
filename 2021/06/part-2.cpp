#include "../lib/template.cpp"

void fish_cycle(vector<long> fishes_map, int daysLeft) {
  if (daysLeft == 0) {
    long all = 0;
    FOR(i, fishes_map) {
      all += fishes_map[i];
    }
    cout << all << endl;
  }

  long num_of_zeros = fishes_map[0];

  FOR(i, fishes_map) {
    if (i == 0)
      continue;
    fishes_map[i - 1] = fishes_map[i];
  }

  fishes_map[6] += num_of_zeros;
  fishes_map[8] = num_of_zeros;

  if (daysLeft > 0) {
    fish_cycle(fishes_map, daysLeft - 1);
  }
};

int main() {
  f file("06/set.txt");

  long r = 0;

  vector<long> fishes_map(9, 0);
  long n;
  char c;
  while (file >> n >> c) {
    fishes_map[n]++;
  }

  fish_cycle(fishes_map, 256);
}
