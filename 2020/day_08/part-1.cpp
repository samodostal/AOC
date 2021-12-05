#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

vector<tuple<string, char, int>> data;
vector<int> was;
int global = 0;

void execute(int i) {
	if(count(was.begin(), was.end(), i)) {
		cout << global << endl;
		return;
	}
	was.push_back(i);
	tuple<string, char, int> current = data[i];
	string word = get<0>(current);
	char sign = get<1>(current);
	int value = get<2>(current);
	if(sign == '+') {
		if(word == "acc") {
			global += value;
			execute(i + 1);
		} else if (word == "jmp") {
			execute(i + value);
		}	else if (word == "nop") {
			execute(i + 1);
		}
	} else if (sign == '-') {
		if(word == "acc") {
			global -= value;
			execute(i + 1);
		} else if (word == "jmp") {
			execute(i - value);
		} else if (word == "nop") {
			execute(i + 1);
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
	execute(0);
}

