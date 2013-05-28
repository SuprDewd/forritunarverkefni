#include <iostream>
using namespace std;

int vegalengd(int timi)
{
    return 10 * timi * timi / 2;
}

int main()
{
    int n;
    cin >> n;
    cout << vegalengd(n) << endl;
    return 0;
}
