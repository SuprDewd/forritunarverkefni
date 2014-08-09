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
    string line;
    getline(cin, line);

    map<char, int> cnt;
    int totcnt = 0;

    for (int i = 0; i < size(line); i++)
    {
        char cur = line[i];
        if (cur >= 'A' && cur <= 'Z') cur = cur - 'A' + 'a';
        if (cur >= 'a' && cur <= 'z')
        {
            cnt[cur]++;
            totcnt++;
        }
    }

    vector<pair<int, char> > arr;
    for (map<char, int>::const_iterator it = cnt.begin(); it != cnt.end(); ++it)
    {
        arr.push_back(pair<int, char>(-it->second, it->first));
    }

    sort(all(arr));

    for (int i = 0; i < size(arr); i++)
    {
        cout << arr[i].second << " " << -100.0 * arr[i].first / totcnt << "%" << endl;
    }

    return 0;
}

