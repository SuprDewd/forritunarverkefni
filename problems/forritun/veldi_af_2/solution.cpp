#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0, p = 1; i <= n; i++, p *= 2)
    {
        cout << "2^" << i << " = " << p << endl;
    }

    return 0;
}
