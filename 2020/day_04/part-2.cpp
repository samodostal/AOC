#include <bits/stdc++.h>

#include "../libs/prettyprint.hpp"
		
using namespace std;

vector<string> raw;
vector<vector<pair<string, string>>> data;
bool firstInit = false;
int fin = 0;

bool isParam(string line)
{
    char* p;
    strtol(line.c_str(), &p, 10);
    return *p == 0;
}

void loadFile() {
	freopen("input.txt", "r", stdin);
	string line;
	int i = 0;
	raw.push_back("");

	while(getline(cin, line)) {
		if(line.empty()) {
			raw.push_back("");
			i++;
			continue;
		} else {
			raw[i] += " ";
		}
		raw[i] += line;
	}
	for(int i = 0; i < raw.size(); i++) {
		data.push_back(vector<pair<string, string>>());
		stringstream ss(raw[i]);
		char num1, num2, num3, dot;
		string value;
		while(ss >> num1 >> num2 >> num3 >> dot >> value) {
			pair <string, string> p;
			string key = "xxx";
			key.at(0) = num1;
			key.at(1) = num2;
			key.at(2) = num3;

			p.first = key;
			p.second = value;

			data[i].push_back(p);
		}
	}
	//remove cid element
	for(int i = 0; i < data.size(); i++) {
		vector<pair<string, string>> &current = data[i];
		for(int k = 0; k < current.size(); k++) {
			pair<string, string> pa = current[k];
			string key = pa.first;
			if(key == "cid") {
				current.erase(current.begin() + k);
			}
		}
	}
	int valid = 0;
	for(int i = 0; i < data.size(); i++) {
		vector<pair<string, string>> &current = data[i];
		if(current.size() != 7) {
			continue;
		}

		int innerSucces = 0;
		// has to be 7

		for(int k = 0; k < current.size(); k++) {
			pair<string, string> &pa = current[k];
			string key = pa.first;
			string second = pa.second;
			if(key == "byr") {
					stringstream convert(second);
					int sec;
					convert >> sec;
					if(1920 <= sec && 2002 >= sec) {
						innerSucces++;
					}
			}
			if(key == "iyr") {
					stringstream convert(second);
					int sec;
					convert >> sec;
					if(2010 <= sec && 2020 >= sec) {
						innerSucces++;
					}
			}
			if(key == "eyr") {
					stringstream convert(second);
					int sec;
					convert >> sec;
					if(2020 <= sec && 2030 >= sec) {
						innerSucces++;
					}
			}
			if(key == "hgt") {
				stringstream convert(second);
				int height;
				string units;
				convert >> height >> units;
				if(units == "cm") {
					if(150 <= height && 193 >= height) {
						innerSucces++;
					}
				} else if (units == "in") {
					if(59 <= height && 76 >= height) {
						innerSucces++;
					}
				}
			}
			char set[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
			if(key == "hcl") {
				//cout << second << endl;
				stringstream convert(second);
				char hash;
				string rest;
				convert >> hash >> rest;
				int ex = 0;
				for(int f = 0; f < rest.length(); f++) {
					char s = rest[f];
					bool exists = find(begin(set), end(set), s) != end(set);
					if(exists) {
						ex++;
					}
				}
				if(ex == 6 && hash == '#') {
					innerSucces++;
				}
			}
			if(key == "ecl") {
				if(second == "amb" || second ==  "blu" || second == "brn" || second == "gry" || second == "grn" || second == "hzl" || second == "oth") {
					innerSucces++;
				}
			}
			if(key == "pid") {
				bool num = isParam(second);
				if(num && second.length() == 9) {
					innerSucces++;
				}
			}
		}
		if(innerSucces == 7) {
			fin++;
		}
	}
}

int main() {
	loadFile();
	cout << fin << endl;
}


