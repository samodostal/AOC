#include <algorithm>
#include <assert.h>
#include <bitset>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <time.h>
#include <utility>
#include <vector>

using namespace std;

#define FOR1(i) for (int j = 0; j < i; j++)
#define FOR2(i, j) for (int i = 0; i < j.size(); i++)
#define FOR3(i, j, k) for (int i = j; i < k; i++)
#define FOR4(i, j, k, l) for (int i = j; i < k; i += l)

#define GET_MACRO(_1, _2, _3, _4, NAME, ...) NAME
#define FOR(...) GET_MACRO(__VA_ARGS__, FOR4, FOR3, FOR2, FOR1)(__VA_ARGS__)

#define p(i) push_back(i)
#define f ifstream
#define vec vector

vector<string> split(string s, string delimiter) {
  vector<string> res;
  size_t pos = 0;
  string token;
  while ((pos = s.find(delimiter)) != string::npos) {
    token = s.substr(0, pos);
    res.push_back(token);
    s.erase(0, pos + delimiter.length());
  }
  res.push_back(s);
  return res;
}

string trim(string s) {
  s.erase(0, s.find_first_not_of(' '));
  s.erase(s.find_last_not_of(' ') + 1);
  return s;
}

bool empty(string s) {
  string t = trim(s);
  if (t.size() == 0)
    return true;
  return false;
}

template <typename T, typename F> void filter(vector<T> &vec, F lambda) {
  FOR(i, 0, vec.size()) {
    if (!lambda(vec[i])) {
      vec.erase(vec.begin() + i);
      i--;
    }
  }
}

template <typename T> std::vector<T> slice(std::vector<T> &v, int m, int n) {
  std::vector<T> vec(n - m + 1);
  std::copy(v.begin() + m, v.begin() + n + 1, vec.begin());
  return vec;
}

//includes, find
