#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

vector<int> data;
vector<int> oneSet;

int target = 21806024;
//int target = 127;

int x = 0;

void check() {
	for(int i = x; x < data.size(); x++) {
		int sum = 0;
		while(sum < target) {
			for(int k = x; k < data.size(); k++) {
				sum += data[k];
				oneSet.push_back(data[k]);
				if(sum == target) {
					int result = data[k] + data[x];
					cout << oneSet << endl;
					int lowest = oneSet[0];
					int largest = 0;
					for(int s = 0; s < oneSet.size(); s++) {
						if(oneSet[s] < lowest) {
							lowest = oneSet[s];
						}
						if(oneSet[s] > largest) {
							largest = oneSet[s];
						}
					}
					cout << lowest + largest << endl;
					return;
				}
			}
			oneSet.clear();
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	int number;
	while(cin >> number) {
		data.push_back(number);
	}
	for(int i = 0; i < data.size(); i++) {
		check();
		x++;
	}
}

