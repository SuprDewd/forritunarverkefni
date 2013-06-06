#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n;
    cin >> n;
    double guess = n / 2.0, lastguess;

    do
    {
        lastguess = guess;
        guess = (guess + n / guess) / 2.0;
    } while (abs(guess - lastguess) >= 0.01 * lastguess);

    cout << guess << endl;
    return 0;
}
