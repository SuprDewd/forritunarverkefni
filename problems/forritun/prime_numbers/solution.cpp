#include <iostream>
using namespace std;

bool is_prime(int n)
{
    if (n <= 1)
    {
        return false;
    }

    bool ok = true;
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            ok = false;
        }
    }

    return ok;
}

int main()
{
    int a, b;
    cin >> a >> b;
    for (int n = a; n <= b; n++)
    {
        if (is_prime(n))
        {
            cout << n << endl;
        }
    }

    return 0;
}
