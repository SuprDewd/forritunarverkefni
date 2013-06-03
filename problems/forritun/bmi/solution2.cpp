#include <iostream>
using namespace std;

int main()
{
    double w, h;
    cin >> w >> h;
    cout.precision(2);
    cout.setf(ios::fixed);
    cout << w / (h * h) << endl;
    return 0;
}
