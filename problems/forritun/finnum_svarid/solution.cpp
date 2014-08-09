#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    bool found = false;
    while (!found)
    {
        int n;
        cin >> n;
        cout << n << endl;
        if (n == 42)
        {
            found = true;
        }
    }

    return 0;
}
