#include <iostream>
using namespace std;

int main()
{
    int h, m;
    cin >> h >> m;
    bool am = true;

    if (h >= 12)
    {
        am = false;
        h -= 12;
    }

    if (h == 0)
    {
        h += 12;
    }

    cout << h << ":";

    if (m < 10)
    {
        cout << "0";
    }

    cout << m;

    if (am)
    {
        cout << " AM";
    }
    else
    {
        cout << " PM";
    }

    cout << endl;
    return 0;
}
