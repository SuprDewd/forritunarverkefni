#include<iostream>
#include <ciso646>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int a = 1,
        b = 1,
        c;

    for (int i = 1; i < n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }

    cout << a << endl;
    return 0;
}
