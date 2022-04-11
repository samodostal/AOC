#include "../lib/template.cpp"

int main() {
  f file("17/set.txt");

  string instructions;
  getline(file, instructions);

  string y_values = split(instructions, "y=")[1];
  vector<string> coords_y = split(y_values, "..");

  int min_y = stoi(min(coords_y[0], coords_y[1]));
  int max_y = stoi(max(coords_y[0], coords_y[1]));

  cout << min_y << " " << max_y << endl << endl;

  int vel_perm = 1;

  while(true) {
    int pos_y = 0, vel_y = vel_perm;
    while(true) {
      pos_y += vel_y;
      if(pos_y <= max_y && pos_y >= min_y) {
        cout << "pos: " << pos_y << ", vel_perm: " << vel_perm << endl;
        break;
      }
      if(pos_y < min_y) {
        break;
      }
      vel_y--;
    }
    vel_perm++;
  }

  //now just sum of 1..vel_perm that is the largest
}
