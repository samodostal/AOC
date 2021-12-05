#include <bits/stdc++.h>
#include "../libs/prettyprint.hpp"
using namespace std;

vector<vector<char>> data;
int n = 0;
int f = 0;

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
			char p1, p2, p3, p4, p5, p6, p7, p8, p9;
			p5 = row[j];
			if(j < row.size()) {
				if(rowAbove.size()) {
					p2 = rowAbove[j];
					p3 = rowAbove[j + 1];
				} else {
					p2 = 'x';
					p3 = 'x';
				}
				p6 = row[j + 1];
				if(rowBellow.size()) {
					p8 = rowBellow[j];
					p9 = rowBellow[j + 1];
				} else {
					p8 = 'x';
					p9 = 'x';
				}
			} else {
				p2 = 'x';
				p3 = 'x';
				p6 = 'x';
				p8 = 'x';
				p9 = 'x';
			}

			if(j > 0) {
				if(rowAbove.size()) {
					p1 = rowAbove[j - 1];
				} else {
					p1 = 'x';
				}
				p4 = row[j - 1];
				if(rowBellow.size()) {
					p7 = rowBellow[j - 1];
				} else {
					p7 = 'x';
				}
			} else {
				p1 = 'x';
				p4 = 'x';
				p7 = 'x';
			}

			if(p5 == '#') u++;
			
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
				if(k >= 4) {

					o[i][j] = 'L';
				}
			}
		}
	}
	if(o != input) {
		cycle(o);
	} else {
		cout << "NOW: " << u << endl;
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
