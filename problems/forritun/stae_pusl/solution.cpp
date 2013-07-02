#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

map<char, int> assoc;
vector<char> chars;
bool used[10];
int mxlen = 0;
string a, b, c, tmp;

bool bt(int at)
{
    if (at == chars.size())
    {
        int an = 0, bn = 0, cn = 0;

        if ((assoc[a[0]] == 0 && a.size() != 1) || (assoc[b[0]] == 0 && b.size() != 1) || (assoc[c[0]] == 0 && c.size() != 1)) return false;

        for (int i = 0; i < a.size(); i++) an = an * 10 + assoc[a[i]];
        for (int i = 0; i < b.size(); i++) bn = bn * 10 + assoc[b[i]];
        for (int i = 0; i < c.size(); i++) cn = cn * 10 + assoc[c[i]];

        if (an + bn != cn) return false;

        for (int i = a.size(); i < mxlen + 2; i++)
        {
            cout << " ";
        }

        for (int i = 0; i < a.size(); i++)
        {
            cout << assoc[a[i]];
        }

        cout << endl;

        cout << "+";
        for (int i = b.size(); i < mxlen + 1; i++)
        {
            cout << " ";
        }

        for (int i = 0; i < b.size(); i++)
        {
            cout << assoc[b[i]];
        }

        cout << endl;

        cout << "=";

        for (int i = c.size(); i < mxlen + 1; i++)
        {
            cout << " ";
        }

        for (int i = 0; i < c.size(); i++)
        {
            cout << assoc[c[i]];
        }

        cout << endl;

        return true;
    }
    else
    {
        for (int i = 0; i < 10; i++)
        {
            if (!used[i])
            {
                assoc[chars[at]] = i;
                used[i] = true;
                if (bt(at+1)) return true;
                used[i] = false;
            }
        }
    }

    return false;
}

int main()
{
    cin >> a >> tmp >> b >> tmp >> c;

    set<char> schars;
    for (int i = 0; i < a.size(); i++) schars.insert(a[i]);
    for (int i = 0; i < b.size(); i++) schars.insert(b[i]);
    for (int i = 0; i < c.size(); i++) schars.insert(c[i]);

    mxlen = max(mxlen, static_cast<int>(a.size()));
    mxlen = max(mxlen, static_cast<int>(b.size()));
    mxlen = max(mxlen, static_cast<int>(c.size()));

    chars = vector<char>(schars.begin(), schars.end());

    memset(used, 0, 10);

    if (!bt(0))
    {
        cout << "Engin lausn" << endl;
    }

    return 0;
}
