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

void rec(int n, int from, int through, int to)
{
    if (n == 0) return;
    rec(n-1, from, to, through);
    cout << "Move from " << static_cast<char>(from + 'A') << " to " << static_cast<char>(to + 'A') << endl;
    rec(n-1, through, from, to);
}

int main()
{
    int n;
    cin >> n;
    rec(n, 0, 1, 2);
    return 0;
}

