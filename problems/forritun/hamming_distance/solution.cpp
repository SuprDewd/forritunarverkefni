#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int a, b, cnt = 0;
    cin >> a >> b;

    for (int i = 0; a || b; i++)
    {
        int acur = a & (1 << i),
            bcur = b & (1 << i);

        a -= acur;
        b -= bcur;

        if (acur != bcur)
        {
            cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}

