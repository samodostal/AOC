#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	string line;
	int i = 0;
	int o = 0;
	int a = 0;
	vector<vector<char>> output;

	while(getline(cin, line)) {
		if(i == 0) {
			output.push_back(vector<char>());
		}
		//cout << a << endl;
		stringstream split(line);
		char temp;
		while(split >> temp) {
				output[i].push_back(temp);
		}
		if(line.empty()) {
			output[i].insert(output[i].begin(), a);
			output.push_back(vector<char>());
			a = 0;
			i++;
		} else {
			a++;
		}
	}
	int x = 0;
	//cout << output << endl;
	for(int i = 0; i < output.size(); i++) {
		vector<char> t = output[i];
		vector<char> c;
		for(int k = 1; k < t.size(); k++) {
			if(count(t.begin(), t.end(), t[k]) == t[0] && count(c.begin(), c.end(), t[k]) == 0) {
				//cout << t[k] << (int)t[0] << endl;
				x++;
				c.push_back(t[k]);
			}
		}
	}
	cout << x << endl;
}

