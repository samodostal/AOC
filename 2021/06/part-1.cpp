#include "../lib/template.cpp"

void fish_cycle(vector<int> &fishes, int daysLeft) {
  if(daysLeft == 0) {
    cout << fishes.size() << endl;
  }
  FOR(i, fishes) {
    int fish = fishes[i];
    if(fish == 0) {
      fishes[i] = 6;
      fishes.push_back(9);
    } else {
      fishes[i] = fish - 1;
    }
  }
  if(daysLeft > 0) {
    fish_cycle(fishes, daysLeft - 1);
  }
};

int main() {
  f file("06/set.txt");

  int r = 0;

  vector<int> fishes;
  int n;
  char c;
  while (file >> n >> c) {
    fishes.push_back(n);
  }

  fish_cycle(fishes, 80);
}
