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
    string line;
    while (getline(cin, line))
    {
        bool open = false;
        int cnt = 0;
        for (int i = 0; i < size(line); i++)
        {
            if ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= 'A' && line[i] <= 'Z'))
            {
                if (!open)
                {
                    cnt++;
                    open = true;
                }
            }
            else
            {
                open = false;
            }
        }

        cout << cnt << endl;
    }

    return 0;
}

