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
#include <cassert>
#include <ciso646>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
#define INF 2147483647
typedef long long ll;
typedef pair<int, int> ii;
template <class T> int size(T x) { return x.size(); }

bool is_open(char c)
{
	return c == '{' || c == '(' || c == '[';
}

char open_to_close(char c)
{
	if (c == '{') return '}';
	if (c == '(') return ')';
	if (c == '[') return ']';
	assert(false);
}

int main()
{
	int n;
	scanf("%d\n", &n);

	for (int i = 0; i < n; i++)
	{
		string line;
		getline(cin, line);
		int len = size(line);

		stack<char> S;
		bool ok = true;

		for (int j = 0; j < len; j++)
		{
			if (is_open(line[j]))
			{
				S.push(line[j]);
			}
			else
			{
				if (S.empty())
				{
					ok = false;
					break;
				}
				else if (open_to_close(S.top()) == line[j])
				{
					S.pop();
				}
				else
				{
					ok = false;
					break;
				}
			}
		}

		ok = ok && S.empty();
		cout << (ok ? "Balanced" : "Not Balanced") << endl;
	}

	return 0;
}
