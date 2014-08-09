#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int cur = 5000;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 1000;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 500;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 100;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 50;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 10;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 5;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    cur = 1;
    if (n / cur > 0) cout << n / cur << " x " << cur << " kr." << endl;
    n = n % cur;
    return 0;
}
