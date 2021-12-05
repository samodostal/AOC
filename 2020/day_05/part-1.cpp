#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	string word;

	int highestId = 0;

	while(cin >> word) {
		string comV = word.substr(0, 7);

		pair<float, float> curV;
		curV.first = 0;
		curV.second = 127;

		for(int i = 0; i < comV.length(); i++) {
			char c = comV[i];
			int diff = curV.second - curV.first;
			if(c == 'B') {
				curV.first += ceil((float)diff/2);
			} else if (c == 'F') {
				curV.second -= floor((float)diff/2);
			}
		}

		string comH = word.substr(7, 9);

		pair<float, float> curH;
		curH.first = 0;
		curH.second = 7;

		for(int i = 0; i < comH.length(); i++) {
			char c = comH[i];
			int diff = curH.second - curH.first;
			if(c == 'R') {
				curH.first += ceil((float)diff/2);
			} else if (c == 'L') {
				curH.second -= floor((float)diff/2);
			}
		}
		int output = (curV.first * 8) + curH.first;
		if(output > highestId) {
			highestId = output;
		}
	}
	cout << highestId << endl;
}


