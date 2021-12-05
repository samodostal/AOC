#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	string line;
	int i = 0;
	int o = 0;
	vector<vector<char>> output;

	while(getline(cin, line)) {
		if(i == 0) {
			output.push_back(vector<char>());
		}
		stringstream split(line);
		char temp;
		while(split >> temp) {
			if(!count(output[i].begin(), output[i].end(), temp)) {
				output[i].push_back(temp);
			}
		}
		if(line.empty()) {
			output.push_back(vector<char>());
			i++;
		}
	}
	cout << output << endl;
	for(int i = 0; i < output.size(); i++) {
		o += output[i].size();
	}
	cout << o << endl;
}


