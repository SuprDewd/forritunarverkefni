#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int n;
    cin >> n;

    if (n == 42)
    {
        cout << "Svarið við spurningunni um tilgang lífsins, alheimsins, og alls er 42." << endl;
    }
    else
    {
        cout << "Svarið við spurningunni um tilgang lífsins, alheimsins, og alls er ekki " << n << "." << endl;
    }

    return 0;
}
