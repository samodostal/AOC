#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

int result = 0;
vector<pair<string, vector<pair<string, int>>>> rules;
vector<string> allNames;

void recFind(string name) {
	if(!count(allNames.begin(), allNames.end(), name)) {
		allNames.push_back(name);
	}
	for(int i = 0; i < rules.size(); i++) {
		string first = rules[i].first;
		vector<pair<string, int>> second = rules[i].second;
		//cout << first << " " << second << endl;
		if(first != name) {
			for(int k = 0; k < second.size(); k++) {
				string fir = second[k].first;
				int sec = second[k].second;
				if(fir == name) {
					recFind(first);
				}
			}
		}
	}
}

void findAll(string name, string initialName) {
	for(int i = 0; i < rules.size(); i++) {
		string ruleName = rules[i].first;
		vector<pair<string, int>> sec = rules[i].second;
		if(ruleName == name) {
			for(int k = 0; k < sec.size(); k++) {
				string first = sec[k].first;
				int second = sec[k].second;
				if(first == "shiny gold") {
					recFind(ruleName);
				}
			}
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	string line;
	int i = 0;
	while(getline(cin, line)) {
		rules.push_back(pair<string, vector<pair<string, int>>>());
		stringstream ss(line);
		string name1, name2, bl;
		string temp;
		while(ss >> name1 >> name2 >> bl >> bl && getline(ss, temp)) {
			string wholeName = name1 + " " + name2;
			rules[i].first = wholeName;
			stringstream split(temp);
			int quant;
			string bag1, bag2, tl;
			while(split >> quant >> bag1 >> bag2 >> tl) {
				string wholeBag = bag1 + " " + bag2;
				rules[i].second.push_back(make_pair(wholeBag, quant));
			}
		}
		i++;
	}
	//cout << rules << endl;
	for(int i = 0; i < rules.size(); i++) {
		string ruleName = rules[i].first;
		findAll(ruleName, ruleName);
	}
	cout << allNames.size() << endl;
}



