#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    cout << static_cast<double>(a) / b << endl;
    cout << a / b << endl;
    return 0;
}

