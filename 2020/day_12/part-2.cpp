#include <bits/stdc++.h>
#include "../libs/prettyprint.hpp"
using namespace std;

#define PI 3.14159265

int posX = 0;
int posY = 0;

int wayX = 10;
int wayY = 1;

int main() {
	freopen("example.txt", "r", stdin);
	char cmd;
	int val;
	while(cin >> cmd >> val) {
		if(cmd == 'N') {
			wayY += val;
		} else if(cmd == 'S') {
			wayY -= val;
		} else if(cmd == 'E') {
			wayX += val;
		} else if(cmd == 'W') {
			wayX -= val;
		} else if(cmd == 'R' || cmd == 'L') {
			if(cmd == 'L') val = -val;
			float temp1 = ((float)wayX * (float)cos(val * PI / 180.0 )) + ((float)wayY * (float)sin(val * PI / 180.0 ));
			float temp2 = -((float)wayX * (float)sin(val * PI / 180.0 )) + ((float)wayY * (float)cos(val * PI / 180.0 ));
			wayX = temp1;
			wayY = temp2;
			val = abs(val);
		} else if(cmd == 'F') {
			posX += wayX * val;
			posY += wayY * val;
		}
		cout << "cmd:" << cmd << val << " " << posX << " " << posY << " / " << wayX << " " << wayY << endl;
	}
	cout << abs(posX) + abs(posY) << endl;
}

