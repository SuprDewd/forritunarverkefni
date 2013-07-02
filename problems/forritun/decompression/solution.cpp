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
    string range;
    bool first = true;
    while (cin >> range)
    {
        bool found = false;
        int a = 0, b = 0;

        for (int i = 0; i < size(range); i++)
        {
            if (range[i] == '-')
            {
                found = true;
            }
            else if (found)
            {
                b = b * 10 + range[i] - '0';
            }
            else
            {
                a = a * 10 + range[i] - '0';
            }
        }

        if (found)
        {
            for (int i = a; i <= b; i++)
            {
                if (first) first = false;
                else cout << " ";
                cout << i;
            }
        }
        else
        {
            if (first) first = false;
            else cout << " ";
            cout << a;
        }
    }

    cout << endl;
    return 0;
}

