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
const int INF = 2147483647;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> int size(T x) { return x.size(); }

// assert or gtfo

int main()
{
	int ts;
	scanf("%d\n", &ts);

	for (int t = 0; t < ts; t++)
	{
		string line;
		getline(cin, line);

		bool fun = true;
		for (int i = 0, cnt = size(line); fun && i < cnt; i++)
		{
			if (line[i] == ' ')
			{
				fun = tolower(line[i-1]) == tolower(line[i+1]);
			}
		}

		if (fun)
		{
			printf("Fun\n");
		}
		else
		{
			printf("Boring\n");
		}
	}

	return 0;
}
