#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int row[n];

    for (int i = 0; i < n; i++)
    {
        row[i] = 1;

        for (int j = i-1; j > 0; j--)
        {
            row[j] += row[j-1];
        }

        for (int j = 0; j <= i; j++)
        {
            if (j != 0)
            {
                cout << " ";
            }

            cout << row[j];
        }

        cout << endl;
    }

    return 0;
}
