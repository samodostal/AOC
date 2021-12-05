#include <bits/stdc++.h>
#include "../libs/prettyprint.hpp"
using namespace std;

int rotation = 90;
int posX = 0;
int posY = 0;

int main() {
	freopen("input.txt", "r", stdin);
	char cmd;
	int val;
	while(cin >> cmd >> val) {
		if(cmd == 'N') {
			posY += val;
		} else if(cmd == 'S') {
			posY -= val;
		} else if(cmd == 'E') {
			posX += val;
		} else if(cmd == 'W') {
			posX -= val;
		} else if(cmd == 'L') {
			rotation = (rotation - val + 360) % 360;
		} else if(cmd == 'R') {
			rotation = (rotation + val) % 360;
		} else if(cmd == 'F') {
			if(rotation == 90) {
				posX += val;
			} else if(rotation == 180) {
				posY -= val;
			} else if(rotation == 270) {
				posX -= val;
			} else if(rotation == 0) {
				posY += val;
			}
		}
	}
	cout << abs(posX) + abs(posY) << endl;
}

