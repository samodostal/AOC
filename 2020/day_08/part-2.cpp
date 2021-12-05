
#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

vector<tuple<string, char, int>> data;
vector<int> was;
int global = 0;

void execute(int i, vector<tuple<string, char, int>>temp) {
	if(count(was.begin(), was.end(), i)) {
		return;
	}
	if(i + 1 > temp.size()) {
		cout << "We won: " << global << endl;
		return;
	}
	was.push_back(i);
	tuple<string, char, int> current = temp[i];
	string word = get<0>(current);
	char sign = get<1>(current);
	int value = get<2>(current);
	if(sign == '+') {
		if(word == "acc") {
			global += value;
			execute(i + 1, temp);
		} else if (word == "jmp") {
			execute(i + value, temp);
		}	else if (word == "nop") {
			execute(i + 1, temp);
		}
	} else if (sign == '-') {
		if(word == "acc") {
			global -= value;
			execute(i + 1, temp);
		} else if (word == "jmp") {
			execute(i - value, temp);
		} else if (word == "nop") {
			execute(i + 1, temp);
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	string word;
	char sign;
	int value;
	while(cin >> word >> sign >> value) {
		data.push_back(make_tuple(word, sign, value));
	}
	execute(0, data);
	for(int i = 0; i < 624; i++) {
		was.clear();
		global = 0;
		string& comm = get<0>(data[i]);
		vector<tuple<string, char, int>> temp = data;

		if(comm == "jmp") {
			get<0>(temp[i]) = "nop";
			execute(0, temp);
		} else if(comm == "nop") {
			get<0>(temp[i]) = "jmp";
			execute(0, temp);
		}
		//cout << temp << endl;
	}
}

