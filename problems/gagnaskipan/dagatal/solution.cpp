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
    int days, start;
    cin >> days >> start;

    cout << "Sun Mán Þri Mið Fim Fös Lau" << endl;

    for (int i = 1; i < start; i++)
    {
        if (i != 1) cout << " ";
        cout << "   ";
    }

    for (int i = 0; i < days; i++)
    {
        if ((i + start - 1) % 7 != 0) cout << " ";
        cout << setw(3) << i+1;
        if ((i + start - 1) % 7 == 6 && i != days - 1) cout << endl;
    }

    cout << endl;

    return 0;
}

