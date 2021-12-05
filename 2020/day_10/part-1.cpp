#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

vector<int> data;

int diff1 = 1;
int diff3 = 1;

int main() {
	freopen("input.txt", "r", stdin);
	int number;
	while(cin >> number) {
		data.push_back(number);
	}
	sort(data.begin(), data.end());
	cout << data << endl;
	for(int i = 1; i < data.size(); i++) {
		int num = data[i];
		int numOld = data[i - 1];
		if(numOld + 1 == num) {
			diff1++;
		} else if (numOld + 3 == num) {
			diff3++;
		}
	}
	int result = diff1 * diff3;
	cout << result << endl;
	//cout << diff1 << " " << diff3 << endl;
}

