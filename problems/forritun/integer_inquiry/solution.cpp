#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
#define INF 2147483647
typedef long long ll;
typedef pair<int, int> ii;
template <class T> int size(T x) { return x.size(); }

vector<char> add(vector<char> a, vector<char> b)
{
	vector<char> res;
	char carry = 0;
	int i = 0, il = size(a), j = 0, jl = size(b);

	while (i < il && j < jl)
	{
		char cur = carry + a[i++] + b[j++];
		res.push_back(cur % 10);
		carry = cur / 10;
	}

	while (i < il)
	{
		char cur = carry + a[i++];
		res.push_back(cur % 10);
		carry = cur / 10;
	}

	while (j < jl)
	{
		char cur = carry + b[j++];
		res.push_back(cur % 10);
		carry = cur / 10;
	}

	if (carry > 0)
	{
		res.push_back(carry);
	}

	return res;
}

int main()
{
	vector<char> sum;
	sum.push_back(0);

	string s;
	while (getline(cin, s) && s != "0")
	{
		int len = size(s);
		vector<char> cur(len);
		for (int i = 0, j = len - 1; i < len; i++, j--)
		{
			cur[i] = s[j] - '0';
		}

		sum = add(sum, cur);
	}

	int sumlen = size(sum);
	for (int i = sumlen - 1; i >= 0; i--)
	{
		printf("%c", sum[i] + '0');
	}

	printf("\n");

	return 0;
}