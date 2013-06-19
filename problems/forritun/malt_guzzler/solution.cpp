#include <iostream>
using namespace std;

int main()
{
    int e, f, c;
    cin >> e >> f >> c;
    e += f;
    int cnt = 0;
    while (e >= c)
    {
        f = e / c;
        e %= c;
        e += f;
        cnt += f;
    }

    cout << cnt << endl;

    return 0;
}
