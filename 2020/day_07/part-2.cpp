#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

int result = 0;
vector<pair<string, vector<pair<string, int>>>> rules;

bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

void recFind(string name, int count) {
	for(int i = 0; i < rules.size(); i++) {
		string intName = rules[i].first;
		vector<pair<string, int>> intRules = rules[i].second;
		if(intName == name) {
			for(int k = 0; k < intRules.size(); k++) {
				string rule = intRules[k].first;
				int quant = intRules[k].second;
				cout << rule << " " << quant << " " << count << endl;
				result += count * quant;
				recFind(rule, count * quant);
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
	for(int i = 0; i < rules.size(); i++) {
		string first = rules[i].first;
		if(first == "shiny gold") {
			cout << rules[i] << endl;
			recFind(first, 1);
		}
	}
	cout << result << endl;
}
