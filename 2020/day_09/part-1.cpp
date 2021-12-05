#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

vector<int> data;

int start = 0;

bool canBeCreated(int num) {
	for(int i = start; i < data.size(); i++) {
		int val1 = data[i];
		for(int j = start; j < data.size(); j++) {
			int val2 = data[j];
			//cout << val1 << " " << val2 << endl;
			if(j == i) continue;
			if(val1 + val2 == num) {
				return true;
			}
		}
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	int number;
	while(cin >> number) {
		if(data.size() < 25) {
			data.push_back(number);
			//cout << data << endl;
		} else {
			//cout << number << endl;
			bool can = canBeCreated(number);
			//cout << "CANN: " << can << endl;
			if(can) {
				data.push_back(number);
				start++;
			} else {
				cout << "We got him: " << number << endl;
				return 0;
			}
		}
	}
}

