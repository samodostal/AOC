#include "../lib/template.cpp"

bool is_in_range(int min_y, int max_y, int min_x, int max_x, int vel_x, int vel_y) {
  int pos_y = 0;
  int pos_x = 0;

  while(pos_y >= min_y && pos_x <= max_x) {
    if(pos_y <= max_y && pos_y >= min_y && pos_x <= max_x && pos_x >= min_x) {
      return true;
    }

    pos_x += vel_x;
    pos_y += vel_y;

    if(vel_x > 0) {
      vel_x--;
    } else if(vel_x < 0) {
      vel_x++;
    }
    vel_y--;
  }
  return false;
}

int main() {
  f file("17/set.txt");

  string instructions;
  getline(file, instructions);

  string y_values = split(instructions, "y=")[1];
  string x_values = split(split(instructions, "x=")[1], ", ")[0];

  vector<string> coords_y = split(y_values, "..");
  vector<string> coords_x = split(x_values, "..");

  int min_y = stoi(min(coords_y[0], coords_y[1]));
  int max_y = stoi(max(coords_y[0], coords_y[1]));

  int min_x = stoi(min(coords_x[0], coords_x[1]));
  int max_x = stoi(max(coords_x[0], coords_x[1]));

  int vel_y_initial = abs(min_y);
  int vel_x_initial = abs(max_x);

  int result = 0;

  for (int i = vel_x_initial; i > 0; i--) {
    for (int j = vel_y_initial; j > -500; j-- ) {
      bool is = is_in_range(min_y, max_y, min_x, max_x, i, j);
      if(is == true) {
        result++;
      }
    }
  }

  cout << "Result: " << result << endl;
}
