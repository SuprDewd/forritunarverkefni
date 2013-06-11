#include <iostream>
using namespace std;

int main()
{
    int b, e, abse;
    cin >> b >> e;
    double res = 1;
    abse = e;
    if (abse < 0) abse = -abse;

    for (int i = 0; i < abse; i++)
    {
        res *= b;
    }

    if (e < 0)
    {
        res = 1.0 / res;
    }

    cout << res << endl;
    return 0;
}
