#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;

        if (a >= b)
        {
            cout << a - b << endl;
        }
        else
        {
            cout << b - a << endl;
        }
    }

    return 0;
}
