#include <iostream>
#include <ciso646>
using namespace std;

int main()
{
    int arr[5];
    for (int i = 0; i < 5; i++)
    {
        cin >> arr[i];
    }

    bool ok = true;
    for (int i = 1; i < 5; i++)
    {
        if (arr[i-1] > arr[i])
        {
            ok = false;
        }
    }

    if (ok)
    {
        cout << "hækkandi röð" << endl;
    }
    else
    {
        cout << "ekki hækkandi röð" << endl;
    }

    return 0;
}
