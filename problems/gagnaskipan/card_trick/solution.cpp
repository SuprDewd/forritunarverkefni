#include <iostream>
#include <list>
#include <ciso646>
using namespace std;

int main()
{
    int ts;
    cin >> ts;
    for (int t = 0; t < ts; t++)
    {
        int n;
        cin >> n;
        list<int> l;
        for (int i = n; i >= 1; --i)
        {
            l.push_front(i);
            for (int j = 0; j < i; j++)
            {
                int b = l.back(); l.pop_back();
                l.push_front(b);
            }
        }

        while (!l.empty())
        {
            cout << l.front();
            l.pop_front();
            if (!l.empty()) cout << " ";
        }

        cout << endl;
    }

    return 0;
}
