#include <iostream>
using namespace std;

int main()
{
    string s;
    getline(cin, s);

    int n = s.size();
    int *h = new int[n];
    int mn = 0, mx = 0;

    h[0] = 0;
    for (int i = 1; i < n; i++)
    {
        h[i] = s[i] > s[i-1] ? h[i-1] - 1 : s[i] < s[i-1] ? h[i-1] + 1 : h[i-1];
        mn = min(mn, h[i]);
        mx = max(mx, h[i]);
    }

    for (int i = mn; i <= mx; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (h[j] == i)
            {
                cout << s[j];
            }
            else
            {
                cout << " ";
            }
        }

        cout << endl;
    }

    return 0;
}
