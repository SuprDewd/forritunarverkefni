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
    int x, y;
    cin >> x >> y;

    int count = 0, remainder = 0;
    int cury = 0;

    while (cury + y <= x)
    {
        count++;
        cury += y;
    }

    cout << y << " gengur " << count << " sinnum upp í " << x << endl;

    if (cury == x)
    {
        cout << "Enginn afgangur" << endl;
    }
    else
    {
        cout << "Afgangur er " << x - cury << endl;
    }

    return 0;
}

