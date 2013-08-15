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

int parset(string x)
{
    int h = 10 * (x[0] - '0') + x[1] - '0',
        m = 10 * (x[3] - '0') + x[4] - '0',
        s = 10 * (x[6] - '0') + x[7] - '0';
    return (h * 60 + m) * 60 + s;
}

int parsen(string s)
{
    int n = 0;
    for (int i = 0; i < size(s); i++)
    {
        n = n * 10 + s[i] - '0';
    }

    return n;
}

int main()
{
    int lastt = 0, speed = 0;
    double len = 0;

    string line;
    while (getline(cin, line))
    {
        if (line.find(' ') != string::npos)
        {
            int t = parset(line.substr(0, line.find(' '))),
                n = parsen(line.substr(line.find(' ') + 1));

            len += (t - lastt) * speed / 60.0 / 60.0;
            lastt = t;
            speed = n;
        }
        else
        {
            int t = parset(line.substr(0));
            len += (t - lastt) * speed / 60.0 / 60.0;
            lastt = t;
            cout << line << " " << setprecision(2) << fixed << len << " km" << endl;
        }
    }

    return 0;
}

