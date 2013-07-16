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

int main()
{
	string line;
	while (getline(cin, line))
	{
		int cnt = 0;
		for (int i = 0; i < size(line); i++)
		{
			if (line[i] >= '0' && line[i] <= '9') cnt += line[i] - '0';
			else if (line[i] == '!') printf("\n");
			else
			{
				while (cnt--) printf("%c", (line[i] == 'b' ? ' ' : line[i]));
				cnt = 0;
			}
		}

		printf("\n");
	}

	return 0;
}