#include <iostream>
using namespace std;

int main()
{
    double a, b;
    cin >> a >> b;
    cout << a / b << endl;
    cout << static_cast<int>(a) / static_cast<int>(b) << endl;
    return 0;
}

