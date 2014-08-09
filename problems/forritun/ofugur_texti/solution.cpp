#include <iostream>
#include <string>
#include <algorithm>
#include <ciso646>
using namespace std;

int main()
{
    bool first = true;
    string s;
    while (cin >> s)
    {
        if (first) first = false;
        else cout << " ";
        for (int i = s.size() - 1; i >= 0; i--) cout << s[i];
    }

    cout << endl;

    return 0;
}
