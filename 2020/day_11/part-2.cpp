#include <bits/stdc++.h>
#include "../libs/prettyprint.hpp"
using namespace std;

vector<vector<char>> data;
int n = 0;
int f = 0;

char checkInDirection(vector<vector<char>>input, int posX, int posY, int movX, int movY) {
	//cout << posX << posY << movX << movY << endl;
	if(posY + movY + 1 > input.size() || posY + movY < 0) return 'x';
	if(posX + movX + 1 > input[0].size() || posX + movX < 0) return 'x';
	char nextInDir = input[posY + movY][posX + movX];
	if(nextInDir == '#') return '#';
	if(nextInDir == 'L') return 'L';
	return checkInDirection(input, posX + movX, posY + movY, movX, movY);
}

void cycle(vector<vector<char>> input) {
	f++;
	int u = 0;
	vector<vector<char>> o = input;
	for(int i = 0; i < input.size(); i++) {
		vector<char> row, rowAbove, rowBellow;
		row = input[i];
		if(i > 0) {
			rowAbove = input[i - 1];
		}
		if(i + 1 < input.size()) {
			rowBellow = input[i + 1];
		}
		for(int j = 0; j < row.size(); j++) {
			//char p1, p2, p3, p4, p5, p6, p7, p8, p9;

			char p5 = row[j];

			char p1 = checkInDirection(input, j, i, -1, -1);
			char p2 = checkInDirection(input, j, i,  0, -1);
			char p3 = checkInDirection(input, j, i, 	1, -1);
			char p4 = checkInDirection(input, j, i, -1,  0);
			char p6 = checkInDirection(input, j, i,  1,  0);
			char p7 = checkInDirection(input, j, i, -1,  1);
			char p8 = checkInDirection(input, j, i,  0,  1);
			char p9 = checkInDirection(input, j, i,  1,  1);

			if(p5 == '#') u++;

			//cout << p1 << p2 << p3 << p4 << p6 << p7 << p8 << p9 << endl;
			//cout << p5;
			
			if(p5 == 'L' && p1 != '#' && p2 != '#' && p3 != '#' && p4 != '#' && p6 != '#' && p7 != '#' && p8 != '#' && p9 != '#') {
				o[i][j] = '#';
			}
			if(p5 == '#') {
				int k = 0;
				if(p1 == '#') k++;
				if(p2 == '#') k++;
				if(p3 == '#') k++;
				if(p4 == '#') k++;
				if(p6 == '#') k++;
				if(p7 == '#') k++;
				if(p8 == '#') k++;
				if(p9 == '#') k++;
				//cout << k << endl;
				if(k >= 5) {
					o[i][j] = 'L';
				}
			}
		}
		//cout << endl;
	}
		//cout << endl;
	if(o != input) {
		cycle(o);
	} else {
		cout << "NOW: " << u << endl;
		//cout << o << endl;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	string line;
	while(getline(cin, line)) {
		data.push_back(vector<char>());
		stringstream ss(line);
		char temp;
		while(ss >> temp) {
			data[n].push_back(temp);
		}
		n++;
	}
	cycle(data);
}
