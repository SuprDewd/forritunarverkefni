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

class fraction
{
public:
    int n, d;

    fraction()
    {
        n = d = 0;
    }

    fraction(int numerator, int denominator)
    {
        n = numerator;
        d = denominator;
    }

    bool less_than(const fraction &other)
    {
        return n * other.d < other.n * d;
    }
};

int main()
{
    int n;
    cin >> n;
    fraction arr[n];
    for (int i = 0; i < n; i++)
    {
        char c;
        cin >> arr[i].n >> c >> arr[i].d;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n-1; j++)
        {
            if (arr[j+1].less_than(arr[j]))
            {
                swap(arr[j], arr[j+1]);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << arr[i].n << "/" << arr[i].d << endl;
    }

    return 0;
}

