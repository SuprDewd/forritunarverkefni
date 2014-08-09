#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int sum = 0, pos = 0, neg = 0;
    for (int i = 0; i < 10; i++)
    {
        int n;
        cin >> n;
        if (n > 0)
        {
            sum += n;
            pos++;
        }
        else
        {
            neg++;
        }
    }

    cout << sum << endl << pos << endl << neg << endl;
    return 0;
}
