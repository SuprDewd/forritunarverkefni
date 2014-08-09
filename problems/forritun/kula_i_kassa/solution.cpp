#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    double x, y, z;
    cin >> x >> y >> z;
    cout << min(x, min(y, z)) / 2.0 << endl;
    return 0;
}
