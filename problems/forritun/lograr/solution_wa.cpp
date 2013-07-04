#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    double a, b;
    cin >> a >> b;
    cout << setprecision(1) << log(b) / log(a) << endl;
    return 0;
}
