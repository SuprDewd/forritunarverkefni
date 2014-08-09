#include <iostream>
#include <iomanip>
#include <ciso646>
using namespace std;

int main()
{
    double w, h;
    cin >> w >> h;
    cout << setprecision(2) << fixed << w / (h * h) << endl;
    return 0;
}
