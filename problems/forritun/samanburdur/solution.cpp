#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    if (a < b)
    {
        cout << "minni" << endl;
    }
    else if (a > b)
    {
        cout << "stærri" << endl;
    }
    else
    {
        cout << "jafnar" << endl;
    }

    return 0;
}
