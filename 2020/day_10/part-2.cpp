#include <bits/stdc++.h>
#include "../libs/prettyprint.hpp"
using namespace std;

vector<int> data;
int a = 0;

void check(int i) {
	int maxVal = data[data.size() - 1];
	if(data[i] == maxVal) {
		a++;
		return;
	}
	if(data[i + 1] - data[i] <= 3) {
		check(i + 1);
	}
	if(data[i + 2] - data[i] <= 3) {
		check(i + 2);
	}
	if(data[i + 3] - data[i] <= 3) {
		check(i + 3);
	}
}

int main() {
	freopen("example.txt", "r", stdin);
	int number;
	while(cin >> number) {
		data.push_back(number);
	}
	sort(data.begin(), data.end());
	cout << data << endl;
	check(0);
	cout << a << endl;
}

