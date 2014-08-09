#include <iostream>
#include <vector>
#include <ciso646>
using namespace std;

int main()
{
    vector<int> ns;
    int tmp;
    while (cin >> tmp)
    {
        ns.push_back(tmp);
    }

    bool first = true;

    int start = ns[0], end = ns[0];
    for (int i = 1; i < ns.size(); i++)
    {
        if (ns[i] == end + 1)
        {
            end = ns[i];
        }
        else
        {
            if (first) first = false;
            else cout << " ";
            if (start == end) cout << start;
            else cout << start << "-" << end;
            start = end = ns[i];
        }
    }

    if (first) first = false;
    else cout << " ";
    if (start == end) cout << start;
    else cout << start << "-" << end;

    cout << endl;

    return 0;
}
