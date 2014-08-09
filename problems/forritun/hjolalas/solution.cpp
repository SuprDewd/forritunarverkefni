#include <iostream>
#include <ciso646>
using namespace std;

int mod(int a, int b)
{
    return (a % b + b) % b;
}

int main()
{
    string a, b;
    getline(cin, a);
    getline(cin, b);

    int cnt = 0;
    for (int i = 0; i < 4; i++)
    {
        int x = a[i] - '0',
            y = b[i] - '0';

        cnt += min(mod(x-y, 10), mod(y-x, 10));
    }

    cout << cnt << endl;

    return 0;
}
